---
tags: [gonvra, errores, bitacora, troubleshooting]
actualizado: 2026-09-23
---

# 🐞 BITÁCORA DE ERRORES — GONVRA

> Todo lo que se rompió, por qué, y cómo se arregló (o por qué no se pudo).
> **Antes de reintentar algo, buscá acá.** Evita repetir horas perdidas.

---

## 🔴 ABIERTOS (sin resolver)

### ~~E-001 · Instagram: "API access blocked"~~ ✅ RESUELTO 23/09

**Era el token invalidado.** Regenerarlo desde el App Dashboard lo arregló.
La app estaba perfecta: sin alertas, en modo Desarrollo, @gonvra1 como evaluador.

**Causa:** el token del 22/09 (184 caracteres) se invalidó solo en ~22 horas, pese a ser
de larga duración. El nuevo tiene 182 caracteres y funciona.

**Verificado el 23/09:** lee la cuenta (`@gonvra1`, BUSINESS) **y crea contenedor de
publicación** (id `18091...`). Cuota 0 de 50 usados.

**Lección:** ante `API access blocked` con la app sana, **regenerar el token primero**.
No perder tiempo revisando permisos.

**Si vuelve a pasar:** `bash ~/Claude/gonvra2/probar-instagram.sh`

### E-023 · 🔑 LA CAUSA REAL: al token le falta `manage_comments`
**Síntoma:** la suscripción a webhooks estaba perfecta (URL verificada, token correcto,
campo `comments` suscrito) pero **no llegaba ningún comentario real**.

**Diagnóstico por capacidades** (probando qué puede hacer el token):
```
leer perfil:       SI   (instagram_business_basic)
publicar:          SI   (content_publish)
mensajes (DM):     SI   (manage_messages)
leer comentarios:  NO   <-- FALTA
```
**Pista que lo delató:** `comments_count: 1` pero `/comments` devuelve `data: []`.
El contador es parte de *basic*; **listar** los comentarios necesita `manage_comments`.

**Sin ese permiso, Meta NO manda los webhooks de comentarios**, por más que la
suscripción figure activa.

**Solución:** regenerar el token con el permiso
`instagram_business_manage_comments` marcado, y probarlo con:
`bash ~/Claude/gonvra2/probar-instagram.sh`

**Lección:** cuando un webhook "está bien configurado" y no llega nada, **probar qué
puede hacer el token** en vez de revisar la configuración una y otra vez.

### E-022 · ⚠️ Webhooks de Instagram: la app tiene que estar PUBLICADA
**Qué dice Meta** (cartel en el panel de webhooks, visto el 23/09):
> *"Para recibir webhooks, tu aplicación debe tener el estado **publicada**."*

**Qué significa:** en modo **Desarrollo**, el botón **Test** de Meta sí dispara el
webhook (y llega a n8n), pero **los comentarios reales de gente podrían no llegar**.

**Estado:** la suscripción está bien armada y verificada:
- URL: `.../webhook/gonvra-ig` — devuelve el `hub.challenge` correctamente
- Token: `gonvra2026verify`
- Campos suscritos: `comments`, `messages`, `live_comments`
- Cuenta @gonvra1 con "Suscripción a webhook: Sí"

**⚠️ TRAMPA AL PROBARLO (23/09):** se comentó desde **@gonvra1** (la propia cuenta)
y no llegó nada. **No era un fallo.** Instagram **no dispara el webhook cuando el dueño
comenta en su propio post**. Encima la API lo confirma raro: `comments_count: 1` pero
`data: []` — no lista el comentario del owner.
El workflow además lo filtra a propósito (`if (autor === 'gonvra1') continue`).

**La prueba válida es comentar desde OTRA cuenta.**

**Prueba definitiva pendiente:** comentar "precio" en un post real de @gonvra1 y ver
si aparece una ejecución del workflow en n8n. Si el Test funciona pero el comentario
real no, hay que publicar la app (App Review).

**Dato aclarado — los dos IDs de Instagram NO son un error:**
```
id:      28674883412124543   (Instagram-scoped ID · se usa para publicar)
user_id: 17841440324900019   (Instagram Business Account ID · el que muestra Meta)
```
Son la misma cuenta. El workflow no filtra por ID, así que acepta los dos.

### ~~E-002 · Replicate: clave rechazada~~ ✅ RESUELTO 24/09
Clave nueva funcionando (cuenta `elpapu897`). Ahora se puede generar
**imágenes y video**.

| Qué | Modelo | Costo |
|---|---|---|
| Imagen rápida | `black-forest-labs/flux-schnell` | **US$0.003** |
| Imagen buena | `google/nano-banana` | US$0.039 |
| Video 6s 768p | `minimax/hailuo-02` | **US$0.28** |
| Video 6s 1080p | `minimax/hailuo-02` | US$0.48 |

**Trampas encontradas:**
1. Replicate devuelve `"error": null` cuando **no** hay error. `if "error" in d`
   da falso positivo: hay que usar `if d.get("error")`.
