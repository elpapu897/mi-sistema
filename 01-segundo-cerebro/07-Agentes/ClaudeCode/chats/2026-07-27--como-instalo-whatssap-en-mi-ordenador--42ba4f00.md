---
tool: ClaudeCode
session_id: 42ba4f00-6d86-41e8-a4a4-e4a017686605
fecha: 2026-07-27 01:37
titulo: "como instalo whatssap en mi ordenador"
tags: [chat, agente, claudecode]
---

# 💬 como instalo whatssap en mi ordenador
> **ClaudeCode** · 2026-07-27 01:37 · `42ba4f00-6d86-41e8-a4a4-e4a017686605`

---

### 🧑 Vos  <small>2026-07-27 01:37</small>

como instalo whatssap en mi ordenador

### 🤖 Claude  <small>2026-07-27 01:38</small>

WhatsApp **no tiene una app oficial para Linux**, pero en tu Fedora tienes varias formas de usarlo en el ordenador. Te las ordeno de más fácil a más completa:

## Opción 1 — WhatsApp Web (la más rápida, sin instalar nada)
1. Abre tu navegador y entra en 👉 [web.whatsapp.com](https://web.whatsapp.com)
2. En el móvil abre WhatsApp → **Ajustes** → **Dispositivos vinculados** → **Vincular un dispositivo**
3. Escanea el código QR que aparece en la pantalla del ordenador.

Puedes crear un acceso directo tipo "app" desde el navegador (en Chrome/Chromium: menú ⋮ → *Guardar y compartir* → *Instalar página como aplicación*).

## Opción 2 — Instalar una app de escritorio (recomendada para Fedora)
La forma más limpia en Fedora es con **Flatpak**, que ya viene configurado en tu sistema. Hay una app de WhatsApp muy buena y ligera llamada **ZapZap**:

```bash
flatpak install flathub com.rtosta.zapzap
```

Luego la abres desde el menú de aplicaciones como cualquier programa. Internamente usa WhatsApp Web, así que también tendrás que escanear el QR la primera vez.

Otra alternativa popular es **Whatsie**:

```bash
flatpak install flathub com.ktechpit.whatsie
```

---

**Mi recomendación:** si solo quieres probar, usa la **Opción 1** (WhatsApp Web). Si lo vas a usar a diario y quieres notificaciones de escritorio integradas, instala **ZapZap** con la Opción 2.

¿Quieres que te ayude a ejecutar el comando de instalación o prefieres la versión web?
