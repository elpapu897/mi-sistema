#!/usr/bin/env bash
# Regenera los datos del Mission Control para que el panel no quede congelado.
# Silencioso si todo sale bien; solo habla cuando falla.
cd /home/matiigonzz/Claude/gonvra2/mission-control || {
  echo "Mission Control: no existe la carpeta"; exit 0; }

SALIDA=$(python3 generar-datos.py 2>&1)
if [ $? -ne 0 ]; then
  echo "Mission Control: fallo al regenerar los datos"
  echo "$SALIDA" | tail -5
fi
exit 0
