---
name: helio-shopify-store
description: "HELIO — segunda tienda Shopify del usuario (afeitadora mini, jm60sa-cp); estructura del tema y trampas de Shopify"
metadata: 
  node_type: memory
  type: project
  originSessionId: 73e36e0c-b68f-440b-aa51-4621f7e2bddd
  modified: 2026-08-24T16:39:27.091Z
---

**HELIO** es la SEGUNDA tienda Shopify del usuario (la otra es [[gonvra-shopify-store|GONVRA]]).
Producto único: **Afeitadora Eléctrica Portátil Helio Mini**, $20.986,53 ARS, 20 unidades de
stock (10 plata + 10 verde). Tienda `jm60sa-cp.myshopify.com`, admin
`admin.shopify.com/store/jm60sa-cp`. Proyecto local en `~/Documents/Codex/tiendas/jm60sa-cp`.
Nota de Obsidian: `~/OBSIDIAN/08-Proyectos-Reales/tiendas/Helio - Afeitadora Mini.md`.

**El Shopify CLI ya está autenticado para esta tienda** (`npx shopify` desde la carpeta del
proyecto, v4.7.0, Node 22). Da lectura Y escritura del tema y de la Admin API
(`shopify store execute --query-file X.graphql --json`; la salida NO viene envuelta en `data`).
Tema en vivo: **"Helio - Nuevo diseño" #147833946227**. Se puede pushear con
`shopify theme push --theme 147833946227 --allow-live --force --only "..."`.

**Reparto de trabajo:** Codex construyó el tema base desde Dawn con la skill `tienda-shopify-v2`
(secciones `mt-*`, `assets/mt-styles.css`, `assets/mt-scripts.js`). Claude añadió después
`mt-specs` (ficha con puntos interactivos sobre la foto), `mt-nosotros`, `mt-video`,
`mt-carrusel`, `mt-banda`, `mt-confianza`, el snippet `mt-icon` y los assets `mt-plus.css` /
`mt-plus.js` (enganchados en `layout/theme.liquid` tras los `mt-styles`/`mt-scripts`).

**Specs REALES del producto** (verificadas mirando `fotos-producto/producto-1..6.jpg`, que son
las del proveedor): doble cabezal autoafilable, cabezales flotantes 0°–6°, pantalla LED circular
con % de batería, carga USB, cabezales lavables bajo el agua, cuerpo de aleación metálica
(estética mecha/cyberpunk), plata y verde. **La autonomía de la batería NO está confirmada** —
no figura en ningún lado y los buscadores (DDG, Bing) devuelven captcha; no afirmar cifras.

**Anti-urgencia falsa** (igual que en GONVRA): el bloque de escasez de `mt-producto.liquid`
muestra el `inventory_quantity` REAL de Shopify y solo si la variante tiene inventario
gestionado y queda por debajo del umbral. Nunca inventar escasez.

**Fallo pendiente en las imágenes:** las 12 fotos generadas por Codex tienen **la pantalla LED
apagada** (disco negro liso), y esa pantalla es el argumento central de toda la web. Hay un
encargo completo de regeneración en `PROMPTS-IMAGENES.md` dentro del proyecto.

## Trampas de Shopify descubiertas acá (valen para cualquier tema)

- En un `range` del `{% schema %}`, **`(max - min)` debe ser divisible exacto por `step`**.
  `min:0, max:180, step:8` → Shopify rechaza **el archivo entero** con "Invalid schema".
  Este error NO lo detecta `shopify theme check`, solo aparece en el push.
- Shopify **rechaza en silencio** un `templates/*.json` que referencie un `type` de sección que
  todavía no existe en el tema. Hay que pushear `sections/` + `snippets/` PRIMERO y
  `templates/*.json` DESPUÉS. Si no, el push dice "complete" y la home sigue igual.
- El `name` de una sección en el schema no puede pasar de **25 caracteres** (`ValidSchemaName`).
  Esto sí lo detecta `theme check`.
- `?preview_theme_id=` sobre un tema **sin publicar exige login** → devuelve 302/página vacía,
  inútil para verificar con navegador headless. Sobre el tema en vivo sí funciona.
- Shopify **minifica** los CSS de `assets/` al servirlos (`inset: 42% 0 0` sale expandido a
  `top/right/bottom/left`). Para comprobar si una regla llegó, bajar el CSS del CDN con la URL
  completa `https://...` — una URL protocolo-relativa (`//...`) hace que curl falle en silencio.

## Verificación visual sin navegador interactivo

`brave-browser --headless --disable-gpu --no-sandbox --hide-scrollbars --window-size=1400,9000
--screenshot=/tmp/x.png --virtual-time-budget=30000 URL`, después recortar con PIL y leer los
trozos. **Ojo:** con una ventana muy alta las unidades `vh` se disparan
(`mt-angles__content` usa `padding-bottom: 20vh` → 1800px de hueco negro falso). Usar alturas
moderadas o ignorar esos huecos. Los anclajes `#seccion` NO funcionan en headless.
Para depurar una regla CSS concreta conviene reproducirla en un HTML local mínimo con el CSS
real copiado: se aísla el fallo en segundos.
