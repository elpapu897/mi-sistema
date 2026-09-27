# CONTEXTO GONVRA — memoria compartida del equipo de agentes

> Todo agente lee este archivo ANTES de trabajar. Si algo cambia, se actualiza acá.
> Última actualización: 2026-08-15

---

## 1. El negocio

- **Marca:** GONVRA — artículos para perros y gatos.
- 🛑 **GONVRA PAUSADA/ABANDONADA (2026-09-03):** Matías CAMBIÓ DE NICHO. Ya **no** se dedica a
  mascotas. **El foco 100% pasó a HELIO** (afeitadora eléctrica, `jm60sa-cp.myshopify.com`).
  Este archivo (GONVRA) queda como referencia histórica; NO trabajar más sobre GONVRA salvo que
  Matías lo pida explícitamente. Ver la memoria/Obsidian de HELIO.
- **Web:** gonvra.com · myshopify: `9em58g-tt.myshopify.com` · admin: admin.shopify.com/store/gonvra
- **País/moneda:** Argentina, ARS.
- **Dueño:** Matías. **No técnico.** Hablarle en español rioplatense, sin jerga, sin "tú".
- **Modelo:** dropshipping/AutoDS + bodega propia ("Besares 2688").
- **Envío:** GRATIS a toda Argentina.
- **Garantía:** 10 días desde la recepción. Si llega defectuoso, incompleto o distinto, el cliente escribe a `gonvra0@gmail.com` dentro de los 10 días con número de pedido y foto/video; GONVRA resuelve con reposición o reintegro.
- **Arrepentimiento:** 10 días corridos desde la recepción, sin costo ni explicaciones; se solicita por `gonvra0@gmail.com` con nombre y número de pedido; producto sin uso y en embalaje original.
- **Devoluciones:** se coordinan por `gonvra0@gmail.com`; se indica cómo y a dónde enviar según cada caso. No publicar una dirección física fija sin confirmación.
- **Estado real:** **10 órdenes en toda la historia**, todas "Cash on Delivery". La tienda está
  prácticamente en cero. Esto no es una tienda que hay que optimizar, es una tienda que hay que
  **arrancar**.

## 2. Productos — ⚠️ EL CATÁLOGO ES DINÁMICO, NO LO ASUMAS

> 🔴 **REGLA MÁS IMPORTANTE DE ESTE ARCHIVO:**
> **El catálogo cambia todo el tiempo y va a seguir cambiando.** El equipo está diseñado para
> encontrar productos ganadores y matar los que no venden, así que la lista de productos de hoy
> no va a ser la de dentro de dos semanas.
>
> **Ningún agente puede asumir qué productos hay.** Antes de cualquier tarea que involucre
> productos, precios o stock, hay que **leer el catálogo en vivo desde la API de Shopify**
> (`graphql_query` sobre `products`). Shopify es **la única fuente de verdad**.
>
> Si un agente nombra un producto que no existe más, o usa un precio viejo, eso es un error grave:
> se pauta un producto sin stock, se escribe una ficha de algo que ya no vendemos, o se calcula un
> margen con un costo que cambió. **Leer en vivo, siempre.**

### Lo único estable (reglas, no productos)

- **Regla de rentabilidad:** no pautar en frío productos de menos de **$16.990**.
- **Margen mínimo:** 2,5× sobre el costo puesto en Argentina.
- **CPA sano objetivo:** $5.000-$7.000. Ticket esperado: $20.000-$32.000.
- Categoría: perros y gatos. Nada frágil, nada que no llegue a Argentina.

### Foto del catálogo al 2026-08-15 (referencia histórica, VERIFICAR SIEMPRE)

- ~13 productos sueltos + 2 combos: "Combo Chau Pelos" (`product.combo-chaupelos`) y
  "Kit Aseo Total Perro" (`product.kit-aseo`).
- El producto que estaba elegido para pautar era la **Cama Redonda Ortopédica y Afelpada $16.990**
  (`/products/cama-redonda-ortopedica-mascotas`). **Puede haber cambiado.**
- Colecciones basura a limpiar: "Live Animals", "Pet Supplies", "cepilo baño".

### AutoDS — el proveedor que también cambia solo

- La mayoría de los productos vienen de **AutoDS** (perfil de envío "AutoDS Free Shipping").
  El resto sale de la bodega propia "Besares 2688".
- ⚠️ **AutoDS cambia cosas sin avisar:** el proveedor sube el costo, se queda sin stock, discontinúa
  el producto, o se alargan los tiempos de envío. Cualquiera de esas cosas puede hacer que un
  producto que era rentable pase a dar pérdida, o que estemos pagando anuncios de algo que no se
  puede entregar.
- Por eso hay un agente dedicado (**AUTODS**) que lo vigila todos los días.
- 🔴 **Trampa de los perfiles de envío:** no mover productos entre perfiles a ciegas — un producto
  sin stock en la bodega de su perfil se queda **SIN tarifas y rompe el checkout**.
  El Combo Chau Pelos es un **bundle**: su envío lo definen los componentes, no su propio perfil.
  Verificar siempre con `draftOrderCalculate` + una dirección argentina real, nunca por la etiqueta
  del perfil.

