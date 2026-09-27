# ▼▼▼ PEGAR ESTO EN HERMES ▼▼▼

Van las respuestas. Ojo que tu numeración venía salteada (la primera no tenía número y no había
un 6), así que te repito la pregunta en corto para que no haya confusión.

---

## ACCESOS

**A0 — ¿Podés entrar al admin de Shopify y modificar Pagos?**
→ **a) Sí, soy el dueño y tengo acceso total.** Es mi tienda. Lo que no puedo es que lo hagas vos:
la config de pagos está fuera del alcance del MCP (`appInstallations` da "access denied"), así que
esa parte la ejecuto yo a mano sí o sí.

**A1 — ¿Te guío botón por botón para desactivar PayPal?**
→ **a) Sí, botón por botón.** No soy técnico. Y aclaro una cosa que ya nos pasó: **sacar el logo de
PayPal del tema NO desactiva la pasarela.** Hay que desactivarla en
`admin.shopify.com/store/gonvra/settings/payments`. Son dos cosas distintas:
- `paypal` (el botón)
- `Credit/Debit card by PayPal` ← **esta es la traicionera**: al cliente se le muestra como
  "Pagos con tarjeta de crédito y débito", parece tarjeta común, pero es PayPal y no procesa
  tarjetas argentinas en pesos.
Las dos van desactivadas. Queda solo **Mercado Pago Checkout Pro**.

**A2 — ¿Entrás al admin de eventos de Meta y a la integración Facebook & Instagram de Shopify?**
→ **a) Sí, a los dos.** Pero anotá esto porque te va a ahorrar tiempo:
- Cuenta de anuncios a usar: **1482478863413097**. Las otras dos no sirven
  (2487859205019090 sin habilitar, 27009241552077096 UNSETTLED).
- **El acceso por API a esa cuenta fluctúa día a día.** Verificá siempre con `ads_get_ad_accounts`
  antes de asumir que podés.
- Píxel bueno: **26889872433954472** ("TIENDA CEPILLO 1").
- ⚠️ **Hay un píxel duplicado, `3919766821491073`**, que inyecta la app de Shopify y NO pertenece a
  la cuenta de anuncios. Recibe los mismos ViewContent. **Unificar todo en el 26889872433954472.**
- **Facebook.com está bloqueado para el navegador del asistente** → Ads Manager y Business Manager
  los manejo yo a mano, con tu guía.

**A3 — ¿Tenés acceso a @gonvra.pets y a la página "Gonvra pets"?**
→ **a) Sí, a ambos.** La página es `page_id 1125904760604828`.
🔴 **Esto es prioridad alta, no la dejes para después:** hoy **NO hay ningún Instagram vinculado** a
la cuenta de anuncios (`ads_get_ig_accounts` → vacío), así que **los anuncios no se entregan en
Instagram ni en Reels**. Es la mejora de mayor impacto que tengo disponible y es gratis. Ponela en
la semana 1, no en la fase de pauta.

**A4 — ¿Cómo lee el equipo gonvra0@gmail.com?**
→ **a) Acceso autorizado (OAuth), sin compartir contraseña.**
📌 Y ojo: **`contacto@gonvra.com` no recibe nada** porque el dominio no tiene registros MX. Si hay
un formulario o un botón "Escribinos" apuntando ahí (la "Auditoría 2026" puso uno en la home),
**estamos perdiendo consultas de clientes sin enterarnos**. Que TIENDA lo cambie a gonvra0@gmail.com
en la semana 1.

**A5 — ¿Qué acceso a WhatsApp aceptás?**
→ **a) Leer WhatsApp Web y dejar respuestas redactadas, sin enviarlas.**
Condición dura: **nada que ponga en riesgo el número.** Si el método de lectura huele a que me
pueden banear la cuenta, no lo uses y avisame. El número de WhatsApp es con el que vendo; perderlo
es peor que no tener el agente.

---

## AUTONOMÍA

**A7 — ¿TIENDA reutiliza una única copia de trabajo del tema?**
→ **a) Sí; puede editar la copia, pero nunca publicarla.**
Y subrayo el "única": **ya tengo como 16 temas dando vueltas y me vuelve loco.** UNA sola copia de
trabajo para todos los cambios pendientes. Si veo que aparecen temas nuevos por cada cambio, apago
el agente.
Además: antes de duplicar, **verificá cuál es el MAIN vigente** — cambia seguido y publicar una
copia vieja revierte trabajo hecho.

**A8 — ¿Qué puede hacer TESTER ante un error que rompe ventas?**
→ **a) Documentarlo, avisar urgente y preparar el arreglo en la copia.** Que me llegue el arreglo
listo para que yo solo apruebe y publique. No quiero enterarme de un checkout roto y encima tener
que esperar a que alguien empiece a arreglarlo.

**A9 — ¿Pueden crear archivos en `~/Claude/gonvra/` sin permiso?**
→ **a) Sí.** Las carpetas de los 30 agentes ya están creadas. Escriban libremente ahí adentro.
Fuera de `~/Claude/gonvra/` sí me preguntan.

**A10 — Si dos agentes se contradicen, ¿quién decide?**
→ **a) JEFE elige la de mayor impacto en pesos y me explica el riesgo.** No quiero que me lleguen
empates para desempatar yo. Si la decisión es realmente cara o irreversible, ahí sí que me muestre
las dos.

---

## NOTIFICACIONES

**A11 — ¿Dónde recibo el SEMÁFORO?** → **a) Chat privado con el bot.**

