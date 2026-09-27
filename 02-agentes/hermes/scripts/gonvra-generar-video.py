#!/usr/bin/env python3
"""
GONVRA — Genera clips de video con Replicate.

⚠️ ESTO CUESTA PLATA DE VERDAD. Mucho más que las imágenes.
   Una imagen: ~US$0.003   ·   Un clip de 6s: ~US$0.25 a US$0.50

Por eso:
  · exige --confirmo para correr (no se dispara solo por accidente)
  · lleva un registro de lo gastado en ~/.hermes/gonvra-gasto-replicate.json
  · corta si se pasa del tope diario

Uso:
    gonvra-generar-video.py "prompt" salida.mp4 --confirmo [--modelo barato|bueno]
"""
import argparse
import json
import os
import sys
import time
import urllib.error
import urllib.request
from datetime import date

SECRETS = os.path.expanduser("~/.hermes/.gonvra-secrets.env")
GASTO = os.path.expanduser("~/.hermes/gonvra-gasto-replicate.json")
API = "https://api.replicate.com/v1"

TOPE_DIARIO = 3.00  # dólares

MODELOS = {
    # 768p sale bastante menos que 1080p y para IG alcanza de sobra
    "barato": ("minimax/hailuo-02", 0.28,
               {"duration": 6, "resolution": "768p", "prompt_optimizer": True}),
    "bueno": ("minimax/hailuo-02", 0.48,
              {"duration": 6, "resolution": "1080p", "prompt_optimizer": True}),
    "wan": ("wan-video/wan-2.5-t2v-fast", 0.20, {"duration": 5}),
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


def gastado_hoy():
    try:
        d = json.load(open(GASTO))
        return float(d.get(date.today().isoformat(), 0))
    except Exception:
        return 0.0


def anotar(monto):
    try:
        d = json.load(open(GASTO))
    except Exception:
        d = {}
    hoy = date.today().isoformat()
    d[hoy] = round(float(d.get(hoy, 0)) + monto, 3)
    json.dump(d, open(GASTO, "w"))
    return d[hoy]


def pedir(metodo, ruta, cuerpo, tok):
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
        return {"error": e.read().decode()[:300]}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("prompt")
    ap.add_argument("salida")
    ap.add_argument("--modelo", default="barato", choices=list(MODELOS))
    ap.add_argument("--confirmo", action="store_true",
                    help="obligatorio: confirma que sabés que esto cuesta plata")
    a = ap.parse_args()

    nombre, costo, extra = MODELOS[a.modelo]

    if not a.confirmo:
        print(f"Esto cuesta ~US${costo:.2f} por clip.", file=sys.stderr)
        print("Si estás de acuerdo, agregá  --confirmo", file=sys.stderr)
        return 1

    ya = gastado_hoy()
    if ya + costo > TOPE_DIARIO:
        print(f"CORTADO: hoy ya se gastaron US${ya:.2f} en Replicate.", file=sys.stderr)
        print(f"El tope diario es US${TOPE_DIARIO:.2f}. Mañana se reinicia.", file=sys.stderr)
        return 1

    tok = token()
    if not tok:
        print("ERROR: falta REPLICATE_API_TOKEN", file=sys.stderr)
        return 1

    entrada = {"prompt": a.prompt}
    entrada.update(extra)
    d = pedir("POST", f"/models/{nombre}/predictions", {"input": entrada}, tok)
    if d.get("error"):
        print(f"ERROR: {str(d['error'])[:200]}", file=sys.stderr)
        return 1
    pid = d.get("id")
    if not pid:
        print(f"ERROR: sin id · {json.dumps(d)[:200]}", file=sys.stderr)
        return 1

    print("generando video (puede tardar 1-3 minutos)...", file=sys.stderr)
    for _ in range(180):
        e = pedir("GET", f"/predictions/{pid}", None, tok)
        st = e.get("status")
        if st == "succeeded":
            out = e.get("output")
            url = out[0] if isinstance(out, list) else out
            if not url:
                print("ERROR: terminó sin video", file=sys.stderr)
                return 1
            crudo = a.salida + ".crudo.mp4"
            with urllib.request.urlopen(url, timeout=300) as r:
                open(crudo, "wb").write(r.read())

            # El modelo devuelve horizontal; Instagram Reels necesita 9:16.
            # Recortamos al centro y escalamos a 1080x1920.
            import subprocess
            ok = subprocess.run([
                "ffmpeg", "-y", "-i", crudo,
                "-vf", ("crop='min(iw,ih*9/16)':'min(ih,iw*16/9)',"
                        "scale=1080:1920:flags=lanczos"),
                "-c:v", "libx264", "-preset", "medium", "-crf", "20",
                "-pix_fmt", "yuv420p", "-movflags", "+faststart",
                a.salida], capture_output=True, timeout=300).returncode == 0

            if ok and os.path.exists(a.salida):
                os.remove(crudo)
            else:
                os.replace(crudo, a.salida)
                print("aviso: no se pudo recortar a 9:16, queda como vino",
                      file=sys.stderr)

            total = anotar(costo)
            print(f"(costó ~US${costo:.2f} · hoy van US${total:.2f} "
                  f"de US${TOPE_DIARIO:.2f})", file=sys.stderr)
            print(a.salida)
            return 0
        if st in ("failed", "canceled"):
            print(f"ERROR: {st} · {str(e.get('error'))[:200]}", file=sys.stderr)
            return 1
        time.sleep(3)

    print("ERROR: tardó demasiado", file=sys.stderr)
    return 1


if __name__ == "__main__":
    sys.exit(main())
