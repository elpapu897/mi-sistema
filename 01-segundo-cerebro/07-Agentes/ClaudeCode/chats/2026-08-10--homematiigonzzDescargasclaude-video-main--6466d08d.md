---
tool: ClaudeCode
session_id: 6466d08d-e9ba-46c5-93db-f8189346d06d
fecha: 2026-08-10 02:16
titulo: "homematiigonzzDescargasclaude video mainzip instal"
tags: [chat, agente, claudecode]
---

# 💬 homematiigonzzDescargasclaude video mainzip instal
> **ClaudeCode** · 2026-08-10 02:16 · `6466d08d-e9ba-46c5-93db-f8189346d06d`

---

### 🧑 Vos  <small>2026-08-10 02:16</small>

@"/home/matiigonzz/Descargas/claude-video-main.zip"
instala esta skill

### 🤖 Claude  <small>2026-08-10 02:16</small>

I'll take a look at the zip file first.

### 🤖 Claude  <small>2026-08-10 02:16</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-08-10 02:16</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-08-10 02:16</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-08-10 02:16</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-08-10 02:16</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-08-10 02:16</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-08-10 02:16</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-08-10 02:16</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-08-10 02:16</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-08-10 02:16</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-08-10 02:16</small>

El plugin ya quedó instalado (la app lo cargó desde el zip). Ahora completo el setup de dependencias.

### 🤖 Claude  <small>2026-08-10 02:16</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-08-10 02:16</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-08-10 02:16</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-08-10 02:16</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-08-10 02:16</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-08-10 02:16</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-08-10 02:16</small>

Ya está instalada y las dependencias (ffmpeg + yt-dlp) están presentes. Falta cerrar dos preferencias del primer arranque:

### 🤖 Claude  <small>2026-08-10 02:17</small>

_[usó herramienta: AskUserQuestion]_

### 🧑 Vos  <small>2026-08-10 02:20</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-08-10 02:20</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-08-10 02:20</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-08-10 02:20</small>

Listo. La skill **`/watch`** quedó instalada y operativa.

**Estado:**
- Plugin `watch@local-desktop-app-uploads` v0.2.0 instalado en `~/.claude/plugins/marketplaces/local-desktop-app-uploads/watch`
- `ffmpeg` ✅ (`/usr/bin/ffmpeg`) y `yt-dlp` ✅ (`~/.local/bin/yt-dlp`) — ya los tenías
- Config creada en `~/.config/watch/.env` con permisos `600`
- `WATCH_DETAIL=balanced` (frames por escena, máx 100) y `SETUP_COMPLETE=true`
- Falta solo tu key de Groq

**Para cargar tu Groq key** (así no la pegás en el chat, corré esto y reemplazá `gsk_tu_key_aca`):

```bash
sed -i 's|^GROQ_API_KEY=.*|GROQ_API_KEY=gsk_tu_key_aca|' ~/.config/watch/.env && chmod 600 ~/.config/watch/.env && grep -c '^GROQ_API_KEY=gsk' ~/.config/watch/.env
```

Si devuelve `1`, quedó bien.

**Cómo se usa:**

```bash
/watch https://youtu.be/VIDEO_ID de qué habla el video
```

También funciona con archivos locales (`/watch ~/Videos/clip.mp4 ¿qué pasa al final?`). Descarga con yt-dlp, extrae frames con ffmpeg, saca la transcripción de los subtítulos nativos (y si no hay, cae a Whisper vía Groq una vez que cargues la key) y yo leo los frames para responderte.

Un detalle: rinde mejor con videos de menos de 10 minutos — arriba de eso el muestreo de frames se vuelve muy espaciado. Si tenés uno largo, conviene que me digas qué tramo te interesa.

### 🧑 Vos  <small>2026-08-10 02:21</small>

xai-YCYl5rgiDFYx7BGtnVv7LYBbyGcGBRHS4UdH1WEAj0y3yVWy1esrCPrvncbupUF7cDHFLEv9zbnKjDhm

### 🤖 Claude  <small>2026-08-10 02:21</small>

Pará un segundo antes de guardarlo: esa key es de **xAI** (`xai-...`), no de Groq. Son servicios distintos que se confunden fácil por el nombre. Dejame verificar qué acepta el script.

