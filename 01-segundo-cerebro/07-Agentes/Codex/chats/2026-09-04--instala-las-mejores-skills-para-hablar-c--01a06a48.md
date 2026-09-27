---
tool: Codex
session_id: 01a06a48-7aae-7462-a59a-59418811810d
fecha: 2026-09-04 02:38
titulo: "instala las mejores skills para hablar con mujeres"
tags: [chat, agente, codex]
---

# 💬 instala las mejores skills para hablar con mujeres
> **Codex** · 2026-09-04 02:38 · `01a06a48-7aae-7462-a59a-59418811810d`

---

### 🧑 Vos  <small>2026-09-04 02:38</small>

instala las mejores skills para hablar con mujeres por chat

### 🤖 Codex  <small>2026-09-04 02:38</small>

[external_agent_tool_call: Bash]
description: Inspect skills setup
command: ls ~/.agents/skills | head -50; echo "---"; ls ~/.claude/skills 2>/dev/null | head; echo "---"; cat ~/Claude/scripts/sync-skills.sh 2>/dev/null | head -40
[/external_agent_tool_call]

### 🤖 Codex  <small>2026-09-04 02:38</small>

[external_agent_tool_result]
37signals-way
3d-logo-animation
a11y-audit
ab-testing
ab-test-setup
ab-test-store-listing
accessibility-review
account-research
action-figure-generator
ad-account-auditor
ad-creative
ad-creative-builder
ads
ad-test-designer
adversarial-reviewer
advocacy-program-designer
aeo
agent-decision-receipts
agent-designer
agent-harness
agenthub
agent-md-refactor
agent-protocol
agent-workflow-designer
agile-product-owner
ai-act-readiness
ai-clipping
ai-fight-scene
aims-audit
ai-security
ai-seo
alpha-scene-gen
amazon-product-listing
analytics
analytics-tracking
analyze
andreessen
android-aso
animal-video-generator
animation-basics
api-design-reviewer
api-test-suite-builder
app-analytics
app-clips
app-icon-optimization
app-launch
apple-hig-expert
apple-search-ads
apply-aesthetic
app-marketing-context
---
37signals-way
3d-logo-animation
a11y-audit
ab-testing
ab-test-setup
ab-test-store-listing
accessibility-review
account-research
action-figure-generator
ad-account-auditor
---
#!/usr/bin/env bash
# sync-skills.sh — Deja TODAS las skills disponibles en TODOS los agentes.
#
# Modelo:
#   ~/.agents/skills/<nombre>/   = fuente canónica (copias reales)
#   ~/.<agente>/skills/<nombre>  = symlink relativo a la canónica
#
# Las skills que vienen dentro de plugins (marketplace de Codex/Claude) se
# COPIAN, no se enlazan, porque su ruta incluye la versión del plugin y los
# symlinks se romperían en cada actualización. Volvé a correr este script
# después de actualizar plugins para refrescarlas.
#
# IMPORTANTE — anti-duplicados: Codex ya carga por su cuenta las skills de los
# plugins que tiene habilitados (marketplaces claude-cowork y
# local-desktop-app-uploads). Si además se las enlazáramos en ~/.codex/skills
# las vería DOS veces y desperdiciaría contexto. Por eso a Codex solo se le
# enlazan las skills que NO provienen de esos plugins.
#
# Uso:  ./sync-skills.sh [--dry-run]

set -uo pipefail

CANON="$HOME/.agents/skills"
DRY=0
[ "${1:-}" = "--dry-run" ] && DRY=1

say() { printf '%s\n' "$*"; }
run() { [ $DRY -eq 1 ] && say "  [dry] $*" || "$@"; }

mkdir -p "$CANON"

# ---------------------------------------------------------------- 1. fuentes
# Carpetas donde viven plugins que empaquetan skills.
PLUGIN_ROOTS=(
    "$HOME/.codex/plugins/cache/claude-cowork"
    "$HOME/.claude/plugins/marketplaces/local-desktop-app-uploads"
)

# Marketplaces que Codex ya carga solo (para no duplicarle skills).
CODEX_OWN_SOURCES='claude-cowork|local-desktop-app-uploads'
[/external_agent_tool_result]

