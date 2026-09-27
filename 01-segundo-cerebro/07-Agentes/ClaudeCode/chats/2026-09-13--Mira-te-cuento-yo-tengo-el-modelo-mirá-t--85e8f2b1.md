---
tool: ClaudeCode
session_id: 85e8f2b1-657c-451b-aa66-946441e02c71
fecha: 2026-09-13 21:35
titulo: "Mira te cuento yo tengo el modelo mirá tengo Codex"
tags: [chat, agente, claudecode]
---

# 💬 Mira te cuento yo tengo el modelo mirá tengo Codex
> **ClaudeCode** · 2026-09-13 21:35 · `85e8f2b1-657c-451b-aa66-946441e02c71`

---

### 🧑 Vos  <small>2026-09-13 21:35</small>

Mira, te cuento, yo tengo el modelo, mirá, tengo Codex, pero Linux. Creo que está les de vuelta, por ese sí, los Codex. La interfaz de Codex en ChatGPT, pero que tenga básicamente el modelo Astra, porque no me aparece me aparece todavía el GPT cinco seis. -- no va a cuadrilear. Entonces, tenés que cuidado con eso, por favor

### 🤖 Claude  <small>2026-09-13 21:36</small>

Pará, no te seguí bien — el dictado llegó bastante cortado y no quiero adivinar y mandarme una macana.

Lo que sí te aclaro de entrada, para que no haya malentendido:

- **Yo soy Claude (Claude Code)**, no Codex. No puedo cambiar qué modelo te aparece en la interfaz de Codex/ChatGPT — eso depende de lo que OpenAI habilite en tu cuenta.
- **"Astra" y "GPT-5.6"**: no te los puedo confirmar desde acá. Puede que existan y yo no los tenga registrados, pero no te voy a inventar specs ni disponibilidad de modelos que no puedo verificar.
- Esta sesión, además, está configurada como **agente de generación de imágenes** (Gemini / Nano Banana), por si entraste al chat equivocado.

Decime cuál es la idea:

### 🤖 Claude  <small>2026-09-13 21:36</small>

_[usó herramienta: AskUserQuestion]_

### 🧑 Vos  <small>2026-09-13 21:36</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-13 21:37</small>

Dale. Antes de teorizar, chequeo qué tenés instalado realmente:

### 🤖 Claude  <small>2026-09-13 21:37</small>

_[usó herramienta: Bash]_

### 🤖 Claude  <small>2026-09-13 21:37</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-09-13 21:37</small>

_[resultado de herramienta]_

### 🧑 Vos  <small>2026-09-13 21:37</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-13 21:37</small>

Ahí hay data. Veo un `config.toml.bak-astra` y un `models_cache.json` — miro ambos:

### 🤖 Claude  <small>2026-09-13 21:37</small>

_[usó herramienta: Read]_

### 🤖 Claude  <small>2026-09-13 21:37</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-09-13 21:37</small>

_[resultado de herramienta]_

### 🧑 Vos  <small>2026-09-13 21:37</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-13 21:37</small>

Config ya apunta a `gpt-6-astra`. Ahora veo qué dice el cache de modelos que devuelve el backend:

### 🤖 Claude  <small>2026-09-13 21:37</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-09-13 21:37</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-13 21:37</small>

Encontré el problema. Profundizo un toque antes de explicarte:

### 🤖 Claude  <small>2026-09-13 21:37</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-09-13 21:37</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-13 21:37</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-09-13 21:37</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-13 21:37</small>

_[usó herramienta: Read]_

### 🤖 Claude  <small>2026-09-13 21:37</small>

_[usó herramienta: Read]_

### 🧑 Vos  <small>2026-09-13 21:37</small>

_[resultado de herramienta]_

### 🧑 Vos  <small>2026-09-13 21:37</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-13 21:38</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-09-13 21:38</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-13 21:38</small>

Listo, ya sé qué pasa. **No es Linux, y tu config está bien escrita — el problema es del lado del servidor.**

## Lo que encontré

