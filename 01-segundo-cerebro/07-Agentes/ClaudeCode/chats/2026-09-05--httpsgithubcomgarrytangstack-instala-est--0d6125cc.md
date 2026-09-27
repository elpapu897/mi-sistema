---
tool: ClaudeCode
session_id: 0d6125cc-8388-4795-8c3b-324a9884df69
fecha: 2026-09-05 02:02
titulo: "httpsgithubcomgarrytangstack instala esta skill"
tags: [chat, agente, claudecode]
---

# 💬 httpsgithubcomgarrytangstack instala esta skill
> **ClaudeCode** · 2026-09-05 02:02 · `0d6125cc-8388-4795-8c3b-324a9884df69`

---

### 🧑 Vos  <small>2026-09-05 02:02</small>

https://github.com/garrytan/gstack instala esta skill

### 🤖 Claude  <small>2026-09-05 02:02</small>

I'll check out that repo and install the skill.

### 🤖 Claude  <small>2026-09-05 02:02</small>

_[usó herramienta: Bash]_

### 🤖 Claude  <small>2026-09-05 02:02</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-09-05 02:02</small>

_[resultado de herramienta]_

### 🧑 Vos  <small>2026-09-05 02:02</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-05 02:02</small>

_[usó herramienta: Bash]_

### 🤖 Claude  <small>2026-09-05 02:02</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-09-05 02:02</small>

_[resultado de herramienta]_

### 🧑 Vos  <small>2026-09-05 02:02</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-05 02:02</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-09-05 02:02</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-05 02:02</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-09-05 02:02</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-05 02:02</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-09-05 02:02</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-05 02:02</small>

Falta `bun`. Lo instalo en tu home (sin sudo):

### 🤖 Claude  <small>2026-09-05 02:02</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-09-05 02:03</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-05 02:03</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-09-05 02:05</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-05 02:05</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-09-05 02:05</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-05 02:05</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-09-05 02:05</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-05 02:05</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-09-05 02:05</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-05 02:05</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-09-05 02:05</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-05 02:05</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-09-05 02:05</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-05 02:05</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-09-05 02:05</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-05 02:05</small>

_[usó herramienta: Read]_

### 🧑 Vos  <small>2026-09-05 02:05</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-05 02:06</small>

_[usó herramienta: Write]_

### 🧑 Vos  <small>2026-09-05 02:06</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-05 02:06</small>

Instalado. ✅

**Qué hice:**
1. Cloné el repo en `~/.claude/skills/gstack`
2. Instalé `bun` (era requisito y no lo tenías) en `~/.bun/bin`, agregado al PATH en `~/.bash_profile`
3. Corrí `./setup` → 55 skills enlazadas + Chromium de Playwright descargado (para `/browse` y `/qa`)
4. Agregué la sección **gstack** a [CLAUDE.md](/home/matiigonzz/.claude/CLAUDE.md) global con la lista de comandos y la regla de usar `/browse` en vez de `mcp__claude-in-chrome__*`

**Dos avisos importantes:**

- **Colisiones de nombres:** gstack pisó 6 skills tuyas en `~/.claude/skills` que venían de `~/.agents/skills`: `codex`, `design-review`, `freeze`, `office-hours`, `retro`, `review`. Las originales siguen intactas en `~/.agents/skills` (solo cambió a dónde apunta el link en Claude Code). Si querés recuperar alguna, hay que renombrarla.
- **`sync-skills.sh`:** la próxima vez que lo corras va a intentar re-enlazar esas 6 y puede dejar directorios raros (gstack crea carpetas con symlinks adentro, no symlinks). Conviene agregar una lista de exclusión al script.

**Probalo (reiniciá la sesión para que cargue las skills):**

```bash
source ~/.bash_profile && ~/.claude/skills/gstack/bin/gstack-config list
```

¿Querés que le agregue la exclusión a `sync-skills.sh` para evitar el conflicto?

### 🧑 Vos  <small>2026-09-05 02:06</small>

quería que me ayudes a instalar este repo, no sé, porque te dije skill. Era era repo, perdón.

### 🤖 Claude  <small>2026-09-05 02:07</small>

Tranquilo, no hay error: **es lo mismo**. gstack es un repo cuya forma oficial de instalación es justamente clonarlo en `~/.claude/skills/gstack` y correr `./setup` — así lo indica el README del propio Garry Tan. Eso es lo que hice, así que el repo ya está instalado correctamente.