### 🤖 Claude  <small>2026-08-10 02:21</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-08-10 02:21</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-08-10 02:21</small>

No la guardé. Dos cosas:

**1. Esa key no sirve para `/watch`.** El script tiene los endpoints hardcodeados y solo soporta dos:
- `https://api.groq.com/openai/v1/audio/transcriptions` → `GROQ_API_KEY`
- `https://api.openai.com/v1/audio/transcriptions` → `OPENAI_API_KEY`

Una key de xAI (Grok) no autentica contra ninguno de los dos, y además xAI no expone un endpoint de transcripción de audio tipo Whisper. Aunque la pegara en el archivo, la transcripción fallaría con un 401 y volverías a quedar solo con frames.

**2. Rotá esa key.** La pegaste en el chat, así que consideralá comprometida. Andá a [console.x.ai](https://console.x.ai) → API Keys, borrá esa y generá una nueva. Es un trámite de 30 segundos y te evita que alguien te queme créditos.

**Para lo que sí necesitás:** una key de Groq en [console.groq.com/keys](https://console.groq.com/keys). Tiene tier gratuito y las keys arrancan con `gsk_`. Cuando la tengas, corré esto reemplazando el placeholder (no hace falta que me la pegues):

```bash
sed -i 's|^GROQ_API_KEY=.*|GROQ_API_KEY=gsk_TU_KEY|' ~/.config/watch/.env && chmod 600 ~/.config/watch/.env && grep -c '^GROQ_API_KEY=gsk' ~/.config/watch/.env
```

Mientras tanto `/watch` ya funciona igual para cualquier video con subtítulos nativos — que en YouTube es la enorme mayoría. La key de Groq solo entra en juego como fallback cuando no hay subtítulos (videos de X, TikTok, archivos locales sin pista de subtítulos).

### 🧑 Vos  <small>2026-08-10 02:24</small>

esa es la aplicación que me dio creo, esa es la API que me dio Grok. Grok, API, es la API Key. Es la que me dio boludo, qué gracias.

### 🤖 Claude  <small>2026-08-10 02:24</small>

Te creo — no estoy diciendo que la key sea trucha ni inventada. Es una key real que te dio Grok. El problema es otro y es una trampa de nombres genuinamente cruel:

- **Grok** = xAI, el chatbot de Musk. Es la tuya (`xai-...`).
- **Groq** = otra empresa, hace chips de inferencia. Su key arranca con `gsk_`.

Se escriben igual salvo una letra y no tienen nada que ver entre sí. Dejame probarlo en vez de discutirlo:

### 🤖 Claude  <small>2026-08-10 02:24</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-08-10 02:24</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-08-10 02:24</small>

Ahí está, en blanco sobre negro:

- **xAI la reconoce** (HTTP 403, no 401): la key es tuya y es válida. Pero tu equipo se quedó sin créditos / llegó al límite mensual de gasto.
- **Groq la rechaza** (HTTP 401 `invalid_api_key`): no la conoce, porque es otra empresa.

Así que no es que yo no quiera usarla — es que hay dos paredes, no una. Aunque xAI tuviera endpoint de transcripción (no lo tiene, solo chat e imágenes), la cuenta está sin créditos igual.

Lo bueno: **Groq es gratis para esto.** Andá a [console.groq.com/keys](https://console.groq.com/keys), entrás con Google, creás la key y listo — el tier gratuito cubre `whisper-large-v3` de sobra para mirar videos. Te va a salir algo tipo `gsk_...`:

```bash
sed -i 's|^GROQ_API_KEY=.*|GROQ_API_KEY=gsk_TU_KEY|' ~/.config/watch/.env && chmod 600 ~/.config/watch/.env && grep -c '^GROQ_API_KEY=gsk' ~/.config/watch/.env
```

Y rotá igual la de xAI cuando puedas, que quedó escrita en el chat.

Igual, no te bloquea nada ahora mismo: tirame un link de YouTube y `/watch` lo procesa con los subtítulos nativos, sin necesidad de ninguna key. La de Groq es solo para videos que no tienen subtítulos.
