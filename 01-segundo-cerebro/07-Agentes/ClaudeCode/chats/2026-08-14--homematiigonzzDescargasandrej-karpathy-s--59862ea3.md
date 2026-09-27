---
tool: ClaudeCode
session_id: 59862ea3-0e31-46de-b3a1-5133be859146
fecha: 2026-08-14 23:56
titulo: "homematiigonzzDescargasandrej karpathy skills main"
tags: [chat, agente, claudecode]
---

# 💬 homematiigonzzDescargasandrej karpathy skills main
> **ClaudeCode** · 2026-08-14 23:56 · `59862ea3-0e31-46de-b3a1-5133be859146`

---

### 🧑 Vos  <small>2026-08-14 23:56</small>

@"/home/matiigonzz/Descargas/andrej-karpathy-skills-main.zip"
instala esta skill en todos los modelos de ia q tengo

### 🤖 Claude  <small>2026-08-14 23:56</small>

I'll take a look at the zip first.

### 🤖 Claude  <small>2026-08-14 23:56</small>

_[usó herramienta: Bash]_

### 🤖 Claude  <small>2026-08-14 23:56</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-08-14 23:56</small>

_[resultado de herramienta]_

### 🧑 Vos  <small>2026-08-14 23:56</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-08-14 23:56</small>

Ya tengo el flujo armado (skills canónicas + `sync-skills.sh`). Extraigo e instalo.

### 🤖 Claude  <small>2026-08-14 23:56</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-08-14 23:56</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-08-14 23:56</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-08-14 23:56</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-08-14 23:56</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-08-14 23:58</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-08-14 23:58</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-08-14 23:58</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-08-14 23:58</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-08-14 23:58</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-08-14 23:58</small>

Listo. **`karpathy-guidelines` instalada en los 47 agentes** que tenés configurados.

Qué hice:
1. Extraje el zip y copié `skills/karpathy-guidelines/` a tu carpeta canónica `~/.agents/skills/` (ahora 258 skills).
2. Corrí [sync-skills.sh](Claude/scripts/sync-skills.sh), que creó los symlinks en cada agente (Claude Code, Codex, Cursor-likes, Qwen, Grok, Trae, Roo, Kilocode, OpenHands, etc.).
3. Verifiqué que el enlace existe en todos: 47 OK, 0 rotos.

Notas:
- No instalé la regla de Cursor (`.cursor/rules/karpathy-guidelines.mdc`) porque no tenés `~/.cursor` — si instalás Cursor después, avisame y la agrego.
- El resto del repo (README, EXAMPLES.md, CLAUDE.md) es documentación; la skill en sí es solo el `SKILL.md`, que es lo que cargan los agentes.

La skill se auto-activa al escribir/revisar/refactorizar código: fuerza pensar antes de codear, mínimo código, cambios quirúrgicos y criterios de éxito verificables.
