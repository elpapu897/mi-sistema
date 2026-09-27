#!/usr/bin/env bash
# =============================================================================
#  REHACER SYMLINKS
#
#  Tu sistema usaba 3154 enlaces simbólicos. Los importantes: las 1067 skills
#  de ~/.claude/skills que apuntan a ~/.agents/skills (para no duplicar 60 MB),
#  y 13 enlaces del vault de Obsidian hacia carpetas de proyectos.
#
#  Git guarda symlinks, pero Windows los rompe al hacer checkout salvo que
#  tengas core.symlinks=true Y Modo Desarrollador activado. Por eso este script
#  los reconstruye desde el manifiesto, sin depender de lo que git haya hecho.
#
#  Uso:  bash scripts/rehacer-symlinks.sh
# =============================================================================
set -uo pipefail

REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
MAPA="$REPO/scripts/SYMLINKS.tsv"

[ -f "$MAPA" ] || { echo "Falta $MAPA"; exit 1; }

echo
echo "  RECONSTRUCCIÓN DE SYMLINKS"
echo "  =========================="
echo

# Traduce la ruta dentro del repo a su destino real en el home
destino_real() {
  local p="$1"
  case "$p" in
    01-segundo-cerebro/*)      echo "$HOME/OBSIDIAN/${p#01-segundo-cerebro/}" ;;
    02-agentes/claude/*)       echo "$HOME/.claude/${p#02-agentes/claude/}" ;;
    02-agentes/agents-skills/*) echo "$HOME/.agents/${p#02-agentes/agents-skills/}" ;;
    02-agentes/codex/*)        echo "$HOME/.codex/${p#02-agentes/codex/}" ;;
    02-agentes/gemini/*)       echo "$HOME/.gemini/${p#02-agentes/gemini/}" ;;
    02-agentes/hermes/*)       echo "$HOME/.hermes/${p#02-agentes/hermes/}" ;;
    02-agentes/kimi-code/*)    echo "$HOME/.kimi-code/${p#02-agentes/kimi-code/}" ;;
    06-dotfiles/config/*)      echo "$HOME/.config/${p#06-dotfiles/config/}" ;;
    *) echo "" ;;
  esac
}

HECHOS=0; SALTADOS=0; ROTOS=0
while IFS=$'\t' read -r ruta target; do
  [ -z "${ruta:-}" ] && continue

  enlace="$(destino_real "$ruta")"
  [ -z "$enlace" ] && { SALTADOS=$((SALTADOS+1)); continue; }

  # $HOME literal del manifiesto -> el home de esta máquina
  target="${target//\$HOME/$HOME}"

  mkdir -p "$(dirname "$enlace")" 2>/dev/null
  rm -rf "$enlace" 2>/dev/null
  ln -s "$target" "$enlace" 2>/dev/null && HECHOS=$((HECHOS+1)) || SALTADOS=$((SALTADOS+1))

  # ¿Quedó apuntando a algo que existe?
  [ -e "$enlace" ] || ROTOS=$((ROTOS+1))
done < "$MAPA"

echo "  Creados: $HECHOS"
echo "  Omitidos (fuera del mapa): $SALTADOS"
echo "  Apuntan a algo que todavía no existe: $ROTOS"
echo
if [ "$ROTOS" -gt 0 ]; then
  echo "  Los enlaces rotos se arreglan solos cuando restaures la carpeta que les"
  echo "  falta. Volvé a correr este script al final de todo y debería dar 0."
fi
echo
