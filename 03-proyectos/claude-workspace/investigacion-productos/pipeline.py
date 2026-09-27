#!/usr/bin/env python3
"""Normaliza, clasifica, filtra y puntua productos de salud / belleza /
cuidado personal segun los 5 criterios pedidos.

Regla de oro de este archivo: NUNCA inventar un dato.
Cada campo de salida se marca con su origen:
  DATO   = viene del catalogo, es verificable
  MODELO = lo calculo yo con un supuesto explicito y editable
  N/D    = no esta disponible en la fuente; se dice, no se rellena

Entradas soportadas:
  - raw.jsonl            (recolector de AliExpress = catalogo base de AutoDS)
  - --csv export.csv     (exportacion de AutoDS; detecta columnas sola)
"""
import json, os, re, sys, csv, math, argparse, unicodedata, collections

BASE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(BASE, "raw.jsonl")
OUT = os.path.join(BASE, "products.json")

FX_USD_ARS = 1497.4528   # oficial, 2026-08-23

# Supuesto de markup por tipo de producto. Es EDITABLE desde el dashboard.
MARKUP = {"dispositivo": 3.6, "herramienta": 3.0, "consumible": 2.5}


def norm(s):
    """minusculas sin acentos, para matchear ES e EN por igual"""
    s = (s or "").lower()
    s = unicodedata.normalize("NFD", s)
    return "".join(c for c in s if unicodedata.category(c) != "Mn")


NICHOS = {
    "Rostro y piel": ["facial", "rostro", "cara", "face", "skin", "piel", "acne",
        "poro", "pore", "blackhead", "punto negro", "espinilla", "arruga", "wrinkle",
        "colageno", "lifting", "microcorriente", "microcurrent", "dermabrasion",
        "exfolia", "gua sha", "jade", "mascarilla led", "led mask", "foton", "photon",
        "radiofrecuencia", "papada", "limpiador facial", "serum facial"],
    "Cabello y cuero cabelludo": ["cabello", "hair", "pelo", "scalp", "cuero cabelludo",
        "barba", "beard", "capilar", "alopecia", "calvicie", "caspa"],
    "Dolor y postura": ["dolor", "pain", "postura", "posture", "masajeador", "massage",
        "cervical", "espalda", "back", "rodilla", "knee", "muscular", "muscle", "tens",
        "lumbar", "fascitis", "plantar", "juanete", "bunion", "tunel carpiano",
        "carpal", "hombro", "shoulder", "ciatica"],
    "Sueno y ansiedad": ["ronquido", "snor", "sueno", "sleep", "insomnio", "antifaz",
        "ansiedad", "anxiety", "fidget", "respiracion", "breathing", "ruido blanco",
        "white noise", "relajacion"],
    "Higiene y cuidado personal": ["oido", "ear", "cerumen", "wax", "dental", "diente",
        "teeth", "encia", "blanqueamiento", "whitening", "irrigador", "floss", "lengua",
        "tongue", "una", "nail", "hongo", "fungus", "callo", "callus", "pie", "foot",
        "sarro", "nariz", "afeitar", "trimmer"],
    "Depilacion y cuerpo": ["depila", "hair removal", "ipl", "epilator", "celulitis",
        "cellulite", "linfatico", "lymphatic", "moldea", "sculpt", "adelgaz"],
    "Salud femenina": ["menstrual", "periodo", "period", "pelvic", "pelvico", "lactancia",
        "breast pump", "postparto", "postpartum", "vaginal", "utero"],
    "Ojos y vista": ["ojo", "eye", "ojera", "parpado", "eyelid", "vista", "lagrima"],
    "Medicion y salud general": ["presion", "blood pressure", "oximetro", "oximeter",
        "termometro", "thermometer", "glucosa", "glucose", "nebulizador", "nebulizer",
        "audifono", "hearing", "bascula", "saturacion", "cardiaco"],
}

# --- tipo de producto: define el valor percibido (criterio 3) ---
T_DISPOSITIVO = ["electrico", "electric", "led", "laser", "ipl", "ems", "ultrasonic",
    "ultrasonido", "microcorriente", "microcurrent", "recargable", "rechargeable",
    "usb", "digital", "inteligente", "smart", "dispositivo", "device", "maquina",
    "machine", "monitor", "camara", "camera", "foton", "photon", "radiofrecuencia",
    "vibra", "bateria", "battery", "electronico", "motorizado"]
