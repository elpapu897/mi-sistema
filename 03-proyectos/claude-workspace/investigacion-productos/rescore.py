#!/usr/bin/env python3
"""
Re-puntuacion de los 50 productos del dashboard contra los criterios REALES
del usuario (los de la ronda 2, 2026-08-23), no contra el score original.

IMPORTANTE — origen de cada columna:
  DATO   : coste, vendidos, rating, dias  -> vienen del catalogo del proveedor
  MODELO : margen                          -> multiplo asignado a mano por categoria
  JUICIO : urgencia, publico, seguridad, no_retail, meta_ok, envio_ok, ltv
           -> los asigno YO por categoria. Son opiniones argumentables,
              no mediciones. Estan aca para que se puedan discutir de a una.

Vetos duros (eliminan sin importar el puntaje):
  - producto ya rechazado explicitamente por el usuario
  - seguridad <= 3  (riesgo de dano fisico)
  - meta_ok  <= 3   (rechazo/ban casi seguro en Meta Ads)
"""
import json
import collections

# ---------------------------------------------------------------- JUICIO ----
# Por categoria: (urgencia, publico, seguridad, no_retail, meta_ok, envio_ok, ltv)
# 0-10 cada uno. envio_ok = "sobrevive la razon de compra a 15-25 dias de envio?"
J = {
 "ear wax removal camera":            (8, 8, 2, 9, 4, 6, 3),
 "sleep aid device insomnia":         (7, 8, 4, 8, 2, 7, 3),
 "skin tag remover device":           (6, 6, 2, 9, 1, 7, 3),
 "tens unit pain relief":             (6, 7, 3, 4, 3, 6, 4),
 "menstrual pain relief device heating": (9, 9, 8, 9, 7, 9, 8),
 "period pain relief device":         (9, 9, 8, 9, 7, 9, 8),
 "acne blue light pen":               (5, 6, 3, 8, 2, 6, 3),
 "baby nasal aspirator electric":     (10, 6, 6, 6, 5, 2, 3),
 "muscle massage gun mini":           (4, 6, 7, 5, 7, 7, 4),
 "manscaping groomer kit":            (2, 7, 8, 3, 8, 8, 4),
 "pubic hair trimmer men":            (2, 7, 8, 3, 8, 8, 4),
 "electric razor bald head shaver":   (2, 7, 8, 3, 8, 8, 4),
 "neck massager cervical pain relief":(6, 8, 4, 4, 5, 6, 4),
 "baby thermometer forehead digital": (7, 6, 8, 3, 6, 3, 2),
 "posture trainer wearable":          (3, 8, 7, 3, 6, 7, 3),
 "carpal tunnel wrist relief":        (5, 5, 8, 3, 6, 6, 3),
 "epilator women rechargeable":       (3, 7, 7, 3, 8, 7, 5),
 "anti snoring device mouthpiece":    (6, 7, 3, 3, 3, 7, 4),
 "silicone face cleansing brush":     (2, 6, 9, 4, 8, 7, 4),
}

# Productos que el usuario YA rechazo explicitamente (chat 2026-08-23)
VETO_USUARIO = {
 "ear wax removal camera":    "lo bocho: 'chico y peligroso'",
 "sleep aid device insomnia": "bocho el antifaz: 'para musica me pongo auriculares comunes'",
}

PESOS = {"urgencia": 22, "publico": 18, "seguridad": 15, "no_retail": 15,
         "meta_ok": 12, "envio_ok": 12, "ltv": 6}
CAMPOS = ["urgencia", "publico", "seguridad", "no_retail", "meta_ok", "envio_ok", "ltv"]


def main():
    d = json.load(open("productos_top50.json"))
    filas = []
    for x in d["productos"]:
        cat = x["categoria"]
        if cat not in J:
            continue
        j = dict(zip(CAMPOS, J[cat]))

        # 70% juicio cualitativo + 30% evidencia dura (ventas y margen absoluto)
        cual = sum(PESOS[c] * j[c] / 10 for c in CAMPOS)          # 0-100
        ventas = min(1.0, x["vendidos"] / 5000)                    # DATO
        margen = min(1.0, x["margen_usd"] / 50)                    # MODELO
        dura = 100 * (0.65 * ventas + 0.35 * margen)

        nota = round(0.70 * cual + 0.30 * dura, 1)

        veto = None
        if cat in VETO_USUARIO:
            veto = "USUARIO: " + VETO_USUARIO[cat]
        elif j["seguridad"] <= 3:
            veto = "SEGURIDAD: riesgo de dano fisico"
        elif j["meta_ok"] <= 3:
            veto = "META ADS: rechazo/ban casi seguro"

        filas.append({**x, "nota": nota, "veto": veto, **j})

    filas.sort(key=lambda r: -r["nota"])

    print("=" * 118)
    print("RANKING RE-PUNTUADO — criterios del usuario (ronda 2)")
    print("=" * 118)
    print(f"{'#':<3}{'nota':<6}{'urg':<4}{'pub':<4}{'seg':<4}{'ret':<4}"
          f"{'meta':<5}{'env':<4}{'ltv':<4}{'vend':<7}{'mrg$':<7} producto")
    print("-" * 118)
    vivos = [f for f in filas if not f["veto"]]
    for i, r in enumerate(vivos, 1):
        print(f"{i:<3}{r['nota']:<6}{r['urgencia']:<4}{r['publico']:<4}{r['seguridad']:<4}"
              f"{r['no_retail']:<4}{r['meta_ok']:<5}{r['envio_ok']:<4}{r['ltv']:<4}"
              f"{r['vendidos']:<7}{r['margen_usd']:<7} {r['titulo'][:52]}")

    print()
    print("=" * 118)
    print("ELIMINADOS POR VETO")
    print("=" * 118)
    porveto = collections.defaultdict(list)
    for r in filas:
        if r["veto"]:
            porveto[(r["categoria"], r["veto"])].append(r)
    for (cat, v), rs in sorted(porveto.items(), key=lambda kv: -len(kv[1])):
        print(f"  {len(rs):>2} producto(s) | {cat:<38} | {v}")
    print(f"\n  Total eliminados: {sum(len(v) for v in porveto.values())} de {len(filas)}")


if __name__ == "__main__":
    main()
