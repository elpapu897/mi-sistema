---
tool: ClaudeCode
session_id: 477257f8-c551-4110-8079-292cae13cdaa
fecha: 2026-09-09 00:06
titulo: "descarga local send en mi pc"
tags: [chat, agente, claudecode]
---

# 💬 descarga local send en mi pc
> **ClaudeCode** · 2026-09-09 00:06 · `477257f8-c551-4110-8079-292cae13cdaa`

---

### 🧑 Vos  <small>2026-09-09 00:06</small>

descarga local send en mi pc

### 🤖 Claude  <small>2026-09-09 00:06</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-09-09 00:07</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-09 00:07</small>

Fedora 44 detectado. Instalo LocalSend vía Flatpak (Flathub) para tu usuario:

### 🤖 Claude  <small>2026-09-09 00:07</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-09-09 00:07</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-09 00:07</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-09-09 00:07</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-09 00:07</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-09-09 00:07</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-09 00:07</small>

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