## 3. Tema y web

- Tema publicado (MAIN): **"GONVRA - Auditoría 2026"** (id 187644969255). ⚠️ Verificar siempre cuál
  es el MAIN vigente antes de tocar nada — cambia seguido.
- Secciones propias con prefijo `gv-`: gv-hero, gv-producto, gv-comparacion, gv-testimonios,
  gv-detalles, gv-garantia, gv-videos, gv-banda.
- Reseñas: app **Loox** + sección nativa `gv-testimonios`.
- El cuadro `gv-comparacion` ("¿Por qué comprar en GONVRA y no en Mercado Libre?") va en cada ficha.
- **Política anti-mentira:** nada de escasez falsa ni contadores truchos. Ya se limpió el código
  para que "STOCK BAJO" y "¡Pocas unidades!" no se rendericen aunque queden guardados. No reponerlo.

### Reglas duras para editar el tema
1. **Nunca escribir sobre el tema publicado** — el MCP lo bloquea igual.
2. Flujo: `themeDuplicate` → `themeFilesUpsert` sobre la copia → **el usuario publica a mano**.
3. **NO crear temas nuevos a lo pavote.** Ya hay ~16 y le molesta el quilombo. Reutilizar UNA sola
   copia de trabajo para todos los cambios pendientes.
4. Si se cambia un texto global (ej: "7 días" → "10 días"), buscarlo en **TODOS lados, incluida la
   home** (`templates/index.json` → `hero.settings.subtitle`). Se frustra si queda uno suelto.
5. Truco para leer secciones sin gastar contexto: `themeFilesCopy` de `sections/x.liquid` a
   `assets/tmp.txt` → `curl https://gonvra.com/cdn/shop/t/<N>/assets/tmp.txt` → parchear local →
   `stagedUploadsCreate` + `themeFilesUpsert` con `body:{type:URL}`.
6. Verificar por `checksumMd5`, nunca por `size` (Shopify minifica los JSON).
7. En un `{% schema %}`, `"default": ""` es inválido y rompe el upsert — omitir la clave.
8. `themeFilesDelete` está bloqueado: los temporales se sobrescriben vacíos y los borra el usuario.

## 4. 🔴 Los dos bloqueantes (prioridad absoluta)

### A. El checkout no cobra con tarjeta
El checkout ofrece tres proveedores:
- `Mercado Pago Checkout Pro` → **el correcto para Argentina** (declara ARS).
- `paypal` → botón de PayPal.
- `Credit/Debit card by PayPal` → se muestra como "Pagos con tarjeta de crédito y débito".
  ⚠️ **Parece tarjeta común pero es PayPal**, que no procesa tarjetas argentinas en pesos →
  el cliente ve "Se produjo un error al procesar tu pago".

**Acción pendiente del usuario** (el asistente no tiene permisos): desactivar PayPal y
"Credit/Debit card by PayPal" en `settings/payments` y probar una compra por Mercado Pago.
Sacar el logo del tema NO desactiva la pasarela.

**Mientras esto no se arregle, escalar tráfico es tirar plata.**

### B. Píxel duplicado y sin conversiones (CORREGIDO 2026-08-21 con diagnóstico de Claude Web)
🔁 **DATO CORREGIDO — antes estaba al revés.** Diagnóstico real de los dos píxeles:
- **`3919766821491073` ("gonvra1's pixel") = EL BUENO / EL QUE SE QUEDA.** Negocio
  `1065947712672679`. Creado 29/07/2026, activo y con actividad reciente. Embudo completo:
  PageView, ViewContent, AddToCart, InitiateCheckout y **AddPaymentInfo** (8 el 20/08).
- **`26889872433954472` ("TIENDA CEPILLO 1") = EL VIEJO / A DESACTIVAR (no borrar).** Negocio
  `975265715432729`. Solo PageView y ViewContent; **dejó de disparar el 16/08/2026**.
- ⚠️ **Los dos píxeles están en NEGOCIOS distintos** → antes de pautar hay que definir qué negocio y
  qué cuenta se usan, y migrar todo al píxel bueno (Meta NO fusiona píxeles: se elige uno y se
  recrean públicos/conversiones; el histórico del viejo no se transfiere).
- 🔴 **EL PROBLEMA MÁS GRAVE: NINGUNO registró jamás un `Purchase`.** Hay AddPaymentInfo e
  InitiateCheckout pero la compra nunca dispara. La compra de prueba por Mercado Pago va a decir si
  ahora el Purchase dispara. Sin Purchase, Meta no puede optimizar por compras.
- **Acceso confuso:** Claude Web NO ve `1482478863413097` (error); solo ve `2487859205019090`
  ("Matias Gonzalez", ARS, acceso vía Claude aún no habilitado). Ordenar qué cuenta es la definitiva.

