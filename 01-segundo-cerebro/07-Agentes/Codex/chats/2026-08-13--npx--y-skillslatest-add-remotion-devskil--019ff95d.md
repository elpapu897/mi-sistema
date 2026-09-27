---
tool: Codex
session_id: 019ff95d-4eb3-7231-994a-47bbd339f150
fecha: 2026-08-13 04:24
titulo: "npx  y skillslatest add remotion devskills  g  y i"
tags: [chat, agente, codex]
---

# 💬 npx  y skillslatest add remotion devskills  g  y i
> **Codex** · 2026-08-13 04:24 · `019ff95d-4eb3-7231-994a-47bbd339f150`

---

### 🧑 Vos  <small>2026-08-13 04:24</small>

npx -y skills@latest add remotion-dev/skills -g -y instala todas las skills  y tambien instala Node.js para usar remotion

### 🤖 Codex  <small>2026-08-13 04:24</small>

I'll help you install Node.js and the Remotion skills. Let me first check the current state of your system.

### 🤖 Codex  <small>2026-08-13 04:24</small>

[external_agent_tool_call: Bash]
description: Check Node.js installation status
command: which node npm npx 2>&1; echo "---"; node --version 2>&1; echo "---"; uname -a
[/external_agent_tool_call]

### 🤖 Codex  <small>2026-08-13 04:24</small>

[external_agent_tool_call: Bash]
description: Check working directory
command: pwd; echo "---"; ls -la
[/external_agent_tool_call]

### 🤖 Codex  <small>2026-08-13 04:24</small>

[external_agent_tool_result]
/home/matiigonzz/edicion de videos
---
total 0
drwxr-xr-x. 1 matiigonzz matiigonzz    0 ago 12 22:55 .
drwx------. 1 matiigonzz matiigonzz 1110 ago 12 22:57 ..
[/external_agent_tool_result]

### 🤖 Codex  <small>2026-08-13 04:24</small>

[external_agent_tool_result]
/home/matiigonzz/.nvm/versions/node/v24.18.1/bin/node
/home/matiigonzz/.nvm/versions/node/v24.18.1/bin/npm
/home/matiigonzz/.nvm/versions/node/v24.18.1/bin/npx
---
v24.18.1
---
Linux fedora 6.19.10-300.fc44.x86_64 #1 SMP PREEMPT_DYNAMIC Wed Mar 25 18:23:49 UTC 2026 x86_64 GNU/Linux
[/external_agent_tool_result]

### 🤖 Codex  <small>2026-08-13 04:24</small>

Node.js v24.18.1 ya está instalado (vía nvm), así que no hace falta instalarlo. Ahora instalo las skills de Remotion:

### 🤖 Codex  <small>2026-08-13 04:24</small>

[external_agent_tool_call: Bash]
description: Install Remotion skills globally
command: cd "/home/matiigonzz/edicion de videos" && npx -y skills@latest add remotion-dev/skills -g -y 2>&1 | tail -50
[/external_agent_tool_call]

### 🤖 Codex  <small>2026-08-13 04:24</small>

[external_agent_tool_result]
│    symlinked: Claude Code                                               │
│  ✓ ~/.agents/skills/remotion-render                                     │
│    universal: Antigravity, Gemini CLI, GitHub Copilot, Kimi Code CLI,   │
│  OpenCode +12 more                                                      │
│    symlinked: Claude Code                                               │
│  ✓ ~/.agents/skills/remotion-saas                                       │
│    universal: Antigravity, Gemini CLI, GitHub Copilot, Kimi Code CLI,   │
│  OpenCode +12 more                                                      │
│    symlinked: Claude Code                                               │
│  ✓ ~/.agents/skills/remotion-studio                                     │
│    universal: Antigravity, Gemini CLI, GitHub Copilot, Kimi Code CLI,   │
│  OpenCode +12 more                                                      │
│    symlinked: Claude Code                                               │
│  ✓ ~/.agents/skills/remotion-upgrade                                    │
│    universal: Antigravity, Gemini CLI, GitHub Copilot, Kimi Code CLI,   │
│  OpenCode +12 more                                                      │
│    symlinked: Claude Code                                               │
│                                                                         │
├─────────────────────────────────────────────────────────────────────────╯

│
■  Failed to install 12
│
│    ✗ remotion-best-practices → PromptScript: PromptScript does not support global skill installation
│
│    ✗ remotion-captions → PromptScript: PromptScript does not support global skill installation
│
│    ✗ remotion-create → PromptScript: PromptScript does not support global skill installation
│
│    ✗ remotion-docs → PromptScript: PromptScript does not support global skill installation
│
│    ✗ remotion-interactivity → PromptScript: PromptScript does not support global skill installation
│
│    ✗ remotion-maps → PromptScript: PromptScript does not support global skill installation
│
│    ✗ remotion-markup → PromptScript: PromptScript does not support global skill installation
│
│    ✗ remotion-multimedia → PromptScript: PromptScript does not support global skill installation
│
│    ✗ remotion-render → PromptScript: PromptScript does not support global skill installation
│
│    ✗ remotion-saas → PromptScript: PromptScript does not support global skill installation
│
│    ✗ remotion-studio → PromptScript: PromptScript does not support global skill installation
│
│    ✗ remotion-upgrade → PromptScript: PromptScript does not support global skill installation

