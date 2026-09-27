#!/usr/bin/env python3
"""
GONVRA — Publica en Instagram lo que esté en 2-APROBADO.

Soporta los tres formatos:
  · Una imagen suelta          -> post simple
  · Una CARPETA con imagenes   -> carrusel (2 a 10 fotos, en orden alfabetico)
  · Un video .mp4              -> reel

El texto sale de un .txt con el mismo nombre (o texto.txt dentro de la carpeta).
Si no hay nada que publicar, no imprime nada.
NADA se publica solo: Matias tiene que mover el archivo a 2-APROBADO.
"""
import json
import os
import shutil
import subprocess
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

BASE = os.path.expanduser("~/GONVRA-PUBLICAR")
APROBADO = os.path.join(BASE, "2-APROBADO")
PUBLICADO = os.path.join(BASE, "3-PUBLICADO")
SECRETS = os.path.expanduser("~/.hermes/.gonvra-secrets.env")
SUBIDOR = os.path.expanduser("~/.hermes/scripts/gonvra-subir-archivo.sh")
IGID = "28674883412124543"
API = "https://graph.instagram.com/v23.0"

IMGS = (".png", ".jpg", ".jpeg")
VIDS = (".mp4", ".mov")


def token():
    try:
        for l in open(SECRETS, encoding="utf-8"):
            if l.startswith("INSTAGRAM_ACCESS_TOKEN="):
                return l.split("=", 1)[1].strip()
    except Exception:
        pass
    return None


TOKEN = token()


def post(ruta, campos):
    campos["access_token"] = TOKEN
    # safe="," es CLAVE: sin esto, la coma de children=id1,id2 se codifica
    # como %2C e Instagram responde "Media ID is not available".
    datos = urllib.parse.urlencode(campos, safe=",").encode()
    req = urllib.request.Request(f"{API}/{ruta}", data=datos)
    try:
        with urllib.request.urlopen(req, timeout=90) as r:
            return json.loads(r.read().decode())
    except urllib.error.HTTPError as e:
        return {"error": json.loads(e.read().decode() or "{}").get("error", {})}


def get(ruta, campos=None):
    c = dict(campos or {})
    c["access_token"] = TOKEN
    url = f"{API}/{ruta}?" + urllib.parse.urlencode(c)
    try:
        with urllib.request.urlopen(url, timeout=60) as r:
            return json.loads(r.read().decode())
    except urllib.error.HTTPError as e:
        return {"error": json.loads(e.read().decode() or "{}").get("error", {})}


def subir(archivo):
    """Sube al CDN de Shopify y devuelve la URL publica."""
    r = subprocess.run(["bash", SUBIDOR, archivo],
                       capture_output=True, text=True, timeout=600)
    url = r.stdout.strip()
    return url if url.startswith("http") else None


def esperar_video(cid, minutos=5):
    """Instagram procesa el video; hay que esperar a que termine."""
    for _ in range(minutos * 6):
        d = get(cid, {"fields": "status_code"})
        st = d.get("status_code")
        if st == "FINISHED":
            return True
        if st == "ERROR":
            return False
        time.sleep(10)
    return False


def publicar(cid):
    d = post(f"{IGID}/media_publish", {"creation_id": cid})
    return d.get("id"), d.get("error", {}).get("message")


def permalink(pid):
    return get(pid, {"fields": "permalink"}).get("permalink", "")


def mover(rutas):
    os.makedirs(PUBLICADO, exist_ok=True)
    for r in rutas:
        try:
            destino = os.path.join(PUBLICADO, os.path.basename(r))
            if os.path.exists(destino):
                destino += f".{int(time.time())}"
            shutil.move(r, destino)
        except Exception:
            pass


def texto_de(ruta):
    """Busca el caption: archivo.txt al lado, o texto.txt dentro de la carpeta."""
    if os.path.isdir(ruta):
        p = os.path.join(ruta, "texto.txt")
    else:
        p = os.path.splitext(ruta)[0] + ".txt"
    if os.path.exists(p):
        return open(p, encoding="utf-8").read().strip(), p
    return "", None


