---
name: gonvra-meta-ads
description: "GONVRA — cuenta de Meta Ads: IDs, estado del píxel, y campaña de prospección creada en pausa"
metadata: 
  node_type: memory
  type: project
  originSessionId: 2b6568b1-1ec9-4789-b366-6ba1e0fb2df8
  modified: 2026-08-01T07:16:15.503Z
---

Campaña de Meta Ads para [[gonvra-shopify-store]]. Acceso vía el MCP de Meta Ads (`ads_*`).

**✅ CUENTA HABILITADA (verificado 2026-08-01):** la cuenta **1482478863413097 ("cuenta 1", Gonvra products) volvió a aparecer y AHORA `is_ads_mcp_enabled=true`** ⇒ SÍ se puede crear campaña/anuncio por API. (La 2487859205019090 sigue sin habilitar; la 27009…096 sigue UNSETTLED.) El acceso a estas cuentas fluctúa día a día — verificar siempre con ads_get_ad_accounts al empezar.

**✅ PÍXEL VIVO (verificado 2026-08-01, corrige el dato viejo de "0 eventos"):** el dataset **TIENDA CEPILLO 1 (26889872433954472)** SÍ dispara — PageView + ViewContent (last_fired 31/07 23:55, y CAPI server-side también). Todavía **no hay AddToCart ni Purchase** (la tienda no tuvo ventas) ⇒ optimizar a Compra sigue siendo inviable. **OJO: hay un SEGUNDO píxel duplicado**, `3919766821491073`, que es el que la app de Shopify inyecta en el storefront (`webPixelsConfigList`, apiClientId 2329312) y que NO pertenece a la cuenta de anuncios — recibe los mismos ViewContent. Conviene unificar todo en 26889872433954472. **No hay Instagram vinculado** (ads_get_ig_accounts → []) ⇒ los anuncios NO se entregan en IG/Reels; vincular @gonvra.pets es la mejora de mayor impacto.

**🚀 CAMPAÑA DE TEST $4.000 TOTAL — CREADA POR API 2026-08-01, EN PAUSA** (el usuario confirmó que son $4.000 **en total**, no por día):
- Campaña **"GONVRA | Test $4.000 | Video Cepillo vs Botella"** id **120250532987940505** — OUTCOME_SALES, CBO **lifetime_budget $4.000** (400000 cents), del **2/8/2026 00:00 al 4/8/2026 00:00** (2 días; el mínimo diario de la cuenta es $1.500,38 ⇒ 3 días costarían $4.510).
- Conjunto **"Broad | AR 18-65 | Vistas de landing"** id **120250532993690505** — **optimization_goal LANDING_PAGE_VIEWS** (no Purchase, porque el píxel no tiene compras), promoted_object `{pixel_id, custom_event_type:PURCHASE}` (sin custom_event_type da error 1885014), Advantage+ Audience, AR, WEBSITE.
- 2 anuncios PAUSED con imagen: `P1-D2-IMG-PROBLEMA-cepillo-v1` id 120250533057040505 (creative 2340102736397811) y `P3-D1-IMG-PROBLEMA-botella-v1` id 120250533060100505 (creative 2479471189241161). CTA SHOP_NOW, UTMs `test4000_ago26`.
- **`ads_creative_upload_video` SIGUE bloqueado** en esta cuenta (probado con URL pública del CDN de Shopify: mismo error "gradually rolled out") ⇒ los 2 videos hay que subirlos a mano en Ads Manager. URLs públicas de los videos en Shopify: `https://cdn.shopify.com/videos/c/o/v/09fb7aca6cbe4273b2e1cfaa350620ec.mp4` (cepillo) y `.../ecf37493667b4076ac76a51b97f94173.mp4` (botella).

**Estructura de creativos (Andrómeda) 2026-08-01:** archivo `Descargas/campaña/gonvra-estructura-creativos-andromeda.md` — 5 buyer personas, 12 dolores, 36 creativos, nomenclatura `P#-D#-FORMATO-ANGULO-v#`, olas de producción y filtro de rentabilidad (no pautar en frío productos <$16.990).

**🚀 CAMPAÑA ANTERIOR CREADA POR API 2026-08-01 (TODA EN PAUSA, cero gasto)** en cuenta 1482478863413097:
- Campaña **"GONVRA | TOFU | Prospección (Cama)"** id **120250532602990505** — OUTCOME_SALES, CBO $4.000/día (400000 cents), PAUSED.
- Conjunto **"Broad | AR | Compra"** id **120250532610800505** — OFFSITE_CONVERSIONS/PURCHASE al píxel 26889872433954472, Advantage+ Audience, AR 18-65, WEBSITE, atrib 7d clic/1d view.
- 2 anuncios PAUSED con imagen (foto del producto, ya diseñada y sin typos): Anuncio 1 id 120250532629960505 (creative 1346272491038847), Anuncio 2 id 120250532636340505 (creative 1349468270112314). Destino gonvra.com/products/cama-redonda-ortopedica-mascotas, CTA SHOP_NOW.
- **Truco que funcionó:** `ads_creative_upload_image` y `ads_creative_upload_video` SIGUEN bloqueados ("gradually rolled out") en esta cuenta, pero `ads_create_creative` acepta **`image_url` directo** (URL pública del CDN de Shopify) y así se crea el creativo sin subir. Los 2 videos de @gonvra.pets (Shopify Video ids 44991284478247 y 44991284511015, gonvra_pets_anuncio_1/2.mp4, verticales 720x404) NO se pudieron subir por API ⇒ el usuario los agrega a mano en Ads Manager como anuncios extra.
- **Falta para PRENDER:** (1) revivir el píxel (sigue en 0 eventos); (2) opcional: sumar los 2 videos como anuncios; (3) el usuario pone en Activo. La campaña vieja …680505 quedó en la cuenta 1 también (revisar/borrar si molesta).