### 🤖 Codex  <small>2026-09-04 02:38</small>

[external_agent_tool_call: Bash]
description: Search for relevant existing skills
command: ls ~/.agents/skills | grep -Ei "date|dating|flirt|convers|social|charis|rapport|charm|relation|text|message|communic|empath|small-talk|storytell|humor|comedy"
[/external_agent_tool_call]

### 🤖 Codex  <small>2026-09-04 02:38</small>

[external_agent_tool_result]
app-marketing-context
consolidate-memory
context-engine
conversion-signal-qa
conversion-value-mapper
daily-meeting-update
dark-social-attributor
data-context-extractor
dependency-updater
difficult-workplace-conversations
marketing-context
message-house-builder
message-system-architect
message-test-designer
muapi-social-media-video
press-media-relations
professional-communication
public-relations
roadmap-communicator
roadmap-update
social
social-calendar-builder
social-content
social-content-os
social-creative-builder
social-measurement-loop
social-media-analyzer
social-media-manager
social-media-video
social-pack
social-pulse-monitor
social-quality-auditor
social-selling-planner
stakeholder-update
team-communications
threejs-textures
update
validate-data
[/external_agent_tool_result]

### 🤖 Codex  <small>2026-09-04 02:38</small>

[external_agent_tool_call: Bash]
description: Read example skill format
command: cat ~/.agents/skills/difficult-workplace-conversations/SKILL.md | head -60; echo "=== FILES"; ls -R ~/.agents/skills/difficult-workplace-conversations | head -20
[/external_agent_tool_call]

### 🤖 Codex  <small>2026-09-04 02:38</small>

[external_agent_tool_result]
---
name: difficult-workplace-conversations
description: Structured approach to workplace conflicts, performance discussions, and challenging feedback using preparation-delivery-followup framework. Use when preparing for tough conversations, addressing conflicts, giving critical feedback, or navigating sensitive workplace discussions.
allowed-tools: Read, Glob, Grep
---

# Difficult Conversations Skill

A structured framework for approaching challenging workplace conversations including conflicts, performance issues, sensitive feedback, and emotionally charged discussions.

## When to Use This Skill

- Preparing for a challenging conversation with a colleague
- Addressing performance issues with a team member
- Delivering difficult feedback to a peer or manager
- Navigating conflict between team members
- Discussing sensitive topics (salary, promotion, termination)
- Handling emotional or defensive reactions
- Following up after difficult discussions

## Core Framework: Preparation-Delivery-Followup

Difficult conversations succeed or fail based on three phases:

### Phase 1: Preparation (Before)

**Purpose:** Set yourself up for a productive conversation

1. **Clarify the Issue**
   - What specifically happened? (Observable facts only)
   - What is the impact? (On you, team, work)
   - What do you need to change?

2. **Check Your Emotions**
   - What am I feeling? Why?
   - Am I calm enough to have this conversation?
   - What might trigger me during this conversation?

3. **Consider Their Perspective**
   - How might they see this situation?
   - What constraints or pressures might they have?
   - What do they care about that I can acknowledge?

4. **Define Your Goal**
   - What outcome do I want?
   - What is the minimum acceptable result?
   - What am I willing to compromise on?

### Phase 2: Delivery (During)

**Purpose:** Have the conversation effectively

1. **Open Neutrally**
   - Start with facts, not judgments
   - Express intent to understand, not accuse
   - Create psychological safety

2. **Share Your Perspective**
   - Describe behavior, not character
   - Focus on impact, not intention
=== FILES
/home/matiigonzz/.agents/skills/difficult-workplace-conversations:
README.md
references
SKILL.md

/home/matiigonzz/.agents/skills/difficult-workplace-conversations/references:
conversation-framework.md
delivery-scripts.md
emotional-regulation.md
preparation-template.md
[/external_agent_tool_result]

### 🤖 Codex  <small>2026-09-04 02:38</small>

Voy a crear un set de skills nuevas (no hay nada de esto instalado) y sincronizarlas a todos tus agentes.

### 🤖 Codex  <small>2026-09-04 02:38</small>

