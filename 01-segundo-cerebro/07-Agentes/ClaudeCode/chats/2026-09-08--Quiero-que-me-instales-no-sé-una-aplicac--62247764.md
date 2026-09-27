---
tool: ClaudeCode
session_id: 62247764-c238-48e4-bdd3-5c0f804c75ff
fecha: 2026-09-08 19:33
titulo: "Quiero que me instales no sé una aplicación no sé"
tags: [chat, agente, claudecode]
---

# 💬 Quiero que me instales no sé una aplicación no sé
> **ClaudeCode** · 2026-09-08 19:33 · `62247764-c238-48e4-bdd3-5c0f804c75ff`

---

### 🧑 Vos  <small>2026-09-08 19:33</small>

Quiero que me instales, no sé, una aplicación, no sé, para ver los videos, ver videos en en Linux, porque me dice, instala estos complementos, y no me deja instalarlo, no sé, porque instálame todos los complementos necesarios para ver videos en Linux. Gracias.

### 🤖 Claude  <small>2026-09-08 19:33</small>

Voy a ver qué distro tenés y qué reproductor hay instalado antes de tocar nada.

### 🤖 Claude  <small>2026-09-08 19:33</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-09-08 19:33</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-08 19:33</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-09-08 19:33</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-08 19:33</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-09-08 19:33</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-08 19:34</small>

## Qué pasa

Ya sé por qué te falla. Es un clásico de Fedora, no es que tu equipo esté roto:

- Tenés **Fedora 44 Workstation**.
- Los codecs de video (H.264, H.265, MPEG-4, etc.) están **patentados**, así que Fedora no los puede distribuir. Te instala `ffmpeg-free`, que es una versión recortada sin esos codecs.
- Cuando GNOME Videos te dice "instalá estos complementos", va a buscarlos... y **no encuentra el repositorio donde viven**. Por eso el botón no hace nada.
- Confirmado: **RPM Fusion no está instalado** (sólo tenés los sub-repos sueltos de NVIDIA y Steam, que vienen por defecto).

No puedo ejecutar los comandos yo porque `sudo` acá me pide contraseña y no tengo forma de escribirla. Te los dejo listos para copiar y pegar, en orden.

## Paso 1 — Habilitar RPM Fusion

```bash
sudo dnf install -y https://mirrors.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm https://mirrors.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm
```

## Paso 2 — Cambiar el ffmpeg recortado por el completo

```bash
sudo dnf swap ffmpeg-free ffmpeg --allowerasing
```

## Paso 3 — Instalar todos los codecs

```bash
sudo dnf install -y gstreamer1-plugins-{bad-\*,good-\*,base} gstreamer1-plugin-openh264 gstreamer1-libav lame\* libavcodec-freeworld --exclude=gstreamer1-plugins-bad-free-devel
```

## Paso 4 — Instalar VLC

```bash
sudo dnf install -y vlc
```

VLC trae sus propios codecs adentro, así que reproduce prácticamente cualquier cosa aunque algo de lo anterior falle. Es tu red de seguridad.

## Después

Reiniciá la sesión (o la máquina) para que GNOME tome los codecs nuevos. Ahí tanto **Videos** (el de GNOME) como **VLC** deberían abrir todo sin pedirte nada.

Un par de aclaraciones:

- El **paso 3 es largo** y va a bajar bastante. Es normal que tarde.
- Si el paso 1 te tira que RPM Fusion 44 todavía no existe, avisame y lo resolvemos por otro lado (Flatpak de VLC, que funciona sin tocar repos).
- Tenés **NVIDIA**. Con esto también te queda funcionando la aceleración por hardware para video, así que los videos pesados van a consumir menos CPU.

Cuando los corras, pegame la salida si algo falla y lo vemos.