**Tu config pide Astra:**
```
model = "gpt-6-astra"
model_reasoning_effort = "xhigh"
```
en [.codex/config.toml:1](.codex/config.toml:1)

**Pero el backend no lo está ofreciendo.** El listado de modelos se refrescó hoy a las 21:34 y devuelve exactamente 6 entradas:

| slug | visible | descripción |
|---|---|---|
| `gpt-5.6-sol` | sí | Reliable agentic workhorse for everyday tasks |
| `gpt-5.6-terra` | sí | Balanced agentic coding model |
| `gpt-5.6-luna` | sí | Fast and affordable agentic coding model |
| `gpt-5.5` | sí | Previous-generation |
| `gpt-reserve` | oculto | — |
| `codex-auto-review` | oculto | — |

Busqué `astra`, `gpt-6` y `gpt6` en el archivo entero: **0 coincidencias.** No es cache viejo — se bajó hoy.

## El diagnóstico

Le estás pidiendo un slug que el servidor no sirve para tu cuenta → Codex lo ignora y cae en un modelo del listado. **Por eso ves GPT-5.6.** No hay nada que tocar localmente que lo traiga de vuelta.

Además hay rastros de que **sí lo tuviste el 7 de septiembre**:
- `config.toml.bak-astra` (7/sep 16:28) — backup hecho justo antes de cambiar a Astra, y adentro dice `model = "gpt-5.6-sol"`
- `[tui.model_availability_nux] gpt-6-astra = 1` — el aviso de "modelo nuevo disponible" que te mostró la TUI

O sea: apareció, lo configuraste, y después dejó de estar en el listado. Tu plan es **Plus**.

## Lo que NO te puedo confirmar

No sé si Astra se retiró, si pasó a requerir un tier más alto, o si es un rollout escalonado que te va a volver. No tengo forma de verificar eso desde acá y no te lo voy a inventar.

## Un detalle aparte que vale la pena

Hay desprolijidad de versiones: el CLI en tu PATH es `0.154.0-alpha.6`, el cache lo escribió un cliente `0.150.0`, y la app de escritorio usa su propio binario en `/opt/codex-desktop/resources/codex`. El listado de modelos **puede variar según versión de cliente**, así que es la única palanca local que quizás mueva algo.

### 🤖 Claude  <small>2026-09-13 21:38</small>

_[usó herramienta: AskUserQuestion]_

### 🧑 Vos  <small>2026-09-13 21:40</small>

_[resultado de herramienta]_

### 🧑 Vos  <small>2026-09-13 21:40</small>

[Request interrupted by user]

### 🧑 Vos  <small>2026-09-13 21:40</small>

gh repo clone ilysenko/codex-desktop-linux descargame este repositorio de linux

### 🤖 Claude  <small>2026-09-13 21:40</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-09-13 21:40</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-13 21:40</small>

`gh` no está instalado. Voy con `git clone` directo:

### 🤖 Claude  <small>2026-09-13 21:40</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-09-13 21:40</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-13 21:40</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-09-13 21:40</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-13 21:41</small>

Clonado en `/home/matiigonzz/codex-desktop-linux`. Y ojo, que esto conecta directo con lo de antes — tu Codex corre desde `/opt/codex-desktop/`, que es justo lo que instala este repo:

### 🤖 Claude  <small>2026-09-13 21:41</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-09-13 21:41</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-13 21:41</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-09-13 21:41</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-13 21:41</small>

Acá hay algo importante. El repo **parchea el selector de modelos**:

### 🤖 Claude  <small>2026-09-13 21:41</small>

_[usó herramienta: Read]_

### 🤖 Claude  <small>2026-09-13 21:41</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-09-13 21:41</small>

_[resultado de herramienta]_

### 🧑 Vos  <small>2026-09-13 21:41</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-13 21:41</small>

Clonado y listo. Y de paso, **el repo confirma el diagnóstico de antes**.

## El clone

