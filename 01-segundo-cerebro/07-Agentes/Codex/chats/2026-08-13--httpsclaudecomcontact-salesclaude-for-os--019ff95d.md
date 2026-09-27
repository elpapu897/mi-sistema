---
tool: Codex
session_id: 019ff95d-50b7-78b1-80c0-e9765be70e9d
fecha: 2026-08-13 04:24
titulo: "httpsclaudecomcontact salesclaude for oss ayudame"
tags: [chat, agente, codex]
---

# 💬 httpsclaudecomcontact salesclaude for oss ayudame
> **Codex** · 2026-08-13 04:24 · `019ff95d-50b7-78b1-80c0-e9765be70e9d`

---

### 🧑 Vos  <small>2026-08-13 04:24</small>

https://claude.com/contact-sales/claude-for-oss

ayudame si nunca entre a github

### 🤖 Codex  <small>2026-08-13 04:24</small>

[external_agent_tool_call: ToolSearch]
input: {"query":"select:WebFetch","max_results":1}
[/external_agent_tool_call]

### 🤖 Codex  <small>2026-08-13 04:24</small>

[external_agent_tool_result]
[/external_agent_tool_result]

### 🤖 Codex  <small>2026-08-13 04:24</small>

[external_agent_tool_call: Bash]
description: Check environment and git setup
command: ls -la /home/matiigonzz/Claude 2>/dev/null | head -50; echo "---GIT---"; which git; git --version 2>/dev/null; echo "---GH---"; which gh 2>/dev/null || echo "gh no instalado"; echo "---SSH---"; ls ~/.ssh 2>/dev/null || echo "sin ~/.ssh"; echo "---GITCONFIG---"; cat ~/.gitconfig 2>/dev/null || echo "sin gitconfig"
[/external_agent_tool_call]

### 🤖 Codex  <small>2026-08-13 04:24</small>

[external_agent_tool_result]
total 792
drwxr-xr-x. 1 matiigonzz matiigonzz    372 ago  4 00:44 .
drwx------. 1 matiigonzz matiigonzz    598 ago  4 20:58 ..
-rw-r--r--. 1 matiigonzz matiigonzz 101182 jul 26 22:52 2.jpg
-rw-r--r--. 1 matiigonzz matiigonzz 114601 jul 26 22:52 3.jpg
-rw-r--r--. 1 matiigonzz matiigonzz 130465 jul 26 22:52 4.jpg
-rw-r--r--. 1 matiigonzz matiigonzz 131415 jul 26 22:52 5.jpg
-rw-r--r--. 1 matiigonzz matiigonzz 140107 jul 26 22:52 6.jpg
-rw-r--r--. 1 matiigonzz matiigonzz  67621 ago  4 01:18 batalla-real.html
drwxr-xr-x. 1 matiigonzz matiigonzz     38 ago  1 04:12 .claude
-rw-r--r--. 1 matiigonzz matiigonzz  20692 ago  3 23:57 fortnite-3d.html
-rw-r--r--. 1 matiigonzz matiigonzz  24081 ago  3 23:52 fortnite-web.html
-rw-r--r--. 1 matiigonzz matiigonzz   4414 ago  1 03:31 gonvra-guia-ejecucion-rapida.md
-rw-r--r--. 1 matiigonzz matiigonzz  29940 ago  3 23:40 juego-disparos.html
-rw-r--r--. 1 matiigonzz matiigonzz  11433 ago  2 04:34 PROMPT-carrusel-gonvra.md
-rw-r--r--. 1 matiigonzz matiigonzz  10395 ago  2 16:05 PROMPTS-carrusel-chaupelos.md
---GIT---
/usr/bin/git
git version 2.53.0
---GH---
gh no instalado
---SSH---
sin ~/.ssh
---GITCONFIG---
sin gitconfig
[/external_agent_tool_result]

### 🤖 Codex  <small>2026-08-13 04:24</small>

[external_agent_tool_call: WebFetch]
input: {"url":"https://claude.com/contact-sales/claude-for-oss","prompt":"What is this program? What are the eligibility requirements and what information does the form ask for (fields)? Does it require a GitHub repository/organization?"}
[/external_agent_tool_call]

### 🤖 Codex  <small>2026-08-13 04:24</small>

[external_agent_tool_result]
# Claude for Open Source Program

## What is it?
The program offers "6 months of free Claude Max 20x" to open-source contributors as recognition for their ecosystem contributions.

## Eligibility Requirements

The program accepts five categories of contributors:

1. **Maintainers/Library Authors**: Maintain packages with "500 or more dependent repos, 100 or more dependent packages, or 200,000 or more combined monthly downloads" across registries like npm, PyPI, or crates.io

2. **Core Contributors**: Listed committers on major projects (CPython, Rust, Node.js, Apache, CNCF, Kubernetes, Linux kernel, Django, Rails)

3. **Active Contributors**: Have authored "100 or more pull requests merged into repos you don't own in the last 12 months"

4. **Community Builders**: Maintain repos with "20 or more unique external contributors with merged pull requests in the last 12 months"

5. **Critical Infrastructure**: Maintain repositories with an OpenSSF criticality score of 0.4 or above

The page notes: "Don't quite fit? If you maintain something the ecosystem quietly depends on, apply anyway."

## Form Details
The page doesn't specify what fields the application form requests. However, eligibility centers on GitHub/repository metrics and contribution history.
[/external_agent_tool_result]

### 🤖 Codex  <small>2026-08-13 04:24</small>

Te explico primero la verdad sobre ese link, y después te dejo el camino armado.

## Qué es "Claude for OSS"

Son **6 meses de Claude Max 20x gratis** para gente que ya mantiene proyectos open source importantes. Los requisitos son bastante duros — hay que cumplir *al menos uno*:

| Categoría | Requisito |
|---|---|
| Autor de librería | Paquete con +500 repos dependientes, o +200.000 descargas/mes (npm, PyPI, etc.) |
| Core contributor | Estar en la lista de committers de CPython, Rust, Node.js, Kubernetes, Django… |
| Contributor activo | +100 pull requests mergeados en repos ajenos en los últimos 12 meses |
| Community builder | Repo tuyo con +20 contribuidores externos en 12 meses |
| Infraestructura crítica | Score OpenSSF ≥ 0.4 |

Siendo directo: si nunca entraste a GitHub, hoy no calificás para ninguna. No es algo que se resuelva creando la cuenta esta semana — se mide en años de contribuciones. Te lo digo para que no pierdas tiempo llenando el formulario esperando una respuesta.

**Pero** entrar a GitHub igual te sirve muchísimo por otras razones: publicás tus juegos con link jugable gratis, tenés respaldo de tu código, y empezás a construir el historial que algún día sí puede calificar.

## Lo que ya te dejé listo

Te preparé la carpeta del juego para subir, sin tocar tus archivos originales:
