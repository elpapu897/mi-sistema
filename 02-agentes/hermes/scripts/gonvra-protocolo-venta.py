#!/usr/bin/env python3
"""
GONVRA — Protocolo de venta (idea D).

Para cada pedido, según los días que pasaron:
  · día 0  -> si es la PRIMERA VENTA de la historia, mensaje especial con
              qué se publicó los 7 días previos (única atribución sin ads)
  · día 3  -> si no se despachó, recordatorio
  · día 10 -> aviso de que toca pedir reseña (la posventa arma el borrador)

Cada aviso se manda UNA sola vez. Silencio si no hay nada.
"""
import json
import os
import subprocess
import sys
import urllib.request
from datetime import datetime, timedelta, timezone

SECRETS = os.path.expanduser("~/.hermes/.gonvra-secrets.env")
MEMORIA = os.path.expanduser("~/.hermes/gonvra-protocolo-venta.json")
PUBLICADO = os.path.expanduser("~/GONVRA-PUBLICAR/3-PUBLICADO")
API = "https://jm60sa-cp.myshopify.com/admin/api/2026-01"
CPA_TECHO = 7129


def tok(nombre):
    try:
        for l in open(SECRETS, encoding="utf-8"):
            if l.startswith(nombre + "="):
                return l.split("=", 1)[1].strip()
    except Exception:
        pass
    return None


def pedidos():
    t = tok("SHOPIFY_ACCESS_TOKEN")
    if not t:
        return []
    r = urllib.request.Request(API + "/orders.json?status=any&limit=100",
                               headers={"X-Shopify-Access-Token": t})
    try:
        with urllib.request.urlopen(r, timeout=30) as resp:
            return json.loads(resp.read().decode()).get("orders", [])
    except Exception:
        return []


def publicado_ultimos_dias(dias=7):
    """Qué contenido salió: es la única atribución que tenemos sin ads."""
    if not os.path.isdir(PUBLICADO):
        return []
    corte = datetime.now().timestamp() - dias * 86400
    out = []
    for n in os.listdir(PUBLICADO):
        p = os.path.join(PUBLICADO, n)
        try:
            if os.path.getmtime(p) >= corte and not n.endswith(".txt"):
                cuando = datetime.fromtimestamp(os.path.getmtime(p))
                out.append(f"{cuando.strftime('%d/%m %H:%M')}  {n}")
        except Exception:
            pass
    return sorted(out, reverse=True)


def fmt(n):
    return "$" + f"{float(n or 0):,.2f}"


def main():
    try:
        hechos = json.load(open(MEMORIA))
    except Exception:
        hechos = {}

    ords = pedidos()
    if not ords:
        return 0

    ahora = datetime.now(timezone.utc)
    avisos = []
    total_historico = len(ords)

    for o in ords:
        oid = str(o.get("id"))
        creado = o.get("created_at")
        if not creado:
            continue
        try:
            fecha = datetime.fromisoformat(creado.replace("Z", "+00:00"))
        except ValueError:
            continue
        dias = (ahora - fecha).days

        # --- día 0: primera venta de la historia ---
        clave = f"{oid}:primera"
        if total_historico == 1 and clave not in hechos:
            piezas = publicado_ultimos_dias(7)
            lineas = [
                "PRIMERA VENTA DE GONVRA",
                "",
                f"Pedido #{o.get('order_number')} — {fmt(o.get('total_price'))}",
                "",
                "QUE SE PUBLICO LOS 7 DIAS PREVIOS",
                "(sin ads, esto es lo unico que la puede explicar):",
            ]
            lineas += ["  " + p for p in piezas[:10]] or ["  (no se publico nada)"]
            lineas += [
                "",
                f"Tu techo de CPA es {fmt(CPA_TECHO)} por venta.",
                "Como no hubo pauta, esta venta costo $0 en publicidad.",
                "",
                "Anota que contenido la trajo: eso decide que hacer mas.",
            ]
            avisos.append("\n".join(lineas))
            hechos[clave] = ahora.isoformat()

        # --- día 3: no se despachó ---
        clave = f"{oid}:despacho3"
        if dias >= 3 and not o.get("fulfillment_status") and clave not in hechos:
            avisos.append(
                f"PEDIDO SIN DESPACHAR\n\n"
                f"#{o.get('order_number')} ({fmt(o.get('total_price'))}) lleva "
                f"{dias} dias sin marcarse como enviado.\n\n"
                f"Si ya lo mandaste, marcalo en Shopify para que el cliente "
                f"reciba el seguimiento.")
            hechos[clave] = ahora.isoformat()

        # --- día 10: toca reseña ---
        clave = f"{oid}:resena"
        if dias >= 10 and clave not in hechos:
            avisos.append(
                f"TOCA PEDIR RESENA\n\n"
                f"El pedido #{o.get('order_number')} cumplio {dias} dias.\n"
                f"El borrador ya esta en Gmail (lo dejo POSVENTA a las 11).\n\n"
                f"Revisalo y mandalo: las resenas reales valen mas que "
                f"cualquier anuncio.")
            hechos[clave] = ahora.isoformat()

    json.dump(hechos, open(MEMORIA, "w"))

    if avisos:
        for a in avisos[:5]:
            print(a)
            print()
            print("─" * 40)
            print()
    return 0


if __name__ == "__main__":
    sys.exit(main())
