#!/usr/bin/env python3
"""Genera los tres carruseles de Instagram (1080x1350) de GONVRA.

Usa SOLO clips ya aprobados en la revision cuadro por cuadro, con la misma
correccion de color y el mismo sistema de carteles que los tres anuncios.
No se genera material nuevo ni se reutiliza ningun clip descartado.
"""
import os, sys, subprocess, shlex
from PIL import Image, ImageDraw, ImageFont, ImageFilter

ED = os.path.expanduser("~/Claude/gonvra-edits")
sys.path.insert(0, ED)
from build import SRC, vf_for   # misma fuente de verdad que los anuncios

CW, CH = 1080, 1350            # formato 4:5 de Instagram
MARGIN_X = 84
TEXT_W = CW - 2 * MARGIN_X
TINTA  = (13, 32, 26)
MARFIL = (247, 248, 242)
LIMA   = (200, 229, 74)
SCRIM  = (9, 11, 10)

INTER_BLACK = os.path.expanduser("~/.local/share/fonts/Inter/Inter-Black.otf")
INTER_BOLD  = os.path.expanduser("~/.local/share/fonts/Inter/Inter-Bold.otf")
EMOJI       = "/usr/share/fonts/google-noto-emoji-fonts/NotoEmoji-Regular.ttf"
EMOJI_SET   = set("😖👀💧")

OUT = f"{ED}/carruseles"

# (clip, segundo, desplazamiento vertical del recorte 0-1, texto)
CARRUSELES = {
    "C1-El-Cajon": [
        ("cajon", 1.60, 0.40, "¿UN APARATO|PARA CADA ZONA?"),
        ("cajon", 2.55, 0.40, "Y NINGUNO|HACE TODO"),
        ("mesada", 1.40, 0.30, "ESTA HACE|LAS TRES"),
        ("rostro", 2.20, 0.30, "ROSTRO, CUERPO|Y ZONA ÍNTIMA"),
        ("enjuague", 2.60, 0.30, "SE ENJUAGA|BAJO LA CANILLA"),
        (None,    None, None, "CTA"),
    ],
    "C2-La-Lamina": [
        ("brazo", 1.60, 0.35, "¿LA MAQUINITA|TE DEJA LA PIEL|ARDIENDO? 😖"),
        ("brazo", 4.80, 0.35, "EL PROBLEMA|ES LA HOJA|PEGADA A LA PIEL"),
        ("blade", 4.20, 0.40, "ESTA TIENE|LÁMINA DE ACERO|EN EL MEDIO 👀"),
        ("blade", 6.00, 0.40, "SE USA|EN SECO"),
        ("enjuague", 3.40, 0.30, "Y SE LAVA|BAJO LA CANILLA 💧"),
        (None,    None, None, "CTA"),
    ],
    "C3-Que-Trae": [
        ("kit",      0.40, "entero", "LO QUE VIENE|EN LA CAJA"),
        ("kit",      2.60, 0.40, "3 PEINES:|1, 3 Y 5 MM"),
        ("limpieza", 1.40, 0.40, "CEPILLO|DE LIMPIEZA"),
        ("limpieza", 6.80, 0.45, "CARGA POR|CABLE USB"),
        ("kit",      5.40, 0.40, "TODO CON|UN SOLO EQUIPO"),
        (None,       None, None, "CTA"),
    ],
}


def tokenize(text):
    runs, cur, cur_is = [], "", None
    for ch in text:
        e = ch in EMOJI_SET
        if cur_is is None:
            cur, cur_is = ch, e
        elif e == cur_is:
            cur += ch
        else:
            runs.append((cur, cur_is)); cur, cur_is = ch, e
    if cur:
        runs.append((cur, cur_is))
    return runs


def measure(runs, fm, fe):
    return sum((fe if e else fm).getlength(t) for t, e in runs)


def fit(lines_raw, max_size=96, min_size=48):
    parts = [p.strip() for p in lines_raw.split("|")]
    for size in range(max_size, min_size - 1, -2):
        fm = ImageFont.truetype(INTER_BLACK, size)
        fe = ImageFont.truetype(EMOJI, int(size * 0.92))
        if all(measure(tokenize(p), fm, fe) <= TEXT_W for p in parts):
            return size, parts, fm, fe
    fm = ImageFont.truetype(INTER_BLACK, min_size)
    fe = ImageFont.truetype(EMOJI, int(min_size * 0.92))
    return min_size, parts, fm, fe


def draw_runs(d, x, y, runs, fm, fe, fill):
    for t, e in runs:
        f = fe if e else fm
        d.text((x, y), t, font=f, fill=fill, embedded_color=e)
        x += f.getlength(t)


