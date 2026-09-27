#!/usr/bin/env bash
# GONVRA — Mantiene los webhooks de Shopify apuntando a la URL actual del tunel.
#
# La URL de Cloudflare es temporal: cambia cada vez que el tunel se reinicia.
# Si no se re-registran, Shopify avisa a una direccion muerta y NO te enteras
# de las ventas. Este script lo arregla solo.
#
# Silencio si ya estaba todo bien.

set -u
SECRETS="$HOME/.hermes/.gonvra-secrets.env"
TIENDA="jm60sa-cp.myshopify.com"
API="https://$TIENDA/admin/api/2026-01"

# 1) URL actual del tunel (la saca del log del servicio)
URL=$(journalctl --user -u gonvra-tunel.service --since "-24 hours" --no-pager 2>/dev/null \
      | grep -oE "https://[a-z0-9-]+\.trycloudflare\.com" | tail -1)
[ -z "$URL" ] && exit 0

# Detectar si la URL cambio respecto de la anterior
ANTERIOR=""
[ -f "$HOME/.hermes/gonvra-url-publica.txt" ] && ANTERIOR=$(cat "$HOME/.hermes/gonvra-url-publica.txt")
CAMBIO=0
[ -n "$ANTERIOR" ] && [ "$ANTERIOR" != "$URL" ] && CAMBIO=1

# Guardar la URL para que otros scripts la usen
echo "$URL" > "$HOME/.hermes/gonvra-url-publica.txt"

# 2) Verificar que el tunel responda de verdad antes de registrar nada
CODE=$(curl -s -o /dev/null -w "%{http_code}" -L --max-time 20 "$URL/webhook/gonvra-venta")
if [ "$CODE" = "000" ]; then
  echo "GONVRA: el tunel no responde. Los webhooks quedaron sin actualizar."
  exit 0
fi

# shellcheck disable=SC1090
set -a; . "$SECRETS" 2>/dev/null; set +a
[ -n "${SHOPIFY_ACCESS_TOKEN:-}" ] || exit 0

python3 - "$URL" <<'PY'
import json, os, sys, urllib.error, urllib.request

url_base = sys.argv[1]
tok = None
for l in open(os.path.expanduser("~/.hermes/.gonvra-secrets.env"), encoding="utf-8"):
    if l.startswith("SHOPIFY_ACCESS_TOKEN="):
        tok = l.split("=", 1)[1].strip()
API = "https://jm60sa-cp.myshopify.com/admin/api/2026-01"
H = {"X-Shopify-Access-Token": tok, "Content-Type": "application/json"}

# Lo que queremos que exista: topic -> ruta del webhook en n8n
QUEREMOS = {
    "orders/create": "/webhook/gonvra-venta",
}

def pedir(metodo, ruta, cuerpo=None):
    datos = json.dumps(cuerpo).encode() if cuerpo else None
    r = urllib.request.Request(API + ruta, data=datos, headers=H, method=metodo)
    try:
        with urllib.request.urlopen(r, timeout=30) as resp:
            txt = resp.read().decode()
            return json.loads(txt) if txt else {}
    except urllib.error.HTTPError as e:
        return {"error": e.read().decode()[:200], "code": e.code}

actuales = pedir("GET", "/webhooks.json").get("webhooks", [])
cambios = []

for topic, ruta in QUEREMOS.items():
    destino = url_base + ruta
    mios = [w for w in actuales if w.get("topic") == topic]
    ok = [w for w in mios if w.get("address") == destino]

    # borrar los que apuntan a una URL vieja
    for w in mios:
        if w.get("address") != destino:
            pedir("DELETE", f"/webhooks/{w['id']}.json")
            cambios.append(f"borrado webhook viejo de {topic}")

    if not ok:
        r = pedir("POST", "/webhooks.json", {"webhook": {
            "topic": topic, "address": destino, "format": "json"}})
        if r.get("webhook"):
            cambios.append(f"{topic} -> apunta a la URL nueva")
        else:
            cambios.append(f"NO se pudo registrar {topic}: {str(r)[:120]}")

if cambios:
    print("GONVRA: webhooks de Shopify actualizados")
    print()
    for c in cambios:
        print("  ·", c)
    print()
    print(f"  URL actual: {url_base}")
PY
# Instagram NO se puede actualizar por API: Meta solo lo deja desde el panel.
# Si la URL cambio, hay que avisarle a Matias con el dato listo para pegar.
if [ "$CAMBIO" = "1" ]; then
  echo ""
  echo "OJO: la direccion publica cambio."
  echo ""
  echo "Shopify ya se actualizo solo."
  echo "Pero los COMENTARIOS de Instagram hay que arreglarlos a mano (2 min):"
  echo ""
  echo "1) Entra a developers.facebook.com/apps -> tu app -> Instagram -> Webhooks"
  echo "2) Editar la suscripcion y pegar esta direccion nueva:"
  echo ""
  echo "   ${URL}/webhook/gonvra-ig"
  echo ""
  echo "3) Token de verificacion: gonvra2026verify"
  echo ""
  echo "Hasta que lo hagas, los comentarios NO disparan el mensaje privado."
fi
exit 0
