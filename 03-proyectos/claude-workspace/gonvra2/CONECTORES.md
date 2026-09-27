---
tags: [gonvra, conectores, apis, mcp]
actualizado: 2026-09-21
---

# 🔌 GONVRA — Conectores (APIs y MCP)

> Ordenado por **lo que más rápido trae plata**, no por lo que más lindo suena.
> Todos los links fueron verificados el 21/09/2026.

---

## 🟢 NIVEL 1 — Se hace hoy, sin pedirle permiso a nadie

### 1. Token de Shopify (⏱️ 2 minutos) — **EL MÁS IMPORTANTE**

**Sin esto, cuando entre la primera venta no nos enteramos.** Hoy los agentes pueden leer
el tema y los productos, pero **no los pedidos**.

La app "GONVRA Agentes" ya está creada e instalada. Solo falta generar el token.

👉 **https://admin.shopify.com/store/jm60sa-cp/settings/apps/development**

1. Entrá al link → elegí la app **GONVRA Agentes**
2. Pestaña **Configuración** → **Admin API** → **Configurar**
3. Tildá estos permisos:
   - `read_orders` ← el que falta (pedidos)
   - `read_customers`
   - `read_checkouts` ← carritos abandonados (CAZADOR)
   - `read_products`, `read_inventory`
4. **Guardar** → pestaña **Credenciales de API** → **Instalar app**
5. Copiá el **token de acceso de Admin API** (empieza con `shpat_`)

⚠️ **El token se muestra UNA SOLA VEZ.** Copialo y pegámelo acá, o guardalo.

**Qué se destraba:** CAZADOR ve carritos abandonados · ANALISTA mide ventas de verdad ·
GUARDIA avisa apenas entra un pedido.

---

### 2. Biblioteca de Anuncios de Meta — espiar sin trámite (⏱️ 0 minutos)

La biblioteca de anuncios de Facebook/Instagram es **pública**. No necesita cuenta,
ni token, ni aprobación. Es la mejor fuente de espionaje que tenemos hoy.

👉 **https://www.facebook.com/ads/library/** (país: Argentina · palabra: "afeitadora",
"rasuradora", "recortadora de barba")

**MCP que lo automatiza** (sin token, usa scraping):
- `RamsesAguirre777/facebook-ads-library-mcp` — 256★, MIT, **sin API token ni cuenta**
- `proxy-intell/facebook-ads-library-mcp` — 300★, MIT

### ⚠️ PROBADO EL 21/09 — NO FUNCIONA (todavía)

Instalé el de `RamsesAguirre777` completo (venv + crawl4ai + Chromium 114 MB) y lo
conecté a Hermes. **Conecta bien y expone sus 2 herramientas**, pero al buscar de verdad
**Facebook lo bloquea con 403 anti-bot**.

Probado dos veces: con la espera por defecto (8 s) y con 30 s + 15 scrolls. Mismo
resultado: `success: false`, 0 anuncios.

**Estado:** queda instalado y marcado **PARCIAL** en el panel. No lo borré porque el
bloqueo de Meta puede aflojar y la instalación ya está hecha.

**Mientras tanto, el espionaje se hace a mano** entrando al link de arriba desde el
navegador normal — ahí sí se ven todos los anuncios, porque hay una sesión real.

**Para qué sirve:** ver qué anuncios de la competencia llevan 30+ días corriendo.
Si alguien paga 30 días seguidos por un anuncio, **es porque le da plata**. Copiamos la
estructura, no el texto.

---

## 🟡 NIVEL 2 — Trámite corto (horas o pocos días)

### 3. Gmail / Google Workspace

**Qué destraba:** MENSAJERO contesta consultas y mails de posventa solo.

👉 **https://console.cloud.google.com/** (crear proyecto)
👉 Activar la API: **https://console.cloud.google.com/apis/library/gmail.googleapis.com**
👉 Credenciales OAuth: **https://console.cloud.google.com/apis/credentials**

Pasos: crear proyecto → activar Gmail API → pantalla de consentimiento (tipo **Externo**,
agregarte a vos como usuario de prueba) → crear credencial **ID de cliente OAuth** tipo
**App de escritorio** → descargar el JSON.