def fit_whole(im):
    """Encaja el cuadro completo dentro de 4:5 sin recortar (fondo tinta)."""
    r = min(CW / im.width, CH / im.height)
    nw, nh = int(im.width * r), int(im.height * r)
    canvas = Image.new("RGB", (CW, CH), TINTA)
    canvas.paste(im.resize((nw, nh), Image.LANCZOS), ((CW - nw) // 2, (CH - nh) // 2))
    return canvas


def grab_frame(key, sec, offset):
    """Extrae un cuadro con la MISMA correccion de color del anuncio y recorta a 4:5."""
    tmp = "/tmp/_car_src.png"
    subprocess.run(f'ffmpeg -y -v error -ss {sec} -i {shlex.quote(SRC[key])} '
                   f'-vf {shlex.quote(vf_for(key))} -frames:v 1 {tmp}',
                   shell=True, check=True)
    im = Image.open(tmp).convert("RGB")          # 1080x1920 ya corregido
    if offset == "entero":
        return fit_whole(im)
    top = int((im.height - CH) * offset)
    return im.crop((0, top, CW, top + CH))


def slide(img, text, idx, total, path):
    img = img.convert("RGBA")
    size, lines, fm, fe = fit(text)
    lh = int(size * 1.14)
    block = lh * len(lines)
    y0 = CH - 150 - block

    # scrim neutro para asegurar contraste sobre cualquier fondo
    sc = Image.new("L", (1, CH), 0)
    sd = ImageDraw.Draw(sc)
    top = max(0, y0 - 250)
    for y in range(top, CH):
        t = (y - top) / max(1, CH - top)
        sd.point((0, y), fill=int(215 * (t ** 0.75)))
    layer = Image.new("RGBA", (CW, CH), SCRIM + (255,))
    layer.putalpha(sc.resize((CW, CH)))
    img = Image.alpha_composite(img, layer)

    d = ImageDraw.Draw(img)
    d.rounded_rectangle([MARGIN_X, y0 - 46, MARGIN_X + 88, y0 - 37], radius=5, fill=LIMA)

    sh = Image.new("RGBA", (CW, CH), (0, 0, 0, 0))
    sdw = ImageDraw.Draw(sh)
    for i, ln in enumerate(lines):
        draw_runs(sdw, MARGIN_X + 3, y0 + i * lh + 4, tokenize(ln), fm, fe, (0, 0, 0, 165))
    img = Image.alpha_composite(img, sh.filter(ImageFilter.GaussianBlur(7)))

    d = ImageDraw.Draw(img)
    for i, ln in enumerate(lines):
        draw_runs(d, MARGIN_X, y0 + i * lh, tokenize(ln), fm, fe, MARFIL + (255,))

    # indicador de progreso del carrusel
    bw, gap = 34, 10
    tw = total * bw + (total - 1) * gap
    x = (CW - tw) / 2
    for i in range(total):
        c = LIMA + (255,) if i == idx else (255, 255, 255, 90)
        d.rounded_rectangle([x + i * (bw + gap), 56, x + i * (bw + gap) + bw, 63],
                            radius=4, fill=c)
    img.convert("RGB").save(path, quality=95)


def cta_slide(path, idx, total):
    img = Image.new("RGB", (CW, CH), TINTA)
    d = ImageDraw.Draw(img)
    f = ImageFont.truetype(INTER_BLACK, 140)
    fd = ImageFont.truetype(INTER_BOLD, 54)
    fs = ImageFont.truetype(INTER_BOLD, 40)
    w = d.textlength("GONVRA", font=f)
    d.text(((CW - w) / 2, 500), "GONVRA", font=f, fill=MARFIL)
    d.rounded_rectangle([(CW - 160) / 2, 682, (CW + 160) / 2, 692], radius=5, fill=LIMA)
    w = d.textlength("gonvra.com", font=fd)
    d.text(((CW - w) / 2, 742), "gonvra.com", font=fd, fill=LIMA)
    sub = "Envío a todo el país con seguimiento"
    w = d.textlength(sub, font=fs)
    d.text(((CW - w) / 2, 836), sub, font=fs, fill=(150, 158, 153))
    bw, gap = 34, 10
    tw = total * bw + (total - 1) * gap
    x = (CW - tw) / 2
    for i in range(total):
        c = LIMA if i == idx else (70, 76, 72)
        d.rounded_rectangle([x + i * (bw + gap), 56, x + i * (bw + gap) + bw, 63],
                            radius=4, fill=c)
    img.save(path, quality=95)


if __name__ == "__main__":
    for nombre, slides in CARRUSELES.items():
        carpeta = f"{OUT}/{nombre}"
        os.makedirs(carpeta, exist_ok=True)
        total = len(slides)
        for i, (key, sec, off, text) in enumerate(slides):
            p = f"{carpeta}/{i+1:02d}.jpg"
            if key is None:
                cta_slide(p, i, total)
            else:
                slide(grab_frame(key, sec, off), text, i, total, p)
            print(f"  {nombre}/{i+1:02d}.jpg  {text[:44]}")
        print()
