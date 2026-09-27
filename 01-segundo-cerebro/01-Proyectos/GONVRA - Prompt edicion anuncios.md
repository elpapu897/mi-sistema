---
tags: [gonvra, ads, prompt, edicion, resolve]
---
# GONVRA · Prompt para editar los anuncios

> Plantilla lista para pegarle a un agente (Claude Code, Codex, GPT-6) que tenga acceso a
> esta máquina y al MCP `davinci-resolve`. Adaptado de un prompt de edición que funcionó
> bien, pero con mis datos, mis rutas y mis reglas.
> Relacionado: [[GONVRA - Prompts Flow]] · [[GONVRA - Fabrica de anuncios]] · [[GONVRA]]

---

## ▼ COPIAR DESDE ACÁ ▼

Soy Matii, dueño de GONVRA (gonvra.com), una tienda de cuidado personal. El producto de
esta tanda es una **rasuradora integral recargable** para rostro, cuerpo y zona íntima.

Generé material de video con Google Flow (Veo, *Frames to Video* sobre mis propias fotos de
producto) y ya tengo los conceptos escritos. Tu encargo es **editar y exportar tres anuncios
verticales para TikTok/Instagram** dentro de DaVinci Resolve, dejándolos editables.

No hay voz en off. Estos anuncios se cuentan con **carteles de texto en pantalla**, sonido
ambiente de los clips y, si corresponde, música. El ritmo lo manda el texto, no una locución.

### ARCHIVOS Y REFERENCIAS

Conceptos, clips previstos y los carteles exactos de cada anuncio:
`~/OBSIDIAN/01-Proyectos/GONVRA - Prompts Flow.md` → sección **ANUNCIOS PARA TIKTOK · 3 conceptos completos**

Identidad de marca (colores exactos, tipografía, voz):
`~/Claude/gonvra-brand/brand-guidelines.md`

Logo y wordmark:
`~/Claude/gonvra-brand/gonvra-wordmark.svg`
`~/Claude/gonvra-brand/logo_gonvra_wordmark_20260906_dark.svg`

Frames de referencia que usé en Flow (sirven para saber cómo tiene que verse el aparato):
`~/Claude/gonvra-brand/flow-refs/ref-1…ref-7`

Clips generados en Flow, repartidos en varias carpetas:
- `~/Descargas/` (sueltos, con fecha en el nombre)
- `~/Descargas/videos para la tienda/`
- `~/Descargas/videos para gonvra/`
- `~/Descargas/GONVRA - flow/`
- `~/Claude/gonvra-brand/clips-utiles/hook-cajon-desordenado.mp4`

Anuncios viejos hechos con Remotion, **solo como referencia de tono y de duración**, no para
reciclar: `~/Claude/gonvra-ads/out/anuncio-gancho.mp4` y los otros tres.

### LOS TRES ANUNCIOS

**TT-1 · "El cajón"** — público frío. Gancho de problema → revelado → cierre.
Carteles: `¿UN APARATO PARA CADA ZONA?` → `Y NINGUNO HACE TODO` → `ESTA HACE LAS TRES` → `gonvra.com`

**TT-2 · "La lámina"** — el ángulo que mejor diferencia al producto.
Carteles: `¿LA MAQUINITA TE DEJA LA PIEL ARDIENDO? 😖` → `EL PROBLEMA ES LA HOJA PEGADA A LA PIEL` → `ESTA TIENE LÁMINA DE ACERO EN EL MEDIO 👀` → `Y SE LAVA BAJO LA CANILLA 💧`

**TT-3 · "Qué trae"** — el de más abajo del embudo, para retargeting.
Carteles: `LO QUE VIENE EN LA CAJA` → `3 PEINES: 1, 3 Y 5 MM` → `CABEZALES DE REPUESTO` → `CABLE USB Y CEPILLO` → `gonvra.com`

Los textos de los carteles los podés ajustar si un corte queda mejor con otra redacción, pero
**no cambies el argumento de venta ni agregues promesas nuevas**. Si cambiás un cartel,
decime cuál y por qué.

Empezá por **TT-1**: ahí fijás el lenguaje visual (tipografía, tamaño, posición, animación de
entrada de los carteles, tratamiento de color). TT-2 y TT-3 heredan esa identidad.

### CÓMO QUIERO QUE TRABAJES

**1 · Inventariá y mirá el material de verdad.**

Recorré las carpetas de arriba y armá un inventario en CSV con ruta completa, duración,
resolución, FPS y códec de cada clip. Usá `ffprobe`, no adivines por el nombre del archivo.

