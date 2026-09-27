---
name: gonvra-shopify-store
description: "GONVRA — user's Shopify store (pet supplies, Argentina); theme structure and access notes"
metadata: 
  node_type: memory
  type: project
  originSessionId: f574ce93-bf18-4392-94c9-470147c7fd26
  modified: 2026-08-02T06:50:56.425Z
---

GONVRA es la tienda Shopify del usuario: productos para perros y gatos, Argentina (ARS), dominio **gonvra.com** (myshopify: 9em58g-tt.myshopify.com), admin: admin.shopify.com/store/gonvra.

Acceso vía el MCP de Shopify (graphql_query/graphql_mutation). **Escrituras al tema publicado (MAIN) están bloqueadas** por el MCP; para editar el tema hay que **duplicarlo** (themeDuplicate → tema UNPUBLISHED), hacer `themeFilesUpsert` sobre la copia, y el usuario **publica** desde el panel (themePublish también bloqueado para el asistente).

Tema publicado: **"GONVRA Premium"**. Secciones propias con prefijo `gv-` (gv-hero, gv-producto, gv-comparacion, gv-testimonios, gv-detalles, gv-garantia, gv-videos, gv-banda, etc.), todas editables desde el editor. Reseñas: usa la app **Loox** (bloque loox-reviews) + la sección nativa editable `gv-testimonios`. Cada producto tiene su propia plantilla `templates/product.<suffix>.json`.

Combos/kits: "Combo Chau Pelos" (product.combo-chaupelos) y "Kit Aseo Total Perro" (product.kit-aseo). El cuadro `gv-comparacion` ("¿Por qué comprar en GONVRA y no en Mercado Libre?") va en cada página de producto.

Usuario **no técnico**: hablarle sin jerga, en español rioplatense, y dejarle el mínimo de pasos manuales (ver [[tienda-shopify-v2]] skill). Colecciones basura a revisar/borrar: Live Animals, Pet Supplies, "cepilo baño".

**Truco para subir archivos grandes al tema sin gastar contexto:** `themeFilesUpsert` acepta `body: {type: URL}`. Flujo: `stagedUploadsCreate` → subir por curl → pasar el `resourceUrl` (privado de GCS) al upsert; Shopify lo lee igual. Ojo: devuelve `upsertedThemeFiles: []` aunque haya funcionado — verificar comparando `size` del archivo remoto contra el local. La `policy` del staged upload se puede reconstruir a partir del `key` (solo la firma es única), lo que ahorra repetir datos.

**Envíos (verificado 2026-07-27):** todo va **gratis a Argentina**. Hay dos perfiles: "AutoDS Free Shipping" (atado a la bodega AutoDS; cubre los 13 productos sueltos) y "Perfil general" (bodega "Besares 2688"; ahí está el Kit Aseo). Su tarifa doméstica se puso en $0. Ojo: **no mover productos entre perfiles a ciegas** — un producto sin stock en la bodega del perfil se queda SIN tarifas y rompe el checkout. El Combo Chau Pelos es un **bundle**: su envío lo definen los componentes, no su propio perfil. Verificar siempre con `draftOrderCalculate` + dirección argentina, no por la etiqueta del perfil.

Trampa de Shopify: en el `{% schema %}` de una sección, `"default": ""` (string vacío) es **inválido** y hace fallar el upsert; hay que omitir la clave. Si una plantilla JSON referencia un `type` de sección que no existe, Shopify la rechaza en silencio (`upsertedThemeFiles: []` sin errores) — subir primero la sección.

**Feedback del usuario (2026-07-30):** (1) NO crear temas nuevos a lo pavote — ya hay ~16 y le molesta el quilombo; reutilizar UNA sola copia para todos los cambios pendientes del tema. (2) Cuando cambia un texto global (ej: garantía 7→10 días), buscarlo en **TODOS lados, incluida la home** (el hero dice "…y garantía de 7 días" en `hero.settings.subtitle` de templates/index.json) — se frustra si me olvido de un lugar. **El tema "GONVRA ⏰" (187492991271) YA está PUBLICADO/MAIN** desde ~2026-07-30 (todos los fixes previos están en vivo). Copia de trabajo para el cambio 7→10: "GONVRA — garantía 10 días" (187600732455).

