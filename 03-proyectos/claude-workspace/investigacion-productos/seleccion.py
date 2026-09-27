#!/usr/bin/env python3
"""Selecciona los 50 mejores productos segun los 5 criterios del usuario.

Corrige el bug critico de la version anterior: AliExpress cambio la moneda de
la sesion a ARS despues de los primeros 60 productos. score.py leia esos
precios como si fueran dolares, asi que el 99% del catalogo quedaba descartado
por "caro". Tipo de cambio derivado de 6 productos capturados en ambas monedas.

Criterios:
  1. Resuelve un problema real (salud / belleza / cuidado personal)
  2. No se consigue facil en supermercado o tienda fisica
  3. Valor percibido alto -> vendible a >=3x el coste
  4. Coste 5-30 USD, pequeno y facil de enviar
  5. Ya genera ventas
"""
import json, re, os, math, ast, collections, datetime

BASE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(BASE, "raw.jsonl")
OUT = os.path.join(BASE, "productos_top50.json")

# Derivado empiricamente de 6 productos capturados en USD y ARS (ver informe).
RATE_ARS = 1497.4
HOY = datetime.date(2026, 9, 4)

# --- Criterio 1: nicho. Los que no estan aca se descartan. ---
NICHO = {
    "face shaver women facial hair":        "Depilacion",
    "hair removal razor women electric":    "Depilacion",
    "electric shaver women body":           "Depilacion",
    "epilator women rechargeable":          "Depilacion",
    "bikini trimmer women intimate":        "Cuidado intimo",
    "pubic hair trimmer men":               "Cuidado intimo",
    "manscaping groomer kit":               "Cuidado intimo",
    "trimmer ceramic blade grooming":       "Afeitado",
    "nose ear hair trimmer electric":       "Afeitado",
    "body groomer trimmer men waterproof":  "Afeitado",
    "electric shaver men rechargeable portable": "Afeitado",
    "mini shaver portable travel pocket":   "Afeitado",
    "back shaver long handle men":          "Afeitado",
    "skull shaver head bald":               "Afeitado",
    "electric razor bald head shaver":      "Afeitado",
    "beard trimmer kit cordless":           "Barba",
    "beard straightener brush heated":      "Barba",
    "dark spot corrector serum roller":     "Piel",
    "facial massager":                      "Piel",
    "silicone face cleansing brush":        "Piel",
    "skin tag remover device":              "Piel",
    "acne blue light pen":                  "Piel",
    "ear wax removal camera":               "Higiene",
    "ear wax removal":                      "Higiene",
    "tongue cleaner scraper":               "Higiene",
    "muscle massage gun mini":              "Dolor",
    "shoulder posture strap":               "Dolor",
    "posture trainer wearable":             "Dolor",
    "tens unit pain relief":                "Dolor",
    "carpal tunnel wrist relief":           "Dolor",
    "neck massager cervical pain relief":   "Dolor",
    "sleep aid device insomnia":            "Sueno",
    "anti snoring device mouthpiece":       "Sueno",
    "period pain relief device":            "Salud femenina",
    "menstrual pain relief device heating": "Salud femenina",
    "baby thermometer forehead digital":    "Salud bebe",
    "baby nasal aspirator electric":        "Salud bebe",
    "hair dryer diffuser travel":           "Cabello",
    "hair clipper cordless professional":   "Cabello",
    "eyebrow trimmer electric precision":   "Belleza",
}
# Excluidos a proposito (no son salud/belleza/cuidado personal):
# hand warmer, lint remover, candle lighter, bag sealer, desk vacuum.

