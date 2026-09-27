#!/usr/bin/env bash
# =============================================================
#  Sound Blue Project — servidor local para la feria
# =============================================================
#  Por qué hace falta: los navegadores bloquean el micrófono
#  cuando abrís un archivo HTML suelto (file://). Sirviendo la
#  carpeta en http://localhost el micrófono SÍ funciona, y todo
#  anda sin internet.
#
#  Uso:  ./servir.sh          (o:  bash servir.sh)
# =============================================================
set -euo pipefail
cd "$(dirname "$0")"

PUERTO="${1:-8000}"
URL="http://localhost:${PUERTO}"

echo ""
echo "  ██  SOUND BLUE PROJECT"
echo "  ──────────────────────────────────────────────"
echo "  Servidor local:  ${URL}"
echo "  Micrófono:       habilitado (contexto seguro)"
echo "  Internet:        no hace falta"
echo ""
echo "  Para cortar:     Ctrl + C"
echo "  ──────────────────────────────────────────────"
echo ""

# abrir el navegador solo, en segundo plano
( sleep 1.2; xdg-open "$URL" >/dev/null 2>&1 || true ) &

exec python3 -m http.server "$PUERTO" --bind 127.0.0.1
