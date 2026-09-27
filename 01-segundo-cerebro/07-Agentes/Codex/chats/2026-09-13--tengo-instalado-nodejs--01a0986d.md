---
tool: Codex
session_id: 01a0986d-980d-7443-88d3-8a76bff59642
fecha: 2026-09-13 01:41
titulo: "tengo instalado nodejs"
tags: [chat, agente, codex]
---

# 💬 tengo instalado nodejs
> **Codex** · 2026-09-13 01:41 · `01a0986d-980d-7443-88d3-8a76bff59642`

---

### 🧑 Vos  <small>2026-09-13 01:41</small>

tengo instalado node.js?

### 🤖 Codex  <small>2026-09-13 01:41</small>

[external_agent_tool_call: Bash]
description: Check Node.js and npm installation
command: which node npm 2>&1; echo "---"; node --version 2>&1; echo "---"; npm --version 2>&1
[/external_agent_tool_call]

### 🤖 Codex  <small>2026-09-13 01:41</small>

[external_agent_tool_result]
/home/matiigonzz/.local/bin/node
/home/matiigonzz/.local/bin/npm
---
v22.23.2
---
10.9.8
[/external_agent_tool_result]

### 🤖 Codex  <small>2026-09-13 01:41</small>

[external_agent_tool_call: Bash]
description: Inspect node binary origin
command: ls -la /home/matiigonzz/.local/bin/node /home/matiigonzz/.local/bin/npm 2>&1; echo "---nvm---"; ls -d /home/matiigonzz/.nvm 2>&1
[/external_agent_tool_call]

### 🤖 Codex  <small>2026-09-13 01:41</small>

[external_agent_tool_result]
lrwxrwxrwx. 1 matiigonzz matiigonzz 38 ago 14 21:05 /home/matiigonzz/.local/bin/node -> /home/matiigonzz/.hermes/node/bin/node
lrwxrwxrwx. 1 matiigonzz matiigonzz 37 ago 14 21:05 /home/matiigonzz/.local/bin/npm -> /home/matiigonzz/.hermes/node/bin/npm
---nvm---
/home/matiigonzz/.nvm
[/external_agent_tool_result]

### 🤖 Codex  <small>2026-09-13 01:41</small>

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