def esperar_listo(cid, segundos=120):
    """Instagram procesa cada foto. Si no esta FINISHED, el carrusel falla
    con 'Media ID is not available'."""
    for _ in range(segundos // 5):
        st = get(cid, {"fields": "status_code"}).get("status_code")
        if st == "FINISHED":
            return True
        if st == "ERROR":
            return False
        time.sleep(5)
    return False


def hacer_post_simple(img, caption):
    url = subir(img)
    if not url:
        return None, "no se pudo subir la imagen"
    d = post(f"{IGID}/media", {"image_url": url, "caption": caption})
    cid = d.get("id")
    if not cid:
        return None, d.get("error", {}).get("message", "Instagram rechazo la imagen")
    # Esperar a que Instagram termine de procesarla. Sin esto, media_publish
    # falla con "Media ID is not available" (mismo bug que tenia el carrusel).
    if not esperar_listo(cid):
        return None, "Instagram no termino de procesar la imagen"
    return publicar(cid)


def hacer_carrusel(imagenes, caption):
    hijos = []
    for img in imagenes[:10]:
        url = subir(img)
        if not url:
            return None, f"no se pudo subir {os.path.basename(img)}"
        d = post(f"{IGID}/media", {"image_url": url, "is_carousel_item": "true"})
        cid = d.get("id")
        if not cid:
            return None, d.get("error", {}).get("message", "rechazo una foto del carrusel")
        hijos.append(cid)

    # Esperar a que TODAS esten procesadas antes de armar el carrusel
    for cid in hijos:
        if not esperar_listo(cid):
            return None, "Instagram no termino de procesar una de las fotos"

    d = post(f"{IGID}/media", {
        "media_type": "CAROUSEL",
        "children": ",".join(hijos),
        "caption": caption})
    cid = d.get("id")
    if not cid:
        return None, d.get("error", {}).get("message", "no se pudo armar el carrusel")
    return publicar(cid)


def hacer_reel(video, caption):
    url = subir(video)
    if not url:
        return None, "no se pudo subir el video"
    d = post(f"{IGID}/media", {
        "media_type": "REELS", "video_url": url, "caption": caption})
    cid = d.get("id")
    if not cid:
        return None, d.get("error", {}).get("message", "Instagram rechazo el video")
    if not esperar_video(cid):
        return None, "Instagram no termino de procesar el video"
    return publicar(cid)


def main():
    if not TOKEN:
        print("GONVRA: falta el token de Instagram")
        return 0
    if not os.path.isdir(APROBADO):
        return 0

    trabajos = []
    for nombre in sorted(os.listdir(APROBADO)):
        ruta = os.path.join(APROBADO, nombre)
        if os.path.isdir(ruta):
            fotos = sorted(f for f in os.listdir(ruta)
                           if f.lower().endswith(IMGS))
            if len(fotos) >= 2:
                trabajos.append(("carrusel", ruta,
                                 [os.path.join(ruta, f) for f in fotos]))
        elif nombre.lower().endswith(VIDS):
            trabajos.append(("reel", ruta, [ruta]))
        elif nombre.lower().endswith(IMGS):
            trabajos.append(("foto", ruta, [ruta]))

    if not trabajos:
        return 0

    for tipo, ruta, archivos in trabajos:
        caption, txt = texto_de(ruta)

        if tipo == "carrusel":
            pid, err = hacer_carrusel(archivos, caption)
            desc = f"carrusel de {len(archivos)} fotos"
        elif tipo == "reel":
            pid, err = hacer_reel(archivos[0], caption)
            desc = "reel"
        else:
            pid, err = hacer_post_simple(archivos[0], caption)
            desc = "foto"

        if not pid:
            print(f"GONVRA: fallo al publicar {os.path.basename(ruta)} ({desc})")
            print(f"  motivo: {err}")
            print("  El archivo sigue en 2-APROBADO, se reintenta despues.")
            continue

        link = permalink(pid)
        mover([ruta] + ([txt] if txt and not os.path.isdir(ruta) else []))

        print(f"PUBLICADO EN INSTAGRAM ({desc})")
        print()
        print(f"Archivo: {os.path.basename(ruta)}")
        if caption:
            print(f"Texto: {caption[:110]}...")
        if link:
            print(f"Ver: {link}")
        print()
        print("Fijate los comentarios: las preguntas son clientes.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
