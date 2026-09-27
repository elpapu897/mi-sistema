# GONVRA · Nota de edición — tres anuncios TikTok

**Fecha:** 2026-09-11 · **Salida:** 1080×1920, 24 fps, H.264

| Anuncio | Duración | Archivo |
|---|---|---|
| TT-1 · El cajón | 16.30 s | `finales/TT-1-Cajon.mp4` |
| TT-2 · La lámina | 15.80 s | `finales/TT-2-Lamina.mp4` |
| TT-3 · Qué trae | 15.04 s | `finales/TT-3-Que-Trae.mp4` |

---

## 1 · Bloqueo: el MCP de Resolve no conectó

Comprobado antes de empezar, como pediste. Error concreto:

```
SCRIPTING_UNAVAILABLE
"DaVinci Resolve is running but is not answering the scripting API."
```

Causa: tenés **DaVinci Resolve v21.1.0.0017, edición free**. Blackmagic bloquea el
scripting externo en free, y en 21.1 movió Python a Studio, así que el menú
`Workspace > Scripts` ya no lista `.py` y el puente in-app **no tiene desde dónde
lanzarse**. Está reportado como issue #203, justamente en Fedora 44.

No es configuración: no hay arreglo por software. Para que el MCP funcione hace falta
**Studio**, o **bajar a Resolve 21.0.x free** (ahí el puente sí funciona).

Se ejecutó el plan B: montaje con `ffmpeg` + interchange editable.

## 2 · Descartes (lo más importante)

Revisé cuadro por cuadro contra `flow-refs`. El producto real es: cuerpo negro mate en
gota, cuello lima, botón lima con ícono de encendido en hueco brillante, triángulo de
eject y cabezal de lámina de acero con topes lima.

**Descartados (6 de 13 candidatos):**

| Clip | Motivo |
|---|---|
| `Electric_shaver_product_reveal_…1322` | No es el producto: trimmer alargado con cuerpo lima (silueta OneBlade). **5 peines** en vez de 3 |
| `Electric_body_shavers_rotating_…1328` | No es el producto (franja lima lateral) y **el cuerpo se curva como banana** entre los cuadros 2 y 4 |
| `Electric_body_shavers_rotating_…1333` | Misma generación fallada que la anterior |
| `Electric_shaver_laid_out_…1321` | Producto off-model + **texto de marca inventado en el mango** + **4 peines y cabezal extra** |
| `Electric_shaver_and_accessories_…1321` | Producto off-model + texto inventado en el mango + 5 peines |
| `Camera_orbiting_metal_blade_…2254` | Desde 1.3 s la silueta se afina y aparece un **aro cromado que no existe** |
| `Man_demonstrating_electric_shaver_1080p` | UGC con voz (no sirve sin locución) y silueta off-model que cambia de proporción |

**Recortados antes de la deformación:**

- `Hand_rinsing_shaver_under_water` → usable **0.00–2.05 s**. Desde ~2.1 s el cuerpo se
  arquea, el botón lima se estira hasta desaparecer y el cabezal se convierte en un
  cartucho sin lámina.
- `Man_organizing_cluttered_bathroo…1304` → usable **0.00–4.20 s**. Después revela un
  aparato off-model.

## 3 · Dos cosas de tus notas que no coincidían

**a) "Los peines reales son 3 y amarillos".** En `ref-1-kit-flatlay` y en el material
bueno los peines tienen **dientes negros con base lima**. No es contradicción real: lo
"amarillo" es la base. Ajusté el criterio de descarte a *"4 peines" o "peines sin base
lima"*, no al color de los dientes — si hubiera filtrado por dientes amarillos habría
descartado todo el material bueno, incluido tu propio frame de referencia.

**b) `Shaver_blade_texture_lighting_720p_202609062312`** es la misma toma que anotaste
para TT-2 pero **al doble de resolución** (720×1280 vs 360×640). Usé esa. Terminó siendo
el clip héroe: muestra el producto entero y después entra en macro sobre la lámina
perforada, justo cuando el cartel la nombra.

## 4 · Carteles que cambié (y por qué)

| Anuncio | Cambio | Motivo |
|---|---|---|
| TT-3 | **Saqué "CABEZALES DE REPUESTO"** | El kit filmado tiene rasuradora + 3 peines + cable USB + cepillo. **No hay cabezal de repuesto en ningún cuadro**, y tu propia descripción de producto tampoco los menciona. No iba a poner una promesa sin respaldo |
| TT-3 | Dividí "CABLE USB Y CEPILLO" en **"CEPILLO DE LIMPIEZA"** + **"CARGA POR CABLE USB"** | Como cartel único quedaba **6.8 s en pantalla**, casi la mitad del anuncio. Dividido, cada mitad cae sobre la acción que la muestra |
| TT-1 | Agregué **"SE ENJUAGA BAJO LA CANILLA"** | Quedaba un tramo de 3.75 s sin ningún cartel. El texto sale de tu propia descripción ("se enjuaga bajo la canilla"), no agrega promesa nueva |

