---
tags: [gonvra, tareas-matias, credenciales]
actualizado: 2026-09-21
---

# ✋ LO QUE TENÉS QUE HACER VOS

> Todo lo demás ya está instalado y funcionando. Esto es lo único que **no puedo hacer yo**,
> porque son cuentas tuyas y hay que poner tu contraseña.
> Están en orden: el primero es el que más plata trae.

---

## 1️⃣ TOKEN DE SHOPIFY — **INSTRUCCIONES CORREGIDAS 22/09**

> ❌ **Lo que decía antes estaba MAL.** Mandaba a un menú que **no existe** en esta tienda.
> Shopify cambió: las "custom apps" del admin ya no están, ahora es el **Dev Dashboard**,
> y ahí no hay ningún botón que devuelva un `shpat_`.

### Lo que se probó y NO funciona (no lo repitas)
- El token `atkn_` del Dev Dashboard → **401** contra la Admin API (probado 4 formas)
- Los 6 tokens guardados del Shopify CLI → **401** en pedidos
  (el de la tienda **sí** sirve para *temas* con header `Authorization: Bearer`,
  pero **no** para pedidos: solo tiene permiso de temas)

### Lo que SÍ funciona: OAuth, y ya está automatizado

**Paso A — Sacar 2 datos de la app** (Dev Dashboard → app **GONVRA Agentes**):
- **Client ID**
- **Client secret**

**Paso B — Autorizar la URL de vuelta.** En la misma app, en *Redirect URLs* / *URLs de
redireccionamiento*, agregá exactamente esto y guardá:

    http://localhost:3456/callback

**Paso C — Correr este comando TAL CUAL.** No hay nada que reemplazar:

```
python3 ~/Claude/gonvra2/sacar-token-shopify.py
```

El script te va a **preguntar** el Client ID y el Client secret. Los pegás cuando
te los pida. Si pegás sin querer el texto de ejemplo, te frena y te avisa.

Eso abre el navegador, apretás **Instalar app**, y el script solo:
consigue el token → **lo prueba contra pedidos, clientes y productos** →
lo guarda cerrado en `~/.hermes/.gonvra-secrets.env`.

No hay que copiar ni pegar ningún token a mano.

---

## 2️⃣ QUE LA COMPU NO SE DUERMA AL CERRAR LA TAPA ⏱️ 30 segundos

Ya dejé que no se suspenda sola. Falta solo la tapa, y eso pide tu contraseña.

Copiá y pegá esto en una terminal:

```
sudo mkdir -p /etc/systemd/logind.conf.d && printf '[Login]\nHandleLidSwitch=ignore\nHandleLidSwitchExternalPower=ignore\nHandleLidSwitchDocked=ignore\n' | sudo tee /etc/systemd/logind.conf.d/gonvra-no-dormir.conf && sudo systemctl restart systemd-logind
```

Te va a pedir tu contraseña de la compu. Después de eso podés cerrar la tapa y los agentes
siguen trabajando.

---

## 3️⃣ OAUTH DE GOOGLE (para Gmail) ⏱️ 10 minutos

**Ya dejé el conector instalado con 15 herramientas** (leer, buscar, responder, etiquetar).
Falta solo la credencial.

👉 **https://console.cloud.google.com/**

1. Arriba a la izquierda: **Crear proyecto** → nombre: `GONVRA` → Crear
2. Buscador de arriba: escribí **"Gmail API"** → entrá → botón **Habilitar**
3. Menú izquierdo: **Pantalla de consentimiento de OAuth**
   - Tipo: **Externo** → Crear
   - Nombre de la app: `GONVRA` · correo: `gonvra0@gmail.com`
   - Seguir hasta el final y guardar
   - En **Usuarios de prueba** → **Agregar** → poné `gonvra0@gmail.com`
4. Menú izquierdo: **Credenciales** → **Crear credenciales** → **ID de cliente de OAuth**
   - Tipo de aplicación: **App de escritorio**
   - Nombre: `GONVRA agentes` → Crear
