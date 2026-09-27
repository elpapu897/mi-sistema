# Memoria operativa

## GONVRA — Meta (2026-09-14)

- Píxel `3919766821491073`, porfolio `gonvra1` (`1065947712672679`).
- Cuenta publicitaria `2487859205019090`: activa, ARS, con medio de pago.
- `gonvra1` tiene control total compartido sobre la cuenta; la cuenta no fue movida ni reclamada.
- Meta muestra la cuenta como el único activo conectado al píxel.
- Shopify Facebook & Instagram está reautorizado y el uso compartido está en `Máximo`.
- El píxel recibe eventos Web + Servidor y no tiene errores activos de diagnóstico.
- Embudo observado: `PageView` 401, `ViewContent` 107, `AddToCart` 7, `InitiateCheckout` 15, `AddPaymentInfo` 18, `Purchase` 0.
- Bloqueo de validación: aún no hubo un pedido exitoso; falta verificar el primer `Purchase` real con `value=36900`, `currency=ARS` y deduplicación por ID de pedido.

### Convención UTM Meta

- `utm_source=meta`
- `utm_medium=paid_social`
- `utm_campaign={objetivo}_{audiencia}_{yyyymm}`
- `utm_content={variante_creativa}`
- Sin PII, sin espacios y siempre en minúsculas.

Informe completo: `memory/ad/conversion-signal-qa/2026-09-14-gonvra-meta-pixel.md`.

