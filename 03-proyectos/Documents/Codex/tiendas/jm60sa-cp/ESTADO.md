# Estado del proyecto — Helio

- Tienda: jm60sa-cp.myshopify.com
- Carpeta: /home/matiigonzz/Documents/Codex/tiendas/jm60sa-cp
- Tema base: Dawn (descargado 2026-08-24)
- Entorno: Node v22.23.2, npm 10.9.8, Shopify 4.7.0 — OK
- Conexión con la tienda: OK (2026-08-24)
- Tema de trabajo: Helio - Nuevo diseño (#147833946227, publicado / live)
- Vista previa: https://jm60sa-cp.myshopify.com?preview_theme_id=147833946227
- Última publicación: 2026-09-04 (tema PUBLICADO / live)

## Fases completadas

- [x] 0 Entorno
- [x] 1 Conexión y lectura del producto
- [x] 2 Proyecto
- [x] 3 Diseño
- [x] 4 Construcción
- [x] 5 Páginas
- [x] 6 Publicación
- [x] 7 Ampliación de estructura + animaciones (Claude, 2026-08-24)

## Producto principal leído

- ID: gid://shopify/Product/8371640533107
- Estado: activo
- Handle: mini-usb-electric-shaver-long-lasting-portable-car-household-trimmer-rechargeable-washable-barber-hair-shaver-for-men-rv-hotel
- Título actual: Afeitadora Eléctrica Portátil Helio Mini
- Descripción actual: reescrita en español con atributos verificables y aviso de cuidado del cuerpo del dispositivo.
- Precio actual: 20.986,53
- Inventario total: 20
- Variantes: plateada y verde; conexión USB; caja de color
- Imágenes descargadas: 6, en `fotos-producto/`
- Imágenes personalizadas añadidas al catálogo: 4 (frontal plata, lateral plata, verde y macro del cabezal)
- Plantilla personalizada asignada: `product.mt`

## Decisiones de diseño

- Idioma: español.
- Dirección: tecnología premium, lejos de una plantilla de Shopify.
- Paleta: grafito `#080A0F`, azul noche `#111827`, plata fría `#CBD5E1`, azul eléctrico `#36C5FF`, verde energía `#65F29A`, blanco hielo `#F7FAFC`.
- Tipografía: sans geométrica de gran impacto para titulares y sans muy legible para cuerpo.
- Fotografía: sesión coherente de estudio, producto fiel a las referencias, sin texto ni marcas de agua. Cada bloque tendrá una imagen específica adaptada a su composición.
- Composición: producto completo y a escala contenida, nunca cortado; espacio negativo reservado para el copy; capas y degradados de la web garantizarán legibilidad.
- Portada: hero panorámico y estrecho; beneficios; escena sticky con varios ángulos; uso en tres pasos con una foto propia por paso; prueba social; preguntas frecuentes; cierre de compra con imagen exclusiva.
- Movimiento: reveals escalonados, parallax suave, tilt de producto, marquesina, contadores y transiciones de galería, con versión reducida para accesibilidad y simplificación móvil.
- Fotos: generadas con la herramienta integrada de Codex, sin clave externa. Se crearán piezas narrativas y fotos limpias para la galería del producto.
- Copy: siempre como texto editable de la web; nunca incrustado en las imágenes.

## Secciones creadas

- Header Helio con anuncio, navegación anclada, estado sticky y menú móvil.
- Hero responsive con composición panorámica propia para desktop y una fotografía vertical específica para móvil.
- Beneficios en tarjetas editoriales con fotografía, degradados y paneles de copy legibles.
- Galería de ángulos con navegación y composición contenida.
- Secuencia de uso en tres pasos, con una fotografía exclusiva por paso.
- Bloque de viaje/lifestyle, momentos de uso, preguntas frecuentes y CTA final.
- Producto `product.mt` con galería, selector de variante, estado de stock y formulario de compra.
- Footer Helio con navegación, políticas nativas y campos opcionales para Cookies/Aviso legal.

## Activos visuales

- 12 fotografías generadas específicamente para Helio, sin texto quemado ni marcas de agua.
- 8 composiciones narrativas para la portada y 4 imágenes cuadradas para el catálogo.
- Fuentes originales archivadas en `work/image-sources/`; versiones WebP optimizadas en `assets/`.

## Verificación

- JSON y JavaScript validados localmente.
- QA visual realizado en desktop y móvil sobre portada y producto.
- Selector plata/verde verificado con cambio de imagen, URL y stock.
- Header sticky, anclas, menú móvil, FAQ y enlaces de contacto/políticas revisados.
- Animaciones respetan `prefers-reduced-motion`.
- Theme Check final: 0 errores; 15 advertencias heredadas de Dawn en archivos no intervenidos.
- Consola final de portada y producto: 0 errores y 0 advertencias.
- Título público del tema corregido a `HELIO`; enlaces de Cookies/Aviso legal ocultos hasta disponer de páginas válidas.
- Fuente responsive de hero móvil confirmada en el preview final.
- Tema publicado; los cambios posteriores se aplican directamente al tema live con autorización del usuario.


---

## Ampliación del 2026-08-24 (Claude Code)

Se trabajó **directamente sobre el tema en vivo** `#147833946227` con el Shopify CLI ya
autenticado. Todo verificado con capturas headless contra la web publicada.

### Secciones nuevas (todas editables desde el editor)

| Archivo | Nombre en el editor | Qué hace |
|---|---|---|
| `sections/mt-specs.liquid` | MT – Ficha técnica | Foto del producto con **puntos numerados interactivos**; al pasar el cursor se resalta la característica correspondiente de la lista. Incluye 4 contadores animados. |
| `sections/mt-nosotros.liquid` | MT – Sobre nosotros | Bloque de marca: foto con recuadro de cristal, frase destacada, texto enriquecido, 3 pilares con icono y firma. |
| `sections/mt-video.liquid` | MT – Cómo funciona | Reproductor con portada, botón de play con pulso y 3 pasos. Acepta video subido a Shopify **o** enlace de YouTube/Vimeo (se convierte solo a embed). Relación de aspecto distinta en escritorio y celular. |
| `sections/mt-carrusel.liquid` | MT – Carrusel | Carrusel arrastrable con mouse y dedo, flechas, barra de avance y panel de cristal sobre cada foto. |
| `sections/mt-banda.liquid` | MT – Banda en movimiento | Marquesina infinita de specs, se pausa al pasar el cursor. |
| `sections/mt-confianza.liquid` | MT – Barra de confianza | 4 tarjetas de envío / cambios / pago / atención. |
| `snippets/mt-icon.liquid` | — | 16 iconos de línea reutilizables. |

### Assets nuevos

- `assets/mt-plus.css` — estilos de las secciones nuevas + motor de animación.
- `assets/mt-plus.js` — revelados escalonados, titulares palabra por palabra, halo que sigue al
  cursor, contadores, puntos interactivos, carrusel arrastrable, barra de stock. Todo respeta
  `prefers-reduced-motion`.
- Enganchados en `layout/theme.liquid` justo después de `mt-styles.css` / `mt-scripts.js`.

### Página de producto

- Distintivo **"PRODUCTO DESTACADO"** y **stock real** leído de Shopify (`inventory_quantity`),
  con barra de progreso. Solo aparece si la variante tiene inventario gestionado por Shopify y
  quedan menos unidades que el umbral configurable (por defecto 25). **No hay escasez falsa.**
- Ficha técnica de 6 características reales y FAQ ampliada a 8 preguntas.
- Se añadieron a `product.mt.json` las secciones de confianza y ficha técnica.

### Orden de la portada

`hero → banda → beneficios → ficha técnica → ángulos → cómo funciona → 3 pasos → carrusel →
viaje → momentos de uso → sobre nosotros → confianza → FAQ → cierre`

### Copy: specs verificadas contra las fotos del proveedor

Se reescribió el copy apoyándose solo en lo que se puede comprobar en `fotos-producto/`:
doble cabezal autoafilable, cabezales flotantes 0°–6°, pantalla circular con % de carga,
cuerpo de aleación metálica, carga USB, cabezales lavables, dos colores.

**La autonomía de la batería NO se afirma en ningún lado**: no aparece en las fotos del
proveedor ni en la descripción, y los buscadores estaban bloqueados. La FAQ lo dice
explícitamente y queda pendiente confirmarlo con el proveedor.

### Pendiente

1. Reemplazar el nombre provisional **HELIO** y el monograma `H` por el nombre final que pase el usuario; después crear un logo minimalista y actualizar título de producto, cabecera, pie y textos globales.
2. **Regenerar las fotos** — ver `PROMPTS-IMAGENES.md`. Fallo crítico: la pantalla LED está
   apagada en las 12 imágenes actuales.
3. Confirmar autonomía y tiempo de carga con el proveedor y rellenar la FAQ.
4. Instalar **Loox** para reseñas reales (decisión del usuario).
5. Confirmar la política real de envíos y cambios: la barra de confianza y las FAQ prometen
   "envío a todo el país con seguimiento" y "si llega fallada, la cambiamos".
6. Subir un video real a la sección "Cómo funciona".

### Trampas encontradas (para la próxima)

- En un `range` del `{% schema %}`, `(max - min)` debe ser divisible exacto por `step`.
  `min:0, max:180, step:8` hace que Shopify rechace **el archivo entero**.
- Shopify **rechaza en silencio** un `templates/*.json` que referencie un tipo de sección que
  aún no existe en el tema: hay que subir `sections/` primero y `templates/` después.
- El nombre de una sección en el schema no puede pasar de **25 caracteres**.
- La vista previa `?preview_theme_id=` de un tema sin publicar **exige login**: no sirve para
  verificar con un navegador headless.
- Al capturar la web con una ventana headless muy alta, las unidades `vh` se disparan
  (`mt-angles__content` usa `padding-bottom: 20vh`) y aparecen huecos enormes que **no existen**
  en pantallas reales.

---

## Mejora de conversión del 2026-08-24 (Codex)

Publicada directamente en el tema live `#147833946227` y verificada en escritorio y móvil.

- La barra superior ahora tiene 3 mensajes que rotan automáticamente, señales luminosas discretas,
  barrido de luz y flechas de navegación. Respeta `prefers-reduced-motion`.
- La ficha técnica centra y agranda las cifras (`2×`, `6°`, `100%`, `2`), y expone su alineación y
  tamaños desde el editor visual.
- Se redujo el espacio muerto al terminar la escena "ángulos" para que la portada avance con más ritmo.
- La compra ya no muestra los selectores de proveedor `Caja del producto` y `USB`, que no eran
  decisiones reales. Solo queda el selector visual de color.
- Se añadió **Elegí tu oferta**: `1 unidad` o `2 unidades`. La segunda opción agrega cantidad `2`
  al mismo producto/variante en el carrito y calcula el total real; no hay descuento inventado.
- El botón de compra y las tarjetas de oferta tienen microanimaciones de brillo, estado seleccionado
  claro y foco accesible.
- Validaciones: JSON y schemas de secciones OK, JavaScript validado con Node, tema subido sin errores,
  captura de escritorio y móvil revisadas. Las variantes plateada y verde siguen resolviendo al ID
  correcto de Shopify.

---

## Optimización móvil y credibilidad del 2026-09-04 (Codex)

Publicada directamente en el tema live #147833946227.

- El carrusel principal ya no captura el dedo con JavaScript: usa desplazamiento horizontal
  nativo, ajuste por tarjeta (scroll snap), barra de avance y flechas como alternativa.
  En celular las tarjetas son más chicas, las imágenes tienen margen y el texto queda separado
  en una ficha editorial.
- Los “momentos de uso” dejaron de parecer reseñas inventadas. En teléfono se desplazan de forma
  nativa y no duplican tarjetas; el movimiento automático queda solo para computadora.
- Las animaciones dependientes del cursor (halo, parallax y entrada palabra por palabra) se
  simplifican en pantallas táctiles. La barra de anuncios conserva su movimiento, pero más lento.
- El bloque “Cómo funciona” ya no afirma que una imagen estática sea una demostración real:
  muestra una vista editorial de tres detalles hasta que se cargue un video real. Cuando se suba
  un video a Shopify o se pegue un enlace de YouTube/Vimeo, se convierte automáticamente en
  reproductor.
- Se reescribió el copy para destacar necesidades concretas (retoque diario, salida, viaje,
  carga visible y USB) sin testimonios, descuentos ni urgencia inventados. Todo el texto público
  personalizado quedó en español.
- El agua se comunica con precisión: cabezales lavables/enjuagables, sin afirmar que el
  cuerpo completo sea impermeable o sumergible.
- Validación: JSON y JavaScript correctos; Theme Check terminó sin errores (15 advertencias
  heredadas de Dawn); archivos y marcado nuevos confirmados en la versión live.
