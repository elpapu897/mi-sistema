#!/usr/bin/env bash
# GONVRA — Sube una imagen o video al tema de Shopify y devuelve su URL publica.
# Instagram necesita URLs publicas; esto las genera.
#
# Uso:  gonvra-subir-archivo.sh /ruta/archivo.(png|jpg|mp4)
# Salida (stdout): la URL publica y nada mas.

set -u
ARCHIVO="${1:-}"
TEMA="${TEMA:-148158414963}"
TIENDA="jm60sa-cp.myshopify.com"
REPO="/home/matiigonzz/Documents/Codex/tiendas/jm60sa-cp"
TNUM="6"

[ -n "$ARCHIVO" ] && [ -f "$ARCHIVO" ] || { echo "ERROR: no existe '$ARCHIVO'" >&2; exit 1; }

EXT="${ARCHIVO##*.}"; EXT="${EXT,,}"
case "$EXT" in
  png|jpg|jpeg|mp4|mov) ;;
  *) echo "ERROR: formato .$EXT no soportado (png/jpg/mp4)" >&2; exit 1;;
esac

NOMBRE="gonvra-$(date +%Y%m%d-%H%M%S)-$RANDOM.$EXT"
cp "$ARCHIVO" "$REPO/live-theme/assets/$NOMBRE" || { echo "ERROR: no se pudo copiar" >&2; exit 1; }

cd "$REPO" || exit 1
if ! npx shopify theme push --store "$TIENDA" --theme "$TEMA" \
     --path ./live-theme --allow-live --force --only "assets/$NOMBRE" >/dev/null 2>&1; then
  echo "ERROR: fallo el push a Shopify" >&2
  rm -f "$REPO/live-theme/assets/$NOMBRE"
  exit 1
fi

URL="https://gonvra.com/cdn/shop/t/$TNUM/assets/$NOMBRE"
for _ in $(seq 1 15); do
  [ "$(curl -s -o /dev/null -w '%{http_code}' -L --max-time 10 "$URL")" = "200" ] && { echo "$URL"; exit 0; }
  sleep 4
done
echo "ERROR: subido pero la URL no responde ($URL)" >&2
exit 1
