---
tool: ClaudeCode
session_id: c024d106-7350-4c39-9dd0-b01ae7596e6e
fecha: 2026-09-24 02:25
titulo: "Quiero que me des ideas para que hagas eh automati"
tags: [chat, agente, claudecode]
---

# 💬 Quiero que me des ideas para que hagas eh automati
> **ClaudeCode** · 2026-09-24 02:25 · `c024d106-7350-4c39-9dd0-b01ae7596e6e`

---

### 🧑 Vos  <small>2026-09-24 02:25</small>

Quiero que me des ideas para que hagas eh, automatizaciones eh, con todos los skills que tienes y todos los aprendizajes que tienes. Eh, ahí te voy a mandar eh, todo de, de cómo funciona una gente y quiero que me digas todas ideas para subirlas en N8N. Quiero que sean eh, buenas, perfectas, con mucho... No sé cómo se llaman los que tienen los N... Eh, eh, Ahí te digo cómo se llama. Que tenga bastantes. Creo que se dice en trigger. Creo que se dice en trigger. No sé cómo se dice el nombre en verdad. Eh, pero eso. Eh, que tenga varios pasos. Que tenga varios flujos. Que tenga varios flujos. Eh, ahí te voy a pasar todo lo, todo lo que tiene que ver con el proyecto.

# 🗺️ GONVRA — Cómo funciona todo

> **Para qué sirve este archivo:** es el mapa completo del sistema. Sirve para
> entender qué hay, qué se puede pedir, y qué NO se puede (con el motivo verificado).
> **Si le vas a pedir una automatización nueva a un agente, pasale este archivo primero.**

---

## 1. EL NEGOCIO EN 30 SEGUNDOS

| | |
|---|---|
| Marca | **GONVRA** · gonvra.com · Argentina |
| Producto | Rasuradora Integral Recargable — Rostro y Cuerpo |
| Precio | **$36.900** (costo $8.672,90 → margen 76%) |
| Tienda | Shopify `jm60sa-cp.myshopify.com` |
| Instagram | **@gonvra1** (BUSINESS) |
| Mail | gonvra0@gmail.com · WhatsApp +54 9 11 5376-7293 |
| **Ventas hasta hoy** | **0** — porque no hubo tráfico, no por un problema técnico |
| **CPA techo** | **$7.129 por venta.** Por debajo de eso, se gana plata seguro |

**Matías no se graba y no tiene el producto físico.** Todo el contenido se hace con
las fotos reales + texto + voz en off.

---

## 2. LAS PIEZAS

```
        ┌──────────── TU LAPTOP (todo corre acá) ────────────┐
        │                                                     │
        │  HERMES  ──► 20 trabajos programados                │
        │    │           (12 agentes IA + 8 scripts)          │
        │    │                                                │
        │  n8n ──────► 7 automatizaciones visuales            │
        │    │           localhost:5678                       │
        │    │                                                │
        │  PORTERO ──► deja pasar SOLO /webhook               │
        │    │           (protege los tokens)                 │
        │    │                                                │
        │  TÚNEL ────► dirección pública de internet          │
        │                                                     │
        │  PANEL ────► localhost:8080 (Mission Control)       │
        └─────────────────────────────────────────────────────┘
              ▲                                    │
              │ avisan cuando pasa algo            │ actúan sobre
              │                                    ▼
        Shopify · Instagram                 Shopify · Instagram · Gmail
```

**6 servicios que arrancan solos con la compu** y se reinician si se caen:
`hermes-gateway` · `gonvra-n8n` · `gonvra-proxy` · `gonvra-tunel` · `gonvra-panel` · `gonvra-gmail-auth`

---

## 3. QUÉ PUEDE HACER EL SISTEMA (capacidades reales, probadas)

### 🛒 Shopify — acceso completo de lectura
- Leer **pedidos, clientes, carritos abandonados, productos, stock**
- **Escribir el tema** (via CLI): editar secciones, subir archivos
- **Registrar webhooks**: enterarse de cosas al instante
- ❌ No puede: políticas, páginas, subir a "Files" (falta permiso)

### 📸 Instagram — @gonvra1
- **Publicar fotos, carruseles (2-10) y reels** ✅ probado
- Leer perfil y publicaciones
- Mandar mensajes privados
- ❌ **No puede leer comentarios** (permiso pendiente en Meta — ver sección 6)

### 📧 Gmail — gonvra0@gmail.com
- Leer, buscar, etiquetar, **crear borradores**, enviar
- 15 herramientas disponibles