**A12 — ¿La aprobación desde Telegram ejecuta al toque?**
→ **a) Sí, pero únicamente la acción exacta mostrada.**
Con un candado: si al momento de ejecutar **algo cambió** respecto de lo que me mostró (subió el
presupuesto, cambió el precio del producto, se quedó sin stock), **no ejecuta: vuelve a preguntar.**
Un ✅ vale para lo que leí, no para una versión nueva.

**A13 — ¿Quién más puede aprobar?** → **a) Solamente yo.**

**A14 — Respaldo si Telegram o Hermes se caen?**
→ **a) Notificación de escritorio + `URGENTE.md`**, y sumale **b) mail a gonvra0@gmail.com**.
Quiero los tres. Si el canal de avisos se cae justo cuando hay una urgencia, no me sirve de nada.
Y que GUARDIA se vigile a sí mismo: si un agente no corre cuando le toca, eso también es una alerta.

---

## PRESUPUESTO

**A15 — Máximo a arriesgar en el primer test de Meta?**
→ **a) Se define recién cuando checkout, píxel y margen estén verificados.**
Como referencia: ya hay una campaña armada y en pausa con **$4.000 en total** (lifetime, 2 días) —
"GONVRA | Test $4.000", id 120250532987940505. Ese es el orden de magnitud con el que pienso
arrancar. Pero el número final me lo tiene que proponer FINANZAS + PRECIOS con el margen real en la
mano, no yo a ojo.
Dato duro para que lo tengas: **el mínimo por conjunto es ~$1.497/día**, así que abajo de eso no se
puede planificar nada.

**A16 — Regla para proponerme una herramienta paga?**
→ **a) Solo si se paga con 3 ventas o menos y no hay alternativa gratis razonable.**
Y agregale dos condiciones: que tenga **prueba gratis o se pueda cancelar en un click**, y que en la
propuesta me digas **qué agente deja de hacer trabajo manual gracias a eso**. Con 10 órdenes en toda
la historia, casi todo va a caer en "no lo pagues ni loco".

---

## CONTENIDO

**A17 — ¿Podés producir contenido casero con el celular?**
→ 🔴 *(Matías: confirmá o cambiá esta)* **a) Sí, si me dan guion y lista exacta de tomas.**
Condición: que el guion sea **grabable en 10 minutos, sin edición complicada y sin equipo**. Si me
piden una producción, no lo voy a hacer y el agente va a quedar generando ideas que nunca se
ejecutan. Volumen simple > perfección.

**A18 — ¿Quién aparece en los videos?**
→ 🔴 *(Matías: confirmá o cambiá esta)* **a) Manos, productos, mascotas y voz en off; sin mi cara.**
Nota para el equipo: si en algún momento los números muestran que mostrar la cara mejora mucho la
conversión, decímelo con el dato y lo reconsidero. Pero por defecto, sin cara.

---

## OPERACIÓN

**A19 — ¿Aceptás una compra real de prueba y después reembolsarla?**
→ **a) Sí, si primero verificamos el costo y el procedimiento.**
Es la única forma de saber si Mercado Pago cobra de verdad. Antes de hacerla quiero por escrito:
1. Qué producto y por cuánto (el más barato que haya).
2. **Si Mercado Pago devuelve la comisión al reembolsar o se la queda** (ese es el costo real de
   la prueba).
3. Cuántos días tarda el reembolso.
4. Qué exactamente vamos a verificar: que se cobre, que **el píxel dispare Purchase**, que llegue el
   mail de confirmación, y que la orden aparezca bien en Shopify.
Esa prueba es el hito que destraba todo. Mientras no esté hecha, no se prende un peso de pauta.
📌 Contexto: las **10 órdenes de toda la historia son Cash on Delivery**. Nunca se cobró una tarjeta.

**A20 — ¿Qué dirección usamos para probar envíos?**
→ **a) Ciudad, provincia y CP; sin calle ni datos personales.** Pero hacelo con **tres**: CABA, una
ciudad grande del interior (Córdoba o Rosario) y una localidad chica de otra provincia.
Motivo: hay **dos perfiles de envío** ("AutoDS Free Shipping" y "Perfil general"/bodega Besares
2688) y ya nos pasó que **un producto sin stock en la bodega de su perfil se queda sin tarifas y
rompe el checkout entero**. Probá con `draftOrderCalculate`, nunca por la etiqueta del perfil.
Y ojo: el **Combo Chau Pelos es un bundle** — su envío lo definen los componentes, no su propio
perfil. Ese probalo aparte.

---

## Tres cosas que te agrego yo, sin que las preguntes

1. **El catálogo cambia todo el tiempo.** No hardcodees ningún producto en la config de los agentes.
   Todo se lee en vivo de la API de Shopify. Configurá con **reglas** (margen ≥ 2,5×, precio ≥
   $16.990 para pautar en frío), no con nombres de productos. Está explicado en la sección 1-ter del
   brief y en el CONTEXTO.

2. **Botón de arrepentimiento.** En Argentina es obligatorio y visible para toda tienda online.
   Que LEGAL lo verifique en la semana 1. También la política de envíos, que hoy da **404** desde el
   footer. Eso es riesgo de multa, no un detalle de prolijidad.

3. **Cuando me des la tabla de costos**, en la columna "podría valer la pena" quiero que revises
   primero **lo que Shopify ya me da gratis y no estoy usando** — sobre todo **Shopify Email
   (gratis hasta 10.000 mails/mes)**. Si eso alcanza para carritos abandonados y post-compra, no
   quiero que me propongas ninguna app de email marketing paga.

---

Con esto, dale: las 5 cosas que prometiste, en ese orden.

# ▲▲▲ FIN ▲▲▲
