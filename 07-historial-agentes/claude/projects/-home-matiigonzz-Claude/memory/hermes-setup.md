# Hermes Agent — instalación en Fedora (2026-08-14)

**Reemplazó a OpenClaw.** El usuario eligió Hermes por seguridad (backends
sandboxeados) y por el learning loop. OpenClaw quedó **desinstalado por completo**.

**Qué es:** agente de IA self-improving de Nous Research (`NousResearch/hermes-agent`,
MIT, ~230k ★). Multi-canal (Telegram, Discord, Slack, WhatsApp, Signal, CLI) desde
un único proceso gateway.

Versión instalada: **v0.20.1 (2026.8.13)**, vía
`curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash --skip-setup`

## Rutas
| Qué | Dónde |
|---|---|
| Binario | `~/.local/bin/hermes` (agregado al `.bashrc` por el instalador) |
| Código | `~/.hermes/hermes-agent` (Python 3.11 propio, vía uv) |
| Config | `~/.hermes/config.yaml` |
| API keys | `~/.hermes/.env` |
| Datos | `~/.hermes/cron/`, `sessions/`, `logs/`, `memories/` |

Runtime **independiente de nvm**: trae su propio Python/uv, así que cambiar de
versión de Node NO lo rompe (a diferencia de lo que pasaba con Codex/OpenClaw).

## Migración desde OpenClaw
`hermes claw migrate` existe pero **NO se usó tal cual**, por dos razones:
1. Quería copiar 517 archivos de skills a `~/.hermes/skills/openclaw-imports/`
   → **duplicado exacto** de las 258 que ya estaban symlinkeadas.
2. Se negaba a aplicar por 2 conflictos (`soul`, `model-config`) y `--overwrite`
   hubiera pisado la config fresca de Hermes con la vieja de OpenClaw.

Lo único valioso se copió a mano:
`cp ~/.openclaw/workspace/USER.md ~/.hermes/memories/USER.md`
El resto que reportó el dry-run: sin secrets, sin MCP, sin cron, sin mensajería.

## Skills: 347 activas
`254 local + 77 builtin + 16 hub-installed`

- Las 254 locales son symlinks a `~/.agents/skills/` (fuente canónica).
  `sync-skills.sh` las agarra solo: su `find $HOME -maxdepth 2 -type d -name skills`
  matchea `~/.hermes/skills`. **No hay que tocar el script.**
- **Sin truncado silencioso** (a diferencia de OpenClaw, que cortaba en 200):
  no hay `skills.limits` en la config, carga todo.
- Alternativa más limpia a los symlinks, si algún día molestan:
  `skills.external_dirs: [~/.agents/skills]` en `config.yaml` (read-only; la
  creación de skills siempre escribe en `~/.hermes/skills`).

### Carpetas-categoría NO se recorren
`~/.hermes/skills/apple/` y `devops/` son carpetas contenedoras (estilo OpenClaw)
y Hermes **no entra un nivel más**. Symlinkear las anidadas al raíz NO sirvió,
igual no las carga. No importa: las 4 de `apple/` son solo-macOS (Notes, Reminders,
FindMy, iMessage) y `devops/sdlc-review` ya viene como builtin de Hermes.

### Hub de skills
`hermes skills search/install/browse` — **90.636 skills**, 117 oficiales de Nous.
Instalar con `hermes skills install <id> --yes` (el `--yes` es obligatorio fuera de TUI).
Filtrar por confianza con `--source official`; el resto (clawhub, browse-sh, lobehub)
es community y muchas son basura scrapeada de sitios.

Las 16 instaladas el 14-ago: honcho, antigravity-cli, social-media-content-calendar,
meme-generation, baoyu-article-illustrator, concept-diagrams, creative-ideation,
hyperframes, docker-management, watchers, pinggy-tunnel, mcporter, agentmail,
excel-author, pptx-author, one-three-one-rule.

## PENDIENTE (lo tiene que hacer el usuario, pide credenciales)
```
hermes setup
```
El modelo por defecto quedó en `anthropic/claude-opus-4.6` pero **`~/.hermes/.env`
está vacío (es la plantilla)**. Sin eso no arranca ninguna conversación.
Con `hermes model` se cambia de proveedor (Nous Portal, OpenRouter, OpenAI, endpoint propio).

