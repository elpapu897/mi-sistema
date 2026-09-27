# GONVRA · Paquete para Google Flow

**Regla de oro:** nunca uses *texto a video*. Siempre **Frames to Video** (subís la imagen
como primer cuadro). Si generás de texto, Veo se inventa el aparato y te sale un OneBlade.

Configuración para todos los clips:
- Modo: **Frames to Video** (imagen inicial)
- Formato: **9:16 vertical**
- Duración: **6-8 s**
- Sin texto ni logos en el video (el texto se pone después en la edición)

Los frames están en esta misma carpeta.

---

## PARA LA PÁGINA DE PRODUCTO — sección "Mirá cómo se usa"

### P1 · Rostro y patillas
**Frame:** `ref-7-rostro.jpg` ← *falta generar, ver el final del archivo*

```
Animate this exact photograph. The man slowly slides the shaver upward along his jawline
in one smooth continuous pass, then lowers his hand. Keep the device identical in shape,
colour and proportions to the reference image — do not redesign it, do not add logos,
text or brand marks. Handheld camera with a slight drift, natural warm bathroom light,
realistic skin texture, 6 seconds, vertical 9:16, photorealistic.
```

### P2 · Cuerpo
**Frame:** `ref-3-uso-brazo.jpg`

```
Animate this exact photograph. The hand keeps sliding the device slowly down the forearm
in one continuous pass, revealing an evenly trimmed strip. Keep the device identical in
shape, colour and proportions to the reference image — do not redesign it, do not add
logos, text or brand marks. Handheld camera, natural window light in a modern bathroom,
shallow depth of field, 6 seconds, vertical 9:16, photorealistic.
```

### P3 · Qué trae la caja
**Frame:** `ref-1-kit-flatlay.jpg`

```
Animate this exact top-down photograph. Very slow camera push-in over the laid-out kit,
with a soft light sweep moving across the surface. Everything stays exactly where it is.
Keep the device and every accessory identical to the reference image — do not redesign
them, do not add or remove items, no logos, no text. Soft natural light, muted earthy
palette, 6 seconds, vertical 9:16, photorealistic.
```

---

## PARA ANUNCIOS (Meta / TikTok)

### A1 · Gancho del problema
**Ya está hecho:** `~/Claude/gonvra-brand/clips-utiles/hook-cajon-desordenado.mp4` (4,3 s)

Es el recorte del clip del cajón, cortado antes de que aparezca el producto equivocado.
Si querés regenerarlo más largo, usá texto a video (acá no se ve el producto, así que no hay riesgo):

```
Vertical 9:16, 6 seconds. A young man opens a bathroom drawer crammed with tangled cables,
an old beard trimmer and a body groomer. He exhales, pushes it shut with his hip and walks
out of frame. Handheld camera, warm bathroom light, realistic documentary style, no text
overlays, no logos.
```

### A2 · Revelado del producto (va después del gancho)
**Frame:** `ref-6-mesada-vertical.jpg`

```
Animate this exact photograph. Slow cinematic push-in toward the device standing on the
marble counter, with soft morning light shifting gently across the surface. Keep the
device identical in shape, colour and proportions to the reference image — do not redesign
it, do not add logos, text or brand marks. 6 seconds, vertical 9:16, photorealistic.
```

### A3 · Cierre con el pack
**Frame:** `ref-4-tres-unidades.jpg`

```
Animate this exact packshot. The three identical units rotate slowly and together on the
ivory surface, with a subtle lime accent light passing across them. Keep them identical
to the reference image — same shape, same colour, same proportions, no logos, no text.
Clean studio product-commercial look, 6 seconds, vertical 9:16.
```

### A4 · Giro de producto (comodín para intros y cierres)
**Frame:** `ref-5-packshot.jpg`

```
Animate this exact packshot. The device rotates slowly 180 degrees on its vertical axis
over a seamless ivory background, soft studio light with a gentle highlight travelling
along the metal head. Keep it identical to the reference image, no logos, no text.
6 seconds, vertical 9:16.
```

---

## Guion de voz en off (15 s, para A1 + A2 + A3)

> "¿Tenés una máquina para la barba, otra para el cuerpo y cuchillas que se gastan?
> Esta hace todo: elegís el largo con los peines, la pasás en seco y se carga por USB.
> Rostro y cuerpo, un solo equipo."

