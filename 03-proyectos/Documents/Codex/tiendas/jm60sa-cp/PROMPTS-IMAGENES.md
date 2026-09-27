# Prompts de imágenes para Helio Mini — encargo para Codex

> Documento preparado por Claude tras auditar el tema en vivo (`jm60sa-cp.myshopify.com`,
> tema **Helio - Nuevo diseño #147833946227**) y las 6 fotos del proveedor en `fotos-producto/`.
> Codex: leé la sección "Reglas" entera antes de generar nada.

---

## 0. Por qué hay que rehacer las fotos

Las 12 imágenes actuales están muy bien resueltas de luz, encuadre y coherencia de serie.
Tienen **un fallo grave y repetido**: en todas, **la pantalla circular frontal está apagada**
(un disco negro liso). Esa pantalla es *la* característica que diferencia al producto —en las
6 fotos del proveedor aparece siempre encendida mostrando el porcentaje de batería— y es sobre
la que ahora se apoya media web: el hero, la ficha técnica, el carrusel, las FAQ y la sección
de beneficios hablan de "la pantalla que te dice cuánta carga te queda".

Con el disco negro, el argumento principal de la página no se ve en ninguna foto.

**Objetivo del encargo:** regenerar la serie con la pantalla encendida y añadir las piezas que
faltan para las secciones nuevas.

---

## 1. Reglas que aplican a TODAS las imágenes

**Fidelidad al producto (lo más importante)**

- Geometría exacta de las referencias `fotos-producto/producto-1..6.jpg`: cuerpo rectangular
  compacto de esquinas achaflanadas, módulo superior negro con dos aletas horizontales, **dos
  cabezales circulares plateados** lado a lado, pantalla circular grande en el frente, botón
  de encendido en el lateral derecho, tornillos hexagonales decorativos, rejillas diagonales
  grabadas y estética "mecha" / cyberpunk industrial.
- **La pantalla SIEMPRE encendida**: disco de cristal negro brillante con dígitos LED blancos
  de matriz de puntos mostrando un número de dos o tres cifras (por ejemplo `86`, `100`), con
  un pequeño símbolo de rayo o candado al lado y un arco de progreso fino en el borde inferior
  izquierdo, tal como se ve en `producto-4.jpg`, `producto-5.jpg` y `producto-6.jpg`.
  El brillo del LED debe derramar un halo tenue frío sobre el metal de alrededor.
- Nada de piezas inventadas, despieces flotantes, mecanismos internos ni engranajes.

**Texto**

- **Cero texto de marketing, títulos, precios, flechas, etiquetas, marcas de agua o logos.**
  Todo el copy va en la web, nunca quemado en la imagen.
- *Excepción:* los dígitos del LED de la pantalla y los micro-grabados propios de la carcasa
  (los chevrones `>>>` y el hexágono con el "1") son parte física del producto y sí van.

**Coherencia de serie**

- Las imágenes deben parecer de **una única sesión fotográfica**: misma temperatura de color,
  misma dirección de luz principal, mismo acabado del metal, mismas proporciones del producto.
- Paleta del sitio, respetala: grafito `#080A0F`, azul noche `#111827`, plata fría `#CBD5E1`,
  azul eléctrico `#36C5FF`, verde energía `#65F29A`, blanco hielo `#F7FAFC`.

**Composición**

- El producto **nunca cortado** por arriba ni por abajo, salvo en la macro (nº 4).
- Dejar **aire alrededor** y, donde se indique, espacio negativo libre para que la web escriba
  encima. El producto no debe ocupar toda la superficie.
- Nada de reflejos exagerados ni brillos que tapen los dígitos de la pantalla.

**Entrega**

- Generar en PNG a la resolución máxima disponible, archivar el original en `work/image-sources/`.
- Exportar la versión optimizada en **WebP** a `assets/` **con el nombre exacto** que indica cada
  ficha. Si respetás los nombres, el tema las toma sola y no hay que tocar ningún ajuste.
- Después de exportar, mirá cada imagen y verificá: ¿pantalla encendida?, ¿dos cabezales enteros?,
  ¿sin texto?, ¿mismo acabado que el resto de la serie?

---

## 2. Imágenes a REGENERAR (prioridad alta)

### 2.1 `mt-catalogo-plata-frontal.webp` — 1:1

> Fotografía publicitaria de producto, formato cuadrado. Afeitadora eléctrica mini plateada
> idéntica a las referencias, vista frontal en tres cuartos, ligeramente elevada. **La pantalla
> circular frontal está encendida**: cristal negro con dígitos LED blancos de matriz de puntos
> marcando `86`, un pequeño icono de rayo a su derecha y un arco de progreso fino en el borde;
> el LED derrama un halo azulado suave sobre el metal contiguo. Cuerpo completo de aleación con
> acabado cepillado, los dos cabezales enteros y nítidos. Fondo de estudio continuo gris hielo
> con caída suave a grafito. Luz principal cenital difusa más un contraluz frío que dibuja el
> canto del cuerpo. Producto centrado con margen generoso. Sin texto, sin marcas, sin agua,
> sin piezas flotantes.

### 2.2 `mt-catalogo-plata-lateral.webp` — 1:1

> Misma sesión, misma afeitadora plateada, girada unos 55° para mostrar el grosor real del
> cuerpo, la pared lateral con las rejillas diagonales y el botón de encendido. La pantalla
> encendida queda **parcialmente visible en escorzo**, con los dígitos LED todavía legibles y
> su halo derramándose sobre el borde metálico. Los dos cabezales completos y bien separados.
> Mismo fondo, misma luz, mismo acabado y mismas restricciones que la frontal.

### 2.3 `mt-catalogo-verde.webp` — 1:1

> Misma geometría, set, luz y tratamiento que las dos plateadas. Cambia **únicamente** el color
> del cuerpo a **verde menta pálido y desaturado**, fiel al tono de `producto-6.jpg`; el módulo
> superior sigue siendo negro y los cabezales plateados. Vista en tres cuartos complementaria
> a la frontal. Pantalla encendida marcando `100`. Producto entero, sin cortes.

### 2.4 `mt-macro-cabezales.webp` — 1:1

> Macro oblicua desde arriba de los **dos cabezales circulares completos**, montados
> normalmente en su carcasa negra. Detalle de los anillos concéntricos, las ranuras finas de
> la lámina de corte y el metal pulido; profundidad de campo corta con el segundo cabezal algo
> desenfocado. Es el único plano donde el cuerpo puede recortarse. **Sin despieces, sin piezas
> levitando, sin mecanismos internos inventados.** Mismo fondo y misma luz de campaña.

---

## 3. Imágenes NUEVAS para las secciones que acabo de añadir

### 3.1 `mt-ficha-tecnica.webp` — 1:1 · **la más importante de todas**

Va en la sección "Cada detalle, a la vista", donde la web dibuja **puntos numerados
interactivos** encima de la foto en estas coordenadas (porcentaje del ancho / alto):

| Punto | Qué señala | x | y |
|---|---|---|---|
| 1 | cabezal izquierdo | 40 % | 13 % |
| 2 | cabezal derecho | 63 % | 15 % |
| 3 | pantalla LED | 52 % | 62 % |
| 4 | cuerpo de aleación | 29 % | 46 % |

> Fotografía cuadrada del producto plateado **de frente, casi sin perspectiva**, perfectamente
> centrado y ocupando alrededor del 70 % del alto del encuadre, de modo que los cuatro puntos
> de la tabla caigan exactamente sobre el cabezal izquierdo, el cabezal derecho, la pantalla y
> la pared metálica izquierda del cuerpo. **Fondo oscuro** (grafito `#080A0F` con un degradado
> radial azulado muy tenue arriba), porque la sección de la web es oscura y hoy la foto entra
> como un rectángulo blanco que rompe el bloque. Iluminación de perfilado frío que separa el
> producto del fondo. Pantalla encendida marcando `100` con su halo. Superficie de apoyo apenas
> insinuada, sin reflejo que compita. Nada de texto ni de líneas indicadoras: los números los
> pone la web encima.

### 3.2 `mt-agua.webp` — 4:5

Hoy no hay ninguna foto que respalde el argumento "cabezales lavables", que sí sale en la
ficha, en las FAQ y en la sección de viaje.

> Un cabezal circular plateado desmontado, sostenido bajo un chorro fino de agua corriente en
> un lavabo de piedra oscura, con gotas nítidas congeladas y salpicaduras finas. El cuerpo de
> la afeitadora aparece desenfocado al fondo, apoyado y con su pantalla encendida brillando a
> través del bokeh. Luz lateral fría, ambiente de baño moderno oscuro. Formato vertical, con
> aire en la mitad superior para que la web pueda escribir encima. Sin texto.

### 3.3 `mt-nosotros.webp` — 4:5

Va en la sección "Elegimos pocos productos. Y los elegimos bien.", con un recuadro de cristal
sobre el tercio inferior.

> Bodegón editorial cálido y sobrio: la afeitadora plateada apoyada sobre una mesa de madera
> oscura junto a un cuaderno cerrado, una taza de café y unas gafas, en un taller o estudio con
> luz de ventana lateral suave al atardecer. Ambiente de "equipo chico que prueba productos",
> no de publicidad agresiva. El producto **no** es el protagonista absoluto: ocupa un tercio del
> encuadre, a la izquierda, con su pantalla encendida como único punto de luz frío. Profundidad
> de campo corta. **Dejar el tercio inferior visualmente tranquilo** (mesa, sombra) porque ahí
> se apoya un recuadro con texto. Sin texto ni logos.

### 3.4 `mt-video-poster.webp` — 16:9

Portada del bloque "Así se usa, en menos de un minuto" mientras no haya video real.

> Plano cinematográfico apaisado de un baño moderno oscuro con iluminación azul y verde tenue
> de fondo. Un hombre de unos 30 años, de perfil parcial y ligeramente desenfocado a la derecha,
> se pasa la afeitadora por la mandíbula. La afeitadora está nítida y su pantalla encendida es
> el punto de luz más brillante del cuadro. **La mitad izquierda queda deliberadamente vacía y
> oscura** para el botón de reproducción y el rótulo de la web. Grano fino, aspecto de fotograma
> de video, no de foto de catálogo. Sin texto.
>
> Ojo: en celular este bloque se recorta a 4:5 tomando el centro. Colocá al hombre y la
> afeitadora suficientemente hacia el centro para que el recorte vertical siga funcionando.

### 3.5 Carrusel "Arrastrá para recorrerla" — 5 tomas en 4:5

Todas verticales, mismo set, **con el tercio inferior tranquilo** (ahí va un panel de cristal
con el título de cada toma). El producto arriba o centrado, nunca pegado al borde inferior.

| Archivo | Contenido |
|---|---|
| `mt-toma-pantalla.webp` | Plano cerrado y frontal de la **pantalla encendida** marcando `100`, con el arco de progreso y el icono de rayo bien legibles; el resto del cuerpo cae en penumbra. Fondo grafito. |
| `mt-toma-cabezales.webp` | Los dos cabezales vistos desde arriba en ángulo bajo, recortados contra un fondo oscuro, con un destello frío recorriendo el filo de las láminas. |
| `mt-toma-verde.webp` | La versión **verde menta** completa, en tres cuartos, sobre fondo oscuro con una luz de acento verde muy sutil detrás. Pantalla encendida. |
| `mt-toma-perfil.webp` | Vista lateral estricta que muestre lo delgado que es el cuerpo, apoyado de canto sobre una superficie oscura reflectante. |
| `mt-toma-viaje.webp` | La afeitadora dentro de un neceser de cuero abierto, junto a un pasaporte y un cable USB enrollado, sobre la cama de una habitación de hotel con luz cálida de noche. |

---

## 4. Checklist final antes de dar el trabajo por cerrado

- [ ] Las 4 imágenes de catálogo tienen **la pantalla encendida** (era el fallo original).
- [ ] `mt-ficha-tecnica.webp` tiene **fondo oscuro** y el producto centrado en las coordenadas
      de la tabla del punto 3.1.
- [ ] Ninguna imagen lleva texto, logos, precios ni marcas de agua.
- [ ] Las 12+ imágenes parecen de la misma sesión.
- [ ] Los verticales (4:5) tienen el tercio inferior despejado para el panel de texto.
- [ ] `mt-video-poster.webp` funciona también recortado a 4:5 por el centro.
- [ ] Todo exportado a `assets/` en WebP con los nombres exactos.
- [ ] Subido con `shopify theme push --theme 147833946227 --allow-live --only "assets/mt-*.webp"`.

## 5. Aviso: orden de subida

Si además tocás secciones o plantillas, subí **primero** `sections/` y `snippets/`, y **después**
`templates/*.json`. Shopify rechaza en silencio una plantilla JSON que mencione un tipo de
sección que todavía no existe en el tema — pasó en esta sesión y las secciones nuevas no se
veían pese a que el push decía "completo".

Y en los `{% schema %}`: en un `range`, `(max - min)` debe ser **divisible exacto** por `step`,
o Shopify rechaza el archivo entero con "Invalid schema".
