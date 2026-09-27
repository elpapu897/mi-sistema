#!/usr/bin/env bash
# Reabre Brave con el puerto de depuración para que Claude pueda usarlo.
# Tus pestañas y tu sesión quedan intactas: es el mismo perfil de siempre.
set -e
echo "Cerrando Brave…"
pkill -f brave-browser 2>/dev/null || true
sleep 3
echo "Abriendo Brave con acceso para Claude…"
nohup brave-browser --remote-debugging-port=9222 --restore-last-session >/dev/null 2>&1 &
sleep 5
if curl -s --max-time 5 http://127.0.0.1:9222/json/version >/dev/null; then
  echo "Listo. Brave está abierto y Claude puede usarlo."
else
  echo "No se abrió el puerto. Probá de nuevo."
fi
