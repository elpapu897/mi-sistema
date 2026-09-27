# GONVRA — Dónde estamos y qué falta (con prompts listos)
> Actualizado: 2026-08-21

## ✅ LO QUE YA ESTÁ HECHO (no tocar)

- **El equipo de agentes está armado y funcionó:** bot de Telegram, SEMÁFORO productivo (aprobación
  con revalidación), tablero Kanban "gonvra", 30 perfiles de agentes.
- **Primera auditoría real hecha** por 6 agentes (JEFE, ANALISTA, GUARDIA, TIENDA, TESTER, LEGAL).
- ✅ **CHECKOUT ARREGLADO** — desactivaste PayPal, quedó solo Mercado Pago. La tienda YA COBRA.
- ✅ **Política de envíos** publicada (ya no da 404).
- ✅ **Política de reembolso** corregida (10 días, no 30).
- **Memoria común:** todos los chats se exportan solos a Obsidian.
- **Espía de videos** listo (`video-intel.py`) para YouTube/TikTok.

---

## ⏳ LO QUE FALTA (en orden de importancia)

### 1. Probar que Mercado Pago cobra de verdad  → **LO HACÉS VOS**
La tienda cobra, pero hay que confirmar que un cliente puede pagar sin error.
- Hacé una compra de prueba con el producto más barato, con tu tarjeta.
- Fijate que llegue a "pago aprobado" y que aparezca la orden en Shopify.
- Después te la reembolsás desde el panel de Shopify.
- (No hay prompt: es algo físico que solo podés hacer vos.)

### 2. Revisar el píxel de Meta  → **CLAUDE WEB** (tiene Facebook conectado)
Prompt para pegar en la app de Claude:
```
Tenés mi Facebook conectado. Revisá el píxel de Meta de la cuenta de anuncios 1482478863413097
del negocio "Gonvra products". Decime: cuántos píxeles hay, si "TIENDA CEPILLO 1"
(id 26889872433954472) está activo y recibiendo eventos, y si existe un duplicado
(id 3919766821491073). Explicame si hay que unificarlos y cómo, pero NO borres ni cambies nada
todavía: primero mostrame el diagnóstico.
```

### 3. Terminar los cambios del tema  → **CLAUDE WEB** (tiene Shopify conectado)
Faltan dos cosas en el tema: el botón de arrepentimiento y cambiar el mail de contacto.
Prompt para pegar en la app de Claude:
```
Tenés mi Shopify conectado (tienda gonvra, gonvra.com). Necesito 2 cambios en el tema, SIEMPRE
sobre una copia (nunca el publicado); yo publico a mano después.
1) Agregar un "Botón de arrepentimiento" visible en la home y el footer, que lleve a la política de
   reembolso (ya publicada) o abra un mail a gonvra0@gmail.com. En Argentina es obligatorio por ley.
2) Reemplazar en TODO el tema "contacto@gonvra.com" por "gonvra0@gmail.com" (incluí los enlaces
   mailto del hero y el footer).
Reglas: NO crear temas nuevos al pedo (ya hay muchos), reutilizá UNA sola copia de trabajo, y
verificá cuál es el tema MAIN vigente antes de duplicar. Cuando termines, decime cómo ver la
vista previa para aprobarla.
```

### 4. Vincular Instagram @gonvra.pets a Meta Ads  → **LO HACÉS VOS** (o Claude Web te guía)
Sin esto, los anuncios no se muestran en Instagram ni Reels. Es gratis y de alto impacto.
Prompt para Claude Web:
```
Guiame paso a paso para vincular mi Instagram @gonvra.pets a la página de Facebook "Gonvra pets"
(id 1125904760604828) y a la cuenta de anuncios 1482478863413097, así mis anuncios se pueden
mostrar en Instagram y Reels.
```

### 5. Avisarle a Hermes lo que avanzó  → **HERMES** (por Telegram o la app de Hermes)
Para que actualice el estado del equipo. Prompt:
```
Update GONVRA: el checkout ya quedó arreglado (desactivé PayPal, quedó solo Mercado Pago). Las dos
políticas están publicadas (envíos ya no da 404, reembolso dice 10 días). Falta: probar una compra
real por Mercado Pago, el píxel de Meta, y los dos cambios del tema (botón de arrepentimiento y
mail), que los estoy haciendo con Claude Web porque tiene Shopify conectado. Actualizá el resumen
del JEFE con esto y decime cuál es la prioridad #1 según los informes de la Fase 1.
```

---

## 🔮 EL PASO GRANDE (para el sueño 24/7)

Para que **Hermes** (y no vos, ni Claude Web a mano) maneje Shopify y Meta solo, hay que darle sus
propias llaves (tokens). Es un trámite de una vez, con pasos delicados. **Lo dejamos para una
sesión dedicada con Claude Code** (yo te guío para crear los tokens y los conecto a Hermes). Hasta
entonces, Claude Web es tu mejor herramienta para ejecutar cosas en Shopify y Meta.

---

## RESUMEN DE QUIÉN HACE QUÉ

| Tarea | Quién |
|---|---|
| Compra de prueba (Mercado Pago) | **Vos** (físico) |
| Revisar píxel de Meta | **Claude Web** |
| Botón arrepentimiento + mail en tema | **Claude Web** |
| Vincular Instagram | **Vos / Claude Web** |
| Actualizar estado del equipo | **Hermes** |
| DNS/MX del dominio (opcional) | **Vos** (en donde compraste el dominio) |
| Darle tokens a Hermes (24/7) | **Claude Code** (otra sesión) |
