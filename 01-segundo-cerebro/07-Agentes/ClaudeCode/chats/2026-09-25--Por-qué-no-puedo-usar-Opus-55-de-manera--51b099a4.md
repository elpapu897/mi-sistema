---
tool: ClaudeCode
session_id: 51b099a4-46f1-4b7e-afa5-c93613d95dcb
fecha: 2026-09-25 23:44
titulo: "Por qué no puedo usar Opus 55 de manera local y so"
tags: [chat, agente, claudecode]
---

# 💬 Por qué no puedo usar Opus 55 de manera local y so
> **ClaudeCode** · 2026-09-25 23:44 · `51b099a4-46f1-4b7e-afa5-c93613d95dcb`

---

### 🧑 Vos  <small>2026-09-25 23:44</small>

¿Por qué no puedo usar Opus 5.5 de manera local y solo me deja usar desde la nube?

### 🤖 Claude  <small>2026-09-25 23:44</small>

Voy a revisar tu instalación local antes de responder, así te digo la causa concreta y no una genérica.

### 🤖 Claude  <small>2026-09-25 23:44</small>

_[usó herramienta: Bash]_

### 🤖 Claude  <small>2026-09-25 23:44</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-09-25 23:44</small>

_[resultado de herramienta]_

### 🧑 Vos  <small>2026-09-25 23:44</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-25 23:44</small>

Encontré pistas importantes. Voy a confirmar la causa exacta:

### 🤖 Claude  <small>2026-09-25 23:44</small>

_[usó herramienta: Bash]_

### 🤖 Claude  <small>2026-09-25 23:45</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-09-25 23:45</small>

_[resultado de herramienta]_

### 🧑 Vos  <small>2026-09-25 23:45</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-25 23:45</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-09-25 23:45</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-25 23:45</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-09-25 23:45</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-25 23:45</small>

Ya tengo la respuesta exacta. Un último chequeo para darte la solución correcta:

### 🤖 Claude  <small>2026-09-25 23:45</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-09-25 23:45</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-25 23:46</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-09-25 23:46</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-25 23:46</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-09-25 23:46</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-25 23:46</small>

No es un tema de tu plan ni de tu cuenta. Es un **bloqueo por versión del cliente**, y lo encontré escrito literalmente en tu config local:

```json
{
  "value": "cc-update-required-2",
  "label": "Opus 5.5 (disabled)",
  "description": "Update to 2.1.280+ to use Opus 5.5",
  "disabled": true
}
```

Eso está cacheado en [../.claude.json](../.claude.json) (`additionalModelOptionsCache`) y lo devolvió el servidor de Anthropic **para tu cuenta** — o sea, acceso tenés; lo que falta es la versión.

## El diagnóstico

| Qué | Versión |
|---|---|
| Requisito de Opus 5.5 | **2.1.280+** |
| Claude Code que usa la app de escritorio (esta sesión) | **2.1.219** (binario del 25-jul) |
| CLI suelto en `~/.local/bin/claude` | **2.1.233** (16-ago) |
| Canal `stable` hoy | 2.1.274 ← *tampoco alcanza* |
| Canal `latest` hoy | **2.1.283** ← este sí |

Tres cosas se combinan:

1. **`"autoUpdates": false`** en tu config → tu instalación quedó congelada hace dos meses.
2. **Ni el canal estable alcanza todavía.** 2.1.274 < 2.1.280. Un `claude update` normal te deja igual de afuera. Hay que ir al canal `latest`.
3. **En la nube sí funciona** porque las sesiones remotas corren en la infra de Anthropic, siempre con un build reciente. Por eso el selector te ofrece Opus 5.5 ahí y te lo tacha acá.

Y un detalle extra: estás usando el paquete **no oficial** de Claude Desktop para Linux (`claude-desktop-unofficial.desktop`). Esa app se baja su *propia* copia de Claude Code en `~/.config/Claude/claude-code/<versión>/`, independiente del CLI. Actualizar el CLI no arregla automáticamente la app.

## Cómo destrabarlo

Instalar el canal `latest` (2.1.283):

```bash
curl -fsSL https://claude.ai/install.sh | bash -s latest
```

Reactivar las actualizaciones automáticas para no volver a quedar colgado:

```bash
claude config set -g autoUpdates true
```

Después reiniciá la app de escritorio y verificá qué binario levanta:

```bash
ls -1 ~/.config/Claude/claude-code/
```

Si ahí sigue apareciendo solo `2.1.219`, el cuello de botella es el paquete no oficial: hay que actualizar la app en sí (o esperar a que el mantenedor publique un build nuevo) para que baje un Claude Code ≥ 2.1.280. Mientras tanto, Opus 5.5 te va a seguir funcionando solo en sesiones cloud.

¿Querés que corra la actualización y verifique el resultado?

### 🧑 Vos  <small>2026-09-25 23:47</small>

<bash-input>claude config set -g autoUpdates true</bash-input><bash-stdout>error: unknown option '-g'</bash-stdout><bash-stderr></bash-stderr>

### 🤖 Claude  <small>2026-09-25 23:47</small>

Mi error — esa sintaxis ya no existe en tu versión. Dejame ver la correcta:

### 🤖 Claude  <small>2026-09-25 23:47</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-09-25 23:47</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-25 23:47</small>

`claude config` ya no existe como subcomando — está cayendo al help general. Veamos qué comandos tiene realmente tu versión:

### 🤖 Claude  <small>2026-09-25 23:47</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-09-25 23:48</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-25 23:48</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-09-25 23:48</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-25 23:48</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-09-25 23:48</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-25 23:48</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-09-25 23:48</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-25 23:48</small>

Confirmado: **`claude config` fue eliminado del CLI**. Por eso el `-g` no existe — el comando entero cayó al parser general y Commander se quejó de la opción. Ahora la config vive en los archivos JSON y en el panel `/config` (que solo se abre en una terminal `claude` interactiva, no acá).

Y hay una noticia mejor: no hace falta el `curl`. Tu versión ya trae el comando adecuado.

## Comandos corregidos

Instalar el canal `latest` (2.1.283, el que habilita Opus 5.5):

```bash
claude install latest
```

Verificar que quedó arriba de 2.1.280:

```bash
claude --version
```

Reactivar las actualizaciones automáticas, editando el JSON directo (escritura atómica, el temporal va en el mismo filesystem):

```bash
jq '.autoUpdates = true' ~/.claude.json > ~/.claude.json.tmp && mv ~/.claude.json.tmp ~/.claude.json
```

## Dos advertencias

**1. Cerrá Claude antes de tocar el JSON.** Tenés **25 procesos `claude` corriendo** ahora mismo. Cada uno tiene su copia en memoria de `~/.claude.json` y la reescribe al salir — si editás con todo abierto, el cambio de `autoUpdates` se te pisa. El `claude install latest` sí lo podés correr ya, ese no depende del archivo.

**2. Ojo con `claude update`.** Va al canal *stable* = 2.1.274, que sigue estando por debajo del mínimo 2.1.280. Es la trampa de este caso: el comando "natural" para actualizar no te alcanza. Tiene que ser `install latest`.

Y recordá lo de antes: esto arregla el CLI de `~/.local/bin`. La app de escritorio sigue levantando su propia copia 2.1.219 desde `~/.config/Claude/claude-code/`, así que Opus 5.5 va a aparecer primero en `claude` desde terminal, no necesariamente en la app.

¿Querés que lo corra yo? Puedo hacer el `install latest`, verificar la versión, y dejarte el ajuste del JSON anotado para cuando cierres todo.

### 🧑 Vos  <small>2026-09-25 23:48</small>

<bash-input>claude config set -g autoUpdates true</bash-input><bash-stdout>error: unknown option '-g'</bash-stdout><bash-stderr></bash-stderr>

### 🤖 Claude  <small>2026-09-25 23:49</small>

Ese es el mismo comando de antes — `claude config` no existe en tu versión, así que `-g` nunca va a ser reconocido (¿flecha arriba del historial?).

El equivalente real es editar el JSON:

```bash
jq '.autoUpdates = true' ~/.claude.json > ~/.claude.json.tmp && mv ~/.claude.json.tmp ~/.claude.json
```

Pero eso es lo secundario. Lo que realmente te destraba Opus 5.5 es:

```bash
claude install latest
```

