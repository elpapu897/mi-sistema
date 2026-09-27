---
tool: ClaudeCode
session_id: 6c4dabea-a898-4d89-a51f-0a05d31b69a9
fecha: 2026-09-07 04:09
titulo: "como veo los chats archivados"
tags: [chat, agente, claudecode]
---

# 💬 como veo los chats archivados
> **ClaudeCode** · 2026-09-07 04:09 · `6c4dabea-a898-4d89-a51f-0a05d31b69a9`

---

### 🧑 Vos  <small>2026-09-07 04:09</small>

como veo los chats archivados??

### 🤖 Claude  <small>2026-09-07 04:09</small>

_[usó herramienta: Bash]_

### 🤖 Claude  <small>2026-09-07 04:09</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-09-07 04:09</small>

_[resultado de herramienta]_

### 🧑 Vos  <small>2026-09-07 04:09</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-07 04:09</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-09-07 04:09</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-07 04:10</small>

Tenés dos formas, según qué "archivados" te refieras:

## 1. El archivo permanente en Obsidian (lo recomendado)

Todos los chats de Claude Code, Codex y Hermes se exportan solos cada 30 min a notas `.md`:

| Agente | Carpeta | Notas |
|---|---|---|
| Claude Code | `~/OBSIDIAN/07-Agentes/ClaudeCode/chats/` | 85 |
| Codex | `~/OBSIDIAN/07-Agentes/Codex/chats/` | 87 |
| Hermes | `~/OBSIDIAN/07-Agentes/Hermes/chats/` | 3 |

Los abrís directamente en Obsidian (vault `~/OBSIDIAN`, carpeta `07-Agentes`) y arrancás por [CHATS-INDICE.md](../OBSIDIAN/07-Agentes/CHATS-INDICE.md).

Desde la terminal, los más recientes:

```bash
ls -t ~/OBSIDIAN/07-Agentes/*/chats/ | head -20
```

Buscar por tema (ej. Shopify):

```bash
grep -ril "shopify" ~/OBSIDIAN/07-Agentes/*/chats/
```

Y si no querés esperar los 30 min del timer, forzás la exportación:

```bash
python3 ~/Claude/scripts/export-chats-to-obsidian.py
```

## 2. Retomar una sesión vieja de Claude Code

Desde una terminal (no acá, porque abre un panel interactivo):

```bash
claude --resume
```

Te lista las sesiones anteriores de este proyecto y podés continuar cualquiera.

Nota: en esta sesión web no puedo abrir los diálogos interactivos tipo `/resume`; si querés, te leo yo cualquier chat viejo — decime tema o fecha y lo busco.
