#!/bin/bash
# Abre el Mission Control de GONVRA correctamente (con servidor local)
cd "$(dirname "$0")"
python3 generar-datos.py >/dev/null 2>&1
if ! curl -s -o /dev/null --max-time 2 http://localhost:8080/mission-control.html; then
  (python3 -m http.server 8080 --bind 127.0.0.1 >/dev/null 2>&1 &)
  sleep 2
fi
xdg-open "http://localhost:8080/mission-control.html" >/dev/null 2>&1
echo "✅ Mission Control abierto en http://localhost:8080/mission-control.html"
