---
tags: [gonvra, handoff, resumen, agentes, mission-control]
actualizado: 2026-09-21
estado: sistema funcionando en la laptop
---

# 📋 GONVRA — Resumen completo del proyecto (handoff)

> **Para el próximo chat:** este archivo es el punto de partida. Leé también
> [[GONVRA - Rasuradora (VIGENTE)]] (detalle técnico) y `~/Claude/gonvra2/CONTEXTO.md`
> (el que leen los agentes).

---

## 1. QUÉ ES ESTO

Matías tiene una tienda Shopify en Argentina y quiere un **equipo de agentes de IA trabajando
24/7** para que la tienda genere plata. El objetivo es uno solo: **ventas**.

**Usuario:** Matías. **No técnico.** Hablarle en español rioplatense, sin jerga, y decirle
exactamente qué botón apretar.

### La tienda (estado actual)
| | |
|---|---|
| Marca | **GONVRA** · gonvra.com |
| Shopify | `jm60sa-cp.myshopify.com` |
| Producto | **Rasuradora Integral Recargable — Rostro y Cuerpo** · **$36.900** |
| Handle | `face-body-electric-shaver` |
| Costo real | **$8.672,90** (del campo "costo" de Shopify) → margen bruto 76% |
| Contacto | `gonvra0@gmail.com` · WhatsApp **+54 9 11 5376-7293** |
| Tema LIVE | `GONVRA — Landing de vista previa` **#148158414963** |

⚠️ **Hubo DOS cambios de nicho.** No confundirse:
1. GONVRA empezó como tienda de **mascotas** (`9em58g-tt.myshopify.com`) → **abandonada**
2. Después fue **"Helio"**, una afeitadora mini → **producto descartado, NO nombrarlo**
3. Hoy es **GONVRA · rasuradora integral** (cuidado personal masculino)

---

## 2. TODO LO QUE SE HIZO

### ✅ La tienda (resuelto y verificado en vivo)
- **Checkout que cobra**: se desactivó PayPal, quedó solo Mercado Pago Tarjetas
- **Las 4 políticas publicadas** (envíos, reembolso, términos, privacidad) — antes 3 daban 404
- **Garantía y arrepentimiento unificados en 10 días** (antes había contradicción 30 vs 10)
- **Botón de arrepentimiento** en el footer (obligatorio por ley argentina)
- **WhatsApp flotante** + mail y teléfono visibles y clickeables
- **Dominio gonvra.com** apuntando a la tienda
- **Nombre de la tienda** corregido (decía "Mi tienda")
- **Olas (`gv-wave`) responsive** — en PC se veían estiradas como manchones
- **"Antes y después"** restaurado en la home y agregado a la ficha de producto
- **Packs**: Individual · Dúo (-10%) · Trío (-15%)

### ✅ El equipo de agentes
- **15 agentes activos** con personalidad, herramientas y horario propio
- **Tablero Kanban `gonvra`** con tareas, estados y dependencias
- **SEMÁFORO productivo**: aprobaciones por Telegram con *snapshot* y revalidación
  (si cambia el precio/stock entre que aprobás y que ejecuta, **se bloquea solo**)
- **Grilla de cron**: reconstruida el 21/09 con 11 jobs reales (antes había **1 solo**, el resto era ficción del panel)
- **Watchdog cada 5 min**: si falla un modelo, reintenta y avisa por Telegram
- **Bot de Telegram** `@gonvra_semaforo_bot`

### ✅ Mission Control (panel visual)
Oficina pixel art donde se ve a los 15 agentes en sus escritorios:
- Estado en vivo: trabajando / descansando / en pausa / a pedido
- **Caminan a la mesa de reuniones** cuando hablan en el chat, y vuelven
- Chat estilo WhatsApp: grupal + privado con cada agente
- Fichas con personalidad, herramientas y **modelo de IA** (con selector para cambiarlo)
- Tareas con tilde, actividad del día, herramientas conectadas, conocimiento
- Archivos: `~/Claude/gonvra2/mission-control/` (`mission-control.html`, `generar-datos.py`,
  `oficina.jpg`, `agentes/*.png`)
- Abrir con: `~/Claude/gonvra2/mission-control/ABRIR-MISSION-CONTROL.sh` o el ícono del escritorio
- ⚠️ **NO abrir el HTML con doble clic / `xdg-open`**: el navegador bloquea `datos.json` y se ve
  vacío. **Siempre por `localhost`.**

### ✅ Meta / píxel
- Píxel **`3919766821491073`** conectado a la cuenta de anuncios **`2487859205019090`**
- El píxel viejo (`26889872433954472`, "TIENDA CEPILLO 1") quedó relegado
- ⚠️ **Nunca disparó un `Purchase`** — porque **todavía no hubo ninguna venta**, no es un bug

