#!/usr/bin/env python3
"""Selector de producto ganador para GONVRA.

Reescrito usando las reglas REALES del negocio del usuario, no supuestos:

  - skill gonvra-meta-ads: CPA sano $5.000-$7.000 ARS/venta, ticket $20.000-$32.000,
    no pautar en frio productos de menos de $16.990.
  - skill hundred-million-offers: Ecuacion de Valor de Hormozi
        Valor = (Sueno x Probabilidad percibida) / (Demora x Esfuerzo)
  - regla del usuario: precio al publico TOPE 25.000 ARS, fijo.
  - correccion propia: el coste es el PRECIO DE LISTA, no el promocional
    (el 74% del catalogo esta con >=50% off temporal).

En vez de un markup fijo de 3x, se calcula la GANANCIA NETA REAL por venta.
"""
import json, os, re, sys, math, unicodedata, argparse, collections

BASE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(BASE, "raw.jsonl")
OUT = os.path.join(BASE, "products.json")

FX = 1497.4528
PRECIO_VENTA = 25000.0     # tope duro del usuario
CPA = 6000.0               # punto medio de su rango real 5.000-7.000
COMISION = 0.07            # pasarela de pago
NETO_MINIMO = 4000.0       # por debajo de esto no vale la pena el laburo


def norm(s):
    s = (s or "").lower()
    s = unicodedata.normalize("NFD", s)
    return "".join(c for c in s if unicodedata.category(c) != "Mn")


# ---------- Ecuacion de Valor: SUENO (que tan grande es la transformacion) ----------
SUENO = [
    (9, ["calvicie", "alopecia", "crecimiento del cabello", "caida del cabello",
         "hair growth", "acne", "cicatriz", "mancha", "arruga", "papada",
         "bebe", "baby", "fiebre", "respirar", "asma", "dolor cronico",
         "hernia", "ciatica", "migrana", "insomnio", "ronquido", "apnea"]),
    (7, ["dolor", "pain", "postura", "cervical", "lumbar", "articulacion",
         "hongo", "fungus", "sarro", "caries", "encia", "celulitis",
         "adelgaz", "circulacion", "varices"]),
    (5, ["limpieza", "limpiador", "cera de oido", "pelusa", "mancha ropa",
         "afilar", "sellar", "encender", "cocina", "parrilla", "barbacoa",
         "organiz", "ahorr"]),
    (3, ["masaje", "relax", "confort", "musica", "decorac", "luz ambiente"]),
]

# ---------- DEMORA: cuanto tarda en verse el resultado (MENOS es mejor) ----------
DEMORA = [
    (1, ["encender", "encendedor", "lighter", "sellar", "sealer", "afilar",
         "aspirador", "vacuum", "limpiador", "cleaner", "pelusa", "lint",
         "cortar", "abrir", "linterna", "extractor", "removedor de cera"]),
    (2, ["masajeador", "massage", "calefactor", "calienta", "vibra", "termometro",
         "medidor", "monitor", "cepillo", "lavado"]),
    (5, ["blanqueamiento", "whitening", "postura", "corrector", "faja",
         "compresion", "plantilla"]),
    (9, ["crecimiento del cabello", "hair growth", "alopecia", "calvicie",
         "arruga", "antiedad", "colageno", "cicatriz", "mancha oscura",
         "adelgaz", "celulitis", "hongo", "fungus"]),
]

# ---------- ESFUERZO: que tanto tiene que hacer el cliente (MENOS es mejor) ----------
ESFUERZO = [
    (1, ["encendedor", "lighter", "sellador", "sealer", "abrelatas", "linterna",
         "afilador", "aspirador", "termometro"]),
    (2, ["masajeador", "limpiador", "cepillo electrico", "removedor", "pelusa"]),
    (5, ["rodillo", "roller", "derma", "gua sha", "ventosa", "faja", "corrector",
         "plantilla", "protector bucal"]),
    (8, ["tratamiento", "serum", "crema", "suplemento", "rutina", "terapia diaria"]),
]

