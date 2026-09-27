#!/usr/bin/env bash
# GONVRA — Sube una imagen al tema de Shopify y devuelve su URL publica.
# Instagram necesita una URL publica para publicar; esto la genera.
#
# Uso:  gonvra-subir-imagen.sh /ruta/a/la/imagen.png
# Salida (stdout): la URL publica, nada mas.

set -u
ARCHIVO="${1:-}"
TEMA="${TEMA:-148158414963}"
TIENDA="jm60sa-cp.myshopify.com"
REPO="/home/matiigonzz/Documents/Codex/tiendas/jm60sa-cp"
TNUM="6"   # carpeta del tema en el CDN (descubierta el 23/09)

if [ -z "$ARCHIVO" ] || [ ! -f "$ARCHIVO" ]; then
  echo "ERROR: no existe el archivo '$ARCHIVO'" >&2
  exit 1
fi

EXT="${ARCHIVO##*.}"
case "${EXT,,}" in
  png|jpg|jpeg) ;;
  *) echo "ERROR: Instagram solo acepta JPG o PNG (llego .$EXT)" >&2; exit 1;;
esac

# Nombre unico para que no pise nada ni quede cacheado
NOMBRE="gonvra-pub-$(date +%Y%m%d-%H%M%S)-$RANDOM.${EXT,,}"

cp "$ARCHIVO" "$REPO/live-theme/assets/$NOMBRE" || {
  echo "ERROR: no se pudo copiar al tema" >&2; exit 1; }

cd "$REPO" || exit 1
if ! npx shopify theme push --store "$TIENDA" --theme "$TEMA" \
     --path ./live-theme --allow-live --force \
     --only "assets/$NOMBRE" >/dev/null 2>&1; then
  echo "ERROR: fallo el push a Shopify" >&2
  rm -f "$REPO/live-theme/assets/$NOMBRE"
  exit 1
fi

URL="https://gonvra.com/cdn/shop/t/$TNUM/assets/$NOMBRE"

# No confiar: verificar que este arriba antes de devolverla
for _ in $(seq 1 12); do
  CODE=$(curl -s -o /dev/null -w "%{http_code}" -L --max-time 10 "$URL")
  [ "$CODE" = "200" ] && { echo "$URL"; exit 0; }
  sleep 5
done

echo "ERROR: se subio pero la URL no responde ($URL)" >&2
exit 1
