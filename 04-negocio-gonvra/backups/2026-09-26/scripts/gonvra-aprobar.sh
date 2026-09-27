#!/usr/bin/env bash
# GONVRA — Mueve una pieza de 1-PENDIENTE a 2-APROBADO (o a 0-DESCARTADO).
# Lo llama el webhook cuando Matias toca el link desde el celular.
#
# Uso:  gonvra-aprobar.sh <nombre-de-la-pieza> <aprobar|descartar> <secreto>

set -u
BASE="$HOME/GONVRA-PUBLICAR"
PEND="$BASE/1-PENDIENTE"
APROB="$BASE/2-APROBADO"
DESC="$BASE/0-DESCARTADO"
SECRETS="$HOME/.hermes/.gonvra-secrets.env"

PIEZA="${1:-}"
ACCION="${2:-}"
TOKEN="${3:-}"

# shellcheck disable=SC1090
set -a; . "$SECRETS" 2>/dev/null; set +a

# Seguridad: sin el secreto correcto no se toca nada
if [ -z "${GONVRA_APROBAR_SECRETO:-}" ] || [ "$TOKEN" != "$GONVRA_APROBAR_SECRETO" ]; then
  echo "RECHAZADO"
  exit 0
fi

# Seguridad: el nombre no puede salirse de la carpeta
case "$PIEZA" in
  ""|*/*|*..*) echo "NOMBRE INVALIDO"; exit 0;;
esac

ORIGEN="$PEND/$PIEZA"
if [ ! -e "$ORIGEN" ]; then
  echo "YA NO ESTA: '$PIEZA' no esta en 1-PENDIENTE (quiza ya lo aprobaste)"
  exit 0
fi

case "$ACCION" in
  aprobar)
    mkdir -p "$APROB"
    mv "$ORIGEN" "$APROB/" 2>/dev/null || { echo "ERROR al mover"; exit 0; }
    # si es un archivo suelto, llevar tambien su .txt
    if [ -f "$APROB/$PIEZA" ]; then
      SIN="${PIEZA%.*}"
      [ -f "$PEND/$SIN.txt" ] && mv "$PEND/$SIN.txt" "$APROB/" 2>/dev/null
    fi
    echo "APROBADO: $PIEZA"
    echo "Publicando ahora..."
    # Publicar al instante, sin esperar los 10 minutos del flujo
    timeout 570 python3 "$HOME/.hermes/scripts/gonvra-publicar-ig.py" 2>&1 | head -20
    ;;
  descartar)
    mkdir -p "$DESC"
    mv "$ORIGEN" "$DESC/" 2>/dev/null
    if [ -f "$DESC/$PIEZA" ]; then
      SIN="${PIEZA%.*}"
      [ -f "$PEND/$SIN.txt" ] && mv "$PEND/$SIN.txt" "$DESC/" 2>/dev/null
    fi
    echo "DESCARTADO: $PIEZA"
    echo "Queda guardado en 0-DESCARTADO por si cambias de idea."
    ;;
  *)
    echo "ACCION INVALIDA"
    ;;
esac
exit 0
