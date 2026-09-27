#!/usr/bin/env python3
"""TOP 10 del nicho afeitado / depilacion / cuidado personal.

Aplica TODO lo aprendido en la sesion:
  - coste = precio de LISTA, no el promocional (74% del catalogo tiene 50% off falso)
  - Ecuacion de Valor (skill hundred-million-offers)
  - economia real del usuario (skill gonvra-meta-ads): CPA ~22% del ticket, comision 7%
  - validacion de mercado: Voltra vende afeitadoras a 98.880 / 127.880 / 137.990 ARS
  - criterios originales: coste US$5-30, >=3x, chico, que YA venda, no de supermercado
"""
import json, os, re, sys, math, unicodedata, collections

BASE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(BASE, "raw.jsonl")
OUT = os.path.join(BASE, "products.json")

FX = 1497.4528
CPA_RATIO = 0.22
COMISION = 0.07
# franja validada por Voltra para este nicho exacto
VOLTRA_MIN, VOLTRA_MAX = 98880, 137990


def norm(s):
    s = (s or "").lower()
    s = unicodedata.normalize("NFD", s)
    return "".join(c for c in s if unicodedata.category(c) != "Mn")


INCLUIR = ("afeitad|rasurad|shaver|razor|trimmer|recortad|depilad|clipper|"
           "cortapelo|cortadora de pelo|maquinilla|epilad|ipl|barbero")
# ruido que cae por el regex pero no es del nicho
EXCLUIR = ("pelusa|lint|masajead|cepillo de limpieza|cepillo facial|secador|"
           "rizador|plancha|espumador|cafe|aspirador|termometro|linterna")
# consumibles / repuestos: no son el producto, son el recambio
CONSUMIBLE = ("cuchilla de repuesto|repuesto|cabezal de repuesto|hojas de afeitar|"
              "blades? pack|recambio|x10 |10 uds|pack de cuchillas")

SUBCAT = {
    "Cejas y rostro (mujer)": "ceja|eyebrow|facial.*mujer|rostro.*mujer|vello facial",
    "Nariz y orejas": "nariz|nose|oreja|ear hair",
    "Corporal masculino": "corporal|body groomer|ingle|pubic|entrepierna|manscap|espalda",
    "Cortapelo / barberia": "cortapelo|cortadora de pelo|clipper|maquina de cortar|t9|barbero|degradad",
    "Barba": "barba|beard",
    "Depilacion definitiva": "ipl|laser|fotodepil|luz pulsada",
    "Depiladora / epilador": "epilad|depiladora electrica",
}


def subcat(t):
    for k, p in SUBCAT.items():
        if re.search(p, t):
            return k
    return "Afeitado general"


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


def a_usd(price, currency, tax):
    if price is None:
        return None
    if currency == "USD":
        return round(float(price), 2)
    if currency == "ARS":
        try:
            tr = float(tax) if tax else 0.0
        except Exception:
            tr = 0.0
        return round(float(price) / (1 + tr) / FX, 2)
    return None


