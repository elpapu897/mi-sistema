#!/usr/bin/env python3
"""Extrae productos de AliExpress (catalogo base de AutoDS) para nichos de
salud, belleza y cuidado personal. Precios forzados a USD."""
import json, re, time, random, urllib.parse, os, sys
import concurrent.futures as cf
import urllib.request

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "raw.jsonl")

UA = ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
# fuerza region US / moneda USD / ingles
COOKIE = ("aep_usuc_f=site=glo&us=USD&region=US&b_locale=en_US&c_tp=USD; "
          "intl_locale=en_US; xman_us_f=x_locale=en_US&x_l=0")

QUERIES = [
    # --- cuidado de la piel / problemas reales ---
    "blackhead remover vacuum", "acne pimple patch", "led light therapy mask",
    "microcurrent face lifting device", "ice roller face", "derma roller microneedle",
    "skin scrubber ultrasonic", "cystic acne treatment", "eye bag remover device",
    "silicone face cleansing brush", "gua sha lymphatic drainage",
    "under eye patches collagen", "scar removal silicone sheet",
    "keratosis pilaris exfoliating", "nose strips pore",
    # --- cabello / cuero cabelludo ---
    "scalp massager hair growth", "hair growth serum derma", "heatless curling rod",
    "hair root touch up powder", "thinning hair fiber", "scalp treatment brush",
    "beard growth roller kit",
    # --- dolor / postura / recuperacion ---
    "posture corrector back brace", "neck stretcher cervical traction",
    "plantar fasciitis sock", "bunion corrector toe separator",
    "carpal tunnel wrist brace", "acupressure mat", "muscle massage gun mini",
    "trigger point massage ball", "knee compression sleeve", "tens unit pain relief",
    "shoulder posture strap", "sciatica pain relief cushion",
    # --- sueno / ansiedad / bienestar ---
    "anti snoring device nose", "mouth tape sleeping", "weighted sleep mask",
    "anxiety fidget ring", "acupressure sleep aid",
    # --- higiene / cuidado personal ---
    "tongue scraper stainless", "water flosser portable", "teeth whitening kit led",
    "ear wax removal camera", "nail fungus laser device", "ingrown toenail tool",
    "callus remover foot file", "electric earwax cleaner",
    # --- depilacion / belleza corporal ---
    "ipl hair removal device", "facial hair epilator women", "eyebrow razor precision",
    "lymphatic drainage massager body", "cellulite massager cup",
    # --- salud femenina / especificos ---
    "menstrual heating pad portable", "period cup kit", "pelvic floor trainer",
    "nipple cream nursing", "hot flash cooling",
    # --- ojos / vista ---
    "eye massager heated", "blue light blocking glasses", "dry eye compress mask",
]

PAGES = 3          # 3 paginas x 60 items = 180 por query
MAX_WORKERS = 4    # cortesia: pocas conexiones simultaneas


def fetch(url):
    req = urllib.request.Request(url, headers={
        "User-Agent": UA, "Cookie": COOKIE,
        "Accept-Language": "en-US,en;q=0.9",
        "Accept": "text/html,application/xhtml+xml",
    })
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read().decode("utf-8", "ignore")


def extract_blob(html):
    i = html.find("init-data-start")
    if i < 0:
        return None
    k = html.find("_init_data_=", i)
    if k < 0:
        return None
    s = html.find("{", html.find("data:", k))
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


def parse_items(blob, query):
    try:
        items = blob["data"]["root"]["fields"]["mods"]["itemList"]["content"]
    except Exception:
        return []
    out = []
    for it in items:
        try:
            pr = it.get("prices") or {}
            sp = pr.get("salePrice") or pr.get("originalPrice") or {}
            cur = sp.get("currencyCode")
            price = sp.get("minPrice")
            if price is None:
                continue
            orig = (pr.get("originalPrice") or {}).get("minPrice")
            out.append({
                "query": query,
                "id": it.get("productId"),
                "title": (it.get("title") or {}).get("displayTitle", ""),
                "currency": cur,
                "price": price,
                "original_price": orig,
                "discount": (sp.get("discount") or 0),
                "rating": (it.get("evaluation") or {}).get("starRating"),
                "sold_raw": (it.get("trade") or {}).get("tradeDesc", ""),
                "image": (it.get("image") or {}).get("imgUrl", ""),
                "url": f"https://www.aliexpress.com/item/{it.get('productId')}.html",
            })
        except Exception:
            continue
    return out


def job(args):
    q, page = args
    url = ("https://www.aliexpress.com/w/wholesale-"
           + urllib.parse.quote(q.replace(" ", "-"))
           + f".html?page={page}&currency=USD&shipCountry=US")
    for attempt in range(3):
        try:
            html = fetch(url)
            blob = extract_blob(html)
            if blob:
                rows = parse_items(blob, q)
                if rows:
                    return rows
        except Exception as e:
            pass
        time.sleep(2 + attempt * 3 + random.random() * 2)
    return []


def main():
    tasks = [(q, p) for q in QUERIES for p in range(1, PAGES + 1)]
    random.shuffle(tasks)
    n = 0
    with open(OUT, "w", encoding="utf-8") as f, \
         cf.ThreadPoolExecutor(max_workers=MAX_WORKERS) as ex:
        for rows in ex.map(job, tasks):
            for r in rows:
                f.write(json.dumps(r, ensure_ascii=False) + "\n")
                n += 1
            f.flush()
            sys.stderr.write(f"\racumulados: {n}   ")
    sys.stderr.write(f"\nTOTAL crudo: {n}\n")


if __name__ == "__main__":
    main()
