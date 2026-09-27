---
name: gonvra-pagos-checkout
description: "GONVRA — el cobro con tarjeta nunca funcionó: la opción 'tarjeta' del checkout es PayPal, que no procesa pesos argentinos"
metadata: 
  node_type: memory
  type: project
  originSessionId: dd4bc7cc-3cf7-45bf-bb64-3afc032fd843
  modified: 2026-08-02T06:51:10.235Z
---

En GONVRA (ver [[gonvra-shopify-store]]) **nunca se cobró una tarjeta**: verificado 2026-08-02, las 10 órdenes de toda la historia de la tienda son "Cash on Delivery".

El checkout ofrece tres proveedores (leídos del HTML real de `/checkout`):
- `Mercado Pago Checkout Pro` → se muestra como **"Mercado Pago"** (OffsiteProvider, declara ARS). Es el correcto para Argentina.
- `paypal` → botón de PayPal.
- `Credit/Debit card by PayPal` → se muestra al cliente como **"Pagos con tarjeta de crédito y débito"**. ⚠️ Parece un cobro con tarjeta común pero **es PayPal**, que no procesa tarjetas argentinas en pesos ⇒ devuelve "Se produjo un error al procesar tu pago".

Acción pendiente del usuario: desactivar PayPal y "Credit/Debit card by PayPal" en `admin.shopify.com/store/gonvra/settings/payments` y probar cobrando por Mercado Pago. Ojo: sacar el logo de PayPal del tema (hecho hace tiempo) **no desactiva la pasarela**.

**No puedo tocar esto yo:** `appInstallations` da "access denied" por el MCP, y la configuración de pagos es del negocio.

**Cómo inspeccionar el checkout sin permisos de admin:** `curl` a `/products/<handle>.js` para sacar un variant id → POST a `/cart/add.js` con cookie jar → GET `/checkout` → buscar `availablePaymentLines` en el HTML (viene con doble escape HTML; hacer `html.unescape` dos veces).

**Dominio sin correo:** `gonvra.com` no tiene registros MX, así que `contacto@gonvra.com` (que la "Auditoría 2026" puso en el botón "Escribinos" de la home) **no recibe nada**. El que funcionaba era `gonvra0@gmail.com`. El usuario dijo el 2026-08-02 que lo dejemos así por ahora.

Link roto detectado: el footer enlaza `/policies/shipping-policy` y da **404** (la política de envíos no está publicada).
