---
tool: Codex
session_id: 01a00334-e7fd-7463-8668-88c9e38e4778
fecha: 2026-08-15 02:16
titulo: "homematiigonzzDescargasandrej karpathy skills main"
tags: [chat, agente, codex]
---

# 💬 homematiigonzzDescargasandrej karpathy skills main
> **Codex** · 2026-08-15 02:16 · `01a00334-e7fd-7463-8668-88c9e38e4778`

---

### 🧑 Vos  <small>2026-08-15 02:16</small>

@"/home/matiigonzz/Descargas/andrej-karpathy-skills-main.zip"
instala esta skill en todos los modelos de ia q tengo

### 🤖 Codex  <small>2026-08-15 02:16</small>

I'll take a look at the zip first.

### 🤖 Codex  <small>2026-08-15 02:16</small>

[external_agent_tool_call: Bash]
command: cd /home/matiigonzz/Descargas && unzip -l andrej-karpathy-skills-main.zip | head -50
[/external_agent_tool_call]

### 🤖 Codex  <small>2026-08-15 02:16</small>

[external_agent_tool_call: Bash]
command: cat /home/matiigonzz/Claude/scripts/sync-skills.sh 2>/dev/null; echo "---"; ls /home/matiigonzz/.agents/skills | head -20; echo "..."; ls /home/matiigonzz/.agents/skills | wc -l
[/external_agent_tool_call]

### 🤖 Codex  <small>2026-08-15 02:16</small>

[external_agent_tool_result]
Archive:  andrej-karpathy-skills-main.zip
2c606141936f1eeef17fa3043a72095b4765b9c2
  Length      Date    Time    Name
---------  ---------- -----   ----
        0  04-20-2026 07:05   andrej-karpathy-skills-main/
        0  04-20-2026 07:05   andrej-karpathy-skills-main/.claude-plugin/
      758  04-20-2026 07:05   andrej-karpathy-skills-main/.claude-plugin/marketplace.json
      390  04-20-2026 07:05   andrej-karpathy-skills-main/.claude-plugin/plugin.json
        0  04-20-2026 07:05   andrej-karpathy-skills-main/.cursor/
        0  04-20-2026 07:05   andrej-karpathy-skills-main/.cursor/rules/
     2638  04-20-2026 07:05   andrej-karpathy-skills-main/.cursor/rules/karpathy-guidelines.mdc
     2357  04-20-2026 07:05   andrej-karpathy-skills-main/CLAUDE.md
     1955  04-20-2026 07:05   andrej-karpathy-skills-main/CURSOR.md
    14838  04-20-2026 07:05   andrej-karpathy-skills-main/EXAMPLES.md
     6198  04-20-2026 07:05   andrej-karpathy-skills-main/README.md
     6042  04-20-2026 07:05   andrej-karpathy-skills-main/README.zh.md
        0  04-20-2026 07:05   andrej-karpathy-skills-main/skills/
        0  04-20-2026 07:05   andrej-karpathy-skills-main/skills/karpathy-guidelines/
     2518  04-20-2026 07:05   andrej-karpathy-skills-main/skills/karpathy-guidelines/SKILL.md
---------                     -------
    37694                     15 files
Shell cwd was reset to /home/matiigonzz/Claude
[/external_agent_tool_result]

### 🤖 Codex  <small>2026-08-15 02:16</small>

[external_agent_tool_result]
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
links=...
[/external_agent_tool_result]

### 🤖 Codex  <small>2026-08-15 02:16</small>

Ya tengo el flujo armado (skills canónicas + `sync-skills.sh`). Extraigo e instalo.

### 🤖 Codex  <small>2026-08-15 02:16</small>

[external_agent_tool_call: Bash]
command: ls -d /home/matiigonzz/.agents/skills/karpathy* 2>/dev/null || echo "no existe"; cd /tmp && rm -rf kskill && mkdir kskill && unzip -q /home/matiigonzz/Descargas/andrej-karpathy-skills-main.zip -d kskill && cat kskill/andrej-karpathy-skills-main/skills/karpathy-guidelines/SKILL.md
[/external_agent_tool_call]

### 🤖 Codex  <small>2026-08-15 02:16</small>

