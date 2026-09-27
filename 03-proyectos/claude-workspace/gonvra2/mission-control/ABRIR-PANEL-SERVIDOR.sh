#!/bin/bash
# Abre el tunel seguro al servidor GONVRA y el Mission Control
SRV="gonvra@47.85.84.11"
echo "════════════════════════════════════════════"
echo "  GONVRA · Mission Control (servidor)"
echo "════════════════════════════════════════════"
echo ""

# ¿el puerto 8080 ya está escuchando?
if ss -tln 2>/dev/null | grep -q "127.0.0.1:8080"; then
  echo "✅ El túnel ya estaba abierto"
else
  echo "🔐 Abriendo túnel seguro al servidor…"
  echo "   Te va a pedir la contraseña del servidor."
  echo "   NO se ve nada mientras la escribís. Es normal. Escribila y Enter."
  echo ""
  ssh -f -N -L 8080:127.0.0.1:8080 -L 5678:127.0.0.1:5678 "$SRV"
  RC=$?
  sleep 3
  if [ $RC -ne 0 ] || ! ss -tln 2>/dev/null | grep -q "127.0.0.1:8080"; then
    echo ""
    echo "❌ No se pudo abrir el túnel."
    echo "   Probá a mano con este comando y mirá qué error da:"
    echo "   ssh -N -L 8080:127.0.0.1:8080 -L 5678:127.0.0.1:5678 $SRV"
    exit 1
  fi
  echo "✅ Túnel abierto"
fi

echo ""
echo "🖥️  Mission Control → http://localhost:8080"
echo "🔌 n8n             → http://localhost:5678"
echo ""
echo "   (usá el usuario y la clave que te dio 'gonvra-access')"
xdg-open "http://localhost:8080" >/dev/null 2>&1
echo ""
echo "Para cerrar el túnel cuando termines:  pkill -f '8080:127.0.0.1:8080'"
