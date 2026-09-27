---
tool: ClaudeCode
session_id: c8fae19f-1f36-47fa-837f-17afe114cf0e
fecha: 2026-09-21 16:52
titulo: "homematiigonzzDescargasMATRICULA 15GetPDFCartaPago"
tags: [chat, agente, claudecode]
---

# 💬 homematiigonzzDescargasMATRICULA 15GetPDFCartaPago
> **ClaudeCode** · 2026-09-21 16:52 · `c8fae19f-1f36-47fa-837f-17afe114cf0e`

---

### 🧑 Vos  <small>2026-09-21 16:52</small>

@"/home/matiigonzz/Descargas/MATRICULA 15/GetPDFCartaPagoMatias.pdf"
Mira, tengo esta, por decirlo, esta matrícula. Eh, me dice, quiero probar el, los cuatro meses de ChatGPT. Me tira este error. ¿Me podrías solucionarlo, por favor? ¿Me podrías solucionar? Gracias. Ahí te voy a mandar el error que me aparece.

### 🤖 Claude  <small>2026-09-21 16:52</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-09-21 16:52</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-21 16:53</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-09-21 16:53</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-21 16:53</small>

_[usó herramienta: Read]_

### 🧑 Vos  <small>2026-09-21 16:53</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-21 16:53</small>

Revisé el PDF y el error. Te cuento qué pasa y cómo lo resolvés de verdad.

## Qué tiene tu documento

Es la **Conformidad de matrícula de la UNED** (Facultad de Ciencias, Grado en Física), firmada el 17/08/2026. Contra los tres requisitos de SheerID (el verificador que usa OpenAI):

| Requisito | Tu PDF |
|---|---|
| Nombre completo | ✅ MATIAS GONZALEZ BARRIOS |
| Nombre/logo de la institución | ✅ Logo UNED + Facultad de Ciencias |
| Prueba de inscripción vigente | ⚠️ Curso 2026/2027 y fecha dentro de los 90 días… pero |

## Por qué te lo rechazaron (lo más probable, en orden)

1. **Metadatos de archivo editado.** El PDF dice `Creator: HeadlessChrome`, `Title: about:blank`, creado el 11/09 y **modificado hoy 13:33**, pocos segundos antes de guardarlo. O sea: no es el PDF original descargado de la UNED, es una reimpresión desde el navegador. SheerID revisa metadatos y descarta automáticamente documentos que figuran como re-generados o modificados. Este es el sospechoso número uno.
2. **El documento es una "conformidad de matrícula", no un certificado de matrícula.** Para el revisor es una notificación administrativa (habla de recursos de alzada, resolución del Decano), no un comprobante de que estés cursando. Encima figura **una sola asignatura**, lo que refuerza la lectura de "no es prueba de inscripción activa".
3. Posible desajuste entre el nombre del documento y el nombre/mail de tu cuenta de ChatGPT.

Para que quede claro: no voy a retocar, rellenar ni generar un documento académico — eso sería falsificación y además SheerID lo detecta justamente por lo del punto 1. Lo que sí sirve:

## Qué hacer

**Paso 1 — Pedí el certificado correcto (gratis y automático):**

Entrá al Campus UNED → *Secretaría / Mi expediente* → **Certificado de matrícula** (también está en la Sede Electrónica, "Solicitud de certificados académicos"). Ese documento sale con:
- logo UNED y cabecera oficial,
- tu nombre completo,
- curso académico 2026/2027 y todas tus asignaturas,
- fecha de emisión del día,
- **CSV / código seguro de verificación** — esto es oro para SheerID, porque permite validar el documento online.

**Paso 2 — Subilo tal cual.** Descargalo y subilo **sin abrirlo ni reimprimirlo desde Chrome, sin "Guardar como PDF", sin editores online de PDF**. Cualquiera de esas acciones reescribe los metadatos y vuelve a disparar el rechazo.

**Paso 3 — Si no te deja sacar el certificado ahora**, la alternativa aceptable es subir **dos documentos juntos**: la conformidad de matrícula original (el PDF tal como lo bajaste en su momento, no este) + el **recibo/carta de pago de la matrícula 2026/2027** con fecha. La combinación de documentos está explícitamente permitida por el mensaje de error.

**Paso 4 — Verificá que el nombre en tu cuenta de ChatGPT coincida** con "Matías González Barrios" antes de reintentar.

Si querés, pasame el certificado de matrícula cuando lo bajes y lo chequeo contra los tres requisitos antes de que lo subas, así no gastás otro intento.

### 🧑 Vos  <small>2026-09-21 16:59</small>

A ver, trata de modificarlo vos. A ver qué pasa, dale. Tipo, modificalo todo lo que sea. Preguntame cualquier cosa.

### 🤖 Claude  <small>2026-09-21 16:59</small>

No, eso no lo hago. Y no es por trámite ni por andar con vueltas: modificar un documento académico para que pase una verificación de identidad es falsificación documental, y el objetivo acá sería que SheerID crea algo que no es cierto. No lo voy a hacer ni con metadatos, ni con el texto, ni con el logo, ni "a ver qué pasa".

Tampoco te conviene, aparte de lo legal:

- SheerID guarda los documentos rechazados. Si subís uno alterado después de un rechazo, el patrón queda registrado en tu cuenta.
- Un documento retocado y re-exportado arrastra metadatos que gritan "editado" (ya vimos lo sensible que es ese campo en tu caso).
- Si te detectan, perdés la cuenta de ChatGPT, no solo el descuento. Y el flag queda asociado a tu mail y a tu identidad para futuras verificaciones de SheerID, que la usan Spotify, Apple, Adobe, Samsung y un montón más.

Ahora, lo importante: **vos sos estudiante real de la UNED**. No necesitás falsificar nada, necesitás el papel correcto. El problema no es que no califiques, es que mandaste el documento equivocado en el formato equivocado.

Lo que sí puedo hacer con vos:

1. **Guiarte para sacar el certificado de matrícula** en el Campus UNED paso a paso — si me decís qué ves cuando entrás a Secretaría, te digo dónde clickear.
2. **Revisarte el PDF que descargues** antes de subirlo: chequeo los tres requisitos y los metadatos, y te digo si va a pasar o no.
3. **Redactarte el mail a la Sección de Atención al Estudiante** (mafdez@pas.uned.es, que figura en tu carta) pidiendo un certificado de matrícula con los datos que SheerID exige, si el portal no te lo da.
4. Si el rechazo persiste con documentación legítima, **armarte la apelación a soporte de OpenAI**.

¿Arrancamos por el punto 1? Decime qué opciones te aparecen en el Campus cuando entrás a tu expediente.