[external_agent_tool_result]
no existe
---
name: karpathy-guidelines
description: Behavioral guidelines to reduce common LLM coding mistakes. Use when writing, reviewing, or refactoring code to avoid overcomplication, make surgical changes, surface assumptions, and define verifiable success criteria.
license: MIT
---

# Karpathy Guidelines

Behavioral guidelines to reduce common LLM coding mistakes, derived from [Andrej Karpathy's observations](https://x.com/karpathy/status/2015883857489522876) on LLM coding pitfalls.

**Tradeoff:** These guidelines bias toward caution over speed. For trivial tasks, use judgment.

## 1. Think Before Coding

**Don't assume. Don't hide confusion. Surface tradeoffs.**

Before implementing:
- State your assumptions explicitly. If uncertain, ask.
- If multiple interpretations exist, present them - don't pick silently.
- If a simpler approach exists, say so. Push back when warranted.
- If something is unclear, stop. Name what's confusing. Ask.

## 2. Simplicity First

**Minimum code that solves the problem. Nothing speculative.**

- No features beyond what was asked.
- No abstractions for single-use code.
- No "flexibility" or "configurability" that wasn't requested.
- No error handling for impossible scenarios.
- If you write 200 lines and it could be 50, rewrite it.

Ask yourself: "Would a senior engineer say this is overcomplicated?" If yes, simplify.

## 3. Surgical Changes

**Touch only what you must. Clean up only your own mess.**

When editing existing code:
- Don't "improve" adjacent code, comments, or formatting.
- Don't refactor things that aren't broken.
- Match existing style, even if you'd do it differently.
- If you notice unrelated dead code, mention it - don't delete it.

When your changes create orphans:
- Remove imports/variables/functions that YOUR changes made unused.
- Don't remove pre-existing dead code unless asked.

The test: Every changed line should trace directly to the user's request.

## 4. Goal-Driven Execution

**Define success criteria. Loop until verified.**

Transform tasks into verifiable goals:
- "Add validation" → "Write tests for invalid inputs, then make them pass"
- "Fix the bug" → "Write a test that reproduces it, then make it pass"
- "Refactor X" → "Ensure tests pass before and after"

For multi-step tasks, state a brief plan:
```
1. [Step] → verify: [check]
2. [Step] → verify: [check]
3. [Step] → verify: [check]
```

Strong success criteria let you loop independently. Weak criteria ("make it work") require constant clarification.
Shell cwd was reset to /home/matiigonzz/Claude
[/external_agent_tool_result]

### 🤖 Codex  <small>2026-08-15 02:16</small>

[external_agent_tool_call: Bash]
command: cp -r /tmp/kskill/andrej-karpathy-skills-main/skills/karpathy-guidelines /home/matiigonzz/.agents/skills/ && ls /home/matiigonzz/.agents/skills/karpathy-guidelines
[/external_agent_tool_call]

### 🤖 Codex  <small>2026-08-15 02:16</small>

[external_agent_tool_result]
SKILL.md
[/external_agent_tool_result]

### 🤖 Codex  <small>2026-08-15 02:16</small>

[external_agent_tool_call: Bash]
command: bash /home/matiigonzz/Claude/scripts/sync-skills.sh 2>&1 | tail -20
[/external_agent_tool_call]

### 🤖 Codex  <small>2026-08-15 02:16</small>

[external_agent_tool_result]
==> Importando skills empaquetadas en plugins
    nuevas: 0   actualizadas: 0   ya existían: 39
==> Detectando carpetas de agentes
    56 carpetas destino
==> Enlazando 258 skills en cada agente
    14214 enlaces   (177 omitidas en Codex por venir ya de sus plugins)
==> Limpiando enlaces rotos
    0 rotos eliminados

Listo. Canónicas: 258 skills
[/external_agent_tool_result]

### 🤖 Codex  <small>2026-08-15 02:16</small>

[external_agent_tool_call: Bash]
command: for d in $(find /home/matiigonzz -maxdepth 2 -type d -name skills 2>/dev/null | grep -v '.agents/skills'); do [ -e "$d/karpathy-guidelines" ] && echo "OK  $d"; done
[/external_agent_tool_call]

### 🤖 Codex  <small>2026-08-15 02:16</small>

[external_agent_tool_result]
OK  /home/matiigonzz/.claude/skills
OK  /home/matiigonzz/.aider-desk/skills
OK  /home/matiigonzz/.autohand/skills
OK  /home/matiigonzz/.augment/skills
OK  /home/matiigonzz/.bob/skills
OK  /home/matiigonzz/.openclaw/skills
OK  /home/matiigonzz/.codeartsdoer/skills
OK  /home/matiigonzz/.codebuddy/skills
OK  /home/matiigonzz/.codex/skills
OK  /home/matiigonzz/.codemaker/skills
OK  /home/matiigonzz/.codestudio/skills
OK  /home/matiigonzz/.commandcode/skills
OK  /home/matiigonzz/.continue/skills
OK  /home/matiigonzz/.factory/skills
OK  /home/matiigonzz/.forge/skills
OK  /home/matiigonzz/.grok/skills
OK  /home/matiigonzz/.lingma/skills
OK  /home/matiigonzz/.mcpjam/skills
OK  /home/matiigonzz/.minimax/skills
OK  /home/matiigonzz/.vibe/skills
OK  /home/matiigonzz/.moxby/skills
OK  /home/matiigonzz/.mux/skills
OK  /home/matiigonzz/.openhands/skills
OK  /home/matiigonzz/.ona/skills
OK  /home/matiigonzz/.qoder/skills
OK  /home/matiigonzz/.qoder-cn/skills
OK  /home/matiigonzz/.qwen/skills
OK  /home/matiigonzz/.reasonix/skills
OK  /home/matiigonzz/.rovodev/skills
OK  /home/matiigonzz/.roo/skills
OK  /home/matiigonzz/.hermes/skills
OK  /home/matiigonzz/.inferencesh/skills
OK  /home/matiigonzz/.jazz/skills
OK  /home/matiigonzz/.junie/skills
OK  /home/matiigonzz/.iflow/skills
OK  /home/matiigonzz/.kilocode/skills
OK  /home/matiigonzz/.kiro/skills
OK  /home/matiigonzz/.kode/skills
OK  /home/matiigonzz/.terramind/skills
OK  /home/matiigonzz/.tinycloud/skills
OK  /home/matiigonzz/.trae/skills
OK  /home/matiigonzz/.trae-cn/skills
OK  /home/matiigonzz/.zcode/skills
OK  /home/matiigonzz/.zencoder/skills
OK  /home/matiigonzz/.neovate/skills
OK  /home/matiigonzz/.pochi/skills
OK  /home/matiigonzz/.adal/skills
[/external_agent_tool_result]

### 🤖 Codex  <small>2026-08-15 02:16</small>

[external_agent_tool_call: Bash]
command: ls -d /home/matiigonzz/.cursor 2>/dev/null && ls /home/matiigonzz/.cursor
[/external_agent_tool_call]

### 🤖 Codex  <small>2026-08-15 02:16</small>

[external_agent_tool_result: error]
Exit code 2
[/external_agent_tool_result]

### 🤖 Codex  <small>2026-08-15 02:16</small>

Listo. **`karpathy-guidelines` instalada en los 47 agentes** que tenés configurados.

Qué hice:
1. Extraje el zip y copié `skills/karpathy-guidelines/` a tu carpeta canónica `~/.agents/skills/` (ahora 258 skills).
2. Corrí [sync-skills.sh](Claude/scripts/sync-skills.sh), que creó los symlinks en cada agente (Claude Code, Codex, Cursor-likes, Qwen, Grok, Trae, Roo, Kilocode, OpenHands, etc.).
3. Verifiqué que el enlace existe en todos: 47 OK, 0 rotos.

Notas:
- No instalé la regla de Cursor (`.cursor/rules/karpathy-guidelines.mdc`) porque no tenés `~/.cursor` — si instalás Cursor después, avisame y la agrego.
- El resto del repo (README, EXAMPLES.md, CLAUDE.md) es documentación; la skill en sí es solo el `SKILL.md`, que es lo que cargan los agentes.

La skill se auto-activa al escribir/revisar/refactorizar código: fuerza pensar antes de codear, mínimo código, cambios quirúrgicos y criterios de éxito verificables.
