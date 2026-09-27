# GONVRA — diagnóstico de señales de conversión de Meta

Fecha: 2026-09-14  
Tienda: `gonvra.com` / `jm60sa-cp.myshopify.com`  
Plataforma: Meta  
Conversión principal: `Purchase`  

Este informe verifica y corrige la infraestructura de medición. No puntúa los vetos R1/R2 ni evalúa rentabilidad publicitaria.

## Estado final

- Píxel: `3919766821491073`, propiedad del porfolio `gonvra1` (`1065947712672679`).
- Cuenta publicitaria: `2487859205019090`, activa, en ARS y con medio de pago.
- `gonvra1` recibió control total y reversible sobre la cuenta publicitaria mediante acceso compartido; la solicitud fue aprobada automáticamente. La cuenta no fue trasladada ni reclamada.
- La cuenta publicitaria quedó asignada al píxel. Meta confirmó: “1 activo está conectado a este píxel” y listó `2487859205019090`.
- La app Facebook & Instagram de Shopify quedó reautorizada.
- Uso compartido de datos cambiado de `Mejorado` a `Máximo` y guardado.
- Integración del píxel en Shopify: app pixel, Web + Servidor; no está insertado en el tema.
- Diagnóstico de Meta: sin errores activos. Un aviso previo sobre dominios ya no estaba activo.
- No se borró, desactivó ni desconectó ningún activo.

## Evidencia del embudo

Ventana revisada en Meta: 2026-09-06 a 2026-09-12, zona horaria de Buenos Aires.

| Evento | Eventos observados | Estado |
|---|---:|---|
| `PageView` | 401 | Recibido |
| `ViewContent` | 107 | Recibido |
| `AddToCart` | 7 | Recibido |
| `InitiateCheckout` | 15 | Recibido |
| `AddPaymentInfo` | 18 | Recibido |
| `Purchase` | 0 | No observado |

Shopify tenía 0 pedidos completados al revisar. Por lo tanto, la ausencia de `Purchase` era coherente: no existía un pedido exitoso que Shopify pudiera enviar a Meta. El checkout abandonado del 2026-09-08 no era la compra de ARS 36.900 y no debe usarse como prueba de `Purchase`.

Parámetros observados en eventos de embudo:

- `ViewContent`, `AddToCart` e `InitiateCheckout`: `value`, `num_items`, `currency`, `content_ids`, `content_type`.
- `AddPaymentInfo`: `value`, `currency`.
- `PageView`: sin parámetros comerciales detectados, esperado para una vista genérica.

Calidad de coincidencia observada antes del cambio:

- `PageView` y `ViewContent`: 4,4/10.
- `AddToCart`, `InitiateCheckout`, `AddPaymentInfo`: 0,0/10.
- La configuración `Máximo` permite que Shopify use el píxel, coincidencias avanzadas y Conversion API, enviando identificadores disponibles conforme a consentimiento y privacidad. La puntuación no se actualiza de inmediato: necesita eventos nuevos con usuarios identificables y procesamiento posterior de Meta.

## Pre-flight

| Control | Estado | Evidencia / próximo paso |
|---|---|---|
| Compra de prueba registrada | Necesita dato | Falta completar una compra real que cree un pedido pagado y comprobar `Purchase` en Meta. |
| Un evento canónico por compra | Necesita dato | Shopify está configurado para el evento estándar `Purchase`, pero todavía no hubo una compra exitosa para validarlo de punta a punta. |
| Valor y moneda del `Purchase` | Necesita dato | Objetivo esperado: `value=36900`, `currency=ARS`; falta observarlo en un evento real. |
| ID estable de deduplicación | Necesita dato | Confirmar `event_id`/ID de pedido en la primera compra exitosa recibida por navegador y servidor. |
| Enlaces pagos etiquetados | Necesita dato | Aún no hay campañas ni exportación de adquisición para auditar. |
| Convención UTM consistente | Listo para usar | Especificación definida debajo; falta aplicarla al crear campañas. |
| Autoetiquetado y UTMs sin colisión | Necesita dato | Revisar cuando exista la primera campaña. |
| Sin PII en UTMs | Listo para usar | La especificación prohíbe nombres, correos, teléfonos e IDs de pedido. |
| Fuente única de verdad | Aprobado | Los pedidos e IDs de Shopify serán la verdad, no el conteo autorreportado de Meta. |
| Método de deduplicación definido | Aprobado | Reconciliar el ID de pedido de Shopify con el `event_id` recibido por Meta. |
| Solapamiento entre plataformas | Necesita dato | No hay campañas de Google ni Meta para comparar todavía. |
| Ventana de atribución | Necesita dato | Elegir y documentar la ventana al crear la primera campaña; no comparar ventanas distintas como si fueran equivalentes. |
| Moneda y zona horaria | Aprobado | ARS y `America/Argentina/Buenos_Aires`. |
| Conversiones offline | Bandera | No se informaron ventas offline; revisar sólo si se incorporan ventas por fuera de Shopify. |
| Modelado iOS/ATT | Bandera | Esperar conversiones modeladas o parciales; no tratarlas automáticamente como error. |

## Especificación UTM

Todos los valores deben ir en minúsculas, sin espacios y sin información personal.

| Campo | Regla para GONVRA | Ejemplo |
|---|---|---|
| `utm_source` | Plataforma fija | `meta` |
| `utm_medium` | Canal pago fijo | `paid_social` |
| `utm_campaign` | `{objetivo}_{audiencia}_{yyyymm}` | `purchase_prospecting_202609` |
| `utm_content` | Variante creativa | `video_a` |
| `utm_term` | Omitir en Meta; reservar para búsqueda | — |

Ejemplo:

`https://gonvra.com/?utm_source=meta&utm_medium=paid_social&utm_campaign=purchase_prospecting_202609&utm_content=video_a`

No incluir nombres, correos, teléfonos ni IDs de pedido en parámetros UTM. No variar `meta`/`paid_social` con mayúsculas o sinónimos.

## Especificación del evento de compra

| Acción | Evento Meta | Valor | Moneda | ID de deduplicación | Se dispara cuando |
|---|---|---|---|---|---|
| Compra | `Purchase` | Total final del pedido; prueba objetivo `36900` | `ARS` | `event_id` estable basado en el ID de pedido Shopify | Shopify completa el checkout, crea el pedido y muestra la confirmación; el servidor replica el evento por Conversion API |

## Veredicto

La cuenta está técnicamente lista para crear y publicar campañas: cuenta activa, medio de pago, píxel recibiendo eventos, cuenta asignada y uso compartido en `Máximo`.

La validación integral de medición queda pendiente hasta que una compra exitosa cree un pedido pagado y Meta reciba `Purchase` con `value=36900`, `currency=ARS` y un ID estable de deduplicación. Para escalar inversión, completar primero esa prueba y documentar la ventana de atribución de la campaña.

## Handoff

- Resultado: conexión cuenta–píxel y uso compartido máximo completados.
- Evidencia clave: Meta muestra un activo conectado (`2487859205019090`) y Shopify muestra `Máximo` para el píxel `3919766821491073`.
- Riesgo abierto: todavía no existe una compra exitosa con la cual validar `Purchase`.
- Próxima acción: hacer una compra real, verificar el pedido pagado y luego validar el evento en Meta.

