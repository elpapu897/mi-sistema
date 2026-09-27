---
tags: [gonvra, arquitectura, manual, prompt-maestro]
actualizado: 2026-09-24
---

# 🗺️ GONVRA — Cómo funciona todo

> **Para qué sirve este archivo:** es el mapa completo del sistema. Sirve para
> entender qué hay, qué se puede pedir, y qué NO se puede (con el motivo verificado).
> **Si le vas a pedir una automatización nueva a un agente, pasale este archivo primero.**

---

## 1. EL NEGOCIO EN 30 SEGUNDOS

| | |
|---|---|
| Marca | **GONVRA** · gonvra.com · Argentina |
| Producto | Rasuradora Integral Recargable — Rostro y Cuerpo |
| Precio | **$36.900** (costo $8.672,90 → margen 76%) |
| Tienda | Shopify `jm60sa-cp.myshopify.com` |
| Instagram | **@gonvra1** (BUSINESS) |
| Mail | gonvra0@gmail.com · WhatsApp +54 9 11 5376-7293 |
| **Ventas hasta hoy** | **0** — porque no hubo tráfico, no por un problema técnico |
| **CPA techo** | **$7.129 por venta.** Por debajo de eso, se gana plata seguro |

**Matías no se graba y no tiene el producto físico.** Todo el contenido se hace con
las fotos reales + texto + voz en off.

---

## 2. LAS PIEZAS

```
        ┌──────────── TU LAPTOP (todo corre acá) ────────────┐
        │                                                     │
        │  HERMES  ──► 20 trabajos programados                │
        │    │           (12 agentes IA + 8 scripts)          │
        │    │                                                │
        │  n8n ──────► 7 automatizaciones visuales            │
        │    │           localhost:5678                       │
        │    │                                                │
        │  PORTERO ──► deja pasar SOLO /webhook               │
        │    │           (protege los tokens)                 │
        │    │                                                │
        │  TÚNEL ────► dirección pública de internet          │
        │                                                     │
        │  PANEL ────► localhost:8080 (Mission Control)       │
        └─────────────────────────────────────────────────────┘
              ▲                                    │
              │ avisan cuando pasa algo            │ actúan sobre
              │                                    ▼
        Shopify · Instagram                 Shopify · Instagram · Gmail
```

**6 servicios que arrancan solos con la compu** y se reinician si se caen:
`hermes-gateway` · `gonvra-n8n` · `gonvra-proxy` · `gonvra-tunel` · `gonvra-panel` · `gonvra-gmail-auth`

---

## 3. QUÉ PUEDE HACER EL SISTEMA (capacidades reales, probadas)

### 🛒 Shopify — acceso completo de lectura
- Leer **pedidos, clientes, carritos abandonados, productos, stock**
- **Escribir el tema** (via CLI): editar secciones, subir archivos
- **Registrar webhooks**: enterarse de cosas al instante
- ❌ No puede: políticas, páginas, subir a "Files" (falta permiso)

### 📸 Instagram — @gonvra1
- **Publicar fotos, carruseles (2-10) y reels** ✅ probado
- Leer perfil y publicaciones
- Mandar mensajes privados
- ❌ **No puede leer comentarios** (permiso pendiente en Meta — ver sección 6)

### 📧 Gmail — gonvra0@gmail.com
- Leer, buscar, etiquetar, **crear borradores**, enviar
- 15 herramientas disponibles

### 🎬 Contenido
- **ffmpeg** — armar y editar videos
- **ImageMagick** — componer placas
- **video-intel.py** — espiar videos de la competencia sin gastar tokens
- **Generar imágenes con IA** (Replicate) — US$0.003 la rápida, US$0.039 la buena
- **Generar video con IA** (Replicate) — US$0.28 un clip de 6s en 768p
  ⚠️ el video **cuesta plata**: exige `--confirmo` y corta a los US$3 por día

