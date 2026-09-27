#!/usr/bin/env bash
# Tapa credenciales que se hayan colado en los chats exportados a Obsidian.
# Silencioso si no hay nada. Solo habla cuando tapo algo (para que quede registro).
SALIDA=$(python3 /home/matiigonzz/Claude/scripts/tapar-credenciales-obsidian.py 2>&1)
if echo "$SALIDA" | grep -q "tapadas"; then
  echo "SEGURIDAD GONVRA - se taparon credenciales en los chats de Obsidian:"
  echo "$SALIDA" | tail -8
fi
exit 0
