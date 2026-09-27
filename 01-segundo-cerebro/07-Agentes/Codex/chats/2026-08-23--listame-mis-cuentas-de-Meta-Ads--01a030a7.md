---
tool: Codex
session_id: 01a030a7-a05a-7a33-a648-e1874085195a
fecha: 2026-08-23 22:04
titulo: "listame mis cuentas de Meta Ads"
tags: [chat, agente, codex]
---

# 💬 listame mis cuentas de Meta Ads
> **Codex** · 2026-08-23 22:04 · `01a030a7-a05a-7a33-a648-e1874085195a`

---

### 🧑 Vos  <small>2026-08-23 22:04</small>

listame mis cuentas de Meta Ads

### 🤖 Codex  <small>2026-08-23 22:04</small>

[external_agent_tool_call: Read]
file: /home/matiigonzz/.claude/projects/-home-matiigonzz-Claude/memory/gonvra-meta-ads.md
[/external_agent_tool_call]

### 🤖 Codex  <small>2026-08-23 22:04</small>

[external_agent_tool_result]
<system-reminder>This memory is 19 days old. Memories are point-in-time observations, not live state — claims about code behavior or file:line citations may be outdated. Verify against current code before asserting as fact.</system-reminder>
1	---
2	name: gonvra-meta-ads
3	description: "GONVRA — cuenta de Meta Ads: IDs, estado del píxel, y campaña de prospección creada en pausa"
4	metadata: 
5	  node_type: memory
6	  type: project
7	  originSessionId: 2b6568b1-1ec9-4789-b366-6ba1e0fb2df8
8	  modified: 2026-08-01T07:16:15.503Z
9	---
10	
11	Campaña de Meta Ads para [[gonvra-shopify-store]]. Acceso vía el MCP de Meta Ads (`ads_*`).
12	
13	**✅ CUENTA HABILITADA (verificado 2026-08-01):** la cuenta **1482478863413097 ("cuenta 1", Gonvra products) volvió a aparecer y AHORA `is_ads_mcp_enabled=true`** ⇒ SÍ se puede crear campaña/anuncio por API. (La 2487859205019090 sigue sin habilitar; la 27009…096 sigue UNSETTLED.) El acceso a estas cuentas fluctúa día a día — verificar siempre con ads_get_ad_accounts al empezar.
14	
15	**✅ PÍXEL VIVO (verificado 2026-08-01, corrige el dato viejo de "0 eventos"):** el dataset **TIENDA CEPILLO 1 (26889872433954472)** SÍ dispara — PageView + ViewContent (last_fired 31/07 23:55, y CAPI server-side también). Todavía **no hay AddToCart ni Purchase** (la tienda no tuvo ventas) ⇒ optimizar a Compra sigue siendo inviable. **OJO: hay un SEGUNDO píxel duplicado**, `3919766821491073`, que es el que la app de Shopify inyecta en el storefront (`webPixelsConfigList`, apiClientId 2329312) y que NO pertenece a la cuenta de anuncios — recibe los mismos ViewContent. Conviene unificar todo en 26889872433954472. **No hay Instagram vinculado** (ads_get_ig_accounts → []) ⇒ los anuncios NO se entregan en IG/Reels; vincular @gonvra.pets es la mejora de mayor impacto.
16	
17	**🚀 CAMPAÑA DE TEST $4.000 TOTAL — CREADA POR API 2026-08-01, EN PAUSA** (el usuario confirmó que son $4.000 **en total**, no por día):
18	- Campaña **"GONVRA | Test $4.000 | Video Cepillo vs Botella"** id **120250532987940505** — OUTCOME_SALES, CBO **lifetime_budget $4.000** (400000 cents), del **2/8/2026 00:00 al 4/8/2026 00:00** (2 días; el mínimo diario de la cuenta es $1.500,38 ⇒ 3 días costarían $4.510).
19	- Conjunto **"Broad | AR 18-65 | Vistas de landing"** id **120250532993690505** — **optimization_goal LANDING_PAGE_VIEWS** (no Purchase, porque el píxel no tiene compras), promoted_object `{pixel_id, custom_event_type:PURCHASE}` (sin custom_event_type da error 1885014), Advantage+ Audience, AR, WEBSITE.
20	- 2 anuncios PAUSED con imagen: `P1-D2-IMG-PROBLEMA-cepillo-v1` id 120250533057040505 (creative 2340102736397811) y `P3-D1-IMG-PROBLEMA-botella-v1` id 120250533060100505 (creative 2479471189241161). CTA SHOP_NOW, UTMs `test4000_ago26`.
21	- **`ads_creative_upload_video` SIGUE bloqueado** en esta cuenta (probado con URL pública del CDN de Shopify: mismo error "gradually rolled out") ⇒ los 2 videos hay que subirlos a mano en Ads Manager. URLs públicas de los videos en Shopify: `https://cdn.shopify.com/videos/c/o/v/09fb7aca6cbe4273b2e1cfaa350620ec.mp4` (cepillo) y `.../ecf37493667b4076ac76a51b97f94173.mp4` (botella).
22	
23	**Estructura de creativos (Andrómeda) 2026-08-01:** archivo `Descargas/campaña/gonvra-estructura-creativos-andromeda.md` — 5 buyer personas, 12 dolores, 36 creativos, nomenclatura `P#-D#-FORMATO-ANGULO-v#`, olas de producción y filtro de rentabilidad (no pautar en frío productos <$16.990).
24	
25	**🚀 CAMPAÑA ANTERIOR CREADA POR API 2026-08-01 (TODA EN PAUSA, cero gasto)** en cuenta 1482478863413097:
26	- Campaña **"GONVRA | TOFU | Prospección (Cama)"** id **120250532602990505** — OUTCOME_SALES, CBO $4.000/día (400000 cents), PAUSED.
27	- Conjunto **"Broad | AR | Compra"** id **120250532610800505** — OFFSITE_CONVERSIONS/PURCHASE al píxel 26889872433954472, Advantage+ Audience, AR 18-65, WEBSITE, atrib 7d clic/1d view.
28	- 2 anuncios PAUSED con imagen (foto del producto, ya diseñada y sin typos): Anuncio 1 id 1202505326299...
[/external_agent_tool_result]