# --- Criterio 3: multiplicador de valor percibido ---
# Aparato terapeutico/tech = se puede cobrar mucho mas que su coste.
MULT = {
    "tens unit pain relief": 4.2, "acne blue light pen": 4.2,
    "ear wax removal camera": 4.0, "sleep aid device insomnia": 4.0,
    "menstrual pain relief device heating": 4.0, "period pain relief device": 4.0,
    "skin tag remover device": 3.9, "muscle massage gun mini": 3.8,
    "posture trainer wearable": 3.8, "baby nasal aspirator electric": 3.6,
    "neck massager cervical pain relief": 3.6, "facial massager": 3.5,
    "baby thermometer forehead digital": 3.4, "carpal tunnel wrist relief": 3.4,
    "anti snoring device mouthpiece": 3.4, "epilator women rechargeable": 3.4,
    "dark spot corrector serum roller": 3.3, "ear wax removal": 3.3,
    "back shaver long handle men": 3.3, "skull shaver head bald": 3.2,
    "bikini trimmer women intimate": 3.2, "manscaping groomer kit": 3.2,
    "electric razor bald head shaver": 3.2, "pubic hair trimmer men": 3.1,
    "silicone face cleansing brush": 3.1, "nose ear hair trimmer electric": 3.1,
    "body groomer trimmer men waterproof": 3.0, "beard straightener brush heated": 3.0,
    "eyebrow trimmer electric precision": 3.0, "shoulder posture strap": 3.0,
    "electric shaver women body": 3.0, "face shaver women facial hair": 3.0,
    "hair removal razor women electric": 3.0, "mini shaver portable travel pocket": 3.0,
    "trimmer ceramic blade grooming": 2.9, "electric shaver men rechargeable portable": 2.8,
    "beard trimmer kit cordless": 2.8, "hair clipper cordless professional": 2.6,
    "hair dryer diffuser travel": 2.6, "tongue cleaner scraper": 2.4,
}

# --- Criterio 2: que tan facil es conseguirlo en una tienda fisica ---
# 0 = no se consigue (ideal) ... 1 = esta en cualquier supermercado
RETAIL = {
    "tongue cleaner scraper": 1.0, "hair clipper cordless professional": 0.85,
    "hair dryer diffuser travel": 0.8, "beard trimmer kit cordless": 0.75,
    "electric shaver men rechargeable portable": 0.7, "ear wax removal": 0.6,
    "face shaver women facial hair": 0.5, "eyebrow trimmer electric precision": 0.5,
    "trimmer ceramic blade grooming": 0.5, "shoulder posture strap": 0.5,
    "epilator women rechargeable": 0.45, "hair removal razor women electric": 0.45,
    "silicone face cleansing brush": 0.4, "baby thermometer forehead digital": 0.4,
    "electric shaver women body": 0.4, "mini shaver portable travel pocket": 0.35,
    "body groomer trimmer men waterproof": 0.35, "beard straightener brush heated": 0.3,
    "dark spot corrector serum roller": 0.3, "facial massager": 0.3,
    "nose ear hair trimmer electric": 0.3, "muscle massage gun mini": 0.3,
    "baby nasal aspirator electric": 0.25, "anti snoring device mouthpiece": 0.25,
    "neck massager cervical pain relief": 0.25, "carpal tunnel wrist relief": 0.25,
    "pubic hair trimmer men": 0.2, "manscaping groomer kit": 0.2,
    "electric razor bald head shaver": 0.2, "skull shaver head bald": 0.15,
    "back shaver long handle men": 0.15, "bikini trimmer women intimate": 0.15,
    "posture trainer wearable": 0.15, "period pain relief device": 0.1,
    "menstrual pain relief device heating": 0.1, "skin tag remover device": 0.1,
    "sleep aid device insomnia": 0.1, "ear wax removal camera": 0.05,
    "tens unit pain relief": 0.05, "acne blue light pen": 0.05,
}

VOLUMINOSO = {"back shaver long handle men", "posture trainer wearable",
              "shoulder posture strap", "hair dryer diffuser travel"}


def parse_sold(s):
    if not s:
        return 0
    t = s.lower().replace(".", "").replace(",", "")
    m = re.search(r"(\d+)", t)
    if not m:
        return 0
    n = int(m.group(1))
    if "mil" in t or "k+" in t:
        n *= 1000
    return n


