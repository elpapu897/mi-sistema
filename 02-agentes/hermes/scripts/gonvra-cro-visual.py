#!/usr/bin/env python3
"""
GONVRA — CRO visual (idea sacada de multimodal_uiux_feedback_agent_team).

El CRO de siempre lee el HTML. Este MIRA la página como la ve un cliente:
saca capturas reales en celular y en compu, y las analiza con Gemini.

Encuentra cosas que el HTML no muestra: texto que no se lee, el botón de
comprar demasiado abajo, precio poco visible, imágenes que tapan lo importante.

Guarda el informe en ~/Claude/gonvra2/cro/AAAA-MM-DD-visual.md
No toca la tienda: solo propone.
"""
import asyncio
import base64
import json
import os
import sys
import urllib.error
import urllib.request
from datetime import date

SECRETS = os.path.expanduser("~/.hermes/.gonvra-secrets.env")
SALIDA = os.path.expanduser("~/Claude/gonvra2/cro")
URL = "https://gonvra.com/products/face-body-electric-shaver"
MODELO = "gemini-3-flash-preview"

VISTAS = [
    ("celular", {"width": 430, "height": 932}, True),
    ("compu", {"width": 1440, "height": 900}, False),
]


def clave():
    v = os.environ.get("GEMINI_API_KEY")
    if v:
        return v
    for archivo in (SECRETS, os.path.expanduser("~/.hermes/.env")):
        try:
            for l in open(archivo, encoding="utf-8"):
                for n in ("GEMINI_API_KEY=", "GOOGLE_API_KEY="):
                    if l.startswith(n):
                        val = l.split("=", 1)[1].strip()
                        if val:
                            return val
        except Exception:
            pass
    return None


async def capturar():
    from playwright.async_api import async_playwright
    salidas = []
    async with async_playwright() as p:
        b = await p.chromium.launch()
        for nombre, vp, movil in VISTAS:
            pg = await b.new_page(viewport=vp, is_mobile=movil)
            try:
                await pg.goto(URL, wait_until="domcontentloaded", timeout=90000)
                await pg.wait_for_timeout(6000)
                ruta = f"/tmp/gonvra-{nombre}.png"
                await pg.screenshot(path=ruta)
                salidas.append((nombre, ruta))
            except Exception as e:
                print(f"no se pudo capturar {nombre}: {str(e)[:60]}", file=sys.stderr)
            await pg.close()
        await b.close()
    return salidas


def analizar(capturas, k):
    partes = [{"text": PROMPT}]
    for nombre, ruta in capturas:
        partes.append({"text": f"\n--- VISTA: {nombre} ---"})
        with open(ruta, "rb") as f:
            partes.append({"inline_data": {
                "mime_type": "image/png",
                "data": base64.b64encode(f.read()).decode()}})

    body = {"contents": [{"parts": partes}],
            "generationConfig": {"temperature": 0.4, "maxOutputTokens": 3000}}
    req = urllib.request.Request(
        f"https://generativelanguage.googleapis.com/v1beta/models/"
        f"{MODELO}:generateContent?key={k}",
        data=json.dumps(body).encode(),
        headers={"Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=240) as r:
            d = json.loads(r.read().decode())
        return d["candidates"][0]["content"]["parts"][0]["text"]
    except urllib.error.HTTPError as e:
        return f"ERROR {e.code}: {e.read().decode()[:200]}"
    except Exception as e:
        return f"ERROR: {str(e)[:200]}"


PROMPT = """Sos experto en conversión de tiendas online (CRO) en Argentina.

Te paso capturas REALES de la ficha de producto de GONVRA, como las ve un cliente.
Producto: Rasuradora Integral Recargable — Rostro y Cuerpo. Precio: $36.900 ARS.
Envío gratis a todo el país. Garantía y arrepentimiento: 10 días.

Analizá SOLO lo que se ve en las imágenes. No inventes nada que no esté ahí.

Respondé en castellano rioplatense, con esta estructura:

## Lo primero que ve el cliente
Qué se entiende en los primeros 3 segundos sin scrollear. ¿Queda claro QUÉ es
y CUÁNTO sale?

## Los 3 problemas que más plata cuestan
Para cada uno:
- **Qué pasa:** lo que ves mal, concreto
- **Por qué cuesta ventas:** el motivo
- **Cómo se arregla:** el cambio exacto, con el texto si aplica
- **Prioridad:** alta / media / baja

## Lo que está bien
2 o 3 cosas que NO hay que tocar.

## Celular vs compu
Diferencias que importen entre las dos vistas.

REGLAS:
- Nada de "mejorar la imagen de marca". Todo tiene que poder medirse en ventas.
- No propongas escasez falsa, contadores truchos ni reseñas inventadas.
- No propongas descuentos: el margen es del 76% y hay que cuidarlo.
- Si algo no se ve en las capturas, decí "no se puede evaluar", no lo inventes.
- Sé concreto: "el botón está debajo del pliegue" sirve; "mejorar el diseño" no.
"""


def main():
    k = clave()
    if not k:
        print("GONVRA CRO: falta GEMINI_API_KEY")
        return 0

    try:
        capturas = asyncio.run(capturar())
    except Exception as e:
        print(f"GONVRA CRO: no se pudo abrir la página ({str(e)[:80]})")
        return 0

    if not capturas:
        print("GONVRA CRO: no se pudo capturar la ficha.")
        return 0

    texto = analizar(capturas, k)
    if texto.startswith("ERROR"):
        print(f"GONVRA CRO: {texto[:160]}")
        return 0

    hoy = date.today().isoformat()
    os.makedirs(SALIDA, exist_ok=True)
    ruta = os.path.join(SALIDA, f"{hoy}-visual.md")
    with open(ruta, "w", encoding="utf-8") as f:
        f.write(f"# CRO visual — {hoy}\n\n")
        f.write(f"Analizado sobre capturas reales de {URL}\n")
        f.write(f"Vistas: {', '.join(n for n, _ in capturas)}\n\n---\n\n")
        f.write(texto + "\n")

    print("CRO VISUAL — miré la ficha como la ve un cliente")
    print()
    # mandar solo el resumen a Telegram, el detalle queda en el archivo
    corte = texto.find("## Lo que está bien")
    print((texto[:corte] if corte > 0 else texto[:1200]).strip())
    print()
    print(f"Informe completo: cro/{hoy}-visual.md")
    return 0


if __name__ == "__main__":
    sys.exit(main())
