# GONVRA — Resumen unificado de Fase 1

Fecha: 2026-08-20 (ART)
Fuente: informes reales de JEFE, ANALISTA, GUARDIA, TIENDA, TESTER y LEGAL, más verificación pública posterior.
Estado actualizado: políticas de envíos y reembolso **PUBLICADAS / RESUELTAS**. No se gastó dinero ni se activó pauta.

## Estado ejecutivo

GONVRA todavía no debe recibir tráfico pago hasta resolver checkout y medición. Las políticas ya no son bloqueantes de publicación:

1. **Checkout y cobro con tarjeta — PENDIENTE / PRIORIDAD MÁXIMA.** Lo resuelve Matías ahora.
2. **Píxel y medición — PENDIENTE / PRIORIDAD MÁXIMA.** Revisión separada; no borrar a ciegas.
3. **Política de envíos — PUBLICADA / RESUELTA.** La URL responde HTTP 200.
4. **Política de reembolso y garantía — PUBLICADA / RESUELTA.** Dice 10 días y usa `gonvra0@gmail.com`.
5. **Botón de arrepentimiento en el tema — PENDIENTE.** Lo prepara Claude al reconectar Shopify.
6. **Contacto en el tema — PENDIENTE.** Reemplazar `contacto@gonvra.com` por `gonvra0@gmail.com` al reconectar Shopify.

## Promesas operativas aprobadas

- Envío gratis a todo el país: **sí**.
- Seguimiento: **no prometer**; el dropshipping no garantiza tracking universal.
- Pago seguro: **sí, condicionado a desactivar PayPal y dejar solo Mercado Pago como pasarela a validar**.

## 1. Checkout: riesgo de perder el cobro y la venta

**Estado:** PENDIENTE. Lo ejecuta Matías manualmente.

**Evidencia:** el checkout expuso `paypal`, `Mercado Pago Checkout Pro` y `Credit/Debit card by PayPal`. No hubo pago real verificado.

**Plata en riesgo:** escenario de 10 intentos fallidos: aproximadamente **$50.000–$70.000 de CPA** y **$200.000–$320.000 de facturación bruta potencial**. No es pérdida medida.

**Acción:** desactivar PayPal y `Credit/Debit card by PayPal`, mantener Mercado Pago, probar cobro, orden, correo y `Purchase` en ARS. Requiere SEMÁFORO si hay cargo.

## 2. Píxel: riesgo de pagar tráfico sin medición

**Estado:** PENDIENTE.

**Acción:** confirmar dataset correcto y origen de `3919766821491073` y `26889872433954472`; no borrar nada sin Events Manager/Test Events; comprobar PageView, ViewContent, AddToCart y luego Purchase.

## 3. Política de envíos: PUBLICADA / RESUELTA

**Verificación:** `https://gonvra.com/policies/shipping-policy` responde HTTP 200.

**Texto público comprobado:** envío gratis a todo el país; los plazos varían por localidad y correo; el detalle se ve al comprar; no promete seguimiento universal; reclamos por `gonvra0@gmail.com`.

**Responsable:** ya lo publicó Matías. Solo queda verificar el checkout cuando se resuelva el pago.

## 4. Garantía, arrepentimiento y devoluciones: PUBLICADO / RESUELTO, con botón pendiente

**Verificación:** `https://gonvra.com/policies/refund-policy` responde HTTP 200 y publica garantía de 10 días, arrepentimiento de 10 días corridos y `gonvra0@gmail.com`.

**Pendiente separado:** hacer visible el botón de arrepentimiento en el tema. Lo prepara Claude al reconectar Shopify; no requiere reescribir la política publicada.

## 5. Contacto en el tema: PENDIENTE

La política publicada ya usa `gonvra0@gmail.com`, pero la home/tema todavía debe revisarse para cambiar `contacto@gonvra.com`. Lo prepara Claude al reconectar Shopify. No tocar DNS por ahora.

## Responsables restantes

- **Matías:** checkout y cualquier compra de prueba; requiere SEMÁFORO si puede generar cargo.
- **Claude/TIENDA al reconectar Shopify:** botón visible de arrepentimiento y cambio de contacto en una copia del tema.
- **Meta/Shopify con Matías:** revisión y unificación del píxel.

## Bloqueos mantenidos

- Cero gasto y campañas pausadas.
- Cero publicaciones adicionales desde agentes.
- Cero mensajes automáticos.
- Cero cambios en el tema publicado.
- No borrar ni unificar píxeles a ciegas.
