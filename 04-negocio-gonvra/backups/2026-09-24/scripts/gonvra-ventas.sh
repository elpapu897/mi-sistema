#!/usr/bin/env bash
# GONVRA — Vigila las ventas. Si entra un pedido nuevo, avisa por Telegram.
# Si no hay nada nuevo, NO dice nada (silencio = sin novedad). Cuesta $0.

python3 - <<'PY'
import json, os, urllib.request

SECRETS = os.path.expanduser("~/.hermes/.gonvra-secrets.env")
VISTOS = os.path.expanduser("~/.hermes/gonvra-pedidos-vistos.json")
BASE = "https://jm60sa-cp.myshopify.com/admin/api/2026-01"

tok = None
try:
    for l in open(SECRETS, encoding="utf-8"):
        if l.startswith("SHOPIFY_ACCESS_TOKEN="):
            tok = l.split("=", 1)[1].strip()
            break
except Exception:
    pass
if not tok:
    raise SystemExit(0)

def pedir(ruta):
    r = urllib.request.Request(BASE + ruta, headers={"X-Shopify-Access-Token": tok})
    with urllib.request.urlopen(r, timeout=25) as resp:
        return json.loads(resp.read().decode())

try:
    pedidos = pedir("/orders.json?status=any&limit=50").get("orders", [])
except Exception:
    raise SystemExit(0)   # si Shopify no responde, no molestar

try:
    vistos = set(json.load(open(VISTOS)))
except Exception:
    vistos = set()

nuevos = [o for o in pedidos if str(o.get("id")) not in vistos]

# Primera corrida: solo memorizar, no gritar por pedidos viejos
primera = not os.path.exists(VISTOS)

if nuevos and not primera:
    total = sum(float(o.get("total_price") or 0) for o in nuevos)
    print("VENTA EN GONVRA" + ("S" if len(nuevos) > 1 else "") + "!")
    print("")
    for o in nuevos:
        cli = o.get("customer") or {}
        nombre = (cli.get("first_name") or "") + " " + (cli.get("last_name") or "")
        print("Pedido #%s - $%s %s" % (o.get("order_number"),
                                       o.get("total_price"),
                                       o.get("currency") or ""))
        print("  Cliente: %s (%s)" % (nombre.strip() or "sin nombre",
                                      o.get("email") or "sin mail"))
        print("  Pago: %s | Envio: %s" % (o.get("financial_status"),
                                          o.get("fulfillment_status") or "pendiente"))
        for li in o.get("line_items", []):
            print("  %sx %s" % (li.get("quantity"), li.get("title")))
        print("")
    if len(nuevos) > 1:
        print("TOTAL: $%.2f en %d pedidos" % (total, len(nuevos)))
    print("Entra al panel de Shopify para despacharlo.")

with open(VISTOS, "w") as f:
    json.dump([str(o.get("id")) for o in pedidos], f)
PY
exit 0