Orden de edición sugerido: **A1 (0-4 s) → A2 (4-9 s) → P2 (9-13 s) → A3 (13-18 s)**

---

## FALTA UNA IMAGEN — pedile esto a Codex/ChatGPT

Es el único frame que no tengo. Adjuntale como referencia
`~/Claude/product-assets/rasuradora-integral-hero-v1.png` y pedile:

```
Vertical 9:16 photograph of a man in his early thirties in a bright modern bathroom,
holding the black and lime-green electric body shaver from the reference image against
his jawline, mid-stroke. Keep the device identical to the reference: rounded teardrop
black body, lime-green power button inside an oval recess, wide stainless steel foil head.
Natural warm window light, blurred bathroom background, shallow depth of field, realistic
skin texture with visible short stubble. No text, no logos, no brand marks, no watermark.
```

Guardala como `~/Claude/gonvra-brand/flow-refs/ref-7-rostro.jpg` y ya tenés los 7 frames.

---

## Recordatorio de qué NO hacer

- No generar de texto a video: aparece un producto que no es el tuyo.
- Revisar siempre el mango antes de usar el clip: si la IA escribió una marca inventada
  (ya pasó con "N&SBRIOT"), ese clip se descarta.
- Los peines reales son **3 y amarillos**. Si en el video aparecen 4 peines negros o un
  cabezal desmontable extra, ese clip no sirve.


---

# PENDIENTES · lo que falta generar (2026-09-07)

## 1 · Antes y después de la zona íntima (2 imágenes)

Reemplaza el antes/después del brazo. **El mismo encuadre en las dos**, sólo cambia la
última línea. Adjuntar como referencia `~/Claude/product-assets/rasuradora-integral-hero-v1.png`.

```
Vertical 4:5 close-up photograph of a man's lower abdomen and bikini line, cropped from
the navel to the top of grey cotton boxer briefs, seen from a fixed camera angle above.
Clean modern bathroom, soft natural window light from the left, blurred background.
The black and lime-green electric body shaver from the reference image rests on the skin
at the edge of the frame. Tasteful, clinical, non-explicit grooming-brand photography.
[ANTES] The skin shows natural, dense body hair.
[DESPUÉS] The skin is smooth and evenly trimmed.
Identical framing, identical lighting, identical pose in both images.
No text, no logos, no watermark.
```
Guardar como `gv-antes.jpg` y `gv-despues.jpg` (1100×1375) en
`~/Claude/gonvra-theme/assets/`. La sección ya las toma automáticamente.

## 2 · Video "limpiala y cargala" (6 s, Flow)

Falta el clip de la persona limpiando con el cepillo y enchufando el USB.
Primero generar el frame con ChatGPT/Codex:

```
Vertical 9:16 photograph of a man's hands holding the black and lime-green electric body
shaver from the reference image over a cream marble bathroom counter, brushing the blade
with the small black cleaning brush that comes in the box. Warm natural window light,
shallow depth of field, realistic skin texture. No text, no logos, no watermark.
```

Y después animarlo en Flow (Frames to Video):

```
Animate this exact photograph. The hands keep brushing the blade twice, then one hand
plugs a USB cable into the base of the device. Keep the device identical in shape, colour
and proportions to the reference image — do not redesign it, no logos, no text.
Handheld camera, natural light, 6 seconds, vertical 9:16, photorealistic.
```

## 3 · Cierre "Una sola rasuradora para toda tu rutina"

Hoy usa el clip de la galería. Si querés algo propio, generar en Flow con
`ref-4-tres-unidades.jpg` y el prompt A3 de más arriba.


## 4 · Comparación para el carrusel: corte disparejo vs. corte parejo

Es sobre **cómo corta la máquina**, no sobre la piel. Eso es real y se puede mostrar.
Una sola imagen partida al medio, con etiqueta en cada lado.

```
Vertical 4:5 split-screen comparison photograph of the same man's chest, same lighting,
same camera angle on both halves. LEFT HALF: the hair is cut unevenly, with visible
patches, steps and uneven lengths, like a rushed job with a cheap trimmer. RIGHT HALF:
the hair is cut perfectly even at a uniform short length, neat and clean. Clean modern
bathroom, soft natural window light, realistic skin texture, no redness, no irritation,
no blemishes. Documentary product-comparison photography. No text, no logos, no watermark.
```

