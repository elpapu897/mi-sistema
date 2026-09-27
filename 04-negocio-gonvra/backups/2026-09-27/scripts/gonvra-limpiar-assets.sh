#!/usr/bin/env bash
# GONVRA — Borra del tema los archivos que se subieron solo para publicar en
# Instagram. Instagram ya se quedó con una copia propia, así que no hacen falta.
# Deja los de los últimos 2 días por las dudas.
# Silencio si no hay nada que borrar.

set -u
REPO="/home/matiigonzz/Documents/Codex/tiendas/jm60sa-cp"
TIENDA="jm60sa-cp.myshopify.com"
TEMA="148158414963"
DIAS=2

cd "$REPO" || exit 0
[ -d live-theme/assets ] || exit 0

LIMITE=$(date -d "-$DIAS days" +%Y%m%d)
BORRADOS=0

shopt -s nullglob
for f in live-theme/assets/gonvra-*; do
  nombre=$(basename "$f")
  # formato: gonvra-AAAAMMDD-HHMMSS-RANDOM.ext
  fecha=$(echo "$nombre" | grep -oE "[0-9]{8}" | head -1)
  [ -z "$fecha" ] && continue
  [ "$fecha" -ge "$LIMITE" ] && continue
  rm -f "$f"
  BORRADOS=$((BORRADOS + 1))
done
shopt -u nullglob

[ "$BORRADOS" -eq 0 ] && exit 0

# --nodelete NO: justamente queremos que borre en el remoto lo que ya no está local.
if npx shopify theme push --store "$TIENDA" --theme "$TEMA" \
     --path ./live-theme --allow-live --force >/dev/null 2>&1; then
  echo "GONVRA: se limpiaron $BORRADOS archivos viejos del tema."
  echo "(eran copias temporales para publicar en Instagram)"
else
  echo "GONVRA: se borraron $BORRADOS archivos locales pero fallo el push."
  echo "Se reintenta manana."
fi
exit 0