T_HERRAMIENTA = ["rodillo", "roller", "gua sha", "pinza", "tweezer", "cepillo", "brush",
    "raspador", "scraper", "corrector", "brace", "faja", "soporte", "ventosa", "cup",
    "bola", "ball", "kit", "herramienta", "tool", "lima", "file", "espatula",
    "extractor", "separador", "plantilla", "insole"]
T_CONSUMIBLE = ["parche", "patch", "serum", "suero", "crema", "cream", "aceite", "oil",
    "tira", "strip", "gel", "polvo", "powder", "ampolla", "locion", "lotion", "shampoo",
    "champu", "mascarilla desechable", "pasta", "jabon", "soap"]

# criterio 2: se consigue en supermercado / farmacia -> penaliza fuerte
COMMODITY = ["parche", "patch", "tira nasal", "nose strip", "crema", "cream", "serum",
    "aceite", "oil", "algodon", "cotton", "curita", "bandage", "shampoo", "champu",
    "jabon", "soap", "hisopo", "cotonete", "pasta dental", "toothpaste", "esponja",
    "sponge", "locion", "lotion", "desodorante", "talco", "vendaje", "gasa",
    "cepillo de dientes", "toothbrush", "pinza de cejas", "lima de unas"]

# criterio 4: bulto / peso -> complica el envio
VOLUMINOSO = ["colchoneta", "mat", "almohada", "pillow", "cojin", "cushion", "silla",
    "chair", "manta", "blanket", "bascula", "scale", "banco", "tabla", "board",
    "foam roller", "bicicleta", "stepper", "cinta"]


def clasificar_nicho(t):
    t = norm(t)
    best, hits = "Otros", 0
    for n, kws in NICHOS.items():
        h = sum(1 for k in kws if k in t)
        if h > hits:
            best, hits = n, h
    return best


def clasificar_tipo(t):
    t = norm(t)
    d = sum(1 for k in T_DISPOSITIVO if k in t)
    h = sum(1 for k in T_HERRAMIENTA if k in t)
    c = sum(1 for k in T_CONSUMIBLE if k in t)
    if d and d >= h and d >= c:
        return "dispositivo"
    if c and c > h:
        return "consumible"
    if h:
        return "herramienta"
    return "herramienta"


def parse_sold(s):
    """'10.000+ vendidos' / '1,000+ sold' / '2 mil+' -> int. None si no hay dato."""
    if not s:
        return None
    t = norm(str(s))
    m = re.search(r"([\d.,]+)\s*(mil|k)?", t)
    if not m:
        return None
    num = m.group(1).replace(".", "").replace(",", "")
    if not num.isdigit():
        return None
    n = int(num)
    if m.group(2):
        n *= 1000
    return n


def a_usd(price, currency, tax_rate):
    """Devuelve (usd, exacto?). El precio ARS de AliExpress para Argentina trae
    impuesto local incluido, asi que se descuenta para llegar al costo real."""
    if price is None:
        return None, False
    if currency == "USD":
        return round(float(price), 2), True
    if currency == "ARS":
        try:
            tr = float(tax_rate) if tax_rate else 0.0
        except Exception:
            tr = 0.0
        return round(float(price) / (1 + tr) / FX_USD_ARS, 2), False
    return None, False


# ---------------- carga ----------------

def cargar_jsonl(path):
    filas = []
    if not os.path.exists(path):
        return filas
    for line in open(path, encoding="utf-8"):
        line = line.strip()
        if not line:
            continue
        try:
            r = json.loads(line)
        except Exception:
            continue
        # COSTE CONSERVADOR: el precio de lista, no el promocional.
        # El 74% del catalogo esta con >=50% off por evento de venta temporal;
        # usar ese precio infla el margen al doble. Si el negocio cierra al
        # precio de lista, cierra siempre.
        usd_promo, exacto = a_usd(r.get("price"), r.get("currency"), r.get("tax_rate"))
        usd_lista, _ = a_usd(r.get("original_price"), r.get("currency"), r.get("tax_rate"))
        usd = usd_lista if usd_lista else usd_promo
        srcs = " ".join(r.get("sp_sources") or [])
        txts = " ".join(r.get("sp_texts") or [])
        filas.append({
            "id": str(r.get("id")),
            "titulo": r.get("title", ""),
            "url": r.get("url", ""),
            "imagen": r.get("image", ""),
            "coste_usd": usd,
            "coste_promo": usd_promo,
            "coste_exacto": exacto,
            "vendidos": parse_sold(r.get("sold_raw")),
            "rating": r.get("rating"),
            "descuento": r.get("discount") or 0,
            "choice": "choice" in srcs.lower(),
            "envio_gratis": "freeshipping" in srcs.lower().replace("_", ""),
            "mas_vendido": ("top ventas" in norm(txts)) or ("best" in norm(txts)),
            "lanzamiento": r.get("launch"),
            "categoria": r.get("query", ""),
            "fuente": "AliExpress (catalogo base AutoDS)",
        })
    return filas


