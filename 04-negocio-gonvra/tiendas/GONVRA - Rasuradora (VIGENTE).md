---
tags: [proyecto, shopify, tienda, gonvra, vigente]
tienda: jm60sa-cp.myshopify.com
dominio: gonvra.com
estado: publicada
nicho: cuidado personal masculino
actualizado: 2026-09-07
---

# 🪒 GONVRA — Rasuradora Integral (PROYECTO VIGENTE)

> 📋 **¿Chat nuevo? Empezá por acá:** [[GONVRA - RESUMEN COMPLETO (handoff)]]

> ⚠️ **ESTE ES EL PROYECTO ACTIVO.** Reemplaza a:
> - [[Helio - Afeitadora Mini]] → producto descartado, ya no se usa ese nombre. **NO nombrarlo.**
> - GONVRA mascotas (`9em58g-tt.myshopify.com`) → **nicho abandonado**, no se toca más.
>
> La **marca GONVRA y el dominio gonvra.com se mantienen**; lo que cambió es el rubro y el producto.

## Datos

| | |
|---|---|
| Nombre de la tienda | **GONVRA** ✅ |
| Shopify | `jm60sa-cp.myshopify.com` |
| Admin | https://admin.shopify.com/store/jm60sa-cp |
| Dominio | **gonvra.com** ✅ |
| Tema LIVE | `GONVRA — Landing de vista previa` **#148158414963** |
| Proyecto local | `~/Documents/Codex/tiendas/jm60sa-cp/live-theme` |
| Moneda | ARS · Argentina |
| Contacto | `gonvra0@gmail.com` · WhatsApp **+54 9 11 5376-7293** |

## Producto (UNO SOLO)

- **Rasuradora Integral Recargable — Rostro y Cuerpo** — **$36.900**
- Handle: `face-body-electric-shaver` · Variante: Negro y verde lima
- Una sola máquina para cara y cuerpo: barba, patillas, pecho, brazos, piernas, zona íntima.
  Peines regulables. Recargable.
- Público: hombres argentinos que usan varios aparatos o van a la peluquería.
- ⚠️ Inventario declarado 50.000 = valor por defecto del proveedor, **no es stock real**.
  No usarlo para escasez.

## ✅ HECHO Y VERIFICADO EN VIVO (2026-09-07) — no volver a preguntar

| Ítem | Estado | Verificación |
|---|---|---|
| **Checkout / Mercado Pago** | ✅ **FUNCIONA** | Único pago activo: **Mercado Pago Tarjetas** (PayPal desactivado, verificado). El rechazo del 8/9 fue por **FONDOS INSUFICIENTES** ($129.475 y no había saldo) → eso prueba que la pasarela **sí se comunica con el banco**. No es un error de configuración. |
| **Política de envío** | ✅ publicada | `/policies/shipping-policy` → HTTP 200 |
| **Política de reembolso** | ✅ publicada | `/policies/refund-policy` → 200, con arrepentimiento + 10 días + mail |
| **Términos del servicio** | ✅ publicada | `/policies/terms-of-service` → 200 |
| **Política de privacidad** | ✅ publicada | `/policies/privacy-policy` → 200 |
| **Nombre de la tienda** | ✅ **GONVRA** | confirmado por Admin API (antes decía "Mi tienda") |
| **Dominio** | ✅ gonvra.com | `primaryDomain.host = gonvra.com` |
| **Botón de arrepentimiento** | ✅ en el footer | columna Legal → `/policies/refund-policy` |
| **WhatsApp flotante** | ✅ activo | `wa_number: 5491153767293` |
| **Mail + teléfono en footer** | ✅ visibles | bloque `.gvft-contacto`, clickeables |
| **Instagram** | ✅ creado | — |

## ⏳ Pendientes reales

1. **Píxel de Meta** — sin verificar para esta tienda. Debe conectarse desde el **canal de Facebook
   & Instagram de Shopify** (no solo en el tema), o el evento `Purchase` nunca dispara.
2. **Que llegue el pedido de prueba** — Matías compró para probar; falta confirmar la entrega.
3. **Equipo de agentes** — migrar el contexto al producto nuevo (ver abajo).
4. **Publicidad** — recién cuando el píxel mida bien y PRECIOS calcule el CPA máximo.