Otros avisos de `hermes doctor` (no bloqueantes): faltan `EXA/TAVILY/FIRECRAWL_API_KEY`
(tool `web`), `XAI_API_KEY` (x_search), `GITHUB_TOKEN` (rate limit del hub, 60 req/hr);
`vision`/`video`/`spotify` sin dependencias de sistema; vulnerabilidades npm en los
workspaces `web` y `ui-tui` que `--fix` no resuelve.

## Interfaz gráfica (el usuario NO quiere terminal)
Hermes tiene **tres** frentes: TUI (`hermes`/`hermes chat`), **dashboard web** y
**app Electron**.

- `hermes dashboard` → web UI en `127.0.0.1:9119` (config, API keys, sesiones).
  Bind loopback, HTTP 200 verificado. `--no-open` para no abrir navegador,
  `--status` / `--stop` para manejarlo. Es el reemplazo de la Control UI de OpenClaw.
  **A diferencia de OpenClaw, la URL no lleva token**: al ser loopback entra directo.
- `hermes serve` → mismo puerto 9119 pero headless (backend JSON-RPC/WebSocket
  para la app de escritorio y clientes remotos). No abre UI.
- `hermes desktop` (alias `hermes gui`) → app Electron real. La primera vez
  **instala deps npm y compila** el artefacto desempaquetado (tarda). **Sin probar aún.**

### Lo que quedó (14-ago-2026) — la app Electron es LA interfaz
El usuario comparó con tutoriales de YouTube y el dashboard web **no se parece**:
el chat del dashboard es una versión embebida y recortada
(`__HERMES_DASHBOARD_EMBEDDED_CHAT__=true`). **La UI de los tutoriales es la app
Electron.** No había ningún problema de CSS ni de logo: son dos UI distintas.

Se compiló con `hermes desktop --build-only` → binario en
`~/.hermes/hermes-agent/apps/desktop/release/linux-unpacked/Hermes`

**Tres trampas, todas resueltas:**
1. **Sandbox de Electron**: la primera ejecución pide `sudo` para dejar
   `chrome-sandbox` setuid root. Sin terminal no puede pedir la contraseña y
   **aborta en silencio**. Lo corrió el usuario:
   `sudo chown root:root <ruta>/chrome-sandbox && sudo chmod 4755 <ruta>/chrome-sandbox`
   (NO usar `--no-sandbox`: el usuario eligió Hermes justamente por seguridad).
2. **El lanzador NO debe usar el wrapper** `hermes desktop`, porque reintenta el
   sudo y muere. `Exec=` apunta **directo al binario** `linux-unpacked/Hermes`.
   Verificado con `gtk-launch hermes` (que es lo que hace GNOME al clickear).
3. **Favoritos de GNOME**: borrar el `.desktop` no alcanza — `openclaw.desktop`
   seguía clavado en `gsettings get org.gnome.shell favorite-apps` como ícono
   fantasma. Se sacó y se agregó `hermes.desktop` en su lugar.

Los `ERROR ... wayland_frame_manager ... buggy presentation feedback` en el log
son **ruido cosmético** de Electron en GNOME/Wayland, no rompen nada.

Se eliminó `~/.local/bin/hermes-ui` y su perfil de Brave: quedó obsoleto y solo
confundía al usuario con la ventana vieja del dashboard. El dashboard web sigue
disponible con `hermes dashboard` para config/API keys.

### Idioma — OJO: dashboard y desktop NO comparten traducciones
- **Dashboard web**: 20 idiomas, `es` incluido (`web/src/i18n/es.ts`). Sin problema.
- **App Electron**: upstream trae **solo 5** (`en, zh, zh-hant, ja, ar`). El usuario
  veía "inglés y cuatro cosas en chino" — era literal, **español no existía**.
  Hay **5 PRs abiertos sin mergear** en NousResearch/hermes-agent agregando `es`.