Después **mirá los clips**. Extraé fotogramas con `ffmpeg` y revisalos. No te fíes del nombre
ni de la miniatura. Armá un catálogo reutilizable con: archivo, intervalo aprovechable
(desde→hasta), qué se ve, qué se escucha y para qué parte de qué anuncio sirve. Marcá las
dudas y lo que falte.

**2 · Descartá los clips fallados. Esto es lo más importante del trabajo.**

Veo me deformó el producto en varias generaciones. Un clip se descarta si:
- el cuerpo de la rasuradora se curva, se estira o cambia de silueta durante el movimiento;
- el cabezal de acero cambia de forma o de tamaño;
- aparece texto o una marca inventada en el mango (ya pasó con "N&SBRIOT");
- aparecen 4 peines negros o un cabezal extra: los peines reales son **3 y amarillos**;
- el aparato directamente no es el mío (pasa cuando se generó de texto a video).

Revisá cada clip candidato cuadro por cuadro en los momentos de más movimiento, no solo el
primer fotograma. Si un clip es bueno en los primeros 3 segundos y se deforma después,
recortalo antes de la deformación y anotalo.

Si después del filtro un anuncio se queda sin un clip necesario, **decime exactamente qué
frame y qué prompt de Flow tengo que generar** (con el formato de mis notas: frame de
referencia + prompt en inglés + la cláusula de rigidez) y seguí con el resto.

**3 · Editá con intención.**

Cada corte tiene que estar justificado por el cartel que está en pantalla y por el
movimiento del clip. No cortes cada N segundos fijos.

El gancho son los primeros 2 segundos: ahí se gana o se pierde. Que el primer cuadro ya
tenga movimiento o el cartel ya legible.

Duración objetivo 15-20 s por anuncio. Si un clip de 6 s aporta 3 s buenos, usá 3 s. No
estires nada para llegar a una duración.

Mostrá lo que el cartel dice. Si el cartel habla de la lámina de acero, en pantalla tiene
que estar la lámina. Nada de b-roll de relleno.

**4 · Carteles y gráficos.**

Usá la paleta de la marca: tinta `#0D201A`, marfil `#F7F8F2`, lima `#C8E54A`, gris `#66706B`.
Sans serif geométrica, títulos con alto contraste. El lima es **acento**, no fondo de todo.

Los carteles tienen que leerse en un teléfono a brillo bajo: peso alto, contraste real contra
el video (usá una caja o un degradado si hace falta), y dentro de los márgenes seguros de
TikTok — nada de texto en los 250 px de abajo ni en los 150 de arriba, que los tapa la UI de
la app.

El cierre lleva el wordmark y `gonvra.com`. Sobrio, un par de segundos, sin fuegos
artificiales.

Animaciones simples y consistentes entre los tres anuncios. Si Fusion te complica, resolvelo
con títulos y keyframes; prefiero limpio y consistente antes que vistoso y desparejo.

**5 · Montá en DaVinci Resolve por el MCP `davinci-resolve`.**

Primero **comprobá la conexión real del MCP** antes de prometer nada. Si es la edición
gratuita, revisá el puente en `Workspace > Scripts > resolve_bridge`. Si el MCP no conecta,
decímelo con el error concreto y armá los anuncios con `ffmpeg` como plan B, dejando
igualmente los EDL/XML para que yo pueda abrirlos.

Proyecto nuevo, **tres timelines independientes**: `TT-1-Cajon`, `TT-2-Lamina`, `TT-3-Que-Trae`.

Vertical **1080×1920**. Revisá los FPS de las fuentes (los clips de Flow no siempre coinciden)
y elegí una configuración coherente; si hay que conformar algo, decilo.

Pistas ordenadas y con nombre: video de clips, carteles, logo, ambiente, música. Que yo pueda
abrirlo y entender qué es cada cosa sin preguntarte.

Los clips de Flow ya son verticales; si usás alguno horizontal, reencuadralo con criterio
(que el producto y las manos queden en cuadro, no cortados).

**6 · Audio y color.**

**Música: no tengo ninguna pista con licencia.** No metas música bajada de cualquier lado.
Trabajá con el ambiente de los clips y, si hace falta, un SFX mínimo y justificado (el agua
del enjuague, el clic del encendido). Si creés que un anuncio necesita música, decime qué
tipo y lo consigo yo.

Nivelá el ambiente para que no haya saltos de volumen entre cortes. Nada saturado.

Igualá exposición y balance de blancos entre clips: vienen de generaciones distintas y se
notan los saltos de temperatura. Compará fotogramas antes y después, no apliques un look a
ciegas.

