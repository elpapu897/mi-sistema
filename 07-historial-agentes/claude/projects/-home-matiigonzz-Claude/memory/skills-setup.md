# Skills y plugins compartidos entre todos los agentes

El usuario quiere que TODAS sus skills/guías estén disponibles en TODOS sus agentes.
Pidió explícitamente "absolutamente todas" incluso sabiendo el costo de contexto.

## Estado final (13-ago-2026): 257 skills canónicas

## Arquitectura
`~/.agents/skills/<nombre>/SKILL.md` = **fuente canónica** (copias reales).
El resto son **symlinks relativos**: `~/.claude/skills/<n> -> ../../.agents/skills/<n>`
Se sincroniza con: **`~/Claude/scripts/sync-skills.sh`** (idempotente, tiene `--dry-run`).
Correrlo de nuevo después de actualizar plugins.

## Quién lee qué (verificado leyendo los binarios con `strings`)
| Agente | Lee de |
|---|---|
| Claude Code | `~/.claude/skills/` |
| OpenCode | auto-carga `~/.claude/skills/` y `~/.agents/skills/` → **nada que hacer** |
| kimi-code | `~/.claude/skills`, `~/.codex/skills`, `~/.kimi-code/skills`, `~/.kimi/skills` |
| Codex CLI | `~/.codex/skills/` + las skills de sus plugins habilitados |
| Gemini/Antigravity | NO soporta skills; solo `~/.gemini/config/GEMINI.md` |

Agentes realmente instalados: claude, opencode, kimi, gemini + codex (bundle en
`/opt/codex-desktop/resources/codex`; **no hay binario `codex` en el PATH**).

## ANTI-DUPLICADOS (importante)
Codex ya carga solo las 177 skills de sus marketplaces `claude-cowork` y
`local-desktop-app-uploads`. Si además se le enlazan en `~/.codex/skills` las ve
DOS veces. Por eso `~/.codex/skills` tiene solo **80** (las propias) y las otras
177 le llegan vía plugins → 257 efectivas. El script ya aplica esta regla
(variable `CODEX_OWN_SOURCES`). Las skills importadas de plugins quedan marcadas
con un archivo `.from-plugin` que guarda su ruta de origen.

## De dónde salieron las 257
- ~70 de marketing/negocio preexistentes + 10 remotion + 10 threejs + find-skills = 80
- **177 importadas** del marketplace `claude-cowork` de Codex
  (`~/.codex/plugins/cache/claude-cowork`, 23 plugins: anthropic-skills, base44,
  wix, bio-research, small-business, sales, finance, legal, marketing, data,
  engineering, design, product-management, operations, HR, etc.)
- 39 se saltearon por colisión de nombre (se conservó la que ya existía)

## Costo de contexto
~25.000 tokens de metadata (name+description) en cada sesión de cada agente.
El usuario lo aceptó a sabiendas. Si alguna vez va lento, la palanca es sacar
base44 (28), wix (20) y bio-research (6), que no usa.

## Plugins
- **Codex ya tiene ~30 plugins habilitados** (5 marketplaces, ver `~/.codex/config.toml`),
  incluidos los 2 de Claude. Codex está mejor equipado que Claude Code en plugins.
- **Claude Code CLI solo tiene 2**: ui-ux-pro-max y watch (`local-desktop-app-uploads`).
- NO se le agregó el marketplace `claude-cowork` a Claude Code porque:
  1. su manifiesto está en `.agents/plugins/marketplace.json` y Claude exige
     `.claude-plugin/marketplace.json` → `claude plugin marketplace add` falla;
  2. duplicaría las 177 skills ya sincronizadas.
- Esos plugins son casi puros contenedores de skills: **0 servidores MCP**, solo
  unos pocos `commands/agents/hooks` (pdf-viewer, product-management, nano-banana).
  O sea que sincronizando las skills ya se capturó el valor real.
- OpenCode usa plugins npm/TS (`~/.config/opencode/package.json`) → formato
  incompatible, no se pueden portar.