# --- Validacion por titulo -------------------------------------------------
# El buscador de AliExpress devuelve listados que NO son lo que se busco
# (una pistola dosificadora dental aparecio buscando "massage gun"). El titulo
# tiene que confirmar que el producto es realmente de la categoria.
VALIDA = {
    "ear wax removal camera": r"o[ií]d|oreja|cerum|otoscop|endoscop",
    "ear wax removal": r"o[ií]d|oreja|cerum|otoscop",
    "acne blue light pen": r"luz azul|acn[eé]|espinilla|fototerap|l[aá]ser facial",
    "period pain relief device": r"menstrual|per[ií]odo|regla|c[oó]lico|calambre|[uú]tero|palacio|vientre|abdominal",
    "menstrual pain relief device heating": r"menstrual|per[ií]odo|regla|c[oó]lico|calambre|[uú]tero|palacio|vientre|abdominal",
    "sleep aid device insomnia": r"dormir|sue[ñn]o|insomnio|hipnosis|relajac|antiestr[eé]s",
    "tens unit pain relief": r"\btens\b|\bems\b|electroestimul|estimulador|impulso|pulso|acupuntur|fisioterap",
    "skin tag remover device": r"verruga|lunar|marcas en la piel|etiquetas de piel|plasma|papiloma",
    "muscle massage gun mini": r"masajead|fascia|percusi|pistola de masaje|muscular",
    "neck massager cervical pain relief": r"cuello|cervical|tracci[oó]n|masajead",
    "carpal tunnel wrist relief": r"mu[ñn]eca|carpian|f[eé]rula|soporte de mano",
    "posture trainer wearable": r"postura|corrector|jorob|espalda recta",
    "shoulder posture strap": r"postura|corrector|hombro|espalda",
    "baby nasal aspirator electric": r"aspirador nasal|aspirador de nariz|mocos|nariz",
    "baby thermometer forehead digital": r"term[oó]metro",
    "anti snoring device mouthpiece": r"ronqui|roncar|apnea|dilatador nasal|tira nasal",
    "manscaping groomer kit": r"recortador|afeitad|rasurad|cortadora de pelo|maquinilla|ingle|[ií]ntim|corporal|depilad",
    "pubic hair trimmer men": r"recortador|afeitad|rasurad|maquinilla|ingle|p[uú]bic|[ií]ntim|corporal",
    "bikini trimmer women intimate": r"recortador|afeitad|rasurad|maquinilla|bikini|[ií]ntim|depilad",
    "epilator women rechargeable": r"depilad|epilad|afeitad|rasurad|vello",
    "back shaver long handle men": r"afeitad|rasurad|espalda|recortador|maquinilla",
    "skull shaver head bald": r"afeitad|rasurad|calv|cabeza|craneo|cr[aá]neo",
    "electric razor bald head shaver": r"afeitad|rasurad|calv|cabeza",
    "facial massager": r"masajead|facial|lifting|microcorriente|rostro|cara",
    "silicone face cleansing brush": r"limpieza facial|cepillo|exfolia|silicona",
    "dark spot corrector serum roller": r"manchas|despigment|s[eé]rum|serum|oscuras|blanque",
    "nose ear hair trimmer electric": r"recortador|nariz|o[ií]d|orej|vello|trimmer",
    "eyebrow trimmer electric precision": r"cejas|recortador|depilad|afeitad",
    "body groomer trimmer men waterproof": r"recortador|afeitad|rasurad|corporal|maquinilla",
    "beard straightener brush heated": r"barba|alisad|cepillo",
    "mini shaver portable travel pocket": r"afeitad|rasurad|maquinilla|recortador",
    "trimmer ceramic blade grooming": r"recortador|afeitad|rasurad|maquinilla|cortapelo",
    "electric shaver women body": r"afeitad|rasurad|depilad|vello",
    "face shaver women facial hair": r"afeitad|rasurad|depilad|vello|facial",
    "hair removal razor women electric": r"depilad|afeitad|rasurad|vello",
}

