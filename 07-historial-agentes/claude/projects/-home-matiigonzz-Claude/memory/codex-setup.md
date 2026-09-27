---
name: codex-setup
description: "Codex CLI en Fedora — lanzador ptyxis, icono propio en hicolor e instrucciones globales en español"
metadata: 
  node_type: memory
  type: project
  originSessionId: d34cdcf7-6b5e-4a1f-b8fb-ddc7834d80aa
  modified: 2026-08-02T02:59:44.150Z
---

Codex CLI 0.145.0 instalado como binario standalone:
`~/.local/bin/codex` → `~/.codex/packages/standalone/current/bin/codex`.
Se abre con [codex.desktop](~/.local/share/applications/codex.desktop), que lanza
`ptyxis --new-window -- ~/.local/bin/codex`.

Hechos no obvios (2026-08-01):

- **El idioma se controla con `~/.codex/AGENTS.md`** (instrucciones globales;
  el binario tiene el error "Failed to read global AGENTS.md instructions from").
  Ahí está la regla de responder siempre en castellano de España. Es el
  equivalente al `~/.gemini/config/GEMINI.md` de [[antigravity-setup]].
- **El icono no salía** porque estaba en `~/.local/share/icons/codex.png`, en la
  raíz — fuera del tema. GTK solo mira `hicolor/<tamaño>/apps/`. Además era un
  libro de 100x100, no el logo. Sustituido por un icono propio (baldosa oscura
  con `>_`, generado con ImageMagick desde SVG) en 32→512 + `scalable`.
  El original quedó en `~/.local/share/icons/codex-libro-antiguo.png.bak`.
- `codex debug-config` **no** imprime y sale: abre la TUI completa y necesita
  TTY real, así que no sirve para verificar config desde un script.

**Cómo aplicarlo:** para cambiar cómo responde Codex, editar
`~/.codex/AGENTS.md`, no `config.toml` (ahí solo hay `trust_level`).