│
└  Done!  Review skills before use; they run with full agent permissions.
[/external_agent_tool_result]

### 🤖 Codex  <small>2026-08-13 04:24</small>

[external_agent_tool_call: Bash]
description: Verify skills installation
command: ls -la ~/.agents/skills/ 2>&1; echo "=== CLAUDE ==="; ls -la ~/.claude/skills/ 2>&1 | head -30
[/external_agent_tool_call]

### 🤖 Codex  <small>2026-08-13 04:24</small>

[external_agent_tool_result]
total 0
drwxr-xr-x. 1 matiigonzz matiigonzz 440 ago 12 22:58 .
drwxr-xr-x. 1 matiigonzz matiigonzz  44 ago  9 04:01 ..
drwxr-xr-x. 1 matiigonzz matiigonzz  16 ago  9 04:01 find-skills
drwxr-xr-x. 1 matiigonzz matiigonzz 386 ago 12 22:58 remotion-best-practices
drwxr-xr-x. 1 matiigonzz matiigonzz 166 ago 12 22:58 remotion-captions
drwxr-xr-x. 1 matiigonzz matiigonzz  92 ago 12 22:58 remotion-create
drwxr-xr-x. 1 matiigonzz matiigonzz  40 ago 12 22:58 remotion-docs
drwxr-xr-x. 1 matiigonzz matiigonzz  40 ago 12 22:58 remotion-interactivity
drwxr-xr-x. 1 matiigonzz matiigonzz  60 ago 12 22:58 remotion-maps
drwxr-xr-x. 1 matiigonzz matiigonzz 836 ago 12 22:58 remotion-markup
drwxr-xr-x. 1 matiigonzz matiigonzz 170 ago 12 22:58 remotion-multimedia
drwxr-xr-x. 1 matiigonzz matiigonzz  82 ago 12 22:58 remotion-render
drwxr-xr-x. 1 matiigonzz matiigonzz 106 ago 12 22:58 remotion-saas
drwxr-xr-x. 1 matiigonzz matiigonzz  40 ago 12 22:58 remotion-studio
drwxr-xr-x. 1 matiigonzz matiigonzz  40 ago 12 22:58 remotion-upgrade
drwxr-xr-x. 1 matiigonzz matiigonzz  58 ago  9 04:01 ui-ux-pro-max
=== CLAUDE ===
total 48
drwxr-xr-x. 1 matiigonzz matiigonzz 1640 ago 12 22:58 .
drwxr-xr-x. 1 matiigonzz matiigonzz  468 ago 10 23:24 ..
drwxr-xr-x. 1 matiigonzz matiigonzz   46 jul 30 02:26 ab-testing
drwxr-xr-x. 1 matiigonzz matiigonzz   58 jul 30 02:26 ad-creative
drwxr-xr-x. 1 matiigonzz matiigonzz   46 jul 30 02:26 ads
drwxr-xr-x. 1 matiigonzz matiigonzz   46 jul 30 02:26 ai-seo
drwxr-xr-x. 1 matiigonzz matiigonzz   46 jul 30 02:26 analytics
drwxr-xr-x. 1 matiigonzz matiigonzz   46 jul 30 02:26 aso
drwxr-xr-x. 1 matiigonzz matiigonzz   46 jul 30 02:26 attribution
drwxr-xr-x. 1 matiigonzz matiigonzz   36 jul 31 04:13 banner-design
drwxr-xr-x. 1 matiigonzz matiigonzz   68 jul 31 04:13 brand
drwxr-xr-x. 1 matiigonzz matiigonzz   46 jul 30 02:26 churn-prevention
drwxr-xr-x. 1 matiigonzz matiigonzz   46 jul 30 02:26 cold-email
drwxr-xr-x. 1 matiigonzz matiigonzz   26 jul 30 02:26 co-marketing
drwxr-xr-x. 1 matiigonzz matiigonzz   26 jul 30 02:26 community-marketing
drwxr-xr-x. 1 matiigonzz matiigonzz   46 jul 30 02:26 competitor-profiling
drwxr-xr-x. 1 matiigonzz matiigonzz   46 jul 30 02:26 competitors
drwxr-xr-x. 1 matiigonzz matiigonzz   46 jul 30 02:26 content-strategy
drwxr-xr-x. 1 matiigonzz matiigonzz   46 jul 30 02:26 copy-editing
drwxr-xr-x. 1 matiigonzz matiigonzz   46 jul 30 02:26 copywriting
drwxr-xr-x. 1 matiigonzz matiigonzz   46 jul 30 02:26 cro
drwxr-xr-x. 1 matiigonzz matiigonzz   46 jul 30 02:26 customer-research
drwxr-xr-x. 1 matiigonzz matiigonzz   58 jul 31 04:13 design
drwxr-xr-x. 1 matiigonzz matiigonzz   76 jul 31 04:13 design-system
drwxr-xr-x. 1 matiigonzz matiigonzz   46 jul 30 02:26 directory-submissions
drwxr-xr-x. 1 matiigonzz matiigonzz   46 jul 30 02:26 emails
drwxr-xr-x. 1 matiigonzz matiigonzz   46 jul 30 02:26 free-tools
drwxr-xr-x. 1 matiigonzz matiigonzz   46 jul 30 02:26 image
drwxr-xr-x. 1 matiigonzz matiigonzz   26 jul 30 02:26 influencer-marketing
[/external_agent_tool_result]