[external_agent_tool_call: Bash]
description: Create skill directories
command: mkdir -p ~/.agents/skills/{chat-primeros-mensajes,coqueteo-calibrado,perfil-apps-citas,invitar-a-salir}/references && echo ok
[/external_agent_tool_call]

### 🤖 Codex  <small>2026-09-04 02:38</small>

[external_agent_tool_result]
ok
[/external_agent_tool_result]

### 🤖 Codex  <small>2026-09-04 02:38</small>

[external_agent_tool_call: Write]
file: /home/matiigonzz/.agents/skills/chat-primeros-mensajes/SKILL.md
[/external_agent_tool_call]

### 🤖 Codex  <small>2026-09-04 02:38</small>

[external_agent_tool_result]
File created successfully at: /home/matiigonzz/.agents/skills/chat-primeros-mensajes/SKILL.md (file state is current in your context — no need to Read it back)
[/external_agent_tool_result]

### 🤖 Codex  <small>2026-09-04 02:38</small>

[external_agent_tool_call: Write]
file: /home/matiigonzz/.agents/skills/chat-primeros-mensajes/references/aperturas.md
[/external_agent_tool_call]

### 🤖 Codex  <small>2026-09-04 02:38</small>

[external_agent_tool_result]
File created successfully at: /home/matiigonzz/.agents/skills/chat-primeros-mensajes/references/aperturas.md (file state is current in your context — no need to Read it back)
[/external_agent_tool_result]

### 🤖 Codex  <small>2026-09-04 02:38</small>

[external_agent_tool_call: Write]
file: /home/matiigonzz/.agents/skills/chat-primeros-mensajes/references/sostener-charla.md
[/external_agent_tool_call]

### 🤖 Codex  <small>2026-09-04 02:38</small>

[external_agent_tool_result]
File created successfully at: /home/matiigonzz/.agents/skills/chat-primeros-mensajes/references/sostener-charla.md (file state is current in your context — no need to Read it back)
[/external_agent_tool_result]

### 🤖 Codex  <small>2026-09-04 02:38</small>

[external_agent_tool_call: Write]
file: /home/matiigonzz/.agents/skills/chat-primeros-mensajes/references/diagnostico-hilo.md
[/external_agent_tool_call]

### 🤖 Codex  <small>2026-09-04 02:38</small>

[external_agent_tool_result]
File created successfully at: /home/matiigonzz/.agents/skills/chat-primeros-mensajes/references/diagnostico-hilo.md (file state is current in your context — no need to Read it back)
[/external_agent_tool_result]

### 🤖 Codex  <small>2026-09-04 02:38</small>

Ahora la de coqueteo:

### 🤖 Codex  <small>2026-09-04 02:38</small>

[external_agent_tool_call: Write]
file: /home/matiigonzz/.agents/skills/coqueteo-calibrado/SKILL.md
[/external_agent_tool_call]

### 🤖 Codex  <small>2026-09-04 02:38</small>

[external_agent_tool_result]
File created successfully at: /home/matiigonzz/.agents/skills/coqueteo-calibrado/SKILL.md (file state is current in your context — no need to Read it back)
[/external_agent_tool_result]

### 🤖 Codex  <small>2026-09-04 02:38</small>

[external_agent_tool_call: Write]
file: /home/matiigonzz/.agents/skills/coqueteo-calibrado/references/escalera-tension.md
[/external_agent_tool_call]

### 🤖 Codex  <small>2026-09-04 02:38</small>

[external_agent_tool_result]
File created successfully at: /home/matiigonzz/.agents/skills/coqueteo-calibrado/references/escalera-tension.md (file state is current in your context — no need to Read it back)
[/external_agent_tool_result]

### 🤖 Codex  <small>2026-09-04 02:38</small>

[external_agent_tool_call: Write]
file: /home/matiigonzz/.agents/skills/coqueteo-calibrado/references/senales.md
[/external_agent_tool_call]

### 🤖 Codex  <small>2026-09-04 02:38</small>

[external_agent_tool_result]
File created successfully at: /home/matiigonzz/.agents/skills/coqueteo-calibrado/references/senales.md (file state is current in your context — no need to Read it back)
[/external_agent_tool_result]

### 🤖 Codex  <small>2026-09-04 02:38</small>

