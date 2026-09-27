#!/usr/bin/env bash
# GONVRA — Espía los precios de la competencia (tiendas Shopify).
# Avisa SOLO cuando algo cambia: baja de precio, sube, o producto nuevo.
# Si no cambió nada, silencio. Cuesta $0 (sin IA).

python3 - <<'PY'
import json, os, urllib.request, urllib.error

LISTA   = os.path.expanduser("~/Claude/gonvra2/competencia.txt")
HISTORIA = os.path.expanduser("~/.hermes/gonvra-precios-competencia.json")

def leer_competidores():
    if not os.path.exists(LISTA):
        return []
    out = []
    for l in open(LISTA, encoding="utf-8"):
        l = l.strip()
        if l and not l.startswith("#"):
            out.append(l.rstrip("/"))
    return out

def traer(dominio):
    """Lee el catálogo público de una tienda Shopify."""
    url = f"{dominio}/products.json?limit=250"
    req = urllib.request.Request(url, headers={
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64)"})
    with urllib.request.urlopen(req, timeout=25) as r:
        return json.loads(r.read().decode())["products"]

try:
    viejo = json.load(open(HISTORIA))
except Exception:
    viejo = {}

primera = not os.path.exists(HISTORIA)
nuevo = {}
avisos = []

for dom in leer_competidores():
    try:
        productos = traer(dom)
    except Exception as e:
        # una tienda caída no es noticia; solo se avisa si es error raro
        code = getattr(e, "code", None)
        if code and code not in (404, 403, 429):
            avisos.append(f"[{dom}] no responde (HTTP {code})")
        continue

    actual = {}
    for p in productos:
        for v in p.get("variants", []):
            clave = f"{p['title']} / {v.get('title','')}".strip(" /")
            try:
                actual[clave] = float(v.get("price") or 0)
            except ValueError:
                pass
    nuevo[dom] = actual

    if primera:
        continue

    antes = viejo.get(dom, {})
    if not antes:
        continue

    # productos nuevos
    agregados = [k for k in actual if k not in antes]
    for k in agregados[:5]:
        avisos.append(f"[{dom}] PRODUCTO NUEVO: {k} - ${actual[k]:,.2f}")

    # cambios de precio
    for k, precio in actual.items():
        if k in antes and abs(precio - antes[k]) > 0.01:
            dif = precio - antes[k]
            pct = (dif / antes[k] * 100) if antes[k] else 0
            flecha = "BAJO" if dif < 0 else "SUBIO"
            avisos.append(
                f"[{dom}] {flecha} {abs(pct):.0f}%: {k}\n"
                f"    de ${antes[k]:,.2f} a ${precio:,.2f}")

    # productos que sacaron
    sacados = [k for k in antes if k not in actual]
    for k in sacados[:3]:
        avisos.append(f"[{dom}] DEJO DE VENDER: {k}")

with open(HISTORIA, "w") as f:
    json.dump(nuevo, f)

# ESCALADA: comparar contra NUESTRO precio vivo, no solo entre ellos
MI_PRECIO = 0.0
try:
    with urllib.request.urlopen(
            "https://gonvra.com/products/face-body-electric-shaver.json",
            timeout=20) as r:
        MI_PRECIO = float(_j.loads(r.read().decode())["product"]["variants"][0]["price"])
except Exception:
    pass

quedamos_caros = []
if MI_PRECIO:
    for dom, prods in nuevo.items():
        for k, precio in prods.items():
            if precio <= 0:
                continue
            # solo productos del MISMO rubro: si no, compara una rasuradora
            # con un cortaunias y te manda ruido todos los dias
            kl = k.lower()
            ES_RASURADORA = any(w in kl for w in (
                "rasurador", "afeitador", "shaver", "recortador",
                "trimmer", "maquina"))
            NO_SIRVE = any(w in kl for w in (
                "hojilla", "repuesto", "cortaun", "bag", "envio",
                "crema", "gel", "aceite", "bolso", "kit de"))
            if not ES_RASURADORA or NO_SIRVE:
                continue
            # y en el mismo orden de magnitud
            if precio < MI_PRECIO * 0.45 or precio > MI_PRECIO * 4:
                continue
            if precio < MI_PRECIO * 0.85:
                dif = (MI_PRECIO - precio) / MI_PRECIO * 100
                quedamos_caros.append(
                    f"[{dom}] {k[:52]}\n"
                    f"    ellos ${precio:,.2f}  vs  nosotros ${MI_PRECIO:,.2f}"
                    f"  ({dif:.0f}% mas caros)")

if avisos and not primera:
    print("MOVIMIENTOS EN LA COMPETENCIA")
    print()
    for a in avisos[:20]:
        print(a)
    if len(avisos) > 20:
        print(f"... y {len(avisos)-20} cambios mas")
    print()

if quedamos_caros and not primera:
    print("QUEDAMOS CAROS FRENTE A ESTOS")
    print()
    for q in quedamos_caros[:6]:
        print(q)
    print()
    print("ANGULO DE COPY sugerido (no bajar el precio de lista):")
    print("  · Destacar que sirve para rostro Y cuerpo (no solo una zona)")
    print("  · Empujar el pack Duo/Trio, que baja el precio por unidad")
    print("  · Envio gratis con seguimiento + 10 dias de garantia")
    print()
    print("Bajar el precio de lista rompe el margen del 76%. Ese es el ultimo recurso.")

if (avisos or quedamos_caros) and not primera:
    pass
PY
exit 0