Decime y lo corro yo: hago el `install latest`, verifico con `claude --version` que haya quedado en 2.1.283, y el `autoUpdates` lo dejamos para cuando cierres las sesiones abiertas (si lo tocamos ahora con 25 procesos vivos, te lo pisan al salir).

### 🧑 Vos  <small>2026-09-25 23:51</small>

<bash-input>claude install latest</bash-input><bash-stdout>✔ Claude Code successfully installed!

  Version: 2.1.283

  Location: ~/.local/bin/claude


  Next: Run claude --help to get started</bash-stdout><bash-stderr></bash-stderr>

### 🤖 Claude  <small>2026-09-25 23:51</small>

Instalado. Verifiquemos que el gate quedó liberado de verdad:

### 🤖 Claude  <small>2026-09-25 23:51</small>

_[usó herramienta: Bash]_

### 🤖 Claude  <small>2026-09-25 23:51</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-09-25 23:51</small>

_[resultado de herramienta]_

### 🧑 Vos  <small>2026-09-25 23:51</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-25 23:52</small>

Funcionó. El gate quedó liberado:

| Chequeo | Resultado |
|---|---|
| Versión CLI | **2.1.283** ✅ (antes 2.1.233) |
| ID `claude-opus-5-5` en el binario | Presente ✅ |
| Strings `cc-update-required` | Desaparecidos ✅ |
| App de escritorio | Sigue en **2.1.219** ❌ |

Y un dato lindo que salió del binario nuevo: *"Opus 5.5 (`claude-opus-5-5`), now the default Opus model"*. O sea que ni vas a tener que elegirlo — al seleccionar Opus ya te va a dar el 5.5.

## Dónde lo vas a ver ahora

Abrí una terminal y corré `claude`. Ahí, en el selector de modelos, Opus 5.5 ya tiene que aparecer habilitado (sin el "(disabled)"). Si lo ves tachado el primer segundo, es la lista vieja cacheada en `additionalModelOptionsCache`; se refresca sola al conectar.

**Esta sesión no cambió.** La app de escritorio arrancó con el binario 2.1.219 y no hace hot-swap, así que seguís hablando con el cliente viejo hasta que la reinicies.

## Para que la app también lo tome

En este orden, que importa:

1. Cerrá la app de escritorio y todas las sesiones `claude` (esta incluida).
2. Con todo cerrado, recién ahí:

```bash
jq '.autoUpdates = true' ~/.claude.json > ~/.claude.json.tmp && mv ~/.claude.json.tmp ~/.claude.json
```

3. Reabrí la app y revisá si bajó un build nuevo:

```bash
ls -1 ~/.config/Claude/claude-code/
```

Si después de eso ahí sigue apareciendo solo `2.1.219`, el problema es el paquete no oficial de Linux: trae su copia de Claude Code clavada y hay que actualizar el paquete en sí. Avisame si pasa eso y lo miramos — mientras tanto tenés Opus 5.5 vía terminal.

### 🧑 Vos  <small>2026-09-25 23:52</small>

<bash-input>claude --version</bash-input><bash-stdout>2.1.283 (Claude Code)</bash-stdout><bash-stderr></bash-stderr>

### 🤖 Claude  <small>2026-09-25 23:52</small>

Confirmado, 2.1.283 desde tu shell. El CLI ya está listo para Opus 5.5.

Lo que queda pendiente es solo la app de escritorio (sigue en 2.1.219). Cuando quieras cerrás todo, corrés el `jq` del `autoUpdates` y la reabrís.

Si preferís probar Opus 5.5 ya mismo sin cerrar nada, abrí una terminal aparte y lanzá `claude` — esa sesión arranca con el binario nuevo.

### 🧑 Vos  <small>2026-09-25 23:54</small>

<bash-input>jq '.autoUpdates = true' ~/.claude.json > ~/.claude.json.tmp && mv ~/.claude.json.tmp ~/.claude.json</bash-input><bash-stdout>[No output was captured. The command ran in the terminal pane (tab 0); if it should have printed something, use read_terminal with tab_id "0" to check.]</bash-stdout><bash-stderr></bash-stderr>

### 🤖 Claude  <small>2026-09-25 23:54</small>

Verifico que quedó bien escrito y que el JSON no se corrompió:

### 🤖 Claude  <small>2026-09-25 23:54</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-09-25 23:54</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-25 23:54</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-09-25 23:54</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-25 23:54</small>

Todo limpio:

- **JSON válido** ✅ — parsea sin errores
- **`autoUpdates: true`** ✅
- **55 claves top-level, 60K** — mismo tamaño que antes, no se perdió nada
- **Sin `.tmp` huérfano** ✅

(De paso: tenés un backup propio de Claude Code en `~/.claude.json.backup`, del 13 de agosto, por si alguna vez lo necesitás.)

Queda el riesgo que te mencioné: **hay 24 procesos `claude` vivos**, cada uno con su copia vieja en memoria. Si alguno reescribe el archivo al cerrarse, te vuelve `autoUpdates` a `false`.

Así que después de cerrar la app y todas las sesiones, revalidá con:

```bash
jq '.autoUpdates' ~/.claude.json
```

Si dice `false`, simplemente volvés a correr el `jq` de antes — ahora sin nada abierto, y ahí sí queda firme.

### 🧑 Vos  <small>2026-09-25 23:55</small>

<bash-input>jq '.autoUpdates' ~/.claude.json</bash-input><bash-stdout>true</bash-stdout><bash-stderr></bash-stderr>

### 🤖 Claude  <small>2026-09-25 23:55</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-09-25 23:55</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-25 23:55</small>

Sigue en `true`, pero ojo: **ese chequeo todavía no es el definitivo.**

El archivo se modificó a las 20:54:04 (tu `jq`, hace un minuto y medio) y hay **25 procesos `claude` vivos**. Lo que estás leyendo es simplemente lo que acabás de escribir — ninguno de esos procesos se cerró todavía, así que ninguno tuvo oportunidad de pisarlo.

La prueba real es la misma línea, pero **después** de cerrar la app de escritorio y todas las sesiones. Ahí vas a saber si el valor sobrevivió.

Cuando reabras, el combo que confirma que quedó todo en orden:

```bash
jq '.autoUpdates' ~/.claude.json && ls -1 ~/.config/Claude/claude-code/
```

Eso te dice dos cosas de una: si el `autoUpdates` aguantó, y si la app finalmente se bajó un Claude Code nuevo (si aparece algo distinto a `2.1.219`, ganaste — Opus 5.5 también en la app).

### 🧑 Vos  <small>2026-09-25 23:56</small>

<bash-input>jq '.autoUpdates' ~/.claude.json && ls -1 ~/.config/Claude/claude-code/</bash-input><bash-stdout>true
2.1.219</bash-stdout><bash-stderr></bash-stderr>

### 🤖 Claude  <small>2026-09-25 23:56</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-09-25 23:56</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-25 23:56</small>

Pará — **esa prueba todavía no corrió.** Mirá el uptime:

```
claude-desktop-unofficial   mié sep 23 19:26:32 2026   etime: 2-01:29:52
```

La app viene corriendo hace **2 días y hora y media**. No la reiniciaste, así que el `2.1.219` es exactamente lo esperado: nunca tuvo ocasión de chequear si hay build nuevo. Y el `true` sigue siendo solo lo que escribimos.

Antes de que hagas el ciclo de reinicio, dejame ver si el paquete no oficial siquiera tiene lógica para bajarse una versión nueva — así no perdés el viaje:

### 🤖 Claude  <small>2026-09-25 23:56</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-09-25 23:56</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-25 23:56</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-09-25 23:56</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-25 23:56</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-09-25 23:57</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-25 23:57</small>

El `rc` no resuelve públicamente. Un último grep, que puede darte un atajo:

### 🤖 Claude  <small>2026-09-25 23:57</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-09-25 23:57</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-25 23:57</small>

`CLAUDE_CODE_LOCAL_BINARY` tiene muy buena pinta. Veamos cómo se usa:

### 🤖 Claude  <small>2026-09-25 23:57</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-09-25 23:57</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-25 23:57</small>

Encontré algo importante. Un último dato para armarte la instrucción exacta:

### 🤖 Claude  <small>2026-09-25 23:57</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-09-25 23:57</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-25 23:58</small>

Acá está la respuesta de fondo, y no es buena para el plan de "reiniciar y listo":

