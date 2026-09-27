#!/usr/bin/env python3
"""
render_carousel.py — render an on-brand 1080x1350 carousel to PNG slides.

Text is rendered as crisp HTML/CSS via headless Chrome (image models can't be
trusted with paragraph text). An optional per-slide background image (e.g. a
fal-media generation) sits behind the type with a readability scrim.

Usage:
    python3 render_carousel.py <carousel_dir>

<carousel_dir> must contain slides.json:
{
  "brand": { ...optional, else falls back to social-content-os/brand.json... },
  "slides": [
    {"n":1,"type":"hook","theme":"dark","eyebrow":"COFFEE TRUTHS",
     "headline":"This coffee should not taste this good.","body":"",
     "bg_image":"bg-1.png"},
    ...
  ]
}

Output: slide-01.png ... slide-NN.png in <carousel_dir>, at 2x (2160x2700).
"""
import json
import os
import shutil
import subprocess
import sys
import html as htmllib

W, H = 1080, 1350
SCALE = 2

# Chrome/Chromium binary: env override first, then common locations on
# macOS / Linux / Windows-WSL, then anything on PATH. Keeps the renderer
# portable for whoever installs the pack.
CHROME_CANDIDATES = [
    os.environ.get("CHROME_BIN", ""),
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "/Applications/Chromium.app/Contents/MacOS/Chromium",
    "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge",
    "/usr/bin/google-chrome",
    "/usr/bin/google-chrome-stable",
    "/usr/bin/chromium",
    "/usr/bin/chromium-browser",
    "/snap/bin/chromium",
]


def find_chrome():
    for path in CHROME_CANDIDATES:
        if path and os.path.exists(path):
            return path
    for name in ("google-chrome", "chromium", "chromium-browser", "chrome"):
        found = shutil.which(name)
        if found:
            return found
    sys.exit(
        "Chrome/Chromium not found. Install Google Chrome, or set CHROME_BIN to "
        "your browser binary, e.g.\n  CHROME_BIN=/path/to/chrome python3 "
        "render_carousel.py <carousel_dir>")

DEFAULT_BRAND = {
    "handle": "@yourhandle",
    "colors": {"bg": "#0E0E10", "bg_alt": "#F5F1E8", "ink": "#0E0E10",
               "ink_inverse": "#F5F1E8", "accent": "#FF4D2E", "muted": "#8A8A8A"},
    "typography": {
        "display": '"Avenir Next","Helvetica Neue",Arial,sans-serif',
        "body": '"Helvetica Neue",Arial,sans-serif'},
    "cta": {"comment_word": "GUIDE"},
}


def load_brand(carousel_dir, inline):
    if inline:
        b = dict(DEFAULT_BRAND)
        b.update(inline)
        for k in ("colors", "typography", "cta"):
            merged = dict(DEFAULT_BRAND.get(k, {}))
            merged.update(inline.get(k, {}))
            b[k] = merged
        return b
    here = os.path.dirname(os.path.abspath(__file__))
    fallback = os.path.join(here, "..", "social-content-os", "brand.json")
    if os.path.exists(fallback):
        with open(fallback) as f:
            data = json.load(f)
        b = dict(DEFAULT_BRAND)
        for k in ("colors", "typography", "cta"):
            merged = dict(DEFAULT_BRAND[k])
            merged.update(data.get(k, {}))
            b[k] = merged
        b["handle"] = data.get("handle", DEFAULT_BRAND["handle"])
        return b
    return DEFAULT_BRAND


def dots(n, total, accent, muted):
    out = []
    for i in range(1, total + 1):
        c = accent if i == n else muted
        w = "30px" if i == n else "10px"
        out.append(
            f'<span style="display:inline-block;height:10px;width:{w};'
            f'border-radius:6px;background:{c};margin-right:8px;"></span>')
    return "".join(out)