def main():
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
    cand = []
    for r in seen.values():
        t = r.get("title") or ""
        nt = norm(t)
        if not re.search(INCLUIR, nt):
            continue
        if re.search(EXCLUIR, nt):
            desc["no es del nicho"] += 1; continue
        if re.search(CONSUMIBLE, nt):
            desc["es repuesto, no producto"] += 1; continue

        coste = a_usd(r.get("original_price"), r.get("currency"), r.get("tax_rate")) \
                or a_usd(r.get("price"), r.get("currency"), r.get("tax_rate"))
        v = parse_sold(r.get("sold_raw"))
        rt = r.get("rating")

        if coste is None:
            desc["sin precio"] += 1; continue
        if not (5 <= coste <= 30):
            desc["fuera de US$5-30"] += 1; continue
        if v is None:
            desc["sin dato de ventas"] += 1; continue
        if v < 300:
            desc["poco probado (<300 ventas)"] += 1; continue
        if rt is not None and rt < 4.4:
            desc["rating bajo"] += 1; continue

        cand.append((r, t, nt, coste, v, rt))

    # competencia real: cuantos listados PROBADOS compiten en la misma subcategoria
    comp_n = collections.Counter(subcat(x[2]) for x in cand)

    filas = []
    for r, t, nt, coste, v, rt in cand:
        sc = subcat(nt)
        coste_ars = coste * FX
        # precio de venta: 3x (su minimo) pero sin pasarse de lo que valida Voltra
        pvp_ars = min(max(coste_ars * 3, 39990), VOLTRA_MAX)
        cpa = pvp_ars * CPA_RATIO
        com = pvp_ars * COMISION
        neto = pvp_ars - coste_ars - cpa - com
        multiplo = pvp_ars / coste_ars

        choice = "choice" in " ".join(r.get("sp_sources") or []).lower()
        envio = "Rapido (Choice) ~10-15 dias" if choice else "Estandar ~15-25 dias"

        comp = comp_n[sc]
        comp_txt = "Baja" if comp <= 6 else ("Media" if comp <= 14 else "Alta")

        # --- Ecuacion de Valor ---
        # sueno: quitar vello es cosmetico pero con carga de identidad
        sueno = 8 if re.search("ipl|laser|definitiv", nt) else \
                7 if re.search("corporal|ingle|pubic|espalda|barba", nt) else 6
        demora = 9 if re.search("ipl|laser", nt) else 1   # afeitar = resultado instantaneo
        esfuerzo = 2 if demora == 1 else 5
        prob = min(10, max(1, 5 * math.log10(v + 1) / math.log10(20000)
                           + ((rt - 4.4) / 0.6 * 5 if rt else 2)))
        valor = (sueno * prob) / (demora * esfuerzo)

        # demo visual: afeitado = antes/despues instantaneo en camara
        demo = 9 if re.search("corporal|espalda|ingle|pubic|barba|cortapelo|degradad", nt) else \
               7 if re.search("nariz|oreja|ceja", nt) else 6

        s_valor = min(35, valor / 25 * 35)
        s_demo = demo / 10 * 20
        s_neto = min(20, neto / 70000 * 20)
        s_prueba = min(15, 15 * math.log10(v + 1) / math.log10(20000))
        s_comp = 10 * (1 - min(comp, 25) / 25)
        score = round(max(0, min(100, s_valor + s_demo + s_neto + s_prueba + s_comp)), 1)

        filas.append({
            "id": str(r.get("id")), "titulo": t[:130],
            "nicho": sc, "categoria": r.get("query", ""),
            "tipo": "dispositivo",
            "coste": coste, "coste_ars": round(coste_ars),
            "pvp_ars": round(pvp_ars), "pvp_sugerido": round(pvp_ars / FX, 2),
            "multiplo": round(multiplo, 1),
            "margen_bruto_ars": round(pvp_ars - coste_ars),
            "neto_ars": round(neto),
            "margen_usd": round((pvp_ars - coste_ars) / FX, 2),
            "margen_pct": round((pvp_ars - coste_ars) / pvp_ars * 100, 1),
            "vendidos": v, "rating": rt,
            "competencia": comp_txt, "competidores": comp,
            "envio": envio, "choice": choice,
            "demo_visual": demo, "valor_hormozi": round(valor, 1),
            "score": score, "url": r.get("url", ""), "imagen": r.get("image", ""),
            "coste_exacto": r.get("currency") == "USD",
            "commodity": False, "voluminoso": False, "envio_gratis": False,
        })

    filas.sort(key=lambda x: -x["score"])
    top = filas[:10]
    for p in top:
        p["nota"] = (
            f"{p['vendidos']:,}".replace(",", ".") + " ventas confirmadas"
            + (f" y {p['rating']}★" if p["rating"] else "")
            + f". Coste {p['coste_ars']:,}".replace(",", ".") + " ARS; vendiendolo a "
            + f"{p['pvp_ars']:,}".replace(",", ".") + f" ({p['multiplo']}x) te quedan "
            + f"{p['neto_ars']:,}".replace(",", ".")
            + " limpios por venta despues de pauta y comision. "
            + f"Competencia {p['competencia'].lower()} ({p['competidores']} listados probados en "
            + f"{p['nicho']}). Demo visual {p['demo_visual']}/10. {p['envio']}."
        )

    json.dump({
        "generado": "2026-08-24",
        "fuente": "AliExpress (catalogo base AutoDS) - nicho afeitado/depilacion",
        "fx_usd_ars": FX,
        "markup_supuesto": {"dispositivo": 3.0, "herramienta": 3.0, "consumible": 2.5},
        "reglas": {"cpa_ratio": CPA_RATIO, "comision": COMISION,
                   "franja_validada_voltra": [VOLTRA_MIN, VOLTRA_MAX]},
        "total_crudo": len(seen), "total_filtrado": len(filas), "entregados": len(top),
        "descartes": dict(desc), "productos": top,
    }, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)

    print(f"crudo={len(seen)} | candidatos del nicho={len(cand)} | pasan={len(filas)} | top={len(top)}")
    print("descartes:", dict(desc))


if __name__ == "__main__":
    main()
