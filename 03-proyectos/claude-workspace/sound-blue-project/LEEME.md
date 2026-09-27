# Sound Blue Project — página de presentación

Página interactiva para presentar el proyecto en la feria.
Funciona **sin internet** y también se puede publicar online para compartir por QR.

---

## Novedades de esta versión

- **Tema oscuro**, con la iluminación del semáforo (los halos verde/amarillo/rojo).
- **Modelo 3D cargado**: `assets/modelo.stl`, el export de Tinkercad. Gira solo, y se puede
  arrastrar y hacer zoom con el dedo o el mouse.
- **Modo calma** ahora se nota de verdad: apaga los halos del semáforo, el brillo de los
  LED, baja el contraste general y esconde el simulador de sobrecarga.
- El modelo 3D **no se descarga hasta que hace falta** (pesa 1,5 MB): baja cuando te acercás
  a la sección 06, o a los 12 segundos con la página ya ociosa. Si el visitante tiene el
  ahorro de datos activado, sólo se descarga si llega a esa sección.

### Sobre el STL
El export traía **120 triángulos sueltos a 800 mm** del objeto (restos del plano de trabajo
de Tinkercad, lo mismo que aparecía en el SVG). Si no se filtraran, los auriculares se verían
microscópicos. El visor los descarta solo, con dos resguardos: sólo si son menos del 5 % del
modelo y sólo si al sacarlos el encuadre se reduce a menos de la mitad. Podés volver a
exportar sin miedo: se sigue viendo bien.

---

## 1. Abrirla el día de la feria

```bash
./servir.sh
```

Se abre el navegador solo en `http://localhost:8000`.

> **Abrila siempre así**, no con doble clic en `index.html`. Los navegadores bloquean el
> micrófono cuando el archivo se abre suelto (`file://`), y el semáforo en vivo es la demo
> más fuerte. Con `servir.sh` el micrófono anda y **no hace falta internet**.
> Si igual la abrís suelta, todo funciona menos el micrófono: la página avisa y ofrece el
> **modo demo** con una barra deslizante.

---

## 2. Modo presentación (la novedad)

Botón **«Presentar»** arriba a la derecha, o **«Activar la guía paso a paso»** en la sección 01.

Aparece una barra abajo con las **8 paradas del recorrido**. Cada una dice qué mostrar y
qué contar, y al pasar de paso la página **baja sola** a la sección correspondiente.

- Se avanza con los botones o con las flechas <kbd>←</kbd> <kbd>→</kbd> del teclado.
- Se sale con «Salir» o con <kbd>Esc</kbd>.
- El recorrido completo son ~11 minutos. Si el visitante tiene apuro: paradas **2 y 7**.

Los textos del guion están en `index.html`, en la constante `PASOS` (arriba del `<script>`).
Cambialos con confianza: son sólo texto.

---

## 3. Qué tiene cada sección

| # | Sección | Qué se puede hacer |
|---|---|---|
| 01 | Recorrido | La guía para presentar, con tiempos |
| 02 | El problema | Datos de referencia de la OMS |
| 03 | Semáforo | 🎙 **Micrófono en vivo**: reproduce los umbrales reales de la micro:bit (115 / 150 / 175), muestra la matriz de LEDs y suena el tono de 294 Hz en rojo. Hay **modo demo** si no hay micrófono |
| 04 | Código | Las nueve líneas, con botón para copiarlas y el tono de ejemplo |
| 05 | El Oso Milo | Lector página por página (flechas, deslizar, clic para ampliar) + Calaméo |
| 06 | Auriculares 3D | Visor 3D que gira (ver arriba) |
| 07 | Merceditas | Escala de decibeles + galería del trabajo de campo |
| 08 | River | El palco sensorial del Monumental |
| 09 | Campaña | Las 3 fases de #EscuchámosNos |
| 10 | Equipo | La escuela, el enfoque y las fotos |
| + | Experiencia | Simulación de sobrecarga sensorial de 20 s. Sin destellos rápidos, se sale con <kbd>Esc</kbd> |

### Modo calma 🟢
Al lado de «Presentar». Apaga movimiento, sonidos y el simulador. Pensado para que
cualquier persona con hipersensibilidad pueda recorrer la página tranquila — y además es un
buen argumento ante el jurado: **la página aplica lo que el proyecto predica.**

---

## 4. Optimización para celular

La mayoría de la gente va a entrar desde el teléfono, así que:

- Todas las fotos tienen versión **WebP** (pesa ~20 % menos) con respaldo JPG automático.
- Tres tamaños por imagen: miniatura (520 px), media (960 px) y completa (1600 px).
  El celular baja la chica; la grande sólo se descarga al ampliar.
- Las galerías cargan en diferido: sólo se baja lo que se ve.
- Botones de 48 px mínimo, epígrafes siempre visibles en celular, una sola columna.
- El modelo 3D se descarga sólo cuando hace falta (ver arriba).
- Primera carga aproximada en celular: **~680 KB**.

---

## 5. Publicar y generar el QR

```bash
./publicar.sh
```

Te deja el ZIP listo y explica dos caminos: **Netlify Drop** (arrastrar y listo) o
**GitHub Pages**. Con la dirección ya en mano:

```bash
python3 hacer-qr.py https://la-direccion-de-tu-pagina/
```

Genera `qr-sound-blue.png` a 300 dpi, con el logo en el centro, listo para imprimir.

---

## 6. Cargar las mediciones propias del jardín

Los decibeles que se muestran son **valores de referencia de la OMS**, no mediciones propias,
y así está aclarado en la página. Cuando tengas los datos reales, buscá `MEDICIONES_PROPIAS`
en `index.html` y completá:

```js
const MEDICIONES_PROPIAS = [
  {et:"Sala Amarilla · 10:30", db:78},
  {et:"Patio · recreo",        db:84},
];
```

Aparecen solas en el gráfico, en azul para distinguirlas de las referencias.

---

## 7. Archivos

```
index.html         la página entera (HTML + CSS + JS, sin dependencias)
assets/img/        fotos en 3 tamaños × 2 formatos + logo + favicon + imagen para redes
assets/modelo.stl  ← acá va el modelo 3D exportado de Tinkercad
servir.sh          abre la página localmente (con micrófono)
publicar.sh        prepara el ZIP y el repo para subirla
hacer-qr.py        genera el QR una vez publicada
```

---

## 8. Datos y enlaces

- **Escuela:** EEM N.° 5 D.E. 15 «Monseñor Enrique Angelelli» — Saavedra, CABA
- **Jardín:** JII N.° 2 D.E. 10 «Merceditas»
- **MakeCode:** https://makecode.microbit.org/S79337-86713-05223-83164
- **Cuento en Calaméo:** https://www.calameo.com/read/004454581afafc5dc460e
- **Redes:** @sound_blue_project
- **Hashtags:** #EscuchámosNos · #SoundBlueProject · #SaavedraInclusiva · #ConvivenciaAcústica