5. Te muestra **ID de cliente** y **Secreto del cliente**. **Copiame los dos.**

⚠️ Mientras la app esté en modo prueba, hay que renovar cada 7 días. Si molesta, después
la publicamos.

---

## 4️⃣ GOOGLE SEARCH CONSOLE ⏱️ 15 minutos — gratis y muy útil

Sirve para saber **con qué palabras la gente llega a gonvra.com**. Es tráfico que no se paga.

👉 **https://search.google.com/search-console**

1. Entrá con `gonvra0@gmail.com`
2. **Agregar propiedad** → opción **Prefijo de URL** → escribí `https://gonvra.com`
3. Método de verificación: **Etiqueta HTML** → copiá la etiqueta que te da
4. **Pegámela en el chat** — yo la pongo en el tema de Shopify y quedás verificado

---

## 5️⃣ INSTAGRAM (publicar automático) ⏱️ 1-2 días

**Antes que nada, verificá esto** (si no, no hay API posible):
- La cuenta de Instagram tiene que ser **Profesional / Empresa** (no personal)
- Tiene que estar **vinculada a una página de Facebook**

Se cambia desde la app: *Configuración → Tipo de cuenta → Cambiar a cuenta profesional*.

Después:

👉 **https://developers.facebook.com/apps/**

1. **Crear app** → tipo **Empresa** → nombre: `GONVRA`
2. Agregar producto: **Instagram Graph API**
3. En **Permisos**, pedí: `instagram_basic`, `instagram_content_publish`, `pages_show_list`
4. Copiame el **ID de la app** y el **Secreto de la app**

✅ **Buena noticia:** para publicar en **tu propia** cuenta **no hace falta** esperar la
revisión de Meta. La revisión es solo para publicar en cuentas de otros.

---

## ❌ LO QUE NO SE PUEDE (y por qué)

| Qué                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Por qué no                                                                                                                                                                |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Espiar anuncios automático**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Instalé el conector y funciona, pero **Facebook lo bloquea** (403 anti-bot). Probado 2 veces. **Se hace a mano:** https://www.facebook.com/ads/library/ → País: Argentina |
| **TikTok GRAM (publicar automático) ⏱️ 1-2 días<br><br>  <br><br>**Antes que nada, verificá esto** (si no, no hay API posible):<br><br>- La cuenta de Instagram tiene que ser **Profesional / Empresa** (no personal)<br><br>- Tiene que estar **vinculada a una página de Facebook**<br><br>  <br><br>Se cambia desde la app: *Configuración → Tipo de cuenta → Cambiar a cuenta profesional*.<br><br>  <br><br>Después:<br><br>  <br><br>👉 **https://developers.facebook.com/apps/**<br><br>  <br><br>1. **Crear app** → tipo **Empresa** → nombre: `GONVRA`<br><br>2. Agregar producto: **Instagram Graph API**<br><br>3. En **Permisos**, pedí: `instagram_basic`, `instagram_content_publish`, `pages_show_list`<br><br>4. Copiame el **ID de la app** y el **Secreto de la app**<br><br>  <br><br>✅ **Buena noticia:** para publicar en **tu propia** cuenta **no hace falta** esperar la<br><br>revisión de Meta. La revisión es solo para publicar en cuentas de otros.<br><br>  <br><br>---<br><br>  <br><br>## ❌ LO QUE NO SE PUEDE (y por qué)<br><br>  <br><br>\|Qué\|Por qué no\|<br>\|---\|---\|<br>\|**Espiar anuncios automático**\|Instalé el conector y funciona, pero **Facebook lo bloquea** (403 anti-bot). Probado 2 veces. **Se hace a mano:** [https://www.facebook.com/ads/library/](https://www.facebook.com/ads/library/) → País: Argentina\|<br>\|**TikTok publicar automático**\|Sin auditoría aprobada de TikTok, los videos suben como **borrador privado** — igual hay que publicarlos a mano. No vale la pena todavía\|<br>\|**Meta Ads (pauta)**\|Necesita un token de un servicio pago. Y sin ventas **no hay nada que optimizar**. Recién cuando haya datos\|<br>\|**Publicar el video 1**\|Es tuyo: entrar a TikTok y subirlo. 3 minutos. **Sigue siendo lo único que trae plata**\|publicar automático** | Sin auditoría aprobada de TikTok, los videos suben como **borrador privado** — igual hay que publicarlos a mano. No vale la pena todavía                                  |
| **Meta Ads (pauta)**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Necesita un token de un servicio pago. Y sin ventas **no hay nada que optimizar**. Recién cuando haya datos                                                               |
| **Publicar el video 1**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Es tuyo: entrar a TikTok y subirlo. 3 minutos. **Sigue siendo lo único que trae plata**                                                                                   |

