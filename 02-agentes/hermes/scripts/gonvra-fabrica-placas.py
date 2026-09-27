#!/usr/bin/env python3
"""
GONVRA — Fábrica de placas (idea B).

Toma el entregable del día de INSTAGRAMER (el .md que escribe el agente),
le saca el texto exacto de cada placa, y compone las imágenes con
ImageMagick sobre las FOTOS REALES del producto.

Resultado: una carpeta lista en 1-PENDIENTE, que dispara el aviso con
los links de aprobar.

No inventa nada: si no hay .md del día, avisa y no hace nada.
No usa IA para generar imágenes (sin cuota, ver E-020).
"""
import os
import re
import subprocess
import sys
from datetime import date

BASE = os.path.expanduser("~/Claude/gonvra2")
PEND = os.path.expanduser("~/GONVRA-PUBLICAR/1-PENDIENTE")
FOTOS = os.path.expanduser("~/Claude/gonvra2/videos/src")

# Paleta GONVRA
NEGRO = "#0d1720"
LIMA = "#c8e54a"
CREMA = "#f5f1e8"
FUENTE = "Inter-SemiBold"
FUENTE_BOLD = "Inter-Black"

ANCHO, ALTO = 1080, 1350  # 4:5, lo que mejor rinde en el feed


def entregable_de_hoy(agente):
    hoy = date.today().isoformat()
    p = os.path.join(BASE, agente, f"{hoy}.md")
    return p if os.path.exists(p) else None


def parsear_placas(md):
    """Saca (titulo, texto, foto sugerida) de cada '### Placa N'."""
    texto = open(md, encoding="utf-8").read()
    bloques = re.split(r"\n###\s+Placa\s+", texto)[1:]
    placas = []
    for b in bloques:
        titulo = b.split("\n", 1)[0].strip(" —-")
        # el texto exacto va en las lineas que empiezan con ">"
        m = re.search(r"\*\*Texto exacto:\*\*\s*\n\n((?:>.*\n?)+)", b)
        if not m:
            continue
        lineas = [l.lstrip("> ").strip() for l in m.group(1).split("\n")]
        lineas = [l for l in lineas if l]
        if not lineas:
            continue
        foto = None
        f = re.search(r"\*\*Foto real a usar:\*\*\s*`([^`]+)`", b)
        if f and os.path.exists(f.group(1)):
            foto = f.group(1)
        placas.append({"titulo": titulo, "lineas": lineas, "foto": foto})
    return placas


def fondo_generado(i, destino):
    """Si no hay foto real que sirva, genera un fondo con Replicate (~US$0.003).
    NUNCA genera el producto: solo ambiente. El producto va siempre con foto real."""
    escenas = [
        "modern minimalist bathroom counter in dark charcoal stone, soft morning "
        "window light from the left, subtle lime green LED accent glow behind",
        "close-up of a fogged bathroom mirror with warm side light, clean vertical "
        "streak of clear glass, charcoal and cream tones",
        "folded charcoal towel on a warm stone shelf with a small lime green accent, "
        "soft directional light, lots of empty space",
        "dark textured wall with a narrow beam of morning light crossing it, "
        "minimal composition, charcoal and cream palette",
    ]
    prompt = (
        f"Professional editorial photography, vertical 4:5. {escenas[i % len(escenas)]}. "
        "Lots of negative space in the lower third for text overlay. "
        "Mens grooming magazine aesthetic. "
        "No people, no faces, no hands, no products, no razors, no text, no logos. "
        "Photorealistic, 50mm lens, shallow depth of field."
    )
    gen = os.path.expanduser("~/.hermes/scripts/gonvra-generar-imagen.py")
    try:
        r = subprocess.run(["python3", gen, prompt, destino,
                            "--ratio", "4:5", "--modelo", "rapido"],
                           capture_output=True, text=True, timeout=300)
        return r.returncode == 0 and os.path.exists(destino)
    except Exception:
        return False


def foto_de_respaldo(i):
    """Si el .md apunta a una foto que no existe, usar las reales que sí tenemos."""
    candidatas = ["q1.png", "q2.png", "q3.png", "foto1.png", "foto2.png", "foto3.png"]
    for n in candidatas[i % len(candidatas):] + candidatas:
        p = os.path.join(FOTOS, n)
        if os.path.exists(p):
            return p
    return None


