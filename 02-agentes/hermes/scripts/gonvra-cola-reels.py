#!/usr/bin/env python3
"""
GONVRA — Cola de reels con Google Flow (idea H).

Dos partes:

1. Te manda los prompts que escribió TIKTOKER, listos para pegar en
   flow.google.com (la API de video es paga, Flow a mano es gratis).

2. Cuando dejás el .mp4 en ~/GONVRA-PUBLICAR/0-VIDEOS-CRUDOS/, lo detecta,
   le pega el guion como .txt y lo pasa a 1-PENDIENTE para que lo apruebes.

Silencio si no hay nada nuevo.
"""
import json
import os
import re
import shutil
import sys
from datetime import date

BASE = os.path.expanduser("~/Claude/gonvra2")
CRUDOS = os.path.expanduser("~/GONVRA-PUBLICAR/0-VIDEOS-CRUDOS")
PEND = os.path.expanduser("~/GONVRA-PUBLICAR/1-PENDIENTE")
MEMORIA = os.path.expanduser("~/.hermes/gonvra-reels.json")

VIDS = (".mp4", ".mov")


def ultimo_entregable(agente, patron):
    d = os.path.join(BASE, agente)
    if not os.path.isdir(d):
        return None
    archivos = sorted((f for f in os.listdir(d) if patron in f and f.endswith(".md")),
                      reverse=True)
    return os.path.join(d, archivos[0]) if archivos else None


def prompts_de(md):
    """Saca los prompts en inglés que dejó TIKTOKER."""
    t = open(md, encoding="utf-8").read()
    bloques = re.findall(r"```(?:text)?\s*\n(.+?)\n```", t, re.S)
    if bloques:
        return [b.strip() for b in bloques if len(b.strip()) > 60][:6]
    # si no vinieron en bloques de código, buscar por encabezado
    partes = re.split(r"\n#{3,4}\s+", t)[1:]
    return [p.strip()[:700] for p in partes if "SUBJECT" in p.upper()][:6]


def main():
    os.makedirs(CRUDOS, exist_ok=True)
    try:
        hechos = json.load(open(MEMORIA))
    except Exception:
        hechos = {}

    salida = []

    # ---------- parte 2 (primero): videos que ya bajaste ----------
    movidos = 0
    for n in sorted(os.listdir(CRUDOS)):
        if not n.lower().endswith(VIDS):
            continue
        origen = os.path.join(CRUDOS, n)
        destino = os.path.join(PEND, n)
        if os.path.exists(destino):
            continue
        shutil.move(origen, destino)

        # buscarle un texto: el del guion del día, o uno genérico honesto
        txt = os.path.splitext(destino)[0] + ".txt"
        if not os.path.exists(txt):
            guion = ultimo_entregable("tiktoker", date.today().isoformat())
            caption = ""
            if guion:
                g = re.search(r"\*\*Gancho[^:]*:\*\*\s*(.+)", open(guion, encoding="utf-8").read())
                if g:
                    caption = g.group(1).strip().strip('"')
            if not caption:
                caption = "Rostro y cuerpo con una sola máquina 🪒"
            caption += ("\n\nRasuradora integral recargable, con peines guía "
                        "para elegir el largo.\nEnvío gratis a todo el país.\n\n"
                        "#afeitadora #rasuradora #cuidadopersonal #barba "
                        "#grooming #argentina #reels")
            open(txt, "w", encoding="utf-8").write(caption)
        movidos += 1

    if movidos:
        salida.append(f"{movidos} VIDEO(S) LISTOS PARA APROBAR")
        salida.append("")
        salida.append("Les puse el texto y ya están en la cola.")
        salida.append("En el próximo aviso te llegan los links para publicarlos.")
        salida.append("")

    # ---------- parte 1: mandar los prompts (una vez por entregable) ----------
    md = ultimo_entregable("tiktoker", "flow")
    if md:
        clave = os.path.basename(md)
        if clave not in hechos:
            ps = prompts_de(md)
            if ps:
                hechos[clave] = True
                salida.append("PROMPTS PARA GOOGLE FLOW")
                salida.append("")
                salida.append("Entrá a flow.google.com (es gratis, con créditos diarios)")
                salida.append("y pegá estos de a uno:")
                salida.append("")
                for i, p in enumerate(ps, 1):
                    salida.append(f"--- {i} ---")
                    salida.append(p[:600])
                    salida.append("")
                salida.append("Cuando bajes los videos, dejalos acá:")
                salida.append(f"  {CRUDOS}")
                salida.append("")
                salida.append("Yo les pongo el texto y te mando el link para publicar.")

    json.dump(hechos, open(MEMORIA, "w"))

    if salida:
        print("\n".join(salida))
    return 0


if __name__ == "__main__":
    sys.exit(main())