# ---------- DEMO VISUAL: se entiende en 3 segundos en un video? ----------
DEMO = [
    (10, ["cera de oido", "earwax", "pelusa", "lint", "punto negro", "blackhead",
          "poro", "sarro", "mancha", "plasma", "arco electrico", "antes y despues",
          "extractor", "aspirador", "succion", "espuma", "burbuja"]),
    (7, ["encendedor", "lighter", "sellador", "corte", "afilar", "vapor",
         "luz led", "brillo", "limpieza profunda", "chorro"]),
    (4, ["masajeador", "calefactor", "vibra", "termometro", "medidor", "monitor"]),
    (2, ["faja", "corrector", "soporte", "banda", "almohadilla", "protector"]),
]

COMMODITY = ["parche", "patch", "crema", "cream", "serum", "aceite", "oil",
             "algodon", "curita", "shampoo", "champu", "jabon", "soap", "hisopo",
             "pasta dental", "toothpaste", "esponja", "locion", "vendaje", "gasa",
             "cepillo de dientes", "toothbrush", "tira nasal", "nose strip",
             "papel", "servilleta", "bolsa de basura", "pila aa", "bateria aa"]

VOLUMINOSO = ["colchoneta", "mat ", "almohada", "pillow", "cojin", "silla", "chair",
              "manta", "blanket", "bascula", "banco", "tabla", "bicicleta",
              "stepper", "secarropa", "tendedero", "aspiradora de pie"]

RIESGO = ["oido", "ear", "otoscopio", "endoscopio", "ems", "tens", "microcorriente",
          "electroestimul", "laser", "ipl", "bisturi", "aguja", "dermapen"]


def puntuar(tabla, texto, default):
    for val, kws in tabla:
        if any(k in texto for k in kws):
            return val
    return default


