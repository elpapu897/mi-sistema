#!/bin/bash
OUT=~/Claude/gonvra-edits/inventario/inventario.csv
echo "ruta,nombre,dur_s,ancho,alto,fps,codec_v,codec_a,audio,bitrate_kbps,tam_mb" > "$OUT"
find ~/Descargas ~/Claude/gonvra-brand/clips-utiles ~/Claude/gonvra-ads/out \
  -maxdepth 2 -type f \( -iname "*.mp4" -o -iname "*.mov" -o -iname "*.webm" -o -iname "*.mkv" -o -iname "*.m4v" \) 2>/dev/null \
| sort | while IFS= read -r f; do
  j=$(ffprobe -v quiet -print_format json -show_format -show_streams "$f" 2>/dev/null)
  [ -z "$j" ] && { echo "\"$f\",\"$(basename "$f")\",ERROR,,,,,,,," >> "$OUT"; continue; }
  python3 - "$f" <<'PY' >> "$OUT"
import json,subprocess,sys,os
f=sys.argv[1]
j=json.loads(subprocess.run(["ffprobe","-v","quiet","-print_format","json","-show_format","-show_streams",f],capture_output=True,text=True).stdout)
v=next((s for s in j["streams"] if s["codec_type"]=="video"),None)
a=next((s for s in j["streams"] if s["codec_type"]=="audio"),None)
def fps(s):
    try:
        n,d=s.get("r_frame_rate","0/1").split("/"); return round(int(n)/int(d),3)
    except: return ""
dur=float(j["format"].get("duration",0) or 0)
br=int(j["format"].get("bit_rate",0) or 0)//1000
sz=round(os.path.getsize(f)/1048576,2)
print(f'"{f}","{os.path.basename(f)}",{dur:.2f},{v["width"] if v else ""},{v["height"] if v else ""},{fps(v) if v else ""},{v["codec_name"] if v else ""},{a["codec_name"] if a else ""},{"si" if a else "NO"},{br},{sz}')
PY
done
wc -l "$OUT"