### ✅ Contenido producido (listo, sin publicar)
- **3 guiones de TikTok** (uno adaptado para grabar sin el producto en mano)
- **5 placas de carrusel + 3 historias** de Instagram
- **Espionaje**: 7 anuncios de la competencia con 30+ días activos
- **Video 1 terminado**: `~/Claude/gonvra2/videos/GONVRA-video1-cuantos-aparatos.mp4`
  (23 s, 9:16, hecho con ffmpeg usando las 3 fotos reales del producto, sin voz para
  ponerle sonido de tendencia en TikTok)

### ✅ Herramientas creadas
| Script | Para qué |
|---|---|
| `~/Claude/scripts/video-intel.py` | Espía videos de YouTube/TikTok/IG sacando datos + transcripción **sin gastar tokens**. `--scan 20` para escanear un canal barato |
| `~/Claude/scripts/export-chats-to-obsidian.py` | Exporta los chats de Claude Code, Codex y Hermes a Obsidian cada 30 min (memoria compartida entre agentes) |
| `~/Claude/scripts/genimage-replicate.py` | Genera imágenes (nano-banana). **Siempre cerrar los prompts con "no text"** |

---

## 3. NÚMEROS DEL NEGOCIO (calculados por PRECIOS)

Precio **$36.900** · costo **$8.672,90** · margen bruto **76%**

**Cuánto podés pagar por conseguir UNA venta (CPA):**
| Escenario | CPA máximo |
|---|---|
| 🟢 Mejor (envío $0, monotributo) | **$19.453** |
| 🟡 Base (envío $5.000, monotributo) | **$15.453** |
| 🔴 Peor (envío $9.000, resp. inscripto) | **$7.129** |

👉 **Con menos de $7.129 por venta, ganás plata seguro.** Ese es el techo prudente para arrancar.
Los descuentos de Dúo y Trío **no rompen el margen**.

**Faltan 3 datos de Matías** para cerrarlo: comisión real de Mercado Pago, costo de envío
por pedido, y si es monotributista o responsable inscripto.

---

## 4. 💥 EL DESASTRE DEL SERVIDOR (21/09)

Se montó todo en un **VPS de Alibaba** (`47.85.84.11`) y funcionó unas horas… hasta que
**se colgó repetidamente y quedó inutilizable**.

**La causa:** el servidor tiene **1 GiB de RAM (894 MB usables)**. No entra:
Ubuntu (~200 MB) + Hermes y agentes (~350 MB) + Mission Control (~50 MB) + **n8n (~400 MB)**.

**Síntomas:** SSH acepta la conexión pero se cuelga en el saludo · la consola web de Alibaba
también falla (usa SSH) · Hermes deja de leer Telegram · `load average 2.00` recién arrancado.

**NO era el disco** (40% usado). Swap de 3 GB existía pero no se usaba.

### ✅ Solución adoptada (costo $0)
**Hermes volvió a la laptop** (15 GB de RAM):
```bash
systemctl --user enable --now hermes-gateway.service
```
El bot volvió a funcionar en minutos.

### 🗺️ Plan acordado
1. **Ahora:** construir el sistema **100% en la laptop** (gratis, RAM de sobra)
2. **Después:** cuando esté completo y probado, mudarlo a un servidor de **2 GB mínimo**
3. Rescatar del servidor lo que se hizo allá → `~/Claude/gonvra2/RESCATE-SERVIDOR/`
   (hay un script esperando la ventana de SSH; puede que nunca abra)

---

## 5. ⚠️ TRAMPAS APRENDIDAS (no repetir)

1. **Verificar antes de afirmar.** Varias veces di por pendiente algo que Matías ya había hecho.
   Chequear en vivo con `curl` antes de decir que algo falta.
2. **`theme pull` SIEMPRE antes de tocar el tema.** La copia local se desactualiza y un agente
   asumió que una sección existía cuando ya estaba borrada del live.
3. **Los cron de agentes necesitan timeout de 600 s**, no 20 (con 20 da exit 124).
4. **No lanzar todos los agentes a la vez** → rate limit. Escalonarlos.
5. **Solo UNO puede escuchar el bot de Telegram.** Si corren el local y el del servidor, pelean.
6. **Abrir el Mission Control por `localhost`**, nunca con `file://`.
7. **El catálogo es dinámico**: ningún agente debe hardcodear productos, se leen en vivo de Shopify.
8. **Cero mentiras en el marketing**: nada de escasez falsa, contadores truchos ni reseñas
   inventadas. El inventario dice 50.000 pero es el default del proveedor, **no es stock real**.
9. **Dictado**: cuando Matías dice "compra" o "gombra" está diciendo **GONVRA**.

---

## 6. 🤖 MODELOS DE IA