## 📊 Diagnóstico del píxel (Codex, 2026-09-13)

**Píxel:** `3919766821491073` · instalado vía app de Facebook & Instagram de Shopify (web pixel,
modo optimizado, navegador + servidor). **Es el único** en la tienda, no hay duplicados.

### 🔴 Problema 1 — El evento `Purchase` NUNCA dispara
Embudo recibido (6-12 sep 2026):

| Evento | 7 días | Última recepción |
|---|---:|---|
| PageView | 401 | hace 2 días |
| ViewContent | 107 | hace 2 días |
| AddToCart | 7 | hace 5 días |
| InitiateCheckout | 15 | hace 5 días |
| AddPaymentInfo | 18 | hace 5 días |
| **Purchase** | **0 / ausente** | **nunca** |

Tampoco aparece en los últimos 28 días. **Hipótesis principal:** con Mercado Pago (proveedor
externo) el cliente sale del sitio; el `Purchase` dispara al volver a la thank-you page. Si no
vuelve, o el pago queda pendiente, el evento no se genera.
**Verificación decisiva pendiente:** ¿la compra de prueba figura como PEDIDO en Shopify?
- Si figura → problema de aviso a Meta (app / thank-you page).
- Si no figura → el pago no se completó realmente.

### ⚠️ Problema 2 — El píxel NO está conectado a ninguna cuenta publicitaria
- Dueño del píxel: portfolio empresarial **gonvra1**, ID `1065947712672679`
- Cuenta publicitaria: **Matias Gonzalez**, ID `2487859205019090` — ACTIVE, ARS, **con medio de
  pago cargado**, habilitada para pautar
- ❌ El portfolio `gonvra1` dice "No se ha añadido ninguna cuenta publicitaria"
- ❌ El píxel dice "No hay activos conectados"
⇒ No impide recibir eventos, pero **impide usar el píxel para optimizar y medir campañas**.

### Diagnóstico de Meta
- Errores activos: **ninguno**. El de "confirmar dominios" ya no se detecta.
- Calidad de coincidencia baja: PageView y ViewContent 4,4/10; AddToCart, InitiateCheckout y
  AddPaymentInfo **0,0/10**. Solo comparte IP, user agent e ID externo — **no manda email ni
  teléfono**, que es lo que sube la calidad.
- Conteos no monotónicos (más AddPaymentInfo que InitiateCheckout) → repeticiones o sesiones.


### ✅ RESUELTO 2026-09-14 (Codex)
- El portfolio **gonvra1** obtuvo control total **reversible** sobre la cuenta `2487859205019090`.
- El píxel `3919766821491073` ahora muestra **"1 activo está conectado"** = la cuenta publicitaria.
- ⇒ **Ya se pueden armar campañas con este píxel.**
- ⏳ Falta solo pasar el uso compartido de datos de **Mejorado → Máximo** en la app de Facebook &
  Instagram de Shopify. Requiere que **Matías** reautorice su cuenta de Facebook a mano
  (la sesión vence cada 90 días; ningún agente puede hacerlo).

### Orden de arreglo
1. Confirmar si el pedido de prueba existe en Shopify (define la causa del Purchase faltante)
2. Conectar el píxel a la cuenta `2487859205019090` (agregar la cuenta al portfolio gonvra1)
3. Activar el envío de email/teléfono para subir la calidad de coincidencia
4. Recién después: pautar

### ❌ Límite conocido de Claude Code
El token del Shopify CLI **no tiene scope de `orders`** (`Access denied for orders field`), así que
desde Claude Code no se puede verificar el pedido. Lo hace Codex (browser) o Matías.


## 🚀 Estado del equipo de agentes (2026-09-19)

**El equipo está VIVO y produciendo.** 16 tareas `done` en el tablero `gonvra`.
- Cron activo: `GONVRA2 — JEFE — resumen único 21 ART` (`0 21 * * *`) → Telegram 7697535044
- Entregables reales en `~/Claude/gonvra2/<agente>/`: COPY, TIKTOKER (3 guiones),
  INSTAGRAMER (calendario 14-20/09), ESPIA (7 anuncios competencia 30+ días), TIENDA, JEFE.

