# Spec: workflow de anuncios GONVRA

## Objetivo

Tener un sistema local y reutilizable para producir creativos de la rasuradora GONVRA sin depender de una sesión de IA. El sistema debe convertir una configuración de campaña en:

- videos verticales MP4 listos para TikTok/Reels;
- carruseles verticales PNG, una carpeta ordenada por publicación;
- una vista previa editable en Remotion Studio;
- prompts de Google Flow para regenerar el material base cuando haga falta.

La primera campaña corresponde a la **Face & Body Electric Shaver**, enfocada en Argentina y con precio de comunicación de **AR$ 36.900**.

## Stack técnico

- Remotion 4.0.521
- React 19
- TypeScript 5.7
- Node.js y sus módulos nativos para el workflow de exportación y las pruebas

## Comandos

```bash
npm run studio
npm run check
npm run export:carruseles
npm run export:videos
npm run export:all
npm test
```

## Estructura

```text
src/                    composiciones y contenido editable
public/clips/           clips verticales de Google Flow
public/carrusel/        imágenes fuente de los carruseles
scripts/                exportador del workflow
tests/                  validaciones automáticas
out/videos/             MP4 finales
out/carruseles/<id>/    PNG finales numerados
tasks/                  plan y estado del trabajo
```

## Estilo de código

Las campañas se describen como datos tipados y los componentes sólo se ocupan de presentarlos:

```ts
{
  id: 'Carrusel-Problema',
  formato: 'tiktok',
  slides: [
    {tipo: 'portada', titulo: '¿Un aparato para cada parte?', imagen: 'carrusel/kit.jpg'},
  ],
}
```

- Identificadores estables en PascalCase con guiones.
- Copy en español rioplatense y sin promesas médicas.
- Una idea principal por slide.
- El precio se define una sola vez y se reutiliza en todos los cierres.

## Estrategia de prueba

- `npm run check`: typecheck y descubrimiento real de composiciones.
- `npm test`: comprueba cantidad, nombres, dimensiones y formato de todos los entregables exportados.
- Revisión visual: contacto de cada carrusel y fotogramas clave de los videos.

## Límites

- Siempre: mantener 1080x1920, respetar zonas seguras, renderizar antes de declarar listo y conservar los assets originales.
- Consultar antes: cambiar producto, marca, precio o claims comerciales.
- Nunca: inventar descuentos, reseñas, escasez, resultados médicos o plazos de entrega.

## Criterios de éxito

- Existen 4 videos MP4 de 1080x1920.
- Existen 3 carruseles, cada uno con 5 PNG de 1080x1920 numerados en orden.
- Un solo comando puede regenerar cada lote o todo el contenido.
- TypeScript compila y las pruebas verifican los 19 archivos finales.
- README y prompts explican cómo cambiar textos, imágenes, clips y volver a exportar.

## Preguntas abiertas

- Las cuotas no se comunican hasta confirmar que están activadas en Mercado Pago.
- Los tiempos de entrega no se precisan hasta completar un pedido de prueba a Argentina.

