# GONVRA — Equipo de agentes IA 24/7

Brief para armar en Hermes. Tienda: **gonvra.com** (artículos para mascotas, Argentina, Shopify).
Objetivo: un "equipo de trabajo" de agentes que corren solos, cada uno con un rol, un horario y un
entregable concreto. Nada de agentes que "piensan": cada uno **produce un archivo o un mensaje**.

---

## 0. Reglas del equipo (aplican a todos)

- **Idioma:** español rioplatense. Nada de "tú".
- **Nunca publican nada solo.** Todo agente **propone**, Matías **aprueba**. Excepción: reportes
  internos (esos sí se escriben solos).
- **Salida a disco:** cada agente escribe en `~/Claude/gonvra/<agente>/AAAA-MM-DD.md`.
- **Un resumen diario único:** a las 08:00 se genera `~/Claude/gonvra/DAILY.md` con lo mejor de
  todos los agentes (máx. 1 pantalla). Eso es lo único que Matías tiene que leer sí o sí.
- **Cero cambios en el theme sin aprobación.** El flujo sigue siendo: duplicar tema → editar copia →
  el usuario publica.
- **Presupuesto Meta:** ningún agente sube presupuesto ni despausa campañas. Solo recomienda.
- **Memoria compartida:** todos leen `~/Claude/gonvra/CONTEXTO.md` (productos, márgenes, tono de
  marca, público objetivo, campañas activas) antes de trabajar.

---

## 1. Los agentes

### 🔍 SCOUT — Cazador de productos en tendencia
**Corre:** todos los días 06:00 y 18:00
**Qué hace:**
- Rastrea tendencias en nicho mascotas: TikTok Creative Center, Google Trends AR, Amazon Movers,
  AliExpress/CJ best sellers, subreddits de perros/gatos, grupos de FB argentinos.
- Filtra por: se puede enviar a AR, margen ≥ 2.5x, no frágil, "wow" visual en 3 segundos.
**Entrega:** top 5 productos con foto, costo estimado, precio sugerido en ARS, ángulo de venta,
por qué ahora, y nivel de saturación (bajo/medio/alto).
**Descartar:** cualquier cosa que ya vendan 10 tiendas argentinas grandes.

---

### 📊 ANALISTA — El que mira los números
**Corre:** diario 07:30 + resumen semanal los lunes
**Qué hace:**
- Lee Shopify (ventas, sesiones, conversión, productos top, carritos abandonados) y Meta Ads
  (gasto, CPA, ROAS, CTR, frecuencia).
- Compara contra los últimos 7 y 30 días. Detecta anomalías: caída de conversión, fatiga de
  creativo (frecuencia > 2.5), producto que se está muriendo, producto que despega.
**Entrega:** 5 bullets máximo. Cada uno: qué pasó → por qué probablemente → qué hacer hoy.
**Alerta urgente** (mensaje inmediato, no espera al daily): ventas 0 en 24h, pixel sin eventos,
gasto sin conversiones > 2x CPA objetivo, producto sin stock que está en anuncios.

---

