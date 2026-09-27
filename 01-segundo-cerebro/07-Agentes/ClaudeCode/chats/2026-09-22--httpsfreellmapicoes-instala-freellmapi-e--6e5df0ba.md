---
tool: ClaudeCode
session_id: 6e5df0ba-7e11-4f58-9fb7-814f5d659f24
fecha: 2026-09-22 05:09
titulo: "httpsfreellmapicoes instala freellmapi en mi orden"
tags: [chat, agente, claudecode]
---

# 💬 httpsfreellmapicoes instala freellmapi en mi orden
> **ClaudeCode** · 2026-09-22 05:09 · `6e5df0ba-7e11-4f58-9fb7-814f5d659f24`

---

### 🧑 Vos  <small>2026-09-22 05:09</small>

https://freellmapi.co/es/
instala freellmapi en mi ordenador

### 🤖 Claude  <small>2026-09-22 05:09</small>

Voy a investigar primero qué es ese servicio antes de instalar nada.

### 🤖 Claude  <small>2026-09-22 05:09</small>

_[usó herramienta: Bash]_

### 🤖 Claude  <small>2026-09-22 05:09</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-09-22 05:09</small>

_[resultado de herramienta]_

### 🧑 Vos  <small>2026-09-22 05:09</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-22 05:10</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-09-22 05:10</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-22 05:10</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-09-22 05:10</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-22 05:10</small>

Es un router self-hosted open source (MIT, 27.9k ⭐). Veo el README para la instalación real.

### 🤖 Claude  <small>2026-09-22 05:10</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-09-22 05:10</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-22 05:10</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-09-22 05:10</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-22 05:10</small>

Fedora 44, Node 22, bun 1.4, **sin Docker**. Reviso la doc de instalación y si hay build para Linux.

### 🤖 Claude  <small>2026-09-22 05:10</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-09-22 05:10</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-22 05:10</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-09-22 05:10</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-22 05:10</small>

Opciones reales para Fedora: RPM nativo (app de escritorio), build desde código fuente, o Podman. Verifico un par de cosas antes de proponer.

### 🤖 Claude  <small>2026-09-22 05:10</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-09-22 05:10</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-22 05:10</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-09-22 05:10</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-22 05:10</small>

Todo verificado. Hay tres caminos válidos y cambian bastante el resultado, así que te pregunto antes de tocar nada:

### 🤖 Claude  <small>2026-09-22 05:11</small>

_[usó herramienta: AskUserQuestion]_

### 🧑 Vos  <small>2026-09-22 05:15</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-22 05:15</small>

Dale: Podman rootless + autoarranque. Primero leo el instalador oficial para replicar exactamente su configuración (rutas, volúmenes, variables).

### 🤖 Claude  <small>2026-09-22 05:15</small>

_[usó herramienta: Bash]_

### 🤖 Claude  <small>2026-09-22 05:15</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-09-22 05:15</small>

_[resultado de herramienta]_

### 🧑 Vos  <small>2026-09-22 05:15</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-22 05:15</small>

Replico exactamente la configuración oficial, pero con Podman. Paso 1: directorio y clave de cifrado.

### 🤖 Claude  <small>2026-09-22 05:16</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-09-22 05:16</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-22 05:16</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-09-22 05:16</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-22 05:16</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-09-22 05:16</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-22 05:16</small>

Imagen descargada. Ahora creo el servicio systemd de usuario (Quadlet, la forma nativa de Podman 5) para el autoarranque:

### 🤖 Claude  <small>2026-09-22 05:16</small>

_[usó herramienta: Write]_

### 🧑 Vos  <small>2026-09-22 05:16</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-22 05:16</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-09-22 05:16</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-22 05:16</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-09-22 05:17</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-22 05:17</small>

Funcionando. Ahora el arranque a nivel boot (sin esperar al login) y reviso el primer arranque:

### 🤖 Claude  <small>2026-09-22 05:17</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-09-22 05:17</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-22 05:17</small>

Instalado y corriendo. Verifico que sobreviva un reinicio del servicio (prueba real del autoarranque):

### 🤖 Claude  <small>2026-09-22 05:17</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-09-22 05:17</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-22 05:18</small>

Listo. FreeLLMAPI quedó instalado y corriendo en tu Fedora.

## Qué instalé

