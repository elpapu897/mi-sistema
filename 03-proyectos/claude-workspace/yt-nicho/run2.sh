#!/bin/bash
cd ~/Claude/yt-nicho
ffmpeg -v error -i nicho.wav -ss 850 -c copy parte2.wav -y
python3 - <<'PY'
from faster_whisper import WhisperModel
m = WhisperModel('small', device='cpu', compute_type='int8', cpu_threads=10)
segs, info = m.transcribe('parte2.wav', language='es', beam_size=1,
                          vad_filter=False, condition_on_previous_text=False)
OFFSET = 830 + 850
with open('transcript2.txt', 'w', encoding='utf-8') as f:
    for s in segs:
        t = int(s.start) + OFFSET
        f.write(f"[{t//60:02d}:{t%60:02d}] {s.text.strip()}\n")
        f.flush()
print("PARTE2 LISTA")
PY