Repetir el mismo prompt cambiando `chest` por `lower abdomen and bikini line` y por
`forearm` para tener tres.

Guardar en `~/Claude/gonvra-theme/assets/` como `gv-comparacion-1.jpg`,
`gv-comparacion-2.jpg`, `gv-comparacion-3.jpg` (1100×1375).

Después, en el editor del tema → sección **GONVRA · Ficha** → campo
**"Imágenes extra al final de la galería"**, escribir:

```
gv-comparacion-1.jpg, gv-comparacion-2.jpg, gv-comparacion-3.jpg
```

Y aparecen al final del carrusel con su miniatura.

> Importante: en estas imágenes la piel va **sana en los dos lados**. Lo que cambia es
> el corte del vello, no la piel. Una comparación de piel irritada a piel perfecta es una
> promesa que el producto no cumple.


---

# REGENERAR · brazo y rostro (2026-09-07)

El problema del clip del brazo fue que Veo **deformó la rasuradora** durante el movimiento.
Se arregla con tres reglas: acción única y corta, cámara casi quieta, y la frase de
rigidez. Cuanto más se mueve la cámara, más se le deforma el objeto.

## A · Brazo · "Pasala en seco, sin espuma"

**Frame:** `ref-3-uso-brazo.jpg`

```
Animate this exact photograph with minimal motion. The hand slides the shaver down the
forearm ONE single slow continuous stroke, revealing a clean trimmed strip behind it.
The camera stays almost completely still, only a tiny handheld drift.
CRITICAL: the device must stay rigid and geometrically identical to the reference image
in every frame — same silhouette, same proportions, same lime-green button, same wide
steel head. Do not bend, stretch, morph or redesign it. No logos, no text, no brand marks.
Natural window light, realistic skin texture, 6 seconds, vertical 9:16, photorealistic.
```

## B · Rostro y patillas

Primero el frame, con ChatGPT/Codex, adjuntando
`~/Claude/product-assets/rasuradora-integral-hero-v1.png`:

```
Vertical 9:16 photograph of a man in his early thirties in a bright modern bathroom,
holding the black and lime-green electric body shaver from the reference image flat
against his cheek at the jawline, mid-stroke, seen from a three-quarter angle. The device
is large and fully visible in the frame. Keep it identical to the reference: rounded
teardrop black body, lime-green power button inside an oval recess, wide stainless steel
foil head. Natural warm window light, blurred bathroom background, shallow depth of field,
realistic skin texture with short stubble. No text, no logos, no brand marks, no watermark.
```

Guardar como `ref-7-rostro.jpg`. Después en Flow (Frames to Video):

```
Animate this exact photograph with minimal motion. The man slides the shaver upward along
his jawline ONE single slow continuous stroke, then stops. The camera stays almost
completely still.
CRITICAL: the device must stay rigid and geometrically identical to the reference image
in every frame — same silhouette, same proportions, same lime-green button, same wide
steel head. Do not bend, stretch, morph or redesign it. No logos, no text, no brand marks.
Natural warm bathroom light, realistic skin texture, 6 seconds, vertical 9:16, photorealistic.
```

## Cómo revisar antes de usar el clip

1. Pausá en el segundo 3 y en el 5: el mango tiene que tener la misma forma que en el frame.
2. Si el cabezal se estira o el cuerpo se curva, descartalo y volvé a tirar la generación.
3. Si aparece texto o marca en el mango, descartalo.


---

# ANUNCIOS PARA TIKTOK · 3 conceptos completos (2026-09-08)

Cada uno son 3 clips de 6 s que después se pegan. Primero la imagen, después el video.
Siempre **Frames to Video**, nunca texto a video.

## TT-1 · "El cajón" — público frío

**Clip 1 (gancho).** No hace falta imagen: acá no se ve el producto, así que va texto a video.
```
Vertical 9:16, 6 seconds. A young man opens a bathroom drawer crammed with tangled cables,
an old beard trimmer and a disposable razor. He exhales, closes it with his hip and leaves
the frame. Handheld phone camera, warm bathroom light, realistic documentary style, slightly
grainy, no text overlays, no logos.
```

