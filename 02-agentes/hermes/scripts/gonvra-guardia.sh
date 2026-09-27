#!/usr/bin/env bash
# GONVRA — GUARDIA (watchdog sin LLM)
# Regla: si todo esta bien, NO imprime nada (silencio = no molesta a Matias).
# Solo escribe en stdout cuando hay algo roto. Cuesta 0 tokens.

PROBLEMAS=""

chequear_url() {
  local nombre="$1" url="$2" esperado="${3:-200}"
  local code
  code=$(curl -s -o /dev/null -w "%{http_code}" --max-time 20 "$url" 2>/dev/null)
  if [ "$code" != "$esperado" ]; then
    PROBLEMAS="${PROBLEMAS}- ${nombre}: responde ${code} (esperado ${esperado}) -> ${url}\n"
  fi
}

# 1) La tienda tiene que estar viva y vendible
chequear_url "Home gonvra.com" "https://gonvra.com/"
chequear_url "Ficha de producto" "https://gonvra.com/products/face-body-electric-shaver"
chequear_url "Politica de envios" "https://gonvra.com/policies/shipping-policy"
chequear_url "Politica de reembolso" "https://gonvra.com/policies/refund-policy"
chequear_url "Terminos" "https://gonvra.com/policies/terms-of-service"
chequear_url "Privacidad" "https://gonvra.com/policies/privacy-policy"

# 2) El precio no tiene que cambiar solo
PRECIO=$(curl -s --max-time 20 "https://gonvra.com/products/face-body-electric-shaver.json" \
  | python3 -c "import sys,json;print(json.load(sys.stdin)['product']['variants'][0]['price'])" 2>/dev/null)
if [ -n "$PRECIO" ] && [ "$PRECIO" != "36900.00" ]; then
  PROBLEMAS="${PROBLEMAS}- PRECIO CAMBIO: ahora \$${PRECIO} (esperado \$36900.00)\n"
fi
if [ -z "$PRECIO" ]; then
  PROBLEMAS="${PROBLEMAS}- No se pudo leer el precio del producto (JSON caido)\n"
fi

# 3) El motor de los agentes tiene que estar vivo (si se cae, nadie trabaja)
#    El pidfile es JSON: {"pid": 12345, ...}. Hay que parsearlo, no grepear digitos.
PID=$(python3 -c "import json,sys;print(json.load(open(sys.argv[1]))['pid'])" \
  "$HOME/.hermes/gateway.pid" 2>/dev/null)
if [ -z "$PID" ] || ! kill -0 "$PID" 2>/dev/null; then
  PROBLEMAS="${PROBLEMAS}- El motor de agentes no esta corriendo: hoy no va a trabajar ninguno. Avisale a Matias.\n"
fi

# 4) Disco: si se llena, se rompe todo
USO=$(df --output=pcent / | tail -1 | tr -dc '0-9')
if [ -n "$USO" ] && [ "$USO" -ge 90 ]; then
  PROBLEMAS="${PROBLEMAS}- Disco al ${USO}%: liberar espacio ya\n"
fi

# 5) RAM libre
LIBRE=$(free -m | awk '/^Mem:/{print $7}')
if [ -n "$LIBRE" ] && [ "$LIBRE" -lt 500 ]; then
  PROBLEMAS="${PROBLEMAS}- RAM disponible baja: ${LIBRE} MB\n"
fi

if [ -n "$PROBLEMAS" ]; then
  echo "GUARDIA GONVRA — hay problemas ($(date '+%d/%m %H:%M')):"
  printf "%b" "$PROBLEMAS"
fi
exit 0
