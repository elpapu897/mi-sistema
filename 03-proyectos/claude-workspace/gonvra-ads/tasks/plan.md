# Plan de implementación: workflow de anuncios GONVRA

## Resumen

Completar el proyecto Remotion parcial encontrado en la sesión de Claude, convertirlo en un workflow de un comando y dejar exportados y verificados los videos y carruseles de la primera campaña.

## Decisiones

- Reutilizar el proyecto y sus assets reales; no duplicar la implementación.
- Usar Remotion tanto para MP4 como para PNG, así textos y marca quedan editables.
- Bundlear una vez por ejecución para que el lote sea reproducible y más rápido.
- Mantener videos sin música para poder elegir un audio en tendencia al publicarlos.

## Orden de trabajo

1. Validar las composiciones y los assets existentes.
2. Añadir el exportador y las pruebas del contrato de salida.
3. Unificar precio y cierre de campaña.
4. Exportar y revisar visualmente el lote completo.
5. Documentar el uso y los prompts de Google Flow.

## Riesgos y mitigaciones

| Riesgo | Impacto | Mitigación |
|---|---|---|
| Copy tapado por la interfaz de TikTok | Alto | Zonas seguras incorporadas y revisión visual |
| Precio distinto del sitio | Alto | Constante única y aviso de sincronización |
| Claims no comprobables | Alto | Copy conservador y sin promesas médicas |
| Render lento o incompleto | Medio | Bundle único, progreso visible y pruebas de archivos |

## Preguntas abiertas

- Confirmar cuotas de Mercado Pago antes de agregarlas al copy.
- Confirmar tiempo real de entrega con el pedido de prueba.