### 🤖 Codex  <small>2026-08-13 04:24</small>

[external_agent_tool_call: Bash]
description: Check Remotion symlinks in Claude skills
command: ls -la ~/.claude/skills/ | grep remotion
[/external_agent_tool_call]

### 🤖 Codex  <small>2026-08-13 04:24</small>

[external_agent_tool_result]
lrwxrwxrwx. 1 matiigonzz matiigonzz   44 ago 12 22:58 remotion-best-practices -> ../../.agents/skills/remotion-best-practices
lrwxrwxrwx. 1 matiigonzz matiigonzz   38 ago 12 22:58 remotion-captions -> ../../.agents/skills/remotion-captions
lrwxrwxrwx. 1 matiigonzz matiigonzz   36 ago 12 22:58 remotion-create -> ../../.agents/skills/remotion-create
lrwxrwxrwx. 1 matiigonzz matiigonzz   34 ago 12 22:58 remotion-docs -> ../../.agents/skills/remotion-docs
lrwxrwxrwx. 1 matiigonzz matiigonzz   43 ago 12 22:58 remotion-interactivity -> ../../.agents/skills/remotion-interactivity
lrwxrwxrwx. 1 matiigonzz matiigonzz   34 ago 12 22:58 remotion-maps -> ../../.agents/skills/remotion-maps
lrwxrwxrwx. 1 matiigonzz matiigonzz   36 ago 12 22:58 remotion-markup -> ../../.agents/skills/remotion-markup
lrwxrwxrwx. 1 matiigonzz matiigonzz   40 ago 12 22:58 remotion-multimedia -> ../../.agents/skills/remotion-multimedia
lrwxrwxrwx. 1 matiigonzz matiigonzz   36 ago 12 22:58 remotion-render -> ../../.agents/skills/remotion-render
lrwxrwxrwx. 1 matiigonzz matiigonzz   34 ago 12 22:58 remotion-saas -> ../../.agents/skills/remotion-saas
lrwxrwxrwx. 1 matiigonzz matiigonzz   36 ago 12 22:58 remotion-studio -> ../../.agents/skills/remotion-studio
lrwxrwxrwx. 1 matiigonzz matiigonzz   37 ago 12 22:58 remotion-upgrade -> ../../.agents/skills/remotion-upgrade
[/external_agent_tool_result]

### 🤖 Codex  <small>2026-08-13 04:24</small>

Todo listo. Verifico dependencias del sistema que Remotion necesita en Linux para renderizar:

### 🤖 Codex  <small>2026-08-13 04:24</small>

[external_agent_tool_call: Bash]
description: Check Chrome headless system libraries
command: for lib in libnss3.so libatk-1.0.so.0 libatk-bridge-2.0.so.0 libcups.so.2 libdrm.so.2 libxkbcommon.so.0 libXcomposite.so.1 libXdamage.so.1 libXfixes.so.3 libXrandr.so.2 libgbm.so.1 libpango-1.0.so.0 libcairo.so.2 libasound.so.2; do
  if ldconfig -p 2>/dev/null | grep -q "$lib"; then echo "OK   $lib"; else echo "FALTA $lib"; fi
done
[/external_agent_tool_call]

### 🤖 Codex  <small>2026-08-13 04:24</small>

[external_agent_tool_result]
OK   libnss3.so
OK   libatk-1.0.so.0
OK   libatk-bridge-2.0.so.0
OK   libcups.so.2
OK   libdrm.so.2
OK   libxkbcommon.so.0
OK   libXcomposite.so.1
OK   libXdamage.so.1
OK   libXfixes.so.3
OK   libXrandr.so.2
OK   libgbm.so.1
OK   libpango-1.0.so.0
OK   libcairo.so.2
OK   libasound.so.2
[/external_agent_tool_result]

### 🤖 Codex  <small>2026-08-13 04:24</small>

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
