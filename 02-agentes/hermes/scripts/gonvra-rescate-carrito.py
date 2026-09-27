#!/usr/bin/env python3
"""
GONVRA — Rescate de carrito en 3 toques (idea E).

  toque 1 -> a las 2 h de abandonado
  toque 2 -> a las 20 h
  toque 3 -> a las 44 h

Antes de cada toque chequea si ya compró. Si compró, CORTA y no molesta más.
Deja el mail como BORRADOR en Gmail y te avisa por Telegram.
Nunca inventa descuentos ni urgencia (regla 2).

Silencio si no hay nada.
"""
import json
import os
import subprocess
import sys
import urllib.request
from datetime import datetime, timezone

SECRETS = os.path.expanduser("~/.hermes/.gonvra-secrets.env")
MEMORIA = os.path.expanduser("~/.hermes/gonvra-rescate.json")
API = "https://jm60sa-cp.myshopify.com/admin/api/2026-01"
WHATSAPP = "+54 9 11 5376-7293"
VENV = os.path.expanduser("~/Claude/mcp/fbads/.venv/bin/python")

TOQUES = [("t1", 2), ("t2", 20), ("t3", 44)]


def tok(nombre):
    try:
        for l in open(SECRETS, encoding="utf-8"):
            if l.startswith(nombre + "="):
                return l.split("=", 1)[1].strip()
    except Exception:
        pass
    return None


def traer(ruta):
    t = tok("SHOPIFY_ACCESS_TOKEN")
    if not t:
        return {}
    r = urllib.request.Request(API + ruta, headers={"X-Shopify-Access-Token": t})
    try:
        with urllib.request.urlopen(r, timeout=30) as resp:
            return json.loads(resp.read().decode())
    except Exception:
        return {}


def borrador(para, asunto, cuerpo):
    codigo = f'''
import asyncio, json
from fastmcp import Client
async def main():
    async with Client("http://localhost:8000/mcp") as c:
        r = await c.call_tool("draft_gmail_message", {{
            "user_google_email": "gonvra0@gmail.com",
            "to": {json.dumps(para)},
            "subject": {json.dumps(asunto)},
            "body": {json.dumps(cuerpo)}}})
        print("OK" if r.content else "FALLO")
asyncio.run(main())
'''
    try:
        r = subprocess.run([VENV, "-c", codigo], capture_output=True,
                           text=True, timeout=120)
        return "OK" in r.stdout
    except Exception:
        return False


def texto(toque, nombre, items, link):
    hola = f"Hola {nombre}," if nombre else "Hola,"
    if toque == "t1":
        return ("Te quedó algo en el carrito", f"""{hola}

Te escribo de GONVRA. Vi que dejaste tu pedido por la mitad.

Si tuviste algún problema con el pago o te quedó una duda del producto,
respondeme este mail y te ayudo.

Si querés retomarlo:
{link}

También estoy por WhatsApp: {WHATSAPP}

Matías — GONVRA""")
    if toque == "t2":
        return ("¿Te quedó alguna duda?", f"""{hola}

Te dejo las tres preguntas que más me hacen, por si alguna es la tuya:

1. ¿Sirve para el cuerpo además de la cara? Sí, está pensada para las dos cosas.
2. ¿Cuánto tarda en llegar? De 12 a 20 días, con envío gratis y seguimiento.
3. ¿Y si no me convence? Tenés 10 días de garantía y 10 para arrepentirte.

Tu pedido sigue disponible acá:
{link}

Matías — GONVRA""")
    return ("Último mensaje por tu pedido", f"""{hola}

Este es el último mail que te mando por esto, no quiero ser pesado.

Si te sirve: la rasuradora viene en pack individual, dúo y trío.
El dúo y el trío tienen mejor precio por unidad y a veces conviene si
lo compartís con alguien.

{link}

Y si ya no te interesa, ignorá este mail tranquilo.

Matías — GONVRA""")


def main():
    try:
        hechos = json.load(open(MEMORIA))
    except Exception:
        hechos = {}

    checkouts = traer("/checkouts.json?limit=100").get("checkouts", [])
    pedidos = traer("/orders.json?status=any&limit=100").get("orders", [])
    mails_que_compraron = {(o.get("email") or "").lower() for o in pedidos}

    ahora = datetime.now(timezone.utc)
    avisos = []

    for c in checkouts:
        mail = (c.get("email") or "").strip()
        if not mail:
            continue
        cid = str(c.get("id"))

        # ¿ya compró? -> cortar la secuencia
        if mail.lower() in mails_que_compraron:
            if not hechos.get(f"{cid}:convertido"):
                hechos[f"{cid}:convertido"] = ahora.isoformat()
                avisos.append(f"CARRITO RECUPERADO\n\n{mail} terminó comprando.\n"
                              f"Se corta la secuencia de recuperación.")
            continue

        try:
            creado = datetime.fromisoformat(
                (c.get("created_at") or "").replace("Z", "+00:00"))
        except ValueError:
            continue
        horas = (ahora - creado).total_seconds() / 3600
        if horas > 24 * 7:
            continue  # ya está frío

        cli = c.get("customer") or {}
        nombre = (cli.get("first_name") or "").strip()
        items = ", ".join(f"{li.get('quantity')}x {li.get('title')}"
                          for li in (c.get("line_items") or []))
        link = c.get("abandoned_checkout_url") or ""
        plata = float(c.get("total_price") or 0)

        for toque, cuando in TOQUES:
            clave = f"{cid}:{toque}"
            if clave in hechos or horas < cuando:
                continue
            asunto, cuerpo = texto(toque, nombre, items, link)
            ok = borrador(mail, asunto, cuerpo)
            hechos[clave] = ahora.isoformat()
            avisos.append(
                f"RESCATE DE CARRITO — toque {toque[-1]} de 3\n\n"
                f"{mail} · ${plata:,.2f} · hace {int(horas)} h\n"
                f"Tenía: {items}\n\n"
                f"Asunto: {asunto}\n"
                f"{'Borrador listo en Gmail' if ok else 'NO se pudo crear el borrador'}\n\n"
                f"Revisalo y mandalo vos.")
            break  # un solo toque por corrida

    json.dump(hechos, open(MEMORIA, "w"))

    for a in avisos[:5]:
        print(a)
        print()
        print("─" * 40)
        print()
    return 0


if __name__ == "__main__":
    sys.exit(main())
