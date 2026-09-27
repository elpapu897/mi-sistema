#!/usr/bin/env bash
# GONVRA — Conecta Gmail. Genera un link NUEVO y lo abre al toque,
# asi no le da tiempo a vencerse. Despues confirma si quedo andando.
set -u

VENV=/home/matiigonzz/Claude/mcp/fbads/.venv/bin/python
CREDS=/home/matiigonzz/.google_workspace_mcp/credentials

echo "════════════════════════════════════════════════════════"
echo "  CONECTAR GMAIL — GONVRA"
echo "════════════════════════════════════════════════════════"

# 1) El servidor que atiende la vuelta de Google tiene que estar vivo
if ! ss -ltn 2>/dev/null | grep -q ":8000"; then
  echo "→ Levantando el servidor de autorizacion..."
  systemctl --user restart gonvra-gmail-auth.service
  for _ in $(seq 1 30); do
    ss -ltn 2>/dev/null | grep -q ":8000" && break
    sleep 1
  done
fi
if ! ss -ltn 2>/dev/null | grep -q ":8000"; then
  echo "✗ No se pudo levantar el servidor. Avisale a Claude."
  exit 1
fi
echo "✓ Servidor listo"

# 2) Link fresco
echo "→ Generando un link nuevo (dura pocos minutos)..."
cat > /tmp/_gmail_link.py <<'PY'
import asyncio, re, webbrowser
from fastmcp import Client

async def main():
    async with Client("http://localhost:8000/mcp") as c:
        r = await c.call_tool("start_google_auth",
                              {"user_google_email": "gonvra0@gmail.com",
                               "service_name": "Gmail"})
        txt = r.content[0].text if r.content else str(r)
        m = re.search(r'https://accounts\.google\.com/o/oauth2/auth\S+', txt)
        if not m:
            print("NO_LINK"); return
        url = m.group(0)
        print("\n" + "=" * 70)
        print("Si no se abre solo, copia este link AHORA (vence rapido):\n")
        print(url)
        print("=" * 70 + "\n")
        try: webbrowser.open(url)
        except Exception: pass

asyncio.run(main())
PY
"$VENV" -u /tmp/_gmail_link.py 2>/dev/null | grep -vE "^\[|FastMCP|╭|│|╰"

echo "AHORA: entra con gonvra0@gmail.com y aceptá."
echo "Si Google dice que la app no esta verificada:"
echo "   Configuracion avanzada  ->  Ir a GONVRA (no seguro)"
echo
echo "Esperando que autorices (3 minutos)..."

# 3) Esperar a que aparezca la credencial
for _ in $(seq 1 90); do
  if ls "$CREDS"/*gonvra0* >/dev/null 2>&1; then
    echo
    echo "✅ LISTO — Gmail quedo conectado."
    exit 0
  fi
  sleep 2
done

echo
echo "⏳ Todavia no llego la autorizacion."
echo "   Volve a correr este mismo comando y probá de nuevo."
exit 1
