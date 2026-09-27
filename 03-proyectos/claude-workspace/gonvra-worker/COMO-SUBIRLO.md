# Asistente GONVRA · cómo ponerlo en marcha

Son 5 minutos. Todo gratis.

## 1 · Sacá la clave de Gemini

1. Entrá a [Google AI Studio](https://aistudio.google.com/apikey)
2. **Create API key** → copiala. Empieza con `AIza…`
3. **No la pegues en ningún lado público.** Solo va a Cloudflare.

## 2 · Creá el Worker en Cloudflare

1. Cuenta gratis en [dash.cloudflare.com](https://dash.cloudflare.com)
2. Menú izquierdo → **Compute (Workers)** → **Create** → **Start with Hello World** → **Deploy**
3. Ponele de nombre `gonvra-asistente`
4. **Edit code** → borrá todo lo que hay y pegá el contenido de `worker.js`
5. **Deploy**

## 3 · Cargá la clave como variable secreta

En el Worker → **Settings** → **Variables and Secrets** → **Add**

| Campo | Valor |
|---|---|
| Type | Secret |
| Name | `GEMINI_API_KEY` |
| Value | la clave `AIza…` |

**Deploy** de nuevo.

> Así la clave queda guardada en Cloudflare. Nadie la puede ver desde la página.

## 4 · Conectalo a la tienda

Copiá la URL del Worker (algo como `https://gonvra-asistente.TUCUENTA.workers.dev`) y pegala en:

**Editor del tema → GONVRA · Pie → Chat de la tienda → URL del servidor de IA**

Listo. El chat pasa a responder con Gemini.

## 5 · Probalo

Abrí gonvra.com, tocá el botón negro y preguntá algo que **no** esté en las 8 preguntas
cargadas, por ejemplo *"¿puedo usarla en la nuca?"*. Si contesta con criterio, funciona.

---

## Si algo falla

El chat está hecho para no romperse: **si el Worker no responde, vuelve solo** a las
respuestas cargadas en el editor. El cliente nunca ve un error.

Para ver qué pasó: Worker → **Logs** → **Begin log stream**, y probá el chat.

## Qué puede y qué no puede decir

Está atado corto a propósito. Tiene prohibido:

- Inventar precios, plazos, descuentos, stock o promociones
- Prometer que evita irritación, foliculitis o pelos encarnados
- Dar consejos médicos o dermatológicos
- Comparar con otras marcas por nombre
- Hablar del estado de un pedido (deriva a WhatsApp)

Si le preguntan algo que no está en la ficha, dice que no lo tiene y manda al WhatsApp.

## Cuando cambien datos de la tienda

Editá la constante `TIENDA` dentro de `worker.js` y volvé a hacer Deploy.
**Acordate de actualizar el precio cuando lo cambies en Shopify.**

## Costo

- Cloudflare Workers: gratis hasta 100.000 consultas por día.
- Gemini: la capa gratuita alcanza de sobra para una tienda nueva.