### ⚠️ Cuello de botella: TODO espera aprobación de Matías
La regla "proponen, Matías aprueba" funciona, pero nada se aprobó todavía ⇒ nada publicado.

### Landing nueva — EN VISTA PREVIA (2026-09-19)
- Copia de trabajo: `~/Documents/Codex/tiendas/jm60sa-cp/work-copy-2026-09-18` (tema completo, 533 archivos)
- Subida al tema **#148200751219 "GONVRA - Landing optimizada 07 Sep"** (NO publicado)
- 🔗 **Vista previa:** https://gonvra.com/?preview_theme_id=148200751219 (verificado HTTP 200)
- Cambia 5 archivos: `templates/index.json`, `templates/product.gonvra.json`,
  `sections/gv-home.liquid`, `sections/gv-producto.liquid`, `sections/gv-faq.liquid`
- Qué hace: hero "Una sola rasuradora para toda tu rutina", CTA "Quiero mi rasuradora",
  saca "Antes y después" y "Comparativa" (sin pruebas), desactiva contador de urgencia y cuotas,
  elimina claims no verificables (agua/enjuague, USB, medidas, potencia, autonomía).
- ⏳ Falta: que Matías la mire y decida publicarla.

### Próxima pieza orgánica recomendada por el JEFE
Guion 1 de TikTok/Reel. Hook: "¿Otro aparato más?". Honesto: aclara que todavía no hay muestra
física. CTA: "Entrá a la ficha completa" → gonvra.com.


## 🖥️ VPS — el equipo corre 24/7 (migrado 2026-09-20)

**El equipo YA NO depende de la laptop.** Corre en un servidor propio.

| | |
|---|---|
| Proveedor | **Alibaba Cloud** — Simple Application Server |
| IP pública | **47.85.84.11** |
| Región | US (Virginia) · ping ~142 ms desde AR |
| Specs | Ubuntu 24.04 · 2 vCPU · 1 GB RAM · 30 GB |
| Costo | **$5/mes** (mensual, sin auto-renovación) |
| Vence | **21 de octubre de 2026** ⚠️ renovar a mano |
| Usuario | `gonvra` (con linger) · root por SSH |
| Llave SSH | `~/.ssh/gonvra_vps` (privada, en la laptop) |

### Acceso
```bash
ssh -i ~/.ssh/gonvra_vps root@47.85.84.11
sudo -u gonvra bash -c 'export PATH=$HOME/.local/bin:$PATH; hermes cron list'
```

### Qué se migró y verificó
- ✅ Hermes v0.21.3 (clonado de GitHub + venv en `/home/gonvra/.hermes/hermes-agent`)
- ✅ Bot de Telegram: **"Connected to Telegram (polling mode)"**
- ✅ Tablero Kanban `gonvra` con 20 tareas
- ✅ Historial completo de sesiones · entregables de los 15 agentes · SEMÁFORO
- ✅ Cron `GONVRA2 — JEFE — resumen único 21 ART` (`0 21 * * *`)
- ✅ Zona horaria Argentina · firewall (solo SSH) · arranque automático (`systemctl enable`)

### ⚠️ Cosas importantes
1. **El gateway de la laptop quedó APAGADO y deshabilitado.** El bot de Telegram solo puede correr
   en UN lugar a la vez (error `Conflict: terminated by other getUpdates request`). Si algún día se
   reactiva en la laptop, el del servidor se cae.
2. **Renovar antes del 21/10** o el servidor se da de baja.
3. El binario `hermes` en el servidor está en `/home/gonvra/.local/bin/hermes` (wrapper al venv).
4. Aviso pendiente: `Nous OAuth quarantined (invalid_grant)` — no afecta si el proveedor es
   openai-codex, pero revisar si algún agente falla por autenticación.


## 🖥️ MUDANZA AL SERVIDOR — 2026-09-20 (Hermes ya NO corre en la laptop)

**Hermes vive ahora en un VPS de Alibaba Cloud: `47.85.84.11`**
- Ruta del proyecto en el servidor: **`/home/gonvra/Claude/gonvra2`** (⚠️ NO `/home/matiigonzz/...`)
- Modelo: **GPT-6 Astra / OpenAI Codex** · cuota 90% sesión, 98% semanal
- Respaldo automático: **Gemini**
- 🚫 **PROHIBIDOS: API Next y DeepSeek.** Permitidos: NVIDIA (Qwen 3) y otros
  (NVIDIA todavía sin credenciales cargadas en el server).
