#!/usr/bin/env python3
"""Renderiza carteles GONVRA 1080x1920 con PNG transparente.

Sistema visual fijado en TT-1 y heredado por TT-2 y TT-3.
Paleta: tinta #0D201A / marfil #F7F8F2 / lima #C8E54A / gris #66706B
Margenes seguros TikTok: nada de texto en los 150 px de arriba ni en los 250 de abajo.
"""
import sys, os
from PIL import Image, ImageDraw, ImageFont, ImageFilter

W, H = 1080, 1920
TINTA  = (13, 32, 26)
MARFIL = (247, 248, 242)
LIMA   = (200, 229, 74)
GRIS   = (102, 112, 107)

INTER_BLACK = os.path.expanduser("~/.local/share/fonts/Inter/Inter-Black.otf")
INTER_BOLD  = os.path.expanduser("~/.local/share/fonts/Inter/Inter-Bold.otf")
EMOJI       = "/usr/share/fonts/google-noto-emoji-fonts/NotoEmoji-Regular.ttf"

# zona segura de texto
SAFE_TOP, SAFE_BOTTOM = 150, 1920 - 250   # 150 .. 1670
MARGIN_X = 84
TEXT_W = W - 2 * MARGIN_X                  # 912 px utiles

EMOJI_SET = set("😖👀💧✅❌🔥")


def split_emoji(text):
    """Separa el texto en tramos (texto, es_emoji) para usar dos fuentes."""
    out, buf = [], ""
    for ch in text:
        is_e = ch in EMOJI_SET
        if buf and is_e != out_last(out):
            out.append((buf, out_last(out))); buf = ""
        buf += ch
        if not out or out_last(out) != is_e:
            pass
        out_flag = is_e
        if buf == ch:
            cur = is_e
        out_cur = cur
    return out


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


def measure(runs, fmain, femoji):
    w = 0
    for t, is_e in runs:
        f = femoji if is_e else fmain
        w += f.getlength(t)
    return w


def wrap(text, size):
    """Parte el texto en lineas que entren en TEXT_W con ese cuerpo."""
    fmain = ImageFont.truetype(INTER_BLACK, size)
    femoji = ImageFont.truetype(EMOJI, int(size * 0.92))
    words, lines, cur = text.split(), [], ""
    for wd in words:
        test = (cur + " " + wd).strip()
        if measure(tokenize(test), fmain, femoji) <= TEXT_W or not cur:
            cur = test
        else:
            lines.append(cur); cur = wd
    if cur:
        lines.append(cur)
    return lines, fmain, femoji


def fit(text, max_size=104, min_size=54, max_lines=3):
    """Baja el cuerpo hasta que entre en max_lines.

    Un '|' en el texto fuerza un salto de linea (evita huerfanas feas)."""
    if "|" in text:
        parts = [t.strip() for t in text.split("|")]
        for size in range(max_size, min_size - 1, -2):
            fmain = ImageFont.truetype(INTER_BLACK, size)
            femoji = ImageFont.truetype(EMOJI, int(size * 0.92))
            if all(measure(tokenize(t), fmain, femoji) <= TEXT_W for t in parts):
                return size, parts, fmain, femoji
        fmain = ImageFont.truetype(INTER_BLACK, min_size)
        femoji = ImageFont.truetype(EMOJI, int(min_size * 0.92))
        return min_size, parts, fmain, femoji
    for size in range(max_size, min_size - 1, -2):
        lines, fmain, femoji = wrap(text, size)
        if len(lines) <= max_lines:
            return size, lines, fmain, femoji
    return (min_size,) + wrap(text, min_size)


def draw_runs(d, x, y, runs, fmain, femoji, fill):
    for t, is_e in runs:
        f = femoji if is_e else fmain
        d.text((x, y), t, font=f, fill=fill, embedded_color=is_e)
        x += f.getlength(t)