No usé el one-liner oficial porque **exige Docker** y vos tenés Podman. Lo repliqué a mano con la misma configuración (imagen, volumen, puerto, clave de cifrado), en modo **rootless** y sin tocar nada del sistema:

| Cosa | Dónde |
|---|---|
| Dashboard / API | http://localhost:3001 (solo loopback) |
| Clave de cifrado | [.env](../freellmapi/.env) (`chmod 600`) |
| Servicio autoarranque | [freellmapi.container](../.config/containers/systemd/freellmapi.container) |
| Base de datos (keys cifradas) | volumen `freellmapi-data` |

**Verificado:** servicio `active`, `/api/ping` responde OK, sobrevive reinicios, y el catálogo ya sincronizó solo (295 modelos nuevos aplicados). Activé **linger**, así que arranca en el boot sin esperar a que inicies sesión.

## Tu próximo paso (2 minutos)

Abrí http://localhost:3001 en el navegador de esta máquina. Como es el primer arranque te pide crear la cuenta — desde este equipo no necesita código, pero si lo pidiera es `5CDCAQVB6H`.

Después, en la página **Keys**: cargá las API keys gratuitas de los proveedores que quieras (Google, Groq, Cerebras, Mistral, Cohere…). **Ojo: sin ninguna key de proveedor el router no sirve para nada** — él solo enruta, no regala tokens propios. Arriba de esa misma página está tu *unified key*, que es el único token que van a ver tus apps.

Para engancharlo a Claude Code, una vez que tengas esa key:

```bash
npx freellmapi setup-claude --url http://localhost:3001 --api-key TU_UNIFIED_KEY
```

## Mantenimiento

Ver logs en vivo:

```bash
podman logs -f freellmapi
```

Actualizar a la última versión:

```bash
podman pull ghcr.io/tashfeenahmed/freellmapi:latest && systemctl --user restart freellmapi
```

Parar / arrancar:

```bash
systemctl --user stop freellmapi
```

## Tres cosas que te conviene saber

1. **Hacé backup de `~/freellmapi/.env`.** Si perdés ese `ENCRYPTION_KEY`, la base queda ilegible y tenés que recargar todas las keys de proveedores a mano.
2. **No pagues los $19 todavía.** El router es gratis y open source para siempre; el premium solo compra el catálogo *en vivo*. Tu instalación gratis recibe el snapshot mensual, o sea que un modelo nuevo te llega 30 días más tarde. Probalo un mes y decidí después si esa demora te molesta.
3. **No lo expongas a internet.** Lo dejé atado a `127.0.0.1` a propósito: es un proxy de un solo usuario protegido apenas por un token, y el propio proyecto lo declara "solo experimentación personal". Aplican los términos de servicio de cada proveedor cuyas free tiers apiles.

### 🧑 Vos  <small>2026-09-26 02:51</small>

<bash-input>systemctl --user stop freellmapi</bash-input><bash-stdout>Warning: The unit file, source configuration file or drop-ins of freellmapi.service changed on disk. Run 'systemctl --user daemon-reload' to reload units.</bash-stdout><bash-stderr></bash-stderr>

### 🤖 Claude  <small>2026-09-26 02:52</small>

El aviso es cosmético de Quadlet, pero lo verifico en vez de asumirlo.

### 🤖 Claude  <small>2026-09-26 02:52</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-09-26 02:52</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-26 02:52</small>

El servicio quedó en **failed**, no en un `inactive` limpio. Eso no es normal para un stop. Diagnostico antes de tocar nada.

### 🤖 Claude  <small>2026-09-26 02:52</small>

_[usó herramienta: Bash]_

### 🤖 Claude  <small>2026-09-26 02:52</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-09-26 02:52</small>

_[resultado de herramienta]_

### 🧑 Vos  <small>2026-09-26 02:52</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-26 02:53</small>

Encontré la causa real, y no es solo cosmética:

```
StopSignal SIGTERM failed to stop container in 10 seconds, resorting to SIGKILL
→ exit 137
```

La app **no atiende el SIGTERM** dentro del plazo de 10s por defecto de Podman, así que la matan a la fuerza. Eso hace dos cosas: deja la unidad en `failed`, y **mata el proceso con la base SQLite abierta**. Voy a medir si es que ignora la señal o si solo necesita más tiempo, con un contenedor descartable para no tocar tus datos.

