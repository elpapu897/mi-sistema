---
tool: Codex
session_id: 01a083d2-11a5-7ab2-99e5-21237f26cc99
fecha: 2026-09-09 01:39
titulo: "descarga local send en mi pc"
tags: [chat, agente, codex]
---

# 💬 descarga local send en mi pc
> **Codex** · 2026-09-09 01:39 · `01a083d2-11a5-7ab2-99e5-21237f26cc99`

---

### 🧑 Vos  <small>2026-09-09 01:39</small>

descarga local send en mi pc

### 🤖 Codex  <small>2026-09-09 01:39</small>

[external_agent_tool_call: Bash]
description: Detect OS and package managers
command: cat /etc/os-release | head -5; echo "---"; which flatpak snap apt dnf pacman 2>/dev/null; echo "---"; uname -m
[/external_agent_tool_call]

### 🤖 Codex  <small>2026-09-09 01:39</small>

[external_agent_tool_result]
NAME="Fedora Linux"
VERSION="44 (Workstation Edition)"
RELEASE_TYPE=stable
ID=fedora
VERSION_ID=44
---
/usr/bin/flatpak
/usr/bin/dnf
/usr/bin/pacman
---
x86_64
[/external_agent_tool_result]

### 🤖 Codex  <small>2026-09-09 01:39</small>

Fedora 44 detectado. Instalo LocalSend vía Flatpak (Flathub) para tu usuario:

### 🤖 Codex  <small>2026-09-09 01:39</small>

[external_agent_tool_call: Bash]
description: Check flatpak remotes
command: flatpak remotes --user; echo "---"; flatpak remotes
[/external_agent_tool_call]

### 🤖 Codex  <small>2026-09-09 01:39</small>

[external_agent_tool_result]
flathub
---
fedora	system,oci
flathub	system
trinity	system
flathub	user
[/external_agent_tool_result]

### 🤖 Codex  <small>2026-09-09 01:39</small>

[external_agent_tool_call: Bash]
description: Install LocalSend from Flathub
command: flatpak install --user -y flathub org.localsend.localsend_app 2>&1 | tail -30
[/external_agent_tool_call]

### 🤖 Codex  <small>2026-09-09 01:39</small>

[external_agent_tool_result]
    dri	file access [1]	dbus access [2]	system dbus access [3]

    [1] xdg-download
    [2] org.kde.StatusNotifierWatcher
    [3] org.freedesktop.NetworkManager, org.freedesktop.hostname1


 1.	   	org.localsend.localsend_app	stable	i	flathub	< 23,1 MB


Instalando…
Instalando…                        0%  0 bytes/s
Instalando… █▊                     9%
Instalando… ██▌                   13%
Instalando… ███▌                  18%
Instalando… ████▊                 24%  4,0 MB/s
Instalando… ██████▏               31%  5,6 MB/s
Instalando… ███████▍              37%  7,2 MB/s
Instalando… ████████▌             43%  4,3 MB/s
Instalando… ██████████▏           51%  5,3 MB/s
Instalando… ███████████▍          57%  6,0 MB/s
Instalando… ████████████▍         62%  4,4 MB/s
Instalando… █████████████▌        68%  4,9 MB/s
Instalando… ███████████████       75%  5,5 MB/s
Instalando… ████████████████▏     81%  4,5 MB/s  00:00
Instalando… █████████████████▌    88%  4,9 MB/s  00:00
Instalando… ███████████████████   95%  5,3 MB/s  00:00
Instalando… ████████████████████ 100%  5,6 MB/s  00:00
Instalando… ████████████████████ 100%  5,6 MB/s  00:00
Instalación completada.
[/external_agent_tool_result]

### 🤖 Codex  <small>2026-09-09 01:39</small>

[external_agent_tool_call: Bash]
description: Verify LocalSend install
command: flatpak info --user org.localsend.localsend_app 2>&1 | head -8
[/external_agent_tool_call]

### 🤖 Codex  <small>2026-09-09 01:39</small>

[external_agent_tool_result]
LocalSend - Share files to nearby devices

                 ID: org.localsend.localsend_app
         Referencia: app/org.localsend.localsend_app/x86_64/stable
       Arquitectura: x86_64
               Rama: stable
            Versión: 1.18.2
[/external_agent_tool_result]

### 🤖 Codex  <small>2026-09-09 01:39</small>

LocalSend 1.18.2 instalado (Flatpak, user).

Lo abrís desde el menú de apps ("LocalSend") o desde terminal:

```bash
flatpak run org.localsend.localsend_app
```

Dos cosas a tener en cuenta:

1. **Firewall** — Fedora bloquea por defecto los puertos que usa LocalSend. Para que otros dispositivos te vean, abrí el puerto 53317 (TCP y UDP):

```bash
sudo firewall-cmd --permanent --add-port=53317/tcp --add-port=53317/udp && sudo firewall-cmd --reload
```

2. **Acceso a archivos** — el sandbox solo tiene permiso sobre `~/Descargas`. Si querés enviar/guardar en otras carpetas:

```bash
flatpak override --user --filesystem=home org.localsend.localsend_app
```
