---
tool: ClaudeCode
session_id: 2c3e09f5-b686-4ad4-b63e-28d12e063c95
fecha: 2026-09-12 16:32
titulo: "tengo instalado nodejs"
tags: [chat, agente, claudecode]
---

# 💬 tengo instalado nodejs
> **ClaudeCode** · 2026-09-12 16:32 · `2c3e09f5-b686-4ad4-b63e-28d12e063c95`

---

### 🧑 Vos  <small>2026-09-12 16:32</small>

tengo instalado node.js?

### 🤖 Claude  <small>2026-09-12 16:32</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-09-12 16:32</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-12 16:32</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-09-12 16:32</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-12 16:32</small>

Sí, tenés Node.js instalado.

| | Versión | Ruta |
|---|---|---|
| node | **v22.23.2** | `~/.local/bin/node` → `~/.hermes/node/bin/node` |
| npm | **10.9.8** | `~/.local/bin/npm` → `~/.hermes/node/bin/npm` |

Dos detalles:

- El Node activo **no** es un install del sistema: son symlinks en `~/.local/bin` que apuntan a la copia que instaló **Hermes** (`~/.hermes/node`). Si algún día borrás esa carpeta, `node` deja de funcionar.
- También tenés **nvm** instalado (`~/.nvm`), así que podrías tener otras versiones ahí. Para verlas:

```bash
bash -lc 'source ~/.nvm/nvm.sh && nvm ls'
```
