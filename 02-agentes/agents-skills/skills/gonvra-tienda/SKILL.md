---
name: gonvra-tienda
description: "Operar la tienda Shopify GONVRA vigente (cuidado personal masculino, Argentina): preparar y ejecutar cambios de tema con SEMÁFORO, snapshot, revalidación y verificación remota."
---

# GONVRA — tienda Shopify vigente

GONVRA vende cuidado personal masculino en Argentina (ARS). Fuente de verdad obligatoria:
`~/Claude/gonvra2/CONTEXTO.md`; reemplaza por completo el contexto viejo de mascotas.
Tienda: `jm60sa-cp.myshopify.com`; admin: `admin.shopify.com/store/jm60sa-cp`.
Tema LIVE vigente: `#148158414963`. Proyecto local: `~/Documents/Codex/tiendas/jm60sa-cp/live-theme`.

## Regla de oro: pull fresco + SEMÁFORO
Antes de leer, preparar o tocar archivos del tema, ejecutar `theme pull` del LIVE vigente
`#148158414963` hacia una carpeta fresca con fecha/hora. Nunca partir de una copia local
anterior: el live puede haber cambiado. La plantilla realmente asignada a la rasuradora es
`templates/product.tienda.json`, no `product.json`.

Trabajar después en una copia local de ese pull fresco y congelar un snapshot exacto
(tienda, theme ID, lista de archivos, tamaños, SHA-256 y comando). Un push al tema LIVE
solo está permitido si Matías aprobó ese snapshot por Telegram, `broker.py revalidate`
devolvió `ready_to_execute` y el executor limita el push a los archivos aprobados
(`--only`, `--nodelete`, `--allow-live`). Descargar luego esos mismos archivos y verificar
el resultado remoto; Shopify agrega encabezados automáticos a JSON, por lo que se compara
el JSON canónico además del hash byte a byte.

No ampliar el alcance si la plantilla activa resulta ser otra: crear un nuevo snapshot y
una nueva aprobación. No crear temas nuevos innecesariamente. Los cambios LIVE del
19/09/2026 —olas responsive, ola de historia apagada, Antes/Después en home y producto,
y packs Individual/Dúo/Trío— ya están verificados: no rehacerlos ni revertirlos.

## Truco clave: editar sin gastar contexto
`sections/*.liquid` y `templates/*.json` no son públicos, pero `assets/*` sí:

```
themeFilesCopy(themeId, files:[{srcFilename:"sections/x.liquid", dstFilename:"assets/tmp.txt"}])
curl https://gonvra.com/cdn/shop/t/<N>/assets/tmp.txt      # <N> sale del preview
# parchear local con reemplazos exactos
stagedUploadsCreate + themeFilesUpsert con body:{type:URL}
```
El md5 coincide ⇒ cero erratas y cero costo de contexto.
`themeFilesDelete` está BLOQUEADO: los temporales se sobrescriben con texto vacío
y los borra el usuario a mano.

## Trampas verificadas
- `themeFilesUpsert` devuelve `upsertedThemeFiles: []` **aunque haya funcionado**.
  Verificar por **`checksumMd5`**, nunca por `size` (Shopify minifica y normaliza los JSON).
- En un `{% schema %}`, `"default": ""` es **inválido** y hace fallar el upsert: omitir la clave.
- Si una plantilla JSON referencia un `type` de sección inexistente, Shopify la
  rechaza **en silencio**: subir primero la sección.
- `gv-styles.css` tiene `.gv-pdp__rating span{font-size:14px}` que pisa cualquier
  span hijo. Al superponer capas ahí, forzar `font-size: inherit; letter-spacing: inherit`.

## Estructura
Secciones propias con prefijo `gv-` (gv-hero, gv-producto, gv-comparacion,
gv-testimonios, gv-detalles, gv-garantia, gv-videos, gv-banda). Reseñas con la app
**Loox** + la sección nativa `gv-testimonios`. Cada producto tiene su
`templates/product.<suffix>.json`. Combos: "Combo Chau Pelos"
(`product.combo-chaupelos`) y "Kit Aseo Total Perro" (`product.kit-aseo`).
El cuadro `gv-comparacion` ("¿Por qué comprar en GONVRA y no en Mercado Libre?")
va en cada página de producto.

## Envíos
**Todo gratis a Argentina.** Dos perfiles: "AutoDS Free Shipping" (bodega AutoDS,
13 productos sueltos) y "Perfil general" (bodega "Besares 2688", ahí está el Kit Aseo).
⚠️ **No mover productos entre perfiles a ciegas**: un producto sin stock en la
bodega del perfil queda SIN tarifas y **rompe el checkout**. El Combo Chau Pelos es
un bundle: su envío lo definen los componentes. Verificar siempre con
`draftOrderCalculate` + dirección argentina, no por la etiqueta del perfil.

## Pagos
`snippets/gv-pagos.liquid` centraliza los logos (usado en gv-producto, gv-marquee
y footer). Mercado Pago es `assets/gv-mercadopago.svg`, tarjeta 38×24 amarilla con
trazados **verbatim** del logo oficial. **Nunca re-transcribir trazados SVG a mano**:
bajarlos (Wikimedia Commons) y recortar por bbox. PayPal fue removido a pedido.

## Honestidad comercial (no revertir)
El render limpia la urgencia falsa aunque queden datos viejos guardados:
`viral_texto` pasa por `replace` que borra "STOCK BAJO"; el aviso de stock solo
sale si no es "¡Pocas unidades disponibles!"; `pagos_texto` borra "PayPal".
La urgencia real la da el contador de la promo. **En el editor puede verse texto
viejo, pero en la web no se muestra.**

## Trato con el usuario
No técnico. Español rioplatense, sin jerga, mínimo de pasos manuales
(ver skill `dictado-rioplatense`). Cuando cambia un texto global (ej. garantía
7→10 días) hay que buscarlo en **TODOS lados, incluida la home** — el hero lo
repite en `hero.settings.subtitle` de `templates/index.json`. Se frustra si
queda un lugar sin actualizar.