CSV_MAP = {
    "titulo": ["title", "product name", "name", "producto", "titulo"],
    "coste_usd": ["cost", "buy price", "supplier price", "item cost", "costo", "coste", "price"],
    "vendidos": ["sold", "orders", "sales", "vendidos", "ventas", "order count"],
    "rating": ["rating", "stars", "valoracion", "puntuacion"],
    "url": ["url", "link", "product url", "enlace"],
    "imagen": ["image", "img", "imagen", "main image"],
    "envio_dias": ["shipping time", "delivery time", "envio", "shipping days"],
    "id": ["id", "product id", "sku", "item id"],
}


def cargar_csv(path):
    filas = []
    with open(path, encoding="utf-8-sig", newline="") as f:
        sample = f.read(8192); f.seek(0)
        try:
            dialect = csv.Sniffer().sniff(sample, delimiters=",;\t|")
        except Exception:
            dialect = csv.excel
        rd = csv.DictReader(f, dialect=dialect)
        cols = {norm(c): c for c in (rd.fieldnames or [])}
        res = {}
        for campo, alias in CSV_MAP.items():
            for a in alias:
                for cn, orig in cols.items():
                    if a == cn or a in cn:
                        res[campo] = orig
                        break
                if campo in res:
                    break
        sys.stderr.write(f"CSV: columnas detectadas -> {res}\n")
        for i, row in enumerate(rd):
            def g(k):
                c = res.get(k)
                return row.get(c) if c else None
            raw_cost = g("coste_usd")
            try:
                cost = round(float(re.sub(r"[^\d.]", "", str(raw_cost or ""))), 2)
            except Exception:
                cost = None
            try:
                rat = float(str(g("rating")).replace(",", "."))
            except Exception:
                rat = None
            filas.append({
                "id": str(g("id") or f"csv{i}"),
                "titulo": g("titulo") or "",
                "url": g("url") or "",
                "imagen": g("imagen") or "",
                "coste_usd": cost,
                "coste_exacto": True,
                "vendidos": parse_sold(g("vendidos")),
                "rating": rat,
                "descuento": 0,
                "choice": False,
                "envio_gratis": False,
                "mas_vendido": False,
                "lanzamiento": None,
                "categoria": "",
                "envio_dias_dato": g("envio_dias"),
                "fuente": "Exportacion AutoDS",
            })
    return filas