---

## 📌 Resumen de 10 segundos

**Hoy, mínimo, hacé estas 3:**
1. El **token de Shopify** (2 min)
2. El comando de la **tapa** (30 seg)
3. **Publicar el video 1** en TikTok (3 min)

Con eso el sistema pasa de "prolijo" a "vendiendo".
---

## 🔌 CONECTAR LOS COMENTARIOS DE INSTAGRAM ⏱️ 5 minutos

**Es la automatización que convierte seguidores en ventas.** Ya está armada y
esperando: cuando alguien comente *"precio"*, *"info"* o *"quiero"* en un post,
le llega el link por privado al instante y a vos te avisa por Telegram.

Falta un solo paso: decirle a Meta a dónde avisar.

👉 **https://developers.facebook.com/apps** → tu app → **Instagram** → **Webhooks**

1. Botón **Agregar suscripción** / *Edit subscription*
2. **URL de devolución de llamada** (Callback URL):

   La URL actual está en: `~/.hermes/gonvra-url-publica.txt`
   Pedísela a Claude, o abrí ese archivo y pegá lo que dice **+ `/webhook/gonvra-ig`**

3. **Token de verificación**: `gonvra2026verify`
4. Botón **Verificar y guardar**
5. En la lista de campos, tildá **`comments`**

⚠️ **Importante:** esa URL es temporal y cambia cuando se reinicia el túnel.
Hay un job que la mantiene viva para Shopify, pero **la de Instagram hay que
actualizarla a mano** cada vez que cambie.

Para que sea fija y no cambie nunca: hace falta conectar `gonvra.com` a Cloudflare
(gratis). Decile a Claude que lo haga cuando quieras.

---
---

## 🎵 TIKTOK — leelo antes de hacer el trámite

**La documentación oficial dice que sin auditoría, tu cuenta tiene que estar en
PRIVADO para publicar por API.** Una cuenta privada no vende.

Todo el detalle y los pasos: `TIKTOK-PASO-A-PASO.md`

**Mi consejo:** subí 5 videos a mano esta semana (15 min en total). Con eso vas a
tener datos de qué funciona **y** historial para que TikTok apruebe la auditoría
después. Hoy la rechazarían.

---

## 📊 META ADS — para leer campañas y la Ad Library

El token de Instagram **no sirve** para esto. Son dos sistemas distintos.

**Paso 1** — En developers.facebook.com → tu app → **Facebook Login** → Configuración,
agregá esta URL en *URI de redireccionamiento de OAuth válidos* y guardá:

```
http://localhost:3457/callback
```

**Paso 2** — Corré esto tal cual (usa la app que ya tenemos guardada):

```
python3 ~/Claude/gonvra2/sacar-token-meta.py
```

Se abre el navegador, das permiso, y el script consigue el token, lo prueba,
lo convierte en uno de 60 días y lo guarda solo.

**Para qué sirve:** leer tus campañas cuando pongas pauta, y **la Ad Library
oficial** (que hoy está bloqueada por anti-bot cuando la scrapeamos).

---
