---
tool: ClaudeCode
session_id: 7fca64d2-2895-4489-a4f6-f8973315bd0d
fecha: 2026-08-13 01:57
titulo: "npx  y skillslatest add remotion devskills  g  y i"
tags: [chat, agente, claudecode]
---

# 💬 npx  y skillslatest add remotion devskills  g  y i
> **ClaudeCode** · 2026-08-13 01:57 · `7fca64d2-2895-4489-a4f6-f8973315bd0d`

---

### 🧑 Vos  <small>2026-08-13 01:57</small>

npx -y skills@latest add remotion-dev/skills -g -y instala todas las skills  y tambien instala Node.js para usar remotion

### 🤖 Claude  <small>2026-08-13 01:57</small>

I'll help you install Node.js and the Remotion skills. Let me first check the current state of your system.

### 🤖 Claude  <small>2026-08-13 01:57</small>

_[usó herramienta: Bash]_

### 🤖 Claude  <small>2026-08-13 01:57</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-08-13 01:57</small>

_[resultado de herramienta]_

### 🧑 Vos  <small>2026-08-13 01:57</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-08-13 01:57</small>

Node.js v24.18.1 ya está instalado (vía nvm), así que no hace falta instalarlo. Ahora instalo las skills de Remotion:

### 🤖 Claude  <small>2026-08-13 01:57</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-08-13 01:58</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-08-13 01:58</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-08-13 01:58</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-08-13 01:58</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-08-13 01:58</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-08-13 01:58</small>

Todo listo. Verifico dependencias del sistema que Remotion necesita en Linux para renderizar:

### 🤖 Claude  <small>2026-08-13 01:58</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-08-13 01:58</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-08-13 01:58</small>

Instalación completada.

## Node.js
Ya estaba instalado — **v24.18.1** vía nvm (`~/.nvm/versions/node/v24.18.1/bin/node`). Es una versión moderna y totalmente compatible con Remotion (requiere ≥18), así que no hice ningún cambio.

## Skills de Remotion — 12 instaladas
Se instalaron globalmente en `~/.agents/skills/` y quedaron enlazadas (symlinks) en `~/.claude/skills/`:

| Skill | Para qué sirve |
|---|---|
| `remotion-create` | Crear proyectos nuevos |
| `remotion-best-practices` | Convenciones y patrones correctos |
| `remotion-docs` | Consultar documentación |
| `remotion-studio` | Trabajar con Remotion Studio |
| `remotion-render` | Renderizar videos |
| `remotion-captions` | Subtítulos y transcripciones |
| `remotion-multimedia` | Audio, video, imágenes |
| `remotion-markup` | Layout y estilos |
| `remotion-interactivity` | Players interactivos |
| `remotion-maps` | Animaciones con mapas |
| `remotion-saas` | Integración en apps SaaS |
| `remotion-upgrade` | Actualizar versiones |

Quedan disponibles también para Antigravity, Gemini CLI, GitHub Copilot, OpenCode y otros 12 agentes.

**Nota sobre los "Failed to install 12":** no es un problema real. Son los mismos 12 skills, pero para el agente *PromptScript*, que no soporta instalación global. Para Claude Code y el resto se instalaron correctamente.

## Dependencias del sistema
Verifiqué las 14 librerías que necesita Chrome Headless (el motor de renderizado de Remotion) en Fedora — **todas presentes**. Podés renderizar sin instalar nada más.

## Siguiente paso
Estás en el directorio vacío `edicion de videos`. Para arrancar un proyecto:

```bash
npx create-video@latest
```

Si preferís, decime qué tipo de video querés hacer y lo armo yo directamente usando las skills.
