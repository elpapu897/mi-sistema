#!/usr/bin/env python3
"""Filtra y puntua productos segun los criterios del usuario.

Criterios:
  1. Resuelve un problema real (salud / belleza / cuidado personal)
  2. No se consigue en supermercado o tienda fisica
  3. Valor percibido alto -> vendible a >=3x el coste
  4. Coste 5-30 USD, pequeno y facil de enviar
  5. Ya genera ventas
"""
import json, re, os, math, collections

BASE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(BASE, "raw.jsonl")
OUT = os.path.join(BASE, "products.json")

# --- nicho por palabras clave del query ---
NICHO = {
    "piel": ["blackhead", "acne", "led light therapy", "microcurrent", "ice roller",
             "derma roller", "skin scrubber", "cystic", "eye bag", "cleansing brush",
             "gua sha", "under eye", "scar removal", "keratosis", "nose strips",
             "facial massager"],
    "cabello": ["scalp", "hair growth", "curling", "root touch", "thinning hair", "beard"],
    "dolor": ["posture", "neck stretcher", "plantar", "bunion", "carpal", "acupressure mat",
              "massage gun", "trigger point", "knee compression", "tens unit",
              "shoulder posture", "sciatica"],
    "sueno": ["snoring", "mouth tape", "sleep mask", "fidget ring", "acupressure sleep"],
    "higiene": ["tongue scraper", "water flosser", "teeth whitening", "ear wax",
                "nail fungus", "ingrown", "callus", "earwax"],
    "depilacion": ["ipl", "epilator", "eyebrow razor", "lymphatic", "cellulite"],
    "femenina": ["menstrual", "period cup", "pelvic floor", "nipple", "hot flash"],
    "ojos": ["eye massager", "blue light", "dry eye"],
}

# Multiplicador de valor percibido: cuanto se puede cobrar sobre el coste.
# Basado en si es un DISPOSITIVO (alto valor percibido) o un CONSUMIBLE/accesorio.
MULT_ALTO = ["ipl", "led light therapy", "microcurrent", "massage gun", "tens unit",
             "water flosser", "ear wax", "eye massager", "nail fungus", "skin scrubber",
             "epilator", "pelvic floor", "teeth whitening"]
MULT_MEDIO = ["derma roller", "scalp", "posture", "neck stretcher", "acupressure mat",
              "cellulite", "gua sha", "menstrual", "sleep mask", "blue light",
              "facial massager", "cleansing brush", "ice roller"]

# Productos que SI se consiguen en supermercado/farmacia -> penalizar
COMMODITY = ["nose strips", "under eye patches", "tongue scraper", "eyebrow razor",
             "mouth tape", "period cup", "nipple cream", "knee compression"]

# Envio: articulos voluminosos o pesados -> penalizar
VOLUMINOSO = ["acupressure mat", "posture corrector back brace", "sciatica pain relief cushion"]


def parse_sold(s):
    """'10.000+ vendidos' / '1,000+ sold' -> 10000"""
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


def nicho_de(q):
    q = q.lower()
    for n, kws in NICHO.items():
        if any(k in q for k in kws):
            return n
    return "otros"


def multiplicador(q):
    q = q.lower()
    if any(k in q for k in MULT_ALTO):
        return 4.0
    if any(k in q for k in MULT_MEDIO):
        return 3.2
    return 2.6


def main():
    rows = [json.loads(l) for l in open(RAW, encoding="utf-8")]

    # dedup por id
    seen = {}
    for r in rows:
        if r["id"] not in seen:
            seen[r["id"]] = r
    rows = list(seen.values())
    total_crudo = len(rows)

    # competencia: cuantos listados compiten por el mismo query
    por_query = collections.Counter(r["query"] for r in rows)

    out = []
    for r in rows:
        p = r["price"]
        sold = parse_sold(r["sold_raw"])
        rating = r.get("rating") or 0
        q = r["query"]

        # --- filtros duros ---
        if not (5 <= p <= 30):
            continue          # criterio 4: coste
        if sold < 50:
            continue          # criterio 5: ya vende
        if rating and rating < 4.3:
            continue          # calidad minima

        mult = multiplicador(q)
        pvp = round(p * mult, 2)
        margen_pct = round((pvp - p) / pvp * 100, 1)
        margen_usd = round(pvp - p, 2)

        # --- scoring 0-100 ---
        s_ventas = min(35, 35 * math.log10(sold + 1) / math.log10(20000))
        s_margen = min(25, (mult - 2) / 2.5 * 25)
        s_rating = max(0, (rating - 4.3) / 0.7) * 15 if rating else 5
        comp = por_query[q]
        s_comp = 15 * (1 - min(comp, 180) / 180)
        s_precio = 10 * (1 - abs(p - 14) / 16)    # optimo cerca de $14

        score = s_ventas + s_margen + s_rating + s_comp + s_precio

        ql = q.lower()
        if any(k in ql for k in COMMODITY):
            score -= 12      # criterio 2: se consigue en tienda fisica
        if any(k in ql for k in VOLUMINOSO):
            score -= 8       # criterio 4: envio

        # competencia legible
        if comp <= 60:
            comp_txt = "Baja"
        elif comp <= 120:
            comp_txt = "Media"
        else:
            comp_txt = "Alta"

        out.append({
            "id": r["id"],
            "titulo": r["title"][:110],
            "nicho": nicho_de(q),
            "query": q,
            "coste": p,
            "pvp_sugerido": pvp,
            "margen_usd": margen_usd,
            "margen_pct": margen_pct,
            "multiplo": round(mult, 1),
            "vendidos": sold,
            "rating": rating,
            "competencia": comp_txt,
            "competidores": comp,
            "envio_dias": "12-25",   # estandar AliExpress a LATAM
            "score": round(max(0, min(100, score)), 1),
            "url": r["url"],
            "imagen": r["image"],
        })

    out.sort(key=lambda x: -x["score"])
    top = out[:50]
    json.dump({
        "generado": "2026-08-23",
        "total_crudo": total_crudo,
        "total_filtrado": len(out),
        "productos": top,
    }, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)

    print(f"crudo: {total_crudo} | pasan filtros: {len(out)} | entregados: {len(top)}")


if __name__ == "__main__":
    main()