- Migrado OK: CONTEXTO.md, tablero `gonvra` (20 tareas done), 31 perfiles `gonvra-*`.
- SEMÁFORO pasó a **rutas relativas**; snapshots históricos de aprobaciones conservados.

### ⚠️ El gateway LOCAL quedó apagado a propósito
`systemctl --user disable --now hermes-gateway.service` — Telegram **no permite dos pollers** del
mismo bot. El local fallaba por conflicto. **El servidor es el único dueño del bot
@gonvra_semaforo_bot.** No reactivar el local.

### ✅ Cron verificado de punta a punta (20/09 18:58)
- Job `2e1a2719befe` "GONVRA2 — JEFE — resumen único 21 ART" (`0 21 * * *`)
- Problema inicial: workdir apuntaba a la ruta vieja de la PC → fallaba.
- Segundo problema: timeout de 20s era muy corto (exit 124). **Con 600s funciona.**
- Resultado: `delivery_outcome: delivered` + archivo `jefe/2026-09-20.md` creado.
- 📌 **Lección: los cron de agentes necesitan timeout de ~600s, no 20s.**

### Cómo se le habla a Hermes ahora
**Solo por Telegram** (@gonvra_semaforo_bot). Claude Code **no tiene acceso SSH** al servidor
(sin clave ni password; la conexión hace timeout). Flujo actual: Claude Code redacta el mensaje →
Matías lo pega en Telegram → pega la respuesta de vuelta.

### Estado del contenido (según JEFE 20/09)
- ✅ CREATIVO produjo **5 placas de carrusel + 3 historias** (archivos verificados)
- ⏳ TikTok: portada y guion listos, **falta el video final** (lo tiene que grabar Matías)
- ⏳ Calendario de Instagram con **fechas vencidas** (14-25/09), hay que recalendarizar
- ⏳ PRECIOS: faltan comisión real de MP, logística e impuestos para cerrar el CPA


## ✅ EQUIPO 24/7 OPERATIVO — 2026-09-20 19:52 (HITO)

**Los 11 agentes se ejecutaron de verdad y escribieron sus archivos.** Gateway habilitado para
arrancar solo si se reinicia el servidor.

### Grilla activa (hora Argentina)
`00 GUARDIA · 02 ESPIA · 04 GUARDIA · 06 ANALISTA · 08 GUARDIA · 09 COPY · 10 TIKTOKER ·
11 INSTAGRAMER · 12 GUARDIA · 13 CRO · 15 CREATIVO · 16 GUARDIA · 19 CAZADOR · 20 GUARDIA ·
21 JEFE · 22 GUARDIA · viernes 17 LEGAL`

### Modelos (configuración final que funciona)
| Rol | Modelo |
|---|---|
| Principal (JEFE, CRO, COPY) | **GPT-6 Astra / OpenAI Codex** |
| Grilla barata (el resto) | **GPT-5.6 Sol / Codex** |
| Respaldo | **Gemini 3.6 Flash** (probado: `RESPALDO_OK`) |

⚠️ **Gemini es free tier y se satura** si corren varios agentes juntos → por eso la grilla usa
GPT-5.6 Sol, no Gemini.
🚫 Sin usar: NVIDIA/Qwen (**falta cargar credenciales**), Nous (revocado), API Next y DeepSeek (prohibidos).

### 🐕 Watchdog anti-caídas (cada 5 min)
Espera 60s, reintenta una vez, y **avisa por Telegram** si falla o si no queda ningún modelo.
Resuelve el problema de "se queda trabado en silencio".

### 📌 Lecciones aprendidas
1. **Timeout de cron: 600s**, no 20s (con 20s da exit 124).
2. **No lanzar todos los agentes a la vez** → rate limit. Escalonarlos en la grilla.
3. Gemini 2.5 fue dado de baja por Google → usar **gemini-3.6-flash**.

### 📅 Contenido listo para aprobar
- **21/09:** historia de 3 pantallas · **22/09:** carrusel de 5 placas
- Piezas corregidas contra el copy aprobado, sin textos cortados. **Nada publicado todavía.**
- ⏳ Reel pendiente: **depende del video que grabe Matías**