El resto de los carteles quedó textual. Ningún argumento de venta cambió.

## 5 · Color

Medí cada clip con `signalstats` antes y después. Había **80 puntos de luma** de
diferencia (Y=95 el cajón, Y=176 el brazo) y dos familias de temperatura (cálida V≈140,
neutra V≈130). Corregí clip por clip hacia un objetivo común en vez de aplicar un look.

Resultado: U convergió a 120–121 y V quedó dentro de **2 puntos** entre los tres
anuncios, contra los 10 de dispersión original. El cajón se dejó a propósito más oscuro
que el resto: es el momento "problema" y subirlo le sacaba la intención.

## 6 · Audio — necesita tu decisión

**Los clips de Flow no tienen ambiente utilizable.** Medido:

| Clip | RMS |
|---|---|
| `Hands_brushing_blade_and_plugging` | **−65 dB** (silencio digital) |
| `Hand_rinsing_shaver_under_water` | −38 a −50 dB (inaudible) |
| `Shaver_blade_texture_lighting_720p` | −19.6 dB, pero **todo grave**: arriba de 4 kHz cae a −48 dB → es un retumbe artefacto de Veo, no sonido de producto |

Normalizarlo a −18 LUFS significaba meterle **+35 dB de ganancia a un piso de ruido**.
Lo probé y dejaba 15 dB de salto entre cortes. Así que los tres anuncios salen con
**pista de audio válida y uniforme en silencio** (−91 dB, sin saltos, sin saturación).

**Esto es lo que falta para publicar.** Como ofreciste conseguir la música, lo que
necesitan estos tres cortes es:

- **Una pista, instrumental, 90–100 BPM, percusión seca y bajo limpio**, sin voces y sin
  build-up dramático. Tipo "minimal electronic / lo-fi house". Los tres anuncios duran
  ~15 s, así que con **20 s de una sola pista** alcanza para los tres.
- Opcional y más barato: **3 SFX sueltos** con licencia — agua de canilla, clic de
  encendido, y un "whoosh" corto para la entrada de los carteles.

Pasame el archivo y los remezclo en una corrida.

## 7 · Entregables

```
~/Claude/gonvra-edits/
├─ finales/          TT-1-Cajon.mp4 · TT-2-Lamina.mp4 · TT-3-Que-Trae.mp4  (+ .srt de cada uno)
├─ proyecto/         .edl · .fcpxml · .drp de cada anuncio + manifiesto-rutas.json
├─ inventario/       inventario.csv (53 archivos) · catalogo-clips.csv (veredicto por clip)
├─ revisiones/       hojas de contacto de 16 cuadros de cada anuncio final
├─ frames/           hojas de contacto de los candidatos (evidencia de los descartes)
├─ carteles/         PNG 1080×1920 + render_card.py
└─ build.py          el montaje completo, reproducible
```

**Sobre el `.drp`:** la herramienta offline (`add_media_clip`) crea un `.drp` con **un
solo clip por proyecto** y no encadena, así que no se puede armar un único proyecto con
las tres timelines multiclip sin Resolve vivo. Entregué:

- **`.drp` por anuncio** → abre en Resolve con el anuncio ya montado en su timeline.
- **`.fcpxml` por anuncio** → esto es lo editable de verdad: importa cada corte como
  clip separado en pista 1 y los carteles en pista 2, con los puntos de entrada y salida
  sobre los **originales** (no se duplicó material).
- **`.edl` por anuncio** → respaldo simple, con el cartel de cada corte como comentario.

## 8 · Verificaciones hechas

- 0 errores de decodificación en los tres MP4
- 0 tramos negros ≥ 0.25 s
- Contraste real del texto medido sobre el peor fondo claro: **10.1:1 y 7.3:1** (mínimo
  aceptable 4.5:1)
- Márgenes seguros TikTok respetados: nada de texto en los 150 px de arriba ni en los 250 de abajo
- Sin huecos sin texto en los cambios de cartel (medido cuadro a cuadro en el corte de TT-2)
- Ortografía de los 13 carteles revisada
- Originales, `flow-refs` y `gonvra-ads/out` intactos

## 8 bis · Generación nueva en Flow (2026-09-11, sesión 2)

Se generó **1 video** en Google Flow y se integró a TT-1.

- **Clip:** `rostro-jawline-720p.mp4` — 720×1280, 8 s, 24 fps
- **Referencia:** `ref-7-rostro.jpg` (frames to video, como manda tu regla)
- **Config:** 720p · 8 s · 9:16 · x1 (720p es el tope de tu plan; no hay 1080p)

