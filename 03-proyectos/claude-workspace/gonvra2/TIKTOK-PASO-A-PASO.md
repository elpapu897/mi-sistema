---
tags: [gonvra, tiktok, api, tramite]
actualizado: 2026-09-24
---

# 🎵 TikTok API — lo que dice la documentación oficial

> Leído el 24/09/2026 en developers.tiktok.com. Esto **no** es de memoria.

---

## ⚠️ LO PRIMERO: el dato que cambia todo

La documentación de TikTok dice, textual, sobre las apps **sin auditar**:

> *"**All user accounts using the API client to post must be set to private**
> at the time of posting."*

Traducido: **mientras la app no esté auditada, tu cuenta de TikTok tiene que estar
en PRIVADO para poder publicar por API.**

Una cuenta privada no aparece en el Para Ti, no la ve nadie que no te siga, y no
vende nada. O sea: **la API sin auditar no sirve para vender.**

Las otras restricciones sin auditoría:
- Los videos quedan en **modo privado**
- Máximo **5 usuarios** publicando en 24 h
- Hay que **verificar el dominio** para poder mandar videos por URL

---

## 🤔 Entonces, ¿conviene?

**Depende de cuánto vayas a publicar.**

| Situación | Qué conviene |
|---|---|
| 1 o 2 videos por día | **Subir a mano.** 3 minutos, cero trámite, cuenta pública |
| 3+ videos por día, todos los días | Hacer la auditoría |

Hoy GONVRA tiene **1 video publicado en total**. Con ese volumen, el trámite es
trabajo que no devuelve nada.

**Y hay una trampa:** TikTok aprueba auditorías mirando que la integración tenga
uso real y contenido legítimo. Con una cuenta nueva y casi sin videos, lo más
probable es que la rechacen. **Publicar primero a mano mejora las chances después.**

---

## 📋 Si igual querés hacerlo, estos son los pasos

### Paso 1 — Crear la cuenta de desarrollador

👉 **https://developers.tiktok.com/signup**

Entrá con la cuenta de TikTok de GONVRA. Te va a pedir mail y verificación.

### Paso 2 — Crear la app

👉 **https://developers.tiktok.com/apps** → **Connect an app**

- Nombre: `GONVRA`
- Categoría: comercio / retail
- Descripción: publicación de contenido propio de la marca

### Paso 3 — Agregar el producto y el scope

Dentro de la app:
1. **Add products** → **Content Posting API**
2. Activar **Direct Post** (si no, los videos quedan en borrador y hay que
   publicarlos a mano igual)
3. En **Scopes**, pedir: `video.publish` y `video.upload`

### Paso 4 — Verificar el dominio

TikTok necesita que pruebes que gonvra.com es tuyo, para poder mandarle videos
por URL.

En la app: **Manage apps** → **URL properties** → agregar `gonvra.com`

Te va a dar un archivo o un meta tag. **Pasámelo y yo lo subo al tema de Shopify**
(eso ya lo sé hacer, es lo mismo que hicimos con Search Console).

### Paso 5 — Pedir la auditoría

Cuando tengas la integración andando, en la app hay un botón para pedir el
**App Review / audit**. Ahí revisan que cumplas los términos.

**Pasame el Client Key y el Client Secret** cuando los tengas y armo el resto:
el flujo OAuth, la subida y la cola, igual que hice con Instagram.

---

## ✅ Mientras tanto: lo que YA funciona

El video está listo y la cuenta es pública. Subirlo a mano son 3 minutos:

👉 **https://www.tiktok.com/upload**

El texto, los hashtags y el horario están en:
`~/Escritorio/GONVRA-PARA-SUBIR/COMO-SUBIRLO.md`

Y ahora, además, **podemos generar clips nuevos con Replicate** (US$0.28 cada uno,
6 segundos, verticales 9:16). El sistema los deja en la cola y los aprobás desde
el celular.

---

## 📌 Mi recomendación

1. **Esta semana:** subí 5 videos a mano. Son 15 minutos en total.
2. **Con eso:** vas a tener datos de qué gancho funciona **y** historial para que
   TikTok te apruebe la auditoría.
3. **Después:** hacemos el trámite, que para entonces va a tener sentido y más
   chances de salir aprobado.

Hacer el trámite hoy es pelear por automatizar algo que todavía no estás haciendo.
