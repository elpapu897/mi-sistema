---
tool: Codex
session_id: 01a083d2-11a3-7811-9192-60c436406cf3
fecha: 2026-09-09 01:39
titulo: "Quiero que me instales no sé una aplicación no sé"
tags: [chat, agente, codex]
---

# 💬 Quiero que me instales no sé una aplicación no sé
> **Codex** · 2026-09-09 01:39 · `01a083d2-11a3-7811-9192-60c436406cf3`

---

### 🧑 Vos  <small>2026-09-09 01:39</small>

Quiero que me instales, no sé, una aplicación, no sé, para ver los videos, ver videos en en Linux, porque me dice, instala estos complementos, y no me deja instalarlo, no sé, porque instálame todos los complementos necesarios para ver videos en Linux. Gracias.

### 🤖 Codex  <small>2026-09-09 01:39</small>

Voy a ver qué distro tenés y qué reproductor hay instalado antes de tocar nada.

### 🤖 Codex  <small>2026-09-09 01:39</small>

[external_agent_tool_call: Bash]
description: Detect distro and installed video players
command: cat /etc/os-release; echo "---"; which vlc mpv totem ffmpeg 2>/dev/null; echo "---"; dpkg -l 2>/dev/null | grep -E "ubuntu-restricted|libavcodec|gstreamer1.0-libav|vlc " | head -20
[/external_agent_tool_call]

### 🤖 Codex  <small>2026-09-09 01:39</small>

[external_agent_tool_result]
NAME="Fedora Linux"
VERSION="44 (Workstation Edition)"
RELEASE_TYPE=stable
ID=fedora
VERSION_ID=44
VERSION_CODENAME=""
PRETTY_NAME="Fedora Linux 44 (Workstation Edition)"
ANSI_COLOR="0;38;2;60;110;180"
LOGO=fedora-logo-icon
CPE_NAME="cpe:/o:fedoraproject:fedora:44"
DEFAULT_HOSTNAME="fedora"
HOME_URL="https://fedoraproject.org/"
DOCUMENTATION_URL="https://docs.fedoraproject.org/en-US/fedora/f44/"
SUPPORT_URL="https://ask.fedoraproject.org/"
BUG_REPORT_URL="https://bugzilla.redhat.com/"
REDHAT_BUGZILLA_PRODUCT="Fedora"
REDHAT_BUGZILLA_PRODUCT_VERSION=44
REDHAT_SUPPORT_PRODUCT="Fedora"
REDHAT_SUPPORT_PRODUCT_VERSION=44
SUPPORT_END=2027-05-19
VARIANT="Workstation Edition"
VARIANT_ID=workstation
---
/usr/bin/ffmpeg
---
[/external_agent_tool_result]

### 🤖 Codex  <small>2026-09-09 01:39</small>

[external_agent_tool_call: Bash]
description: Check codec packages, repos and sudo access
command: rpm -q ffmpeg-free ffmpeg libavcodec-free libavcodec-freeworld 2>&1; echo "--- repos ---"; dnf repolist 2>/dev/null | grep -i -E "rpmfusion|fedora|updates"; echo "--- sudo ---"; sudo -n true 2>&1 && echo "SUDO_SIN_PASS" || echo "SUDO_PIDE_PASS"
[/external_agent_tool_call]

### 🤖 Codex  <small>2026-09-09 01:39</small>

[external_agent_tool_result]
ffmpeg-free-8.0.1-6.fc44.x86_64
el paquete ffmpeg no está instalado
libavcodec-free-8.0.1-6.fc44.x86_64
el paquete libavcodec-freeworld no está instalado
--- repos ---
claude-desktop                                 Claude Desktop for Fedora/RHEL
copr:copr.fedorainfracloud.org:phracek:PyCharm Copr repo for PyCharm owned by phracek
fedora                                         Fedora 44 - x86_64
fedora-cisco-openh264                          Fedora 44 openh264 (From Cisco) - x86_64
rpmfusion-nonfree-nvidia-driver                RPM Fusion for Fedora 44 - Nonfree - NVIDIA Driver
rpmfusion-nonfree-steam                        RPM Fusion for Fedora 44 - Nonfree - Steam
updates                                        Fedora 44 - x86_64 - Updates
--- sudo ---
sudo: a password is required
SUDO_PIDE_PASS
[/external_agent_tool_result]

### 🤖 Codex  <small>2026-09-09 01:39</small>

[external_agent_tool_call: Bash]
description: Check RPM Fusion release packages and disabled repos
command: rpm -q rpmfusion-free-release rpmfusion-nonfree-release 2>&1; echo "--- todos los repos rpmfusion (incl. deshabilitados) ---"; dnf repolist --all 2>/dev/null | grep -i rpmfusion
[/external_agent_tool_call]

### 🤖 Codex  <small>2026-09-09 01:39</small>

[external_agent_tool_result]
el paquete rpmfusion-free-release no está instalado
el paquete rpmfusion-nonfree-release no está instalado
--- todos los repos rpmfusion (incl. deshabilitados) ---
rpmfusion-nonfree-nvidia-driver                RPM Fusion for Fedora 44 - Nonfree - NVIDIA Driver         enabled
rpmfusion-nonfree-nvidia-driver-debuginfo      RPM Fusion for Fedora 44 - Nonfree - NVIDIA Driver Debug  disabled
rpmfusion-nonfree-nvidia-driver-source         RPM Fusion for Fedora 44 - Nonfree - NVIDIA Driver Source disabled
rpmfusion-nonfree-steam                        RPM Fusion for Fedora 44 - Nonfree - Steam                 enabled
rpmfusion-nonfree-steam-debuginfo              RPM Fusion for Fedora 44 - Nonfree - Steam Debug          disabled
rpmfusion-nonfree-steam-source                 RPM Fusion for Fedora 44 - Nonfree - Steam Source         disabled
[/external_agent_tool_result]

### 🤖 Codex  <small>2026-09-09 01:39</small>

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