| | |
|---|---|
| Path | `/home/matiigonzz/codex-desktop-linux` |
| Branch | `main` |
| Último commit | `f445a44` — hoy 13/sep — *"Fix updater self-termination during deb upgrades (#1430)"* |
| Tamaño | 18M |

Repo activo, con commits de hoy mismo.

## Lo que encontré adentro sobre tu problema

Hay un feature opt-in llamado **`model-picker-default-presets`** y el ejemplo del README usa literalmente tu caso:

```json
{ "model": "gpt-6-astra", "effort": "medium", "default": true }
```

Así que `gpt-6-astra` es un slug real, no algo que inventaste. Pero leé la sección *Runtime fallback* de [README.md:71](codex-desktop-linux/linux-features/model-picker-default-presets/README.md:71):

> At runtime, the feature keeps only presets **whose model is present in the current account catalog**.
> - if every configured pair is unavailable, the complete upstream Default configuration is returned unchanged.

Y arriba del todo aclara que **no** toca *"account entitlements, workspace policy, or upstream Ultra/XHigh gates"*.

**Traducción:** ni siquiera este port puede hacer aparecer Astra si tu catálogo de cuenta no lo tiene. Y tu catálogo, refrescado hoy 21:34, no lo tiene. El parche filtra el preset y cae al Default de upstream → GPT-5.6. Exactamente el comportamiento que estás viendo.

## Una pista que sí vale explorar

Hay otro feature, **`api-key-model-visibility`**, que maneja qué modelos se ven cuando autenticás por API key en vez de cuenta ChatGPT. Tu `auth.json` tiene **las dos cosas**: un `OPENAI_API_KEY` y los tokens de ChatGPT (plan Plus).

Si tu cuenta de API tuviera acceso a Astra, ese camino podría exponerlo aunque el catálogo de ChatGPT Plus no lo liste. **No te lo puedo confirmar** — no sé qué modelos habilita tu API key y no voy a hacer llamadas con tu credencial sin que me lo pidas.

## Antes de instalar nada

No corrí `install.sh` ni `make install-native` — eso te reemplaza el `/opt/codex-desktop/` que estás usando ahora mismo, y no lo voy a hacer sin que me lo digas explícitamente.

Si querés, puedo:
- Leer el `install.sh` y el `README.md` principal y contarte qué hace exactamente antes de que decidas
- Consultar qué modelos lista tu API key (con tu OK, usando la credencial que ya tenés en `auth.json`)
- Revisar si tu `/opt/codex-desktop` actual salió de este repo y en qué versión está respecto de `main`

### 🧑 Vos  <small>2026-09-13 21:42</small>

instalalo igual bldo

### 🤖 Claude  <small>2026-09-13 21:42</small>

Dale, pero leo el `install.sh` primero — no voy a correr a ciegas un script que te pisa `/opt/codex-desktop` mientras lo estás usando.

### 🤖 Claude  <small>2026-09-13 21:42</small>

_[usó herramienta: Read]_

### 🧑 Vos  <small>2026-09-13 21:42</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-13 21:42</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-09-13 21:42</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-13 21:43</small>

Pará — dos cosas importantes que cambian el panorama:

### 🤖 Claude  <small>2026-09-13 21:43</small>

_[usó herramienta: Bash]_

### 🤖 Claude  <small>2026-09-13 21:43</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-09-13 21:43</small>

_[resultado de herramienta]_

### 🧑 Vos  <small>2026-09-13 21:43</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-13 21:43</small>

Bien, esto **corrige lo que te advertí antes** — me pasé de precavido:

- El guard de "app corriendo" chequea solo si corre **desde `$INSTALL_DIR`**, no cualquier codex
- Y `INSTALL_DIR` por defecto es `codex-desktop-linux/codex-app`, **no `/opt/codex-desktop`**

O sea: instalación paralela, tu Codex actual no se toca. Chequeo deps y arranco:

### 🤖 Claude  <small>2026-09-13 21:43</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-09-13 21:43</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-13 21:43</small>

Todo presente. Arranco la instalación en background (descarga el `.deb` oficial y parchea, puede tardar varios minutos):