### Otros pendientes menores
- `gonvra.com` **no tiene registros MX** ⇒ `contacto@gonvra.com` no recibe nada. El mail que
  funciona es `gonvra0@gmail.com`.
- ✅ Política de envíos publicada: `/policies/shipping-policy` responde HTTP 200; envío gratis a todo el país, sin promesa universal de tracking.
- ✅ Política de reembolso publicada: `/policies/refund-policy` responde HTTP 200 y declara garantía/arrepentimiento de 10 días con `gonvra0@gmail.com`.
- ⏳ Botón visible de arrepentimiento y cambio de contacto en el tema: pendiente hasta reconectar Shopify.

## 5. Meta Ads

- **Cuenta a usar: `1482478863413097`** ("cuenta 1", negocio "Gonvra products", ARS, con medio de
  pago). Ojo: el acceso **fluctúa día a día** — verificar siempre con `ads_get_ad_accounts`.
  - `2487859205019090` → sin habilitar. `27009241552077096` → UNSETTLED. **No usar ninguna.**
- Página FB: **"Gonvra pets"** (page_id 1125904760604828).
- ⚠️ **NO hay Instagram vinculado** → los anuncios **no se entregan en IG ni Reels**.
  Vincular **@gonvra.pets** es la mejora de mayor impacto disponible hoy.
- **Presupuesto mínimo por conjunto: ~$1.497/día.** El plan de "$1.000 de retargeting" es imposible.
- Catálogo: no hay.

### Límites de la API (probados)
- `ads_creative_upload_image` y `ads_creative_upload_video` → **bloqueados** ("gradually rolled out").
- ✅ **Workaround que sí funciona:** `ads_create_creative` acepta **`image_url` directo** con una URL
  pública del CDN de Shopify.
- Videos: hay que subirlos a mano en Ads Manager. URLs públicas:
  `https://cdn.shopify.com/videos/c/o/v/09fb7aca6cbe4273b2e1cfaa350620ec.mp4` (cepillo)
  `https://cdn.shopify.com/videos/c/o/v/ecf37493667b4076ac76a51b97f94173.mp4` (botella)
- **El navegador está bloqueado en facebook.com** ⇒ Ads Manager no se puede manejar por browser.
  Todo lo manual lo hace el usuario con guía paso a paso.
- `promoted_object` necesita `custom_event_type` o tira error 1885014.

### Campañas existentes (TODAS EN PAUSA, cero gasto)
| Campaña | ID | Estado |
|---|---|---|
| GONVRA \| Test $4.000 \| Video Cepillo vs Botella | 120250532987940505 | PAUSED, lifetime $4.000 |
| GONVRA \| TOFU \| Prospección (Cama) | 120250532602990505 | PAUSED, CBO $4.000/día |
| GONVRA \| Ventas – Prospección (Envío GRATIS) | 120250360311680505 | PAUSED, CBO $3.300/día |

### Reglas de escalado ya definidas
- ROAS > 2.5 → subir presupuesto 20-30% (no más, no rompe el aprendizaje).
- CTR < 0.8% → creativo malo, cambiar.
- Gasto de 2× el CPA objetivo sin una venta → pausar.
- Frecuencia > 2.5 → creativo quemado, renovar.

## 6. Creativos

- Estructura Andrómeda: `~/Descargas/campaña/gonvra-estructura-creativos-andromeda.md`
  → 5 buyer personas, 12 dolores, 36 creativos, nomenclatura `P#-D#-FORMATO-ANGULO-v#`.
- **Typos a corregir en las imágenes viejas:** Masoctas→Mascotas, Antidldiszante→Antideslizante,
  Cómóda→Cómoda, Comoridad→Comodidad. Los 2 videos están OK.
- **Generación de imágenes:** script Replicate en `~/Claude/scripts/genimage-replicate.py`, token en
  `~/.replicate-env`, modelo **nano-banana** (soporta 4:5 y referencias).
  ⚠️ **Siempre cerrar los prompts con "no text"** — el modelo escribe cualquier cosa.
  Formatos: **4:5** para feed de Meta, **9:16** para stories/Reels/TikTok.

## 7. Archivos de referencia ya existentes

- `~/Claude/campana-meta-gonvra.md` — plan full-funnel + copys TOFU/MOFU/BOFU.
- `~/Claude/gonvra-guia-ejecucion-rapida.md` — pasos de ejecución.
- `~/Claude/gonvra-brief-para-nuevo-chat.md` — handoff.
- `~/Claude/PROMPT-carrusel-gonvra.md` y `PROMPTS-carrusel-chaupelos.md` — prompts de carrusel.
- `~/Claude/gonvra-equipo-agentes.md` — diseño del equipo de agentes.

## 8. Tono de marca

Cercano, argentino, honesto. Habla de "tu perro" / "tu gato", no de "su mascota".
Cero urgencia falsa, cero promesas que no se cumplen. El diferencial contra Mercado Libre es
**envío gratis + garantía de 10 días + atención de verdad**, no el precio.