def parse_sold(s):
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
    if price is None:
        return None
    if currency == "USD":
        return round(float(price), 2)
    if currency == "ARS":
        try:
            tr = float(tax_rate) if tax_rate else 0.0
        except Exception:
            tr = 0.0
        return round(float(price) / (1 + tr) / FX, 2)
    return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--top", type=int, default=50)
    ap.add_argument("--min-ventas", type=int, default=300)
    a = ap.parse_args()

    seen = {}
    for line in open(RAW, encoding="utf-8"):
        line = line.strip()
        if not line:
            continue
        try:
            r = json.loads(line)
        except Exception:
            continue
        seen.setdefault(str(r.get("id")), r)

    desc = collections.Counter()
    filas = []
    for r in seen.values():
        t = r.get("title") or ""
        nt = norm(t)
        # COSTE = precio de lista (no el promocional)
        coste = a_usd(r.get("original_price"), r.get("currency"), r.get("tax_rate")) \
                or a_usd(r.get("price"), r.get("currency"), r.get("tax_rate"))
        v = parse_sold(r.get("sold_raw"))
        rt = r.get("rating")

        if coste is None:
            desc["sin precio"] += 1; continue
        if v is None:
            desc["sin dato de ventas"] += 1; continue
        if v < a.min_ventas:
            desc["poco probado (<%d ventas)" % a.min_ventas] += 1; continue
        if rt is not None and rt < 4.5:
            desc["rating bajo"] += 1; continue

        coste_ars = coste * FX
        neto = PRECIO_VENTA - coste_ars - CPA - PRECIO_VENTA * COMISION
        if neto < NETO_MINIMO:
            desc["no deja ganancia a 25.000"] += 1; continue
        if any(k in nt for k in COMMODITY):
            desc["se consigue en super/farmacia"] += 1; continue
        if any(k in nt for k in VOLUMINOSO):
            desc["voluminoso"] += 1; continue

        # --- Ecuacion de Valor ---
        sueno = puntuar(SUENO, nt, 4)
        demora = puntuar(DEMORA, nt, 4)
        esfuerzo = puntuar(ESFUERZO, nt, 4)
        demo = puntuar(DEMO, nt, 4)
        # probabilidad percibida: reputacion + prueba social
        prob = 0.0
        prob += min(5.0, 5.0 * math.log10(v + 1) / math.log10(20000))
        prob += ((rt - 4.5) / 0.5 * 5.0) if rt is not None else 2.0
        prob = max(1.0, min(10.0, prob))

        valor = (sueno * prob) / (demora * esfuerzo)      # Hormozi
        riesgoso = any(k in nt for k in RIESGO)

        # --- score final 0-100 ---
        s_valor = min(40, valor / 12.0 * 40)     # ecuacion de valor
        s_demo = demo / 10 * 25                  # se puede pautar?
        s_neto = min(20, neto / 12000 * 20)      # plata real por venta
        s_prueba = min(15, 15 * math.log10(v + 1) / math.log10(20000))
        score = s_valor + s_demo + s_neto + s_prueba
        if riesgoso:
            score -= 10                          # el usuario rechaza lo que puede lastimar

        filas.append({
            "id": str(r.get("id")), "titulo": t[:130],
            "coste": coste, "coste_ars": round(coste_ars),
            "precio_venta": PRECIO_VENTA,
            "neto_ars": round(neto), "multiplo": round(PRECIO_VENTA / coste_ars, 1),
            "vendidos": v, "rating": rt,
            "sueno": sueno, "probabilidad": round(prob, 1),
            "demora": demora, "esfuerzo": esfuerzo, "demo_visual": demo,
            "valor_hormozi": round(valor, 1), "riesgoso": riesgoso,
            "categoria": r.get("query", ""),
            "score": round(max(0, min(100, score)), 1),
            "url": r.get("url", ""), "imagen": r.get("image", ""),
            "nicho": ("Hogar y vida diaria" if any(k in nt for k in
                        ["encendedor","lighter","sellador","cocina","parrilla","afilador",
                         "aspirador","pelusa","lint","vela","linterna"])
                      else "Higiene y cuidado personal" if any(k in nt for k in
                        ["lengua","oido","dental","sarro","una","pie","cera"])
                      else "Rostro y piel" if any(k in nt for k in
                        ["facial","rostro","piel","poro","acne"])
                      else "Salud y dolor"),
            "tipo": ("dispositivo" if any(k in nt for k in
                        ["electric","eléctric","usb","recargable","led","plasma","digital",
                         "intelig","bateria","batería","motor"]) else "herramienta"),
            "competencia": "Baja", "competidores": 0,
            "envio": "Choice" if "choice" in " ".join(r.get("sp_sources") or []).lower() else "Estandar",
            "margen_usd": round(neto / FX, 2), "margen_pct": round(neto / PRECIO_VENTA * 100, 1),
            "pvp_sugerido": round(PRECIO_VENTA / FX, 2),
            "coste_exacto": r.get("currency") == "USD", "commodity": False,
            "voluminoso": False, "choice": "choice" in " ".join(r.get("sp_sources") or []).lower(),
        })

    filas.sort(key=lambda x: -x["score"])
    for i, f in enumerate(filas, 1):
        f["nota"] = (
            f"Deja {f['neto_ars']:,} ARS limpios por venta despues de pagar producto, "
            f"pauta ({int(CPA):,}) y comision. {f['vendidos']:,} ventas probadas"
            + (f", {f['rating']}★" if f['rating'] else "")
            + f". Demo visual {f['demo_visual']}/10, "
            f"resultado en {'segundos' if f['demora']<=2 else 'semanas' if f['demora']<=5 else 'meses'}."
            + (" OJO: puede lastimar a alguien, vos ya rechazaste ese tipo." if f["riesgoso"] else "")
        ).replace(",", ".")

    top = filas[:a.top]
    json.dump({
        "generado": "2026-08-23",
        "fuente": "AliExpress (catalogo base AutoDS) - motor Ecuacion de Valor",
        "fx_usd_ars": FX,
        "markup_supuesto": {"dispositivo": 3.6, "herramienta": 3.0, "consumible": 2.5},
        "reglas": {
            "precio_venta_ars": PRECIO_VENTA, "cpa_ars": CPA,
            "comision": COMISION, "neto_minimo_ars": NETO_MINIMO,
        },
        "total_crudo": len(seen), "total_filtrado": len(filas), "entregados": len(top),
        "descartes": dict(desc), "productos": top,
    }, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)

    print(f"crudo={len(seen)} | pasan={len(filas)} | entregados={len(top)}")
    print("descartes:", dict(desc))


if __name__ == "__main__":
    main()
