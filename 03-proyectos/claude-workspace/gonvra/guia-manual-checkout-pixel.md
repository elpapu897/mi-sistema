# GONVRA — Guía manual para Matías: checkout y píxel

Estado: instrucciones, no ejecutadas por ningún agente.

## A. Checkout y cobro con tarjeta

### Antes de tocar nada

1. Abrí Shopify Admin.
2. Verificá que estés en la tienda GONVRA correcta.
3. Abrí **Configuración** → **Pagos**.
4. Sacá una captura o anotá los métodos activos: esto es el snapshot que debe aprobar el SEMÁFORO.
5. No cambies nada si el snapshot aprobado no coincide con lo que ves.

### Cambio recomendado para validar Mercado Pago

1. En **Pagos**, ubicá `PayPal`.
2. Ubicá también `Credit/Debit card by PayPal` o la opción que se muestre como “Pagos con tarjeta de crédito y débito” pero indique que pertenece a PayPal.
3. No desactives Mercado Pago Checkout Pro.
4. Pedí/confirmá el SEMÁFORO para la acción exacta: desactivar únicamente esas dos opciones.
5. Después de la aprobación, desactivá esas opciones manualmente y guardá.
6. Abrí la tienda en una ventana privada.
7. Agregá un producto vigente del catálogo vivo.
8. Llegá al checkout y verificá que aparezca Mercado Pago en ARS.
9. Para una compra real, pedí otra aprobación específica porque puede generar un cargo. No uses datos inventados ni completes el pago sin esa aprobación.
10. Si se hace la compra aprobada, verificá: cobro, orden Shopify, email y evento `Purchase` en ARS.

**No alcanza con sacar logos del tema:** eso no desactiva una pasarela.

## B. Píxel y eventos

### No borrar nada a ciegas

1. Entrá a Meta Events Manager.
2. Elegí el negocio y la cuenta correctos.
3. Abrí **Fuentes de datos / Datasets**.
4. Buscá el dataset documentado `26889872433954472` y el ID público observado `3919766821491073`.
5. Anotá nombre, cuenta, dominio, última actividad y origen de cada uno.
6. Abrí **Configuración** y **Eventos de prueba** de cada dataset.
7. No borres, desconectes ni unifiques nada todavía.

### Qué hay que confirmar

- Cuál dataset debe quedar como único.
- De dónde se inyecta `3919766821491073`.
- Si `26889872433954472` recibe PageView y ViewContent.
- Si existe CAPI y cómo se deduplican eventos.
- Si AddToCart y Purchase llegan con valor y moneda ARS.

### Prueba no destructiva

1. En Events Manager, abrí **Eventos de prueba** del dataset que se confirme como correcto.
2. Copiá el código o parámetro de prueba que Meta muestre.
3. Abrí la tienda en una ventana privada y visitá home y una ficha de producto.
4. Agregá un producto al carrito sin pagar.
5. Volvé a Events Manager y verificá PageView, ViewContent y AddToCart.
6. No completes una compra sin aprobación SEMÁFORO específica.
7. Solo después de una compra aprobada, verificá Purchase, valor ARS, moneda ARS y deduplicación browser/CAPI.

### Regla de pauta

Mientras no haya checkout probado y medición confiable:

- campañas pausadas;
- presupuesto $0;
- no optimizar a Purchase;
- no activar ni publicar nada.
