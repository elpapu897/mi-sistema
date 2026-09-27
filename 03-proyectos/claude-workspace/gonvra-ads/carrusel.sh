#!/usr/bin/env bash
# Renderiza las placas de un carrusel como PNG sueltos, listas para subir.
#   ./carrusel.sh                      → renderiza todos
#   ./carrusel.sh Carrusel-Problema    → sólo ese
set -e
cd "$(dirname "$0")"

renderizar() {
  local id="$1"
  local n
  n=$(npx --no-install remotion compositions 2>/dev/null | awk -v id="$id" '$1==id {print $4}')
  [ -z "$n" ] && { echo "No encontré el carrusel '$id'"; exit 1; }
  mkdir -p "out/$id"
  echo "▸ $id  ($n placas)"
  for ((i=0; i<n; i++)); do
    printf "   placa %d/%d\n" $((i+1)) "$n"
    npx --no-install remotion still "$id" "out/$id/$(printf '%02d' $((i+1))).png" --frame="$i" --log=error
  done
  echo "   → out/$id/"
}

if [ -n "$1" ]; then
  renderizar "$1"
else
  for id in $(npx --no-install remotion compositions 2>/dev/null | awk '/^Carrusel-/ {print $1}'); do
    renderizar "$id"
  done
fi
echo "Listo."
