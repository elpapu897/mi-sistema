#!/usr/bin/env python3
"""
GONVRA — Los agentes aprenden de lo que publicaste
(idea sacada de self-improving-agent-skills).

Cruza QUÉ se publicó con CÓMO le fue (vistas, likes, comentarios de Instagram)
y escribe las conclusiones en un archivo que leen COPY, CREATIVO, TIKTOKER
e INSTAGRAMER antes de trabajar.

Así el equipo deja de escribir a ciegas: repite lo que funcionó y descarta
lo que no. Sin esto, mañana proponen lo mismo que ayer no anduvo.

Corre semanal. Si no hay suficientes publicaciones, lo dice y no inventa.
"""
import json
import os
import sys
import urllib.error
import urllib.request
from datetime import date

SECRETS = os.path.expanduser("~/.hermes/.gonvra-secrets.env")
SALIDA = os.path.expanduser("~/Claude/gonvra2/conocimiento")
ARCHIVO = os.path.join(SALIDA, "QUE-FUNCIONA.md")
API = "https://graph.instagram.com/v23.0"
MINIMO = 3  # menos que esto, no hay nada que aprender


def tok():
    try:
        for l in open(SECRETS, encoding="utf-8"):
            if l.startswith("INSTAGRAM_ACCESS_TOKEN="):
                return l.split("=", 1)[1].strip()
    except Exception:
        pass
    return None


def pedir(ruta, campos):
    t = tok()
    if not t:
        return {}
    campos["access_token"] = t
    url = f"{API}/{ruta}?" + urllib.parse.urlencode(campos)
    try:
        with urllib.request.urlopen(url, timeout=40) as r:
            return json.loads(r.read().decode())
    except Exception:
        return {}


def main():
    import urllib.parse
    globals()["urllib"].parse = urllib.parse

    d = pedir("me/media", {
        "fields": "id,caption,media_type,permalink,timestamp,like_count,comments_count",
        "limit": "50"})
    medios = d.get("data", [])

    if len(medios) < MINIMO:
        print(f"APRENDIZAJE: solo hay {len(medios)} publicacion(es).")
        print(f"Con menos de {MINIMO} no se puede sacar ninguna conclusion seria.")
        print("Publicá más y esto empieza a servir.")
        return 0

    # juntar métricas
    filas = []
    for m in medios:
        interac = (m.get("like_count") or 0) + (m.get("comments_count") or 0)
        cap = (m.get("caption") or "").strip()
        gancho = cap.split("\n")[0][:70] if cap else "(sin texto)"
        filas.append({
            "tipo": m.get("media_type", "?"),
            "fecha": (m.get("timestamp") or "")[:10],
            "gancho": gancho,
            "likes": m.get("like_count") or 0,
            "coment": m.get("comments_count") or 0,
            "total": interac,
            "link": m.get("permalink", ""),
        })

    filas.sort(key=lambda x: x["total"], reverse=True)

    # por tipo de contenido
    por_tipo = {}
    for f in filas:
        t = f["tipo"]
        por_tipo.setdefault(t, []).append(f["total"])
    resumen_tipo = sorted(
        ((t, sum(v) / len(v), len(v)) for t, v in por_tipo.items()),
        key=lambda x: x[1], reverse=True)

    hoy = date.today().isoformat()
    L = [
        "# Qué funciona en GONVRA — lo que dicen los números",
        "",
        f"*Actualizado el {hoy} · {len(filas)} publicaciones analizadas*",
        "",
        "> **Para los agentes:** leé esto ANTES de proponer contenido nuevo.",
        "> Son datos reales de @gonvra1, no opiniones.",
        "",
        "## Qué formato rinde más",
        "",
    ]
    nombres = {"IMAGE": "Foto sola", "CAROUSEL_ALBUM": "Carrusel", "VIDEO": "Reel"}
    for t, prom, n in resumen_tipo:
        L.append(f"- **{nombres.get(t, t)}**: {prom:.1f} interacciones de promedio "
                 f"({n} publicación{'es' if n > 1 else ''})")

    L += ["", "## Los que mejor anduvieron", ""]
    for f in filas[:5]:
        L.append(f"**{f['total']} interacciones** · {nombres.get(f['tipo'], f['tipo'])} · {f['fecha']}")
        L.append(f'> "{f["gancho"]}"')
        L.append("")

    if len(filas) > 5:
        L += ["## Los que peor anduvieron", ""]
        for f in filas[-3:]:
            L.append(f"**{f['total']} interacciones** · {nombres.get(f['tipo'], f['tipo'])} · {f['fecha']}")
            L.append(f'> "{f["gancho"]}"')
            L.append("")

    L += ["## Qué hacer con esto", ""]
    mejor = resumen_tipo[0]
    L.append(f"- El formato que más rinde es **{nombres.get(mejor[0], mejor[0])}**. "
             f"Hacer más de eso.")
    if filas[0]["total"] > 0:
        L.append(f"- El gancho que mejor funcionó fue: *\"{filas[0]['gancho']}\"*. "
                 "Probar variantes del mismo ángulo.")
    else:
        L.append("- **Todavía no hay interacciones.** Con este volumen no se puede "
                 "decir qué funciona: lo único que corresponde es publicar más "
                 "seguido y volver a medir.")
    L.append("")
    L.append("**Ojo:** con pocas publicaciones estos números son ruido. "
             "Recién con 15 o 20 posts las conclusiones empiezan a ser confiables.")

    os.makedirs(SALIDA, exist_ok=True)
    with open(ARCHIVO, "w", encoding="utf-8") as f:
        f.write("\n".join(L) + "\n")

    print("APRENDIZAJE ACTUALIZADO")
    print()
    print(f"{len(filas)} publicaciones analizadas.")
    print()
    for t, prom, n in resumen_tipo:
        print(f"  {nombres.get(t, t)}: {prom:.1f} interacciones de promedio ({n})")
    print()
    print("Los agentes de contenido ya lo tienen para mañana.")
    return 0


if __name__ == "__main__":
    import urllib.parse  # noqa
    sys.exit(main())