### 🤖 Codex  <small>2026-08-23 22:04</small>

No tengo el MCP de Meta Ads (`ads_*`) conectado en esta sesión, así que no puedo consultarlas en vivo ahora mismo. Pero según lo que tengo registrado de tu cuenta (última verificación **2026-08-01**), estas son tus cuentas de Meta Ads:

| Cuenta (ID) | Nombre / negocio | Estado | Uso |
|---|---|---|---|
| **1482478863413097** | "cuenta 1" — Gonvra products (ARS, con medio de pago) | ✅ ACTIVE, `is_ads_mcp_enabled=true` | La operativa — acá están tus campañas |
| **2487859205019090** | — | ⚠️ Sin habilitar por API | No usar |
| **27009241552077096** | "cuenta 2" | ⚠️ UNSETTLED | No usar |

Datos asociados a la cuenta buena (1482478863413097):
- **Página FB:** "Gonvra pets" (page_id 1125904760604828)
- **Píxel/dataset:** "TIENDA CEPILLO 1" (26889872433954472) — vivo (PageView + ViewContent), sin AddToCart/Purchase todavía
- **Instagram:** ninguno vinculado
- **Campañas creadas (todas en PAUSA):** Test $4.000 (120250532987940505), Prospección Cama (120250532602990505), y la vieja de Envío Gratis (120250360311680505)

⚠️ **Ojo:** el acceso a estas cuentas fluctúa día a día. Para tener la lista real y actualizada hoy hay que correr `ads_get_ad_accounts` con el MCP de Meta Ads conectado.

