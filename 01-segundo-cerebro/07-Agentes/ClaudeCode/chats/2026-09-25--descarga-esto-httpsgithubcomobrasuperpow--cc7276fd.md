---
tool: ClaudeCode
session_id: cc7276fd-f4f6-47f4-ada1-e7bcb49dc7eb
fecha: 2026-09-25 02:25
titulo: "descarga esto httpsgithubcomobrasuperpowers"
tags: [chat, agente, claudecode]
---

# 💬 descarga esto httpsgithubcomobrasuperpowers
> **ClaudeCode** · 2026-09-25 02:25 · `cc7276fd-f4f6-47f4-ada1-e7bcb49dc7eb`

---

### 🧑 Vos  <small>2026-09-25 02:25</small>

descarga esto https://github.com/obra/superpowers

### 🤖 Claude  <small>2026-09-25 02:25</small>

I'll clone that repo. Let me check where to put it first.

### 🤖 Claude  <small>2026-09-25 02:25</small>

_[usó herramienta: Bash]_

### 🤖 Claude  <small>2026-09-25 02:25</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-09-25 02:25</small>

_[resultado de herramienta]_

### 🧑 Vos  <small>2026-09-25 02:25</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-25 02:25</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-09-25 02:25</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-25 02:25</small>

Voy a clonarlo.

### 🤖 Claude  <small>2026-09-25 02:25</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-09-25 02:25</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-25 02:25</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-09-25 02:25</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-25 02:25</small>

Clonado. Veo qué es y cómo se instala.

### 🤖 Claude  <small>2026-09-25 02:25</small>

_[usó herramienta: Read]_

### 🧑 Vos  <small>2026-09-25 02:25</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-25 02:25</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-09-25 02:25</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-25 02:26</small>

Listo. Clonado en [superpowers](superpowers) (`~/Claude/superpowers`), 11 MB, versión **v6.4.1**.

**Qué es:** una metodología completa de desarrollo para agentes de código (Claude Code, Codex, Cursor, Gemini CLI, Hermes, etc.). No es una librería: son 15 skills que se activan solas y fuerzan un flujo spec → plan → TDD → subagentes.

Las 15 skills:

| | |
|---|---|
| brainstorming | requesting-code-review |
| writing-plans | receiving-code-review |
| executing-plans | verification-before-completion |
| subagent-driven-development | systematic-debugging |
| test-driven-development | using-git-worktrees |
| dispatching-parallel-agents | finishing-a-development-branch |
| writing-skills | diagnosing-superpowers |
| using-superpowers | |

**Ojo:** clonar el repo *no* lo activa. Para que Claude Code lo use realmente hay que instalarlo como plugin desde el marketplace oficial:

```bash
/plugin install superpowers@claude-plugins-official
```

Ese comando abre un panel interactivo, así que corrélo desde una terminal `claude` normal, no acá.

Dos cosas a tener en cuenta antes de instalarlo:

1. Ya tenés `agent-skills` cargado en esta sesión, con su propio flowchart de descubrimiento (spec-driven-development, incremental-implementation, etc.). Superpowers cubre terreno muy parecido — los dos van a competir por el mismo momento del flujo. Vale la pena decidir con cuál te quedás en vez de correr ambos.
2. El repo tiene hooks de session-start; si lo instalás, se ejecutan en cada sesión.

¿Querés que revise algo puntual del contenido, o lo dejamos descargado como referencia?

### 🧑 Vos  <small>2026-09-25 02:26</small>

<bash-input>/plugin install superpowers@claude-plugins-official</bash-input><bash-stdout>bash: /plugin: No existe el fichero o el directorio</bash-stdout><bash-stderr></bash-stderr>

### 🤖 Claude  <small>2026-09-25 02:26</small>

Eso no es un comando de shell — es un slash command de Claude Code, se escribe en el prompt del chat, no en modo bash. Por eso el `bash: /plugin: No existe el fichero`.

Déjame ver si tu versión tiene subcomando CLI no interactivo:

### 🤖 Claude  <small>2026-09-25 02:26</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-09-25 02:26</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-25 02:26</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-09-25 02:26</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-25 02:26</small>

Sí hay CLI no interactiva:

### 🤖 Claude  <small>2026-09-25 02:26</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-09-25 02:26</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-25 02:26</small>

`claude plugin install` existe. Veo qué marketplaces tenés registrados:

### 🤖 Claude  <small>2026-09-25 02:26</small>

_[usó herramienta: Bash]_

### 🤖 Claude  <small>2026-09-25 02:27</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-09-25 02:27</small>

_[resultado de herramienta]_

### 🧑 Vos  <small>2026-09-25 02:27</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-25 02:27</small>

El marketplace ya está registrado. Instalo:

### 🤖 Claude  <small>2026-09-25 02:27</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-09-25 02:27</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-25 02:27</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-09-25 02:27</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-25 02:27</small>

✔ Instalado: **superpowers@claude-plugins-official v6.4.1**, scope user, enabled.

Tres cosas para cerrar:

**1. Hay que reiniciar.** Los hooks de session-start y las skills se cargan al arrancar la sesión, así que no está activo en este chat. Salí y volvé a entrar a `claude`.

