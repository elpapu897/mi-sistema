#!/usr/bin/env bash
# =============================================================================
#  RESTAURAR  —  Linux, WSL o macOS
#
#  Devuelve cada carpeta del repo a su lugar en el home, leyendo scripts/MAPA.tsv.
#  Nunca borra nada sin avisar: si el destino ya existe, lo renombra a
#  <nombre>.previo-<fecha> antes de escribir.
#
#  Uso:
#    bash scripts/restaurar.sh --dry-run      ver qué haría, sin tocar nada
#    bash scripts/restaurar.sh                restaurar todo
#    bash scripts/restaurar.sh --solo ic,pr   restaurar solo algunas categorías
#
#  Categorías:  ic=irremplazable  pr=proyectos  ng=negocio  md=media  hi=historial
# =============================================================================
set -uo pipefail

REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
MAPA="$REPO/scripts/MAPA.tsv"
SELLO="$(date +%Y%m%d-%H%M%S)"
DRY=0
SOLO="ic,pr,ng,md,hi"

while [ $# -gt 0 ]; do
  case "$1" in
    --dry-run) DRY=1; shift ;;
    --solo)    SOLO="$2"; shift 2 ;;
    -h|--help) sed -n '2,20p' "$0" | sed 's/^# \{0,1\}//'; exit 0 ;;
    *) echo "Opción desconocida: $1"; exit 1 ;;
  esac
done

[ -f "$MAPA" ] || { echo "Falta $MAPA. ¿Estás corriendo esto desde el repo?"; exit 1; }

nombre_cat() { case "$1" in
  ic) echo "IRREMPLAZABLE" ;; pr) echo "PROYECTOS" ;; ng) echo "NEGOCIO" ;;
  md) echo "MEDIA" ;; hi) echo "HISTORIAL" ;; *) echo "$1" ;; esac; }

echo
echo "  ┌────────────────────────────────────────────────────────────┐"
echo "  │  RESTAURACIÓN DEL SISTEMA                                  │"
echo "  └────────────────────────────────────────────────────────────┘"
echo "  Origen : $REPO"
echo "  Destino: $HOME"
[ $DRY -eq 1 ] && echo "  MODO SIMULACIÓN — no se escribe nada"
echo

# --- ¿Los archivos de LFS bajaron de verdad? ------------------------------
if [ -d "$REPO/05-media" ]; then
  MUESTRA="$(find "$REPO/05-media" -name '*.mp4' -o -name '*.mov' 2>/dev/null | head -1)"
  if [ -n "$MUESTRA" ] && [ "$(stat -c%s "$MUESTRA" 2>/dev/null || echo 0)" -lt 1000 ]; then
    echo "  AVISO: los videos son punteros de LFS, no archivos reales."
    echo "  Corré esto antes de seguir:  git lfs install && git lfs pull"
    echo
  fi
fi

TOTAL=0; SALTADOS=0
declare -a RESTAURADOS=()
while IFS=$'\t' read -r cat origen destino desc; do
  [ -z "${cat:-}" ] && continue
  case ",$SOLO," in *",$cat,"*) ;; *) continue ;; esac

  SRC="$REPO/$origen"
  DST="$HOME/$destino"

  if [ ! -e "$SRC" ]; then
    printf '  [ ] %-34s no está en el repo\n' "$origen"
    SALTADOS=$((SALTADOS+1)); continue
  fi

  PESO="$(du -sh "$SRC" 2>/dev/null | cut -f1)"
  printf '  [%s] %-30s -> ~/%-28s %6s\n' "$(nombre_cat "$cat" | cut -c1-2)" "$origen" "$destino" "$PESO"
  printf '       %s\n' "$desc"

  if [ $DRY -eq 0 ]; then
    # Protección: si este destino está DENTRO de algo que ya restauramos en
    # esta corrida, no lo apartamos (lo apartaríamos justo después de haberlo
    # creado). En ese caso fusionamos.
    ANIDADO=0
    for YA in "${RESTAURADOS[@]:-}"; do
      case "$destino/" in "$YA"/*) ANIDADO=1; break ;; esac
    done
    if [ -e "$DST" ] && [ ! -L "$DST" ] && [ $ANIDADO -eq 0 ]; then
      mv "$DST" "$DST.previo-$SELLO"
      printf '       (lo que había quedó en ~/%s.previo-%s)\n' "$destino" "$SELLO"
    elif [ $ANIDADO -eq 1 ]; then
      printf '       (se fusiona dentro de lo ya restaurado)\n'
    fi
    mkdir -p "$(dirname "$DST")"
    cp -a "$SRC" "$DST" 2>/dev/null || rsync -a "$SRC/" "$DST/"
  fi
  RESTAURADOS+=("$destino")
  TOTAL=$((TOTAL+1))
done < "$MAPA"

echo
echo "  Restauradas: $TOTAL   Omitidas: $SALTADOS"
echo

if [ $DRY -eq 1 ]; then
  echo "  Era una simulación. Para hacerlo de verdad, corré sin --dry-run."
  echo
  exit 0
fi

# --- Pasos que dependen de que las carpetas ya estén en su lugar ----------
echo "  ── Siguientes pasos ─────────────────────────────────────────"
echo
echo "  1) Symlinks (las 1067 skills y los enlaces del vault):"
echo "         bash scripts/rehacer-symlinks.sh"
echo
echo "  2) Repos de terceros:"
echo "         bash scripts/reclonar-terceros.sh"
echo
echo "  3) Credenciales (te va a pedir la passphrase):"
echo "         bash scripts/descifrar-secretos.sh"
echo
echo "  4) Dependencias, en cada proyecto que vayas a usar:"
echo "         cd ~/g && npm install"
echo
echo "  Lo que había antes quedó con sufijo .previo-$SELLO."
echo "  Cuando confirmes que todo anda, borralos:"
echo "         rm -rf ~/*.previo-$SELLO"
echo
