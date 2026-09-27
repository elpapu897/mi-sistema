#!/usr/bin/env bash
# GONVRA — Guardián del túnel público.
#
# No se conforma con "el servicio está active" (eso ya nos mintió una vez, E-018).
# Hace un PING REAL desde afuera y confirma que llegó a n8n.
# Si no llega dos veces seguidas, reinicia el túnel y avisa.
#
# Silencio si todo está bien.

set -u
ESTADO="$HOME/.hermes/gonvra-tunel-fallos"
URLFILE="$HOME/.hermes/gonvra-url-publica.txt"

# 1) URL actual segun el log del tunel
URL=$(journalctl --user -u gonvra-tunel.service --since "-24 hours" --no-pager 2>/dev/null \
      | grep -oE "https://[a-z0-9-]+\.trycloudflare\.com" | tail -1)

if [ -z "$URL" ]; then
  echo "GUARDIAN: el tunel no publico ninguna direccion."
  echo "Los avisos de venta y los botones de aprobar NO funcionan."
  exit 0
fi

# 2) PING REAL desde internet: no alcanza con que el servicio diga "active"
CODE=$(curl -s -o /dev/null -w "%{http_code}" -X POST -L --max-time 25 \
       -H "Content-Type: application/json" -d '{"ping":1}' \
       "$URL/webhook/gonvra-venta")

FALLOS=0
[ -f "$ESTADO" ] && FALLOS=$(cat "$ESTADO" 2>/dev/null || echo 0)

if [ "$CODE" = "200" ]; then
  # sano: resetear el contador
  echo 0 > "$ESTADO"

  ANTERIOR=""
  [ -f "$URLFILE" ] && ANTERIOR=$(cat "$URLFILE")
  if [ -n "$ANTERIOR" ] && [ "$ANTERIOR" != "$URL" ]; then
    echo "$URL" > "$URLFILE"
    echo "GUARDIAN: la direccion publica cambio."
    echo ""
    echo "Shopify se reapunta solo (job de webhooks)."
    echo "Los LINKS de aprobar viejos ya no sirven: el proximo aviso trae los nuevos."
    echo ""
    echo "Instagram hay que actualizarlo a mano:"
    echo "  ${URL}/webhook/gonvra-ig   (token: gonvra2026verify)"
  fi
  exit 0
fi

# 3) No responde
FALLOS=$((FALLOS + 1))
echo "$FALLOS" > "$ESTADO"

if [ "$FALLOS" -lt 2 ]; then
  # primer fallo: puede ser un hipo de red, no molestar todavia
  exit 0
fi

echo "GUARDIAN: el tunel NO responde (${FALLOS} veces seguidas, codigo $CODE)."
echo "Reiniciandolo..."
systemctl --user restart gonvra-tunel.service
sleep 30

NUEVA=$(journalctl --user -u gonvra-tunel.service --since "-2 min" --no-pager 2>/dev/null \
        | grep -oE "https://[a-z0-9-]+\.trycloudflare\.com" | tail -1)
if [ -n "$NUEVA" ]; then
  CODE2=$(curl -s -o /dev/null -w "%{http_code}" -X POST -L --max-time 25 \
          -H "Content-Type: application/json" -d '{"ping":1}' \
          "$NUEVA/webhook/gonvra-venta")
  if [ "$CODE2" = "200" ]; then
    echo "$NUEVA" > "$URLFILE"
    echo 0 > "$ESTADO"
    echo ""
    echo "Arreglado. Direccion nueva:"
    echo "  $NUEVA"
    echo ""
    echo "Instagram hay que actualizarlo a mano:"
    echo "  ${NUEVA}/webhook/gonvra-ig   (token: gonvra2026verify)"
    exit 0
  fi
fi

echo ""
echo "NO se pudo arreglar solo. Mientras tanto:"
echo "  · las ventas NO avisan al instante (igual el job de cada 15 min las agarra)"
echo "  · los links de aprobar NO funcionan (movelo a mano a 2-APROBADO)"
exit 0