[external_agent_tool_call: Write]
file: /home/matiigonzz/.agents/skills/coqueteo-calibrado/references/despues-del-no.md
[/external_agent_tool_call]

### 🤖 Codex  <small>2026-09-04 02:38</small>

[external_agent_tool_result]
File created successfully at: /home/matiigonzz/.agents/skills/coqueteo-calibrado/references/despues-del-no.md (file state is current in your context — no need to Read it back)
[/external_agent_tool_result]

### 🤖 Codex  <small>2026-09-04 02:38</small>

[external_agent_tool_call: Write]
file: /home/matiigonzz/.agents/skills/invitar-a-salir/SKILL.md
[/external_agent_tool_call]

### 🤖 Codex  <small>2026-09-04 02:38</small>

[external_agent_tool_result]
File created successfully at: /home/matiigonzz/.agents/skills/invitar-a-salir/SKILL.md (file state is current in your context — no need to Read it back)
[/external_agent_tool_result]

### 🤖 Codex  <small>2026-09-04 02:38</small>

[external_agent_tool_call: Write]
file: /home/matiigonzz/.agents/skills/invitar-a-salir/references/formulas-invitacion.md
[/external_agent_tool_call]

### 🤖 Codex  <small>2026-09-04 02:38</small>

[external_agent_tool_result]
File created successfully at: /home/matiigonzz/.agents/skills/invitar-a-salir/references/formulas-invitacion.md (file state is current in your context — no need to Read it back)
[/external_agent_tool_result]

### 🤖 Codex  <small>2026-09-04 02:38</small>

[external_agent_tool_call: Write]
file: /home/matiigonzz/.agents/skills/invitar-a-salir/references/planes-primera-cita.md
[/external_agent_tool_call]

### 🤖 Codex  <small>2026-09-04 02:38</small>

[external_agent_tool_result]
File created successfully at: /home/matiigonzz/.agents/skills/invitar-a-salir/references/planes-primera-cita.md (file state is current in your context — no need to Read it back)
[/external_agent_tool_result]

### 🤖 Codex  <small>2026-09-04 02:38</small>

[external_agent_tool_call: Write]
file: /home/matiigonzz/.agents/skills/invitar-a-salir/references/antes-y-despues.md
[/external_agent_tool_call]

### 🤖 Codex  <small>2026-09-04 02:38</small>

[external_agent_tool_result]
File created successfully at: /home/matiigonzz/.agents/skills/invitar-a-salir/references/antes-y-despues.md (file state is current in your context — no need to Read it back)
[/external_agent_tool_result]

### 🤖 Codex  <small>2026-09-04 02:38</small>

Ahora la de perfiles de apps:

### 🤖 Codex  <small>2026-09-04 02:38</small>

[external_agent_tool_call: Write]
file: /home/matiigonzz/.agents/skills/perfil-apps-citas/SKILL.md
[/external_agent_tool_call]

### 🤖 Codex  <small>2026-09-04 02:38</small>

[external_agent_tool_result]
File created successfully at: /home/matiigonzz/.agents/skills/perfil-apps-citas/SKILL.md (file state is current in your context — no need to Read it back)
[/external_agent_tool_result]

### 🤖 Codex  <small>2026-09-04 02:38</small>

[external_agent_tool_call: Write]
file: /home/matiigonzz/.agents/skills/perfil-apps-citas/references/checklist-fotos.md
[/external_agent_tool_call]

### 🤖 Codex  <small>2026-09-04 02:38</small>

[external_agent_tool_result]
File created successfully at: /home/matiigonzz/.agents/skills/perfil-apps-citas/references/checklist-fotos.md (file state is current in your context — no need to Read it back)
[/external_agent_tool_result]

### 🤖 Codex  <small>2026-09-04 02:38</small>

[external_agent_tool_call: Write]
file: /home/matiigonzz/.agents/skills/perfil-apps-citas/references/bios-y-prompts.md
[/external_agent_tool_call]

### 🤖 Codex  <small>2026-09-04 02:38</small>

[external_agent_tool_result]
File created successfully at: /home/matiigonzz/.agents/skills/perfil-apps-citas/references/bios-y-prompts.md (file state is current in your context — no need to Read it back)
[/external_agent_tool_result]