### 🤖 Claude  <small>2026-09-13 21:43</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-09-13 21:43</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-13 21:43</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-09-13 21:43</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-13 21:43</small>

_[usó herramienta: Read]_

### 🧑 Vos  <small>2026-09-13 21:43</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-13 21:43</small>

Anda bien — resolvió el paquete oficial desde el índice APT firmado. Espero a que termine:

### 🤖 Claude  <small>2026-09-13 21:43</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-09-13 21:43</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-13 21:43</small>

Exit 0. Verifico qué quedó:

### 🤖 Claude  <small>2026-09-13 21:43</small>

_[usó herramienta: Read]_

### 🧑 Vos  <small>2026-09-13 21:43</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-13 21:44</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-09-13 21:44</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-13 21:44</small>

Instalación limpia. Pero **hay un detalle clave para tu tema de Astra** — mirá la línea 11 del log:

> `No ASAR feature descriptors enabled; preserving official app.asar byte-for-byte`

Chequeo versiones antes de sacar conclusiones:

### 🤖 Claude  <small>2026-09-13 21:44</small>

_[usó herramienta: Bash]_

### 🤖 Claude  <small>2026-09-13 21:44</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-09-13 21:44</small>

_[resultado de herramienta]_

### 🧑 Vos  <small>2026-09-13 21:44</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-13 21:44</small>

Listo, instalado. Y **apareció algo que puede ser exactamente tu respuesta.**

## La instalación

| | |
|---|---|
| Ubicación | `/home/matiigonzz/codex-desktop-linux/codex-app/` |
| Lanzador | `codex-app/start.sh` |
| Paquete upstream | `chatgpt 26.908.40834` (oficial, firmado, sha256 verificado) |
| Build del repo | `0.11.1` — commit `f445a44` |

`/opt/codex-desktop` quedó **intacto** (sigue root, fecha 25/ago) y tu Codex actual sigue corriendo, PID 72850. Instalación paralela, como te dije.

## Lo importante: las versiones no coinciden

```
codex NUEVO  → codex-cli 0.154.0-alpha.6.2
codex /opt   → codex-cli 0.150.0-alpha.8
```

¿Te acordás del `models_cache.json`? Decía `client_version: 0.150.0`. **Coincide exacto con tu instalación vieja.**

Y la app también está atrasada: la tuya es `26.820.60940`, esta trae `26.908.40834`.

Así que la hipótesis que te mencioné antes ahora tiene peso real: **estabas pidiendo el catálogo de modelos con un cliente de hace ~3 semanas.** Si Astra se habilitó para clientes más nuevos, tu 0.150 nunca lo iba a ver.

**No te lo puedo garantizar** — sigue siendo el servidor el que decide según tu cuenta Plus. Pero es la única variable local que encontré que efectivamente estaba mal, y ahora está corregida.

## Lo que NO hace esta instalación

El log avisó:

> `No ASAR feature descriptors enabled; preserving official app.asar byte-for-byte`

No existe `linux-features/features.json`, así que **ningún feature del repo está activo** — incluido `model-picker-default-presets`. Esto es la app oficial pura con el envoltorio de Linux. Si más adelante querés esos parches, hay que crear el archivo y reconstruir.

## Para probarlo

Ojo: comparte `~/.codex` con la instancia que ya tenés abierta, y dos apps peleándose por las mismas sqlite puede dar problemas. **Cerrá el Codex actual antes.**

```bash
/home/matiigonzz/codex-desktop-linux/codex-app/start.sh
```

Cuando arranque, va a refrescar el catálogo con el cliente 0.154. Si querés, después lo chequeo:

```bash
python3 -c "import json;d=json.load(open('/home/matiigonzz/.codex/models_cache.json'));print(d['client_version']);[print(m['slug']) for m in d['models']]"
```

Tu `config.toml` ya apunta a `gpt-6-astra`, así que si el modelo aparece en el catálogo, lo agarra solo — no hay que tocar nada más.
