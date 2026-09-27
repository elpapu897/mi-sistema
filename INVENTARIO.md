# Inventario

Qué se respaldó, dónde va al restaurar, y **qué se dejó afuera de cada carpeta y
por qué**. La última columna es la importante: es la que explica por qué 113 GB
se convirtieron en 26,85.

---

## Resumen

| | Cantidad |
|---|--:|
| Home original | 113 GB |
| **Respaldado** | **26,85 GB** |
| Descartado a propósito | ~86 GB |
| Archivos | 19.046 |
| Notas `.md` | 5.555 |
| Skills únicas | 1.235 |
| Symlinks mapeados | 3.154 |
| Repos de terceros catalogados | 15 |
| Archivos en Git LFS | 1.678 (24,85 GB) |
| Archivos en git normal | 17.349 (2,01 GB) |

---

## Mapa origen → destino

Esta tabla es la versión legible de [`scripts/MAPA.tsv`](scripts/MAPA.tsv), que
es lo que leen los scripts de restauración.

### 01 · Segundo cerebro

| Repo | Destino | Peso | Qué es |
|---|---|--:|---|
| `01-segundo-cerebro` | `~/OBSIDIAN` | 17 MB | Vault completo: 389 archivos, 5.555 notas contando el resto del repo. Incluye `.obsidian/` con plugins, temas y atajos. |

**Excluido:** `.trash/` (la papelera de Obsidian).

### 02 · Agentes

| Repo | Destino | Peso | Qué es |
|---|---|--:|---|
| `02-agentes/claude` | `~/.claude` | 41 MB | `settings.json`, `CLAUDE.md`, 72 skills propias, config de plugins |
| `02-agentes/agents-skills` | `~/.agents` | 47 MB | **La biblioteca canónica: 1.125 skills.** Acá apuntan los 3.134 symlinks de los tres agentes. |
| `02-agentes/codex` | `~/.codex` | 41 MB | Config, prompts, 1 skill propia, 946 symlinks a la biblioteca |
| `02-agentes/gemini` | `~/.gemini` | 34 MB | Config e historial de Gemini / Antigravity |
| `02-agentes/hermes` | `~/.hermes` | 128 MB | Config, `SOUL.md`, memorias, 37 skills propias, `state.db` |
| `02-agentes/kimi-code` | `~/.kimi-code` | 52 KB | Config y sesiones |
| `02-agentes/opencode` | `~/.opencode` | 14 KB | Solo `package.json` y el lock |

**Excluido:** `projects/`, `telemetry/`, `shell-snapshots/`, `statsig/`,
`cache/`, backups `.bak` de settings, y los binarios `bin/`, `node/`, `lsp/`,
`profiles/` (176 MB de OpenCode, 163 MB de Kimi, 279 MB de Hermes). Todos se
reinstalan. `~/.hermes/hermes-agent` (4,9 GB) es un clon de terceros: está en el
manifiesto.

> **Por qué la biblioteca está una sola vez:** Claude, Codex y Hermes comparten
> las mismas skills vía symlinks relativos (`../../.agents/skills/X`). Copiar el
> contenido de cada uno habría triplicado 47 MB y, peor, habría hecho que editar
> una skill no se reflejara en los otros agentes.

### 03 · Proyectos propios

| Repo | Destino | Peso | Qué es |
|---|---|--:|---|
| `03-proyectos/g` | `~/g` | 6,6 MB | App Next.js. **De 494 MB a 6,6 MB** sacando `node_modules` y `.next`. |
| `03-proyectos/claude-workspace` | `~/Claude` | 1,5 GB | Workspace: gonvra, gonvra-ads, yt-nicho, migracion-vps, MCPs propios, experimentos |
| `03-proyectos/roblox-broll-edit` | `~/proyectos/roblox-broll-edit` | 738 MB | Proyecto de edición (incluye el render final y el source) |
| `03-proyectos/skills-para-claude-ai` | `~/skills-para-claude-ai` | 19 MB | 1.139 skills empaquetadas en `.zip` + manifiesto CSV |
| `03-proyectos/Documents` | `~/Documents` | 52 MB | Documentos de Codex |
| `03-proyectos/Documentos` | `~/Documentos` | 277 KB | Proyectos de Blackmagic / DaVinci |