# Basura / commodity que se cuela: no es del nicho o se consigue en cualquier lado.
BLOQUEO_TERMS = [
    r"dental", r"profilaxis", r"impresi[oó]n dental", r"\bcable\b", r"alambre",
    r"manicur", r"cortau[ñn]as", r"bolsa de agua", r"almohada",
    r"rodillo de madera", r"pinza de mano", r"fortalecedor", r"de agarre",
    r"tapones", r"\bfunda\b", r"repuesto", r"soporte para tel",
    r"calentador de manos", r"de invierno", r"cargador", r"adaptador", r"bombilla", r"l[aá]mpara de mesa",
]
BLOQUEO = re.compile("|".join(BLOQUEO_TERMS), re.I)

# Claims medicos regulados: Meta y Google restringen estos anuncios, y varios
# son directamente peligrosos (quemar un lunar puede tapar un melanoma).
RIESGO = re.compile(
    r"hemoglobin|glucosa|cet[oó]n|presi[oó]n arterial|diab[eé]t|"
    r"insuficiencia venosa|c[aá]ncer|tumor|verruga|lunar|papiloma|plasma|"
    r"adelgaz|p[eé]rdida de peso|quema(r)? grasa|slimming|reduce medidas|"
    r"diagn[oó]stic|cura[r]?\b|tratamiento m[eé]dico", re.I)


def titulo_valido(q, titulo):
    """True si el titulo confirma la categoria y no es basura."""
    if BLOQUEO.search(titulo):
        return False
    pat = VALIDA.get(q)
    if pat and not re.search(pat, titulo, re.I):
        return False
    return True


def flags(r):
    s = r.get("sp_sources") or []
    if isinstance(s, str):
        try: s = ast.literal_eval(s)
        except Exception: s = []
    txt = " ".join(s)
    return ("choice" in txt), ("FreeShipping" in txt)


def cargar():
    """Normaliza moneda y deduplica, quedandose con el registro mas completo."""
    seen = {}
    for line in open(RAW, encoding="utf-8"):
        try: r = json.loads(line)
        except Exception: continue
        if r.get("currency") == "ARS":
            if r.get("price"): r["price"] = round(r["price"] / RATE_ARS, 2)
            if r.get("original_price"): r["original_price"] = round(r["original_price"] / RATE_ARS, 2)
            r["currency"] = "USD"
        prev = seen.get(r["id"])
        if prev is None or (not prev.get("sp_sources") and r.get("sp_sources")):
            seen[r["id"]] = r
    return list(seen.values())


