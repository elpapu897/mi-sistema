#!/usr/bin/env python3
"""
GONVRA — Posventa automática.

Mira los pedidos de Shopify y, según los días que pasaron, prepara el mail
que corresponde. NO lo manda solo: lo deja como BORRADOR en Gmail y te avisa
por Telegram, para que lo revises antes de que le llegue al cliente.

  día 0   -> gracias por la compra
  día 3   -> "ya salió" (si está despachado)
  día 12  -> cómo se usa / tips
  día 20  -> pedido de reseña

Cada mail se manda UNA sola vez por pedido (memoria en disco).
Silencio si no hay nada que hacer.
"""
import json
import os
import subprocess
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone

SECRETS = os.path.expanduser("~/.hermes/.gonvra-secrets.env")
MEMORIA = os.path.expanduser("~/.hermes/gonvra-posventa.json")
API = "https://jm60sa-cp.myshopify.com/admin/api/2026-01"
WHATSAPP = "+54 9 11 5376-7293"

ETAPAS = [
    ("gracias", 0),
    ("despacho", 3),
    ("tips", 12),
    ("resena", 20),
]


def token(nombre):
    try:
        for l in open(SECRETS, encoding="utf-8"):
            if l.startswith(nombre + "="):
                return l.split("=", 1)[1].strip()
    except Exception:
        pass
    return None


def pedidos():
    tok = token("SHOPIFY_ACCESS_TOKEN")
    if not tok:
        return []
    r = urllib.request.Request(
        API + "/orders.json?status=any&limit=100",
        headers={"X-Shopify-Access-Token": tok})
    try:
        with urllib.request.urlopen(r, timeout=30) as resp:
            return json.loads(resp.read().decode()).get("orders", [])
    except Exception:
        return []


def nombre_de(o):
    c = o.get("customer") or {}
    e = o.get("shipping_address") or {}
    n = (c.get("first_name") or e.get("first_name") or "").strip()
    return n


def texto(etapa, o):
    n = nombre_de(o)
    hola = f"Hola {n}," if n else "Hola,"
    num = o.get("order_number") or o.get("name") or ""

    if etapa == "gracias":
        return (f"Gracias por tu compra #{num}", f"""{hola}

Gracias por comprar en GONVRA. Ya tenemos tu pedido #{num}.

Lo preparamos y te aviso apenas salga. El envío es gratis y con seguimiento.

Tenés 10 días de garantía y 10 días para arrepentirte desde que lo recibís.

Cualquier cosa respondeme este mail o escribime por WhatsApp: {WHATSAPP}

Matías — GONVRA
gonvra.com""")

    if etapa == "despacho":
        return (f"Tu pedido #{num} está en camino", f"""{hola}

Tu pedido #{num} ya salió.

El tiempo estimado de entrega es de 12 a 20 días. Te va a llegar el seguimiento
al mail apenas el correo lo registre.

Si pasan más de 20 días y no llegó, avisame y lo reclamo yo.

Matías — GONVRA""")

    if etapa == "tips":
        return (f"Cómo sacarle el mejor provecho", f"""{hola}

¿Te llegó bien la rasuradora?

Tres cosas que conviene saber:

1. Cargala completa la primera vez antes de usarla.
2. Usá el peine guía que corresponda al largo que querés. Si dudás, empezá por
   el más largo: siempre podés cortar más, pero no al revés.
3. Limpiala después de cada uso con el cepillito. Es lo que más le alarga la vida.

Si algo no salió como esperabas, respondeme este mail y lo resolvemos.

Matías — GONVRA""")

    if etapa == "resena":
        return (f"¿Cómo te fue?", f"""{hola}

Pasaron unos días desde que te llegó el pedido y quería saber cómo te fue.

Si te gustó, ¿me dejarías tu opinión? A alguien que está dudando le sirve
muchísimo leer a alguien real.

Y si algo no te convenció, contámelo a mí primero. Prefiero saberlo y
resolverlo antes que te quedes con una mala experiencia.

Gracias,
Matías — GONVRA""")

    return ("", "")


def crear_borrador(para, asunto, cuerpo):
    """Deja el mail como borrador en Gmail usando el MCP ya autorizado."""
    codigo = f'''
import asyncio, json
from fastmcp import Client
async def main():
    async with Client("http://localhost:8000/mcp") as c:
        r = await c.call_tool("draft_gmail_message", {{
            "user_google_email": "gonvra0@gmail.com",
            "to": {json.dumps(para)},
            "subject": {json.dumps(asunto)},
            "body": {json.dumps(cuerpo)}
        }})
        print("OK" if r.content else "FALLO")
asyncio.run(main())
'''
    venv = os.path.expanduser("~/Claude/mcp/fbads/.venv/bin/python")
    try:
        r = subprocess.run([venv, "-c", codigo], capture_output=True,
                           text=True, timeout=120)
        return "OK" in r.stdout
    except Exception:
        return False


def main():
    try:
        hechos = json.load(open(MEMORIA))
    except Exception:
        hechos = {}

    ahora = datetime.now(timezone.utc)
    avisos = []

    for o in pedidos():
        oid = str(o.get("id"))
        mail = o.get("email")
        if not mail:
            continue
        creado = o.get("created_at")
        if not creado:
            continue
        try:
            fecha = datetime.fromisoformat(creado.replace("Z", "+00:00"))
        except ValueError:
            continue
        dias = (ahora - fecha).days

        for etapa, cuando in ETAPAS:
            clave = f"{oid}:{etapa}"
            if clave in hechos:
                continue
            if dias < cuando:
                continue
            if etapa == "despacho" and not o.get("fulfillment_status"):
                continue  # todavia no salio

            asunto, cuerpo = texto(etapa, o)
            if not asunto:
                continue
            ok = crear_borrador(mail, asunto, cuerpo)
            hechos[clave] = ahora.isoformat()
            avisos.append(
                f"· Pedido #{o.get('order_number')} ({mail}) - dia {dias}\n"
                f"  Etapa: {etapa.upper()}\n"
                f"  Asunto: {asunto}\n"
                f"  {'Borrador listo en Gmail' if ok else 'NO se pudo crear el borrador'}")

    json.dump(hechos, open(MEMORIA, "w"))

    if avisos:
        print("POSVENTA GONVRA - hay mails esperando tu revision")
        print()
        for a in avisos[:10]:
            print(a)
            print()
        print("Entra a Gmail, reviselos y mandalos.")
        print("Estan en BORRADORES, no se mandaron solos.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