**La app tiene la versión clavada.** Dentro del `app.asar` (del 25 de julio) hay una variable `buildPinVersion` fijada en `2.1.219`:

```js
_.info(`[CCD] Initialized with version ${this.buildPinVersion}`)
```

No es que esté desactualizada esperando un update — está *pinneada*. Reiniciar no te va a traer 2.1.283, y el `autoUpdates: true` que pusimos no aplica a la copia de la app. Ese cambio sirve para tu CLI, no para esto.

## Pero hay una puerta trasera

En el mismo bundle encontré esto:

```js
async initLocalBinary(t) {
  await W.access(t, Y.constants.X_OK),
  this.localBinaryPath = t,
  _.warn(`[CCD] LOCAL OVERRIDE: Using local binary at ${t}`)
}
```

La app **lee `CLAUDE_CODE_LOCAL_BINARY` del entorno** y, si la ruta es ejecutable, la usa en lugar del binario pinneado. Tu `~/.local/bin/claude` es 2.1.283 y pasa el chequeo `X_OK`. O sea: podés forzar a la app a usar el binario nuevo.

Creás un override de usuario del lanzador (no toca nada del sistema, y se revierte borrando el archivo):

```bash
mkdir -p ~/.local/share/applications && cat > ~/.local/share/applications/claude-desktop-unofficial.desktop <<EOF
[Desktop Entry]
Name=Claude
Exec=env CLAUDE_CODE_LOCAL_BINARY=$HOME/.local/bin/claude /usr/bin/claude-desktop-unofficial %u
Icon=claude-desktop-unofficial
Type=Application
Terminal=false
Categories=Office;Utility;
MimeType=x-scheme-handler/claude;
StartupWMClass=com.anthropic.Claude
EOF
```

Después cerrás la app del todo y la reabrís **desde el menú de aplicaciones** (no desde la terminal, para que tome el `.desktop` nuevo):

```bash
pkill -f claude-desktop-unofficial
```

⚠️ Ese `pkill` mata esta conversación. Es esperable — nos vemos del otro lado.

Al reabrir, verificás en la terminal de la app:

```bash
echo "$AI_AGENT | $CLAUDE_CODE_EXECPATH"
```

Si dice `claude-code_2-1-283_agent` y apunta a `~/.local/bin/claude`, el override funcionó y Opus 5.5 ya te tiene que aparecer en el selector. Si sigue diciendo `2-1-219`, el pin ganó y ahí sí toca esperar al mantenedor del paquete.

¿Te creo el archivo yo así lo dejás listo antes de reiniciar?

### 🧑 Vos  <small>2026-09-26 00:00</small>

<bash-input>echo "$AI_AGENT | $CLAUDE_CODE_EXECPATH"</bash-input><bash-stdout> |</bash-stdout><bash-stderr></bash-stderr>

### 🤖 Claude  <small>2026-09-26 00:00</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-09-26 00:01</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-26 00:01</small>

El dato clave: hay un proceso de la app con **39 segundos** de vida. Algo se relanzó. Déjame ver exactamente qué:

### 🤖 Claude  <small>2026-09-26 00:01</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-09-26 00:01</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-26 00:01</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-09-26 00:01</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-26 00:01</small>

El override **se está aplicando**: el lanzador nuevo (pid 681058, ~1 minuto de vida) tiene la variable. Ahora, la prueba definitiva — ¿la app realmente la está usando?

### 🤖 Claude  <small>2026-09-26 00:01</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-09-26 00:01</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-26 00:01</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-09-26 00:01</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-26 00:01</small>

Ojo acá — el log dice `Initialized with version 2.1.219` y **no aparece** la línea `LOCAL OVERRIDE`. Pero necesito saber si eso es de la instancia nueva o de la vieja:

### 🤖 Claude  <small>2026-09-26 00:01</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-09-26 00:01</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-26 00:02</small>

Ahora sí es concluyente. Y encontré **por qué** falló:

### 🤖 Claude  <small>2026-09-26 00:02</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-09-26 00:02</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-26 00:02</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-09-26 00:02</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-26 00:02</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-09-26 00:02</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-26 00:02</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-09-26 00:02</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-26 00:02</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-09-26 00:02</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-26 00:03</small>

Diagnóstico cerrado. El override se aplicó a medias y sé exactamente dónde se corta:

| Eslabón | Estado |
|---|---|
| `.desktop` de usuario creado | ✅ (21:00) |
| App relanzada | ✅ (instancia nueva, pid 681058) |
| Launcher bash tiene la variable | ✅ `tiene_var=1` |
| **Proceso Electron la recibe** | ❌ **`tiene_var=0`** |
| Log `[CCD] LOCAL OVERRIDE` | ❌ **0 ocurrencias** |
| Log real a las 21:00:24 | `Initialized with version 2.1.219` |

La variable muere entre el script de bash y Electron. Y el log dice por qué:

```
[CCD] Resolved 25 login-shell env vars
```

**La app no confía en el entorno que hereda.** Lo descarta y lo reconstruye ejecutando un *login shell*. Por eso inyectar la variable en el `Exec=` del `.desktop` no sirve: se evapora en ese paso. La puerta de entrada es tu config de login shell — tu shell es `/bin/bash` y tenés `~/.bash_profile`.

```bash
echo 'export CLAUDE_CODE_LOCAL_BINARY="$HOME/.local/bin/claude"' >> ~/.bash_profile
```

Comprobá que un login shell efectivamente la exporta (es literalmente lo que hace la app):

```bash
bash -lc 'echo $CLAUDE_CODE_LOCAL_BINARY'
```

Si eso imprime la ruta, reiniciás la app y el veredicto está acá:

```bash
grep -aE "LOCAL OVERRIDE|Initialized with version" ~/.config/Claude/logs/main.log | tail -3
```

Aparece `[CCD] LOCAL OVERRIDE: Using local binary at /home/matiigonzz/.local/bin/claude` → ganaste, Opus 5.5 también en la app.

**Siendo honesto sobre las chances:** puede que `initLocalBinary` esté además detrás de algún flag interno que no llegué a ver — el fragmento del bundle estaba minificado y truncado. Si tras el login shell la línea `LOCAL OVERRIDE` sigue sin aparecer, el pin gana y no hay más que rascar del lado del usuario: queda esperar que el mantenedor del paquete no oficial suba el `buildPinVersion`.

Mientras tanto Opus 5.5 lo tenés operativo en `claude` desde terminal, que es donde igual corre mejor. El `.desktop` que creaste podés dejarlo, es inofensivo.

### 🧑 Vos  <small>2026-09-26 02:03</small>

<bash-input>echo 'export CLAUDE_CODE_LOCAL_BINARY="$HOME/.local/bin/claude"' >> ~/.bash_profile</bash-input><bash-stdout>[No output was captured. The command ran in the terminal pane (tab 0); if it should have printed something, use read_terminal with tab_id "0" to check.]</bash-stdout><bash-stderr></bash-stderr>

### 🤖 Claude  <small>2026-09-26 02:03</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-09-26 02:04</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-26 02:04</small>

Todas las precondiciones cumplidas:

- **Línea agregada una sola vez** ✅ (sin duplicados)
- **El login shell la exporta** ✅ → `/home/matiigonzz/.local/bin/claude`
- **La ruta es ejecutable y responde 2.1.283** ✅

Ese último punto es el que importa: `initLocalBinary` hace exactamente un `access(ruta, X_OK)` antes de aceptar el override. Acabás de pasar esa misma prueba a mano.

Ya no queda nada por preparar. Solo reiniciar:

```bash
pkill -f claude-desktop-unofficial
```

Reabrís desde el menú (ahora da igual el `.desktop`, la variable viaja por el login shell) y el veredicto sale de acá:

```bash
grep -aE "LOCAL OVERRIDE|Initialized with version" ~/.config/Claude/logs/main.log | tail -3
```

- Sale `[CCD] LOCAL OVERRIDE: Using local binary at /home/matiigonzz/.local/bin/claude` → funcionó, Opus 5.5 en la app.
- Sale solo `Initialized with version 2.1.219` otra vez → el pin gana, y ahí cerramos el tema: Opus 5.5 por terminal y a esperar al mantenedor.

⚠️ El `pkill` corta esta conversación. Si querés, pegame después la salida de ese `grep` en un chat nuevo y te digo cómo quedó.

### 🧑 Vos  <small>2026-09-26 02:04</small>