**Revisión cuadro por cuadro: APROBADO.** Verifiqué la ventana de más movimiento
(3.0–5.0 s, 16 cuadros a 8 fps con zoom al aparato): el cuerpo no se curva ni cambia de
silueta, el cabezal mantiene forma y topes lima, y no hay texto de marca inventado.

**Dos cosas honestas sobre este clip:**
- El movimiento no es el "trazo único" que pidió el prompt: pasa por mentón, mandíbula y
  mejilla.
- **No revela la línea afeitada.** La barba se ve igual al principio y al final, así que el
  clip muestra *el uso*, no *el resultado*.

**Color:** era el más cálido de todo el material (V=148.3 contra 134 de objetivo).
Corrección fuerte (`rm=-0.114`, `bm=+0.091`). TT-1 quedó en U=119.2 / V=132.6, alineado
con TT-2 (121.5/129.4) y TT-3 (120.5/131.4).

**Dónde entró:** TT-1 pasó de 15.58 s a 16.48 s. Ahora "ESTA HACE LAS TRES" se sostiene
con producto → **rostro** → cuerpo, en vez de solo el brazo. Eso cierra el pendiente 4 de
la versión anterior de esta nota. También reemplacé el slide 4 del carrusel C1
("ROSTRO, CUERPO Y ZONA ÍNTIMA"), que antes usaba el plano del brazo.

**Salvedad:** ese cartel queda 6.6 s en pantalla sobre tres planos. Es una sola idea
cubriendo un montaje, no un cartel repetido sobre acciones distintas, pero conviene saberlo.

**Nota sobre el navegador:** tu Chrome es en realidad **Brave** (se identifica como
Chrome/150). Para volver a automatizarlo hay que lanzarlo así:

```
/usr/bin/brave-browser --remote-debugging-port=9222 \
  --user-data-dir="$HOME/.config/BraveSoftware/Brave-Browser" --profile-directory=Default
```

## 8 ter · Tres generaciones más (sesión 3)

| Clip | Referencia | Veredicto |
|---|---|---|
| `cajon-720p.mp4` | — (texto a video: el producto no aparece) | **APROBADO**. Arco completo: abre el cajón, primeros planos del enredo de cables con maquinita vieja y descartable amarilla, lo cierra y se va |
| `enjuague-720p.mp4` | `ref-5-packshot.jpg` | **APROBADO**. Rígido los 8 s, verificado en la cola (5.5–8.0 s), que es donde el clip viejo se rompía |
| `mesada-720p.mp4` | `ref-6-mesada-vertical.jpg` | **APROBADO**. Push-in sobre mármol con barrido de luz; producto correcto y rígido |

Los tres a 720×1280, 8 s, 24 fps. Ninguno mostró deformación, silueta cambiada ni marca inventada.

**Lo que arreglaron:**

1. **TT-1 ya no arranca en 360p.** El gancho del cajón pasó de `360x640` (3× de upscale,
   imagen blanda) a `720x1280` (1.5×). Era el último defecto de calidad real del paquete.
   El clip viejo quedó archivado como `cajon_360` en `build.py`, no se borró.
2. **El enjuague pasó de 2.05 s útiles a 8.** El anterior se deformaba a los 2.1 s. Eso
   permitió alargar el cierre de TT-2 de 2.05 s a 3.20 s y darle aire a TT-1.
3. **TT-1 ganó un revelado limpio** con el plano de mesada, en vez de resolverlo con el
   macro de la lámina.

**Color tras integrar:** U entre 117.2 y 120.6, V entre 131.1 y 133.8 en los tres anuncios
— más ajustado que antes (objetivo U=119 / V=134).

**Carruseles actualizados:** C1 usa el cajón nuevo en los slides 1 y 2, la mesada en el 3 y
el enjuague nuevo en el 5. C2 usa el enjuague nuevo en el 5.

## 9 · Pendientes reales

1. **Música o SFX con licencia** — ver punto 6. Es lo único que bloquea publicar.
2. **Resolve Studio o downgrade a 21.0.x** si querés que el MCP monte nativo la próxima vez.
3. ~~TT-1 arranca en 360×640~~ **RESUELTO** — regenerado a 720p (ver 8 ter). Ya no queda
   material de 360p en ningún anuncio.
4. ~~No hay clip válido de rostro~~ **RESUELTO** — generado e integrado (ver 8 bis).
   Sigue sin haber material de zona íntima, y no lo va a haber: no es contenido
   publicable en TikTok ni Instagram. El cartel cubre la afirmación; el video muestra
   rostro y cuerpo.
5. **Te quedan pocos puntos de Flow.** Flow no muestra el costo antes de generar ni el
   saldo en la página, así que no puedo llevarte la cuenta. El saldo está en el avatar
   de arriba a la derecha.
