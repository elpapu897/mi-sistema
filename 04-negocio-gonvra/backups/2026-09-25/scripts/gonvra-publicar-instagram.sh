#!/usr/bin/env bash
# GONVRA — Publica en Instagram lo que este en 2-APROBADO.
# Si no hay nada, no dice nada (silencio = sin novedad).
# Nada se publica solo: Matias tiene que mover el archivo a 2-APROBADO.

set -u
BASE="$HOME/GONVRA-PUBLICAR"
APROBADO="$BASE/2-APROBADO"
PUBLICADO="$BASE/3-PUBLICADO"
SECRETS="$HOME/.hermes/.gonvra-secrets.env"
IGID="28674883412124543"

[ -d "$APROBADO" ] || exit 0

# shellcheck disable=SC1090
set -a; . "$SECRETS" 2>/dev/null; set +a
[ -n "${INSTAGRAM_ACCESS_TOKEN:-}" ] || { echo "GONVRA: falta el token de Instagram"; exit 0; }

shopt -s nullglob nocaseglob
ARCHIVOS=("$APROBADO"/*.png "$APROBADO"/*.jpg "$APROBADO"/*.jpeg)
shopt -u nocaseglob
[ ${#ARCHIVOS[@]} -eq 0 ] && exit 0

for IMG in "${ARCHIVOS[@]}"; do
  NOMBRE=$(basename "$IMG")
  SINEXT="${NOMBRE%.*}"
  TXT="$APROBADO/$SINEXT.txt"
  CAPTION=""
  [ -f "$TXT" ] && CAPTION=$(cat "$TXT")

  # 1) URL publica
  URL=$(bash "$HOME/.hermes/scripts/gonvra-subir-imagen.sh" "$IMG" 2>/dev/null)
  if [ -z "$URL" ]; then
    echo "GONVRA: no se pudo subir '$NOMBRE'. Queda en 2-APROBADO para reintentar."
    continue
  fi

  # 2) Contenedor
  CONT=$(curl -s -X POST --max-time 60 "https://graph.instagram.com/v23.0/$IGID/media" \
    --data-urlencode "image_url=$URL" \
    --data-urlencode "caption=$CAPTION" \
    --data-urlencode "access_token=$INSTAGRAM_ACCESS_TOKEN")
  CID=$(echo "$CONT" | python3 -c "import sys,json;print(json.load(sys.stdin).get('id',''))" 2>/dev/null)
  if [ -z "$CID" ]; then
    echo "GONVRA: Instagram rechazo '$NOMBRE'"
    echo "$CONT" | head -c 240
    continue
  fi

  # 3) Publicar de verdad
  sleep 6
  PUB=$(curl -s -X POST --max-time 60 "https://graph.instagram.com/v23.0/$IGID/media_publish" \
    -d "creation_id=$CID" -d "access_token=$INSTAGRAM_ACCESS_TOKEN")
  PID=$(echo "$PUB" | python3 -c "import sys,json;print(json.load(sys.stdin).get('id',''))" 2>/dev/null)
  if [ -z "$PID" ]; then
    echo "GONVRA: se armo el post de '$NOMBRE' pero fallo al publicarlo"
    echo "$PUB" | head -c 240
    continue
  fi

  # 4) Link real del post
  LINK=$(curl -s --max-time 30 \
    "https://graph.instagram.com/v23.0/$PID?fields=permalink&access_token=$INSTAGRAM_ACCESS_TOKEN" \
    | python3 -c "import sys,json;print(json.load(sys.stdin).get('permalink',''))" 2>/dev/null)

  mkdir -p "$PUBLICADO"
  mv "$IMG" "$PUBLICADO/" 2>/dev/null
  [ -f "$TXT" ] && mv "$TXT" "$PUBLICADO/" 2>/dev/null

  echo "PUBLICADO EN INSTAGRAM"
  echo ""
  echo "Archivo: $NOMBRE"
  [ -n "$CAPTION" ] && echo "Texto: $(echo "$CAPTION" | head -c 120)..."
  [ -n "$LINK" ] && echo "Ver: $LINK"
  echo ""
  echo "Entra y fijate los comentarios: las preguntas son clientes."
done
exit 0