### 🎬 Contenido
- **ffmpeg** — armar y editar videos
- **ImageMagick** — componer placas
- **video-intel.py** — espiar videos de la competencia sin gastar tokens
- ❌ Generar imágenes con IA: **sin cuota** (ver sección 6)

### 🕵️ Inteligencia
- **Espiar precios** de cualquier tienda Shopify (`/products.json` es público)
- Leer cualquier web con navegador real (Chromium instalado)

### 📢 Avisos
- **Telegram** — todo lo urgente llega ahí
- **Mission Control** — panel visual en localhost:8080

---

## 4. LO QUE YA CORRE SOLO

### Trabajos programados (20)

| Hora | Quién | Qué hace |
|---|---|---|
| 02:00 | ESPIA 🤖 | Espía competencia |
| 06:00 | ANALISTA 🤖 | Revisa números |
| 09:00 | COPY 🤖 | Escribe textos |
| 10:00 | TIKTOKER 🤖 | Guiones de video |
| 11:00 | INSTAGRAMER 🤖 | Carruseles e historias |
| 13:00 | CRO 🤖 | Mejoras de la ficha |
| 15:00 | CREATIVO 🤖 | Piezas visuales |
| 19:00 | CAZADOR 🤖 | Dónde está el público |
| 21:00 | JEFE 🤖 | **Único resumen diario** a Telegram |
| Lunes 16 | CREATIVO 🤖 | Estrategia Andrómeda para Meta Ads |
| Miérc 16 | TIKTOKER 🤖 | Prompts para Google Flow |
| cada 4 h | GUARDIA ⚙️ | Salud de la tienda (sin IA, $0) |
| cada 15 m | VENTAS ⚙️ | Avisa si entró un pedido |
| cada 20 m | WEBHOOKS ⚙️ | Mantiene viva la URL pública |
| cada 30 m | PANEL ⚙️ | Refresca los datos |
| cada 30 m | SEGURIDAD ⚙️ | Tapa credenciales en los chats |
| 08 y 20 | PRECIOS ⚙️ | Competencia: avisa si cambian |
| 11:00 | POSVENTA ⚙️ | Borradores de mail a clientes |
| 04:00 | BACKUP ⚙️ | Copia de todo (7 días) |
| 05:00 | LIMPIEZA ⚙️ | Borra archivos temporales |

🤖 = usa IA (cuesta tokens) · ⚙️ = script puro (cuesta $0)

### Automatizaciones n8n (7)

1. **Venta instantánea** — Shopify avisa → Telegram con dirección y qué comprar
2. **Carritos abandonados** — cada 3 h, con el mail ya redactado
3. **Reporte diario** — 20:00, ventas y plata parada
4. **Cola IG: avisar** — qué espera tu OK
5. **Cola IG: publicar** — publica lo aprobado
6. **Comentario → privado** — armado, esperando el permiso de Meta
7. **Errores** — si algo se rompe, te avisa

---

## 5. CÓMO SE PUBLICA (lo único manual)

```
~/GONVRA-PUBLICAR/
   1-PENDIENTE/   ← poné acá el contenido
   2-APROBADO/    ← movelo acá = tu OK
   3-PUBLICADO/   ← queda el historial
```

- **Foto:** `imagen.png` + `imagen.txt` (el texto)
- **Carrusel:** una **carpeta** con `01-x.png`, `02-y.png`... + `texto.txt` adentro
- **Reel:** `video.mp4` + `video.txt`

Cada 30 min te avisa qué hay esperando. Cada 10 min publica lo aprobado.
**Nada sale sin que muevas el archivo.**

---

## 6. LO QUE NO SE PUEDE (verificado, no insistir)

| Qué | Por qué | Cómo se soluciona |
|---|---|---|
| **Leer comentarios de IG** | Permiso `manage_comments` pendiente en Meta ("Acciones necesarias") | Completar lo que pide Meta |
| **Generar imágenes con IA** | Gemini: 429 sin cuota en los 4 modelos. Replicate: 403 | Pagar, o componer con ImageMagick |
| **Generar video con IA** | La API de Veo es **solo pago**; Flow web no tiene API | Prompts automáticos + Flow a mano |
| **Publicar en TikTok** | Sin auditoría, los videos quedan privados | Subir a mano (3 min) |
| **Espiar Ad Library** | Anti-bot 403 | A mano en facebook.com/ads/library |
| **WhatsApp** | Trámite de Meta | Hermes tiene `whatsapp-cloud` listo |
| **Meta Ads** | Token de servicio pago + no hay ads corriendo | Cuando haya pauta |