**Clip 2 (revelado).** Frame: `ref-6-mesada-vertical.jpg`
```
Animate this exact photograph with minimal motion. Slow cinematic push-in toward the device
standing on the marble counter, morning light shifting gently across the surface.
CRITICAL: the device stays rigid and geometrically identical to the reference image in every
frame. Do not bend, stretch or redesign it. No logos, no text.
6 seconds, vertical 9:16, photorealistic.
```

**Clip 3 (cierre).** Frame: `ref-4-tres-unidades.jpg`
```
Animate this exact packshot. The three identical units rotate slowly together on the ivory
surface with a subtle lime accent light passing across them. Keep them identical to the
reference image. No logos, no text. 6 seconds, vertical 9:16.
```

**Carteles para poner encima al editar:**
1. `¿UN APARATO PARA CADA ZONA?` → 2. `Y NINGUNO HACE TODO` → 3. `ESTA HACE LAS TRES` → 4. `gonvra.com`

---

## TT-2 · "La lámina" — el ángulo que mejor diferencia

**Clip 1.** Frame: `ref-3-uso-brazo.jpg`
```
Animate this exact photograph with minimal motion. The hand slides the shaver down the
forearm ONE single slow continuous stroke, revealing a clean trimmed strip behind it. The
camera stays almost completely still.
CRITICAL: the device must stay rigid and geometrically identical to the reference image in
every frame. Do not bend, stretch, morph or redesign it. No logos, no text.
Natural window light, realistic skin texture, 6 seconds, vertical 9:16, photorealistic.
```

**Clip 2 (macro del filo).** Generar primero la imagen con ChatGPT/Codex:
```
Vertical 9:16 extreme macro photograph of the stainless steel foil head of the black and
lime-green electric body shaver from the reference image, filling most of the frame, lit
from the side so the perforated metal texture and the lime-green frame are clearly visible.
Dark blurred background, studio product photography. No text, no logos, no watermark.
```
Y animarla:
```
Animate this exact macro photograph. The camera orbits very slowly around the steel head
while a highlight travels along the metal. Keep the head identical to the reference image.
No logos, no text. 6 seconds, vertical 9:16.
```

**Clip 3.** El del enjuague que ya tenés: `Hand_rinsing_shaver_under_water`.

**Carteles:**
1. `¿LA MAQUINITA TE DEJA LA PIEL ARDIENDO? 😖` → 2. `EL PROBLEMA ES LA HOJA PEGADA A LA PIEL` → 3. `ESTA TIENE LÁMINA DE ACERO EN EL MEDIO 👀` → 4. `Y SE LAVA BAJO LA CANILLA 💧`

---

## TT-3 · "Qué trae" — el que mejor convierte al final del embudo

**Clip 1.** Frame: `ref-1-kit-flatlay.jpg`
```
Animate this exact top-down photograph. Very slow camera push-in over the laid-out kit with
a soft light sweep crossing the surface. Everything stays exactly where it is. Keep the
device and every accessory identical to the reference image — do not add or remove items.
No logos, no text. 6 seconds, vertical 9:16, photorealistic.
```

**Clip 2.** El de la mano levantando el peine que ya tenés: `Hand_picking_up_comb_guard`.

**Clip 3.** El de limpieza y carga que ya tenés: `Hands_brushing_blade_and_plugging`.

**Carteles:**
1. `LO QUE VIENE EN LA CAJA` → 2. `3 PEINES: 1, 3 Y 5 MM` → 3. `CABEZALES DE REPUESTO` → 4. `CABLE USB Y CEPILLO` → 5. `gonvra.com`

---

## Descripción del producto para el pie de los TikToks

> Rasuradora integral recargable. Rostro, cuerpo y zona íntima con el mismo equipo.
> Peines de 1, 3 y 5 mm, se usa en seco, se enjuaga bajo la canilla y se carga por USB.
> Envío a todo el país con seguimiento. gonvra.com

**Hashtags:** #cuidadopersonal #afeitadora #rutinamasculina #argentina #envioatodoelpais

---

## Los videos ya renderizados

Si no querés armar nada, en `~/Claude/gonvra-ads/out/` ya están los cuatro anuncios listos
para subir, con carteles, música muteada y cierre de marca. El que más se parece a lo que
funciona en TikTok es `anuncio-gancho.mp4`.
