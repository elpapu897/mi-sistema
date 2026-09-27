#!/usr/bin/env python3
"""Genera EDL (CMX3600) y FCPXML (XMEML v5) de los tres anuncios.

Ambos referencian los CLIPS ORIGINALES con sus puntos de entrada y salida,
asi que al importarlos en Resolve queda una timeline editable de verdad
(un clip por corte), no un plano aplanado.
"""
import os, sys, html

sys.path.insert(0, os.path.expanduser("~/Claude/gonvra-edits"))
from build import ADS, SRC, ENDCARD, FPS, W, H   # una sola fuente de verdad

PROY = os.path.expanduser("~/Claude/gonvra-edits/proyecto")
CARTELES = os.path.expanduser("~/Claude/gonvra-edits/carteles")


def tc(seconds, fps=FPS):
    f = int(round(seconds * fps))
    h, r = divmod(f, 3600 * fps)
    m, r = divmod(r, 60 * fps)
    s, fr = divmod(r, fps)
    return f"{h:02d}:{m:02d}:{s:02d}:{fr:02d}"


def frames(seconds, fps=FPS):
    return int(round(seconds * fps))


def build_events(ad):
    """[(n, ruta, src_in, src_out, rec_in, rec_out, cartel)]"""
    ev, rec = [], 0.0
    for i, (key, t0, t1, card) in enumerate(ADS[ad], start=1):
        d = t1 - t0
        ev.append((i, SRC[key], t0, t1, rec, rec + d, card))
        rec += d
    ev.append((len(ev) + 1, f"{CARTELES}/endcard.png", 0.0, ENDCARD,
               rec, rec + ENDCARD, "endcard"))
    return ev


def write_edl(ad):
    ev = build_events(ad)
    out = f"{PROY}/{ad}.edl"
    L = [f"TITLE: {ad}", "FCM: NON-DROP FRAME", ""]
    for n, path, si, so, ri, ro, card in ev:
        reel = os.path.splitext(os.path.basename(path))[0][:8].upper().replace(" ", "_")
        L.append(f"{n:03d}  {reel:8} V     C        "
                 f"{tc(si)} {tc(so)} {tc(ri)} {tc(ro)}")
        L.append(f"* FROM CLIP NAME: {os.path.basename(path)}")
        if card and card != "endcard":
            L.append(f"* COMMENT: CARTEL {card}")
        L.append("")
    open(out, "w").write("\n".join(L))
    return out, len(ev)


def write_fcpxml(ad):
    ev = build_events(ad)
    total = frames(ev[-1][5])
    files, seen = [], {}
    for _, path, *_ in ev:
        if path not in seen:
            seen[path] = f"file-{len(seen)+1}"
            files.append((seen[path], path))

    items = []
    for n, path, si, so, ri, ro, card in ev:
        fid = seen[path]
        nm = html.escape(os.path.basename(path))
        first = f'''
            <file id="{fid}">
              <name>{nm}</name>
              <pathurl>file://{html.escape(path)}</pathurl>
              <rate><timebase>{FPS}</timebase><ntsc>FALSE</ntsc></rate>
              <media><video><samplecharacteristics>
                <width>{W}</width><height>{H}</height>
              </samplecharacteristics></video></media>
            </file>''' if fid not in [i[0] for i in items] else f'<file id="{fid}"/>'
        items.append((fid, f'''
          <clipitem id="clip-{n}">
            <name>{nm}</name>
            <rate><timebase>{FPS}</timebase><ntsc>FALSE</ntsc></rate>
            <start>{frames(ri)}</start>
            <end>{frames(ro)}</end>
            <in>{frames(si)}</in>
            <out>{frames(so)}</out>{first}
          </clipitem>'''))

    # pista 2: los carteles como archivos PNG, alineados al corte que acompañan
    cards = []
    for n, path, si, so, ri, ro, card in ev:
        if not card or card == "endcard":
            continue
        p = f"{CARTELES}/{card}.png"
        cards.append(f'''
          <clipitem id="card-{n}">
            <name>{card}.png</name>
            <rate><timebase>{FPS}</timebase><ntsc>FALSE</ntsc></rate>
            <start>{frames(ri)}</start>
            <end>{frames(ro)}</end>
            <in>0</in>
            <out>{frames(ro - ri)}</out>
            <file id="card-file-{n}">
              <name>{card}.png</name>
              <pathurl>file://{p}</pathurl>
              <rate><timebase>{FPS}</timebase><ntsc>FALSE</ntsc></rate>
              <media><video><samplecharacteristics>
                <width>{W}</width><height>{H}</height>
              </samplecharacteristics></video></media>
            </file>
          </clipitem>''')

    xml = f'''<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE xmeml>
<xmeml version="5">
  <sequence id="{ad}">
    <name>{ad}</name>
    <duration>{total}</duration>
    <rate><timebase>{FPS}</timebase><ntsc>FALSE</ntsc></rate>
    <media>
      <video>
        <format><samplecharacteristics>
          <width>{W}</width><height>{H}</height>
          <rate><timebase>{FPS}</timebase><ntsc>FALSE</ntsc></rate>
        </samplecharacteristics></format>
        <track>{"".join(i[1] for i in items)}
        </track>
        <track>{"".join(cards)}
        </track>
      </video>
    </media>
  </sequence>
</xmeml>
'''
    out = f"{PROY}/{ad}.fcpxml"
    open(out, "w").write(xml)
    return out, len(ev), len(cards)


if __name__ == "__main__":
    os.makedirs(PROY, exist_ok=True)
    for ad in ADS:
        e, n = write_edl(ad)
        x, nc, ncard = write_fcpxml(ad)
        print(f"{ad:16} EDL {n} eventos -> {os.path.basename(e)} | "
              f"XML {nc} clips + {ncard} carteles -> {os.path.basename(x)}")
