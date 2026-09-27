#!/usr/bin/env python3
"""Monta los tres anuncios GONVRA para TikTok con ffmpeg.

Plan B: el MCP davinci-resolve no conecta (Resolve 21.1 free bloquea el scripting
externo), asi que el montaje se hace con ffmpeg y se entrega ademas el proyecto
editable en .drp + EDL.

Todo sale a 1080x1920, 24 fps, h264 yuv420p.
"""
import os, subprocess, json, shlex

HOME = os.path.expanduser("~")
ED   = f"{HOME}/Claude/gonvra-edits"
CAR  = f"{ED}/carteles"
REC  = f"{ED}/recortes"
OUT  = f"{ED}/finales"

FPS = 24
W, H = 1080, 1920

# ---------------------------------------------------------------- fuentes
SRC = {
    "cajon":    f"{HOME}/Descargas/gonvra-flow-nuevo/cajon-720p.mp4",
    "cajon_360": f"{HOME}/Claude/gonvra-brand/clips-utiles/hook-cajon-desordenado.mp4",
    "mesada":   f"{HOME}/Descargas/gonvra-flow-nuevo/mesada-720p.mp4",
    "enjuague": f"{HOME}/Descargas/gonvra-flow-nuevo/enjuague-720p.mp4",
    "cajon2":   f"{HOME}/Descargas/videos para gonvra/Man_organizing_cluttered_bathroo…_202609061304.mp4",
    "brazo":    f"{HOME}/Descargas/GONVRA - flow/brazo-corregido.mp4",
    "blade":    f"{HOME}/Descargas/videos para la tienda/Shaver_blade_texture_lighting_720p_202609062312.mp4",
    "rinse":    f"{HOME}/Descargas/Hand_rinsing_shaver_under_water_202609071535.mp4",
    "kit":      f"{HOME}/Descargas/videos para la tienda/Hand_picking_up_comb_guard_202609062254.mp4",
    "limpieza": f"{HOME}/Descargas/Hands_brushing_blade_and_pluggin…_202609071553.mp4",
    "rostro":   f"{HOME}/Descargas/gonvra-flow-nuevo/rostro-jawline-720p.mp4",
}

# correccion de color medida con signalstats; objetivo comun U=119 V=134
# (brillo en unidades ffmpeg eq, rm/bm en unidades colorbalance de medios)
GRADE = {
    "cajon":    dict(b=+0.033, rm=-0.070, bm=+0.094, sat=1.04, sharp=False),
    "cajon_360": dict(b=+0.057, rm=-0.047, bm=+0.034, sat=1.04, sharp=True),
    "mesada":   dict(b=-0.107, rm=-0.010, bm=+0.015, sat=1.05, sharp=False),
    "enjuague": dict(b=-0.108, rm=+0.013, bm=-0.013, sat=1.04, sharp=False),
    "cajon2":   dict(b=+0.057, rm=-0.047, bm=+0.034, sat=1.04, sharp=True),
    "brazo":    dict(b=-0.078, rm=-0.030, bm=+0.018, sat=1.08, sharp=False),
    "blade":    dict(b=+0.038, rm=+0.030, bm=-0.015, sat=1.05, sharp=False),
    "rinse":    dict(b=-0.050, rm=+0.034, bm=-0.045, sat=1.03, sharp=False),
    "kit":      dict(b=+0.007, rm=-0.008, bm=-0.005, sat=1.03, sharp=False),
    "limpieza": dict(b=+0.009, rm=-0.045, bm=+0.023, sat=1.03, sharp=False),
    # el mas calido de todos (V=148): correccion fuerte hacia el objetivo comun
    "rostro":   dict(b=+0.031, rm=-0.114, bm=+0.091, sat=1.04, sharp=False),
}

# ---------------------------------------------------------------- guion
# (fuente, desde, hasta, cartel|None)
ADS = {
    "TT-1-Cajon": [
        ("cajon",    0.30, 3.00, "t1_c1"),
        ("cajon",    3.00, 4.80, "t1_c2"),
        ("mesada",   0.40, 2.40, "t1_c3"),   # revelado
        ("rostro",   1.20, 3.40, "t1_c3"),   # rostro
        ("brazo",    1.20, 3.20, "t1_c3"),   # cuerpo
        ("enjuague", 1.50, 3.70, "t1_c4"),
        ("kit",      0.60, 1.80, None),
    ],
    "TT-2-Lamina": [
        ("brazo",    0.20, 3.40, "t2_c1"),
        ("brazo",    3.40, 6.20, "t2_c2"),
        ("blade",    1.80, 6.20, "t2_c3"),
        ("enjuague", 1.20, 4.40, "t2_c4"),
    ],
    "TT-3-Que-Trae": [
        ("kit",      0.00, 3.20, "t3_c1"),
        ("kit",      3.20, 6.00, "t3_c2"),
        ("limpieza", 0.20, 3.40, "t3_c3"),   # cepillo
        ("limpieza", 4.60, 8.20, "t3_c4"),   # cable USB
    ],
}
ENDCARD = 2.20   # segundos de cierre de marca


def run(cmd):
    r = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if r.returncode:
        print("FALLO:", cmd[:300]); print(r.stderr[-1800:]); raise SystemExit(1)
    return r