---

## 7. REGLAS QUE NO SE ROMPEN

1. **Nada se publica ni se envía sin aprobación** de Matías
2. **Cero mentiras**: sin reseñas inventadas, sin escasez falsa, sin contadores truchos
3. **Sin promesas técnicas sin prueba**: nada de batería, potencia, impermeabilidad
4. **Las credenciales van en `~/.hermes/.gonvra-secrets.env`** (chmod 600), nunca en
   un entregable, un chat o Obsidian
5. **El catálogo se lee en vivo** de Shopify, nunca hardcodeado
6. **Todo dato del panel que se pueda verificar, se verifica.** Nada escrito a mano
7. **Antes de reintentar algo, leer `BITACORA-ERRORES.md`** (23 errores documentados)

---

## 8. 📝 CÓMO PEDIR UNA AUTOMATIZACIÓN NUEVA

Copiá esto y completá:

```
Quiero una automatización que:

QUÉ LA DISPARA:
  (  ) A una hora fija: ______
  (  ) Cada X tiempo: ______
  (  ) Cuando pasa algo en Shopify (venta, carrito, producto)
  (  ) Cuando pasa algo en Instagram
  (  ) Cuando aparece un archivo en una carpeta

QUÉ TIENE QUE HACER:
  (describilo en una frase, como se lo contarías a una persona)

CON QUÉ DATOS:
  (  ) Pedidos / clientes / carritos de Shopify
  (  ) Publicaciones de Instagram
  (  ) Mails de Gmail
  (  ) Precios de la competencia
  (  ) Lo que escribieron los agentes

CÓMO ME ENTERO:
  (  ) Telegram
  (  ) Borrador en Gmail
  (  ) Solo lo anota, sin molestarme
  (  ) Solo si hay algo raro

¿NECESITA MI APROBACIÓN ANTES DE ACTUAR?
  (  ) Sí, siempre      (  ) No, si es solo leer
```

**Antes de construir, el agente tiene que:**
1. Chequear en la sección 6 si algo lo bloquea
2. Decir qué **no** va a poder hacer y por qué
3. **Probarlo con datos reales** antes de decir que funciona
4. Anotar en `BITACORA-ERRORES.md` lo que se rompa

---

## 9. ARCHIVOS IMPORTANTES

```
~/Claude/gonvra2/
   COMO-FUNCIONA-TODO.md      ← este archivo
   CONTEXTO.md                ← lo que leen los 15 agentes
   BITACORA-ERRORES.md        ← 23 errores con causa y arreglo
   HACE-ESTO-MATIAS.md        ← lo que solo puede hacer Matías
   CONECTORES.md              ← APIs y MCPs
   RESUMEN-COMPLETO-handoff.md
   n8n-workflows/             ← los 7 flujos en JSON
   competencia.txt            ← tiendas a vigilar

~/GONVRA-PUBLICAR/            ← la cola de publicación
~/GONVRA-BACKUPS/             ← 7 días de copias
~/.hermes/scripts/gonvra-*    ← los scripts del sistema
```

---

## 10. LA VERDAD INCÓMODA

El sistema está completo: publica, vende, avisa, respalda y vigila.

**Pero todavía no vendió nada. Y no va a vender hasta que entre gente a la tienda.**

Ninguna automatización nueva cambia eso. Lo que lo cambia es **publicar seguido**:
3 posts en Instagram es un arranque, no una estrategia. El sistema ya deja el contenido
listo todos los días — lo único que falta es aprobarlo y que salga.

**Si tenés que elegir entre una automatización más o publicar 5 videos esta semana,
elegí publicar.**

### 🤖 Claude  <small>2026-09-24 02:25</small>

Antes de tirar ideas al aire, voy a mirar qué hay realmente construido para no repetir flujos ni proponer cosas que choquen con lo bloqueado.

### 🤖 Claude  <small>2026-09-24 02:25</small>

_[usó herramienta: Bash]_

### 🤖 Claude  <small>2026-09-24 02:25</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-09-24 02:25</small>

_[resultado de herramienta]_

### 🧑 Vos  <small>2026-09-24 02:25</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-24 02:26</small>

_[usó herramienta: Bash]_

### 🤖 Claude  <small>2026-09-24 02:26</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-09-24 02:26</small>

_[resultado de herramienta]_