### 🕵️ Inteligencia
- **Espiar precios** de cualquier tienda Shopify (`/products.json` es público)
- Leer cualquier web con navegador real (Chromium instalado)

### 📢 Avisos
- **Telegram** — todo lo urgente llega ahí
- **Mission Control** — panel visual en localhost:8080

---

## 4. LO QUE YA CORRE SOLO

### Trabajos programados (20)

| Hora | Quién | Qué hace |
|---|---|---|
| 02:00 | ESPIA 🤖 | Espía competencia |
| 06:00 | ANALISTA 🤖 | Revisa números |
| 09:00 | COPY 🤖 | Escribe textos |
| 10:00 | TIKTOKER 🤖 | Guiones de video |
| 11:00 | INSTAGRAMER 🤖 | Carruseles e historias |
| 13:00 | CRO 🤖 | Mejoras de la ficha |
| 15:00 | CREATIVO 🤖 | Piezas visuales |
| 19:00 | CAZADOR 🤖 | Dónde está el público |
| 21:00 | JEFE 🤖 | **Único resumen diario** a Telegram |
| Lunes 16 | CREATIVO 🤖 | Estrategia Andrómeda para Meta Ads |
| Miérc 16 | TIKTOKER 🤖 | Prompts para Google Flow |
| cada 4 h | GUARDIA ⚙️ | Salud de la tienda (sin IA, $0) |
| cada 15 m | VENTAS ⚙️ | Avisa si entró un pedido |
| cada 20 m | WEBHOOKS ⚙️ | Mantiene viva la URL pública |
| cada 30 m | PANEL ⚙️ | Refresca los datos |
| cada 30 m | SEGURIDAD ⚙️ | Tapa credenciales en los chats |
| 08 y 20 | PRECIOS ⚙️ | Competencia: avisa si cambian |
| 11:00 | POSVENTA ⚙️ | Borradores de mail a clientes |
| 04:00 | BACKUP ⚙️ | Copia de todo (7 días) |
| 05:00 | LIMPIEZA ⚙️ | Borra archivos temporales |

🤖 = usa IA (cuesta tokens) · ⚙️ = script puro (cuesta $0)

### Automatizaciones n8n (7)

1. **Venta instantánea** — Shopify avisa → Telegram con dirección y qué comprar
2. **Carritos abandonados** — cada 3 h, con el mail ya redactado
3. **Reporte diario** — 20:00, ventas y plata parada
4. **Cola IG: avisar** — qué espera tu OK
5. **Cola IG: publicar** — publica lo aprobado
6. **Comentario → privado** — armado, esperando el permiso de Meta
7. **Errores** — si algo se rompe, te avisa

---

## 5. CÓMO SE PUBLICA (lo único manual)

```
~/GONVRA-PUBLICAR/
   1-PENDIENTE/   ← poné acá el contenido
   2-APROBADO/    ← movelo acá = tu OK
   3-PUBLICADO/   ← queda el historial
```

- **Foto:** `imagen.png` + `imagen.txt` (el texto)
- **Carrusel:** una **carpeta** con `01-x.png`, `02-y.png`... + `texto.txt` adentro
- **Reel:** `video.mp4` + `video.txt`

Cada 30 min te avisa qué hay esperando. Cada 10 min publica lo aprobado.
**Nada sale sin que muevas el archivo.**

---

## 6. LO QUE NO SE PUEDE (verificado, no insistir)

| Qué | Por qué | Cómo se soluciona |
|---|---|---|
| **Leer comentarios de IG** | Permiso `manage_comments` pendiente en Meta ("Acciones necesarias") | Completar lo que pide Meta |
| **Generar video con Veo/Flow gratis** | La API de Veo es solo pago; Flow web no tiene API | Se usa Replicate (hailuo-02), que sí funciona |
| **Publicar en TikTok** | Sin auditoría, los videos quedan privados | Subir a mano (3 min) |
| **Espiar Ad Library** | Anti-bot 403 | A mano en facebook.com/ads/library |
| **WhatsApp** | Trámite de Meta | Hermes tiene `whatsapp-cloud` listo |
| **Meta Ads** | Token de servicio pago + no hay ads corriendo | Cuando haya pauta |

