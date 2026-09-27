#!/usr/bin/env python3
"""Recolector cortes y reanudable del catalogo base (AliExpress = catalogo que
alimenta a AutoDS) para nichos de salud, belleza y cuidado personal.

Principios:
  - UNA sola conexion, secuencial. Nada de concurrencia (eso fue lo que gatillo
    el muro anti-bot la vez anterior).
  - Pausa configurable + jitter entre pedidos.
  - Si detecta bloqueo: espera larga, baja el ritmo y reintenta.
  - Reanudable: guarda que (query, page) ya bajo. Se puede cortar y seguir.
  - Captura SIN PERDIDA: guarda los campos crudos tal como vienen, incluidos
    los tags de la tarjeta (Choice, envio gratis, mas vendido), la fecha de
    lanzamiento y la moneda. La interpretacion se hace despues, en score.py.
"""
import json, os, re, sys, time, random, argparse, subprocess

BASE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(BASE, "raw.jsonl")
STATE = os.path.join(BASE, "collect_state.json")

UA = ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36")

# IMPORTANTE: NO mandar cabecera Cookie. Se comprobo que la cabecera Cookie es
# lo que dispara el muro anti-bot. El pedido limpio pasa sin problema.

QUERIES = [
    # --- piel: problemas reales ---
    "blackhead remover vacuum", "acne pimple patch", "led light therapy mask",
    "microcurrent face lifting device", "ice roller face", "derma roller microneedle",
    "skin scrubber ultrasonic", "eye bag remover device", "silicone face cleansing brush",
    "gua sha lymphatic drainage", "scar removal silicone sheet",
    "keratosis pilaris exfoliating", "blackhead extractor tool kit",
    "red light therapy device face", "skin tag remover device",
    "facial steamer nano ionic", "pore vacuum cleaner", "acne blue light pen",
    "dark spot corrector serum roller", "collagen face lifting device",
    # --- cabello / cuero cabelludo ---
    "scalp massager hair growth", "hair growth serum derma roller",
    "heatless curling rod", "hair root touch up powder", "thinning hair fiber",
    "scalp treatment brush", "beard growth roller kit", "laser hair growth comb",
    "hair straightener brush mini", "scalp scrubber exfoliator",
    # --- dolor / postura / recuperacion ---
    "posture corrector back brace", "neck stretcher cervical traction",
    "plantar fasciitis sock", "bunion corrector toe separator",
    "carpal tunnel wrist brace", "muscle massage gun mini",
    "trigger point massage ball", "tens unit pain relief",
    "shoulder posture strap", "back massager shiatsu neck",
    "foot massager acupressure", "heel spur insole", "hand grip strengthener therapy",
    "knee massager heated", "lower back stretcher device",
    # --- sueno / ansiedad / bienestar ---
    "anti snoring device nose", "mouth tape sleeping", "weighted sleep mask",
    "anxiety fidget ring", "white noise machine sleep", "sleep aid device insomnia",
    "breathing trainer device", "vagus nerve stimulator",
    # --- higiene / cuidado personal ---
    "water flosser portable", "teeth whitening kit led", "ear wax removal camera",
    "nail fungus laser device", "ingrown toenail tool", "callus remover foot file",
    "electric earwax cleaner", "tongue cleaner scraper", "dental calculus remover",
    "nose hair trimmer electric", "electric nail file drill", "teeth night guard grinding",
    # --- depilacion / belleza corporal ---
    "ipl hair removal device", "facial hair epilator women",
    "lymphatic drainage massager body", "cellulite massager cup",
    "body sculpting device ems", "hair removal laser permanent",
    # --- salud femenina ---
    "menstrual heating pad portable", "pelvic floor trainer", "period pain relief device",
    "breast pump wearable", "postpartum recovery belt",
    # --- ojos / vista ---
    "eye massager heated", "dry eye compress mask", "eyelid cleanser device",
    # --- salud general / medicion ---
    "posture trainer wearable", "blood pressure monitor wrist", "pulse oximeter fingertip",
    "body fat scale smart", "thermometer infrared forehead", "nebulizer portable mesh",
    "hearing amplifier mini", "blood sugar monitor device",
    "cold sore treatment device", "nasal irrigation device",
    "humidifier personal desk", "aromatherapy diffuser portable",
]


def extract_blob(html):
    i = html.find("init-data-start")
    if i < 0:
        return None
    k = html.find("_init_data_=", i)
    if k < 0:
        return None
    s = html.find("{", html.find("data:", k))
    if s < 0:
        return None
    depth = 0; instr = False; esc = False
    for j in range(s, len(html)):
        c = html[j]
        if instr:
            if esc: esc = False
            elif c == "\\": esc = True
            elif c == '"': instr = False
        else:
            if c == '"': instr = True
            elif c == "{": depth += 1
            elif c == "}":
                depth -= 1
                if depth == 0:
                    try:
                        return json.loads(html[s:j + 1])
                    except Exception:
                        return None
    return None


