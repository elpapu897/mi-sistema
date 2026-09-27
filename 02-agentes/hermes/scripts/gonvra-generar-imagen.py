#!/usr/bin/env python3
"""
GONVRA — Genera imágenes con Replicate.

Uso:
    gonvra-generar-imagen.py "el prompt" salida.png [--ratio 4:5] [--modelo rapido|bueno]

  --ratio  : 4:5 (feed IG), 1:1, 9:16 (historia/reel), 16:9
  --modelo : rapido (flux-schnell, ~US$0.003)  ·  bueno (nano-banana, ~US$0.039)

Imprime la ruta del archivo generado.
"""
import argparse
import json
import os
import sys
import time
import urllib.error
import urllib.request

SECRETS = os.path.expanduser("~/.hermes/.gonvra-secrets.env")
API = "https://api.replicate.com/v1"

MODELOS = {
    "rapido": ("black-forest-labs/flux-schnell", 0.003),
    "bueno": ("google/nano-banana", 0.039),
}


def token():
    # El archivo de secretos MANDA: en el entorno puede haber una clave vieja.
    try:
        for l in open(SECRETS, encoding="utf-8"):
            if l.startswith("REPLICATE_API_TOKEN="):
                v = l.split("=", 1)[1].strip()
                if v:
                    return v
    except Exception:
        pass
    return os.environ.get("REPLICATE_API_TOKEN")


def pedir(metodo, ruta, cuerpo=None, tok=None):
    datos = json.dumps(cuerpo).encode() if cuerpo else None
    r = urllib.request.Request(
        API + ruta, data=datos, method=metodo,
        headers={"Authorization": f"Bearer {tok}",
                 "Content-Type": "application/json",
                 "User-Agent": "gonvra/1.0"})
    try:
        with urllib.request.urlopen(r, timeout=60) as resp:
            return json.loads(resp.read().decode())
    except urllib.error.HTTPError as e:
        return {"error": e.read().decode()[:300], "code": e.code}


def generar(prompt, salida, ratio, modelo):
    tok = token()
    if not tok:
        print("ERROR: falta REPLICATE_API_TOKEN", file=sys.stderr)
        return False

    nombre, costo = MODELOS.get(modelo, MODELOS["rapido"])
    entrada = {"prompt": prompt}
    if modelo == "rapido":
        entrada.update({"aspect_ratio": ratio, "output_format": "png",
                        "num_outputs": 1, "go_fast": True})
    else:
        entrada.update({"aspect_ratio": ratio, "output_format": "png"})

    d = pedir("POST", f"/models/{nombre}/predictions", {"input": entrada}, tok)
    if d.get("error"):
        print(f"ERROR al pedir: {str(d['error'])[:200]}", file=sys.stderr)
        return False

    pid = d.get("id")
    if not pid:
        print(f"ERROR: no vino id. {json.dumps(d)[:200]}", file=sys.stderr)
        return False

    # esperar a que termine
    for _ in range(90):
        e = pedir("GET", f"/predictions/{pid}", None, tok)
        estado = e.get("status")
        if estado == "succeeded":
            out = e.get("output")
            url = out[0] if isinstance(out, list) else out
            if not url:
                print("ERROR: terminó sin imagen", file=sys.stderr)
                return False
            with urllib.request.urlopen(url, timeout=120) as r:
                open(salida, "wb").write(r.read())
            print(f"(costó ~US${costo:.3f})", file=sys.stderr)
            return True
        if estado in ("failed", "canceled"):
            print(f"ERROR: {estado} · {str(e.get('error'))[:200]}", file=sys.stderr)
            return False
        time.sleep(2)

    print("ERROR: tardó demasiado", file=sys.stderr)
    return False


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("prompt")
    ap.add_argument("salida")
    ap.add_argument("--ratio", default="4:5")
    ap.add_argument("--modelo", default="rapido", choices=list(MODELOS))
    a = ap.parse_args()

    if generar(a.prompt, a.salida, a.ratio, a.modelo):
        print(a.salida)
        return 0
    return 1


if __name__ == "__main__":
    sys.exit(main())
