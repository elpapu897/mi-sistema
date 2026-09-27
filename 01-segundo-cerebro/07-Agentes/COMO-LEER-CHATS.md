---
tags: [agentes, memoria, instrucciones]
---

# 🧠 Cómo leer los chats de los otros agentes

Todos los chats de **Claude Code, Codex y Hermes** se exportan automáticamente a este vault de
Obsidian como notas markdown legibles. Se actualiza **solo, cada 30 minutos**.

## Dónde están

| Agente | Carpeta |
|--------|---------|
| Claude Code | `~/OBSIDIAN/07-Agentes/ClaudeCode/chats/` |
| Codex | `~/OBSIDIAN/07-Agentes/Codex/chats/` |
| Hermes | `~/OBSIDIAN/07-Agentes/Hermes/chats/` |

Índice general: [[CHATS-INDICE]]

## Para cualquier agente (Claude Code, Codex, Hermes, OpenCode)

**Si el usuario te pide "leé el chat de Codex" / "fijate qué hablamos con Hermes" / "qué dijimos
antes", buscá en esas carpetas.** Son archivos `.md` normales: podés leerlos con tus herramientas
de archivos (grep, read, etc.). El nombre de cada archivo es `FECHA--titulo--id.md`, así que podés
filtrar por fecha o por tema.

Ejemplos:
- Buscar por tema: `grep -ril "shopify" ~/OBSIDIAN/07-Agentes/*/chats/`
- Ver los más recientes: `ls -t ~/OBSIDIAN/07-Agentes/Codex/chats/ | head`

## Cómo se actualiza

- Script: `~/Claude/scripts/export-chats-to-obsidian.py`
- Automático: temporizador de systemd `export-chats.timer` (cada 30 min).
- A mano: `python3 ~/Claude/scripts/export-chats-to-obsidian.py`

← Volver a [[README]]