def fetch(url, timeout=35):
    """Devuelve (html, blocked). Replica exactamente el pedido que funciona."""
    try:
        r = subprocess.run(
            ["curl", "-s", "--compressed", "--max-time", str(timeout),
             "-H", f"User-Agent: {UA}",
             "-H", "Accept-Language: en-US,en;q=0.9",
             "-H", "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
             url],
            capture_output=True, timeout=timeout + 10)
        html = r.stdout.decode("utf-8", "ignore")
    except Exception:
        return None, False
    if not html:
        return None, False
    if "_____tmd_____" in html or len(html) < 50000:
        return None, True
    return html, False


def parse_items(blob, query, page):
    try:
        items = blob["data"]["root"]["fields"]["mods"]["itemList"]["content"]
    except Exception:
        return []
    out = []
    for it in items:
        try:
            pid = it.get("productId")
            if not pid:
                continue
            pr = it.get("prices") or {}
            sp = pr.get("salePrice") or {}
            op = pr.get("originalPrice") or {}
            price = sp.get("minPrice", op.get("minPrice"))
            if price is None:
                continue
            sps = it.get("sellingPoints") or []
            sources = [x.get("source") for x in sps if x.get("source")]
            texts = []
            for x in sps:
                t = ((x.get("tagContent") or {}).get("tagText"))
                if t:
                    texts.append(t)
            trade = it.get("trade") or {}
            ev = it.get("evaluation") or {}
            out.append({
                "query": query,
                "page": page,
                "id": str(pid),
                "title": (it.get("title") or {}).get("displayTitle", ""),
                "currency": sp.get("currencyCode") or op.get("currencyCode"),
                "price": price,
                "original_price": op.get("minPrice"),
                "discount": sp.get("discount") or 0,
                "tax_rate": pr.get("taxRate"),
                "rating": ev.get("starRating"),          # puede faltar
                "sold_raw": trade.get("tradeDesc", ""),  # puede faltar
                "launch": it.get("lunchTime"),
                "sp_sources": sources,                   # choice_atm, freeShipping, etc
                "sp_texts": texts,                       # "Top ventas", "Envio gratis"...
                "image": (it.get("image") or {}).get("imgUrl", ""),
                "url": f"https://www.aliexpress.com/item/{pid}.html",
            })
        except Exception:
            continue
    return out


def load_state():
    if os.path.exists(STATE):
        try:
            return set(tuple(x) for x in json.load(open(STATE))["done"])
        except Exception:
            pass
    return set()


def save_state(done):
    json.dump({"done": [list(x) for x in done]}, open(STATE, "w"))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--pages", type=int, default=2)
    ap.add_argument("--delay", type=float, default=15.0)
    ap.add_argument("--max-delay", type=float, default=75.0)
    ap.add_argument("--queries-file", help="archivo con una consulta por linea")
    args = ap.parse_args()

    done = load_state()
    qs = QUERIES
    if args.queries_file:
        qs = [l.strip() for l in open(args.queries_file, encoding="utf-8")
              if l.strip() and not l.startswith("#")]
    tasks = [(q, p) for q in qs for p in range(1, args.pages + 1)
             if (q, p) not in done]
    random.shuffle(tasks)

    delay = args.delay
    total = 0
    blocks = 0
    if os.path.exists(OUT):
        total = sum(1 for _ in open(OUT, encoding="utf-8"))

    fh = open(OUT, "a", encoding="utf-8")
    for idx, (q, p) in enumerate(tasks, 1):
        url = ("https://www.aliexpress.com/w/wholesale-"
               + q.replace(" ", "-") + f".html?page={p}")
        html, blocked = fetch(url)

        if blocked:
            blocks += 1
            delay = min(args.max_delay, delay * 1.5)
            cool = 180 + blocks * 60 + random.random() * 30
            sys.stderr.write(f"\n[bloqueo #{blocks}] enfriando {int(cool)}s, "
                             f"nuevo ritmo {delay:.0f}s\n")
            sys.stderr.flush()
            time.sleep(cool)
            continue

        if html:
            blob = extract_blob(html)
            rows = parse_items(blob, q, p) if blob else []
            if rows:
                for r in rows:
                    fh.write(json.dumps(r, ensure_ascii=False) + "\n")
                total += len(rows)
                fh.flush()
                done.add((q, p))
                save_state(done)
                # se porta bien: recuperar ritmo de a poco
                delay = max(args.delay, delay * 0.95)

        sys.stderr.write(f"\r[{idx}/{len(tasks)}] items={total} ritmo={delay:.0f}s "
                         f"bloqueos={blocks}   ")
        sys.stderr.flush()
        time.sleep(delay + random.random() * 5)

    fh.close()
    sys.stderr.write(f"\nTERMINADO. items crudos totales: {total}\n")


if __name__ == "__main__":
    main()