¿Querés que revisemos por qué el MCP de Meta Ads no está disponible en esta sesión, o te alcanza con esta info de referencia?

### 🧑 Vos  <small>2026-08-23 22:04</small>

Pero ¿de qué cuenta? Porque yo quiero entrar a alguna de ellas, tipo se llama Gombra cero punto Gmail punto com. así literal, y se llama Matías González. Eso.

### 🤖 Codex  <small>2026-08-23 22:04</small>

Ah, entiendo — vos me estás hablando del **usuario/login de Facebook** (el mail y el nombre con los que entrás), no del número de cuenta publicitaria. Son dos cosas distintas:

- **El login personal de Facebook/Meta** → un mail (ej. `gonvra0@gmail.com`) + un nombre de perfil (**Matías González**). Con eso te logueás.
- **La cuenta publicitaria (Ad Account)** → es un número largo (ej. `1482478863413097`) que vive *dentro* de ese perfil, en el Business Manager.

Eso que me decís —**"gonvra0@gmail.com" (o parecido) + perfil "Matías González"**— sería tu **login de Facebook** para entrar a Ads Manager. Pero acá tengo que ser sincero: **ese dato del mail y nombre de login no lo tengo registrado en mi memoria**. Yo solo tengo guardados los IDs de las cuentas publicitarias, la página ("Gonvra pets") y el píxel — no las credenciales de acceso.

Dato que sí me cierra: tu página de Facebook se llama **"Gonvra pets"**, así que es coherente que el perfil "Matías González" con ese Gmail sea el dueño/admin.

Para no marearte, decime qué necesitás exactamente:

1. **Entrar a Ads Manager** → andá a [business.facebook.com](https://business.facebook.com) o [adsmanager.facebook.com](https://adsmanager.facebook.com) y logueate con ese mail + tu contraseña. Ahí vas a ver la cuenta **Gonvra products (1482478863413097)**.
2. **¿Te olvidaste el mail exacto o la contraseña?** → eso lo recuperás desde la pantalla de login de Facebook (yo no lo tengo).
3. **¿Querés que confirme cuál es el mail dueño de la cuenta?** → eso sí lo podría chequear, pero necesito el **MCP de Meta Ads conectado** (ahora no lo está).

¿Cuál de las tres es lo que buscás?

### 🧑 Vos  <small>2026-08-23 22:04</small>

Pero las campañas, ¿cómo se llaman?

### 🤖 Codex  <small>2026-08-23 22:04</small>

Estas son las campañas que tenés creadas en la cuenta **Gonvra products (1482478863413097)** — todas quedaron **en PAUSA** (cero gasto):

| Campaña | ID | Presupuesto | Estado |
|---|---|---|---|
| **GONVRA \| Test $4.000 \| Video Cepillo vs Botella** | 120250532987940505 | $4.000 total (2 días) | ⏸️ En pausa |
| **GONVRA \| TOFU \| Prospección (Cama)** | 120250532602990505 | $4.000/día (CBO) | ⏸️ En pausa |
| **GONVRA \| Ventas – Prospección (Envío GRATIS)** | 120250360311680505 | $3.300/día (CBO) | ⏸️ En pausa (la más vieja) |

Notas:
- Las tres son objetivo **Ventas (OUTCOME_SALES)**.
- La "Test $4.000" tiene 2 anuncios con imagen (cepillo y botella); los videos había que subirlos a mano en Ads Manager.
- La "Prospección (Cama)" apunta a `gonvra.com/products/cama-redonda-ortopedica-mascotas`.

⚠️ Ojo: esto es de mi última verificación (**2026-08-01**). Si desde entonces creaste, renombraste o borraste alguna, no me va a figurar. Para ver la lista exacta de hoy hay que abrir Ads Manager o conectar el MCP de Meta Ads.

¿Querés que te arme un resumen de qué anuncios tiene cada una, o buscás cuál prender primero?