### 🤖 Codex  <small>2026-09-04 02:38</small>

Ahora sincronizo a todos los agentes:

### 🤖 Codex  <small>2026-09-04 02:38</small>

[external_agent_tool_call: Bash]
description: Run skills sync script
command: bash ~/Claude/scripts/sync-skills.sh 2>&1 | tail -25
[/external_agent_tool_call]

### 🤖 Codex  <small>2026-09-04 02:38</small>

[external_agent_tool_result]
Command did not complete within its 120s timeout and was moved to the background (ID: bhx4oamth). Output is being written to: /tmp/claude-1000/-home-matiigonzz-Claude/9bc8c381-c8c9-41f6-8082-b296f377a28e/tasks/bhx4oamth.output. You will be notified when it completes. To check interim output, use Read on that file path.
[/external_agent_tool_result]

### 🤖 Codex  <small>2026-09-04 02:38</small>

[external_agent_tool_call: Bash]
description: Wait and check sync output
command: sleep 45; tail -20 /tmp/claude-1000/-home-matiigonzz-Claude/9bc8c381-c8c9-41f6-8082-b296f377a28e/tasks/bhx4oamth.output
[/external_agent_tool_call]

### 🤖 Codex  <small>2026-09-04 02:38</small>

[external_agent_tool_result: error]
<tool_use_error>Blocked: sleep 45 followed by: tail -20 /tmp/claude-1000/-home-matiigonzz-Claude/9bc8c381-c8c9-41f6-8082-b296f377a28e/tasks/bhx4oamth.output. To wait for a condition, use Monitor with an until-loop (e.g. `until <check>; do sleep 2; done`). To wait for a command you started, use run_in_background: true. Do not chain shorter sleeps to work around this block.</tool_use_error>
[/external_agent_tool_result]

### 🤖 Codex  <small>2026-09-04 02:38</small>

[external_agent_tool_call: Bash]
description: Wait for sync to finish and show output
command: until ! pgrep -f sync-skills.sh >/dev/null; do sleep 3; done; tail -15 /tmp/claude-1000/-home-matiigonzz-Claude/9bc8c381-c8c9-41f6-8082-b296f377a28e/tasks/bhx4oamth.output
[/external_agent_tool_call]

### 🤖 Codex  <small>2026-09-04 02:38</small>

[external_agent_tool_result]
Command did not complete within its 300s timeout and was moved to the background (ID: btmxcdns1). Output is being written to: /tmp/claude-1000/-home-matiigonzz-Claude/9bc8c381-c8c9-41f6-8082-b296f377a28e/tasks/btmxcdns1.output. You will be notified when it completes. To check interim output, use Read on that file path.
[/external_agent_tool_result]

### 🤖 Codex  <small>2026-09-04 02:38</small>

[external_agent_tool_call: Bash]
description: Check sync result and verify symlinks
command: tail -20 /tmp/claude-1000/-home-matiigonzz-Claude/9bc8c381-c8c9-41f6-8082-b296f377a28e/tasks/bhx4oamth.output; echo "=== VERIF"; for d in ~/.claude/skills ~/.codex/skills ~/.hermes/skills; do echo "-- $d"; ls "$d" 2>/dev/null | grep -E "chat-primeros|coqueteo|perfil-apps|invitar-a"; done
[/external_agent_tool_call]

### 🤖 Codex  <small>2026-09-04 02:38</small>

[external_agent_tool_result]
==> Importando skills empaquetadas en plugins
    nuevas: 0   actualizadas: 0   ya existían: 39
==> Detectando carpetas de agentes
    55 carpetas destino
==> Enlazando 1100 skills en cada agente
    60208 enlaces   (177 omitidas en Codex por venir ya de sus plugins)
==> Limpiando enlaces rotos
    0 rotos eliminados

Listo. Canónicas: 1100 skills
=== VERIF
-- /home/matiigonzz/.claude/skills
chat-primeros-mensajes
coqueteo-calibrado
invitar-a-salir
perfil-apps-citas
-- /home/matiigonzz/.codex/skills
chat-primeros-mensajes
coqueteo-calibrado
invitar-a-salir
perfil-apps-citas
-- /home/matiigonzz/.hermes/skills
chat-primeros-mensajes
coqueteo-calibrado
invitar-a-salir
perfil-apps-citas
[/external_agent_tool_result]

