#!/usr/bin/env bash
# =============================================================================
#  RE-CLONAR REPOS DE TERCEROS
#
#  Los repos que no son tuyos no se respaldaron como código (habría duplicado
#  ~1 GB y creado repos anidados). Acá se vuelven a clonar en el commit exacto
#  en el que los tenías, así quedan idénticos a como estaban.
#
#  Uso:  bash scripts/reclonar-terceros.sh
# =============================================================================
set -uo pipefail

REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
LISTA="$REPO/scripts/REPOS-EXTERNOS.tsv"

[ -f "$LISTA" ] || { echo "Falta $LISTA"; exit 1; }

echo
echo "  RE-CLONADO DE REPOS EXTERNOS"
echo "  ============================"
echo

OK=0; FALLO=0; YA=0
while IFS=$'\t' read -r ruta url sha; do
  [ -z "${ruta:-}" ] && continue
  destino="$HOME/$ruta"

  if [ -d "$destino/.git" ]; then
    printf '  [=] %-46s ya existe\n' "$ruta"
    YA=$((YA+1)); continue
  fi

  printf '  [>] %-46s ' "$ruta"
  mkdir -p "$(dirname "$destino")"
  if git clone --quiet "$url" "$destino" 2>/dev/null; then
    if [ "$sha" != "?" ] && git -C "$destino" checkout --quiet "$sha" 2>/dev/null; then
      echo "OK ($sha)"
    else
      echo "OK (rama por defecto; el commit $sha ya no existe)"
    fi
    OK=$((OK+1))
  else
    echo "FALLÓ — puede ser privado o borrado: $url"
    FALLO=$((FALLO+1))
  fi
done < "$LISTA"

echo
echo "  Clonados: $OK   Ya estaban: $YA   Fallaron: $FALLO"
[ $FALLO -gt 0 ] && echo "  Los que fallaron ya no están públicos. No es culpa del backup."
echo
echo "  Recordá instalar dependencias donde haga falta:  npm install / pip install -r"
echo
