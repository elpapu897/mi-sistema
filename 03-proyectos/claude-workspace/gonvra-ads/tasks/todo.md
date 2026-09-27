# Tareas

## Base

- [x] Auditar composiciones, dimensiones y assets existentes.
- [x] Definir contrato de salida y criterios de éxito.

## Workflow

- [x] Crear exportación automática de carruseles y videos.
  - Aceptación: un comando exporta el lote solicitado en carpetas predecibles.
  - Verificación: `npm run export:carruseles` y `npm run export:videos`.
- [x] Añadir validaciones automáticas de los entregables.
  - Aceptación: se comprueban IDs, cantidad, formato y dimensiones.
  - Verificación: `npm test`.

## Campaña

- [x] Unificar el precio AR$ 36.900 en los cierres.
  - Aceptación: todos los cierres usan la misma constante.
  - Verificación: `npm run check` y revisión visual.
- [x] Exportar los 4 videos y los 3 carruseles completos.
  - Aceptación: 4 MP4 y 15 PNG listos para publicar.
  - Verificación: `npm test` y contacto visual.

## Entrega

- [x] Documentar el uso y los prompts de Google Flow.
- [x] Revisar todo el lote y marcar el workflow completo.
