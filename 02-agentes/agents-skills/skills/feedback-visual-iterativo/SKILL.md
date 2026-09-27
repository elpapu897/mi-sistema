---
name: feedback-visual-iterativo
description: "Manejar pedidos de cambios visuales descritos por voz y sin vocabulario técnico ('más gordo', 'esa partecita de la derecha'). Usar al ajustar UI, temas, logos, iconos, CSS o imágenes cuando el feedback llega en lenguaje coloquial."
---

# Feedback visual iterativo (usuario no técnico)

El usuario describe cambios visuales **hablando y señalando**, sin nombres de
elementos. Es su modo normal de trabajo: iteraciones cortas, muchas seguidas.

## Traducir su vocabulario

| Dice | Quiere decir |
|---|---|
| "más gordo" | mayor peso/grosor de trazo, o más tamaño |
| "no tan redondeado" | menos `border-radius` |
| "esa partecita de la derecha" | pedile una captura o describí candidatos y confirmá |
| "que se parezca a macOS" | referencia estética concreta: revisar su tema WhiteSur-Dark |
| "trucho" | el asset se ve falso/mal hecho — casi siempre un SVG mal transcripto |
| "es lo mismo literalmente" | tu cambio **no se aplicó** o no se ve: verificá antes de discutir |

## Reglas duras

1. **Verificá visualmente antes de decir "listo".** Si dice "es igual", casi
   siempre tiene razón: el cambio no se renderizó (caché, tema equivocado,
   selector pisado). Sacá una captura y miralá vos.
2. **Logos de marcas: bajar el oficial, nunca dibujarlo.** Ya pasó con Mercado
   Pago: trazados re-transcriptos a mano = "borrón". Bajar de Wikimedia Commons
   y recortar por bbox. Respetar el color real (Mercado Pago es **amarillo**,
   no azul — se equivocó una vez y lo recuerda).
3. **Un cambio de texto o color hay que buscarlo en TODOS lados**, incluida la
   home y los defaults del schema. Se frustra mucho si queda un lugar viejo.
4. **Vale lo último que dijo.** Se autocorrige en la misma frase ("azul, perdón,
   gris"). Ver skill `dictado-rioplatense`.
5. **No pidas que aclare dos veces.** Elegí la interpretación más probable,
   anunciála en una línea y ejecutá.

## Verificación visual sin navegador interactivo
Cuando el panel del browser no está a la vista, `computer screenshot` falla.
Alternativa que funciona:

```
python3 -m http.server        # en el scratchpad
brave-browser --headless --screenshot=out.png --virtual-time-budget=8000 http://localhost:PORT
```
Después **leer el PNG**. Para ver una sección tal como la sirve Shopify:
`curl "https://gonvra.com/?preview_theme_id=<id>"`, extraer el `<style>` + el
`<section id="shopify-section-...">` y montarlo con el `gv-styles.css` del CDN.
⚠️ Apuntar el headless directo a gonvra.com **se cuelga**.