### 🤖 Codex  <small>2026-09-04 02:38</small>

[external_agent_tool_call: Bash]
description: Clean up background monitor
command: pkill -f "until ! pgrep" 2>/dev/null; echo done
[/external_agent_tool_call]

### 🤖 Codex  <small>2026-09-04 02:38</small>

[external_agent_tool_result: error]
Exit code 144
[/external_agent_tool_result]

### 🤖 Codex  <small>2026-09-04 02:38</small>

Listo. No había nada de esto instalado (revisé las 1096 skills existentes: cero sobre citas o conversación personal), así que escribí 4 skills nuevas y las sincronicé a los 55 agentes con tu `sync-skills.sh`.

## Las 4 skills

| Skill | Para qué |
|---|---|
| [chat-primeros-mensajes](/home/matiigonzz/.agents/skills/chat-primeros-mensajes/SKILL.md) | Aperturas, sostener la charla, revivirla, y diagnóstico de un hilo entero |
| [coqueteo-calibrado](/home/matiigonzz/.agents/skills/coqueteo-calibrado/SKILL.md) | Escalera de 8 escalones de tensión, leer señales, manejar el no |
| [invitar-a-salir](/home/matiigonzz/.agents/skills/invitar-a-salir/SKILL.md) | Cuándo y cómo proponer verse, qué plan, qué escribir antes y después |
| [perfil-apps-citas](/home/matiigonzz/.agents/skills/perfil-apps-citas/SKILL.md) | Fotos, bio, prompts de Hinge, estrategia de swipe |

Cada una tiene 2-3 archivos de referencia con detalle (bancos de aperturas, checklist de fotos, catálogo de señales, planes de primera cita, etc.). Todo escrito en argentino y con voseo.

## Criterio con el que las escribí

Nada de técnicas de "seducción" manipuladoras: sin negging, sin celos fabricados, sin insistir después de un no, sin personajes inventados. Eso no está por mojigatería sino porque no funciona y te quema el círculo social. Lo que sí está: ser específico, leer la calibración, y **ser directo** — que es el consejo que más se subestima.

Dos cosas que las skills van a repetirte mucho porque son los errores más caros:
1. **Si tenés pocos matches, el problema son las fotos, no los mensajes.** Ninguna apertura salva una foto principal mala.
2. **Invitá antes de lo que te resulta cómodo.** Tres semanas de chat sin proponer nada es donde mueren la mayoría de las conversaciones.

Ya están activas en Claude Code, Codex y Hermes. Se disparan solas cuando le preguntes algo del tema, o podés invocarlas por nombre.

### 🧑 Vos  <small>2026-09-04 02:38</small>

y lo puedo usar para el celu??

### 🤖 Codex  <small>2026-09-04 02:38</small>

Buena pregunta — las skills viven en tu compu, así que en el celular no se cargan solas. Dejame ver qué tenés sincronizado.

### 🤖 Codex  <small>2026-09-04 02:38</small>

[external_agent_tool_call: Bash]
description: Check Obsidian vault and sync setup
command: ls ~/OBSIDIAN 2>/dev/null; echo "=== sync?"; ls -a ~/OBSIDIAN | grep -iE "obsidian|git|sync" ; echo "=== remotes"; git -C ~/OBSIDIAN remote -v 2>/dev/null || echo "no es repo git"
[/external_agent_tool_call]

### 🤖 Codex  <small>2026-09-04 02:38</small>

[external_agent_tool_result]
🧠 SEGUNDO CEREBRO.md
00-Inbox
01-Proyectos
02-Areas
03-Recursos
04-Archivo
05-Notas-Zettelkasten
06-Diario
07-Agentes
08-Proyectos-Reales
_attachments
_templates
=== sync?
.obsidian
=== remotes
no es repo git
[/external_agent_tool_result]

### 🤖 Codex  <small>2026-09-04 02:38</small>