| Rol | Modelo |
|---|---|
| Principal (JEFE, CRO, COPY) | `gpt-6-astra` · OpenAI Codex |
| Económico (el resto) | `gpt-5.6-sol` · OpenAI Codex |
| **Respaldo** | **`moonshotai/kimi-k3` vía NVIDIA** ✅ probado con failover real |
| Última opción | `gemini-3.6-flash` (da 429 seguido, relegado) |
| ⏳ Falta | OpenRouter (sin credencial) |
| 🚫 **PROHIBIDOS** | **DeepSeek · API Next/APINEX** (hay claves guardadas pero NO se usan) |

---

## 7. 🎯 QUÉ FALTA (en orden de importancia)

### 🔴 Lo único que trae plata
**Matías tiene que publicar contenido.** Todo el sistema está listo y esperando:
- El video 1 ya está hecho y sin publicar
- Las 5 placas y 3 historias de Instagram, sin publicar
- **Matías NO se graba a sí mismo y NO tiene el producto físico** → todos los guiones deben ser
  con fotos reales + texto + voz en off, sin persona en cámara

### 🟡 Datos que solo Matías puede conseguir
- Comisión efectiva de Mercado Pago
- Costo de envío por pedido
- Situación fiscal (monotributo o responsable inscripto)
- Token de Shopify Admin API con `read_orders` (para que CAZADOR vea carritos abandonados)
  — quedó a medias: la app "GONVRA Agentes" está creada e instalada, falta el token `shpat_`

### 🟢 Mejoras pendientes
- Reconstruir en la laptop lo que se hizo en el servidor (chats separados por agente,
  APRENDIZAJES.md, el `server.py` del chat)
- Instagram/TikTok API para publicar automático (necesita trámites de aprobación)
- Gmail y WhatsApp para MENSAJERO
- Cuando haya plata: servidor de 2 GB

---

## 8. 🔑 ACCESOS Y RUTAS

```
~/Claude/gonvra2/                      → entregables de los agentes + CONTEXTO.md
~/Claude/gonvra2/mission-control/      → el panel
~/Claude/gonvra2/videos/               → videos producidos
~/Claude/scripts/                      → video-intel.py, export-chats, genimage
~/Documents/Codex/tiendas/jm60sa-cp/   → el tema de Shopify (live-theme/)
~/OBSIDIAN/07-Agentes/<Herramienta>/chats/  → chats de todos los agentes (auto cada 30 min)
```

**Shopify CLI** (autenticado, desde `~/Documents/Codex/tiendas/jm60sa-cp`):
```bash
npx shopify theme pull --store jm60sa-cp.myshopify.com --theme 148158414963 --path ./live-theme
npx shopify theme push --store jm60sa-cp.myshopify.com --theme 148158414963 --path ./live-theme --allow-live --force --only "sections/X.liquid"
```
✅ Se puede: leer productos, leer/escribir el **tema**
❌ No se puede (falta scope): políticas, páginas, **pedidos** — eso lo hace Matías a mano

**Servidor** (caído, por si vuelve): `ssh gonvra-srv` (llave en `~/.ssh/gonvra_server`,
respaldo en `~/Descargas/RESPALDO-LLAVE-SERVIDOR/`)

---

## 9. 💬 CÓMO TRABAJAR CON MATÍAS

- **Verificá antes de hablar.** Si no estás seguro, chequealo en vivo.
- **Hacé vos lo que puedas hacer**, no le pases tareas que podés resolver.
- **Sé honesto con los límites.** Si algo no lo podés hacer, decilo de frente y ofrecé la
  alternativa. Prefiere eso a que le prometas algo que no se cumple.
- **Leé los chats de otros agentes en Obsidian** cuando te falte contexto, en vez de preguntar.
- **Anotá en Obsidian** todo lo que se confirme, para que no se pierda entre sesiones.
- Todo se mide en **pesos**. "Mejora la imagen de marca" no es un argumento.

---

## 10. 🔄 ACTUALIZACIÓN 21/09 (noche) — sesión Opus

### Lo que se descubrió (el resumen de arriba estaba mal en esto)
- **La "grilla 24/7" nunca existió.** Había **1 solo** cron activo (JEFE 21:00) y 2 apagados.
  No se perdió con el VPS: nunca se construyó.
- El Mission Control mostraba **horarios inventados** (GUARDIA "22:00" no existía) y decía que
  el servidor `47.85.84.11` estaba **"activo"** cuando está muerto hace días.
- `datos.json` estaba **congelado hacía más de un día**.
- Las 4 políticas **SÍ responden 200**. El resumen viejo daba a entender que podían fallar.

### Lo que quedó funcionando
- **11 jobs de cron activos**, escalonados uno por hora para no pegarle al rate limit:
  ESPIA 02 · ANALISTA 06 · COPY 09 · TIKTOKER 10 · INSTAGRAMER 11 · CRO 13 · CREATIVO 15 ·
  CAZADOR 19 · JEFE 21 · GUARDIA cada 4 h · Mission Control cada 30 min