---

## 7. REGLAS QUE NO SE ROMPEN

1. **Nada se publica ni se envía sin aprobación** de Matías
2. **Cero mentiras**: sin reseñas inventadas, sin escasez falsa, sin contadores truchos
3. **Sin promesas técnicas sin prueba**: nada de batería, potencia, impermeabilidad
4. **Las credenciales van en `~/.hermes/.gonvra-secrets.env`** (chmod 600), nunca en
   un entregable, un chat o Obsidian
5. **El catálogo se lee en vivo** de Shopify, nunca hardcodeado
6. **Todo dato del panel que se pueda verificar, se verifica.** Nada escrito a mano
7. **Antes de reintentar algo, leer `BITACORA-ERRORES.md`** (23 errores documentados)

---

## 8. 📝 CÓMO PEDIR UNA AUTOMATIZACIÓN NUEVA

Copiá esto y completá:

```
Quiero una automatización que:

QUÉ LA DISPARA:
  (  ) A una hora fija: ______
  (  ) Cada X tiempo: ______
  (  ) Cuando pasa algo en Shopify (venta, carrito, producto)
  (  ) Cuando pasa algo en Instagram
  (  ) Cuando aparece un archivo en una carpeta

QUÉ TIENE QUE HACER:
  (describilo en una frase, como se lo contarías a una persona)

CON QUÉ DATOS:
  (  ) Pedidos / clientes / carritos de Shopify
  (  ) Publicaciones de Instagram
  (  ) Mails de Gmail
  (  ) Precios de la competencia
  (  ) Lo que escribieron los agentes

CÓMO ME ENTERO:
  (  ) Telegram
  (  ) Borrador en Gmail
  (  ) Solo lo anota, sin molestarme
  (  ) Solo si hay algo raro

¿NECESITA MI APROBACIÓN ANTES DE ACTUAR?
  (  ) Sí, siempre      (  ) No, si es solo leer
```

**Antes de construir, el agente tiene que:**
1. Chequear en la sección 6 si algo lo bloquea
2. Decir qué **no** va a poder hacer y por qué
3. **Probarlo con datos reales** antes de decir que funciona
4. Anotar en `BITACORA-ERRORES.md` lo que se rompa

---

## 9. ARCHIVOS IMPORTANTES

```
~/Claude/gonvra2/
   COMO-FUNCIONA-TODO.md      ← este archivo
   CONTEXTO.md                ← lo que leen los 15 agentes
   BITACORA-ERRORES.md        ← 23 errores con causa y arreglo
   HACE-ESTO-MATIAS.md        ← lo que solo puede hacer Matías
   CONECTORES.md              ← APIs y MCPs
   RESUMEN-COMPLETO-handoff.md
   n8n-workflows/             ← los 7 flujos en JSON
   competencia.txt            ← tiendas a vigilar

~/GONVRA-PUBLICAR/            ← la cola de publicación
~/GONVRA-BACKUPS/             ← 7 días de copias
~/.hermes/scripts/gonvra-*    ← los scripts del sistema
```

---

## 10. LA VERDAD INCÓMODA

El sistema está completo: publica, vende, avisa, respalda y vigila.

**Pero todavía no vendió nada. Y no va a vender hasta que entre gente a la tienda.**

Ninguna automatización nueva cambia eso. Lo que lo cambia es **publicar seguido**:
3 posts en Instagram es un arranque, no una estrategia. El sistema ya deja el contenido
listo todos los días — lo único que falta es aprobarlo y que salga.

**Si tenés que elegir entre una automatización más o publicar 5 videos esta semana,
elegí publicar.**