### 🧑 Vos  <small>2026-09-24 02:26</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-24 02:26</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-09-24 02:26</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-24 02:26</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-09-24 02:26</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-24 02:26</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-09-24 02:26</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-24 02:26</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-09-24 02:26</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-24 02:28</small>

Miré el sistema real antes de inventar nada. Dos cosas que cambian las prioridades:

**1. Los nombres que buscabas:** **trigger** (disparador — el nodo que arranca el flujo) y **nodos** (los bloquecitos de cada paso). Un flujo "grande" = muchos nodos + a veces varios triggers al mismo flujo.

**2. El dato incómodo, verificado ahora:** `1-PENDIENTE` y `2-APROBADO` están **vacías**. Hay 3 piezas en `3-PUBLICADO` en total. O sea: el sistema deja contenido listo, pero hace días que no entra ni sale nada de la cola. **El cuello de botella no es la falta de automatizaciones, es que aprobar requiere estar en la laptop moviendo archivos a mano.**

Así que ordené las ideas por eso: primero las que sacan contenido a la calle, después las que reportan.

---

## 🔴 Nivel 1 — Las que mueven la aguja

### A. Aprobar desde Telegram con botones
*~14 nodos · 2 triggers · esta es LA que falta*

| | |
|---|---|
| **Trigger 1** | Schedule cada 30 min → `executeCommand` que lee `1-PENDIENTE` |
| **Trigger 2** | Webhook `/webhook/gonvra-tg` ← Telegram te devuelve el botón apretado |

**Cadena:** detecta pieza nueva → **te manda la imagen real** (`sendPhoto` / `sendMediaGroup` para carruseles) con el copy debajo y 3 botones: `✅ Publicar` `❌ Descartar` `✏️ Otro texto` → apretás desde el celular → el webhook valida que el `chat_id` sea el tuyo (si no, descarta) → mueve el archivo a `2-APROBADO` o a `0-DESCARTADO` → edita el mensaje a "✅ aprobado 21:05" → **dispara la publicación al instante** (no esperás los 10 min del flujo 5).

**Bloqueos reales que encontré:**
- ❌ **No usar el nodo Telegram Trigger.** `WEBHOOK_URL` no está seteado en el servicio de n8n, así que registraría un `localhost` en Telegram y no llegaría nada. Va Webhook común + `setWebhook` a mano.
- ⚠️ La URL de `trycloudflare` rota al reiniciar → hay que extender `gonvra-sincronizar-webhooks.sh` para re-registrar también el de Telegram (ver idea G).
- ✅ La regla 1 se respeta: nada sale sin que aprietes el botón. Solo cambia *dónde* aprietas.

---

### B. Fábrica de contenido: del .md del agente a la cola
*~18 nodos · 2 triggers*

| | |
|---|---|
| **Trigger 1** | Schedule 11:30 (después de INSTAGRAMER de las 11:00) |
| **Trigger 2** | Webhook `/webhook/gonvra-forzar-contenido` para dispararlo cuando quieras |

**Cadena:** lee `instagramer/2026-XX-XX.md` y `copy/` del día → nodo Code parsea los bloques de copy → `executeCommand` con **ImageMagick** compone la placa sobre las fotos reales del producto → guarda `imagen.png` + `imagen.txt` en `1-PENDIENTE` → le avisa al flujo A.

**Bloqueos:** ❌ imágenes IA sin cuota (Gemini 429 / Replicate 403, sección 6) → **todo se compone con ImageMagick sobre las fotos reales**. Si no existe el .md del día, el flujo avisa en vez de inventar contenido.

**Por qué importa:** hoy el agente escribe el .md y ahí muere. Esto lo convierte en archivo aprobable. Combinado con A: de idea a publicado en 2 toques.

---

### C. Guardián de la URL pública (verificación real, no "parece que sí")
*~12 nodos · esta es E-018 y E-022 convertidas en automatización*

**Trigger:** Schedule cada 20 min.

**Cadena:** lee la URL del túnel → la compara con la registrada en **Shopify** y en **Telegram** → si cambió, re-registra las dos → **hace un POST real desde afuera a `/webhook/gonvra-ping` y confirma que la ejecución llegó** → si falla 2 veces seguidas, reinicia el túnel y te avisa.

**Por qué es nivel 1:** sin esto, la venta instantánea y el botón de aprobar mueren en silencio cuando rota el túnel. Y el ping end-to-end es lo que pide la bitácora: "cuando un webhook *está bien configurado* y no llega nada, probar qué llega de verdad".