def main():
    rows = cargar()
    total_crudo = len(rows)
    densidad = collections.Counter(r["query"] for r in rows)

    stats = collections.Counter()
    out = []
    for r in rows:
        q = r["query"]
        nicho = NICHO.get(q)
        if not nicho:
            stats["fuera de nicho"] += 1; continue          # criterio 1
        p = r.get("price") or 0
        if not (5 <= p <= 30):
            stats["precio fuera de 5-30"] += 1; continue    # criterio 4
        sold = parse_sold(r.get("sold_raw"))
        if sold < 50:
            stats["sin ventas suficientes"] += 1; continue  # criterio 5
        rating = r.get("rating") or 0
        if rating and rating < 4.3:
            stats["rating bajo"] += 1; continue
        mult = MULT.get(q, 2.8)
        if mult < 3.0:
            stats["no llega a 3x"] += 1; continue           # criterio 3
        retail = RETAIL.get(q, 0.5)
        if retail >= 0.8:
            stats["se consigue en tienda fisica"] += 1; continue  # criterio 2
        if not titulo_valido(q, r["title"]):
            stats["listado no coincide / commodity"] += 1; continue
        riesgo = bool(RIESGO.search(r["title"]))

        choice, free_ship = flags(r)
        pvp = round(p * mult, 2)
        margen_usd = round(pvp - p, 2)
        margen_pct = round(margen_usd / pvp * 100, 1)

        # Envio: Choice usa logistica consolidada y llega bastante mas rapido.
        envio = "15-25 dias" if choice else "25-45 dias"
        envio_score = 1.0 if choice else 0.45

        # Antiguedad del listado -> proxy de saturacion
        dias = None
        if r.get("launch"):
            try:
                d = datetime.datetime.strptime(r["launch"][:10], "%Y-%m-%d").date()
                dias = (HOY - d).days
            except Exception:
                pass
        frescura = 1.0 if dias is None else max(0.0, min(1.0, 1 - (dias - 60) / 700))

        comp_n = densidad[q]
        comp_ratio = min(comp_n, 180) / 180
        # competencia = saturacion de listados + disponibilidad en retail fisico
        comp_idx = 0.6 * comp_ratio + 0.4 * retail
        comp_txt = "Baja" if comp_idx < 0.33 else ("Media" if comp_idx < 0.6 else "Alta")

        # ---- score 0-100 ----
        s_ventas   = 30 * min(1.0, math.log10(sold + 1) / math.log10(20000))
        s_margen   = 25 * min(1.0, (mult - 2.8) / 1.4)
        s_rating   = 12 * (max(0.0, min(1.0, (rating - 4.3) / 0.7)) if rating else 0.4)
        s_comp     = 18 * (1 - comp_idx)
        s_envio    = 10 * envio_score
        s_precio   = 5 * (1 - min(1.0, abs(p - 15) / 14))
        score = s_ventas + s_margen + s_rating + s_comp + s_envio + s_precio
        score += 3 * frescura
        if q in VOLUMINOSO:
            score -= 4          # criterio 4: peor de enviar
        if free_ship:
            score += 1.5
        if riesgo:
            score -= 14      # claims regulados: riesgo de ban publicitario

        out.append({
            "id": r["id"],
            "titulo": r["title"][:120],
            "nicho": nicho,
            "categoria": q,
            "coste": round(p, 2),
            "pvp_sugerido": pvp,
            "margen_usd": margen_usd,
            "margen_pct": margen_pct,
            "multiplo": round(mult, 1),
            "vendidos": sold,
            "rating": rating or None,
            "competencia": comp_txt,
            "competidores": comp_n,
            "retail_fisico": retail,
            "envio": envio,
            "choice": choice,
            "envio_gratis": free_ship,
            "riesgo_regulatorio": riesgo,
            "dias_publicado": dias,
            "score": round(max(0, min(100, score)), 1),
            "url": r["url"],
            "imagen": ("https:" + r["image"]) if r["image"].startswith("//") else r["image"],
        })

    out.sort(key=lambda x: -x["score"])

    # Diversidad: maximo 4 por categoria, para no entregar 50 afeitadoras.
    top, por_cat = [], collections.Counter()
    for p in out:
        if por_cat[p["categoria"]] >= 4:
            continue
        top.append(p); por_cat[p["categoria"]] += 1
        if len(top) == 50:
            break

    json.dump({
        "generado": HOY.isoformat(),
        "fuente": "AliExpress (catalogo proveedor). AutoDS no disponible en esta sesion.",
        "rate_ars": RATE_ARS,
        "total_crudo": total_crudo,
        "total_filtrado": len(out),
        "descartes": dict(stats),
        "productos": top,
    }, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)

    print(f"crudo {total_crudo} | califican {len(out)} | entregados {len(top)}")
    print("descartes:", dict(stats))
    print("categorias en el top50:", len(por_cat))
    print("nichos:", dict(collections.Counter(p["nicho"] for p in top)))


if __name__ == "__main__":
    main()