## Instalador de skills nuevas
```bash
npx --yes skills@latest add <owner>/<repo> --global --all
```
Trampas: **no instala en `~/.codex/skills`** aunque reporta éxito; crea ~56 carpetas
`~/.<agente>/skills/` de agentes que el usuario no tiene (inofensivo, ensucia el home);
Eve y PromptScript siempre fallan. `gh` no está instalado: usar `git clone`.
Después de instalar algo nuevo, correr `sync-skills.sh`.

## Hermes Agent (2026-08-14) — reemplazó a OpenClaw
OpenClaw fue **desinstalado** (npm, servicio systemd, lanzador, iconos y `~/.openclaw`).
Ver [[hermes-setup]] para el detalle.

`~/.hermes/skills/` tiene los 258 symlinks (los creó el instalador `npx skills@latest`
el 13-ago, antes de que Hermes existiera en la máquina). `sync-skills.sh` lo agarra
solo con su `find $HOME -maxdepth 2 -type d -name skills` → **no hay que editar el script**.

**Hermes NO trunca** (OpenClaw cortaba en 200 en silencio, ver historial en git):
no tiene `skills.limits`, carga las 254 locales + 77 builtin + las del hub = 347.

Dos detalles:
- Las carpetas-categoría (`apple/`, `devops/`) **no se recorren**: Hermes no baja un
  nivel. Se pierden 5 skills anidadas, todas irrelevantes (4 son solo-macOS y
  `sdlc-review` ya es builtin).
- Trae **hub propio** con 90.636 skills: `hermes skills search --source official`
  para filtrar solo las 117 confiables de Nous.

## Expansión masiva (2026-08-14): 258 → 1096 skills canónicas
El usuario pidió "todo, sin filtrar". Se clonaron 19 repos de GitHub en
`/tmp/skillrepos` (1481 SKILL.md) y se instalaron **833 nuevas** en `~/.agents/skills`
(647 eran duplicados entre repos — se pisan muchísimo entre sí; ante colisión gana
la que ya existía). Cada skill importada tiene un archivo `.from-repo` con su origen.

Top aportantes: alirezarezvani/claude-skills (419), aaron-he-zhu/aaron-marketing-skills
(117), SamurAIGPT/Generative-Media-Skills (72), wondelai/skills (61),
nowork-studio/notfair-plugin (47), Eronred/aso-skills (40), softaworks/agent-toolkit (40).

Totales tras `sync-skills.sh`: **Hermes 1134** (1041 local + 77 builtin + 16 hub),
Claude Code 1091, Codex 914. ~60.000 symlinks en 55 carpetas destino.
⚠️ Costo de contexto estimado: pasó de ~22k a **~90k tokens** de metadata por sesión.
Si algún agente va lento, la palanca es borrar de `~/.agents/skills` las que tengan
`.from-repo` de los repos menos útiles y re-sincronizar.

### Skills propias destiladas de los historiales (2026-08-14)
Se minaron los chats con `/tmp/mine_chats.py` (860 mensajes reales del usuario:
292 de Claude Code + 568 de Codex; los 13GB de `~/.config/Claude` son caché, el
corpus útil son 0,6 MB). Temas dominantes: agentes/skills, imagen/diseño,
juego/gamedev, GONVRA/Shopify, ads, redes/video.

Se crearon 4 skills nuevas — **clave: las notas de memoria las lee SOLO Claude Code,
las skills las leen todos los agentes**, así que esto lleva el contexto a Hermes y Codex:
- `dictado-rioplatense` — cómo interpretar su voz mal transcripta (glosario
  Open Cloud→OpenClaw, Germes→Hermes, Gombra→GONVRA, "coso"=comodín, vale lo último).
- `gonvra-tienda` — manual operativo de la tienda (duplicar tema, truco de
  themeFilesCopy→assets→curl, trampas de schema/md5, envíos, pagos).
- `gonvra-meta-ads` — IDs, mínimo $1.497/día, qué está bloqueado por API, crear en PAUSA.
- `feedback-visual-iterativo` — traducir "más gordo"/"trucho", verificar con captura
  antes de decir listo, logos oficiales nunca dibujados a mano.