2. `wan-video/wan-2.5-t2v-fast` falla con **E002** aunque solo pida `prompt`.
   Usar `hailuo-02`, que tiene 454k usos.
3. **El video sale HORIZONTAL** (1366x768). Instagram Reels necesita 9:16 →
   el script recorta al centro y escala a 1080x1920 con ffmpeg.

**Freno de gasto:** `gonvra-generar-video.py` exige `--confirmo`, lleva registro
en `~/.hermes/gonvra-gasto-replicate.json` y **corta a los US$3 por día**.

### E-003 · Meta Ad Library: bloqueo anti-bot
### E-003 · Meta Ad Library: bloqueo anti-bot
```
Blocked by anti-bot protection: HTTP 403
```
**Probado 2 veces:** espera de 8 s y de 30 s + 15 scrolls. Mismo resultado, 0 anuncios.
**Causa:** Meta detecta el navegador headless.
**Workaround:** espiar a mano en facebook.com/ads/library (ahí sí funciona, hay sesión real).
**No borrar el MCP:** la instalación ya está hecha por si Meta afloja.

### E-004 · Shopify: faltan permisos de temas y archivos
```
403 · "This action requires merchant approval for read_themes scope"
404 · files.json
```
**Impacto:** no se pueden subir archivos propios para tener URL pública.
**Workaround encontrado:** las imágenes de producto YA están en CDN público:
`https://cdn.shopify.com/s/files/1/0722/4652/6067/files/rasuradora-integral-hero-v1.png`
Verificado HTTP 200 sin login. **Sirven para publicar en Instagram.**

---

## ✅ RESUELTOS

### E-005 · Shopify: el flujo del token `shpat_` no existe más
**Error:** las instrucciones mandaban a "Configuración de API de administrador → Instalar app".
**Ese menú fue eliminado por Shopify.** Ahora es el Dev Dashboard.
**Lo que NO sirve:**
- Token `atkn_` del Dev Dashboard → **401** (probado en 2 versiones de API, header normal,
  Bearer y GraphQL)
- Los 6 tokens del Shopify CLI → **401** en pedidos. El de la tienda sirve para *temas*
  **con header `Authorization: Bearer`**, no con `X-Shopify-Access-Token`.
**Solución:** OAuth → `sacar-token-shopify.py`. Funcionó: 5/5 endpoints en 200.

### E-006 · Mission Control se veía "caído"
**Causa:** el servidor se levantaba con `python3 -m http.server` colgado de la terminal.
Al cerrar la terminal, **moría**.
**Solución:** servicio `gonvra-panel.service` con `Restart=always`. Arranca solo.

### E-007 · El panel mostraba datos falsos
**Casos encontrados:** GUARDIA "22:00" que no existía · servidor muerto como "activo" ·
Gmail "sin conectar" estando conectado · **Replicate en verde estando roto** ·
Instagram "falta permiso" estando OK.
**Causa raíz:** los datos estaban **escritos a mano** en `generar-datos.py`.
**Solución:** ahora 9 de 13 se verifican en vivo (API, proceso, archivo).
**Regla:** *ningún dato del panel se escribe a mano si se puede verificar.*

### E-008 · `hermes cron create` "unrecognized arguments"
**Causa:** las opciones van **ANTES** del horario. Si van después, no crea nada.
```
✅ hermes cron create --name X --model Y "0 9 * * *" "prompt"
❌ hermes cron create "0 9 * * *" --name X "prompt"
```

### E-009 · Watchdog daba falsa alarma
**Causa:** `gateway.pid` es un **JSON**, no un número. Sacar los dígitos con `tr` pegaba
el pid con el `start_time` → pid inválido.
**Solución:** parsear el JSON con python.

### E-010 · Hermes bloquea cron que mencionen reiniciar el gateway
```
Blocked: cron job contains a gateway lifecycle command
```
Pasa **aunque sea dentro del texto de un mensaje**. Anti-loop de respawn.

### E-011 · Links de OAuth de Google que vencen
**Causa:** se mandó el link por chat y se abrió 45 min después → `Invalid or expired OAuth state`.
**Solución:** `conectar-gmail.sh` genera uno fresco y lo abre al instante.

### E-012 · Comandos con huecos tipo `TU_CLIENT_ID`
**Pasó 2 veces** (con el curl del token y con el script de OAuth): se copian literal.
```
Could not find Shopify API application with api_key TU_CLIENT_ID
```
**Regla:** los scripts **preguntan** los datos, no se pasan por argumento.
Y validan que no sea el texto de ejemplo.

### E-013 · Credenciales filtradas en los chats de Obsidian
**20 credenciales en 5 archivos** (incluidas 9 viejas de NVIDIA).
**Causa:** el exportador de chats guarda todo lo que se pega en la conversación.
**Solución:** `tapar-credenciales-obsidian.py` + job cada 30 min.

### E-014 · n8n: `import` no alcanza para activar
**Causa:** n8n 2.x usa borrador/publicado. Un workflow importado queda con
`activeVersionId = NULL` y **no arranca**, aunque `active = 1`.
**Solución:** `n8n publish:workflow --id=XXX` y **reiniciar n8n**.

