---
tags: [gonvra, shopify, landing, prompts, dropshipping]
tienda: jm60sa-cp
producto: face-body-electric-shaver
tema: 148158414963
actualizado: 2026-09-06
---

# GONVRA · Landing de la rasuradora

Tienda **jm60sa-cp** · producto **Rasuradora Integral Recargable — Rostro y Cuerpo** (ARS 64.737,52, costo ~US$5).
Tema de vista previa: **GONVRA — Landing de vista previa** `#148158414963` (el tema activo sigue siendo *Helio - Nuevo diseño*).

- [Ficha de producto](https://jm60sa-cp.myshopify.com/products/face-body-electric-shaver?preview_theme_id=148158414963)
- [Inicio](https://jm60sa-cp.myshopify.com/?preview_theme_id=148158414963)
- [Editor del tema](https://admin.shopify.com/store/jm60sa-cp/themes/148158414963/editor)

Archivos del tema: `~/Claude/gonvra-theme/` (copia de trabajo) y `~/Claude/gonvra-theme-full/` (tema completo Horizon 4.1.4).

---

## Estructura de la página (sacada de los videos de referencia)

| # | Sección | Archivo |
|---|---------|---------|
| 1 | Cabecera + barra animada | `gv-header.liquid` |
| 2 | Ficha: galería, packs, CTA, contador, línea de entrega, acordeones, garantías | `gv-producto.liquid` |
| 3 | Números (3 / 2 / 0) | `gv-datos.liquid` |
| 4 | Videos verticales | `gv-videos.liquid` |
| 5 | Problema → 3 pasos de uso | `gv-historia.liquid` |
| 6 | Antes y después (slider) | `gv-antes.liquid` |
| 7 | Comparativa vs. máquina común | `gv-comparativa.liquid` |
| 8 | Reseñas (vacía hasta tener reales) | `gv-resenas.liquid` |
| 9 | FAQ + cierre de compra | `gv-faq.liquid` |
| 10 | Pie + WhatsApp | `gv-footer.liquid` |
| — | Ola animada con degradé | `snippets/gv-wave.liquid` |

Videos de referencia analizados: `~/Descargas/1001297297.mp4`, `1001297298.mp4`, `1001297299.mp4`
(estructura de Sternify + método AIDA de @masterwebfco). Estilo de animaciones: **reactbits.dev**.

---

## Estado operativo (auditado el 2026-09-06)

- [ ] **Activar medios de pago** en Configuración → Pagos. No lo activa Codex: Shopify requiere que el titular complete identidad, cuenta de cobro e información fiscal.
- [ ] **Descuento automático**. Verificado con los carritos de 1, 2 y 3 unidades: hoy el descuento aplicado es `$0`. La ficha volvió a mostrar precios reales para no prometer una rebaja inexistente. Crear desde [nuevo descuento](https://admin.shopify.com/store/jm60sa-cp/discounts/new/automatic/order): 2 unidades = 10% · 3 unidades = 20%; luego reactivar los porcentajes en la plantilla.
- [ ] **Producto regalo del Dúo**. El catálogo activo contiene una sola rasuradora; no hay un segundo producto real que pueda asignarse sin inventar inventario. Producto recomendado para importar primero desde Zendrop: `beard shaving bib / beard catcher apron` (capa atrapa-pelos con ventosas), liviana y directamente complementaria. Luego se elige en el bloque Dúo desde el editor del tema.
- [ ] Subir 3 videos verticales propios a la sección "Mirá cómo se usa".
- [ ] Cargar el número de WhatsApp en el pie.
- [x] Verificar precio de la competencia en Mercado Libre antes de fijar el precio final. Resultado y recomendación abajo.
- [x] Crear e integrar recursos visuales nuevos: hero desktop, hero móvil y foto de contenido de caja.

### Competencia y precio final recomendado

El relevamiento muestra dos mercados distintos: genéricos internacionales entre **AR$17.529–30.242**, y productos de marca o de nicho corporal entre **AR$42.290–99.500**. Tu rasuradora no debe presentarse como Philips/OneBlade ni prometer prestaciones que no puede demostrar.

**Precio inicial recomendado: AR$44.900**, no AR$64.737,52. Está apenas por debajo de las opciones de marca de entrada (GA.MA / VGR) y deja margen amplio frente a un coste aproximado de US$5; reduce el choque de precio frente a Mercado Libre mientras tu entrega tarda 12–20 días. Testear 7 días; si el ratio de inicio de checkout es saludable, probar AR$49.900 como variante A/B.

Fuentes: [listado Mercado Libre de rasuradoras corporales](https://listado.mercadolibre.com.ar/rasuradora-electrica-corporal), [listado masculino](https://listado.mercadolibre.com.ar/afeitadora-cuerpo-masculina), [listado tipo Razor](https://listado.mercadolibre.com.ar/maquina-rasuradora-corporal-razer).

---

## PROMPTS DE IMÁGENES

> Todas para generar con Nano Banana / ChatGPT. **Siempre adjuntar como referencia**
> `~/Claude/product-assets/rasuradora-integral-hero-v1.png` para que respete el producto real
> (cuerpo negro mate, detalles verde lima, cabezal de acero).
> Cerrar siempre con: *no text, no logos, no watermark*.

### 1 · Hero de la portada (16:9)

```
Editorial product photograph of the black and lime-green electric body shaver from the
reference image standing upright on a warm cream marble bathroom counter. Soft morning
light coming from the left, long gentle shadow, blurred background with folded ivory
towels and a wooden tray. Large empty negative space on the LEFT THIRD of the frame for
headline text. Muted earthy palette, shallow depth of field, premium skincare-brand
aesthetic. No text, no logos, no watermark.
```
Ratio `16:9` · resolución `2K`

### 2 · Hero para celular (9:16)

```
Vertical editorial photograph of the black and lime-green electric body shaver from the
reference image standing on a cream marble bathroom counter, positioned in the UPPER
THIRD of the frame. Bottom half is soft empty counter surface with gentle shadow, clean
and uncluttered, so text can be placed there. Warm morning light, blurred bathroom
background. Premium minimal aesthetic. No text, no logos, no watermark.
```
Ratio `9:16` · resolución `2K`

### 3 · Packs de 1, 2 y 3 unidades (1:1)

```
Studio packshot of exactly [ONE / TWO / THREE] identical black and lime-green electric
body shavers from the reference image, standing upright side by side and slightly
overlapping, perfectly centered on a seamless warm ivory background (#F3F2EC). Soft
diffused top light, subtle contact shadow under each unit, generous margin around the
group. Crisp e-commerce packshot. No props, no text, no logos.
```
Ratio `1:1` · una imagen por cantidad → guardar como `gv-pack-1.png`, `gv-pack-2.png`, `gv-pack-3.png`

### 4 · Paso 1 — Elegí el largo (4:3)

```
Top-down flat lay on a cream stone surface: the black and lime-green electric body shaver
from the reference image next to its three guide combs of different sizes and a braided
USB cable, arranged with generous spacing. Natural side light, soft shadows, muted earthy
palette, editorial product photography. No text, no logos, no watermark.
```
Ratio `4:3`

### 5 · Paso 2 — Pasala en seco (4:3)

```
Lifestyle photograph of a man in his early thirties in a bright modern bathroom, running
the black and lime-green electric body shaver from the reference image along his forearm.
Natural window light, warm wood and cream tones, shallow depth of field, relaxed
documentary feel, realistic skin texture. No text, no logos, no watermark.
```
Ratio `4:3`

### 6 · Paso 3 — Limpiala y cargala (4:3)

```
Close-up photograph of a hand plugging a USB cable into the black and lime-green electric
body shaver from the reference image, resting on a cream marble counter next to a small
cleaning brush. Warm bathroom light, soft reflections, shallow depth of field, premium
minimal aesthetic. No text, no logos, no watermark.
```
Ratio `4:3`

### 7 · Antes y después (dos imágenes 4:5, MISMO encuadre)

> Generar las dos con el mismo prompt base cambiando sólo la última frase, para que el
> deslizador calce perfecto.

```
Vertical photograph of a man's forearm resting on a cream marble bathroom counter, seen
from the same fixed camera angle, natural window light from the left, blurred bathroom
background with a small plant. The black and lime-green electric body shaver from the
reference image lies on the counter beside the arm.
[ANTES] The forearm shows natural, visible body hair.
[DESPUÉS] The forearm shows neatly trimmed, even short hair.
Identical framing, identical lighting, identical composition in both images.
No text, no logos, no watermark.
```
Ratio `4:5` → guardar como `gv-antes.jpg` y `gv-despues.jpg`

### 8 · Tarjetas verticales de la sección "Mirá cómo se usa" (9:16)

```
Vertical smartphone-style photograph, slightly candid: [ESCENA]. Warm bathroom light,
blurred background, shallow depth of field, natural skin texture, real user-generated
content feel, no studio lighting. No text, no logos, no watermark.
```
Escenas:
- `a man trimming his beard line along the jaw with the black and lime-green shaver from the reference image`
- `a man running the shaver down his forearm, close crop on the hand and arm`
- `the shaver, its guide combs, USB cable and cleaning brush laid out on a linen surface, top-down`

---

## PROMPTS DE VIDEO (anuncios y sección de uso)

> Para Sora / Veo / Kling. Duración objetivo **6-8 s por clip**, vertical 9:16, sin texto quemado
> (el texto se agrega después en la edición).

### V1 · Hook de problema (para Meta/TikTok)

```
Vertical 9:16, 7 seconds. A young man opens a bathroom drawer crowded with a beard
trimmer, a razor, a body groomer and tangled cables. He sighs and closes it. Cut to the
same drawer holding only one black and lime-green electric body shaver, clean and tidy.
Handheld camera, warm bathroom light, realistic documentary style, no text overlays,
no logos.
```

### V2 · Demostración de uso

```
Vertical 9:16, 8 seconds. Close-up of a man's hand attaching a guide comb onto a black
and lime-green electric body shaver, then running it in one smooth pass along his jawline.
Slow push-in on the trimmed area. Natural window light in a modern bathroom, shallow
depth of field, crisp macro detail on the stainless steel blade, realistic skin texture.
No text overlays, no logos.
```

### V3 · Rostro y cuerpo

```
Vertical 9:16, 7 seconds. Three quick connected shots of the same man using the black and
lime-green electric body shaver: first on his jawline, then on his chest, then on his
forearm. Consistent warm bathroom lighting, handheld camera, natural movement between
shots. No text overlays, no logos.
```

### V4 · Qué viene en la caja

```
Vertical 9:16, 6 seconds. Slow top-down camera move over a linen surface where a black
and lime-green electric body shaver, three guide combs, a spare head, a USB cable and a
cleaning brush are laid out one by one. Soft natural light, muted earthy palette,
satisfying product-reveal rhythm. No text overlays, no logos.
```

### V5 · Cierre con oferta

```
Vertical 9:16, 6 seconds. The black and lime-green electric body shaver rotates slowly on
a cream marble surface with soft studio light, then two identical units slide in beside it
to form a set of three. Clean premium product-commercial look, warm ivory background,
subtle lime accent light. No text overlays, no logos.
```

**Guion de voz en off (para V1 + V2 juntos, 15 s):**
> "¿Tenés una máquina para la barba, otra para el cuerpo y cuchillas que se gastan?
> Esta hace todo: elegís el largo con los peines de 1, 3 o 5 milímetros, la pasás en seco
> y se carga por USB. Rostro y cuerpo, un solo equipo."

---

## Notas de criterio

- **No inventar reseñas, porcentajes ni "+1.000 clientes".** Es publicidad engañosa (Ley 24.240) y motivo de baja en Shopify. La sección de reseñas calcula sola el promedio con las reseñas reales que se carguen.
- **No poner precio tachado falso** en el individual: la Resolución 7/2002 exige que ese precio anterior haya existido de verdad.
- Los descuentos de los packs se muestran en la ficha **sólo si existe el descuento automático en Shopify**; si no, el cliente ve un precio en la ficha y otro en el carrito.

---

## Videos de Google Flow · revisión del 2026-09-06

Carpeta revisada: `~/Descargas/videos para gonvra/` (11 clips, 9:16, 6-8 s).

**Problema: el producto de los videos no es el producto que se vende.**
Los clips muestran una máquina tipo Philips OneBlade (cuerpo plano rectangular, laterales
verdes acanalados, cabezal desmontable, peines negros). El producto real es una **MLG LT-187**:
cuerpo redondeado tipo gota, botón verde lima en un óvalo, cabezal ancho de lámina y
**3 peines amarillos**. Además, en `Electric_shaver_laid_out_202609061321.mp4` se lee una
marca inventada por la IA en el mango ("N&SBRIOT").

Riesgo concreto: el cliente ve un producto y recibe otro → contracargos, disputas y rechazo
de anuncios en Meta por creativo que no coincide con la landing. No se subieron a la tienda.

### Lo único aprovechable tal cual

`~/Claude/gonvra-brand/clips-utiles/hook-cajon-desordenado.mp4` — recorte de 4,3 s del clip
del cajón (cajón lleno de aparatos y cables → lo cierra). No se ve ningún producto, sirve
como gancho de anuncio.

### Cómo rehacerlos bien en Google Flow

El error está en generar de **texto a video**: el modelo inventa el aparato. Hay que usar
**Frames to Video / Ingredients to Video** y arrancar de una foto del producto real.

Frames listos para arrastrar (720×1280): `~/Claude/gonvra-brand/flow-refs/`

| Frame | Usar para |
|-------|-----------|
| `ref-1-kit-flatlay.jpg` | Qué viene en la caja |
| `ref-2-counter.jpg` | Producto sobre la mesada / apertura |
| `ref-3-uso-brazo.jpg` | Demostración de uso en el cuerpo |
| `ref-4-tres-unidades.jpg` | Cierre con el pack de 3 |
| `ref-5-packshot.jpg` | Giro de producto sobre fondo marfil |
| `ref-6-mesada-vertical.jpg` | Revelado del producto para anuncios |
| `ref-7-rostro.jpg` | *falta generar* — uso en la cara |

**Paquete completo con los 7 prompts listos para copiar:**
`~/Claude/gonvra-brand/flow-refs/PROMPTS-FLOW.md`

Prompts para Flow (con el frame cargado como primer cuadro):

```
Animate this exact product photograph. Keep the device identical in shape, colour and
proportions — do not redesign it, do not add logos or text. Slow camera push-in, subtle
parallax, soft natural light, 6 seconds, vertical 9:16, photorealistic.
```

```
Animate this exact photograph: the hand keeps sliding the device slowly along the forearm
in one continuous pass. Keep the device identical in shape and colour, no logos, no text.
Handheld camera, natural bathroom light, 6 seconds, vertical 9:16, photorealistic.
```

```
Animate this exact packshot: the three identical units rotate slowly together on the ivory
surface. Keep them identical to the photograph, no logos, no text. Studio light with a
subtle lime accent, 6 seconds, vertical 9:16.
```

Regla para todos: *"Keep the device identical to the reference image. No logos, no text,
no brand marks."*

---

## Videos propios integrados (2026-09-07)

Los clips de `~/Descargas/videos para la tienda/` **sí muestran el producto correcto**
(cuerpo redondeado, botón lima en óvalo, cabezal ancho de lámina). Ya están en la tienda.

### En la página

Shopify **no acepta .mp4 como asset del tema** (lo sube pero devuelve 404). Solución: los
clips se convirtieron a **WebP animado** (12 fps, 460 px de ancho, ~4 s, 400-570 KB cada uno).

| Asset | Dónde |
|-------|-------|
| `gv-galeria-clip.webp` | primer cuadro de la galería del producto, con ícono de play |
| `gv-clip-rostro.webp` | tarjeta "Rostro y patillas" |
| `gv-clip-cuerpo.webp` | tarjeta "Cuerpo" |
| `gv-clip-caja.webp` | tarjeta "Qué trae la caja" |
| `gv-clip-agua.webp` | tarjeta "Se enjuaga" |

La sección `gv-videos` acepta tres fuentes por tarjeta, en este orden: video subido a
Shopify → **URL de un .mp4** → clip WebP del tema → imagen. Cuando se suban los mp4 a
Content → Files conviene pegar la URL: mejor calidad y menos peso.

Corrección de contenido: la FAQ decía que no se podía mojar. La caja del proveedor dice
**100% washable** y hay un clip enjuagándola, así que ahora dice que el cabezal se enjuaga
bajo la canilla y que no se cargue mojada.

### Anuncios con Remotion

Proyecto: `~/Claude/gonvra-ads/` (Remotion 4.0.521, ya instalado).

```bash
cd ~/Claude/gonvra-ads && npx remotion studio      # editar en el navegador
cd ~/Claude/gonvra-ads && npx remotion render Anuncio-Problema out/anuncio-problema.mp4
```

Los guiones están en `src/guiones.ts` (texto, clip y duración de cada escena).
Salida en `~/Claude/gonvra-ads/out/`, 1080×1920 a 30 fps:

| Archivo | Duración | Para qué |
|---------|---------:|----------|
| `anuncio-problema.mp4` | 19,5 s | frío: cajón desordenado → solución → demostración → cierre |
| `anuncio-producto.mp4` | 13,5 s | retargeting: producto, barba, cuerpo, enjuague |
| `anuncio-demo.mp4` | 12,5 s | demostración pura, sin promesas |

Los tres cierran con el pack de 3 sobre tarjeta marfil, la ola animada de la marca y el
botón GONVRA.COM. Sin reseñas ni porcentajes inventados.

---

## ⚠️ El tema está PUBLICADO

`GONVRA — Landing de vista previa` (#148158414963) figura como **[live]**: lo que se sube
ya lo ve el público. Los push ahora necesitan `--allow-live`.

Con la tienda en vivo y **sin medios de pago activos**, cualquier visita que llegue no
puede comprar. Es lo primero a resolver.

← Ver también [[GONVRA]] · [[GONVRA - Meta Ads]] · [[Generar imagenes]]
