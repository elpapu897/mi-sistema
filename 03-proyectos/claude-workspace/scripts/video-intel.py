#!/usr/bin/env python3
"""
video-intel.py — Espía de videos AHORRADOR DE TOKENS.

En vez de bajar y "mirar" un video entero (carísimo en tokens), saca solo lo que importa:
título, canal, vistas, likes, fecha, descripción, hashtags y la TRANSCRIPCIÓN en texto.
Sirve para YouTube, TikTok, Instagram Reels, y todo lo que soporte yt-dlp.

Uso:
    python3 video-intel.py <URL>                 # 1 video → ficha compacta
    python3 video-intel.py <URL> --json          # salida JSON
    python3 video-intel.py <URL_canal_o_hashtag> --scan 20   # escanea N videos SOLO metadata (baratísimo)

Salida por defecto: markdown compacto a stdout (para pegar/leer sin gastar tokens de más).
"""
import argparse, json, subprocess, sys, tempfile, os, glob, re

def run(cmd, timeout=120):
    return subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)

def num(n):
    try:
        n = int(n)
    except (TypeError, ValueError):
        return "?"
    for u, d in (("M", 1_000_000), ("K", 1_000)):
        if n >= d:
            return f"{n/d:.1f}{u}"
    return str(n)

def get_meta(url):
    r = run(["yt-dlp", "-J", "--no-warnings", "--skip-download", url], timeout=90)
    if r.returncode != 0:
        return None, r.stderr.strip()[:300]
    try:
        return json.loads(r.stdout), None
    except Exception as e:
        return None, str(e)

def get_transcript(url):
    """Baja subtítulos automáticos y los pasa a texto plano."""
    with tempfile.TemporaryDirectory() as td:
        run(["yt-dlp", "--skip-download", "--write-auto-subs", "--write-subs",
             "--sub-langs", "es,es-419,en", "--sub-format", "vtt",
             "-o", os.path.join(td, "sub"), "--no-warnings", url], timeout=120)
        vtts = glob.glob(os.path.join(td, "*.vtt"))
        if not vtts:
            return ""
        raw = open(vtts[0], encoding="utf-8", errors="ignore").read()
        # limpiar formato VTT → texto
        lines, seen = [], set()
        for ln in raw.splitlines():
            if "-->" in ln or ln.strip().isdigit() or ln.startswith("WEBVTT") or not ln.strip():
                continue
            ln = re.sub(r"<[^>]+>", "", ln).strip()
            if ln and ln not in seen:
                seen.add(ln)
                lines.append(ln)
        return " ".join(lines)

def ficha(d, transcript):
    tags = d.get("tags") or []
    hashtags = re.findall(r"#\w+", d.get("description", "") or "")
    out = [
        f"# 🎬 {d.get('title','(sin título)')}",
        f"- **Canal/autor:** {d.get('uploader','?')} ({num(d.get('channel_follower_count'))} seguidores)",
        f"- **Vistas:** {num(d.get('view_count'))} · **Likes:** {num(d.get('like_count'))} · "
        f"**Comentarios:** {num(d.get('comment_count'))}",
        f"- **Duración:** {d.get('duration','?')}s · **Fecha:** {d.get('upload_date','?')}",
        f"- **URL:** {d.get('webpage_url','')}",
    ]
    if hashtags:
        out.append(f"- **Hashtags:** {' '.join(hashtags[:15])}")
    if tags:
        out.append(f"- **Tags:** {', '.join(tags[:12])}")
    desc = (d.get("description") or "").strip()
    if desc:
        out += ["", "## Descripción", desc[:800]]
    if transcript:
        out += ["", "## Transcripción (lo que se dice en el video)", transcript[:4000]]
    else:
        out += ["", "_(Sin transcripción disponible — video sin subtítulos.)_"]
    return "\n".join(out)

def scan(url, n):
    r = run(["yt-dlp", "--flat-playlist", "--playlist-end", str(n),
             "--print", "%(view_count)s\t%(title)s\t%(webpage_url)s",
             "--no-warnings", url], timeout=120)
    if r.returncode != 0:
        return f"Error: {r.stderr.strip()[:200]}"
    rows = []
    for ln in r.stdout.splitlines():
        parts = ln.split("\t")
        if len(parts) >= 3:
            rows.append(parts)
    rows.sort(key=lambda x: int(x[0]) if x[0].isdigit() else 0, reverse=True)
    out = ["# 🔎 Escaneo (ordenado por vistas)", "", "| Vistas | Título | URL |", "|---:|---|---|"]
    for v, t, u in rows[:n]:
        out.append(f"| {num(v)} | {t[:60]} | {u} |")
    out.append("\n_Tip: pasá la URL del que más rinde a `video-intel.py <URL>` para ver su guion._")
    return "\n".join(out)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("url")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--scan", type=int, metavar="N", help="Escanear N videos (solo metadata, barato)")
    ap.add_argument("--no-transcript", action="store_true")
    a = ap.parse_args()

    if a.scan:
        print(scan(a.url, a.scan))
        return

    d, err = get_meta(a.url)
    if not d:
        print(f"No pude leer el video: {err}", file=sys.stderr)
        sys.exit(1)
    transcript = "" if a.no_transcript else get_transcript(a.url)

    if a.json:
        print(json.dumps({
            "title": d.get("title"), "uploader": d.get("uploader"),
            "views": d.get("view_count"), "likes": d.get("like_count"),
            "comments": d.get("comment_count"), "duration": d.get("duration"),
            "upload_date": d.get("upload_date"), "url": d.get("webpage_url"),
            "description": d.get("description"), "tags": d.get("tags"),
            "transcript": transcript,
        }, ensure_ascii=False, indent=2))
    else:
        print(ficha(d, transcript))

if __name__ == "__main__":
    main()