### E-019 · Carrusel de Instagram: "Media ID is not available"
**Síntoma:** los hijos se creaban bien (FINISHED) pero al armar el carrusel fallaba.
**Causa:** Python codifica la coma de `children=id1,id2` como `%2C` e Instagram no la
reconoce. Con `curl -d` la coma va literal y funciona.
```python
urlencode({"children":"111,222"})              -> children=111%2C222  ❌
urlencode({"children":"111,222"}, safe=",")    -> children=111,222    ✅
```
**Además:** hay que esperar a que **cada foto** esté `status_code=FINISHED` antes de
armar el carrusel.

### E-020 · Gemini: sin cuota para generar imágenes
```
429 · You exceeded your current quota
```
Probado en `gemini-3-pro-image`, `gemini-2.5-flash-image`, `gemini-3.1-flash-image`
y `nano-banana-pro-preview`. **Los cuatro dan 429.** El free tier no cubre imagen.
**Alternativa:** componer las placas con las **fotos reales** + ImageMagick/ffmpeg
(está instalado), o generar a mano en Google AI Studio.

### E-021 · Los assets de publicación se acumulaban en el tema
Cada publicación sube una copia al tema para tener URL pública. Nunca se borraban:
**30 archivos en una noche.**
**Solución:** `gonvra-limpiar-assets.sh` a las 5:00, borra los de más de 2 días.
Instagram ya guarda su propia copia, así que no se pierde nada.

### E-018 · ⚠️ CASI EXPONGO n8n ENTERO A INTERNET
**Qué pasó:** puse el portero de webhooks en el puerto **5679**... que ya lo usaba
**el Task Broker interno de n8n**. El portero no arrancó (`Address already in use`)
pero **el servicio figuraba "active"**, y el túnel quedó apuntando directo a n8n.

**Cómo se detectó:** al probar, `/rest/credentials` y `/webhook/x` devolvían **las dos**
respuestas de n8n (`Cannot GET ...`) en vez de una bloqueada y otra no.

**Por qué era grave:** con esa URL pública cualquiera podía llegar al panel de n8n,
donde están guardados los tokens de **Shopify, Instagram y Telegram**.

**Solución:** portero movido al puerto **8099** (verificado libre) y el túnel apuntando ahí.

**Lecciones:**
1. **`systemctl is-active` puede decir "active" con el proceso muerto.** Verificar el
   puerto con `ss -ltnp` y **quién** lo tiene, no solo que esté ocupado.
2. Antes de exponer algo, **probar el filtro localmente** y distinguir las respuestas
   por el **cuerpo**, no por el código HTTP (los dos daban 404).
3. n8n usa 5678 (web) **y 5679 (task broker)**. No pisar ninguno.

### E-016 · n8n 2.x deshabilita `executeCommand` por defecto
```
Activation did fail: "Unrecognized node type: n8n-nodes-base.executeCommand"
```
**Causa:** breaking change de n8n 2.0. En `@n8n/config/dist/configs/nodes.config.js`:
```js
this.exclude = ['n8n-nodes-base.executeCommand', 'n8n-nodes-base.localFileTrigger'];
```
**Solución:** en el servicio, `Environment=NODES_EXCLUDE=["n8n-nodes-base.localFileTrigger"]`
Eso habilita executeCommand y deja bloqueado el otro. **Reiniciar n8n después.**

### E-017 · Instagram necesita URL pública (RESUELTO)
**Problema:** la API no acepta archivos locales, solo URLs públicas.
**Solución encontrada:** subir al tema de Shopify con el CLI. Queda público en:
```
https://gonvra.com/cdn/shop/t/6/assets/ARCHIVO.png
```
El `t/6` se encontró probando del 1 al 15 (no hay forma de consultarlo sin `read_themes`).
Script: `~/.hermes/scripts/gonvra-subir-imagen.sh` — sube, **verifica que responda 200**
y recién ahí devuelve la URL.

### E-015 · n8n CLI choca con la instancia corriendo
```
n8n Task Broker's port 5679 is already in use
```
**Solución:** parar el servicio, correr el comando, volver a arrancarlo.
Y `n8n execute --id` **no sirve** para workflows con Schedule Trigger
(pide un "Execute Workflow Trigger").

---

## 🚫 LO QUE NO SE PUEDE (verificado, no insistir)

| Qué | Por qué | Verificado |
|---|---|---|
| **Automatizar Google Flow** | La web es gratis pero **no tiene API**. La API de video (Veo / Omni Flash) dice textual: **"Free Tier: Not available"** — solo pago | 23/09 en la doc de precios |
| **Publicar en TikTok por API** | Doc oficial: *"All content posted by unaudited clients will be restricted to private viewing mode"*. Son **2 aprobaciones**: scope + auditoría | 23/09 en la doc |
| **Espiar Ad Library automático** | Anti-bot 403 | 2 intentos |
| **Meta Ads API** | Necesita token de un servicio pago. Y sin ventas no hay nada que optimizar | — |
