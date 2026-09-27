---
tags: [proyecto, shopify, tienda, helio]
tienda: jm60sa-cp.myshopify.com
estado: publicada
actualizado: 2026-09-04
---

# 🪒 Helio — Afeitadora Eléctrica Portátil Mini

Segunda tienda Shopify (la primera es [[GONVRA - Meta Ads|GONVRA]]). Producto único,
estilo tecnológico premium.

## Datos

| | |
|---|---|
| Tienda | `jm60sa-cp.myshopify.com` |
| Admin | https://admin.shopify.com/store/jm60sa-cp |
| Tema en vivo | **Helio - Nuevo diseño** `#147833946227` |
| Proyecto local | `~/Documents/Codex/tiendas/jm60sa-cp` |
| Moneda | ARS · Buenos Aires |
| Producto | Afeitadora Eléctrica Portátil Helio Mini — $20.986,53 |
| Stock real | 10 plata + 10 verde = **20 unidades** |
| Plantilla | `product.mt` |

## Especificaciones reales del producto

Verificadas mirando las 6 fotos del proveedor (`fotos-producto/`). **Solo estas se afirman en la web:**

- Doble cabezal **autoafilable** (dos discos circulares de corte)
- Cabezales **flotantes**, se inclinan de 0° a 6°
- **Pantalla LED circular** frontal con el porcentaje de batería
- Carga por **USB** (sin cargador propietario)
- Cabezales **lavables** bajo el agua (no sumergir el cuerpo)
- **Cuerpo de aleación metálica** fundida, estética "mecha" / cyberpunk
- Dos colores: plateado y verde menta

> [!warning] La autonomía de la batería NO está confirmada
> No aparece en las fotos del proveedor ni en la descripción, y los buscadores estaban
> bloqueados por captcha. **No se afirma ningún número en la web.** La FAQ lo dice
> explícitamente. Pendiente: confirmarlo con el proveedor.

## Historia

1. **Codex** (2026-08-24, madrugada) construyó el tema desde Dawn con la skill
   `tienda-shopify-v2`: header, hero, beneficios, ángulos sticky, 3 pasos, viaje, momentos,
   FAQ, CTA, footer y página de producto. Generó 12 imágenes propias. Ver chat
   `2026-08-24--tienda-shopify-v2...`.
2. **Claude** (2026-08-24) amplió la estructura, añadió 6 secciones y el motor de animaciones,
   reescribió el copy con las specs reales y publicó. Ver `ESTADO.md` del proyecto.

## Estructura de la portada

`hero → banda → beneficios → ficha técnica → ángulos → cómo funciona → 3 pasos → carrusel →
viaje → momentos de uso → sobre nosotros → confianza → FAQ → cierre`

## Secciones propias

Prefijo `mt-`. Las de Codex: `mt-hero`, `mt-beneficios`, `mt-angulos`, `mt-pasos`, `mt-viaje`,
`mt-resenas`, `mt-faq`, `mt-cta`, `mt-producto`.
Las añadidas después: `mt-specs` (ficha con puntos interactivos), `mt-nosotros`, `mt-video`,
`mt-carrusel`, `mt-banda`, `mt-confianza`, más el snippet `mt-icon`.

Estilos y comportamiento nuevos en `assets/mt-plus.css` y `assets/mt-plus.js`.

## Iteración de 2026-09-04 — móvil y confianza

- Carrusel principal: pasó de arrastre manual por JavaScript a desplazamiento nativo con
  scroll snap. En celular las tarjetas e imágenes ocupan menos, se deslizan con el dedo y los
  controles de flechas quedan como alternativa.
- “Momentos de uso”: se eliminó la estética que podía confundirse con reseñas. En móvil es una
  tira táctil sin duplicados; en escritorio conserva movimiento suave.
- Efectos táctiles: se desactivan el halo de cursor, el parallax y el texto palabra por palabra;
  se mantienen revelados discretos y la barra de anuncios, más lenta.
- “Cómo funciona”: cuando no hay archivo o enlace cargado, se muestra una vista editorial de
  producto, no un falso botón de reproducción ni la frase “demostración real”. Si se sube un
  video a Shopify o se pega YouTube/Vimeo, el reproductor se activa solo.
- Copy: se enfatizan situaciones reales de uso (retoque diario, salida, viaje, USB y porcentaje
  de carga) sin urgencia ni testimonios falsos. Toda la interfaz personalizada está en español.
- Agua: la web dice “cabezales lavables” y aclara no sumergir el cuerpo completo. No se afirma
  impermeabilidad total porque no hay certificación comprobada.
- Publicación y comprobaciones: subida limpia al tema en vivo #147833946227; JSON y JavaScript
  válidos; Theme Check sin errores (15 advertencias heredadas de Dawn).

## Anti-urgencia falsa

Igual que en GONVRA: el bloque de escasez de la página de producto muestra el
**inventario real** que devuelve Shopify (`inventory_quantity`), y solo si la variante tiene
inventario gestionado y quedan menos unidades que el umbral. Nunca se inventa escasez.

## Pendientes

- [ ] **Regenerar las fotos** → `PROMPTS-IMAGENES.md` en el proyecto. La pantalla LED está
      apagada en las 12 imágenes actuales y es el argumento central de la web.
- [ ] Confirmar autonomía y tiempo de carga con el proveedor
- [ ] Instalar **Loox** para reseñas reales
- [ ] Confirmar política de envíos y cambios (la web ya la promete)
- [ ] Subir un video real a "Cómo funciona"

## Trampas de Shopify aprendidas acá

- En un `range` del `{% schema %}`, `(max - min)` debe ser **divisible exacto** por `step`.
  `min:0, max:180, step:8` hace que Shopify rechace el archivo entero con "Invalid schema".
- Shopify **rechaza en silencio** un `templates/*.json` que mencione un tipo de sección que
  todavía no existe en el tema. Subir siempre `sections/` primero y `templates/` después.
- El `name` de una sección no puede pasar de **25 caracteres**.
- `?preview_theme_id=` de un tema sin publicar **exige login** → inútil para verificar con un
  navegador headless. Hay que trabajar sobre el tema en vivo o pedirle la captura al usuario.
- Capturar con una ventana headless muy alta dispara las unidades `vh` y aparecen huecos
  enormes que no existen en pantallas reales.