**Cuenta vieja (verificado 2026-07-27, ya sin acceso):**
- Ad account: **1482478863413097** ("cuenta 1", negocio "Gonvra products", ACTIVE, ARS, con medio de pago). Hay una 2ª cuenta 27009241552077096 UNSETTLED → NO usar.
- Página FB: **"Gonvra pets"** (page_id 1125904760604828).
- Píxel/dataset: **"TIENDA CEPILLO 1"** (dataset_id **26889872433954472**), activo pero **sin eventos desde 15/6/2026** (probablemente porque la tienda no tiene tráfico todavía). Confirmar que dispare en gonvra.com antes de gastar (app Facebook & Instagram en Shopify).
- **Instagram: NO hay ninguno vinculado.** Catálogo: NO hay.
- **Presupuesto mínimo diario de Meta: ~$1.497 ARS por conjunto** (min_daily_budget_cents 149689). ⇒ el plan viejo de "$1.000 retargeting" es imposible; arrancar con 1 sola campaña de prospección.

**Creado el 2026-07-27, EN PAUSA (cero gasto):**
- Campaña **"GONVRA | Ventas – Prospección (Envío GRATIS)"** id **120250360311680505** — objetivo OUTCOME_SALES, CBO, $3.300/día (330000 cents; se puso $3.300 y no $4.000 para dejar margen a IVA+percepciones AR y quedar cerca de los $4.000 reales).
- Conjunto **"Prospección | Argentina | Compra (Envío GRATIS)"** id **120250360323480505** — optimiza OFFSITE_CONVERSIONS/PURCHASE al píxel, Advantage+ Audience, AR 21-65, destino WEBSITE, atribución 7d clic/1d view.

**Límite descubierto 2026-07-28:** `ads_creative_upload_video` da error "This tool is new and is being gradually rolled out" para esta cuenta ⇒ **NO se puede subir video ni crear el anuncio por API todavía**. El anuncio hay que crearlo a mano en Ads Manager (o reintentar la API más adelante). Los 2 videos del usuario (@gonvra.pets) SÍ quedaron subidos a Shopify Files (2026-07-28): Video 1 (18s) id 44991284478247 y Video 2 (10s) id 44991284511015; para subir archivos locales a Shopify usar el flujo stagedUploadsCreate(resource:VIDEO)→POST multipart a GCS (ojo: al copiar la `signature` no perder el `==` final, es base64)→fileCreate(contentType:VIDEO)→esperar READY.

**Plan definido 2026-08-01 (sesión de estrategia):** producto elegido para pautar = **Cama Redonda Ortopédica y Afelpada $16.990** (`gonvra.com/products/cama-redonda-ortopedica-mascotas`); aparece en 4/5 imágenes. Presupuesto arranque **$4.000/día**, objetivo Ventas/Compra. Se armó **plan full-funnel** (TOFU broad $4.000 + MOFU remarketing interacción $1.500 + BOFU abandono carrito $1.500, estos 2 en pausa hasta ~semana 2). Copys TOFU/MOFU/BOFU + públicos personalizados + reglas de escalado (ROAS>2.5 → +20-30%; CTR<0.8% o 2×CPA sin venta → pausar) quedaron en 3 archivos en `/home/matiigonzz/Claude/`: `campana-meta-gonvra.md`, `gonvra-guia-ejecucion-rapida.md`, `gonvra-brief-para-nuevo-chat.md` (este último es un handoff para pegar en un chat nuevo). **Imágenes con typos a corregir:** Masoctas→Mascotas, Antidldiszante→Antideslizante, Cómóda→Cómoda, Comoridad→Comodidad (los 2 videos están OK). **Browser bloqueado en facebook.com** (Claude-in-Chrome no puede manejar Ads Manager) ⇒ la campaña la carga el usuario a mano con guía por capturas.

**Falta para poder PRENDER (no depende del asistente):** (1) subir el/los videos (creatividad) y crear el anuncio; (2) confirmar que el píxel dispara. El retargeting se arma en ~2 semanas cuando haya tráfico. Objetivo de CPA sano: $5.000-$7.000 por venta (ticket ~$20.000-$32.000).