**MCP recomendado:** `taylorwilsdon/google_workspace_mcp` — **3.202★**, MIT,
actualizado el 21/09/2026. Cubre Gmail, Calendar, Docs, Sheets y Drive.

⚠️ En modo "prueba" el token vence cada 7 días. Para que dure, hay que publicar la app
(y ahí Google puede pedir verificación).

---

### 4. Google Search Console (⏱️ 15 minutos) — **gratis y subestimado**

**Qué destraba:** ver con qué palabras la gente llega a gonvra.com. Es tráfico **gratis**.

👉 **https://search.google.com/search-console**

Verificás gonvra.com (con el registrador del dominio o un meta tag en el tema) y listo.
Con esto ANALISTA deja de decir "no hay datos".

---

## 🔴 NIVEL 3 — Requieren aprobación de la plataforma (semanas)

### 5. Instagram — publicar automático

⚠️ Requisito previo: la cuenta tiene que ser **Profesional (Empresa)** y estar
**vinculada a una página de Facebook**. Sin eso no hay API posible.

👉 Crear app: **https://developers.facebook.com/apps/**
👉 Documentación: **https://developers.facebook.com/docs/instagram-platform/content-publishing**

Permisos a pedir: `instagram_basic`, `instagram_content_publish`, `pages_show_list`.

**Realidad:** en modo desarrollo funciona **solo con tu propia cuenta** — que es
justamente lo que necesitamos. **No hace falta esperar la revisión de Meta para
publicar en tu propio Instagram.** La revisión recién hace falta si publicás en cuentas
de terceros.

**Límite:** 25 publicaciones por día. De sobra.

---

### 6. TikTok — publicar automático

👉 **https://developers.tiktok.com/**
👉 **https://developers.tiktok.com/doc/content-posting-api-get-started**

⚠️ **El más trabado de todos.** Sin auditoría aprobada, los videos que suba la API
quedan **en borrador privado** — igual hay que entrar a la app y publicarlos a mano.

**Mi consejo:** no gastes tiempo acá todavía. Subir el video a mano son 3 minutos.
Esto recién vale la pena con 3+ videos por día.

**Alternativa:** `taisly/agent` (213★, MIT) — kit para publicar en TikTok, IG y YouTube.

---

### 7. Meta Ads (Marketing API) — solo cuando haya pauta

👉 **https://developers.facebook.com/docs/marketing-apis/**

**MCP:** `pipeboard-co/meta-ads-mcp` — 1.270★, el más usado.

**No lo conectes todavía.** Con cero ventas no hay nada que optimizar, y un agente con
permiso de gastar plata sin datos es la forma más rápida de quemar el presupuesto.
Primero el CPA techo: **$7.129 por venta**.

---

## 📋 Orden que recomiendo

| # | Conector | Tiempo | Trae plata |
|---|---|---|---|
| 1 | **Token de Shopify** | 2 min | 🟢 Directo: detectar ventas y carritos |
| 2 | **Ad Library de Meta** | 0 min | 🟢 Directo: qué le funciona a la competencia |
| 3 | **Search Console** | 15 min | 🟡 Tráfico gratis a mediano plazo |
| 4 | **Instagram publicar** | 1-2 días | 🟡 Ahorra tiempo, no crea ventas |
| 5 | **Gmail** | 1 hora | 🟡 Posventa (todavía no hay clientes) |
| 6 | **TikTok API** | semanas | 🔴 No vale la pena aún |
| 7 | **Meta Ads** | días | 🔴 Recién cuando haya datos |

---

## 🚫 Sobre n8n

**No lo instalé, a propósito.** Fue lo que tumbó el VPS (se comía ~400 MB de RAM).

En la laptop entraría, pero hoy **no orquesta nada que el cron de Hermes no haga ya**:
la grilla de 11 agentes corre sola, con reintentos y avisos. Meter n8n sería una segunda
capa que hace lo mismo, con más cosas que se pueden romper.

**Cuándo sí:** el día que haya webhooks de verdad (pedido entra → mail + WhatsApp +
planilla). Ahí n8n gana. Hoy no.