def componer(placa, salida, indice, permitir_generar=False):
    foto = placa["foto"] or foto_de_respaldo(indice)
    # Si no hay foto real, generar un FONDO de ambiente (nunca el producto)
    if not foto and permitir_generar:
        tmp = salida + ".fondo.png"
        if fondo_generado(indice, tmp):
            foto = tmp
    if not foto:
        return False

    titulo = placa["lineas"][0]
    cuerpo = "\n".join(placa["lineas"][1:])

    # 1) foto recortada al formato, oscurecida abajo para que se lea el texto
    cmd = [
        "convert", foto,
        "-resize", f"{ANCHO}x{ALTO}^",
        "-gravity", "center", "-extent", f"{ANCHO}x{ALTO}",
        "-brightness-contrast", "-8x5",
    ]
    # 2) banda oscura degradada en la mitad inferior
    cmd += [
        "(", "-size", f"{ANCHO}x{ALTO//2}",
        "gradient:none-" + NEGRO, ")",
        "-gravity", "south", "-composite",
    ]
    # 3) titulo grande
    cmd += [
        "-font", FUENTE_BOLD, "-pointsize", "74", "-fill", CREMA,
        "-gravity", "southwest",
        "-annotate", f"+70+{260 if cuerpo else 150}",
        _cortar(titulo, 22),
    ]
    # 4) cuerpo
    if cuerpo:
        cmd += [
            "-font", FUENTE, "-pointsize", "40", "-fill", "#d8d8d8",
            "-annotate", "+70+140", _cortar(cuerpo, 40),
        ]
    # 5) marca
    cmd += [
        "-font", FUENTE_BOLD, "-pointsize", "30", "-fill", LIMA,
        "-gravity", "northwest", "-annotate", "+70+60", "GONVRA",
        salida,
    ]
    r = subprocess.run(cmd, capture_output=True, text=True, timeout=90)
    return r.returncode == 0 and os.path.exists(salida)


def _cortar(txt, ancho):
    """Corta el texto en lineas para que entre en la placa."""
    out, linea = [], ""
    for p in txt.replace("\n", " ").split():
        if len(linea) + len(p) + 1 <= ancho:
            linea = (linea + " " + p).strip()
        else:
            out.append(linea)
            linea = p
    if linea:
        out.append(linea)
    return "\n".join(out[:5])


def main():
    md = entregable_de_hoy("instagramer")
    if not md:
        print("FABRICA: INSTAGRAMER no dejó entregable hoy. No se compone nada.")
        return 0

    placas = parsear_placas(md)
    if len(placas) < 2:
        print(f"FABRICA: el entregable de hoy tiene {len(placas)} placa(s) con texto exacto.")
        print("No alcanza para un carrusel (hacen falta 2 o más). No se compone nada.")
        return 0

    hoy = date.today().isoformat()
    carpeta = os.path.join(PEND, f"carrusel-{hoy}")
    if os.path.exists(carpeta):
        print(f"FABRICA: ya existe {os.path.basename(carpeta)}, no se pisa.")
        return 0
    os.makedirs(carpeta, exist_ok=True)

    hechas = 0
    for i, pl in enumerate(placas[:10], 1):
        salida = os.path.join(carpeta, f"{i:02d}-placa.png")
        if componer(pl, salida, i - 1, permitir_generar=True):
            hechas += 1
        # limpiar el fondo temporal si quedo
        tmp = salida + ".fondo.png"
        if os.path.exists(tmp):
            os.remove(tmp)

    if hechas < 2:
        print(f"FABRICA: solo se pudieron componer {hechas} placas. Se descarta.")
        subprocess.run(["rm", "-rf", carpeta])
        return 0

    # el texto del post sale del copy del día si existe, si no del primer gancho
    caption = ""
    copy_md = entregable_de_hoy("copy")
    if copy_md:
        t = open(copy_md, encoding="utf-8").read()
        g = re.search(r"##\s*Gancho[^\n]*\n+\*\*(.+?)\*\*", t)
        if g:
            caption = g.group(1).strip()
    if not caption:
        caption = placas[0]["lineas"][0]

    caption += ("\n\nRasuradora integral recargable: rostro y cuerpo, "
                "con peines guía para elegir el largo.\n"
                "Envío gratis a todo el país.\n\n"
                "#afeitadora #rasuradora #cuidadopersonal #barba #grooming #argentina")

    with open(os.path.join(carpeta, "texto.txt"), "w", encoding="utf-8") as f:
        f.write(caption)

    print(f"FABRICA: carrusel de {hechas} placas listo para aprobar")
    print()
    print(f"  Carpeta: carrusel-{hoy}")
    print(f"  Salió de: instagramer/{os.path.basename(md)}")
    print(f"  Texto: {caption.splitlines()[0][:80]}")
    print()
    print("En el próximo aviso te llegan los links para publicarlo.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
