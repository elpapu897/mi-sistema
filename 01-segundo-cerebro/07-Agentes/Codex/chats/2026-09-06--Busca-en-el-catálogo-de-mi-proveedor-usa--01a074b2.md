---
tool: Codex
session_id: 01a074b2-1abb-7d62-86b3-de3aac95fcd4
fecha: 2026-09-06 03:10
titulo: "Busca en el catálogo de mi proveedor usando el con"
tags: [chat, agente, codex]
---

# 💬 Busca en el catálogo de mi proveedor usando el con
> **Codex** · 2026-09-06 03:10 · `01a074b2-1abb-7d62-86b3-de3aac95fcd4`

---

### 🧑 Vos  <small>2026-09-06 03:10</small>

Busca en el catálogo de mi proveedor, usando el conector de AutoDS, productos que:

- Solucionen un problema real en los nichos de salud, belleza o cuidado personal
- No se puedan encontrar en un supermercado o en cualquier tienda física
- Tengan un valor percibido alto, para que se puedan vender por al menos 3 veces su coste
- Cuesten entre 5 y 30 dólares y sean pequeños y fáciles de enviar
- Ya estén generando ventas

Explora más de 1.000 productos y entrégame los 50 mejores en un dashboard interactivo con margen, coste, tiempo de envío, competencia y una nota final para cada uno.

### 🤖 Codex  <small>2026-09-06 03:10</small>

I'll start by checking whether the AutoDS connector is actually available in this session.

### 🤖 Codex  <small>2026-09-06 03:10</small>

[external_agent_tool_call: Bash]
description: Check MCP config and research pipeline dir
command: ls ~/.claude/mcp*.json 2>/dev/null; ls ~/Claude/investigacion-productos 2>/dev/null | head -30
[/external_agent_tool_call]

### 🤖 Codex  <small>2026-09-06 03:10</small>

[external_agent_tool_result]
/home/matiigonzz/.claude/mcp-needs-auth-cache.json
build_dashboard.py
capilar.txt
collect_capilar.log
collect.log
collect.py
collect_rasu.log
collect_state.json
collect_urg.log
collect_vida.log
collect_voltra.log
dashboard.html
ganadores.py
LEEME.md
OFERTA-kit-capilar.md
pipeline.py
products.json
__pycache__
rasuradoras.txt
raw_backup_60.jsonl
raw.jsonl
score.py
scrape.py
top10.py
urgencia.txt
vidacotidiana.txt
voltra.txt
[/external_agent_tool_result]

### 🤖 Codex  <small>2026-09-06 03:10</small>

[external_agent_tool_call: Bash]
description: Inspect configured MCP servers
command: cat ~/.claude/mcp-needs-auth-cache.json 2>/dev/null; echo "---SETTINGS---"; cat ~/.claude.json 2>/dev/null | python3 -c "import json,sys; d=json.load(sys.stdin); print(json.dumps(d.get('mcpServers',{}),indent=2)[:2000])" 2>/dev/null; echo "---PROJECT---"; cat ~/.claude.json 2>/dev/null | python3 -c "
import json,sys
d=json.load(sys.stdin)
for k,v in d.get('projects',{}).items():
    ms=v.get('mcpServers') or {}
    if ms: print(k, list(ms.keys()))
" 2>/dev/null
[/external_agent_tool_call]

### 🤖 Codex  <small>2026-09-06 03:10</small>

[external_agent_tool_result]
{"plugin:small-business:quickbooks":{"timestamp":1788573631457},"plugin:legal:docusign":{"timestamp":1788573632562},"claude.ai autods":{"timestamp":1787282453679,"id":"mcpsrv_01UqhDTK25QpDR7opXsU8ADc"},"claude.ai Slack":{"timestamp":1787282454143,"id":"mcpsrv_016AaHd491ZeLqQepEHbyb2A"}}---SETTINGS---
{}
---PROJECT---
[/external_agent_tool_result]

### 🤖 Codex  <small>2026-09-06 03:10</small>

[external_agent_tool_call: Bash]
description: Review existing product research pipeline
command: cd ~/Claude/investigacion-productos && cat LEEME.md 2>/dev/null | head -60; echo "=== products.json size ==="; wc -c products.json raw.jsonl 2>/dev/null; echo "=== collect_state ==="; head -c 500 collect_state.json
[/external_agent_tool_call]

### 🤖 Codex  <small>2026-09-06 03:10</small>

[external_agent_tool_result]
# Investigación de productos — salud, belleza y cuidado personal

## Estado honesto, en una línea

**No pude entregarte los 50 productos todavía.** Tengo 8 que cumplen tus 5 criterios,
salidos de 60 productos crudos. Falta catálogo, y te explico exactamente por qué.

## Qué pasó con AutoDS

El conector de AutoDS **no está disponible en esta sesión**. Está registrado en tu
cuenta de claude.ai (`claude.ai autods`) pero figura como "necesita autenticación",
y las herramientas del conector se cargan sólo al arrancar la sesión. O sea: por más
que lo reconectes ahora, esta sesión no lo va a ver.

Como plan B fui al catálogo que está **debajo** de AutoDS (AliExpress). Ahí sí saqué
productos reales, pero el sitio corta el acceso automático cuando detecta muchas
consultas seguidas. Tu IP quedó marcada. Dejé un recolector corriendo **muy lento**
(1 consulta cada 5 minutos) que va juntando catálogo solo, sin forzar nada.

**Lo que NO hice: rellenar la lista con 50 productos inventados.** Un dashboard lindo
con costos, márgenes y ventas ficticias es peor que no tener nada, porque comprarías
stock en base a números que me inventé.

## Cómo llegamos a los 50 (elegí una)

### Opción rápida y segura — exportar de AutoDS (recomendada)
Vos ya pagás AutoDS y ahí están los datos buenos: costo real, tiempo de envío real,
ventas del proveedor.

1. Entrá a AutoDS, a la sección de productos / investigación de productos.
2. Poné los filtros: precio 5 a 30 USD, categoría salud / belleza / cuidado personal.
3. Buscá el botón de exportar a CSV (suele estar arriba a la derecha).
4. Guardá el archivo y decime dónde quedó.

Después corro esto y el dashboard se llena con datos exactos:

```bash
cd ~/Claude/investigacion-productos && python3 pipeline.py --csv /ruta/al/export.csv && python3 build_dashboard.py
```

### Opción lenta — esperar al recolector
Ya está corriendo en segundo plano y es reanudable. Cuando junte más, corré:

```bash
cd ~/Claude/investigacion-productos && python3 pipeline.py && python3 build_dashboard.py
```

## Ver el dashboard

```bash
xdg-open ~/Claude/investigacion-productos/dashboard.html
```

## Lo importante: qué es dato y qué es supuesto mío

Esto es lo que más te conviene entender antes de comprar nada.

| Columna | Origen | Confiar |
|---|---|---|
| Coste | **Dato real** del catálogo | Sí |
=== products.json size ===
  12936 products.json