<bash-input>bash -lc 'echo $CLAUDE_CODE_LOCAL_BINARY'</bash-input><bash-stdout>/home/matiigonzz/.local/bin/claude</bash-stdout><bash-stderr></bash-stderr>

### 🤖 Claude  <small>2026-09-26 02:04</small>

Confirmado, mismo resultado que el chequeo anterior: el login shell exporta la ruta correcta.

Todo listo. Lo único que falta es el reinicio:

```bash
pkill -f claude-desktop-unofficial
```

Reabrís desde el menú y mirás el log. Nos vemos del otro lado.

### 🧑 Vos  <small>2026-09-26 02:04</small>

<bash-input>grep -aE "LOCAL OVERRIDE|Initialized with version" ~/.config/Claude/logs/main.log | tail -3</bash-input><bash-stdout>2026-09-25 21:00:24 [info] [CCD] Initialized with version 2.1.219
2026-09-25 21:00:25 [info] [CCD] Initialized with version 2.1.219
2026-09-25 21:00:25 [info] [CCD] Initialized with version 2.1.219</bash-stdout><bash-stderr></bash-stderr>

### 🤖 Claude  <small>2026-09-26 02:04</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-09-26 02:04</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-26 02:04</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-09-26 02:04</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-26 02:04</small>

La app **acaba de reiniciarse** (23:04:30, hace 13 segundos) — el grep anterior lo hiciste un segundo antes del arranque, por eso mostraba las líneas viejas de las 21:00. Momento de la verdad:

### 🤖 Claude  <small>2026-09-26 02:04</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-09-26 02:04</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-26 02:05</small>

Resultado definitivo. Y el log revela algo muy específico — mirá los timestamps:

### 🤖 Claude  <small>2026-09-26 02:05</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-09-26 02:05</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-26 02:05</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-09-26 02:05</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-26 02:06</small>

Caso cerrado, y con una causa muy precisa. Mirá el orden de los eventos:

```
23:04:32  [CCD] Initialized with version 2.1.219   ← acá lee CLAUDE_CODE_LOCAL_BINARY
23:04:33  [CCD] Initialized with version 2.1.219
23:04:34  [CCD] Resolved 26 login-shell env vars   ← acá recién llega tu variable
```

**Tu variable sí llegó** — la cuenta pasó de **25 a 26** env vars, ese +1 es exactamente la línea que agregaste al `.bash_profile`. Prueba irrefutable de que el login shell funcionó.

Pero llega **dos segundos tarde**. El componente que decide qué binario usar ya se inicializó en el segundo :32, leyendo un `process.env` donde la variable todavía no existía (por eso el `environ` de Electron daba 0). Para cuando la app resuelve el entorno del login shell, la decisión ya está tomada y el pin ya ganó. El mismo orden se repite en los dos reinicios, 21:00 y 23:04.

O sea: **el override es código inalcanzable por esta vía.** No hay `LOCAL OVERRIDE` en todo el log, nunca. No es algo que puedas arreglar desde tu lado — es un problema de orden de inicialización en el build de la app.

## Qué ganaste igual

| | Antes | Ahora |
|---|---|---|
| CLI en terminal | 2.1.233 | **2.1.283** ✅ |
| Opus 5.5 por terminal | Bloqueado | **Disponible** (y es el Opus por defecto) |
| `autoUpdates` | `false` | **`true`** ✅ sobrevivió al reinicio de las 23:04 |
| App de escritorio | 2.1.219 | 2.1.219 ❌ |

Y la respuesta a tu pregunta original quedó clara: **nunca fue tu plan ni tu cuenta.** Era un gate de versión del cliente, y la nube simplemente corre una versión más nueva que la que tenías instalada.

## Lo que queda

Para usar Opus 5.5 hoy: `claude` desde una terminal. En la app vas a seguir con 2.1.219 hasta que el mantenedor del paquete no oficial publique un build con el `buildPinVersion` actualizado — vale la pena revisar el repo cada tanto.

La línea del `.bash_profile` dejala: es inofensiva y si algún día arreglan el orden de inicialización, empieza a funcionar sola. El `.desktop` de `~/.local/share/applications/` ya no aporta nada; si querés limpiarlo:

```bash
rm ~/.local/share/applications/claude-desktop-unofficial.desktop
```
