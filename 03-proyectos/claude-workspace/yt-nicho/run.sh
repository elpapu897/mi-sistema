#!/bin/bash
cd ~/Claude/yt-nicho
# esperar a que yt-dlp termine el mp3
while [ ! -f nicho.mp3 ]; do sleep 10; done
sleep 3
python3 - <<'PY'
from faster_whisper import WhisperModel
m = WhisperModel('small', device='cpu', compute_type='int8', cpu_threads=10)
segs, info = m.transcribe('nicho.mp3', language='es', beam_size=1,
                          vad_filter=True, condition_on_previous_text=False)
OFFSET = 830  # el corte empieza en 13:50 del video original
with open('transcript.txt', 'w', encoding='utf-8') as f:
    for s in segs:
        t = int(s.start) + OFFSET
        f.write(f"[{t//60:02d}:{t%60:02d}] {s.text.strip()}\n")
        f.flush()
print("TRANSCRIPCION LISTA")
PY