2765087 raw.jsonl
2778023 total
=== collect_state ===
{"done": [["beard straightener brush heated", 2], ["pubic hair trimmer men", 1], ["usb desk vacuum crumb sweeper", 1], ["hair dryer diffuser travel", 1], ["face shaver women facial hair", 2], ["ear wax removal camera", 1], ["electric razor bald head shaver", 1], ["mini shaver portable travel pocket", 2], ["trimmer ceramic blade grooming", 3], ["lint remover electric fabric shaver", 1], ["tongue cleaner scraper", 1], ["neck massager cervical pain relief", 1], ["electric shaver women body", 1], ["
[/external_agent_tool_result]

### 🤖 Codex  <small>2026-09-06 03:10</small>

[external_agent_tool_call: Bash]
description: Check accumulated product data volume
command: cd ~/Claude/investigacion-productos && echo "raw.jsonl lines: $(wc -l < raw.jsonl)"; echo "backup60 lines: $(wc -l < raw_backup_60.jsonl)"; echo "=== queries done ==="; python3 -c "
import json
d=json.load(open('collect_state.json'))
print('queries done:', len(d.get('done',[])))
print('keys:', list(d.keys()))
"; echo "=== collector running? ==="; pgrep -af "collect.py" || echo "NO collector process"; echo "=== last log lines ==="; tail -5 collect.log
[/external_agent_tool_call]

### 🤖 Codex  <small>2026-09-06 03:10</small>

[external_agent_tool_result]
raw.jsonl lines: 3822
backup60 lines: 60
=== queries done ===
queries done: 62
keys: ['done']
=== collector running? ===
290215 /bin/bash -c source /home/matiigonzz/.claude/shell-snapshots/snapshot-bash-1788575309633-6achkb.sh 2>/dev/null || true && shopt -u extglob 2>/dev/null || true && { \builtin unalias -- 'unsetenv'; \builtin unset -f -- 'unsetenv'; } >/dev/null 2>&1 || true && eval 'cd ~/Claude/investigacion-productos && echo "raw.jsonl lines: $(wc -l < raw.jsonl)"; echo "backup60 lines: $(wc -l < raw_backup_60.jsonl)"; echo "=== queries done ==="; python3 -c " import json d=json.load(open('"'"'collect_state.json'"'"')) print('"'"'queries done:'"'"', len(d.get('"'"'done'"'"',[]))) print('"'"'keys:'"'"', list(d.keys())) "; echo "=== collector running? ==="; pgrep -af "collect.py" || echo "NO collector process"; echo "=== last log lines ==="; tail -5 collect.log' && pwd -P >| /tmp/claude-63da-cwd
=== last log lines ===
[14/271] items=642 ritmo=176s bloqueos=7   
[bloqueo #8] enfriando 663s, nuevo ritmo 264s

[bloqueo #9] enfriando 747s, nuevo ritmo 300s
[17/271] items=702 ritmo=285s bloqueos=9   [18/271] items=762 ritmo=271s bloqueos=9   [19/271] items=822 ritmo=257s bloqueos=9   [20/271] items=882 ritmo=244s bloqueos=9
[/external_agent_tool_result]

### 🤖 Codex  <small>2026-09-06 03:10</small>

[external_agent_tool_call: Bash]
description: Inspect raw scraped product structure
command: cd ~/Claude/investigacion-productos && head -1 raw.jsonl | python3 -m json.tool | head -40; echo "=== unique ids ==="; python3 -c "
import json
ids=set(); n=0
for line in open('raw.jsonl'):
    try: d=json.loads(line)
    except: continue
    n+=1
    ids.add(d.get('id') or d.get('product_id') or d.get('itemId'))
print('lines',n,'unique',len(ids))
"
[/external_agent_tool_call]

### 🤖 Codex  <small>2026-09-06 03:10</small>

[external_agent_tool_result]
{
    "query": "facial massager",
    "id": "1005008677525892",
    "title": "Masajeador facial de s\u00e1ndalo, masajeador facial para nariz y cara, herramienta para aliviar los ojos, masaje meridiano Facial de caracol, 1 ud.",
    "currency": "USD",
    "price": 3.78,
    "original_price": 8.03,
    "discount": 52,
    "rating": 4.8,
    "sold_raw": "10.000+ vendidos",
    "image": "//ae-pic-a1.aliexpress-media.com/kf/Saa73b28953fb424e850932b4e7db9698E.jpg",
    "url": "https://www.aliexpress.com/item/1005008677525892.html"
}
=== unique ids ===
lines 3822 unique 3294
[/external_agent_tool_result]

### 🤖 Codex  <small>2026-09-06 03:10</small>

[external_agent_tool_call: Bash]
description: Review scoring logic
command: cd ~/Claude/investigacion-productos && wc -l pipeline.py score.py build_dashboard.py collect.py && echo "=== score.py ===" && cat score.py
[/external_agent_tool_call]

### 🤖 Codex  <small>2026-09-06 03:10</small>

[external_agent_tool_result]
  398 pipeline.py
  174 score.py
  263 build_dashboard.py
  251 collect.py
 1086 total
=== score.py ===
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
            continue          # ...
[/external_agent_tool_result]

### 🤖 Codex  <small>2026-09-06 03:10</small>

Good news: there's prior work here with real scraped data. Let me check the AutoDS connector status definitively, then run the scoring pipeline.

### 🤖 Codex  <small>2026-09-06 03:10</small>

[external_agent_tool_call: Bash]
description: Run scoring pipeline on accumulated data
command: cd ~/Claude/investigacion-productos && python3 score.py
[/external_agent_tool_call]

### 🤖 Codex  <small>2026-09-06 03:10</small>

[external_agent_tool_result]
crudo: 3294 | pasan filtros: 7 | entregados: 7
[/external_agent_tool_result]

### 🤖 Codex  <small>2026-09-06 03:10</small>

Only 7 of 3,294 pass. Let me diagnose the funnel before trusting that.

### 🤖 Codex  <small>2026-09-06 03:10</small>

[external_agent_tool_call: Bash]
description: Diagnose filter funnel dropoff
command: cd ~/Claude/investigacion-productos && python3 -c "
import json,re,collections
rows={}
for l in open('raw.jsonl',encoding='utf-8'):
    r=json.loads(l); rows.setdefault(r['id'],r)
rows=list(rows.values())
print('total unicos:',len(rows))
def parse_sold(s):
    if not s: return 0
    t=s.lower().replace('.','').replace(',','')
    m=re.search(r'(\d+)',t)
    if not m: return 0
    n=int(m.group(1))
    if 'mil' in t or 'k+' in t: n*=1000
    return n
precio=[r for r in rows if r.get('price') and 5<=r['price']<=30]
print('pasan precio 5-30:',len(precio))
sold=[r for r in precio if parse_sold(r.get('sold_raw'))>=50]
print('  + vendidos>=50:',len(sold))
rat=[r for r in sold if not r.get('rating') or r['rating']>=4.3]
print('  + rating>=4.3:',len(rat))
print()
print('--- sold_raw vacios en el set de precio:',sum(1 for r in precio if not r.get('sold_raw')))
print('--- ejemplos sold_raw:',collections.Counter(str(r.get('sold_raw'))[:25] for r in precio).most_common(12))
"

[/external_agent_tool_call]

### 🤖 Codex  <small>2026-09-06 03:10</small>

[external_agent_tool_result]
total unicos: 3294
pasan precio 5-30: 32
  + vendidos>=50: 8
  + rating>=4.3: 7

--- sold_raw vacios en el set de precio: 4
--- ejemplos sold_raw: [('', 4), ('2 vendidos', 3), ('5 vendidos', 2), ('3 vendidos', 2), ('162 vendidos', 2), ('7 vendidos', 2), ('11 vendidos', 2), ('30 vendidos', 1), ('71 vendidos', 1), ('295 vendidos', 1), ('4 vendidos', 1), ('8 vendidos', 1)]
[/external_agent_tool_result]

### 🤖 Codex  <small>2026-09-06 03:10</small>

The bottleneck is price — only 32 of 3,294 land in $5–30. Let me check the price distribution.

### 🤖 Codex  <small>2026-09-06 03:10</small>

[external_agent_tool_call: Bash]
description: Analyze price distribution in scraped data
command: cd ~/Claude/investigacion-productos && python3 -c "
import json,collections
rows={}
for l in open('raw.jsonl',encoding='utf-8'):
    r=json.loads(l); rows.setdefault(r['id'],r)
rows=list(rows.values())
b=collections.Counter()
for r in rows:
    p=r.get('price')
    if p is None: b['none']+=1; continue
    if p<1: b['<1']+=1
    elif p<2: b['1-2']+=1
    elif p<3: b['2-3']+=1
    elif p<5: b['3-5']+=1
    elif p<10: b['5-10']+=1
    elif p<30: b['10-30']+=1
    else: b['>30']+=1
for k in ['none','<1','1-2','2-3','3-5','5-10','10-30','>30']:
    print(f'{k:>6}: {b[k]}')
print()
print('precio medio:', round(sum(r[\"price\"] for r in rows if r.get(\"price\"))/len(rows),2))
print()
print('--- original_price (antes de descuento) en rango 5-30:')
n=sum(1 for r in rows if r.get('original_price') and 5<=r['original_price']<=30)
print(n)
"

[/external_agent_tool_call]

### 🤖 Codex  <small>2026-09-06 03:10</small>

[external_agent_tool_result]
  none: 0
    <1: 0
   1-2: 1
   2-3: 2
   3-5: 9
  5-10: 19
 10-30: 13
   >30: 3250

precio medio: 97833.24

--- original_price (antes de descuento) en rango 5-30:
30
[/external_agent_tool_result]

### 🤖 Codex  <small>2026-09-06 03:10</small>

Price data is corrupted — mean price is $97,833. The scraper broke partway. Let me find where.

### 🤖 Codex  <small>2026-09-06 03:10</small>

[external_agent_tool_call: Bash]
description: Trace where price parsing broke
command: cd ~/Claude/investigacion-productos && python3 -c "
import json
rows=[json.loads(l) for l in open('raw.jsonl',encoding='utf-8')]
print('=== primeras 3 ===')
for r in rows[:3]: print(r['currency'], r['price'], '|', r['title'][:50])
print()
print('=== linea 100, 500, 1500, 3000, ultima ===')
for i in [100,500,1500,3000,len(rows)-1]:
    r=rows[i]; print(i, r['currency'], r['price'], r.get('original_price'), '|', r['query'][:28], '|', r['title'][:45])
print()
import collections
print('monedas:', collections.Counter(r['currency'] for r in rows))
print()
# donde empieza a romperse
for i,r in enumerate(rows):
    if r['price'] and r['price']>1000:
        print('primer precio >1000 en linea', i, ':', r['currency'], r['price'], r['title'][:50]); break
"

[/external_agent_tool_call]

### 🤖 Codex  <small>2026-09-06 03:10</small>

[external_agent_tool_result]
=== primeras 3 ===
USD 3.78 | Masajeador facial de sándalo, masajeador facial pa
USD 38.43 | Dispositivo Multifuncional de Lifting Facial, Masa
USD 6.9 | Masajeador Facial Antiarrugas 2026, Dispositivo Re

=== linea 100, 500, 1500, 3000, ultima ===
100 ARS 5941 13036.98 | silicone face cleansing brus | Cepillo de Silicona para Limpieza Facial, Exf
500 ARS 8832 18400 | skin tag remover device | NUEVO Kit de Eliminación de Verrugas 2 en 1, 
1500 ARS 9871 21935.56 | handheld bag sealer usb | Mini máquina de sellado, sellador térmico rec
3000 ARS 4144 8900.29 | face shaver women facial hai | Pinzas invisibles para el cabello, bandas par
3821 ARS 407987 971397.62 | hair removal razor women ele | Instrumento Multifuncional para el Cuidado de

monedas: Counter({'ARS': 3762, 'USD': 60})

primer precio >1000 en linea 60 : ARS 27649 Juego de 4 Uds. De cepillo exfoliante suave de sil
[/external_agent_tool_result]

### 🤖 Codex  <small>2026-09-06 03:10</small>

AliExpress silently switched currency to Argentine pesos after the first 60 items. 3,762 records are ARS, not USD. Let me derive the exact rate from overlapping products.

### 🤖 Codex  <small>2026-09-06 03:10</small>

[external_agent_tool_call: Bash]
description: Find products priced in both currencies to derive rate
command: cd ~/Claude/investigacion-productos && python3 -c "
import json,collections,statistics
rows=[json.loads(l) for l in open('raw.jsonl',encoding='utf-8')]
usd={}; ars={}
for r in rows:
    (usd if r['currency']=='USD' else ars).setdefault(r['id'], r)
common=set(usd)&set(ars)
print('productos con precio en AMBAS monedas:', len(common))
rates=[]
for i in common:
    if usd[i]['price'] and ars[i]['price']:
        rates.append(ars[i]['price']/usd[i]['price'])
        print(f\"  {usd[i]['price']:>8} USD  <->  {ars[i]['price']:>10} ARS   = {ars[i]['price']/usd[i]['price']:.1f}\")
if rates:
    print()
    print('rate mediana:', round(statistics.median(rates),1))
"

[/external_agent_tool_call]

### 🤖 Codex  <small>2026-09-06 03:10</small>

[external_agent_tool_result]
productos con precio en AMBAS monedas: 6
     22.64 USD  <->       33900 ARS   = 1497.3
     11.57 USD  <->       17330 ARS   = 1497.8
     38.43 USD  <->       57549 ARS   = 1497.5
     13.85 USD  <->       20746 ARS   = 1497.9
     61.04 USD  <->       88779 ARS   = 1454.4
      3.78 USD  <->        5651 ARS   = 1495.0

rate mediana: 1497.4
[/external_agent_tool_result]

### 🤖 Codex  <small>2026-09-06 03:10</small>

Rate derived empirically: **1497.4 ARS/USD** (consistent across all 6 overlaps). Let me fix the normalization and re-check the funnel.

### 🤖 Codex  <small>2026-09-06 03:10</small>

[external_agent_tool_call: Bash]
description: Re-run funnel with currency normalization
command: cd ~/Claude/investigacion-productos && python3 -c "
import json,re,collections
RATE=1497.4
rows={}
for l in open('raw.jsonl',encoding='utf-8'):
    r=json.loads(l)
    if r['currency']=='ARS':
        if r.get('price'): r['price']=round(r['price']/RATE,2)
        if r.get('original_price'): r['original_price']=round(r['original_price']/RATE,2)
        r['currency']='USD'
    rows.setdefault(r['id'],r)
rows=list(rows.values())
print('total unicos:',len(rows))
def parse_sold(s):
    if not s: return 0
    t=s.lower().replace('.','').replace(',','')
    m=re.search(r'(\d+)',t)
    if not m: return 0
    n=int(m.group(1))
    if 'mil' in t or 'k+' in t: n*=1000
    return n
b=collections.Counter()
for r in rows:
    p=r['price']
    b['<5' if p<5 else '5-30' if p<=30 else '>30']+=1
print('precio:',dict(b))
pr=[r for r in rows if 5<=r['price']<=30]
print('pasan precio:',len(pr))
s=[r for r in pr if parse_sold(r.get('sold_raw'))>=50]
print(' + vendidos>=50:',len(s))
rr=[r for r in s if not r.get('rating') or r['rating']>=4.3]
print(' + rating>=4.3:',len(rr))
print()
print('nichos/queries distintos en los que pasan:',len(set(r['query'] for r in rr)))
" 

[/external_agent_tool_call]

### 🤖 Codex  <small>2026-09-06 03:10</small>

[external_agent_tool_result]
total unicos: 3294
precio: {'<5': 409, '>30': 812, '5-30': 2073}
pasan precio: 2073
 + vendidos>=50: 871
 + rating>=4.3: 757

nichos/queries distintos en los que pasan: 45
[/external_agent_tool_result]

### 🤖 Codex  <small>2026-09-06 03:10</small>

Funnel now works: 3,294 → 2,073 in price → 871 with sales → **757 qualified** across 45 product categories. Let me check what fields I actually have (especially shipping).

### 🤖 Codex  <small>2026-09-06 03:10</small>

[external_agent_tool_call: Bash]
description: List available data fields and query coverage
command: cd ~/Claude/investigacion-productos && python3 -c "
import json,collections
keys=collections.Counter()
for l in open('raw.jsonl',encoding='utf-8'):
    keys.update(json.loads(l).keys())
print('campos disponibles:'); [print(' ',k,v) for k,v in keys.most_common()]
"; echo "=== queries cubiertos ==="; python3 -c "
import json,collections
qs=collections.Counter()
for l in open('raw.jsonl',encoding='utf-8'):
    qs[json.loads(l)['query']]+=1
print(len(qs),'queries')
for q,n in qs.most_common(): print(f'  {n:>4}  {q}')
" | head -70
[/external_agent_tool_call]

### 🤖 Codex  <small>2026-09-06 03:10</small>

[external_agent_tool_result]
campos disponibles:
  query 3822
  id 3822
  title 3822
  currency 3822
  price 3822
  original_price 3822
  discount 3822
  rating 3822
  sold_raw 3822
  image 3822
  url 3822
  page 3762
  tax_rate 3762
  launch 3762
  sp_sources 3762
  sp_texts 3762
=== queries cubiertos ===
45 queries
   180  face shaver women facial hair
   180  hair removal razor women electric
   180  trimmer ceramic blade grooming
   180  nose ear hair trimmer electric
   180  bikini trimmer women intimate
   120  dark spot corrector serum roller
   120  pubic hair trimmer men
   120  body groomer trimmer men waterproof
   120  electric shaver men rechargeable portable
   120  beard trimmer kit cordless
   120  mini shaver portable travel pocket
   120  beard straightener brush heated
   120  electric shaver women body
   120  back shaver long handle men
    60  facial massager
    60  silicone face cleansing brush
    60  ear wax removal camera
    60  muscle massage gun mini
    60  sleep aid device insomnia
    60  tongue cleaner scraper
    60  skin tag remover device
    60  shoulder posture strap
    60  posture trainer wearable
    60  tens unit pain relief
    60  period pain relief device
    60  acne blue light pen
    60  menstrual pain relief device heating
    60  carpal tunnel wrist relief
    60  neck massager cervical pain relief
    60  baby thermometer forehead digital
    60  baby nasal aspirator electric
    60  anti snoring device mouthpiece
    60  hair dryer diffuser travel
    60  rechargeable hand warmer usb
    60  lint remover electric fabric shaver
    60  electric candle lighter usb rechargeable
    60  handheld bag sealer usb
    60  usb desk vacuum crumb sweeper
    60  skull shaver head bald
    60  electric razor bald head shaver
    60  manscaping groomer kit
    60  epilator women rechargeable
    60  hair clipper cordless professional
    60  eyebrow trimmer electric precision
    42  ear wax removal
[/external_agent_tool_result]

### 🤖 Codex  <small>2026-09-06 03:10</small>

No shipping field in the data. Let me check the unexplored fields in case shipping info is hiding there.

### 🤖 Codex  <small>2026-09-06 03:10</small>

[external_agent_tool_call: Bash]
description: Inspect remaining fields for shipping data
command: cd ~/Claude/investigacion-productos && python3 -c "
import json,collections
launch=collections.Counter(); tax=collections.Counter(); srcs=collections.Counter(); texts=collections.Counter()
for l in open('raw.jsonl',encoding='utf-8'):
    r=json.loads(l)
    if 'launch' in r: launch[str(r['launch'])[:40]]+=1
    if 'tax_rate' in r: tax[str(r['tax_rate'])[:30]]+=1
    if 'sp_sources' in r: srcs[str(r['sp_sources'])[:60]]+=1
    if 'sp_texts' in r: texts[str(r['sp_texts'])[:70]]+=1
print('launch:',launch.most_common(5)); print()
print('tax_rate:',tax.most_common(5)); print()
print('sp_sources:',srcs.most_common(6)); print()
print('sp_texts:',texts.most_common(8))
"
[/external_agent_tool_call]

### 🤖 Codex  <small>2026-09-06 03:10</small>

[external_agent_tool_result]
launch: [('2026-08-11 00:00:00', 39), ('2026-08-14 00:00:00', 32), ('2026-07-24 00:00:00', 29), ('2026-08-12 00:00:00', 28), ('2026-07-28 00:00:00', 25)]

tax_rate: [('0.21', 3290), ('0', 472)]

sp_sources: [("['choice_atm', 'bigSale_atm', 'bigSale_discount', 'platformF", 1164), ("['choice_atm', 'bigSale_atm', 'welcomedeal_test', 'platformF", 238), ("['common_brand_plus_atm', 'bigSale_atm', 'welcomedeal_test',", 185), ("['choice_atm', 'card_super_deals_bigsale_pop_atm', 'earlyBir", 166), ('[]', 157), ("['choice_atm', 'platformFreeShipping_atm']", 146)]

sp_texts: [("['Envío gratis a partir de $22.000']", 163), ('[]', 162), ("['Envío gratis a partir de $22.000', 'El mejor precio en ofertas simil", 78), ("['Oferta anticipada, solo quedan 1', 'Envío gratis a partir de $22.000", 74), ("['-$6.987,68 · Nuevo comprador', 'Envío gratis a partir de $22.000']", 66), ("['Oferta anticipada, solo quedan 4', 'Envío gratis a partir de $22.000", 58), ("['Envío gratis a partir de $22.000', '-1% con monedas']", 47), ("['-2% con monedas']", 33)]
[/external_agent_tool_result]

### 🤖 Codex  <small>2026-09-06 03:10</small>

Found real signals I can use: `sp_sources` flags AliExpress **Choice** (faster tracked shipping) and free shipping, and `launch` gives product age. Let me quantify those.

### 🤖 Codex  <small>2026-09-06 03:10</small>

[external_agent_tool_call: Bash]
description: Quantify Choice and shipping flags
command: cd ~/Claude/investigacion-productos && python3 -c "
import json,collections,ast
RATE=1497.4
rows={}
for l in open('raw.jsonl',encoding='utf-8'):
    r=json.loads(l)
    if r['currency']=='ARS':
        r['price']=round(r['price']/RATE,2)
        if r.get('original_price'): r['original_price']=round(r['original_price']/RATE,2)
    rows.setdefault(r['id'],r)
rows=list(rows.values())
ch=fs=0; lau=0
for r in rows:
    s=r.get('sp_sources') or []
    if isinstance(s,str): s=ast.literal_eval(s)
    if any('choice' in x for x in s): ch+=1
    if any('FreeShipping' in x for x in s): fs+=1
    if r.get('launch'): lau+=1
print('total',len(rows))
print('Choice:',ch, f'({ch*100//len(rows)}%)')
print('FreeShipping flag:',fs)
print('con fecha launch:',lau)
"
[/external_agent_tool_call]

### 🤖 Codex  <small>2026-09-06 03:10</small>

[external_agent_tool_result]
total 3294
Choice: 2182 (66%)
FreeShipping flag: 1895
con fecha launch: 3234
[/external_agent_tool_result]

### 🤖 Codex  <small>2026-09-06 03:10</small>

Now I have everything I need. Let me write an improved selector that fixes the currency bug, enforces all 5 criteria, and uses the real Choice/launch signals.

### 🤖 Codex  <small>2026-09-06 03:10</small>

[external_agent_tool_call: Write]
file: /home/matiigonzz/Claude/investigacion-productos/seleccion.py
[/external_agent_tool_call]

### 🤖 Codex  <small>2026-09-06 03:10</small>

[external_agent_tool_result]
File created successfully at: /home/matiigonzz/Claude/investigacion-productos/seleccion.py (file state is current in your context — no need to Read it back)
[/external_agent_tool_result]

### 🤖 Codex  <small>2026-09-06 03:10</small>

[external_agent_tool_call: Bash]
description: Run improved product selection
command: cd ~/Claude/investigacion-productos && python3 seleccion.py
[/external_agent_tool_call]

### 🤖 Codex  <small>2026-09-06 03:10</small>

[external_agent_tool_result]
crudo 3294 | califican 593 | entregados 50
descartes: {'precio fuera de 5-30': 1149, 'sin ventas suficientes': 1043, 'rating bajo': 104, 'no llega a 3x': 110, 'fuera de nicho': 295}
categorias en el top50: 18
nichos: {'Higiene': 4, 'Piel': 8, 'Salud femenina': 8, 'Sueno': 5, 'Dolor': 14, 'Salud bebe': 5, 'Cuidado intimo': 4, 'Afeitado': 1, 'Depilacion': 1}
[/external_agent_tool_result]

### 🤖 Codex  <small>2026-09-06 03:10</small>

593 qualify across 18 categories. Let me sanity-check the top entries before building the dashboard.

### 🤖 Codex  <small>2026-09-06 03:10</small>

[external_agent_tool_call: Bash]
description: Verify top product results
command: cd ~/Claude/investigacion-productos && python3 -c "
import json
d=json.load(open('productos_top50.json'))
print(f\"{'#':>2} {'score':>5} {'coste':>6} {'pvp':>6} {'mult':>4} {'vend':>7} {'rat':>4} {'comp':>6} {'envio':>11}  titulo\")
for i,p in enumerate(d['productos'][:15],1):
    print(f\"{i:>2} {p['score']:>5} {p['coste']:>6} {p['pvp_sugerido']:>6} {p['multiplo']:>4} {p['vendidos']:>7} {str(p['rating']):>4} {p['competencia']:>6} {p['envio']:>11}  {p['titulo'][:58]}\")
print()
print('rango coste:', min(p['coste'] for p in d['productos']), '-', max(p['coste'] for p in d['productos']))
print('rango score:', min(p['score'] for p in d['productos']), '-', max(p['score'] for p in d['productos']))
print('todos >=3x:', all(p['multiplo']>=3 for p in d['productos']))
print('todos con ventas:', min(p['vendidos'] for p in d['productos']))
"
[/external_agent_tool_call]

### 🤖 Codex  <small>2026-09-06 03:10</small>

[external_agent_tool_result]
 # score  coste    pvp mult    vend  rat   comp       envio  titulo
 1  84.3   7.78  31.12  4.0   10000  4.7   Baja  15-25 dias  Limpiador de cera de oídos inalámbrico con cámara, endosco
 2  82.5  16.93  71.11  4.2     800    5   Baja  25-45 dias  Nuevo Lápiz de Luz Azul 2026 para Solucionar la Insuficien
 3  82.4   12.7   50.8  4.0   10000  4.5   Baja  15-25 dias  Estimulador muscular eléctrico de pulso EMS, masajeador co
 4  82.0  17.16  68.64  4.0    5000  4.7   Baja  15-25 dias  Auriculares para dormir con Bluetooth, máscara de ojos 3D,
 5  81.2  18.27  76.73  4.2    2000  4.6   Baja  15-25 dias  Fisioterapia Tens Estimulador muscular Acupuntura eléctric
 6  81.0    7.4   29.6  4.0    4000  4.7   Baja  15-25 dias  Limpiador de oídos Visual inteligente, palillos para los o
 7  80.7  12.81  51.24  4.0    3000  4.7   Baja  15-25 dias  El monitor multifunción 4 en 1 mide Hemoglobina, Cetonas e
 8  80.6  19.87  77.49  3.9    2000  4.8   Baja  15-25 dias  Kit de herramientas de eliminación automática de marcas en
 9  80.6    8.7   34.8  4.0    5000  4.6   Baja  15-25 dias  Tiras nasales antironquidos para corrección de respiración
10  80.0  15.98  63.92  4.0    5000  4.4   Baja  15-25 dias  Dispositivo de hipnosis de pulso de microcorriente, tratam
11  79.7  10.21  42.88  4.2     500  4.6   Baja  15-25 dias  Instrumento masajeador de pulso Tens eléctrico de doble sa
12  79.3  11.51  48.34  4.2      68    5   Baja  15-25 dias  Rodillo de masaje de espalda de madera, herramientas de ma
13  79.1  13.67  54.68  4.0    1000  4.6   Baja  15-25 dias  Cinturón de palacio de masaje calentado portátil, disposit
14  79.0  19.14  80.39  4.2    1000  4.8   Baja  25-45 dias  Sigue usando, las verrugas se desvanecerán de forma natura
15  78.8  12.16  48.64  4.0     700  4.7   Baja  15-25 dias  Limpiador de oídos visual inalámbrico con cámara, kit de o

rango coste: 6.07 - 23.35
rango score: 65.3 - 84.3
todos >=3x: True
todos con ventas: 68
[/external_agent_tool_result]

### 🤖 Codex  <small>2026-09-06 03:10</small>

Results are real, but I spot a quality problem: some listings don't match their search category (e.g. #12 is a wooden roller scored as a TENS device), and a few are regulated medical-claim products. Let me add title validation and a risk flag.

### 🤖 Codex  <small>2026-09-06 03:10</small>

[external_agent_tool_call: Bash]
description: Review all 50 titles vs categories for mismatches
command: cd ~/Claude/investigacion-productos && python3 -c "
import json
d=json.load(open('productos_top50.json'))
for i,p in enumerate(d['productos'],1):
    print(f\"{i:>2} [{p['categoria'][:26]:<26}] {p['titulo'][:70]}\")
" 
[/external_agent_tool_call]

### 🤖 Codex  <small>2026-09-06 03:10</small>

[external_agent_tool_result]
 1 [ear wax removal camera    ] Limpiador de cera de oídos inalámbrico con cámara, endoscopio seguro p
 2 [acne blue light pen       ] Nuevo Lápiz de Luz Azul 2026 para Solucionar la Insuficiencia Venosa, 
 3 [period pain relief device ] Estimulador muscular eléctrico de pulso EMS, masajeador corporal para 
 4 [sleep aid device insomnia ] Auriculares para dormir con Bluetooth, máscara de ojos 3D, reproductor
 5 [tens unit pain relief     ] Fisioterapia Tens Estimulador muscular Acupuntura eléctrica masaje cor
 6 [ear wax removal camera    ] Limpiador de oídos Visual inteligente, palillos para los oídos HD, oto
 7 [period pain relief device ] El monitor multifunción 4 en 1 mide Hemoglobina, Cetonas en Sangre, Gl
 8 [skin tag remover device   ] Kit de herramientas de eliminación automática de marcas en la piel 2 e
 9 [period pain relief device ] Tiras nasales antironquidos para corrección de respiración, expansión 
10 [sleep aid device insomnia ] Dispositivo de hipnosis de pulso de microcorriente, tratamiento de rel
11 [tens unit pain relief     ] Instrumento masajeador de pulso Tens eléctrico de doble salida, Estimu
12 [tens unit pain relief     ] Rodillo de masaje de espalda de madera, herramientas de masaje de espa
13 [menstrual pain relief devi] Cinturón de palacio de masaje calentado portátil, dispositivo de cintu
14 [tens unit pain relief     ] Sigue usando, las verrugas se desvanecerán de forma natural, dejando l
15 [ear wax removal camera    ] Limpiador de oídos visual inalámbrico con cámara, kit de otoscopio par
16 [skin tag remover device   ] Pluma de Plasma eliminador de marcas en la piel, eliminador de verruga
17 [menstrual pain relief devi] Bolsa de agua caliente más cálida y bonita para el dolor del período, 
18 [menstrual pain relief devi] Almohadilla térmica para calambres menstruales, gran capacidad de 5000
19 [ear wax removal camera    ] Generación-2, limpiador de cera de oídos Visual, cámara segura, elimin
20 [acne blue light pen       ] Lápiz de Terapia de Luz Azul Nano de 830nm, Dispositivo Portátil de Cu
21 [skin tag remover device   ] Kit 2 en 1 para la eliminación de verrugas y lunares sin dolor, equipo
22 [skin tag remover device   ] Kit de eliminación automática de etiquetas de piel para etiquetas de p
23 [period pain relief device ] Cinturón de calambres para el período de calefacción eléctrica, 3 nive
24 [menstrual pain relief devi] Masajeador eléctrico de cintura, masajeador de calambres, cinturón cal
25 [muscle massage gun mini   ] Pistola dispensadora de mezcla de impresión Dental 1:1/1:2 pistola dis
26 [sleep aid device insomnia ] Nuevo 1 Juego de dispositivo de hipnosis de pulso de microcorriente, a
27 [acne blue light pen       ] La última generación de bolígrafos para eliminar verrugas con luz azul
28 [sleep aid device insomnia ] Ayuda para dormir, alivio del insomnio, microcorriente, hipnosis portá
29 [acne blue light pen       ] Máquina Facial con luz azul, eliminación de arrugas y acné, pluma láse
30 [neck massager cervical pai] Camilla relajante para cuello y hombros, dispositivo de tracción quiro
31 [baby nasal aspirator elect] Aspirador Nasal Eléctrico para Bebés 2026, Nuevo Modelo, Versión Recar
32 [muscle massage gun mini   ] Masajeador de Fascia muscular portátil de 6 velocidades, máquina de ma
33 [baby nasal aspirator elect] Dispositivo Inteligente de Fototerapia Nasal con Luz Roja e Infrarroja
34 [neck massager cervical pai] Almohada ensanchadora de espalda, masaje de cintura, masajeador de sop
35 [baby nasal aspirator elect] Aspirador Nasal Eléctrico para Bebés, Aspirador de Nariz Automático pa
36 [baby nasal aspirator elect] Aspirador Nasal eléctrico para bebé, nuevo patrón, versión de carga, a
37 [manscaping groomer kit    ] Cortadora de pelo eléctrica portátil 2 en 1 para hombres, cortadora de
38 [carpal tunnel wrist relief] Pinza de mano pesada para recuperación muscular, dispositivo de entren
39 [neck massager cervical pai] Masajeador de Cuello Recargable F2, Dispositivo Por...
[/external_agent_tool_result]

### 🤖 Codex  <small>2026-09-06 03:10</small>

Confirmed — the search engine returned genuinely wrong products: **#25 is a dental mixing gun**, **#41 is 100 dental prophy brushes**, **#42 is silicone cable**. Plus regulated medical devices (#7 hemoglobin monitor, #2 "venous insufficiency"). Let me add a title validation layer.

### 🤖 Codex  <small>2026-09-06 03:10</small>

[external_agent_tool_call: Read]
file: /home/matiigonzz/Claude/investigacion-productos/seleccion.py
[/external_agent_tool_call]

### 🤖 Codex  <small>2026-09-06 03:10</small>

[external_agent_tool_result]
128	        return 0
129	    t = s.lower().replace(".", "").replace(",", "")
130	    m = re.search(r"(\d+)", t)
131	    if not m:
132	        return 0
133	    n = int(m.group(1))
134	    if "mil" in t or "k+" in t:
135	        n *= 1000
136	    return n
137	
138	
139	def flags(r):
140	    s = r.get("sp_sources") or []
141	    if isinstance(s, str):
142	        try: s = ast.literal_eval(s)
143	        except Exception: s = []
144	    txt = " ".join(s)
145	    return ("choice" in txt), ("FreeShipping" in txt)
146	
147	
[/external_agent_tool_result]

### 🤖 Codex  <small>2026-09-06 03:10</small>

[external_agent_tool_call: Bash]
description: Add title validation and risk flags, re-run
command: cd ~/Claude/investigacion-productos && python3 - <<'PY'
import re
p='seleccion.py'
s=open(p,encoding='utf-8').read()

valida = '''
# --- Validacion por titulo -------------------------------------------------
# El buscador de AliExpress devuelve listados que NO son lo que se busco
# (una pistola dosificadora dental aparecio buscando "massage gun"). El titulo
# tiene que confirmar que el producto es realmente de la categoria.
VALIDA = {
    "ear wax removal camera": r"o[ií]d|oreja|cerum|otoscop|endoscop",
    "ear wax removal": r"o[ií]d|oreja|cerum|otoscop",
    "acne blue light pen": r"luz azul|acn[eé]|espinilla|fototerap|l[aá]ser facial",
    "period pain relief device": r"menstrual|per[ií]odo|regla|c[oó]lico|calambre|[uú]tero|palacio|vientre|cintura",
    "menstrual pain relief device heating": r"menstrual|per[ií]odo|regla|c[oó]lico|calambre|[uú]tero|palacio|vientre|cintura",
    "sleep aid device insomnia": r"dormir|sue[ñn]o|insomnio|hipnosis|relajac|antiestr[eé]s",
    "tens unit pain relief": r"\\btens\\b|\\bems\\b|electroestimul|estimulador|impulso|pulso|acupuntur|fisioterap",
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
BLOQUEO = r"""dental|profilaxis|impresi[oó]n dental|cable|alambre|manicur|cortau[ñn]as|
bolsa de agua|almohada|rodillo de madera|pinza de mano|fortalecedor|agarre|
tapones|auricular(?!es para dormir)|funda|repuesto|cabezal de repuesto|
soporte para tel|cargador|adaptador|bombilla|l[aá]mpara de mesa"""
BLOQUEO = re.compile("|".join(x.strip() for x in BLOQUEO.split("\\n") if x.strip()), re.I)

# Claims medicos regulados: Meta y Google restringen estos anuncios, y varios
# son directamente peligrosos (quemar un lunar puede tapar un melanoma).
RIESGO = re.compile(
    r"hemoglobin|glucosa|cet[oó]n|presi[oó]n arterial|diab[eé]t|"
    r"insuficiencia venosa|c[aá]ncer|tumor|verruga|lunar|papiloma|plasma|"
    r"diagn[oó]stic|cura[r]?\\b|tratamiento m[eé]dico", re.I)


def titulo_valido(q, titulo):
    """True si el titulo confirma la categoria y no es basura."""
    if BLOQUEO.search(titulo):
        return False
    pat = VALIDA.get(q)
    if pat and not re.search(pat, titulo, re.I):
        return False
    return True

'''
s = s.replace("def flags(r):", valida.lstrip("\n") + "\ndef flags(r):",1)

# insertar filtros en el loop
old = """        retail = RETAIL.get(q, 0.5)
        if retail >= 0.8:
            stats["se consigue en tienda fisica"] += 1; continue  # criterio 2
"""
new = """        retail = RETAIL.get(q, 0.5)
        if retail >= 0.8:
            stats["se consigue en tienda fisica"] += 1; continue  # criterio 2
        if not titulo_valido(q, r["title"]):
            stats["listado no coincide / commodity"] += 1; continue
        riesgo = bool(RIESGO.search(r["title"]))
"""
assert old in s
s = s.replace(old,new,1)

# penalizar riesgo en el score y exponer el flag
s = s.replace("""        if free_ship:
            score += 1.5""","""        if free_ship:
            score += 1.5
        if riesgo:
            score -= 14      # claims regulados: riesgo de ban publicitario""",1)
s = s.replace('''            "envio_gratis": free_ship,''','''            "envio_gratis": free_ship,
            "riesgo_regulatorio": riesgo,''',1)
open(p,'w',encoding='utf-8').write(s)
print("ok")
PY
python3 seleccion.py
[/external_agent_tool_call]

### 🤖 Codex  <small>2026-09-06 03:10</small>

[external_agent_tool_result]
ok
crudo 3294 | califican 0 | entregados 0
descartes: {'precio fuera de 5-30': 1149, 'sin ventas suficientes': 1043, 'listado no coincide / commodity': 593, 'rating bajo': 104, 'no llega a 3x': 110, 'fuera de nicho': 295}
categorias en el top50: 0
nichos: {}
[/external_agent_tool_result]

### 🤖 Codex  <small>2026-09-06 03:10</small>

The blocklist regex has an empty alternation (`||`) from my line-splitting, which matches everything. Let me fix it properly.

### 🤖 Codex  <small>2026-09-06 03:10</small>

[external_agent_tool_call: Bash]
description: Fix blocklist regex and re-run selection
command: cd ~/Claude/investigacion-productos && python3 - <<'PY'
p='seleccion.py'
s=open(p,encoding='utf-8').read()
start=s.index('BLOQUEO = r"""')
end=s.index('# Claims medicos regulados')
nuevo = '''BLOQUEO_TERMS = [
    r"dental", r"profilaxis", r"impresi[oó]n dental", r"\\bcable\\b", r"alambre",
    r"manicur", r"cortau[ñn]as", r"bolsa de agua", r"almohada",
    r"rodillo de madera", r"pinza de mano", r"fortalecedor", r"de agarre",
    r"tapones", r"\\bfunda\\b", r"repuesto", r"soporte para tel",
    r"cargador", r"adaptador", r"bombilla", r"l[aá]mpara de mesa",
]
BLOQUEO = re.compile("|".join(BLOQUEO_TERMS), re.I)

'''
s = s[:start] + nuevo + s[end:]
open(p,'w',encoding='utf-8').write(s)
PY
python3 seleccion.py
[/external_agent_tool_call]

### 🤖 Codex  <small>2026-09-06 03:10</small>

[external_agent_tool_result]
crudo 3294 | califican 452 | entregados 50
descartes: {'precio fuera de 5-30': 1149, 'sin ventas suficientes': 1043, 'rating bajo': 104, 'listado no coincide / commodity': 141, 'no llega a 3x': 110, 'fuera de nicho': 295}
categorias en el top50: 19
nichos: {'Higiene': 4, 'Sueno': 6, 'Dolor': 14, 'Piel': 10, 'Salud femenina': 5, 'Salud bebe': 5, 'Cuidado intimo': 3, 'Depilacion': 1, 'Afeitado': 2}
[/external_agent_tool_result]

### 🤖 Codex  <small>2026-09-06 03:10</small>

[external_agent_tool_call: Bash]
description: Review validated top 50
command: cd ~/Claude/investigacion-productos && python3 -c "
import json
d=json.load(open('productos_top50.json'))
for i,p in enumerate(d['productos'],1):
    r='!' if p['riesgo_regulatorio'] else ' '
    print(f\"{i:>2}{r} {p['score']:>5} \${p['coste']:>5} [{p['nicho'][:14]:<14}] {p['titulo'][:62]}\")
"
[/external_agent_tool_call]

### 🤖 Codex  <small>2026-09-06 03:10</small>

[external_agent_tool_result]
 1   84.3 $ 7.78 [Higiene       ] Limpiador de cera de oídos inalámbrico con cámara, endoscopio 
 2   82.0 $17.16 [Sueno         ] Auriculares para dormir con Bluetooth, máscara de ojos 3D, rep
 3   81.2 $18.27 [Dolor         ] Fisioterapia Tens Estimulador muscular Acupuntura eléctrica ma
 4   81.0 $  7.4 [Higiene       ] Limpiador de oídos Visual inteligente, palillos para los oídos
 5   80.6 $19.87 [Piel          ] Kit de herramientas de eliminación automática de marcas en la 
 6   80.0 $15.98 [Sueno         ] Dispositivo de hipnosis de pulso de microcorriente, tratamient
 7   79.7 $10.21 [Dolor         ] Instrumento masajeador de pulso Tens eléctrico de doble salida
 8   79.1 $13.67 [Salud femenina] Cinturón de palacio de masaje calentado portátil, dispositivo 
 9   78.8 $12.16 [Higiene       ] Limpiador de oídos visual inalámbrico con cámara, kit de otosc
10   77.4 $23.35 [Higiene       ] Generación-2, limpiador de cera de oídos Visual, cámara segura
11   77.1 $18.28 [Piel          ] Lápiz de Terapia de Luz Azul Nano de 830nm, Dispositivo Portát
12   76.6 $15.29 [Piel          ] Kit de eliminación automática de etiquetas de piel para etique
13   75.6 $13.73 [Sueno         ] Nuevo 1 Juego de dispositivo de hipnosis de pulso de microcorr
14   74.5 $  9.2 [Sueno         ] Ayuda para dormir, alivio del insomnio, microcorriente, hipnos
15   74.5 $11.69 [Piel          ] Kit de eliminación de marcas en la piel para etiquetas de piel
16   74.5 $ 6.17 [Dolor         ] Masajeador de cuello EMS, parche de masaje eléctrico para vért
17   74.3 $20.27 [Salud femenina] Calentador de manos con cinturón calefactor eléctrico, calenta
18   74.2 $12.19 [Piel          ] Nuevo Producto 2026: Lápiz Portátil de Terapia de Luz Azul |  
19   74.1 $ 6.99 [Piel          ] Kit de eliminación automática de etiquetas de piel de gran tam
20   73.5 $ 6.19 [Piel          ] Pluma láser para eliminación de arrugas y acné, eliminación de
21   73.2 $19.07 [Salud bebe    ] Aspirador Nasal Eléctrico para Bebés 2026, Nuevo Modelo, Versi
22   71.9 $ 8.75 [Piel          ] Lápiz Láser de Luz Azul para Cuidado Corporal, Apto para Uso D
23   71.6 $ 9.61 [Dolor         ] Máquina Tens, masajeador de pulso, acupuntura Tens, instrument
24   71.6 $18.98 [Salud femenina] Cinturón Eléctrico Calefactor, Calentador de Manos, Calentador
25   71.4 $15.41 [Dolor         ] Masajeador de Fascia muscular portátil de 6 velocidades, máqui
26   70.6 $19.64 [Salud bebe    ] Aspirador Nasal Eléctrico para Bebés, Aspirador de Nariz Autom
27   70.5 $21.97 [Salud bebe    ] Aspirador Nasal eléctrico para bebé, nuevo patrón, versión de 
28   70.3 $ 7.46 [Cuidado intimo] Cortadora de pelo eléctrica portátil 2 en 1 para hombres, cort
29   70.0 $ 9.65 [Salud femenina] Almohadillas térmicas menstruales para mujer, cinturón de aliv
30   69.1 $16.17 [Dolor         ] Masajeador de Cuello Recargable F2, Dispositivo Portátil de Ma
31   67.7 $11.38 [Dolor         ] Masajeador Eléctrico Inteligente TENS para Espalda y Cuello, 4
32   67.7 $ 17.6 [Salud bebe    ] Aspirador Nasal eléctrico para bebé, nuevo patrón, versión de 
33   67.4 $19.99 [Salud femenina] Cinturón calefactor de Sauna eléctrico para adelgazar, pérdida
34   66.9 $ 6.07 [Salud bebe    ] JUSTLANG Termómetro digital para frente LED Termómetro médico 
35   66.3 $14.96 [Dolor         ] Masajeador de vibración con soporte para cuello con calefacció
36   65.9 $22.91 [Dolor         ] Corrector de postura ajustable para la parte superior de la es
37   65.8 $15.66 [Cuidado intimo] Maquinilla eléctrica para cortar el pelo de la ingle para homb
38   65.4 $ 8.11 [Dolor         ] Soporte de Muñeca para Túnel Carpiano con Férulas, Soporte de 
39   65.3 $16.25 [Depilacion    ] Nueva Depiladora 2026, Depiladora Facial, Afeitadora Tipo Lápi
40   65.2 $ 8.28 [Sueno         ] 30 Tiras Nasales para Ronquidos, Tiras Nasales para Respirar, 
41   65.2 $16.89 [Afeitado      ] Mini Afeitadora eléctrica inteligente para el hogar y el coche
42   65.1 $ 8.32 [Su...
[/external_agent_tool_result]

### 🤖 Codex  <small>2026-09-06 03:10</small>

Much cleaner — the dental gun, cables and prophy brushes are gone. Two remaining issues: weight-loss claims (#33) and hand-warmers miscategorized as menstrual (#17, #24). Let me tighten those.

### 🤖 Codex  <small>2026-09-06 03:10</small>

[external_agent_tool_call: Bash]
description: Inspect borderline product titles
command: cd ~/Claude/investigacion-productos && python3 -c "
import json
d=json.load(open('productos_top50.json'))
for i in (16,23,32):
    p=d['productos'][i]; print(i+1, '|', p['categoria'], '|', p['titulo'])
"
[/external_agent_tool_call]

### 🤖 Codex  <small>2026-09-06 03:10</small>

[external_agent_tool_result]
17 | menstrual pain relief device heating | Calentador de manos con cinturón calefactor eléctrico, calentador de invierno, calentadores de cintura, compresa calient
24 | menstrual pain relief device heating | Cinturón Eléctrico Calefactor, Calentador de Manos, Calentador de Cintura para Invierno, Compresa Caliente Abdominal, Lu
33 | menstrual pain relief device heating | Cinturón calefactor de Sauna eléctrico para adelgazar, pérdida de peso, belleza, infrarrojo lejano, herramienta para ali
[/external_agent_tool_result]

### 🤖 Codex  <small>2026-09-06 03:10</small>

[external_agent_tool_call: Bash]
description: Apply final filter refinements
command: cd ~/Claude/investigacion-productos && python3 - <<'PY'
p='seleccion.py'; s=open(p,encoding='utf-8').read()
# 1. menstrual: exigir termino realmente menstrual (quitar "cintura" que colaba calentadores de invierno)
men_old = r'r"menstrual|per[ií]odo|regla|c[oó]lico|calambre|[uú]tero|palacio|vientre|cintura"'
men_new = r'r"menstrual|per[ií]odo|regla|c[oó]lico|calambre|[uú]tero|palacio|vientre|abdominal"'
assert s.count(men_old)==2, s.count(men_old)
s = s.replace(men_old, men_new)
# 2. bloquear calentadores de invierno genericos
s = s.replace('r"cargador", r"adaptador",', 'r"calentador de manos", r"de invierno", r"cargador", r"adaptador",',1)
# 3. claims de adelgazamiento -> riesgo regulatorio (Meta restringe)
s = s.replace(r'r"insuficiencia venosa|c[aá]ncer|tumor|verruga|lunar|papiloma|plasma|"',
              r'r"insuficiencia venosa|c[aá]ncer|tumor|verruga|lunar|papiloma|plasma|"' "\n"
              r'    r"adelgaz|p[eé]rdida de peso|quema(r)? grasa|slimming|reduce medidas|"',1)
open(p,'w',encoding='utf-8').write(s)
PY
python3 seleccion.py && python3 -c "
import json
d=json.load(open('productos_top50.json'))
print()
for i,p in enumerate(d['productos'],1):
    if i>34: break
    print(f\"{i:>2} {p['score']:>5} \${p['coste']:>5} [{p['nicho'][:14]:<14}] {p['titulo'][:58]}\")
"
[/external_agent_tool_call]

### 🤖 Codex  <small>2026-09-06 03:10</small>

[external_agent_tool_result]
crudo 3294 | califican 451 | entregados 50
descartes: {'precio fuera de 5-30': 1149, 'sin ventas suficientes': 1043, 'rating bajo': 104, 'listado no coincide / commodity': 142, 'no llega a 3x': 110, 'fuera de nicho': 295}
categorias en el top50: 19
nichos: {'Higiene': 4, 'Sueno': 6, 'Piel': 10, 'Dolor': 15, 'Salud femenina': 2, 'Salud bebe': 6, 'Cuidado intimo': 3, 'Depilacion': 1, 'Afeitado': 3}

 1  84.3 $ 7.78 [Higiene       ] Limpiador de cera de oídos inalámbrico con cámara, endosco
 2  82.0 $17.16 [Sueno         ] Auriculares para dormir con Bluetooth, máscara de ojos 3D,
 3  81.0 $  7.4 [Higiene       ] Limpiador de oídos Visual inteligente, palillos para los o
 4  80.6 $19.87 [Piel          ] Kit de herramientas de eliminación automática de marcas en
 5  80.0 $15.98 [Sueno         ] Dispositivo de hipnosis de pulso de microcorriente, tratam
 6  79.7 $10.21 [Dolor         ] Instrumento masajeador de pulso Tens eléctrico de doble sa
 7  79.1 $13.67 [Salud femenina] Cinturón de palacio de masaje calentado portátil, disposit
 8  78.8 $12.16 [Higiene       ] Limpiador de oídos visual inalámbrico con cámara, kit de o
 9  77.4 $23.35 [Higiene       ] Generación-2, limpiador de cera de oídos Visual, cámara se
10  77.1 $18.28 [Piel          ] Lápiz de Terapia de Luz Azul Nano de 830nm, Dispositivo Po
11  76.6 $15.29 [Piel          ] Kit de eliminación automática de etiquetas de piel para et
12  75.6 $13.73 [Sueno         ] Nuevo 1 Juego de dispositivo de hipnosis de pulso de micro
13  74.5 $  9.2 [Sueno         ] Ayuda para dormir, alivio del insomnio, microcorriente, hi
14  74.5 $11.69 [Piel          ] Kit de eliminación de marcas en la piel para etiquetas de 
15  74.5 $ 6.17 [Dolor         ] Masajeador de cuello EMS, parche de masaje eléctrico para 
16  74.2 $12.19 [Piel          ] Nuevo Producto 2026: Lápiz Portátil de Terapia de Luz Azul
17  74.1 $ 6.99 [Piel          ] Kit de eliminación automática de etiquetas de piel de gran
18  73.5 $ 6.19 [Piel          ] Pluma láser para eliminación de arrugas y acné, eliminació
19  73.2 $19.07 [Salud bebe    ] Aspirador Nasal Eléctrico para Bebés 2026, Nuevo Modelo, V
20  71.9 $ 8.75 [Piel          ] Lápiz Láser de Luz Azul para Cuidado Corporal, Apto para U
21  71.6 $ 9.61 [Dolor         ] Máquina Tens, masajeador de pulso, acupuntura Tens, instru
22  71.4 $15.41 [Dolor         ] Masajeador de Fascia muscular portátil de 6 velocidades, m
23  70.6 $19.64 [Salud bebe    ] Aspirador Nasal Eléctrico para Bebés, Aspirador de Nariz A
24  70.5 $21.97 [Salud bebe    ] Aspirador Nasal eléctrico para bebé, nuevo patrón, versión
25  70.3 $ 7.46 [Cuidado intimo] Cortadora de pelo eléctrica portátil 2 en 1 para hombres, 
26  70.0 $ 9.65 [Salud femenina] Almohadillas térmicas menstruales para mujer, cinturón de 
27  69.1 $16.17 [Dolor         ] Masajeador de Cuello Recargable F2, Dispositivo Portátil d
28  67.7 $11.38 [Dolor         ] Masajeador Eléctrico Inteligente TENS para Espalda y Cuell
29  67.7 $ 17.6 [Salud bebe    ] Aspirador Nasal eléctrico para bebé, nuevo patrón, versión
30  67.2 $18.27 [Dolor         ] Fisioterapia Tens Estimulador muscular Acupuntura eléctric
31  66.9 $ 6.07 [Salud bebe    ] JUSTLANG Termómetro digital para frente LED Termómetro méd
32  66.3 $14.96 [Dolor         ] Masajeador de vibración con soporte para cuello con calefa
33  65.9 $22.91 [Dolor         ] Corrector de postura ajustable para la parte superior de l
34  65.8 $15.66 [Cuidado intimo] Maquinilla eléctrica para cortar el pelo de la ingle para
[/external_agent_tool_result]

### 🤖 Codex  <small>2026-09-06 03:10</small>

The list is clean and coherent now. Let me build the interactive dashboard.

### 🤖 Codex  <small>2026-09-06 03:10</small>

[external_agent_tool_call: Write]
file: /home/matiigonzz/Claude/investigacion-productos/dashboard.py
[/external_agent_tool_call]

### 🤖 Codex  <small>2026-09-06 03:10</small>

[external_agent_tool_result]
File created successfully at: /home/matiigonzz/Claude/investigacion-productos/dashboard.py (file state is current in your context — no need to Read it back)
[/external_agent_tool_result]

### 🤖 Codex  <small>2026-09-06 03:10</small>

[external_agent_tool_call: Bash]
description: Generate interactive dashboard
command: cd ~/Claude/investigacion-productos && python3 dashboard.py
[/external_agent_tool_call]

### 🤖 Codex  <small>2026-09-06 03:10</small>

[external_agent_tool_result]
dashboard.html escrito: 51613 bytes, 50 productos
[/external_agent_tool_result]

### 🤖 Codex  <small>2026-09-06 03:10</small>

Let me verify the dashboard actually renders and the interactions work.

### 🤖 Codex  <small>2026-09-06 03:10</small>

[external_agent_tool_call: Bash]
description: Serve dashboard locally for testing
command: cd ~/Claude/investigacion-productos && python3 -m http.server 8899 >/dev/null 2>&1 &
sleep 1; curl -s -o /dev/null -w "%{http_code}\n" http://localhost:8899/dashboard.html
[/external_agent_tool_call]

### 🤖 Codex  <small>2026-09-06 03:10</small>

[external_agent_tool_result]
200
[/external_agent_tool_result]

### 🤖 Codex  <small>2026-09-06 03:10</small>

[external_agent_tool_call: mcp__Claude_Browser__navigate]
input: {"url":"http://localhost:8899/dashboard.html"}
[/external_agent_tool_call]

### 🤖 Codex  <small>2026-09-06 03:10</small>

[external_agent_tool_result: error]
<tool_use_error>Error: No such tool available: mcp__Claude_Browser__navigate</tool_use_error>
[/external_agent_tool_result]

### 🤖 Codex  <small>2026-09-06 03:10</small>

[external_agent_tool_call: Bash]
description: Validate embedded data and required fields
command: cd ~/Claude/investigacion-productos && which node >/dev/null 2>&1 && node -e "
const fs=require('fs');
const h=fs.readFileSync('dashboard.html','utf8');
// extraer el bloque script principal
const m=h.match(/const P = (\[.*?\]), M = (\{.*?\});/s);
if(!m){console.log('NO match datos');process.exit(1)}
const P=JSON.parse(m[1]), M=JSON.parse(m[2]);
console.log('productos parseados:',P.length);
console.log('meta ok:',M.total_crudo,'crudo,',M.total_filtrado,'filtrados');
// validar campos que usa el JS
const req=['titulo','nicho','categoria','coste','pvp_sugerido','margen_usd','margen_pct','multiplo','vendidos','rating','competencia','competidores','envio','choice','score','url','imagen','retail_fisico','riesgo_regulatorio','dias_publicado'];
let bad=0;
P.forEach((p,i)=>req.forEach(k=>{if(!(k in p)){console.log('FALTA',k,'en',i);bad++}}));
console.log('campos faltantes:',bad);
console.log('imagenes https:',P.filter(p=>p.imagen.startsWith('https')).length);
console.log('nichos:',[...new Set(P.map(p=>p.nicho))].join(', '));
console.log('rango coste: \$'+Math.min(...P.map(p=>p.coste))+' - \$'+Math.max(...P.map(p=>p.coste)));
console.log('todos 5-30:',P.every(p=>p.coste>=5&&p.coste<=30));
console.log('todos >=3x:',P.every(p=>p.multiplo>=3));
console.log('todos con ventas>=50:',P.every(p=>p.vendidos>=50));
" || echo "node no disponible"
[/external_agent_tool_call]

### 🤖 Codex  <small>2026-09-06 03:10</small>

[external_agent_tool_result]
productos parseados: 50
meta ok: 3294 crudo, 451 filtrados
campos faltantes: 0
imagenes https: 50
nichos: Higiene, Sueno, Piel, Dolor, Salud femenina, Salud bebe, Cuidado intimo, Depilacion, Afeitado
rango coste: $5.44 - $23.35
todos 5-30: true
todos >=3x: true
todos con ventas>=50: true
[/external_agent_tool_result]

### 🤖 Codex  <small>2026-09-06 03:10</small>

Data validates. Let me check the JavaScript for syntax errors and test the filter/sort logic.

### 🤖 Codex  <small>2026-09-06 03:10</small>

[external_agent_tool_call: Bash]
description: Test JS syntax and filter logic
command: cd ~/Claude/investigacion-productos && node -e "
const fs=require('fs');
const h=fs.readFileSync('dashboard.html','utf8');
const js=h.split('<script>')[1].split('</'+'script>')[0];
try{ new Function(js); console.log('sintaxis JS: OK'); }
catch(e){ console.log('ERROR sintaxis:',e.message); process.exit(1); }
// probar la logica de sort/filtro aislada
const m=h.match(/const P = (\[.*?\]), M = (\{.*?\});/s);
const P=JSON.parse(m[1]);
function test(fp){const[a,b]=fp.split('-').map(Number);return P.filter(p=>p.coste>=a&&p.coste<b).length;}
console.log('filtro \$5-10:',test('0-10'),'| \$10-20:',test('10-20'),'| \$20-30:',test('20-99'));
console.log('suma =',test('0-10')+test('10-20')+test('20-99'),'(debe ser 50)');
console.log('competencia Baja:',P.filter(p=>p.competencia==='Baja').length,
            'Media:',P.filter(p=>p.competencia==='Media').length,
            'Alta:',P.filter(p=>p.competencia==='Alta').length);
console.log('Choice (envio rapido):',P.filter(p=>p.choice).length);
console.log('con riesgo regulatorio:',P.filter(p=>p.riesgo_regulatorio).length);
const o={Baja:0,Media:1,Alta:2};
console.log('sort competencia ok:',[...P].sort((a,b)=>o[a.competencia]-o[b.competencia])[0].competencia);
console.log('sort score desc ok:',[...P].sort((a,b)=>b.score-a.score)[0].score);
"
[/external_agent_tool_call]

### 🤖 Codex  <small>2026-09-06 03:10</small>

[external_agent_tool_result]
sintaxis JS: OK
filtro $5-10: 18 | $10-20: 28 | $20-30: 4
suma = 50 (debe ser 50)
competencia Baja: 43 Media: 7 Alta: 0
Choice (envio rapido): 44
con riesgo regulatorio: 1
sort competencia ok: Baja
sort score desc ok: 84.3
[/external_agent_tool_result]

### 🤖 Codex  <small>2026-09-06 03:10</small>

All logic tests pass. Let me clean up and update the project README.

### 🤖 Codex  <small>2026-09-06 03:10</small>

[external_agent_tool_call: Bash]
description: Generate final summary stats
command: pkill -f "http.server 8899" 2>/dev/null; cd ~/Claude/investigacion-productos && python3 -c "
import json,collections
d=json.load(open('productos_top50.json'))
P=d['productos']
print('=== RESUMEN FINAL ===')
print('crudo explorado:',d['total_crudo'])
print('califican:',d['total_filtrado'])
print('entregados:',len(P))
print()
print('coste medio: \$%.2f'%(sum(p['coste'] for p in P)/50))
print('margen medio: %.0f%%'%(sum(p['margen_pct'] for p in P)/50))
print('multiplo medio: %.1fx'%(sum(p['multiplo'] for p in P)/50))
print('vendidos mediana:',sorted(p['vendidos'] for p in P)[25])
print()
print('nichos:',dict(collections.Counter(p['nicho'] for p in P)))
"
[/external_agent_tool_call]

### 🤖 Codex  <small>2026-09-06 03:10</small>

[external_agent_tool_result: error]
Exit code 144
[/external_agent_tool_result]

### 🤖 Codex  <small>2026-09-06 03:10</small>

[external_agent_tool_call: Bash]
description: Print final summary statistics
command: cd ~/Claude/investigacion-productos && python3 -c "
import json,collections
d=json.load(open('productos_top50.json'))
P=d['productos']
print('crudo explorado:',d['total_crudo'],'| califican:',d['total_filtrado'],'| entregados:',len(P))
print('coste medio: \$%.2f'%(sum(p['coste'] for p in P)/50))
print('margen medio: %.0f%%'%(sum(p['margen_pct'] for p in P)/50))
print('multiplo medio: %.1fx'%(sum(p['multiplo'] for p in P)/50))
print('vendidos mediana:',sorted(p['vendidos'] for p in P)[25])
print('nichos:',dict(collections.Counter(p['nicho'] for p in P)))
"
[/external_agent_tool_call]

### 🤖 Codex  <small>2026-09-06 03:10</small>

[external_agent_tool_result]
crudo explorado: 3294 | califican: 451 | entregados: 50
coste medio: $13.28
margen medio: 73%
multiplo medio: 3.7x
vendidos mediana: 1000
nichos: {'Higiene': 4, 'Sueno': 6, 'Piel': 10, 'Dolor': 15, 'Salud femenina': 2, 'Salud bebe': 6, 'Cuidado intimo': 3, 'Depilacion': 1, 'Afeitado': 3}
[/external_agent_tool_result]

### 🤖 Codex  <small>2026-09-06 03:10</small>

[external_agent_tool_call: Write]
file: /home/matiigonzz/Claude/investigacion-productos/LEEME.md
[/external_agent_tool_call]

### 🤖 Codex  <small>2026-09-06 03:10</small>

[external_agent_tool_result]
The file /home/matiigonzz/Claude/investigacion-productos/LEEME.md has been updated successfully. (file state is current in your context — no need to Read it back)
[/external_agent_tool_result]

### 🤖 Codex  <small>2026-09-06 03:10</small>

[external_agent_tool_call: Bash]
description: Open dashboard in browser
command: cd ~/Claude/investigacion-productos && xdg-open dashboard.html >/dev/null 2>&1 & sleep 2; ls -la dashboard.html productos_top50.json seleccion.py dashboard.py
[/external_agent_tool_call]

### 🤖 Codex  <small>2026-09-06 03:10</small>

[external_agent_tool_result]
-rw-r--r--. 1 matiigonzz matiigonzz 51856 sep  4 23:36 dashboard.html
-rw-r--r--. 1 matiigonzz matiigonzz 16994 sep  4 23:36 dashboard.py
-rw-r--r--. 1 matiigonzz matiigonzz 39358 sep  4 23:35 productos_top50.json
-rw-r--r--. 1 matiigonzz matiigonzz 17478 sep  4 23:34 seleccion.py
[/external_agent_tool_result]

### 🤖 Codex  <small>2026-09-06 03:10</small>

Listo. Abrí el dashboard: **[dashboard.html](dashboard.html)**

## Primero, lo que tenés que saber

**No pude usar el conector de AutoDS.** Está registrado en tu cuenta pero figura como "necesita autenticación", y los conectores se cargan sólo al arrancar la sesión — así que aunque lo reconectes ahora, esta sesión no lo va a ver.

Fui al catálogo que está **debajo** de AutoDS: AliExpress, que es lo que AutoDS revende. Los costes son reales. Lo que perdés respecto a AutoDS son dos cosas: el tiempo de envío real por proveedor y las ventas medidas por AutoDS.

## Dos bugs que encontré y arreglé

**La moneda.** Había trabajo previo en esta carpeta que entregaba 7 productos de 3.294. El motivo: AliExpress cambió la moneda de la sesión a pesos argentinos después de los primeros 60 productos, y el script viejo leía esos precios como dólares. Un producto de 9.000 ARS lo descartaba como "9.000 dólares, muy caro". Deduje el tipo de cambio de 6 productos que quedaron capturados en ambas monedas: 1.497,4 ARS/USD, con las 6 mediciones coincidiendo entre 1.495 y 1.498.

**Listados que no eran lo que se buscó.** Buscando "massage gun" apareció una pistola dosificadora dental; buscando "back shaver", 100 cepillos de profilaxis dental; buscando "manscaping kit", cable de silicona. Estaban rankeando alto. Agregué validación por título, que descartó 142 listados.

## El resultado

3.294 productos únicos explorados → 451 cumplen los cinco criterios → top 50, con tope de 4 por categoría para que no fueran 50 afeitadoras.

- Coste medio **$13,28**, todos entre $5,44 y $23,35
- Múltiplo medio **3,7x** (ninguno baja de 3x, era tu criterio)
- Mediana de **1.000 unidades vendidas**
- 43 de 50 con competencia baja, 44 con envío Choice
- 9 nichos: dolor (15), piel (10), sueño (6), salud bebé (6), higiene (4)

Arriba de todo quedan los limpiadores de oído con cámara (~$7,78, se venden a 4x, difíciles de conseguir en tienda física) y los dispositivos TENS.

## Lo que no te puedo garantizar

El dashboard separa en el pie qué columna es dato y cuál es supuesto mío. Resumido: **coste, vendidos y rating son datos reales**. **PVP, margen, competencia y nota son estimaciones mías** — el PVP dice a cuánto *se podría* vender según el tipo de producto, no a cuánto se vende hoy en Argentina. Validá contra competencia local antes de comprar volumen.

Y el coste es sólo el producto: faltan envío al cliente, pasarela, impuestos y publicidad. En dropshipping la publicidad se come buena parte del margen bruto, así que ese 73% promedio no es 73% en tu bolsillo.

También marqué los productos con claims médicos regulados (verrugas, lunares, adelgazamiento, hemoglobina) y les bajé la nota: Meta rechaza esos anuncios, y con tu cuenta de Meta Ads eso te importa.

**Si querés los datos reales de envío y ventas de AutoDS**, exportá el CSV desde su panel y decime dónde quedó — el pipeline lo absorbe y regenera el dashboard.

### 🧑 Vos  <small>2026-09-06 03:10</small>

QUIERO Q VOS ELIGAS EL MEJOR PRODUCTO, YO CONFIO EN TI, QUE ME GARANTIZE VENTAS Bueno, además que me garantice ventas que sea muy promocionable, que esté viral últimamente, que es un producto que, mire, al futuro va a ser yendo, que toda la gente en TikTok, Instagram y redes sociales siempre hablen de él, pero que no haya muchos competidores, y nada de eso.

### 🤖 Codex  <small>2026-09-06 03:10</small>

Antes de elegir, dejame hacer un análisis que no hice todavía: **velocidad de venta** (unidades por día desde que se publicó el listado). Eso es lo más cerca que puedo estar de "está explotando ahora" con datos reales.

### 🤖 Codex  <small>2026-09-06 03:10</small>

[external_agent_tool_call: Bash]
description: Analyze sales velocity as momentum proxy
command: cd ~/Claude/investigacion-productos && python3 - <<'PY'
import json, re, ast, datetime, collections, math
RATE=1497.4; HOY=datetime.date(2026,9,4)
import importlib.util
spec=importlib.util.spec_from_file_location("sel","seleccion.py")
sel=importlib.util.module_from_spec(spec); spec.loader.exec_module(sel)

rows=sel.cargar()
dens=collections.Counter(r["query"] for r in rows)
cand=[]
for r in rows:
    q=r["query"]; nicho=sel.NICHO.get(q)
    if not nicho: continue
    p=r.get("price") or 0
    if not (5<=p<=30): continue
    s=sel.parse_sold(r.get("sold_raw"))
    if s<50: continue
    rat=r.get("rating") or 0
    if rat and rat<4.3: continue
    if sel.MULT.get(q,2.8)<3.0: continue
    if sel.RETAIL.get(q,0.5)>=0.8: continue
    if not sel.titulo_valido(q,r["title"]): continue
    if not r.get("launch"): continue
    d=(HOY-datetime.datetime.strptime(r["launch"][:10],"%Y-%m-%d").date()).days
    if d<14: continue
    cand.append({"q":q,"nicho":nicho,"t":r["title"],"p":p,"s":s,"rat":rat,
                 "dias":d,"vel":s/d,"url":r["url"]})

print(f"candidatos con fecha: {len(cand)}\n")
print("=== TOP 15 POR VELOCIDAD (unidades/dia) ===")
for c in sorted(cand,key=lambda x:-x["vel"])[:15]:
    print(f"{c['vel']:>6.1f}/d  {c['s']:>6} en {c['dias']:>4}d  ${c['p']:>6.2f} {c['rat'] or '-':>4}★  [{c['nicho'][:13]:<13}] {c['t'][:52]}")

print("\n=== VELOCIDAD MEDIANA POR CATEGORIA (min 4 productos) ===")
g=collections.defaultdict(list)
for c in cand: g[c["q"]].append(c)
rank=[]
for q,v in g.items():
    if len(v)<4: continue
    vs=sorted(x["vel"] for x in v)
    med=vs[len(vs)//2]
    edad=sorted(x["dias"] for x in v)[len(v)//2]
    rank.append((med,q,len(v),edad,sel.MULT.get(q,2.8),sel.RETAIL.get(q,.5),dens[q]))
for med,q,n,edad,mult,ret,dn in sorted(rank,reverse=True):
    print(f"{med:>6.2f}/d  n={n:>3}  edad_med={edad:>4}d  {mult}x  retail={ret:<4} listados={dn:>3}  {q}")
PY
[/external_agent_tool_call]

### 🤖 Codex  <small>2026-09-06 03:10</small>

[external_agent_tool_result]
candidatos con fecha: 444

=== TOP 15 POR VELOCIDAD (unidades/dia) ===
 147.1/d  100000 en  680d  $  7.46  4.7★  [Cuidado intim] Cortadora de pelo eléctrica portátil 2 en 1 para hom
 113.4/d   50000 en  441d  $  7.42  4.6★  [Afeitado     ] Recortador de pelo de nariz eléctrico recargable, re
 108.9/d  100000 en  918d  $  7.44  4.4★  [Afeitado     ] Cortadora de pelo T9, reparación de barba, afeitador
  84.7/d    5000 en   59d  $  6.29  4.5★  [Afeitado     ] 3/6/12 Piezas/Cuchillas de Afeitar de Alta Calidad p
  35.7/d   10000 en  280d  $ 18.14  4.6★  [Afeitado     ] Afeitadora de lámina compacta ENCHEN MS003 con recor
  27.8/d   10000 en  360d  $  8.34  4.8★  [Afeitado     ] Recortador de pelo de nariz recortador portátil para
  25.9/d   10000 en  386d  $  7.78  4.7★  [Higiene      ] Limpiador de cera de oídos inalámbrico con cámara, e
  25.7/d   10000 en  389d  $  7.60  4.6★  [Afeitado     ] Recortador de pelo de nariz y orejas para hombres: c
  25.0/d    1000 en   40d  $ 12.38    -★  [Depilacion   ] Afeitadora Eléctrica T9 para Hombre, Máquina de Afei
  22.2/d    2000 en   90d  $  9.32  4.4★  [Afeitado     ] Nueva Afeitadora Eléctrica Digital Inteligente Multi
  15.5/d   10000 en  646d  $ 16.89  4.4★  [Afeitado     ] Mini Afeitadora eléctrica inteligente para el hogar 
  15.2/d    5000 en  330d  $  6.84  4.4★  [Depilacion   ] Recortador eléctrico de pelo de nariz, afeitadora pa
  13.7/d    5000 en  365d  $  6.45  4.5★  [Cuidado intim] Cortadora de pelo eléctrica para hombres, afeitadora
  13.7/d   10000 en  732d  $  5.28  4.6★  [Depilacion   ] Maquinilla de afeitar para peluquero para hombre, cu
  13.2/d    4000 en  303d  $ 18.46  4.7★  [Piel         ] Juego de 4 Uds. De cepillo exfoliante suave de silic

=== VELOCIDAD MEDIANA POR CATEGORIA (min 4 productos) ===
  3.38/d  n=  9  edad_med= 400d  3.2x  retail=0.2  listados= 49  electric razor bald head shaver
  2.96/d  n=  5  edad_med= 680d  3.2x  retail=0.2  listados= 49  manscaping groomer kit
  2.88/d  n=  6  edad_med= 308d  3.1x  retail=0.4  listados= 60  silicone face cleansing brush
  2.72/d  n= 16  edad_med= 436d  3.0x  retail=0.35 listados= 95  mini shaver portable travel pocket
  2.43/d  n=  4  edad_med= 823d  4.2x  retail=0.05 listados= 58  tens unit pain relief
  2.32/d  n= 19  edad_med= 366d  3.0x  retail=0.35 listados= 91  body groomer trimmer men waterproof
  2.26/d  n= 15  edad_med= 765d  3.0x  retail=0.5  listados= 60  shoulder posture strap
  1.77/d  n= 34  edad_med= 514d  3.1x  retail=0.2  listados= 94  pubic hair trimmer men
  1.41/d  n= 12  edad_med= 514d  3.0x  retail=0.3  listados=110  beard straightener brush heated
  1.30/d  n= 36  edad_med= 448d  3.2x  retail=0.15 listados=115  bikini trimmer women intimate
  1.10/d  n= 34  edad_med= 427d  3.1x  retail=0.3  listados=151  nose ear hair trimmer electric
  1.05/d  n=  9  edad_med= 473d  4.0x  retail=0.1  listados= 60  sleep aid device insomnia
  1.05/d  n= 15  edad_med= 263d  4.0x  retail=0.05 listados= 60  ear wax removal camera
  1.01/d  n= 12  edad_med= 698d  3.4x  retail=0.25 listados= 58  anti snoring device mouthpiece
  0.99/d  n= 15  edad_med= 379d  3.9x  retail=0.1  listados= 60  skin tag remover device
  0.91/d  n= 33  edad_med= 416d  3.0x  retail=0.5  listados=140  face shaver women facial hair
  0.77/d  n=  4  edad_med= 821d  3.8x  retail=0.15 listados= 52  posture trainer wearable
  0.73/d  n= 23  edad_med= 759d  3.4x  retail=0.4  listados= 60  baby thermometer forehead digital
  0.73/d  n= 13  edad_med= 483d  3.6x  retail=0.25 listados= 58  neck massager cervical pain relief
  0.70/d  n= 11  edad_med= 426d  3.4x  retail=0.25 listados= 60  carpal tunnel wrist relief
  0.69/d  n= 11  edad_med= 277d  4.2x  retail=0.05 listados= 59  acne blue light pen
  0.69/d  n= 26  edad_med= 511d  3.0x  retail=0.45 listados=121  hair removal razor women electric
  0.63/d  n= 21  edad_med= 505d  3.3x  retail=0.15 listados= 91  back shaver long handle men
  0.60/d  n= 10  edad_med= 910d  3.2x  retail=0.15 li...
[/external_agent_tool_result]

### 🤖 Codex  <small>2026-09-06 03:10</small>

Ahora tengo lo que me faltaba. Dejame ver en detalle los candidatos finales.

### 🤖 Codex  <small>2026-09-06 03:10</small>

[external_agent_tool_call: Bash]
description: Deep dive on final candidates
command: cd ~/Claude/investigacion-productos && python3 - <<'PY'
import json, datetime, importlib.util, collections
spec=importlib.util.spec_from_file_location("sel","seleccion.py")
sel=importlib.util.module_from_spec(spec); spec.loader.exec_module(sel)
HOY=datetime.date(2026,9,4)
rows=sel.cargar()
for q in ["ear wax removal camera","electric razor bald head shaver"]:
    print("="*100); print(q.upper())
    v=[]
    for r in rows:
        if r["query"]!=q: continue
        p=r.get("price") or 0; s=sel.parse_sold(r.get("sold_raw"))
        if not(5<=p<=30) or s<50: continue
        if not sel.titulo_valido(q,r["title"]): continue
        d=None
        if r.get("launch"):
            d=(HOY-datetime.datetime.strptime(r["launch"][:10],"%Y-%m-%d").date()).days
        ch,fs=sel.flags(r)
        v.append((s,p,r.get("rating"),d,ch,r["title"][:60],r["url"]))
    for s,p,rt,d,ch,t,u in sorted(v,key=lambda x:-x[0])[:8]:
        vel=f"{s/d:.1f}/d" if d else "-"
        print(f"  {s:>6}u ${p:>6.2f} {str(rt):>4}★ {str(d):>5}d {vel:>8} {'Choice' if ch else '     '} {t}")
    ps=[x[1] for x in v]
    print(f"  -> {len(v)} listados validos | precio min ${min(ps):.2f} max ${max(ps):.2f} | total unidades {sum(x[0] for x in v):,}")
PY
[/external_agent_tool_call]

### 🤖 Codex  <small>2026-09-06 03:10</small>

[external_agent_tool_result]
====================================================================================================
EAR WAX REMOVAL CAMERA
   10000u $  7.78  4.7★   386d   25.9/d Choice Limpiador de cera de oídos inalámbrico con cámara, endoscopi
    4000u $  7.40  4.7★   470d    8.5/d Choice Limpiador de oídos Visual inteligente, palillos para los oíd
    1000u $ 23.35  4.7★   261d    3.8/d Choice Generación-2, limpiador de cera de oídos Visual, cámara segu
    1000u $ 11.63  4.6★   270d    3.7/d Choice Limpiador de Cera para Oídos con Cámara, Endoscopio Seguro p
     800u $ 26.70  4.9★   242d    3.3/d       Generación-2, limpiador de cera de oídos Visual, cámara segu
     800u $  7.84  4.3★   283d    2.8/d Choice 1 Juego de removedor de cera de oídos eléctrico, juego de he
     700u $ 12.16  4.7★   133d    5.3/d Choice Limpiador de oídos visual inalámbrico con cámara, kit de oto
     474u $  7.70  4.3★   689d    0.7/d       Tinsol-limpiador de oídos Visual inteligente, 1296P, otoscop
  -> 16 listados validos | precio min $7.40 max $26.70 | total unidades 19,867
====================================================================================================
ELECTRIC RAZOR BALD HEAD SHAVER
   10000u $  7.64  4.4★   918d   10.9/d Choice Afeitadora de pelo eléctrica inalámbrica T9, recortadora de 
   10000u $ 16.89  4.4★   646d   15.5/d Choice Mini Afeitadora eléctrica inteligente para el hogar y el coc
    2000u $ 18.72  4.7★  1151d    1.7/d Choice ENCHEN-Afeitadora rotativa eléctrica Blackstone para hombres
    2000u $  9.32  4.4★    90d   22.2/d Choice Nueva Afeitadora Eléctrica Digital Inteligente Multifunciona
     600u $ 21.21  4.8★   367d    1.6/d       ENCHEN Blackstone Max Afeitadora eléctrica Cabezales flexibl
     500u $ 26.47  4.6★   148d    3.4/d       Afeitadora eléctrica original Andis Profoil Lithium Plus 172
     325u $ 23.01  4.8★   400d    0.8/d       Nuevo Cortadora potente portátil de doble red, Afeitadora el
     310u $  8.81 None★    24d   12.9/d Choice Afeitadora eléctrica profesional para hombres, máquina de af
  -> 9 listados validos | precio min $7.64 max $26.47 | total unidades 25,918
[/external_agent_tool_result]

### 🤖 Codex  <small>2026-09-06 03:10</small>

[external_agent_tool_call: Bash]
description: Get full details of recommended product
command: cd ~/Claude/investigacion-productos && python3 -c "
import json
d=json.load(open('productos_top50.json'))
p=d['productos'][0]
for k in ['titulo','coste','pvp_sugerido','margen_usd','margen_pct','multiplo','vendidos','rating','competencia','competidores','envio','choice','dias_publicado','score','url']:
    print(f'{k:>16}: {p[k]}')
"
[/external_agent_tool_call]

### 🤖 Codex  <small>2026-09-06 03:10</small>

[external_agent_tool_result]
          titulo: Limpiador de cera de oídos inalámbrico con cámara, endoscopio seguro para eliminación de cera de oídos con cámara, otosc
           coste: 7.78
    pvp_sugerido: 31.12
      margen_usd: 23.34
      margen_pct: 75.0
        multiplo: 4.0
        vendidos: 10000
          rating: 4.7
     competencia: Baja
    competidores: 60
           envio: 15-25 dias
          choice: True
  dias_publicado: 386
           score: 84.3
             url: https://www.aliexpress.com/item/1005009734016590.html
[/external_agent_tool_result]

### 🤖 Codex  <small>2026-09-06 03:10</small>

Elegí. Pero antes, dos cosas que te tengo que decir de frente, porque si no la elección no te sirve.

**No existe un producto que garantice ventas.** Nadie te puede prometer eso — ni yo, ni un curso, ni un proveedor. Lo que sí puedo hacer es elegir el que tiene mejores probabilidades y, sobre todo, el que si sale mal te hace perder poco. Eso es lo que hice.

**Y "que todos hablen de él en TikTok" + "que no haya competidores" no pueden pasar juntos.** Si todo el mundo lo muestra, hay competencia; es la misma cosa vista de dos lados. Lo que sí se puede conseguir es un producto con *formato* viral probado que todavía no está saturado. Eso es lo que busqué.

Último aviso: **no tengo datos de TikTok ni Instagram.** Nada de lo que digo sobre viralidad sale de medir redes. Sale de la velocidad de venta real del catálogo y de las características del producto.

---

## Mi elección: limpiador de oídos con cámara (otoscopio)

**[Ver el producto](https://www.aliexpress.com/item/1005009734016590.html)** — $7,78 el costo

| | |
|---|---|
| Costo | **$7,78** |
| PVP sugerido | **~$31** (4x) |
| Margen bruto | $23,34 (75%) |
| Vendidos | 10.000 unidades · 4,7★ |
| Velocidad | **25,9 unidades/día** — la más alta de todo lo que no es maquinita de afeitar |
| Envío | 15-25 días (Choice) |
| Competencia | Baja |

### Por qué este y no otro

**El video es el producto.** Una cámara metida en un oído sacando cera es el género "oddly satisfying", uno de los formatos más duraderos que existe en TikTok. No necesitás ser creativo, ni salir en cámara, ni tener buena luz: la grabación se vende sola. Cuando me pedís "muy promocionable", esto es literalmente lo que significa en la práctica. Y cada limpieza es un video nuevo — el contenido es infinito y gratis.

**La gente ya paga caro por esto, y lo puedo probar.** En el mismo catálogo, este producto se vende desde $7,40 hasta $26,70. La versión "Generación-2" a $23,35 tiene 1.000 vendidas con 4,7★. O sea: no estoy inventando que se puede cobrar 4x — hay gente pagando 3x el precio base *dentro de AliExpress*, que es el lugar más barato del mundo. Ese es el dato que más me convenció.

**No lo conseguís en el Carrefour ni en una farmacia.** Es el producto con menor disponibilidad en tienda física de toda mi lista (0,05 sobre 1). No tenés un precio de góndola contra el cual competir, y eso es exactamente lo que te deja poner $31.

**Y esto es lo más importante para vos:** no hace ninguna afirmación médica. Es una herramienta de limpieza, no un tratamiento. Los otros productos que puntuaban alto — TENS, lápiz de luz azul, quita-verrugas — son claims regulados y **Meta te rechaza los anuncios o te suspende la cuenta**. Vos manejás Meta Ads. Elegir uno de esos era ponerte a jugar con la cuenta publicitaria de garantía.

### Lo que puede salir mal

**El wifi y la app.** Es la falla número uno de estos endoscopios baratos: la cámara se desconecta, la app es mala, anda en Android pero no en iPhone. Si eso pasa te llueven las devoluciones y las reseñas malas. **Es el riesgo real de este producto y no lo puedo verificar desde acá.**

**No es nuevo.** Bebird lo hizo popular alrededor de 2020-2021. Esto es "probado y todavía funcionando", no "nadie lo descubrió". Si buscabas algo que nadie vio nunca, no es este — y te diría que desconfíes de cualquiera que te ofrezca eso con ventas ya probadas, porque las dos cosas juntas no existen.

**Mis 60 listados no son la competencia mundial.** Es baja *comparada con las otras categorías que medí*, no baja en términos absolutos.

### Qué hacer ahora

Comprá **una sola unidad** ($7,78) y probala vos: la app en tu teléfono, la batería, si la imagen se ve bien. Con esa misma unidad filmás los primeros 5 o 10 videos. Recién si la app funciona bien, comprás volumen.

Esa es la única garantía que te puedo dar de verdad: que si me equivoqué, te enteraste por $8 y no por $800.

¿Querés que arme la ficha de producto y los ángulos de video para arrancar?