### 🤖 Claude  <small>2026-09-26 02:53</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-09-26 02:54</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-26 02:54</small>

Confirmado: **ignora el SIGTERM por completo** — con 60s de plazo tampoco sale, lo matan igual con SIGKILL. Es un bug del proyecto (no tiene handler de apagado). Darle más tiempo no sirve de nada, solo alarga cada parada. Verifico la clave correcta de Quadlet y limpio el test.

### 🤖 Claude  <small>2026-09-26 02:54</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-09-26 02:54</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-26 02:55</small>

El `man` no está instalado; valido con el generador de Quadlet en modo dry-run antes de aplicar. Primero edito:

### 🤖 Claude  <small>2026-09-26 02:55</small>

_[usó herramienta: Read]_

### 🧑 Vos  <small>2026-09-26 02:55</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-26 02:55</small>

_[usó herramienta: Write]_

### 🧑 Vos  <small>2026-09-26 02:55</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-26 02:55</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-09-26 02:55</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-26 02:55</small>

Ambas claves válidas y aplicadas. Ahora el ciclo completo de verificación:

### 🤖 Claude  <small>2026-09-26 02:55</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-09-26 02:55</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-26 02:56</small>

Arreglado: parada en 3s y termina en `inactive`, no `failed`. Como levanté antes el tema de SQLite, lo verifico en serio en tu base real:

### 🤖 Claude  <small>2026-09-26 02:56</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-09-26 02:56</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-26 02:56</small>

Permiso denegado por el user namespace de rootless. Entro con `podman unshare`:

### 🤖 Claude  <small>2026-09-26 02:56</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-09-26 02:56</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-26 02:56</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-09-26 02:56</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-26 02:57</small>

Base intacta y ahora entiendo el cuadro completo.

## Qué pasaba

No era cosmético, pero tampoco era lo que yo sospechaba al principio. Lo medí en vez de suponerlo:

- **La app ignora SIGTERM.** Con 60s de plazo tampoco sale — siempre termina en SIGKILL (exit 137). Es un bug del proyecto: no tiene handler de apagado.
- Con `SuccessExitStatus` vacío, systemd interpretaba ese 137 como fallo, así que **todo `stop` intencional dejaba la unidad en `failed`**.
- Encima, cada parada (y cada apagado de la máquina) se colgaba 10s esperando una respuesta que nunca iba a llegar.

**Me corrijo en una cosa que dije antes:** insinué que el SIGKILL podía dañar la base. Lo verifiqué y el riesgo era bajo — la base está en modo **WAL**, que está diseñado justamente para sobrevivir muertes abruptas. `PRAGMA integrity_check` da `ok`, 32 tablas, 314 modelos. No se perdió nada.

## Qué cambié

Dos líneas en [freellmapi.container](../.config/containers/systemd/freellmapi.container), validadas con el generador de Quadlet en dry-run antes de aplicarlas:

| Línea | Para qué |
|---|---|
| `StopTimeout=3` | No esperar 10s a una señal que la app nunca atiende |
| `SuccessExitStatus=137 143` | Que un stop intencional no quede como `failed` |

**Verificado** con un ciclo completo: arranca → `/api/ping` OK → para en **3s** (antes 10) → queda en `inactive`, ya no en `failed`.

## Estado actual

El servicio quedó **parado**, que es como vos lo dejaste. Para levantarlo:

```bash
systemctl --user start freellmapi
```

Dos cosas que te conviene saber:

1. **Parado no es desactivado.** Como activamos el autoarranque, en el próximo reinicio va a volver a levantar solo. Si lo que querés es que no arranque más, hay que sacarle la sección `[Install]` al archivo `.container` y hacer `daemon-reload` — con `systemctl disable` no alcanza, porque es una unidad generada.

2. **Todavía no tiene ninguna key de proveedor cargada** (`api_keys: 0 filas`). O sea que nunca llegaste a completar el setup en el dashboard. Tal como está, el router funciona pero no puede enrutar a ningún lado. Si querés retomarlo: arrancalo, entrá a http://localhost:3001 y cargá al menos una key gratuita (Google o Groq son las más rápidas de obtener).

¿Querés que te deje el autoarranque desactivado hasta que decidas si lo vas a usar?
