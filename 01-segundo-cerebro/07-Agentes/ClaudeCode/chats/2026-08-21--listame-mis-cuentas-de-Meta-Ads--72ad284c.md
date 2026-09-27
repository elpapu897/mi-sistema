---
tool: ClaudeCode
session_id: 72ad284c-68dc-4fa4-954d-62fca2c3fed5
fecha: 2026-08-21 03:23
titulo: "listame mis cuentas de Meta Ads"
tags: [chat, agente, claudecode]
---

# 💬 listame mis cuentas de Meta Ads
> **ClaudeCode** · 2026-08-21 03:23 · `72ad284c-68dc-4fa4-954d-62fca2c3fed5`

---

### 🧑 Vos  <small>2026-08-21 03:23</small>

listame mis cuentas de Meta Ads

### 🤖 Claude  <small>2026-08-21 03:23</small>

_[usó herramienta: Read]_

### 🧑 Vos  <small>2026-08-21 03:23</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-08-21 03:23</small>

No tengo el MCP de Meta Ads (`ads_*`) conectado en esta sesión, así que no puedo consultarlas en vivo ahora mismo. Pero según lo que tengo registrado de tu cuenta (última verificación **2026-08-01**), estas son tus cuentas de Meta Ads:

| Cuenta (ID) | Nombre / negocio | Estado | Uso |
|---|---|---|---|
| **1482478863413097** | "cuenta 1" — Gonvra products (ARS, con medio de pago) | ✅ ACTIVE, `is_ads_mcp_enabled=true` | La operativa — acá están tus campañas |
| **2487859205019090** | — | ⚠️ Sin habilitar por API | No usar |
| **27009241552077096** | "cuenta 2" | ⚠️ UNSETTLED | No usar |

Datos asociados a la cuenta buena (1482478863413097):
- **Página FB:** "Gonvra pets" (page_id 1125904760604828)
- **Píxel/dataset:** "TIENDA CEPILLO 1" (26889872433954472) — vivo (PageView + ViewContent), sin AddToCart/Purchase todavía
- **Instagram:** ninguno vinculado
- **Campañas creadas (todas en PAUSA):** Test $4.000 (120250532987940505), Prospección Cama (120250532602990505), y la vieja de Envío Gratis (120250360311680505)

⚠️ **Ojo:** el acceso a estas cuentas fluctúa día a día. Para tener la lista real y actualizada hoy hay que correr `ads_get_ad_accounts` con el MCP de Meta Ads conectado.

¿Querés que revisemos por qué el MCP de Meta Ads no está disponible en esta sesión, o te alcanza con esta info de referencia?

### 🧑 Vos  <small>2026-08-21 03:24</small>

Pero ¿de qué cuenta? Porque yo quiero entrar a alguna de ellas, tipo se llama Gombra cero punto Gmail punto com. así literal, y se llama Matías González. Eso.

### 🤖 Claude  <small>2026-08-21 03:24</small>

Ah, entiendo — vos me estás hablando del **usuario/login de Facebook** (el mail y el nombre con los que entrás), no del número de cuenta publicitaria. Son dos cosas distintas:

- **El login personal de Facebook/Meta** → un mail (ej. `gonvra0@gmail.com`) + un nombre de perfil (**Matías González**). Con eso te logueás.
- **La cuenta publicitaria (Ad Account)** → es un número largo (ej. `1482478863413097`) que vive *dentro* de ese perfil, en el Business Manager.

Eso que me decís —**"gonvra0@gmail.com" (o parecido) + perfil "Matías González"**— sería tu **login de Facebook** para entrar a Ads Manager. Pero acá tengo que ser sincero: **ese dato del mail y nombre de login no lo tengo registrado en mi memoria**. Yo solo tengo guardados los IDs de las cuentas publicitarias, la página ("Gonvra pets") y el píxel — no las credenciales de acceso.

Dato que sí me cierra: tu página de Facebook se llama **"Gonvra pets"**, así que es coherente que el perfil "Matías González" con ese Gmail sea el dueño/admin.

Para no marearte, decime qué necesitás exactamente:

1. **Entrar a Ads Manager** → andá a [business.facebook.com](https://business.facebook.com) o [adsmanager.facebook.com](https://adsmanager.facebook.com) y logueate con ese mail + tu contraseña. Ahí vas a ver la cuenta **Gonvra products (1482478863413097)**.
2. **¿Te olvidaste el mail exacto o la contraseña?** → eso lo recuperás desde la pantalla de login de Facebook (yo no lo tengo).
3. **¿Querés que confirme cuál es el mail dueño de la cuenta?** → eso sí lo podría chequear, pero necesito el **MCP de Meta Ads conectado** (ahora no lo está).

¿Cuál de las tres es lo que buscás?

### 🧑 Vos  <small>2026-08-21 03:31</small>

Pero las campañas, ¿cómo se llaman?

### 🤖 Claude  <small>2026-08-21 03:31</small>

Estas son las campañas que tenés creadas en la cuenta **Gonvra products (1482478863413097)** — todas quedaron **en PAUSA** (cero gasto):

| Campaña | ID | Presupuesto | Estado |
|---|---|---|---|
| **GONVRA \| Test $4.000 \| Video Cepillo vs Botella** | 120250532987940505 | $4.000 total (2 días) | ⏸️ En pausa |
| **GONVRA \| TOFU \| Prospección (Cama)** | 120250532602990505 | $4.000/día (CBO) | ⏸️ En pausa |
| **GONVRA \| Ventas – Prospección (Envío GRATIS)** | 120250360311680505 | $3.300/día (CBO) | ⏸️ En pausa (la más vieja) |

Notas:
- Las tres son objetivo **Ventas (OUTCOME_SALES)**.
- La "Test $4.000" tiene 2 anuncios con imagen (cepillo y botella); los videos había que subirlos a mano en Ads Manager.
- La "Prospección (Cama)" apunta a `gonvra.com/products/cama-redonda-ortopedica-mascotas`.

⚠️ Ojo: esto es de mi última verificación (**2026-08-01**). Si desde entonces creaste, renombraste o borraste alguna, no me va a figurar. Para ver la lista exacta de hoy hay que abrir Ads Manager o conectar el MCP de Meta Ads.

¿Querés que te arme un resumen de qué anuncios tiene cada una, o buscás cuál prender primero?