# ---------------- scoring ----------------

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--csv", help="exportacion CSV de AutoDS")
    ap.add_argument("--min-cost", type=float, default=5.0)
    ap.add_argument("--max-cost", type=float, default=30.0)
    ap.add_argument("--min-sold", type=int, default=50)
    ap.add_argument("--top", type=int, default=50)
    a = ap.parse_args()

    filas = cargar_csv(a.csv) if a.csv else cargar_jsonl(RAW)

    # dedup por id
    seen = {}
    for r in filas:
        seen.setdefault(r["id"], r)
    filas = list(seen.values())
    total_crudo = len(filas)

    # --- competencia REAL medible: cuantos listados PROBADOS (>=100 ventas)
    #     compiten en la misma categoria dentro del corpus relevado ---
    probados = collections.Counter()
    for r in filas:
        if (r.get("vendidos") or 0) >= 100:
            probados[r.get("categoria", "")] += 1

    descartes = collections.Counter()
    out = []
    for r in filas:
        c = r.get("coste_usd")
        v = r.get("vendidos")
        rt = r.get("rating")
        t = r["titulo"]

        # --- criterio 4: coste 5-30 USD ---
        if c is None:
            descartes["sin precio"] += 1; continue
        if not (a.min_cost <= c <= a.max_cost):
            descartes["fuera de rango 5-30 USD"] += 1; continue
        # --- criterio 5: YA vende (dato duro, no se adivina) ---
        if v is None:
            descartes["sin dato de ventas"] += 1; continue
        if v < a.min_sold:
            descartes["ventas insuficientes"] += 1; continue
        # calidad minima verificable
        if rt is not None and rt < 4.2:
            descartes["rating bajo"] += 1; continue

        nt = norm(t)
        tipo = clasificar_tipo(t)
        nicho = clasificar_nicho(t)
        mult = MARKUP[tipo]
        pvp = round(c * mult, 2)

        es_commodity = any(k in nt for k in COMMODITY)
        es_voluminoso = any(k in nt for k in VOLUMINOSO)
        comp = probados.get(r.get("categoria", ""), 0)

        # ---- componentes del score (0-100) ----
        s_demanda = min(30, 30 * math.log10(v + 1) / math.log10(20000))
        s_calidad = ((rt - 4.2) / 0.8 * 15) if rt is not None else 6.0
        s_calidad = max(0, min(15, s_calidad))
        s_valor = {"dispositivo": 20, "herramienta": 13, "consumible": 6}[tipo]
        s_dif = 0 if es_commodity else 15
        s_log = (4 if not es_voluminoso else 0) + (3 if r.get("choice") else 0) \
                + (3 if r.get("envio_gratis") else 0)
        s_comp = 10 * (1 - min(comp, 40) / 40)
        score = s_demanda + s_calidad + s_valor + s_dif + s_log + s_comp
        score = round(max(0, min(100, score)), 1)

        comp_txt = "Baja" if comp <= 8 else ("Media" if comp <= 20 else "Alta")
        envio_txt = "Rapido (Choice)" if r.get("choice") else "Estandar"
        if r.get("envio_dias_dato"):
            envio_txt = str(r["envio_dias_dato"])

        # ---- nota final, construida SOLO con datos reales ----
        n = []
        n.append(f"{v:,}".replace(",", ".") + " ventas confirmadas")
        n.append(f"{rt}★" if rt is not None else "sin rating publicado")
        n.append({"dispositivo": "dispositivo electronico (valor percibido alto)",
                  "herramienta": "herramienta reutilizable (valor percibido medio)",
                  "consumible": "consumible (valor percibido bajo)"}[tipo])
        if es_commodity:
            n.append("OJO: se consigue en farmacia/super, incumple tu criterio 2")
        if es_voluminoso:
            n.append("OJO: voluminoso, encarece el envio")
        if r.get("choice"):
            n.append("etiqueta Choice = envio mas rapido y fiable")
        n.append(f"competencia {comp_txt.lower()} ({comp} listados probados en su categoria)")
        if not r.get("coste_exacto"):
            n.append("costo estimado desde precio en ARS")
        nota = ". ".join(n) + "."

        out.append({
            "id": r["id"], "titulo": t[:130], "nicho": nicho, "tipo": tipo,
            "categoria": r.get("categoria", ""),
            "coste": c, "coste_promo": r.get("coste_promo"),
            "coste_exacto": r.get("coste_exacto", True),
            "markup": mult, "pvp_sugerido": pvp,
            "margen_usd": round(pvp - c, 2),
            "margen_pct": round((pvp - c) / pvp * 100, 1) if pvp else 0,
            "vendidos": v, "rating": rt,
            "competencia": comp_txt, "competidores": comp,
            "envio": envio_txt, "choice": bool(r.get("choice")),
            "envio_gratis": bool(r.get("envio_gratis")),
            "commodity": es_commodity, "voluminoso": es_voluminoso,
            "score": score, "nota": nota,
            "url": r.get("url", ""), "imagen": r.get("imagen", ""),
            "fuente": r.get("fuente", ""),
        })

    out.sort(key=lambda x: -x["score"])
    top = out[:a.top]

    meta = {
        "generado": "2026-08-23",
        "fuente": (f"Exportacion AutoDS ({os.path.basename(a.csv)})" if a.csv
                   else "AliExpress - catalogo base de AutoDS"),
        "fx_usd_ars": FX_USD_ARS,
        "markup_supuesto": MARKUP,
        "total_crudo": total_crudo,
        "total_filtrado": len(out),
        "entregados": len(top),
        "descartes": dict(descartes),
        "procedencia": {
            "DATO": ["coste", "vendidos", "rating", "descuento", "choice",
                     "envio_gratis", "categoria"],
            "MODELO": ["markup", "pvp_sugerido", "margen_usd", "margen_pct",
                       "competencia", "score", "nicho", "tipo"],
            "N/D": ["dias exactos de envio (no los publica el buscador del catalogo; "
                    "se confirman en la ficha de AutoDS)"],
        },
        "productos": top,
    }
    json.dump(meta, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"crudo={total_crudo} | pasan={len(out)} | entregados={len(top)}")
    print("descartes:", dict(descartes))


if __name__ == "__main__":
    main()