## 🎛️ MISSION CONTROL EN EL SERVIDOR — 2026-09-21 (HITO)

**Panel de control completo corriendo 24/7 en el VPS.**
Ruta: `/home/gonvra/Claude/gonvra2/mission-control/`

### Cómo entrar
1. Credenciales (una sola vez): `ssh gonvra@47.85.84.11 /home/gonvra/.local/bin/gonvra-access`
2. Túnel: `ssh -N -L 8080:127.0.0.1:8080 -L 5678:127.0.0.1:5678 gonvra@47.85.84.11`
   (o el script `~/Claude/gonvra2/mission-control/ABRIR-PANEL-SERVIDOR.sh` / ícono del escritorio)
3. Navegador: **Mission Control** `http://localhost:8080` · **n8n** `http://localhost:5678`
⚠️ Ninguno está expuesto a internet. Solo por túnel SSH + usuario y contraseña.

### Qué tiene el panel
- **Oficina pixel art**: los 15 agentes en sus escritorios, caminan a la mesa de reuniones al hablar
- **Estado en vivo desde los cron REALES** + si la última corrida salió bien o falló
- **Chat estilo WhatsApp**: grupal e individual. **Conectado directo a Hermes** (probado: `MC_CHAT_OK`)
- **Agentes**: ficha, personalidad, herramientas y **selector de modelo**
- **Tareas** del kanban con tilde · **Actividad de hoy** · **Herramientas** · **Conocimiento**
- **Consumo diario de tokens** (entrada, salida, caché, razonamiento)

### Verificaciones que hizo Hermes
6 pruebas automáticas OK · sin contraseña → HTTP 401 · con contraseña → HTTP 200 ·
cron horario `cf181fbfbc24` probado (`succeeded`) · avisa por Telegram si falla

### Servicios 24/7 (enabled + active, arrancan solos al reiniciar)
- Mission Control → `127.0.0.1:8080`
- **n8n 2.39.8** → `127.0.0.1:5678` (Node 24 local, SQLite reparada). Falta crear la cuenta admin
  desde el navegador la primera vez.

## 🤖 CADENA DE MODELOS (actualizada 2026-09-21, probada)
| Rol | Modelo |
|---|---|
| Principal (JEFE, CRO, COPY) | `gpt-6-astra` · OpenAI Codex |
| Económico (resto) | `gpt-5.6-sol` · OpenAI Codex |
| **Respaldo 1** | **`moonshotai/kimi-k3` vía NVIDIA** ✅ probado con failover real (`KIMI_FAILOVER_OK`) |
| Última opción | `gemini-3.6-flash` (da 429 seguido, quedó relegado) |
| ⏳ Falta | OpenRouter — sin credencial |
| 🚫 Prohibidos | DeepSeek · API Next/APINEX (hay claves guardadas pero NO se usan) |
| ❌ Roto | Kimi China (credencial vieja, da 401) |


## 🔴 CAÍDA DEL SERVIDOR — 2026-09-21 (LECCIÓN IMPORTANTE)

**El VPS de Alibaba se colgó repetidamente y quedó inutilizable.**

### Specs reales del servidor (el problema de fondo)
`Ubuntu-gbrh` · 2 vCPU · **1 GiB RAM (894 MB usables)** · 30 GB disco · `47.85.84.11`

### Síntomas
- SSH: acepta TCP pero **timeout en "banner exchange"** (no completa el saludo)
- La consola web de Alibaba también falla (`SocketTimeoutException`) porque usa SSH
- Hermes deja de leer Telegram (mensajes se acumulan sin leer)
- Responde al ping → la máquina está viva, los servicios no
- `load average: 2.00` **recién arrancado** en 2 vCPU = CPU al 100% desde el arranque

### Diagnóstico
- **NO era el disco** (40% usado, 17 GB libres)
- Swap: 3 GB configurada pero **sin usar** (0 B)
- Memoria: 717-753 MB usados de 894 MB, **~140-177 MB disponibles incluso con agentes pausados**
- Lo que no entra: Ubuntu (~200 MB) + Hermes/agentes (~300-400 MB) + Mission Control (~50 MB)
  + **n8n/Node.js (~400 MB)**