**Anti-urgencia falsa (2026-07-27, en `sections/gv-producto.liquid` del tema "GONVRA ⏰"):** el render limpia solo la mentira aunque los datos viejos sigan guardados. El cartel `viral_texto` pasa por `replace` que borra "STOCK BAJO"/"|" → queda "PRODUCTO VIRAL". El aviso de stock solo aparece si `stock_texto` NO es blank y NO es "¡Pocas unidades disponibles!" (así la escasez falsa nunca se muestra; stock real 100-654). El `pagos_texto` pasa por `replace` que borra cualquier "PayPal". Defaults del schema ya honestos (viral="PRODUCTO VIRAL", mostrar_stock=false). ⇒ En el editor un campo puede seguir mostrando texto viejo, pero en la web NO se ve. La urgencia real la da el contador de la promo.

Pagos: el snippet `snippets/gv-pagos.liquid` centraliza los logos (se usa en gv-producto, gv-marquee y footer). Mercado Pago va como `assets/gv-mercadopago.svg`; el resto son iconos nativos vía `payment_type_svg_tag`. PayPal fue removido a pedido del usuario.

**Estado 2026-08-02:** el tema MAIN pasó a ser **"GONVRA - Auditoría 2026" (187644969255)**. Ninguna de las copias viejas coincide con él (publicar cualquiera revertiría cambios) ⇒ hay que duplicar el MAIN vigente. Copia de trabajo actual: **"GONVRA — logo MP + promo" (187645395239)**.

**Logo de Mercado Pago (arreglado 2026-08-02):** el SVG anterior tenía los trazados corruptos (el apretón de manos se veía como un borrón) y además era un cuadrado 32×32 entre tarjetas de 38×24 (`.gv-pay-icon`), con una regla `.gv-pay-icon--mp` en gv-styles.css que lo forzaba. Ahora `assets/gv-mercadopago.svg` es una tarjeta 38×24 amarilla con los trazados **verbatim** del logo oficial (Wikimedia Commons `File:Mercado Pago.svg` → `commons.wikimedia.org/w/api.php` para la URL real), solo la marca sin la palabra (ilegible a ese tamaño), y el snippet ya no usa la clase `--mp`. **Nunca re-transcribir trazados SVG a mano** — bajarlos y recortar por bbox.

**⭐ TRUCO CLAVE — editar secciones/plantillas sin gastar contexto:** los `sections/*.liquid` y `templates/*.json` NO son públicos, pero `assets/*` SÍ. Flujo: `themeFilesCopy(themeId, files:[{srcFilename:"sections/x.liquid", dstFilename:"assets/tmp.txt"}])` (copia server-side, dentro del mismo tema) → `curl https://gonvra.com/cdn/shop/t/<N>/assets/tmp.txt` → parchear local con un script de reemplazos exactos → `stagedUploadsCreate` + `themeFilesUpsert` con `body:{type:URL}`. El md5 del archivo bajado coincide con el del tema ⇒ **cero riesgo de erratas y cero costo de contexto**. El `<N>` de `t/<N>` sale de la vista previa del tema. `themeFilesDelete` está BLOQUEADO por el MCP: los temporales hay que sobrescribirlos con texto vacío y que el usuario los borre a mano.

**Shopify guarda los JSON de tema MINIFICADOS** (sin el comentario de cabecera ni indentación) y los **normaliza al hacer upsert** ⇒ el `size` que reporta no coincide con un JSON prettificado, y no hace falta respetar el formato al subir. Verificar siempre por `checksumMd5`, no por `size`.

**Trampa CSS (2026-08-02):** `gv-styles.css` tiene `.gv-pdp__rating span{font-size:14px}`, que pisa el tamaño de CUALQUIER span hijo. Rompió el relleno de las estrellas (fondo 17px, relleno 14px → desalineado). Si se agregan capas superpuestas ahí dentro, forzar `font-size: inherit; letter-spacing: inherit`.

**Verificación visual sin la pane del navegador:** `mcp__Claude_Browser__computer screenshot` falla si la pane no está a la vista. Alternativa que sí funciona: `python3 -m http.server` en el scratchpad + `brave-browser --headless --screenshot=... --virtual-time-budget=...` y leer el PNG. Para ver una sección tal cual la sirve Shopify: `curl "https://gonvra.com/?preview_theme_id=<id>"`, extraer el `<style>` + `<section id="shopify-section-...">` y montarlo con el `gv-styles.css` del CDN. Ojo: apuntar el headless directo a gonvra.com se cuelga.