---

## 🟡 Nivel 2 — Protegen la plata

### D. Primera venta: protocolo completo + atribución artesanal
*~22 nodos · el flujo más largo de todos*

**Trigger:** webhook Shopify `orders/create`.

**Cadena:** aviso a Telegram con dirección y qué comprar *(ya existe)* → **+ borrador de bienvenida en Gmail** → **+ snapshot de qué publicaste los últimos 7 días** (sin ads, esta es tu única atribución) → Wait 3 días → ¿se despachó? si no, te recuerda → Wait 10 días → borrador pidiendo reseña **real** → si es la **primera venta de la historia**, mensaje aparte con el CPA implícito vs. tu techo de $7.129.

**Bloqueos:** ninguno. Todo lectura de Shopify + borradores de Gmail (nada se envía sin tu OK).

### E. Rescate de carrito en 3 toques
*~16 nodos · 2 triggers*

Webhook `checkouts/create` (instantáneo) + Schedule cada 3 h de respaldo → Wait 45 min → **chequea si ya se convirtió en pedido** (si sí, corta y no molesta) → borrador en Gmail personalizado con el nombre y el producto → Telegram con botón "enviar ahora" → toque 2 a las 20 h → toque 3 a las 44 h. **Mismo texto, sin descuento falso ni escasez inventada** (regla 2).

### F. Vigía de la ficha de producto
*~10 nodos · 2 triggers*

Webhook Shopify `products/update` + Schedule 07:00 → compara snapshot contra el anterior (precio, título, stock, imágenes) → si cambió, manda el **diff** → si el precio bajó de $36.900 lo suficiente para romper el margen del 76%, **alerta roja**. Protege contra que una app, un tema o vos mismo rompan la ficha sin darse cuenta.

---

## 🟢 Nivel 3 — Inteligencia y salud

### G. Radar de competencia con escalada
Schedule 08:00 y 20:00 → `/products.json` de cada tienda de `competencia.txt` → histórico en disco → detecta bajadas de precio, quiebres de stock y **productos nuevos** → si alguien te deja mal parado, Telegram con "tu precio quedó N% arriba" + ángulo de copy sugerido → **escribe el hallazgo en `espia/` para que el agente del día siguiente lo use**. (❌ Ad Library sigue 403, eso sigue a mano.)

### H. Cola de reels ↔ Google Flow
Schedule miércoles 16:30 → toma los prompts del TIKTOKER → te los manda de a uno a Telegram listos para copiar → cuando dejás el `.mp4` en una carpeta, el flujo lo detecta, le pega el guion como `.txt` y lo pone en `1-PENDIENTE`. (❌ Veo API es paga y Flow no tiene API → el video lo generás a mano; TikTok sin auditoría → subida manual.)

### I. Watchdog de los watchdogs
Schedule cada hora → verifica los 6 servicios activos + que los 20 jobs de Hermes hayan corrido en las últimas 24 h + ejecuciones falladas de n8n → si un agente dejó de correr en silencio, te enterás. Hoy no te enterarías.

### J. Cierre del día que mide lo correcto
Schedule 20:00 + domingo 20:00 → junta ventas, carritos, **piezas publicadas hoy**, piezas que quedaron sin aprobar, errores → **le pasa el resumen al JEFE de las 21:00 en vez de mandarte un mensaje aparte** (no duplicar avisos, regla del doc) → métrica principal: *publicaste X de Y piezas esta semana*, no las ventas.

---

## ⚠️ Dos correcciones a tu propio doc

1. **La sección 8 ofrece "cuando aparece un archivo en una carpeta" como trigger — eso no existe en tu n8n.** `localFileTrigger` está deshabilitado a propósito en el servicio (`NODES_EXCLUDE`). Todo lo de carpetas va con **Schedule + executeCommand**. Lo tuve en cuenta en A, B y H.
2. **Importar el JSON no alcanza** (E-014): hay que `n8n publish:workflow --id=XXX` y reiniciar. Cualquier flujo que construya lo entrego con ese paso incluido y probado.

---

## Mi recomendación

Construiría **A + C juntas, en ese orden**. A sin C se rompe sola en el primer reinicio del túnel. Con las dos andando, aprobar contenido pasa de "prender la laptop y mover archivos" a dos toques en el colectivo — y eso es lo único de esta lista que puede cambiar el 0 de ventas.

B va tercera: llena la cola que hoy está vacía.

¿Arranco con A + C y te las dejo probadas con datos reales?
