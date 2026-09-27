#!/usr/bin/env bash
# GONVRA — Avisa si hay contenido esperando aprobacion.
# Silencio si no hay nada.

set -u
PEND="$HOME/GONVRA-PUBLICAR/1-PENDIENTE"
[ -d "$PEND" ] || exit 0

shopt -s nullglob nocaseglob
IMGS=("$PEND"/*.png "$PEND"/*.jpg "$PEND"/*.jpeg "$PEND"/*.mp4)
CARPETAS=()
for d in "$PEND"/*/; do [ -d "$d" ] && CARPETAS+=("$d"); done
shopt -u nocaseglob
[ ${#IMGS[@]} -eq 0 ] && [ ${#CARPETAS[@]} -eq 0 ] && exit 0

TOTAL=$(( ${#IMGS[@]} + ${#CARPETAS[@]} ))
echo "HAY $TOTAL PIEZA(S) ESPERANDO TU OK"
echo ""
for C in "${CARPETAS[@]}"; do
  N=$(basename "$C")
  CANT=$(ls "$C" 2>/dev/null | grep -icE "\.(png|jpg|jpeg)$")
  echo "· $N  (CARRUSEL de $CANT fotos)"
  [ -f "$C/texto.txt" ] && echo "  Texto: $(head -c 140 "$C/texto.txt")"
done
for IMG in "${IMGS[@]}"; do
  NOMBRE=$(basename "$IMG")
  SINEXT="${NOMBRE%.*}"
  TXT="$PEND/$SINEXT.txt"
  case "$NOMBRE" in *.mp4) echo "· $NOMBRE  (REEL)";; *) echo "· $NOMBRE  (foto)";; esac
  if [ -f "$TXT" ]; then
    echo "  Texto: $(head -c 160 "$TXT")"
  else
    echo "  (sin texto - se publicaria sin caption)"
  fi
done
echo ""
echo "Para publicar: mové el archivo (y su .txt) a la carpeta 2-APROBADO"
echo "Ruta: ~/GONVRA-PUBLICAR/2-APROBADO"
echo ""
echo "Se publica en @gonvra1 dentro de los 10 minutos siguientes."
exit 0
