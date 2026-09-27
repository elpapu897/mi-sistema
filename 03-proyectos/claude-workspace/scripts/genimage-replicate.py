#!/usr/bin/env python3
"""
Generador de imagenes via Replicate (Imagen 4 / Nano Banana).

Alternativa a la API de Gemini directa, que exige billing en Google Cloud.
Requiere: export REPLICATE_API_TOKEN="r8_..."

Ejemplos:
    python genimage-replicate.py --prompt "un golden retriever feliz" --output hero.png
    python genimage-replicate.py --prompt "..." --model imagen-4-fast --aspect-ratio 16:9
    python genimage-replicate.py --prompt "sacale el fondo" --images foto.jpg --model nano-banana
"""

import argparse
import base64
import mimetypes
import os
import sys
import time
import json

import requests

API = "https://api.replicate.com/v1"

# Modelos disponibles y su costo aproximado por imagen (USD)
MODELS = {
    "imagen-4":         ("google/imagen-4",          0.04),
    "imagen-4-fast":    ("google/imagen-4-fast",     0.02),
    "imagen-4-ultra":   ("google/imagen-4-ultra",    0.06),
    "nano-banana":      ("google/nano-banana",       0.039),
    "nano-banana-pro":  ("google/nano-banana-pro",   0.139),
}

# Modelos que aceptan imagenes de entrada (edicion / composicion)
EDIT_CAPABLE = {"nano-banana", "nano-banana-pro"}

# Imagen 4 solo acepta estos ratios; nano-banana acepta todos
IMAGEN_RATIOS = {"1:1", "9:16", "16:9", "3:4", "4:3"}


def die(msg):
    print(f"ERROR: {msg}", file=sys.stderr)
    sys.exit(1)


def to_data_uri(path):
    if not os.path.isfile(path):
        die(f"no existe la imagen de entrada: {path}")
    mime = mimetypes.guess_type(path)[0] or "image/png"
    with open(path, "rb") as f:
        b64 = base64.b64encode(f.read()).decode()
    return f"data:{mime};base64,{b64}"


def build_input(args, model_key):
    inp = {"prompt": args.prompt}

    if model_key.startswith("imagen"):
        if args.aspect_ratio not in IMAGEN_RATIOS:
            die(f"{model_key} no soporta {args.aspect_ratio}. "
                f"Usa uno de {sorted(IMAGEN_RATIOS)}, o cambia a --model nano-banana "
                f"que si soporta {args.aspect_ratio}")
        inp["aspect_ratio"] = args.aspect_ratio
        inp["output_format"] = "png" if args.output.lower().endswith(".png") else "jpg"
        inp["safety_filter_level"] = "block_only_high"
    else:  # nano-banana
        inp["aspect_ratio"] = args.aspect_ratio
        inp["output_format"] = "png" if args.output.lower().endswith(".png") else "jpg"
        if args.images:
            inp["image_input"] = [to_data_uri(p) for p in args.images]
        if args.resolution and model_key == "nano-banana-pro":
            inp["resolution"] = args.resolution

    return inp


def run(args):
    token = os.environ.get("REPLICATE_API_TOKEN")
    if not token:
        die("falta REPLICATE_API_TOKEN.\n"
            "  1. Crea una cuenta en https://replicate.com\n"
            "  2. Saca el token en https://replicate.com/account/api-tokens\n"
            '  3. export REPLICATE_API_TOKEN="r8_..."')

    model_key = args.model
    if model_key not in MODELS:
        die(f"modelo desconocido: {model_key}. Opciones: {', '.join(MODELS)}")

    slug, cost = MODELS[model_key]

    if args.images and model_key not in EDIT_CAPABLE:
        die(f"{model_key} no acepta imagenes de entrada. Usa --model nano-banana o nano-banana-pro")

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "Prefer": "wait",  # espera hasta 60s la respuesta, evita hacer polling
    }
    payload = {"input": build_input(args, model_key)}

    print(f"Generando con {slug} (~${cost:.3f} USD)...")
    r = requests.post(f"{API}/models/{slug}/predictions",
                      headers=headers, json=payload, timeout=180)

    if r.status_code == 401:
        die("token invalido o vencido (401)")
    if r.status_code == 402:
        die("sin credito en Replicate (402). Carga saldo en https://replicate.com/account/billing")
    if r.status_code >= 400:
        die(f"HTTP {r.status_code}: {r.text[:400]}")

    pred = r.json()

    # Si todavia no termino, hacemos polling
    deadline = time.time() + 300
    while pred.get("status") in ("starting", "processing"):
        if time.time() > deadline:
            die("timeout esperando la prediccion")
        time.sleep(2)
        pred = requests.get(f"{API}/predictions/{pred['id']}",
                            headers=headers, timeout=60).json()
        print(f"  ...{pred.get('status')}")

    if pred.get("status") != "succeeded":
        die(f"la generacion fallo: {pred.get('error') or json.dumps(pred)[:400]}")

    out = pred.get("output")
    url = out[0] if isinstance(out, list) else out
    if not url:
        die("la respuesta no trajo ninguna imagen")

    img = requests.get(url, timeout=120)
    img.raise_for_status()

    os.makedirs(os.path.dirname(os.path.abspath(args.output)) or ".", exist_ok=True)
    with open(args.output, "wb") as f:
        f.write(img.content)

    kb = len(img.content) / 1024
    print(f"Listo -> {args.output} ({kb:.0f} KB)")


def main():
    p = argparse.ArgumentParser(description="Genera imagenes con Replicate")
    p.add_argument("--prompt", required=True, help="Descripcion de la imagen")
    p.add_argument("--output", default="generated_image.png", help="Archivo de salida")
    p.add_argument("--model", default="imagen-4",
                   help=f"Modelo: {', '.join(MODELS)}")
    p.add_argument("--aspect-ratio", default="1:1",
                   choices=["1:1", "9:16", "16:9", "3:4", "4:3", "2:3", "3:2", "4:5", "5:4", "21:9"])
    p.add_argument("--resolution", choices=["1K", "2K", "4K"],
                   help="Solo nano-banana-pro")
    p.add_argument("--images", nargs="*", help="Imagenes de entrada (solo nano-banana*)")
    run(p.parse_args())


if __name__ == "__main__":
    main()
