---
name: gonvra-meta-ads
description: "Pautar Meta Ads para GONVRA: IDs de cuenta y píxel, límites de presupuesto en ARS, qué se puede crear por API y qué no. Usar ante cualquier pedido de campañas, anuncios, creativos o píxel de Meta/Facebook/Instagram."
---

# GONVRA — Meta Ads

Acceso por el MCP de Meta Ads (`ads_*`). Tienda: ver skill `gonvra-tienda`.

## IDs
| Qué | ID |
|---|---|
| Cuenta de anuncios ("cuenta 1", Gonvra products, ARS) | `1482478863413097` |
| Página FB "Gonvra pets" | `1125904760604828` |
| Píxel/dataset "TIENDA CEPILLO 1" | `26889872433954472` |
| Píxel duplicado que inyecta la app de Shopify | `3919766821491073` |

⚠️ El acceso a las cuentas **fluctúa día a día**: arrancar SIEMPRE con
`ads_get_ad_accounts` y verificar `is_ads_mcp_enabled`. La cuenta
`27009241552077096` está UNSETTLED → **no usar**.

## Límites que ya nos golpearon
- **Presupuesto mínimo diario: ~$1.497 ARS por conjunto** (`min_daily_budget_cents`
  149689). Cualquier plan de "$1.000 para retargeting" es **imposible**.
- **`ads_creative_upload_video` está bloqueado** en esta cuenta ("gradually rolled
  out"), incluso con URL pública. Los videos los sube el usuario a mano en Ads Manager.
- **`ads_creative_upload_image` también**, PERO hay vuelta: `ads_create_creative`
  acepta **`image_url` directo** (URL pública del CDN de Shopify) y crea el creativo
  sin subir nada. Ese es el camino.
- `promoted_object` sin `custom_event_type` da **error 1885014**.
- **Browser bloqueado en facebook.com**: no se puede manejar Ads Manager por
  navegador ⇒ lo que no salga por API se le guía al usuario con capturas.

## Estado del embudo
- El píxel **sí dispara** PageView + ViewContent (también CAPI server-side).
- **No hay AddToCart ni Purchase** (la tienda todavía no vendió) ⇒ **optimizar a
  Compra es inviable**: usar `LANDING_PAGE_VIEWS` hasta que haya conversiones.
- **No hay Instagram vinculado** (`ads_get_ig_accounts` → []) ⇒ los anuncios **no
  se entregan en IG/Reels**. Vincular **@gonvra.pets** es la mejora de mayor impacto.
- Conviene unificar todo en el píxel `26889872433954472` (el otro es duplicado).

## Reglas de negocio
- Producto elegido para pautar: **Cama Redonda Ortopédica $16.990**
  (`gonvra.com/products/cama-redonda-ortopedica-mascotas`).
- **No pautar en frío productos de menos de $16.990** (no dan rentabilidad).
- CPA sano objetivo: **$5.000–$7.000** por venta (ticket ~$20.000–$32.000).
- Escalado: ROAS > 2,5 → subir 20-30%. CTR < 0,8% o 2× CPA sin venta → pausar.
- Nomenclatura de creativos: `P#-D#-FORMATO-ANGULO-v#` (5 buyer personas, 12 dolores).

## Cuidados con el usuario
- **Crear todo en PAUSA** y que él lo prenda. Ya gastó de más una vez por dejar
  algo activo ("pagué tres mil, me gastó cinco mil").
- Confirmar SIEMPRE si el presupuesto es **total o diario**: lo aclara y le importa.
- La cuenta tuvo problemas por estar asociada a **un menor de edad**: si algo no
  se puede vincular, esa suele ser la causa, no un bug.
- Documentos de estrategia en `/home/matiigonzz/Claude/`: `campana-meta-gonvra.md`,
  `gonvra-guia-ejecucion-rapida.md`, `gonvra-brief-para-nuevo-chat.md`.