**Excluido:** `node_modules`, `.next`, `dist`, `build`, `.venv`, `__pycache__`.
Los 4 repos de terceros que vivían dentro de `~/Claude` (`mcp/fbads`,
`mcp-servers/google-flow-browser-mcp`, `pinguclean`, `threejs-skills`) están en
el manifiesto — solo `fbads` traía 242 MB de `.venv` con dos copias del driver de
Playwright.

### 04 · Negocio GONVRA

| Repo | Destino | Peso | Qué es |
|---|---|--:|---|
| `04-negocio-gonvra/tiendas` | `~/tiendas` | 51 MB | Tiendas, auditoría 2026, landing, handoffs, fichas de producto |
| `04-negocio-gonvra/backups` | `~/GONVRA-BACKUPS` | 400 MB | Backups diarios del 23 al 27 de septiembre, con el tema de Shopify |
| `04-negocio-gonvra/publicar` | `~/GONVRA-PUBLICAR` | 20 MB | Pipeline de publicación: descartado / crudos / pendiente / aprobado / publicado |

> Los `tema-shopify.tgz` de los días 25 y 26 son idénticos en peso (143 MB cada
> uno). Se respaldan los dos igual: ocupan poco al lado de la media y desduplicar
> backups a mano es cómo se pierden cosas.

### 05 · Media (Git LFS)

| Repo | Destino | Peso | Qué es |
|---|---|--:|---|
| `05-media/planetamati-edit` | `~/planetamati-edit` | 16 GB | Proyecto de video completo |
| `05-media/grabaciones-flexclip` | `~/Descargas/grabaciones-flexclip` | 4,5 GB | Las 7 grabaciones de pantalla originales |
| `05-media/videos-sueltos` | `~/Vídeos/sueltos` | 404 MB | Los 3 `.mp4` que estaban tirados en la raíz del home |
| `05-media/Vídeos` | `~/Vídeos` | 29 MB | Carpeta Vídeos |
| `05-media/Imágenes` | `~/Imágenes` | 47 MB | Carpeta Imágenes |
| `05-media/Escritorio` | `~/Escritorio` | 1,5 MB | Escritorio |

Dentro de `planetamati-edit`:

| Subcarpeta | Peso | Reemplazable? |
|---|--:|---|
| `out/` | 5,1 GB | **No.** El video final (28m58s, 1080p), el preview y el timeline XML para Resolve. |
| `clips/` | 11 GB | Sí, en teoría: son los 49 cortes transcodificados a DNxHR desde el original. Regenerarlos requiere el crudo y varias horas de máquina. Se respaldan. |
| `motion/` | 643 MB | **No.** El proyecto de Remotion con 13 piezas animadas en ProRes 4444 con alfa. |
| `audio/` | 150 MB | **No.** Audio y transcripción. |
| `frames/`, `sheets/` | 9 MB | Sí, pero pesan nada. |

**Excluido:** `motion/node_modules` (527 MB, se recupera con `npm install`).

### 06 · Dotfiles

| Repo | Destino | Peso |
|---|---|--:|
| `06-dotfiles` | `~/` y `~/.config/` | 1,5 MB |

Incluye `.bashrc`, `.bash_profile`, `.profile`, `.zshrc`, `.tmux.conf`,
`.config/gtk-3.0`, `.config/gtk-4.0`, `.config/nvim`, `.config/autostart`, y
`.ssh/config` más las claves **públicas**.

**Excluido:** las claves SSH privadas (van cifradas).
También saqué el symlink `gtk-dark.css` porque colisionaba con `gtk-Dark.css` en
Windows, que no distingue mayúsculas. El archivo real está; el enlace lo
reconstruye `rehacer-symlinks.sh` en Linux.

### 07 · Historial de agentes

| Repo | Destino | Peso | Qué es |
|---|---|--:|---|
| `07-historial-agentes/claude/projects` | `~/.claude/projects` | 457 MB | Conversaciones de Claude Code + **la auto-memoria (`MEMORY.md`)** |
| `07-historial-agentes/codex/sessions` | `~/.codex/sessions` | 680 MB | Sesiones de Codex (una llega a 241 MB) |
| `07-historial-agentes/codex/generated_images` | `~/.codex/generated_images` | 110 MB | Imágenes generadas |
| `07-historial-agentes/codex/thread_history_1.sqlite` | `~/.codex/thread_history_1.sqlite` | 235 MB | Base de threads |

