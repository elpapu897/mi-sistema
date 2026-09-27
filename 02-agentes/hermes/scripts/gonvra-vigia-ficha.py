#!/usr/bin/env python3
"""
GONVRA — Vigía de la ficha de producto (idea F).

Guarda una foto del producto (precio, título, stock, imágenes, estado)
y avisa si algo cambió. Protege contra que una app, el tema o una edición
distraída rompan la ficha sin que nadie se entere.

Alerta ROJA si el precio baja lo suficiente para romper el margen.
Silencio si no cambió nada.
"""
import json
import os
import sys
import urllib.request

SECRETS = os.path.expanduser("~/.hermes/.gonvra-secrets.env")
MEMORIA = os.path.expanduser("~/.hermes/gonvra-ficha.json")
API = "https://jm60sa-cp.myshopify.com/admin/api/2026-01"

COSTO = 8672.90          # costo real del producto
MARGEN_MINIMO = 0.55     # por debajo de esto, se enciende la alarma


def tok():
    try:
        for l in open(SECRETS, encoding="utf-8"):
            if l.startswith("SHOPIFY_ACCESS_TOKEN="):
                return l.split("=", 1)[1].strip()
    except Exception:
        pass
    return None


def foto_actual():
    t = tok()
    if not t:
        return None
    r = urllib.request.Request(API + "/products.json?limit=50",
                               headers={"X-Shopify-Access-Token": t})
    try:
        with urllib.request.urlopen(r, timeout=30) as resp:
            productos = json.loads(resp.read().decode()).get("products", [])
    except Exception:
        return None

    out = {}
    for p in productos:
        v = (p.get("variants") or [{}])[0]
        out[str(p.get("id"))] = {
            "titulo": p.get("title"),
            "estado": p.get("status"),
            "precio": float(v.get("price") or 0),
            "comparar": float(v.get("compare_at_price") or 0),
            "stock": v.get("inventory_quantity"),
            "imagenes": len(p.get("images") or []),
            "handle": p.get("handle"),
        }
    return out


def main():
    actual = foto_actual()
    if actual is None:
        return 0

    primera = not os.path.exists(MEMORIA)
    try:
        antes = json.load(open(MEMORIA))
    except Exception:
        antes = {}

    json.dump(actual, open(MEMORIA, "w"))
    if primera or not antes:
        return 0

    alertas, rojas = [], []

    for pid, a in actual.items():
        b = antes.get(pid)
        if not b:
            alertas.append(f"PRODUCTO NUEVO: {a['titulo']} — ${a['precio']:,.2f}")
            continue

        if a["precio"] != b["precio"]:
            margen = (a["precio"] - COSTO) / a["precio"] if a["precio"] else 0
            linea = (f"PRECIO: {a['titulo'][:40]}\n"
                     f"  de ${b['precio']:,.2f} a ${a['precio']:,.2f} "
                     f"(margen {margen*100:.0f}%)")
            if margen < MARGEN_MINIMO:
                rojas.append(linea + f"\n  << EL MARGEN BAJO DEL {MARGEN_MINIMO*100:.0f}% >>")
            else:
                alertas.append(linea)

        if a["estado"] != b["estado"]:
            linea = f"ESTADO: {a['titulo'][:40]} pasó de {b['estado']} a {a['estado']}"
            (rojas if a["estado"] != "active" else alertas).append(linea)

        if a["titulo"] != b["titulo"]:
            alertas.append(f"TITULO cambió:\n  antes: {b['titulo']}\n  ahora: {a['titulo']}")

        if a["imagenes"] != b["imagenes"]:
            linea = f"IMAGENES: {a['titulo'][:40]} pasó de {b['imagenes']} a {a['imagenes']}"
            (rojas if a["imagenes"] < b["imagenes"] else alertas).append(linea)

        if a["handle"] != b["handle"]:
            rojas.append(f"CAMBIO EL LINK del producto: /{b['handle']} -> /{a['handle']}\n"
                         f"  Todo link publicado antes quedó ROTO.")

    for pid, b in antes.items():
        if pid not in actual:
            rojas.append(f"DESAPARECIO UN PRODUCTO: {b['titulo']}")

    if not alertas and not rojas:
        return 0

    if rojas:
        print("ALERTA EN LA FICHA DE PRODUCTO")
        print()
        for r in rojas:
            print(r)
            print()

    if alertas:
        print("Otros cambios" if rojas else "CAMBIOS EN LA FICHA DE PRODUCTO")
        print()
        for a in alertas:
            print(a)
            print()

    if rojas:
        print("Revisalo YA en Shopify: esto puede estar costando ventas.")
    else:
        print("Si los hiciste vos, ignoralo.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