**7 · Reglas de contenido que no se negocian.**

- Nada de promesas que el producto no cumple. Nada de "antes irritado / después piel
  perfecta": lo que cambia es **el corte del vello**, no la piel. Piel sana en los dos lados.
- Sin afirmaciones clínicas, sin reseñas o testimonios inventados, sin urgencia falsa
  ("últimas unidades", contadores).
- No inventes cifras, ni porcentajes, ni cantidad de clientes.
- El material generado sirve para mostrar el producto y explicar el uso, no para fabricar
  pruebas sociales.
- Tono de marca: directo, claro y tranquilo. Primero lo útil, después lo aspiracional.

**8 · Revisá de verdad.**

Exportá versiones de revisión y **miralas completas**, con sonido. Buscá: producto deformado
que se te pasó, carteles tapados por la UI, texto que entra o sale mal, faltas de ortografía,
negros, huecos, saltos de color o de volumen, y cortes donde la imagen no acompaña al cartel.

Corregí y volvé a revisar lo tocado. Guardá versiones recuperables de las timelines.

### DÓNDE TRABAJAR Y QUÉ ENTREGAR

Trabajá en `~/Claude/gonvra-edits/` (creala). Ahí van el inventario, el catálogo, los
recortes, las revisiones y los finales. Referenciá los originales de `~/Descargas`, no los
dupliques.

**Dejá intactos** los clips originales, los frames de `flow-refs` y los proyectos que ya
existen en `~/Claude/`.

Entregables:
- Tres MP4 verticales 1080×1920: `TT-1-Cajon.mp4`, `TT-2-Lamina.mp4`, `TT-3-Que-Trae.mp4`
- Proyecto de Resolve exportado en `.drp` con las tres timelines
- El CSV del inventario y el catálogo de clips (me sirve para las próximas tandas)
- Un manifiesto de rutas para reabrir el proyecto sin material perdido
- SRT con los carteles, para subir a TikTok como texto accesible
- Una nota corta con: decisiones de edición, **qué clips descartaste y por qué**, qué falta
  generar en Flow, y pendientes reales

### AUTONOMÍA Y CRITERIO DE TERMINACIÓN

Tomá las decisiones de edición y ejecutá. No te quedes en un plan ni me pidas aprobar cada
corte. Te autorizo a crear el proyecto, editar los tres anuncios y renderizar.

Si hay un bloqueo real —el MCP no conecta, falta un clip insalvable, una decisión que solo yo
puedo tomar— explicá el punto concreto y avanzá con lo demás.

**No des el trabajo por terminado por haber creado las timelines o lanzado un render.**
Terminás cuando los tres anuncios están exportados, revisados y entregados con su proyecto
editable, o cuando identificás con claridad qué impide completar uno.

No afirmes que hiciste algo que no ejecutaste. No inventes capacidades de las herramientas:
comprobá qué hay disponible en esta instalación antes de prometer.

Mi prioridad es que los tres anuncios se vean bien y que **en ningún cuadro aparezca un
producto deformado o una marca que no es la mía**. Antes prefiero un anuncio de 12 segundos
impecable que uno de 20 con dos cuadros malos.

## ▲ COPIAR HASTA ACÁ ▲

---

## Notas para mí (no van en el prompt)

- Verificado el 2026-09-11: Resolve está en `/opt/resolve`, MCP `davinci-resolve` registrado,
  `ffmpeg`/`ffprobe` disponibles.
- Clips candidatos que ya existen para cada anuncio:
  - **TT-1**: `clips-utiles/hook-cajon-desordenado.mp4` · `Electric_body_shaver_standing_up…_202609071550.mp4` · `videos para gonvra/Electric_body_shavers_rotating_202609061328.mp4`
  - **TT-2**: `GONVRA - flow/brazo-corregido.mp4` · `Shaver_blade_texture_lighting_202609071529.mp4` o `videos para la tienda/Camera_orbiting_metal_blade_product_202609062254.mp4` · `Hand_rinsing_shaver_under_water_202609071535.mp4`
  - **TT-3**: `videos para gonvra/Electric_shaver_laid_out_202609061321.mp4` · `videos para la tienda/Hand_picking_up_comb_guard_202609062254.mp4` · `Hands_brushing_blade_and_pluggin…_202609071553.mp4`
- Los tres anuncios tienen material completo. No hace falta generar nada nuevo en Flow para
  esta tanda (sí para los pendientes de [[GONVRA - Prompts Flow]]).
- Pendiente mío: conseguir una pista de música con licencia.

← [[01-Proyectos/README|Proyectos]]
