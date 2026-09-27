# Cómo subir LA DIEZ a internet

## La forma más simple (2 minutos, gratis)

1. Entrá a **https://app.netlify.com/drop** desde la computadora.
2. **Arrastrá la carpeta `ladiez-web` entera** al recuadro de la página.
   Ojo: la carpeta completa, no el archivo suelto. Adentro tiene que estar
   `index.html` y la carpeta `assets` (si falta `assets`, no se ven las fotos).
3. Esperá unos segundos. Te queda una dirección tipo
   `https://algo-raro-12345.netlify.app`.
4. Esa dirección ya funciona en cualquier teléfono, sin instalar nada.

## Ponerle un nombre lindo (sigue siendo gratis)

En Netlify: **Site configuration → Change site name**.
Poné por ejemplo `ladiez` y te queda `https://ladiez.netlify.app`.
Está tomado el nombre? Probá `ladiez-futbol`, `ladiez-potrero`, `jugaladiez`.

## Un dominio propio (esto sí se paga)

Si querés `ladiez.com.ar` o `ladiez.app` hay que comprarlo:

| Dónde | Qué conviene | Precio aproximado por año |
|---|---|---|
| **nic.ar** | `.com.ar` (es el oficial de Argentina) | muy barato, se paga en pesos |
| **Namecheap / Porkbun** | `.com`, `.app`, `.futbol` | 10 a 15 dólares |
| **Netlify** | te lo vende y lo configura solo | 15 a 20 dólares |

Después de comprarlo, en Netlify vas a **Domain management → Add a domain**,
escribís tu dominio y te dice qué dos o tres datos copiar en el panel donde
lo compraste. En una o dos horas ya anda, con candadito (https) incluido.

## Si subís una versión nueva y seguís viendo la vieja

Es la memoria del navegador. Tres opciones:
- Volvé a arrastrar la carpeta a Netlify (reemplaza todo).
- En el celular, recargá manteniendo apretado el botón de recargar.
- O abrí la dirección agregando `?v=2` al final: `https://ladiez.netlify.app/?v=2`.

Igual, el archivo `_headers` que va en esta carpeta ya le dice al navegador
que **el juego nunca se guarde en caché** y que **las fotos sí**, así que esto
no te debería volver a pasar.

## Qué hay en esta carpeta

| Archivo | Para qué |
|---|---|
| `index.html` | el juego entero |
| `assets/menu/` | las 24 fotos del menú y de los correos |
| `netlify.toml` | configuración de Netlify |
| `_headers` | reglas de caché |

## La otra opción: un solo archivo

En la carpeta de arriba está **`ladiez-un-archivo.html`**: es el mismo juego
pero con las fotos adentro del propio archivo. Pesa más (unos 7 MB) pero
**no depende de nada**: lo podés mandar por WhatsApp, guardarlo en el
teléfono, abrirlo sin internet o subirlo suelto a cualquier lado y siempre
se va a ver completo.