**2. El clon que bajé antes quedó al pedo.** El plugin maneja su propia copia en `~/.claude/plugins/`. El `~/Claude/superpowers` es redundante salvo que quieras leer el código o contribuir. Si no:

```bash
rm -rf /home/matiigonzz/Claude/superpowers
```

**3. Sigue el solapamiento con `agent-skills`.** Ahora tenés los dos enabled y ambos pelean por el mismo momento del flujo — Superpowers dice "brainstorming → writing-plans → TDD", agent-skills dice "spec-driven-development → planning-and-task-breakdown → TDD". No se rompe nada, pero vas a comer el doble de tokens de instrucciones en cada sesión y los flowcharts se van a contradecir en los bordes.

Si querés probar Superpowers solo:

```bash
claude plugin disable agent-skills@addy-agent-skills
```

Y para volver atrás es `enable` con el mismo nombre. Mi recomendación: corré una tarea real con Superpowers solo antes de decidir — es la única forma de saber cuál te sirve más.

### 🧑 Vos  <small>2026-09-25 02:31</small>

<bash-input>rm -rf /home/matiigonzz/Claude/superpowers</bash-input><bash-stdout>[No output was captured. The command ran in the terminal pane (tab 0); if it should have printed something, use read_terminal with tab_id "0" to check.]</bash-stdout><bash-stderr></bash-stderr>

### 🤖 Claude  <small>2026-09-25 02:31</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-09-25 02:31</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-25 02:32</small>

Borrado. Estado final:

- **superpowers v6.4.1** instalado como plugin (user scope, enabled)
- Clon redundante eliminado
- `agent-skills` sigue enabled en paralelo

Falta reiniciar `claude` para que cargue. Y queda pendiente decidir si convivís con los dos o desactivás `agent-skills`.

### 🧑 Vos  <small>2026-09-25 02:32</small>

<bash-input>claude plugin disable agent-skills@addy-agent-skills</bash-input><bash-stdout>✔ Successfully disabled plugin: agent-skills (scope: user)</bash-stdout><bash-stderr></bash-stderr>

### 🤖 Claude  <small>2026-09-25 02:32</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-09-25 02:32</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-25 02:32</small>

Confirmado — `agent-skills` disabled, Superpowers solo.

| Plugin | Estado |
|---|---|
| superpowers 6.4.1 | ✔ enabled |
| agent-skills 0.6.8 | ✘ disabled |
| ui-ux-pro-max 2.13.0 | ✔ enabled |
| watch 0.2.0 | ✔ enabled |
| humanizer 2.8.2 | ✔ loaded (skills-dir) |

Ojo con esto: la sesión actual todavía tiene `agent-skills` cargado en memoria — lo ves arriba de todo en mi contexto, con su flowchart. El disable recién aplica al reiniciar. Así que si seguís trabajando acá, vas a estar corriendo el que acabás de apagar.

```bash
claude
```

Para volver atrás, `claude plugin enable agent-skills@addy-agent-skills`.

Después de probarlo un rato contame cómo te fue — si Superpowers te resulta demasiado ceremonioso para tareas chicas, se puede tener ambos desactivados y llamar skills puntuales a mano.

### 🧑 Vos  <small>2026-09-25 02:34</small>

https://github.com/Shubhamsaboo/awesome-llm-apps

### 🤖 Claude  <small>2026-09-25 02:35</small>

Asumo lo mismo que antes: clonarlo. Primero miro el tamaño, que este repo tiene fama de pesado:

### 🤖 Claude  <small>2026-09-25 02:35</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-09-25 02:35</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-25 02:35</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-09-25 02:35</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-25 02:35</small>

216 MB, 139k estrellas, actualizado ayer. Es una colección de ~100 apps de ejemplo (agentes, RAG, skills), no una librería que se instala.

Como es material de referencia y no algo donde vayas a commitear, clono sin historial (`--depth 1`) para bajar bastante menos:

### 🤖 Claude  <small>2026-09-25 02:35</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-09-25 02:35</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-25 02:35</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-09-25 02:35</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-25 02:35</small>

Clonado en [awesome-llm-apps](awesome-llm-apps) — 159 MB, sin historial.

| Carpeta | Qué hay |
|---|---|
| `starter_ai_agents/` | agentes simples, punto de entrada |
| `advanced_ai_agents/` | multi-agente, autónomos |
| `agent_skills/` | skills al estilo de las que ya usás |
| `rag_tutorials/` | RAG, el bloque más grande |
| `mcp_ai_agents/` | agentes sobre MCP |
| `voice_ai_agents/` · `generative_ui_agents/` · `always_on_agents/` | voz, UI generativa, procesos persistentes |
| `ai_agent_framework_crash_course/` | curso por framework |

219 READMEs, 550 archivos `.py`.

Dos avisos:

**No es instalable.** Cada app es un proyecto suelto con su propio `requirements.txt` y sus API keys. Se usa entrando a una carpeta puntual, no "activando" nada.

**Esto no se cruza con Superpowers.** Superpowers es metodología de trabajo; esto es código de ejemplo para leer y copiar. Conviven sin problema.

Si me decís qué te interesa (RAG, MCP, voz, skills) te reviso esa carpeta y te marco cuáles valen la pena — con 219 ejemplos, la mitad son variaciones del mismo patrón.