def vf_for(key):
    g = GRADE[key]
    f = (f"scale={W}:{H}:force_original_aspect_ratio=increase:flags=lanczos,"
         f"crop={W}:{H},fps={FPS}")
    if g["sharp"]:
        f += ",unsharp=5:5:0.65:3:3:0.3"
    f += (f",eq=brightness={g['b']:.3f}:saturation={g['sat']:.2f}:gamma=1.02"
          f",colorbalance=rm={g['rm']:.3f}:bm={g['bm']:.3f}"
          f",format=yuv420p")
    return f


def build_segment(ad, i, key, t0, t1, card, fade_in=True, fade_out=True):
    """Genera un segmento corregido, con cartel animado y audio nivelado."""
    dur = round(t1 - t0, 3)
    out = f"{REC}/{ad}_{i:02d}.mp4"
    src = SRC[key]

    # animacion del cartel: entra con fade 0.28s, sale 0.22s antes del final
    if card:
        # entrada: fade de alfa 0.28s + leve subida de 14 px; salida: fade 0.22s
        # si hay cartel a ambos lados del corte, el texto cambia en seco:
        # un fundido dejaria un hueco sin texto dentro de una toma continua
        fin, fout = 0.16, 0.10
        st_out = max(0.0, dur - fout)
        fades = ""
        if fade_in:
            fades += f"fade=t=in:st=0:d={fin}:alpha=1,"
        if fade_out:
            fades += f"fade=t=out:st={st_out:.3f}:d={fout}:alpha=1,"
        filt = (f"[0:v]{vf_for(key)}[v];"
                f"[1:v]scale={W}:{H},format=rgba,"
                f"{fades}null[c];"
                f"[v][c]overlay=x=0:y='if(lt(t,{fin}),14*(1-t/{fin}),0)'"
                f":format=auto[vo]")
        cmd = (f'ffmpeg -y -v error -ss {t0} -t {dur} -i {shlex.quote(src)} '
               f'-loop 1 -t {dur} -i {shlex.quote(f"{CAR}/{card}.png")} '
               f'-f lavfi -t {dur} -i anullsrc=channel_layout=stereo:sample_rate=48000 '
               f'-filter_complex {shlex.quote(filt)} -map "[vo]" -map 2:a '
               f'-c:v libx264 -preset medium -crf 17 -pix_fmt yuv420p '
               f'-c:a aac -b:a 192k -ar 48000 -ac 2 -shortest {shlex.quote(out)}')
    else:
        cmd = (f'ffmpeg -y -v error -ss {t0} -t {dur} -i {shlex.quote(src)} '
               f'-f lavfi -t {dur} -i anullsrc=channel_layout=stereo:sample_rate=48000 '
               f'-vf {shlex.quote(vf_for(key))} -map 0:v -map 1:a '
               f'-c:v libx264 -preset medium -crf 17 -pix_fmt yuv420p '
               f'-c:a aac -b:a 192k -ar 48000 -ac 2 -shortest {shlex.quote(out)}')
    run(cmd)
    return out, dur


def build_endcard(ad):
    out = f"{REC}/{ad}_99_end.mp4"
    cmd = (f'ffmpeg -y -v error -loop 1 -t {ENDCARD} -i {shlex.quote(f"{CAR}/endcard.png")} '
           f'-f lavfi -t {ENDCARD} -i anullsrc=channel_layout=stereo:sample_rate=48000 '
           f'-vf "scale={W}:{H},fps={FPS},fade=t=in:st=0:d=0.30,format=yuv420p" '
           f'-c:v libx264 -preset medium -crf 17 -pix_fmt yuv420p '
           f'-c:a aac -b:a 192k -ar 48000 -ac 2 -shortest {shlex.quote(out)}')
    run(cmd)
    return out, ENDCARD


def build_ad(ad):
    print(f"\n=== {ad} ===")
    segs, t = [], 0.0
    plan = ADS[ad]
    for i, (key, t0, t1, card) in enumerate(plan):
        prev_card = plan[i - 1][3] if i > 0 else None
        next_card = plan[i + 1][3] if i + 1 < len(plan) else None
        p, d = build_segment(ad, i, key, t0, t1, card,
                             fade_in=(prev_card is None),
                             fade_out=(next_card is None))
        print(f"  {t:6.2f}  {key:9} {t0:5.2f}-{t1:5.2f}  {d:4.2f}s  {card or '—'}")
        segs.append(p); t += d
    p, d = build_endcard(ad)
    print(f"  {t:6.2f}  endcard              {d:4.2f}s  gonvra.com")
    segs.append(p); t += d

    lst = f"{REC}/{ad}_lista.txt"
    with open(lst, "w") as f:
        for s in segs:
            f.write(f"file '{s}'\n")
    out = f"{OUT}/{ad}.mp4"
    run(f'ffmpeg -y -v error -f concat -safe 0 -i {shlex.quote(lst)} '
        f'-c:v libx264 -preset slow -crf 18 -pix_fmt yuv420p '
        f'-c:a aac -b:a 192k -ar 48000 -ac 2 -movflags +faststart {shlex.quote(out)}')
    print(f"  -> {out}  total {t:.2f}s")
    return out, t


if __name__ == "__main__":
    os.makedirs(REC, exist_ok=True); os.makedirs(OUT, exist_ok=True)
    res = {}
    for ad in ADS:
        res[ad] = build_ad(ad)
    print("\n=== LISTO ===")
    for k, (p, t) in res.items():
        print(f"{k:16} {t:5.2f}s  {p}")