### Qué se intentó
1. Reinicio desde el panel → volvió unos minutos y se colgó otra vez
2. "Cazadores" (scripts que esperan la ventana de SSH y actúan) → lograron apagar n8n y
   ejecutar `hermes pause`, pero el servidor se volvía a caer
3. Agregar swap → ya había 3 GB, no se usaba

### ✅ SOLUCIÓN ADOPTADA (costo $0)
**Hermes volvió a la laptop** (15 GB RAM, sobra):
```bash
systemctl --user enable --now hermes-gateway.service
```
El bot de Telegram volvió a funcionar en minutos y consumió los mensajes atrasados.

### 📌 LECCIONES
1. **1 GB de RAM no alcanza** para Hermes + 15 agentes + Mission Control + n8n.
2. **n8n (Node.js) es el más pesado** (~400 MB). Se borró: nunca se usó, cero flujos creados.
3. Un servidor sin SSH **no se arregla por SSH**. Hay que tener acceso por consola VNC real
   (la de Alibaba Simple Application Server usa SSH, así que no sirve de rescate).
4. **Solo UNO puede escuchar el bot de Telegram.** Si corre el local y el del servidor, pelean.
   Al caerse el del servidor, reactivar el local lo recupera automáticamente.

### 🗺️ PLAN ACORDADO CON MATÍAS
1. **Ahora:** construir el sistema 100% en la laptop (gratis, RAM de sobra)
2. **Después:** cuando esté completo y probado, mudarlo a un servidor **con al menos 2 GB**
3. Mientras tanto: rescatar del servidor lo que se construyó allá
   (`conversaciones/`, `conocimiento/`, informes nuevos, `mission-control/server.py`)
   → queda en `~/Claude/gonvra2/RESCATE-SERVIDOR/`

## Promesas REALES (lo único que se puede afirmar)

- ✅ Envío gratis a todo el país, con seguimiento
- ✅ Garantía 10 días · arrepentimiento 10 días corridos (Ley 24.240)
- ✅ Despacho 24-48 h hábiles · entrega estimada 12-20 días
- ✅ Pago con tarjeta o Mercado Pago
- ❌ **Prohibido**: escasez falsa, contadores truchos, reseñas inventadas, cifras de batería o
  potencia no confirmadas

## Acceso técnico (para Claude Code)

El Shopify CLI está autenticado para esta tienda:
```bash
cd ~/Documents/Codex/tiendas/jm60sa-cp
npx shopify theme pull --store jm60sa-cp.myshopify.com --theme 148158414963 --path ./live-theme
npx shopify theme push --store jm60sa-cp.myshopify.com --theme 148158414963 --path ./live-theme --allow-live --force --only "sections/X.liquid"
npx shopify store execute --store jm60sa-cp.myshopify.com --query-file X.graphql --json
```
- ✅ **SE PUEDE:** leer productos · leer y escribir el **tema**
- ❌ **NO SE PUEDE** (falta scope en el token): **políticas, páginas, themes por Admin API**.
  Eso lo hace Matías a mano en el panel.

## Equipo de agentes

- Contexto vigente: `~/Claude/gonvra2/CONTEXTO.md`
- Entregables: `~/Claude/gonvra2/<agente>/AAAA-MM-DD.md`
- Infraestructura de Hermes **ya construida y reutilizable**: bot de Telegram, SEMÁFORO con
  snapshot y revalidación, tablero Kanban `gonvra`, perfiles `gonvra-*`.
- Con **un solo producto** alcanzan 15 agentes: JEFE, ANALISTA, GUARDIA, CRO, CAZADOR, PRECIOS,
  COPY, CREATIVO, TIKTOKER, INSTAGRAMER, ESPIA, MEDIABUYER, TIENDA, MENSAJERO, LEGAL.
  Pausar SCOUT, PODADOR, AUTODS, MARKETPLACES, PROVEEDORES (sin trabajo con un solo producto).

## Tono de marca

Cercano, argentino, honesto, directo. Le habla a un tipo que quiere resolver su afeitado sin
vueltas. El diferencial **no es el precio**: es envío gratis + garantía 10 días + atención real
por WhatsApp. Cero urgencia falsa.
