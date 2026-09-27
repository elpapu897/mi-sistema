#!/usr/bin/env python3
"""Genera el QR para imprimir y pegar en el stand de la feria.

Uso:
    python3 hacer-qr.py https://usuario.github.io/sound-blue-project/
    python3 hacer-qr.py <url> --salida qr-stand.png

Sale un PNG de alta resolución, con el logo del proyecto en el centro y el
texto "ESCANEÁ Y ESCUCHÁ" abajo. Listo para imprimir en A5 o A4.

Requiere:  python3 -m pip install --user qrcode pillow
"""
import argparse
import os
import sys

try:
    import qrcode
    from qrcode.constants import ERROR_CORRECT_H
    from PIL import Image, ImageDraw, ImageFont
except ImportError:
    sys.exit("Falta una librería. Instalá con:\n"
             "    python3 -m pip install --user qrcode pillow")

AQUI = os.path.dirname(os.path.abspath(__file__))
AZUL = (6, 26, 69)
CIAN = (56, 189, 248)


def buscar_fuente(tam):
    """Devuelve una fuente TrueType del sistema, sea cual sea la distro."""
    rutas = [
        "/usr/share/fonts/google-carlito-fonts/Carlito-Bold.ttf",
        "/usr/share/fonts/adwaita-sans-fonts/AdwaitaSans-Regular.ttf",
        "/usr/share/fonts/dejavu-sans-fonts/DejaVuSans-Bold.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
        "/usr/share/fonts/liberation-sans/LiberationSans-Bold.ttf",
    ]
    # último recurso: preguntarle a fontconfig cuál es la sans-serif del sistema
    try:
        import subprocess
        r = subprocess.run(["fc-match", "-f", "%{file}", "sans-serif:bold"],
                           capture_output=True, text=True, timeout=5)
        if r.stdout.strip():
            rutas.append(r.stdout.strip())
    except Exception:
        pass
    for r in rutas:
        if os.path.exists(r):
            try:
                return ImageFont.truetype(r, tam)
            except Exception:
                pass
    print("Aviso: no se encontró una fuente TrueType; el texto va a salir chico.")
    return ImageFont.load_default()


def main():
    ap = argparse.ArgumentParser(description="QR del Sound Blue Project")
    ap.add_argument("url", help="Dirección web de la página ya publicada")
    ap.add_argument("--salida", default="qr-sound-blue.png")
    ap.add_argument("--sin-logo", action="store_true",
                    help="No pegar el logo en el centro")
    args = ap.parse_args()

    # ERROR_CORRECT_H aguanta hasta 30% de daño: por eso el logo del centro
    # no impide que el celular lo lea.
    qr = qrcode.QRCode(version=None, error_correction=ERROR_CORRECT_H,
                       box_size=20, border=3)
    qr.add_data(args.url)
    qr.make(fit=True)
    img = qr.make_image(fill_color=AZUL, back_color="white").convert("RGB")

    # logo al centro
    logo_path = os.path.join(AQUI, "assets", "img", "logo.jpg")
    if not args.sin_logo and os.path.exists(logo_path):
        lado = img.size[0] // 5
        logo = Image.open(logo_path).convert("RGB").resize((lado, lado), Image.LANCZOS)
        marco = Image.new("RGB", (lado + 24, lado + 24), "white")
        marco.paste(logo, (12, 12))
        pos = ((img.size[0] - marco.size[0]) // 2, (img.size[1] - marco.size[1]) // 2)
        img.paste(marco, pos)

    # lienzo final con título y pie
    m = 90
    alto_txt = 260
    lienzo = Image.new("RGB", (img.size[0] + m * 2, img.size[1] + m + alto_txt), "white")
    lienzo.paste(img, (m, m // 2))
    d = ImageDraw.Draw(lienzo)

    f_gr = buscar_fuente(78)
    f_ch = buscar_fuente(44)
    y = img.size[1] + m // 2 + 30

    def centrado(txt, fuente, y, color):
        an = d.textbbox((0, 0), txt, font=fuente)[2]
        d.text(((lienzo.size[0] - an) // 2, y), txt, font=fuente, fill=color)

    centrado("ESCANEÁ Y ESCUCHÁ", f_gr, y, AZUL)
    centrado("Sound Blue Project · Semáforo Sensorial", f_ch, y + 105, (90, 110, 140))

    salida = args.salida if os.path.isabs(args.salida) else os.path.join(AQUI, args.salida)
    lienzo.save(salida, dpi=(300, 300))
    print("QR generado:", salida)
    print("Apunta a:   ", args.url)
    print("Tamaño:     ", "x".join(map(str, lienzo.size)), "px @300dpi")


if __name__ == "__main__":
    main()