### 🎯 MEDIABUYER — Campañas Meta
**Corre:** diario 09:00
**Qué hace:**
- Revisa cada conjunto de anuncios activo y decide: escalar / mantener / pausar / renovar creativo.
- Arma la estructura de campañas nuevas (públicos, ubicaciones, presupuesto mínimo ~$1.500/día).
- Detecta cuándo un creativo se quemó y le pide reemplazo a CREATIVO.
**Entrega:** lista de acciones concretas con el cambio exacto ("subir presupuesto de X de 1500 a
2200", "pausar adset Y, CPA 3x"). Matías ejecuta o le da OK para ejecutar.
**Ojo:** el pixel estaba dormido — si no hay eventos, el primer entregable es arreglar eso.

---

### 📱 TIKTOKER — Especialista TikTok
**Corre:** diario 10:00
**Qué hace:**
- Mira qué está funcionando en el nicho mascotas en TikTok AR/LatAm: sonidos, formatos, hooks,
  cuentas que crecen rápido.
- Detecta el formato ganador de la semana y lo adapta a productos de GONVRA.
**Entrega:** 3 ideas de video con guion completo: hook (primeros 2s), desarrollo, CTA, sonido
sugerido, texto en pantalla, duración. Listas para grabar con el celular.

---

### 📸 INSTAGRAMER — Especialista Instagram
**Corre:** diario 10:00
**Qué hace:**
- Reels, carruseles e historias. Vigila competencia argentina y cuentas de mascotas grandes.
- Cuida el feed como marca (paleta, coherencia visual).
**Entrega:** plan de 3 posteos + 5 historias, con copy listo, hashtags y formato.
Un carrusel educativo por semana (los que más guardan).

---

### ✍️ CONTENIDO — Guías, blog y SEO
**Corre:** lunes, miércoles y viernes 11:00
**Qué hace:**
- Escribe guías útiles para dueños de mascotas que además venden ("cómo elegir el arnés correcto",
  "por qué tu perro tira de la correa"). Cada guía linkea productos de la tienda.
- Optimiza fichas de producto: título, descripción, bullets, SEO, objeciones resueltas.
**Entrega:** 1 artículo completo (800-1200 palabras) o 5 fichas de producto reescritas.

---

### 🎨 CREATIVO — Imágenes y visuales
**Corre:** a pedido de MEDIABUYER / TIKTOKER / INSTAGRAMER
**Qué hace:**
- Genera creativos publicitarios, banners, fotos de producto en contexto, thumbnails.
- Usa el script de Replicate (nano-banana) que ya está configurado. Formato 4:5 para Meta,
  9:16 para stories/TikTok. Siempre cierra los prompts con "no text".
**Entrega:** los archivos en `~/Claude/gonvra/creativos/` + una línea explicando el ángulo.

---

### 💬 ATENCIÓN — Voz del cliente
**Corre:** diario 12:00 y 19:00
**Qué hace:**
- Revisa consultas (DM, WhatsApp, mail), preguntas repetidas y objeciones.
- Detecta patrones: "¿hacen envío a X?", "¿es de buena calidad?" → esos son huecos en la tienda.
**Entrega:** top 3 objeciones de la semana + propuesta de FAQ/copy/sección para matarlas.
Bonus: borradores de respuesta para lo repetitivo.

---

### 🕵️ ESPÍA — Competencia
**Corre:** martes y jueves 15:00
**Qué hace:**
- Monitorea tiendas argentinas de mascotas: precios, productos nuevos, promos, y sobre todo la
  **biblioteca de anuncios de Meta** (qué están corriendo y hace cuánto — si un anuncio lleva
  30+ días activo, funciona).
**Entrega:** qué cambió esta semana + 2 cosas robables (con criterio).

---

### 🧠 JEFE — Coordinador
**Corre:** diario 08:00 (después de que los demás dejaron su output) y domingos 20:00
**Qué hace:**
- Lee todo lo que produjo el equipo, tira lo irrelevante, resuelve contradicciones y arma el DAILY.
- Domingo: informe semanal + las 3 prioridades de la semana que viene.
- Es el único que le habla a Matías cuando no hay urgencia.
**Entrega:** `DAILY.md` — máximo 10 líneas: 1 número clave, 1 alerta, 3 acciones para hoy.

---

## 2. Cómo se conectan

```
SCOUT ──────┐
ESPÍA ──────┤
ANALISTA ───┼──> JEFE ──> DAILY.md ──> Matías (decide)
ATENCIÓN ───┤                              │
            │                              └──> aprueba ──> se ejecuta
MEDIABUYER ─┤
TIKTOKER ───┼──> CREATIVO (les hace los visuales)
INSTAGRAMER ┤
CONTENIDO ──┘
```

**Cadena típica:** SCOUT encuentra producto → CONTENIDO le escribe la ficha → CREATIVO hace las
imágenes → TIKTOKER/INSTAGRAMER hacen los videos → MEDIABUYER arma la campaña → ANALISTA mide →
JEFE reporta. Todo el ciclo en 48-72hs en vez de dos semanas.

---

## 3. Arranque por fases (no prendas los 10 de una)

| Fase | Agentes | Por qué |
|---|---|---|
| **1 (semana 1)** | ANALISTA + JEFE | Primero hay que VER. Además hay que arreglar el pixel. |
| **2 (semana 2)** | SCOUT + ESPÍA | Empieza a entrar munición nueva. |
| **3 (semana 3)** | CREATIVO + TIKTOKER + INSTAGRAMER | Producción de contenido en volumen. |
| **4 (semana 4)** | MEDIABUYER + CONTENIDO + ATENCIÓN | Se cierra el ciclo completo. |

---

## 4. Lo que hay que resolver antes

- [ ] **Pixel de Meta dormido** — sin eventos, MEDIABUYER y ANALISTA trabajan a ciegas.
- [ ] **Checkout**: la opción "tarjeta" es PayPal y no procesa ARS → nunca se cobró una tarjeta.
      Esto es prioridad absoluta, no tiene sentido escalar tráfico a un checkout roto.
- [ ] Accesos: token Shopify Admin, token Meta Ads, API keys en `~/.hermes/.env` (hoy está vacío).
- [ ] Escribir `~/Claude/gonvra/CONTEXTO.md` con productos, costos, márgenes y tono de marca.

---

## 5. Qué NO hacer

- No 10 agentes desde el día 1 → ruido, tokens quemados, cero acción.
- No agentes que solo "investigan" sin entregable. Si no produce un archivo, no existe.
- No dejar que ningún agente gaste plata o publique sin aprobación humana.
- No leer 10 reportes por día. Solo el DAILY. Los demás quedan archivados por si se los quiere ver.