def slide_html(slide, brand, total):
    c = brand["colors"]
    typ = brand["typography"]
    theme = slide.get("type") == "hook" and "dark" or slide.get("theme", "light")
    if theme == "dark":
        bg, ink, sub = c["bg"], c["ink_inverse"], c["muted"]
    else:
        bg, ink, sub = c["bg_alt"], c["ink"], c["muted"]
    accent = c["accent"]
    n = slide.get("n", 1)
    stype = slide.get("type", "value")
    eyebrow = htmllib.escape(slide.get("eyebrow", "")).upper()
    headline = htmllib.escape(slide.get("headline", ""))
    body = htmllib.escape(slide.get("body", ""))
    handle = htmllib.escape(brand.get("handle", ""))

    bg_layer = ""
    if slide.get("bg_image"):
        scrim = "rgba(14,14,16,0.72)" if theme == "dark" else "rgba(245,241,232,0.78)"
        bg_layer = (
            f'<div style="position:absolute;inset:0;'
            f'background-image:linear-gradient({scrim},{scrim}),'
            f'url(\'{slide["bg_image"]}\');'
            f'background-size:cover;background-position:center;"></div>')

    # headline size scales down as it gets longer
    hl_len = len(slide.get("headline", ""))
    hsize = 104 if stype == "hook" else 78
    if hl_len > 70:
        hsize = int(hsize * 0.8)
    if hl_len > 120:
        hsize = int(hsize * 0.82)

    if stype == "hook":
        center = (
            f'<div style="position:relative;z-index:2;">'
            f'<div style="width:84px;height:8px;background:{accent};'
            f'margin-bottom:40px;border-radius:4px;"></div>'
            f'<h1 style="font-family:{typ["display"]};font-weight:800;'
            f'font-size:{hsize}px;line-height:1.02;letter-spacing:-0.02em;'
            f'color:{ink};margin:0;">{headline}</h1>'
            + (f'<p style="font-family:{typ["body"]};font-size:34px;'
               f'line-height:1.35;color:{sub};margin-top:36px;max-width:80%;">'
               f'{body}</p>' if body else "")
            + '</div>')
    elif stype == "cta":
        word = htmllib.escape(brand.get("cta", {}).get("comment_word", "GUIDE"))
        center = (
            f'<div style="position:relative;z-index:2;">'
            f'<div style="width:84px;height:8px;background:{accent};'
            f'margin-bottom:40px;border-radius:4px;"></div>'
            f'<h1 style="font-family:{typ["display"]};font-weight:800;'
            f'font-size:{hsize}px;line-height:1.05;letter-spacing:-0.02em;'
            f'color:{ink};margin:0 0 44px;">{headline}</h1>'
            + (f'<p style="font-family:{typ["body"]};font-size:36px;'
               f'line-height:1.4;color:{ink};opacity:.85;margin:0 0 48px;'
               f'max-width:88%;">{body}</p>' if body else "")
            + f'<div style="display:inline-block;background:{accent};color:#fff;'
            f'font-family:{typ["display"]};font-weight:800;font-size:40px;'
            f'padding:26px 46px;border-radius:18px;">Comment '
            f'&ldquo;{word}&rdquo;</div></div>')
    else:  # value
        center = (
            f'<div style="position:relative;z-index:2;">'
            + (f'<div style="font-family:{typ["display"]};font-weight:800;'
               f'font-size:120px;color:{accent};line-height:1;'
               f'margin-bottom:24px;">{n - 1:02d}</div>')
            + f'<h2 style="font-family:{typ["display"]};font-weight:800;'
            f'font-size:{hsize}px;line-height:1.06;letter-spacing:-0.02em;'
            f'color:{ink};margin:0 0 28px;">{headline}</h2>'
            + (f'<p style="font-family:{typ["body"]};font-size:38px;'
               f'line-height:1.45;color:{ink};opacity:.82;max-width:92%;">'
               f'{body}</p>' if body else "")
            + '</div>')

    eyebrow_el = (
        f'<div style="position:relative;z-index:2;font-family:{typ["body"]};'
        f'font-weight:700;font-size:26px;letter-spacing:0.18em;color:{accent};">'
        f'{eyebrow}</div>' if eyebrow else '<div></div>')

    footer = (
        f'<div style="position:relative;z-index:2;display:flex;'
        f'justify-content:space-between;align-items:center;">'
        f'<div>{dots(n, total, accent, sub)}</div>'
        f'<div style="font-family:{typ["body"]};font-weight:700;font-size:28px;'
        f'color:{sub};">{handle}</div></div>')

    return f"""<!doctype html><html><head><meta charset="utf-8">
<style>*{{margin:0;padding:0;box-sizing:border-box;}}
html,body{{width:{W}px;height:{H}px;}}
.slide{{position:relative;width:{W}px;height:{H}px;background:{bg};
overflow:hidden;padding:88px 84px;display:flex;flex-direction:column;
justify-content:space-between;-webkit-font-smoothing:antialiased;}}
</style></head><body><div class="slide">{bg_layer}{eyebrow_el}{center}{footer}</div></body></html>"""


def main():
    if len(sys.argv) < 2:
        print("usage: python3 render_carousel.py <carousel_dir>")
        sys.exit(1)
    cdir = os.path.abspath(sys.argv[1])
    chrome = find_chrome()
    with open(os.path.join(cdir, "slides.json")) as f:
        data = json.load(f)
    brand = load_brand(cdir, data.get("brand"))
    slides = data["slides"]
    total = len(slides)
    build = os.path.join(cdir, ".build")
    os.makedirs(build, exist_ok=True)

    for s in slides:
        n = s.get("n", slides.index(s) + 1)
        if s.get("bg_image") and not os.path.isabs(s["bg_image"]):
            s["bg_image"] = os.path.join(cdir, s["bg_image"])
        hpath = os.path.join(build, f"slide-{n:02d}.html")
        with open(hpath, "w") as f:
            f.write(slide_html(s, brand, total))
        out = os.path.join(cdir, f"slide-{n:02d}.png")
        subprocess.run([
            chrome, "--headless=new", "--disable-gpu", "--hide-scrollbars",
            "--no-sandbox", "--default-background-color=00000000",
            f"--force-device-scale-factor={SCALE}",
            f"--window-size={W},{H}",
            f"--screenshot={out}", f"file://{hpath}",
        ], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print(f"rendered {out}")

    print(f"done: {total} slides in {cdir}")


if __name__ == "__main__":
    main()