**Solución aplicada (14-ago-2026):** se parcheó local con el PR **#86195**
(+3175/-4, 4 archivos: `apps/desktop/src/i18n/{es.ts,catalog.ts,languages.ts,types.ts}`).
Aplicó limpio con `git apply` sobre el commit c83061b. Backup del i18n original en
`/tmp/i18n-backup`. Después: `hermes desktop --build-only --force-build`.
Verificado: "Español" quedó en `apps/desktop/dist/assets/i18n-*.js`.

### ⚠️ El parche de español ROMPÍA la UI — arreglado con fallback (16-ago)
La traducción del PR está desactualizada respecto al código: claves que en inglés
son **funciones** (reciben parámetros) quedaron como **texto plano** en español.
Al renderizarlas la app moría con pantalla azul:
`Something broke in the interface — r.titlebar.layoutEditorTitle is not a function`.

Auditoría (en.ts tiene 354 funciones, es.ts 346): **2 mal tipadas**
(`layoutEditorTitle`, `commitPlaceholder`) y **5 ausentes** (`removeConfirmDesc`,
`alreadyInstalled`, `toolCallCount`, `deleteDesc`, `turnDuration`).

**Arreglo (mejor que parchear una por una):** se reescribió
`apps/desktop/src/i18n/catalog.ts` con `withEnglishFallback(en, locale)`, que
recorre el catálogo inglés y **solo acepta el valor traducido si es del mismo
tipo**; si no, usa el inglés. Se aplica a **todos** los idiomas (zh, ja, ar
también), así que ninguna traducción de la comunidad puede volver a tirar la UI.
Aparte se convirtieron a función las 2 claves mal tipadas, para no perder el español.

⚠️ NO tocar el `Icon=` del `.desktop`: debe apuntar a
`apps/desktop/assets/icon.png` (el logo oficial). El usuario se dio cuenta al
toque cuando se cambió por los iconos generados en hicolor y le molestó.

⚠️ **`hermes update` va a pisar el parche.** Si tras actualizar vuelve el inglés,
rebajar el diff: `curl -sL https://github.com/NousResearch/hermes-agent/pull/86195.diff`
→ `git apply` → rebuild.

### ✅ SOLUCIÓN DEFINITIVA al "no abre" (16-ago-2026)
Tras `hermes update` la app dejó de abrir. Causa: **cada rebuild regenera
`chrome-sandbox` sin el setuid**, y el wrapper `hermes desktop` intenta `sudo`,
no puede pedir contraseña sin terminal y **muere en silencio**. Volver a correr
el `sudo chmod 4755` a mano sería un parche eterno (se rompe en cada update).

**Fix real:** Fedora tiene user namespaces habilitados
(`user.max_user_namespaces = 61174`) ⇒ Electron puede usar el **sandbox de
namespaces** y NO necesita el helper setuid. Se lanza con
**`--disable-setuid-sandbox`** (¡OJO: NO es `--no-sandbox`, sigue aislado;
si no hubiera sandbox disponible Electron ni arrancaría`).

Se creó **`~/.local/bin/hermes-app`**, al que apunta `hermes.desktop`. El script:
1. **Se auto-repara el `.desktop`** si un build lo pisó con el wrapper.
2. Compila la app si falta el binario (instalación nueva).
3. Lanza con `--disable-setuid-sandbox`, sin sudo ni contraseña, log en
   `~/.hermes/logs/desktop.log`.

⇒ Ya no hace falta tocar nada después de un `hermes update`. Verificado:
0 procesos con `--no-sandbox`. Aparte, `stt.language` venía en `en` y se puso en **`es`**
(y `stt.openai.language`): el usuario **habla por dictado**, con inglés le
transcribía cualquier cosa.

## Backups por si hay que volver atrás
- `~/openclaw-backup-2026-08-14.tar.gz` (todo `~/.openclaw`, 74K)
- `/tmp/openclaw-backup-2026-08-14.json` (solo la config)
- Hermes escribe restore-points en `~/.hermes/backups/` (restaurables con `hermes import`)

Relacionado: [[skills-setup]], [[antigravity-setup]], [[codex-setup]].
