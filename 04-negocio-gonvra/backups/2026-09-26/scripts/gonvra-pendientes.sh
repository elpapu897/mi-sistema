#!/usr/bin/env bash
# GONVRA — Avisa si hay contenido esperando aprobacion, con LINKS para
# aprobar o descartar desde el celular con un toque.
# Silencio si no hay nada.

set -u
PEND="$HOME/GONVRA-PUBLICAR/1-PENDIENTE"
SECRETS="$HOME/.hermes/.gonvra-secrets.env"
[ -d "$PEND" ] || exit 0

# shellcheck disable=SC1090
set -a; . "$SECRETS" 2>/dev/null; set +a
URL=$(cat "$HOME/.hermes/gonvra-url-publica.txt" 2>/dev/null)
SEC="${GONVRA_APROBAR_SECRETO:-}"

shopt -s nullglob nocaseglob
IMGS=("$PEND"/*.png "$PEND"/*.jpg "$PEND"/*.jpeg "$PEND"/*.mp4)
CARPETAS=()
for d in "$PEND"/*/; do [ -d "$d" ] && CARPETAS+=("$d"); done
shopt -u nocaseglob
[ ${#IMGS[@]} -eq 0 ] && [ ${#CARPETAS[@]} -eq 0 ] && exit 0

# Arma los dos links de una pieza (o avisa si el tunel no esta)
links() {
  local nombre="$1"
  if [ -z "$URL" ] || [ -z "$SEC" ]; then
    echo "   (sin link: movelo a mano a 2-APROBADO)"
    return
  fi
  local enc
  enc=$(python3 -c "import urllib.parse,sys;print(urllib.parse.quote(sys.argv[1]))" "$nombre")
  echo "   PUBLICAR:  ${URL}/webhook/gonvra-aprobar?pieza=${enc}&accion=aprobar&t=${SEC}"
  echo "   DESCARTAR: ${URL}/webhook/gonvra-aprobar?pieza=${enc}&accion=descartar&t=${SEC}"
}

TOTAL=$(( ${#IMGS[@]} + ${#CARPETAS[@]} ))
echo "HAY $TOTAL PIEZA(S) ESPERANDO TU OK"
echo ""

for C in "${CARPETAS[@]}"; do
  N=$(basename "$C")
  CANT=$(ls "$C" 2>/dev/null | grep -icE "\.(png|jpg|jpeg)$")
  echo "· $N  (CARRUSEL de $CANT fotos)"
  [ -f "$C/texto.txt" ] && echo "  Texto: $(head -c 140 "$C/texto.txt")"
  links "$N"
  echo ""
done

for IMG in "${IMGS[@]}"; do
  NOMBRE=$(basename "$IMG")
  SINEXT="${NOMBRE%.*}"
  TXT="$PEND/$SINEXT.txt"
  case "$NOMBRE" in
    *.mp4|*.MP4) echo "· $NOMBRE  (REEL)";;
    *)           echo "· $NOMBRE  (foto)";;
  esac
  if [ -f "$TXT" ]; then
    echo "  Texto: $(head -c 160 "$TXT")"
  else
    echo "  (sin texto - se publicaria sin caption)"
  fi
  links "$NOMBRE"
  echo ""
done

echo "Tocá PUBLICAR y sale en @gonvra1 al instante."
echo "Nada se publica si no tocás vos."
exit 0