> Esto está **en claro**. Es la transcripción de todo lo conversado con los
> agentes. Por eso el repo es privado. Ver [CREDENCIALES.md](CREDENCIALES.md).

### 99 · Secretos

| Repo | Peso |
|---|--:|
| `99-secretos/secretos.tar.gpg` | ~50 KB |

Cifrado AES-256 con `--s2k-count 65011712` (endurecido contra fuerza bruta).
Contenido detallado en [CREDENCIALES.md](CREDENCIALES.md).

---

## Lo que NO se respaldó

### Regenerable con un comando

| Qué | Peso aprox. | Cómo vuelve |
|---|--:|---|
| `node_modules` (todos los proyectos) | ~1,5 GB | `npm install` |
| `.cache` | 15 GB | Se rehace solo |
| `.var` (datos de apps Flatpak) | 16 GB | Al reinstalar las apps |
| `.npm`, `.nvm`, `.bun`, `.deno` | 5,3 GB | Al instalar los runtimes |
| `.rustup`, `.cargo` | 693 MB | `rustup install` |
| `.local`, `.config` (partes de apps) | ~30 GB | Al reinstalar |
| `.venv`, `__pycache__` | ~250 MB | `pip install -r` |
| Binarios de agentes (`bin/`, `node/`, `lsp/`) | ~700 MB | Al reinstalar cada agente |

### Repos de terceros

15 repos, ~1 GB de código ajeno. URL y commit exacto en
[03-proyectos/REPOS-EXTERNOS.md](03-proyectos/REPOS-EXTERNOS.md).
Se recuperan con `bash scripts/reclonar-terceros.sh`.

### Descargas descartables (~7 GB)

| Qué | Peso | Por qué no |
|---|--:|---|
| `TomexOS 10 21H2 LTSC Pro V1.1 x64.iso` | 2,2 GB | Es el sistema al que estás migrando. Ya lo tenés. |
| 3 APKs de Minecraft | 3,2 GB | Se vuelven a descargar |
| `codex-desktop-linux` (copia en Descargas) | 1,9 GB | Duplicado de `~/codex-desktop-linux`, y es un repo de terceros |
| `ventoy-1.1.17-livecd.iso` | 187 MB | Se vuelve a descargar |
| `node-v24.21.0-linux-x64` | 204 MB | Y además no sirve en Windows |

> Las **grabaciones de pantalla** que estaban en `Descargas` sí se respaldaron
> (4,5 GB): son material propio, no algo descargable.

### Aplicaciones

| Qué | Peso | Por qué no |
|---|--:|---|
| `~/Aplicaciones/antigravity` | 496 MB | Aplicación instalada. Se reinstala, y encima es un build de Linux que en Windows no corre. |
| `~/codex-desktop-linux` | 1,4 GB | Repo de terceros + build de Linux |
| `~/.mac-theme-build` | 219 MB | 4 repos de temas de terceros, y son temas de GTK: en Windows no aplican |
| `~/open-generative-ai` | 1,5 GB | Repo de terceros |

---

## Verificaciones que se corrieron

| Chequeo | Resultado |
|---|---|
| `git check-ignore` sobre los 6 archivos de credenciales | 6/6 bloqueados |
| `git check-attr` sobre los 69 archivos de más de 90 MB | 69/69 en LFS, 0 fugas |
| Archivos sobre el límite duro de 100 MB de GitHub | 0 sin LFS |
| Caracteres prohibidos en Windows (`< > : " \| ? *`) | 0 |
| Nombres reservados de Windows (`CON`, `AUX`, `COM1`…) | 0 |
| Rutas de más de 260 caracteres | 0 (la más larga: 164) |
| Colisiones por mayúsculas/minúsculas | 1, corregida |
| Nombres con punto o espacio final | 0 |
| `restaurar.sh --dry-run` | 27 entradas, 0 omitidas |
| Destinos que se pisaban entre sí | 2 encontrados, corregidos |
