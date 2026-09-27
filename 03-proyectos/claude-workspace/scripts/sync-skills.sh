#!/usr/bin/env bash
# sync-skills.sh — Deja TODAS las skills disponibles en TODOS los agentes.
#
# Modelo:
#   ~/.agents/skills/<nombre>/   = fuente canónica (copias reales)
#   ~/.<agente>/skills/<nombre>  = symlink relativo a la canónica
#
# Las skills que vienen dentro de plugins (marketplace de Codex/Claude) se
# COPIAN, no se enlazan, porque su ruta incluye la versión del plugin y los
# symlinks se romperían en cada actualización. Volvé a correr este script
# después de actualizar plugins para refrescarlas.
#
# IMPORTANTE — anti-duplicados: Codex ya carga por su cuenta las skills de los
# plugins que tiene habilitados (marketplaces claude-cowork y
# local-desktop-app-uploads). Si además se las enlazáramos en ~/.codex/skills
# las vería DOS veces y desperdiciaría contexto. Por eso a Codex solo se le
# enlazan las skills que NO provienen de esos plugins.
#
# Uso:  ./sync-skills.sh [--dry-run]

set -uo pipefail

CANON="$HOME/.agents/skills"
DRY=0
[ "${1:-}" = "--dry-run" ] && DRY=1

say() { printf '%s\n' "$*"; }
run() { [ $DRY -eq 1 ] && say "  [dry] $*" || "$@"; }

mkdir -p "$CANON"

# ---------------------------------------------------------------- 1. fuentes
# Carpetas donde viven plugins que empaquetan skills.
PLUGIN_ROOTS=(
    "$HOME/.codex/plugins/cache/claude-cowork"
    "$HOME/.claude/plugins/marketplaces/local-desktop-app-uploads"
)

# Marketplaces que Codex ya carga solo (para no duplicarle skills).
CODEX_OWN_SOURCES='claude-cowork|local-desktop-app-uploads'

# Lee el campo `name:` del frontmatter; si no hay, usa el nombre de la carpeta.
skill_name() {
    local md="$1" n
    n=$(awk '
        /^---[[:space:]]*$/ { c++; next }
        c==1 && /^name:[[:space:]]*/ {
            sub(/^name:[[:space:]]*/, ""); gsub(/^["'\'']|["'\'']$/, "")
            print; exit
        }
        c==2 { exit }
    ' "$md")
    [ -n "$n" ] || n=$(basename "$(dirname "$md")")
    printf '%s' "$n"
}

added=0; skipped=0; refreshed=0

say "==> Importando skills empaquetadas en plugins"
for root in "${PLUGIN_ROOTS[@]}"; do
    [ -d "$root" ] || continue
    while IFS= read -r md; do
        dir=$(dirname "$md")
        # Ignora copias internas de asset/build de los plugins.
        case "$dir" in */cli/assets/*|*/node_modules/*|*/.git/*) continue ;; esac

        name=$(skill_name "$md")
        [ -n "$name" ] || continue
        dest="$CANON/$name"

        if [ -e "$dest" ]; then
            # Si ya la trajimos nosotros desde un plugin, la refrescamos.
            if [ -f "$dest/.from-plugin" ] && [ "$(cat "$dest/.from-plugin")" = "$dir" ]; then
                if ! diff -rq "$dir" "$dest" --exclude=.from-plugin >/dev/null 2>&1; then
                    run rm -rf "$dest"
                    run cp -r "$dir" "$dest"
                    run sh -c "printf '%s' '$dir' > '$dest/.from-plugin'"
                    refreshed=$((refreshed+1))
                fi
            else
                skipped=$((skipped+1))   # ya existe de otra fuente: no la pisamos
            fi
            continue
        fi

        run cp -r "$dir" "$dest"
        run sh -c "printf '%s' '$dir' > '$dest/.from-plugin'"
        added=$((added+1))
    done < <(find "$root" -name SKILL.md -type f 2>/dev/null)
done
say "    nuevas: $added   actualizadas: $refreshed   ya existían: $skipped"

# ------------------------------------------------- 2. destinos (agentes)
say "==> Detectando carpetas de agentes"
mapfile -t AGENT_DIRS < <(
    {
        find "$HOME" -maxdepth 2 -type d -name skills 2>/dev/null
        find "$HOME/.config" "$HOME/.astrbot" "$HOME/.tabnine" "$HOME/.codeium" \
             "$HOME/.pi" "$HOME/.snowflake" -maxdepth 3 -type d -name skills 2>/dev/null
        echo "$HOME/.codex/skills"
    } | sort -u | grep -v "^$CANON$"
)
say "    ${#AGENT_DIRS[@]} carpetas destino"

# ------------------------------------------------- 3. enlazar todo en todos
say "==> Enlazando $(find "$CANON" -maxdepth 1 -mindepth 1 -type d | wc -l) skills en cada agente"
links=0; dedup=0
for d in "${AGENT_DIRS[@]}"; do
    [ -d "$d" ] || continue
    is_codex=0
    [ "$d" = "$HOME/.codex/skills" ] && is_codex=1

    rel=$(realpath --relative-to="$d" "$CANON" 2>/dev/null) || continue
    for s in "$CANON"/*/; do
        n=$(basename "$s")
        [ -f "$s/SKILL.md" ] || continue
        tgt="$d/$n"

        # Codex: saltear las skills que ya le llegan por sus propios plugins.
        if [ $is_codex -eq 1 ] && [ -f "$s/.from-plugin" ] &&
           grep -Eq "$CODEX_OWN_SOURCES" "$s/.from-plugin"; then
            [ -L "$tgt" ] && { run rm -f "$tgt"; }
            dedup=$((dedup+1))
            continue
        fi

        # No tocar skills reales (no-symlink) que el agente tenga propias.
        if [ -e "$tgt" ] && [ ! -L "$tgt" ]; then continue; fi
        run ln -sfn "$rel/$n" "$tgt"
        links=$((links+1))
    done
done
say "    $links enlaces   ($dedup omitidas en Codex por venir ya de sus plugins)"

# ------------------------------------------------- 4. limpieza de rotos
say "==> Limpiando enlaces rotos"
broken=0
for d in "${AGENT_DIRS[@]}"; do
    [ -d "$d" ] || continue
    while IFS= read -r l; do
        run rm -f "$l"; broken=$((broken+1))
    done < <(find "$d" -maxdepth 1 -xtype l 2>/dev/null)
done
say "    $broken rotos eliminados"

say
say "Listo. Canónicas: $(find "$CANON" -maxdepth 1 -mindepth 1 -type d | wc -l) skills"