[external_agent_tool_call: Bash]
description: Check Obsidian plugins and syncthing
command: ls ~/OBSIDIAN/.obsidian/plugins 2>/dev/null; echo "=== syncthing?"; systemctl --user is-active syncthing 2>/dev/null; ls ~/.config/syncthing 2>/dev/null | head -3
[/external_agent_tool_call]

### 🤖 Codex  <small>2026-09-04 02:38</small>

[external_agent_tool_result]
=== syncthing?
inactive
[/external_agent_tool_result]

### 🤖 Codex  <small>2026-09-04 02:38</small>

No tenés sync configurado en el vault (ni Obsidian Sync, ni Syncthing, ni git), así que las skills están sólo en la compu. La solución práctica es empaquetar todo en un archivo que puedas pegar en la app de Claude del celular como **Proyecto**.

Te armo las dos versiones:

### 🤖 Codex  <small>2026-09-04 02:38</small>

[external_agent_tool_call: Write]
file: /home/matiigonzz/OBSIDIAN/03-Recursos/chat-guia-celular.md
[/external_agent_tool_call]

### 🤖 Codex  <small>2026-09-04 02:38</small>

[external_agent_tool_result]
File created successfully at: /home/matiigonzz/OBSIDIAN/03-Recursos/chat-guia-celular.md (file state is current in your context — no need to Read it back)
[/external_agent_tool_result]

### 🤖 Codex  <small>2026-09-04 02:38</small>

[external_agent_tool_call: Bash]
description: Check file size and clipboard tools
command: wc -c ~/OBSIDIAN/03-Recursos/chat-guia-celular.md; command -v xclip xsel wl-copy 2>/dev/null
[/external_agent_tool_call]

### 🤖 Codex  <small>2026-09-04 02:38</small>

[external_agent_tool_result]
8782 /home/matiigonzz/OBSIDIAN/03-Recursos/chat-guia-celular.md
/usr/bin/wl-copy
[/external_agent_tool_result]

### 🤖 Codex  <small>2026-09-04 02:38</small>

[external_agent_tool_call: Bash]
description: Copy guide to clipboard
command: wl-copy < ~/OBSIDIAN/03-Recursos/chat-guia-celular.md && echo "copiado al portapapeles (8.7 KB)"
[/external_agent_tool_call]

### 🤖 Codex  <small>2026-09-04 02:38</small>

[external_agent_tool_result]
copiado al portapapeles (8.7 KB)
[/external_agent_tool_result]

### 🤖 Codex  <small>2026-09-04 02:38</small>

Sí, pero no automáticamente — las skills son archivos en tu compu y la app del celular no los ve. Te lo dejé listo en un solo archivo:

📄 [chat-guia-celular.md](OBSIDIAN/03-Recursos/chat-guia-celular.md) — las 4 skills condensadas en 8,7 KB, **ya copiado a tu portapapeles**.

## Cómo usarlo en el celu (2 minutos)

1. Abrí la app de **Claude** → **Proyectos** → *Nuevo proyecto*, llamalo "Chat"
2. Andá a **Instrucciones del proyecto** y pegá el contenido
3. Listo: desde el celular abrís ese proyecto, mandás screenshot del chat o pegás la conversación, y te responde con todo ese criterio cargado

Funciona igual en ChatGPT (Proyectos) o Gemini (Gems). En ChatGPT ojo con las *custom instructions* globales: tienen límite de 1500 caracteres, esto no entra — tiene que ser un Proyecto.

## Lo que perdés y lo que no

**Se mantiene:** el criterio completo — escalera de coqueteo, lectura de señales, fórmulas de invitación, checklist de fotos, y el tono argentino.

**Se pierde:** el detalle fino de los archivos de referencia (los bancos largos de aperturas, la tabla de planes de primera cita, el diagnóstico de hilo métrica por métrica). Eso queda sólo en la compu.

## Si querés que se sincronice solo

Tu vault de Obsidian no tiene ningún sync activo (ni Obsidian Sync, ni Syncthing, ni git). Si lo configurás, la nota aparece sola en el Obsidian del celular y podés editarla desde ahí. La opción gratis es **Syncthing** entre la compu y el teléfono. Decime si querés que te lo deje andando.