- **GUARDIA es un script sin IA** (`~/.hermes/scripts/gonvra-guardia.sh`): chequea tienda,
  precio, motor de agentes, disco y RAM. **Si está todo bien no dice nada.** Cuesta $0.
  Probado en los dos caminos (sano = silencio, roto = avisa).
- **Solo el JEFE escribe a Telegram.** El resto entrega en silencio, o serían 17 mensajes/día.
- **Mission Control ya no puede mentir**: lee los horarios y los fallos directo de la grilla
  real (`jobs.json` + `executions.db`), no de una lista escrita a mano.
- **Auto-refresh cada 60 s** + el agente que falló se pinta **en rojo con led parpadeando**.
- **La laptop ya no se suspende** (ni con batería). Falta que Matías corra el comando de
  `sudo` para que tampoco se duerma al cerrar la tapa.
- **`CONECTORES.md`**: todos los links de APIs verificados + qué MCP usar para cada cosa.

### Trampas nuevas aprendidas
10. **`hermes cron create` quiere las opciones ANTES del horario.** Si las ponés después,
    tira "unrecognized arguments" y **no crea nada**.
11. **`gateway.pid` es un JSON**, no un número pelado. Sacarle los dígitos con `tr` pega
    el pid con el `start_time` y da falsa alarma.
12. **Hermes bloquea cron jobs que mencionen reiniciar el gateway** (anti-loop de respawn).
    Ni siquiera dentro del texto de un mensaje.
13. **El panel tenía los horarios hardcodeados.** Cualquier dato del panel escrito a mano
    se desincroniza y nadie se entera. Todo dato del panel debe salir de la fuente real.

### Qué falta (actualizado)
- 🔴 **Publicar el video 1.** Sigue sin publicar. Es lo único que trae plata.
- 🔴 **Token `shpat_` de Shopify** — 2 minutos, link exacto en `CONECTORES.md`.
- 🟡 El comando `sudo` de la tapa (está en el chat).
- 🟢 18 perfiles vacíos en `~/.hermes/profiles/` (cáscaras de 278 bytes). **No se borraron
  a propósito**: no molestan y borrar es irreversible.

---

## 11. 🔌 CONECTORES — cerrado el 22/09 (madrugada)

| Conector | Estado | Detalle |
|---|---|---|
| **Shopify** | ✅ ANDANDO | token `shpat_` por OAuth · 5/5 endpoints en 200 |
| **Gmail** | ✅ ANDANDO | 15 herramientas · autorizado con gonvra0@gmail.com |
| **Instagram** | ✅ ANDANDO | @gonvra1 BUSINESS · puede publicar · token 60 días |
| **Search Console** | ✅ verificado | ya estaba puesto desde el admin de Shopify |
| **Ad Library** | 🟡 instalado | Facebook lo bloquea (403). Se espía a mano |
| **TikTok / Meta Ads** | ❌ | no valen la pena todavía |

### Cómo se sacó el token de Shopify (el flujo viejo NO existe más)
El menú "Configuración de API de administrador → Instalar app" **fue eliminado por Shopify**.
Tampoco sirven: el `atkn_` del Dev Dashboard (401) ni los 6 tokens del Shopify CLI
(solo tienen permiso de *themes*, y con header `Authorization: Bearer`, no
`X-Shopify-Access-Token`).
**La única vía es OAuth** → `~/Claude/gonvra2/sacar-token-shopify.py` (interactivo,
detecta si pegás un texto de ejemplo, prueba el token y lo guarda solo).

### Lo que se descubrió al conectar Shopify
- **0 pedidos reales.** Cero ventas, confirmado por la API.
- **1 carrito abandonado de $129.475** del 8/09 — pero es **una prueba**, no un cliente:
  nombre "sjaj uwwu", mail aleatorio, dirección basura, duró 21 minutos.
- El precio del producto **era $64.737,52** y se bajó a **$36.900** (quedó como precio tachado).

### Avisos automáticos nuevos
- **`gonvra-ventas.sh` cada 15 min**: si entra un pedido, llega Telegram con cliente,
  monto y qué compró. Si no hay nada, silencio. Cuesta $0 (sin LLM).
  Probado con un pedido simulado: el aviso sale bien.

### Trampas nuevas
14. **Los links de OAuth de Google vencen en minutos.** No mandarlos por chat:
    usar `conectar-gmail.sh`, que genera uno fresco y lo abre al instante.
15. **Nunca dar comandos con huecos tipo `TU_CLIENT_ID`.** Matías los copia literal
    (pasó dos veces). Los scripts deben *preguntar* los datos.
16. **Las credenciales van en `~/.hermes/.gonvra-secrets.env`** (chmod 600).
    Nunca en los .md del proyecto ni en Obsidian.