def make_card(text, out_path, style="normal", anchor="bottom"):
    """style: normal | cta ; anchor: bottom | center"""
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))

    size, lines, fmain, femoji = fit(text)
    lh = int(size * 1.14)
    block_h = lh * len(lines)

    if anchor == "center":
        y0 = (H - block_h) // 2
    else:
        y0 = SAFE_BOTTOM - 120 - block_h          # bloque apoyado sobre el margen seguro
    y0 = max(y0, SAFE_TOP + 40)

    # --- scrim: degradado tinta desde abajo para garantizar contraste ---
    scrim = Image.new("L", (1, H), 0)
    sd = ImageDraw.Draw(scrim)
    grad_top = max(SAFE_TOP, y0 - 260)
    for y in range(grad_top, H):
        t = (y - grad_top) / max(1, (H - grad_top))
        sd.point((0, y), fill=int(215 * (t ** 0.75)))
    scrim = scrim.resize((W, H))
    SCRIM = (9, 11, 10)   # casi negro neutro: oscurece sin teñir de verde
    layer = Image.new("RGBA", (W, H), SCRIM + (255,))
    layer.putalpha(scrim)
    img = Image.alpha_composite(img, layer)

    d = ImageDraw.Draw(img)

    # --- barra lima de acento arriba del bloque ---
    bar_y = y0 - 46
    if style == "cta":
        d.rounded_rectangle([MARGIN_X, bar_y - 6, MARGIN_X + 132, bar_y + 4],
                            radius=5, fill=LIMA)
    else:
        d.rounded_rectangle([MARGIN_X, bar_y, MARGIN_X + 88, bar_y + 9],
                            radius=5, fill=LIMA)

    # --- texto (con sombra suave para despegarlo del video) ---
    shadow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    sdw = ImageDraw.Draw(shadow)
    for i, ln in enumerate(lines):
        runs = tokenize(ln)
        draw_runs(sdw, MARGIN_X + 3, y0 + i * lh + 4, runs, fmain, femoji, (0, 0, 0, 165))
    shadow = shadow.filter(ImageFilter.GaussianBlur(7))
    img = Image.alpha_composite(img, shadow)

    d = ImageDraw.Draw(img)
    color = LIMA + (255,) if style == "cta" else MARFIL + (255,)
    for i, ln in enumerate(lines):
        runs = tokenize(ln)
        draw_runs(d, MARGIN_X, y0 + i * lh, runs, fmain, femoji, color)

    img.save(out_path)
    return out_path, size, len(lines)


def make_endcard(out_path):
    """Cierre de marca: fondo tinta, wordmark y dominio. Sobrio."""
    img = Image.new("RGBA", (W, H), TINTA + (255,))
    d = ImageDraw.Draw(img)
    f = ImageFont.truetype(INTER_BLACK, 132)
    fd = ImageFont.truetype(INTER_BOLD, 52)
    word = "GONVRA"
    tw = d.textlength(word, font=f)
    d.text(((W - tw) / 2, 830), word, font=f, fill=MARFIL + (255,))
    # subrayado lima
    d.rounded_rectangle([(W - 150) / 2, 1000, (W + 150) / 2, 1010], radius=5, fill=LIMA)
    dom = "gonvra.com"
    dw = d.textlength(dom, font=fd)
    d.text(((W - dw) / 2, 1058), dom, font=fd, fill=LIMA + (255,))
    img.save(out_path)
    return out_path


if __name__ == "__main__":
    out = os.path.expanduser("~/Claude/gonvra-edits/carteles")
    cards = {
        # TT-1
        "t1_c1": "¿UN APARATO|PARA CADA ZONA?",
        "t1_c2": "Y NINGUNO HACE TODO",
        "t1_c3": "ESTA HACE LAS TRES",
        "t1_c4": "SE ENJUAGA|BAJO LA CANILLA",
        # TT-2
        "t2_c1": "¿LA MAQUINITA|TE DEJA LA PIEL|ARDIENDO? 😖",
        "t2_c2": "EL PROBLEMA|ES LA HOJA|PEGADA A LA PIEL",
        "t2_c3": "ESTA TIENE|LÁMINA DE ACERO|EN EL MEDIO 👀",
        "t2_c4": "Y SE LAVA|BAJO LA CANILLA 💧",
        # TT-3
        "t3_c1": "LO QUE VIENE|EN LA CAJA",
        "t3_c2": "3 PEINES:|1, 3 Y 5 MM",
        "t3_c3": "CEPILLO|DE LIMPIEZA",
        "t3_c4": "CARGA POR|CABLE USB",
    }
    for k, v in cards.items():
        p, s, n = make_card(v, f"{out}/{k}.png")
        print(f"{k:8} cuerpo={s:3} lineas={n}  {v}")
    make_endcard(f"{out}/endcard.png")
    print("endcard  OK")
