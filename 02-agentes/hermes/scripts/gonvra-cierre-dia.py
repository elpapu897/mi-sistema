#!/usr/bin/env python3
"""
GONVRA — Cierre del día (idea J).

Junta todo en un solo lugar y lo deja escrito para que el JEFE lo use
en su resumen de las 21:00 (en vez de mandarte un mensaje aparte).

La métrica principal NO son las ventas: es cuántas piezas publicaste
de las que el equipo dejó listas. Con 0 tráfico, publicar es lo único
que mueve la aguja.
"""
import json
import os
import sqlite3
import sys
import urllib.request
from datetime import date, datetime, timedelta

SECRETS = os.path.expanduser("~/.hermes/.gonvra-secrets.env")
SALIDA = os.path.expanduser("~/Claude/gonvra2/jefe")
PUB = os.path.expanduser("~/GONVRA-PUBLICAR")
N8NDB = os.path.expanduser("~/.n8n/database.sqlite")
API = "https://jm60sa-cp.myshopify.com/admin/api/2026-01"


def tok(nombre):
    try:
        for l in open(SECRETS, encoding="utf-8"):
            if l.startswith(nombre + "="):
                return l.split("=", 1)[1].strip()
    except Exception:
        pass
    return None


def shopify(ruta):
    t = tok("SHOPIFY_ACCESS_TOKEN")
    if not t:
        return {}
    r = urllib.request.Request(API + ruta, headers={"X-Shopify-Access-Token": t})
    try:
        with urllib.request.urlopen(r, timeout=30) as resp:
            return json.loads(resp.read().decode())
    except Exception:
        return {}


def instagram():
    t = tok("INSTAGRAM_ACCESS_TOKEN")
    if not t:
        return None
    try:
        u = f"https://graph.instagram.com/v23.0/me?fields=media_count&access_token={t}"
        with urllib.request.urlopen(u, timeout=20) as r:
            return json.loads(r.read().decode()).get("media_count")
    except Exception:
        return None


def contar(carpeta, desde=None):
    p = os.path.join(PUB, carpeta)
    if not os.path.isdir(p):
        return 0
    n = 0
    for x in os.listdir(p):
        if x.endswith(".txt"):
            continue
        if desde:
            try:
                if os.path.getmtime(os.path.join(p, x)) < desde:
                    continue
            except Exception:
                continue
        n += 1
    return n


def errores_n8n():
    try:
        c = sqlite3.connect(f"file:{N8NDB}?mode=ro", uri=True)
        desde = (datetime.now() - timedelta(hours=24)).strftime("%Y-%m-%d %H:%M:%S")
        n = c.execute(
            """select count(*) from execution_entity
               where status not in ('success','running','waiting','new')
                 and startedAt > ?""", (desde,)).fetchone()[0]
        c.close()
        return n
    except Exception:
        return 0


def main():
    hoy = date.today()
    inicio = datetime.combine(hoy, datetime.min.time()).timestamp()
    hoy_iso = hoy.isoformat()

    ords = shopify("/orders.json?status=any&limit=250").get("orders", [])
    chks = shopify("/checkouts.json?limit=250").get("checkouts", [])
    del_dia = [o for o in ords if (o.get("created_at") or "")[:10] == hoy_iso]
    plata = lambda a: sum(float(o.get("total_price") or 0) for o in a)

    publicadas = contar("3-PUBLICADO", inicio)
    pendientes = contar("1-PENDIENTE")
    aprobadas = contar("2-APROBADO")
    descartadas = contar("0-DESCARTADO", inicio)
    listas = publicadas + pendientes + aprobadas + descartadas

    L = [
        f"# Cierre del día — {hoy.strftime('%d/%m/%Y')}",
        "",
        "## Lo que importa hoy: ¿salió contenido?",
        "",
        f"- **Publicadas hoy: {publicadas}** de {listas} piezas que el equipo dejó listas",
        f"- Esperando tu OK: **{pendientes}**",
        f"- Aprobadas sin publicar aún: {aprobadas}",
        f"- Descartadas hoy: {descartadas}",
    ]
    ig = instagram()
    if ig is not None:
        L.append(f"- Total en @gonvra1: **{ig} publicaciones**")

    L += ["", "## Plata", ""]
    L += [
        f"- Ventas hoy: **{len(del_dia)}** (${plata(del_dia):,.2f})",
        f"- Ventas totales: {len(ords)} (${plata(ords):,.2f})",
        f"- Carritos con mail sin cerrar: {len([c for c in chks if c.get('email')])} "
        f"(${plata([c for c in chks if c.get('email')]):,.2f})",
    ]

    err = errores_n8n()
    L += ["", "## Salud", "",
          f"- Automatizaciones falladas en 24 h: {err}" if err
          else "- Automatizaciones: sin fallas en 24 h"]

    L += ["", "## Lectura", ""]
    if publicadas == 0 and pendientes > 0:
        L.append(f"⚠️ Hoy **no salió nada**, y hay **{pendientes} pieza(s) esperando**. "
                 "El contenido está hecho; lo que falta es aprobarlo. "
                 "Los links de publicar llegan por Telegram cada 30 min.")
    elif publicadas == 0 and pendientes == 0:
        L.append("⚠️ Hoy no salió nada y **la cola está vacía**. "
                 "Revisar si los agentes de contenido dejaron entregable.")
    elif len(del_dia) == 0:
        L.append(f"Salieron {publicadas} pieza(s) y no hubo ventas. "
                 "Es lo esperable al principio: el alcance tarda. "
                 "Lo que no se puede dejar de hacer es publicar todos los días.")
    else:
        L.append(f"Salieron {publicadas} pieza(s) y entraron {len(del_dia)} venta(s). "
                 "Anotá qué se publicó: eso es lo que hay que repetir.")

    os.makedirs(SALIDA, exist_ok=True)
    ruta = os.path.join(SALIDA, f"{hoy_iso}-cierre.md")
    with open(ruta, "w", encoding="utf-8") as f:
        f.write("\n".join(L) + "\n")

    # No manda Telegram: el JEFE lo levanta a las 21:00 (no duplicar avisos)
    print(f"cierre guardado en jefe/{os.path.basename(ruta)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