O sea:

- **El repo** está clonado en `~/.claude/skills/gstack` (podés entrar, leer el código, hacerle `git pull`, forkearlo, lo que quieras)
- **El setup** enlazó sus 55 comandos para que Claude Code los pueda usar

Si lo que querías era otra cosa, decime cuál:

1. **Tener el repo en otro lado** (ej. `~/proyectos/gstack`) solo para leerlo/modificarlo, sin que toque tu config global → lo muevo y revierto los cambios
2. **Dejarlo como está** y usarlo (`/office-hours`, `/review`, `/qa`, etc.)
3. **Desinstalarlo del todo** y devolver las 6 skills que quedaron pisadas (`codex`, `design-review`, `freeze`, `office-hours`, `retro`, `review`)

¿Cuál de las tres?

### 🧑 Vos  <small>2026-09-05 02:07</small>

1

### 🤖 Claude  <small>2026-09-05 02:07</small>

Voy a revertir el setup y mover el repo. Primero veo si trae desinstalador:

### 🤖 Claude  <small>2026-09-05 02:07</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-09-05 02:07</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-05 02:07</small>

Hay `gstack-uninstall`. Lo corro:

### 🤖 Claude  <small>2026-09-05 02:07</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-09-05 02:07</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-05 02:07</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-09-05 02:07</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-05 02:07</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-09-05 02:07</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-05 02:07</small>

Restauro las 6 skills que habían quedado pisadas:

### 🤖 Claude  <small>2026-09-05 02:07</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-09-05 02:09</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-05 02:10</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-09-05 02:10</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-05 02:10</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-09-05 02:10</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-05 02:10</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-09-05 02:10</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-05 02:10</small>

Ahora revierto el CLAUDE.md global:

### 🤖 Claude  <small>2026-09-05 02:10</small>

_[usó herramienta: Write]_

### 🧑 Vos  <small>2026-09-05 02:10</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-05 02:10</small>

Listo. Todo revertido y el repo está donde querías.

**Estado final:**

| Cosa | Estado |
|---|---|
| Repo gstack | ✅ Clonado en `~/proyectos/gstack` (160 MB, historial completo) |
| Install en `~/.claude/skills/gstack` | ❌ Eliminado (`gstack-uninstall --force`) |
| 55 skills enlazadas | ❌ Eliminadas |
| Hooks en `settings.json` | ❌ Eliminados (SessionStart + Stop) |
| Estado en `~/.gstack/` | ❌ Eliminado |
| Tus 6 skills pisadas (`codex`, `design-review`, `freeze`, `office-hours`, `retro`, `review`) | ✅ Restauradas apuntando a `~/.agents/skills` |
| `CLAUDE.md` global | ✅ Volvió al original |

**Lo único que quedó instalado:**
- **`bun`** en `~/.bun/bin` (+ línea de PATH en `~/.bash_profile`)
- **Chromium de Playwright** en `~/.cache/ms-playwright` (~300 MB)

Los dejé porque son herramientas genéricas y útiles, pero si querés que los saque también decime.

El repo lo podés explorar así:

```bash
ls ~/proyectos/gstack
```

Lo interesante para leer: `SKILL.md`, `ARCHITECTURE.md`, `ETHOS.md` y las carpetas de cada comando (`review/`, `qa/`, `office-hours/`) — son puro Markdown, muy fáciles de canibalizar para tus propias skills.

### 🧑 Vos  <small>2026-09-05 02:13</small>

<task-notification>
<task-id>bq4ahnujv</task-id>
<tool-use-id>toolu_01DQeswZ4XrVhxQbSLYLLVPR</tool-use-id>
<output-file>/tmp/claude-1000/-home-matiigonzz-Claude/0d6125cc-8388-4795-8c3b-324a9884df69/tasks/bq4ahnujv.output</output-file>
<status>completed</status>
<summary>Background command "Finish skills sync in background" completed (exit code 0)</summary>
</task-notification>

### 🤖 Claude  <small>2026-09-05 02:13</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-09-05 02:13</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-05 02:13</small>

El sync de skills terminó bien (código 0): **1100 skills canónicas**, 0 symlinks rotos, y no quedó ningún rastro de gstack en `~/.claude/skills`, `~/.codex/skills` ni `~/.agents/skills`.

La limpieza está completa. El repo te queda solo en `~/proyectos/gstack` para leerlo tranquilo.
