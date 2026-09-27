# GONVRA Ads

Workflow local de Remotion para crear videos verticales y carruseles de la rasuradora GONVRA.

## Lo más rápido

```bash
cd /home/matiigonzz/Claude/gonvra-ads
npm run workflow
```

Ese comando genera todo y después verifica los 19 archivos finales.

## Resultado

- Videos: `out/videos/` — 4 MP4 verticales de 1080x1920.
- Carruseles: `out/carruseles/` — 3 carpetas con 5 PNG verticales cada una.
- Los videos salen sin música para poder sumar un audio en tendencia dentro de TikTok o Instagram.
- En cada carrusel, subí las placas en orden: `01.png`, `02.png`, …, `05.png`.

## Vista previa y exportación

```bash
# Abrir el editor visual
npm run studio

# Comprobar código y composiciones
npm run check

# Exportar solamente las imágenes
npm run export:carruseles

# Exportar solamente los videos
npm run export:videos

# Exportar todo
npm run export:all
```

## Qué editar para una campaña nueva

1. Precio y sitio: `src/campaign.ts`.
2. Estructura de los videos: `src/guiones.ts`.
3. Textos y orden de los carruseles: `src/carruseles.ts`.
4. Clips: reemplazalos en `public/clips/` conservando los nombres o actualizá el nombre en `guiones.ts`.
5. Fotos: agregalas a `public/carrusel/` y referencialas desde `carruseles.ts`.

Los componentes visuales (`Anuncio.tsx` y `Carrusel.tsx`) se tocan sólo si querés cambiar el diseño general de todas las piezas.

## Google Flow

Los prompts de imagen y video están en `PROMPTS-GOOGLE-FLOW.md`. El flujo recomendado es:

1. Generar o elegir una imagen limpia del producto.
2. Usarla como referencia en Flow para conservar el mismo modelo negro y verde lima.
3. Generar clips sin texto ni logos.
4. Guardarlos con los nombres de `public/clips/`.
5. Ejecutar `npm run workflow`; Remotion agrega marca, copy, animaciones, precio y CTA.

## Reglas comerciales activas

- Precio comunicado: **AR$ 36.900**.
- Con el costo actual de Zendrop (producto US$ 5,75 + envío US$ 9,69), este precio deja poco margen para anuncios pagos. Priorizá tráfico orgánico hasta conseguir una tarifa menor con Private Agent.
- No se muestran cuotas hasta confirmar que estén activas en Mercado Pago.
- No se promete una fecha exacta de entrega hasta validar el envío con un pedido de prueba.
- No se usan claims médicos, urgencia falsa ni resultados garantizados.
