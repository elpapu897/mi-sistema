> 📋 **Resumen completo del proyecto:** `~/Claude/gonvra2/RESUMEN-COMPLETO-handoff.md`
> (también en Obsidian: `08-Proyectos-Reales/tiendas/GONVRA - RESUMEN COMPLETO (handoff).md`)

# CONTEXTO GONVRA — memoria compartida del equipo (VERSIÓN VIGENTE)

> 🗺️ **Mapa completo del sistema:** `~/Claude/gonvra2/COMO-FUNCIONA-TODO.md`
> Ahí está qué se puede hacer, qué no, y por qué. **Leelo antes de proponer
> una automatización nueva**, así no proponés algo que ya se probó que no anda.

> ⚠️ **ESTE ARCHIVO REEMPLAZA A `~/Claude/gonvra/CONTEXTO.md`**, que quedó obsoleto (era del nicho
> viejo de mascotas). Todo agente lee ESTE archivo antes de trabajar.
> Última actualización: 2026-09-22

---

## 🔴 CAMBIO DE NICHO (leer primero)

Matías **cambió de nicho y de producto**. Ya **NO** se venden artículos para mascotas.
La marca **GONVRA se mantiene** (mismo dominio, mismo nombre), pero ahora el rubro es
**cuidado personal masculino**. Ignorar todo lo anterior sobre perros, gatos, camas, cepillos y
combos. La tienda de mascotas (`9em58g-tt.myshopify.com`) **ya no se toca**.

---

## 1. El negocio

- **Marca:** GONVRA · **Web:** gonvra.com
- **Tienda Shopify:** `jm60sa-cp.myshopify.com` · admin: `admin.shopify.com/store/jm60sa-cp`
- **País / moneda:** Argentina, ARS
- **Dueño:** Matías. **No técnico.** Hablarle en español rioplatense, sin jerga, sin "tú".
- **Contacto público:** `gonvra0@gmail.com` · WhatsApp **+54 9 11 5376-7293**
- **Estado real:** ventas prácticamente en cero. Esto es una tienda que hay que **ARRANCAR**,
  no optimizar.

## 2. El producto (UNO SOLO)

- **Título:** Rasuradora Integral Recargable — Rostro y Cuerpo
- **Precio:** **$36.900 ARS**
- **Handle:** `face-body-electric-shaver` → `gonvra.com/products/face-body-electric-shaver`
- **Variante:** Negro y verde lima
- **Qué es:** una sola máquina para **cara y cuerpo** — barba, patillas, pecho, brazos, piernas y
  zona íntima. Peines regulables para elegir el largo. Recargable.
- **Público:** hombres argentinos que hoy usan varios aparatos distintos o van a la peluquería.
- ⚠️ El inventario declarado es 50.000 (valor por defecto del proveedor, no es stock real).
  **No usarlo para escasez.**

### Promesas REALES (solo estas se pueden afirmar)
- ✅ **Envío gratis a todo el país**, con seguimiento.
- ✅ **Garantía 10 días** y **arrepentimiento 10 días corridos** (Ley 24.240).
- ✅ Despacho 24-48 h hábiles · entrega estimada 12-20 días.
- ✅ Pago con tarjeta o Mercado Pago.
- ❌ **Prohibido** inventar: escasez falsa, contadores truchos, reseñas inventadas, cifras de
  batería o potencia que no estén confirmadas.

## 3. Tema y web

- **Tema LIVE:** `GONVRA — Landing de vista previa` **#148158414963**
- Proyecto local del tema: `~/Documents/Codex/tiendas/jm60sa-cp/live-theme`
- Secciones propias con prefijo `gv-` (gv-header, gv-footer, gv-faq, gv-comparativa, gv-antes,
  gv-datos, gonvra-product-landing, etc.)
- **Acceso real desde Claude Code:** el Shopify CLI está autenticado para esta tienda.
  - ✅ SE PUEDE: leer productos, y **leer/escribir el TEMA** (`npx shopify theme pull/push
    --store jm60sa-cp.myshopify.com --theme 148158414963`)
  - ❌ NO SE PUEDE (el token no tiene scope): **políticas, páginas, temas por Admin API**.
    Eso lo hace Matías a mano en el panel.

### Hecho el 2026-09-07 (ya está en vivo, verificado)
- ✅ **Botón de arrepentimiento** agregado a la columna Legal del footer (obligatorio por ley AR).
- ✅ **WhatsApp flotante activado** (`wa_number: 5491153767293`).
- ✅ **Mail y teléfono visibles** en el footer, clickeables (bloque `.gvft-contacto`).

## 4. ✅ HECHO Y VERIFICADO EN VIVO (2026-09-07) — NO volver a proponerlo

| Ítem | Estado |
|---|---|
| **Checkout / Mercado Pago** | ✅ **FUNCIONA.** Única opción: Mercado Pago Tarjetas. PayPal desactivado. El rechazo fue por fondos insuficientes = la pasarela funciona bien. |
| **Política de envío** | ✅ publicada (HTTP 200) |
| **Política de reembolso** | ✅ publicada (200) — arrepentimiento + garantía 10 días + mail |
| **Términos del servicio** | ✅ publicada (200) |
| **Política de privacidad** | ✅ publicada (200) |
| **Nombre de la tienda** | ✅ **GONVRA** (ya no dice "Mi tienda") |
| **Dominio** | ✅ gonvra.com apuntando a esta tienda |
| **Botón de arrepentimiento** | ✅ en el footer, columna Legal |
| **WhatsApp flotante + mail/teléfono en footer** | ✅ activos y clickeables |
| **Instagram** | ✅ creado |

🚫 **Ningún agente debe volver a listar lo de arriba como pendiente.** Si duda, que lo verifique
en vivo con `curl` antes de afirmar que algo falta.

## 5. ℹ️ Sobre las "0 ventas" — NO es un problema, NO alarmarse

La tienda tiene 0 pedidos porque **es nueva y todavía no hay tráfico**: no se subió ningún video,
no hay publicidad, no hay campañas. Es lo esperable.
- El rechazo del 8/9 ($129.475) fue por **fondos insuficientes**, no por configuración.
- ⇒ **El checkout funciona.** No hay nada que arreglar ahí.
- ⇒ El `Purchase` no aparece en Meta simplemente porque **todavía no hubo ninguna venta**.
🚫 **Ningún agente debe tratar las 0 ventas como un bug ni volver a "investigar el checkout".**

## 6. ⏳ Otros pendientes

1. **Píxel de Meta — RESUELTO según confirmación de Matías en el arranque del equipo.** Píxel `3919766821491073` conectado a cuenta de anuncios `2487859205019090`, activa, ARS y con medio de pago. No reabrir auditoría; ya se pueden preparar campañas, siempre EN PAUSA.
2. **Que llegue el pedido de prueba** — comprado, falta confirmar la entrega; no bloquea preparar contenido.
3. **Publicidad** — orgánico gratis primero. Antes de gastar: PRECIOS calcula margen/CPA máximo y Matías aprueba acción exacta por Telegram con SEMÁFORO y revalidación. No activar ni gastar automáticamente.

### Equipo y operación vigente (confirmado 2026-09-14)
- Activos: JEFE, ANALISTA, GUARDIA, CRO, CAZADOR, PRECIOS, COPY, CREATIVO, TIKTOKER, INSTAGRAMER, ESPIA, MEDIABUYER, TIENDA, MENSAJERO, LEGAL.
- Pausados: SCOUT, PODADOR, AUTODS, MARKETPLACES, PROVEEDORES, AOV, RECOMPRA, COMUNIDAD, CREADORES, CONTENIDO, DISEÑO, TESTER, FINANZAS, ESTRATEGA, BIBLIOTECARIO. Perfil auxiliar gonvra-shopify también pausado, fuera del equipo activo.
- Fase 1: COPY, TIKTOKER, INSTAGRAMER y ESPIA producen borradores listos para aprobar, no auditorías.
- JEFE: UN resumen diario a las 21:00 Argentina por Telegram. Aviso único adicional autorizado cuando los cuatro entregables iniciales estén listos, con limitaciones explícitas.
- Infraestructura existente se conserva: gateway único, Kanban gonvra y SEMÁFORO en `~/Claude/gonvra/semaforo/`. Contexto comercial viejo no se usa.
- Ninguna publicación, mensaje comercial, gasto ni cambio del tema publicado sin OK de Matías por Telegram. Las capacidades técnicas del CLI descriptas arriba NO autorizan escribir en LIVE.


## 🔧 CAMBIOS EN EL TEMA LIVE — 19/09/2026 (hechos por Claude Code, verificados en vivo)

⚠️ **La copia local del tema estaba desactualizada (del 07/09).** Antes de tocar el tema, SIEMPRE
hacer `theme pull` primero. Un agente dio por hecho que una sección existía cuando ya había sido
borrada del live.

Cambios aplicados al tema **#148158414963** (LIVE):
1. **Olas (`gv-wave`) responsive:** en PC se veían estiradas como manchones. Se bajó la altura y se
   suavizó la opacidad en pantallas ≥900px (`assets/gv-wave.css`).
2. **Ola sobrante apagada:** la sección `historia` ("Cómo usar") no tenía el ajuste `wave` guardado
   y tomaba el default `true` con un color que no pegaba. Se puso `wave: false`.
3. **Sección "Antes y después" (`gv-antes`) restaurada en la HOME** — había sido borrada del live.
   Orden home: `portada · antes · numeros · historia · preguntas`.
4. **"Antes y después" agregado a la PÁGINA DE PRODUCTO**, debajo de "Cómo usar" (sin ola).
   Orden producto: `ficha · numeros · historia · antes · resenas · preguntas`.
5. **Packs restaurados en la ficha:** `Individual` · `Dúo` (-10%, etiqueta "Más elegido") ·
   `Trío` (-15%). Aplicado a `product.gonvra.json`, `product.json` y `product.tienda.json`.
   ⚠️ Los porcentajes son provisorios, **Matías tiene que confirmarlos**.
6. ⏳ **Pendiente:** Matías va a pasar imágenes reales de antes/después. Hoy están las genéricas.
   Ojo legal: si no son del producto real, mantener la aclaración de "imágenes ilustrativas".

📌 **Plantilla real de la ficha: `product.tienda.json`** (no `product.json`).

## 7. Economía (para PRECIOS y MEDIABUYER)

- Ticket: **$36.900**. Antes de pautar, PRECIOS debe calcular el margen real
  (precio − costo − comisión Mercado Pago − impuestos − envío) y de ahí el **CPA máximo**.
- Mínimo por conjunto en Meta: ~$1.500/día.
- **Regla dura:** MEDIABUYER arma campañas **siempre en PAUSA**. Nunca gasta, nunca despausa,
  nunca sube presupuesto sin el OK de Matías por Telegram.

## 7. Herramientas del equipo

- **Entregables:** cada agente escribe en `~/Claude/gonvra2/<agente>/AAAA-MM-DD.md`
- **Espía de videos (ahorra tokens):** `python3 ~/Claude/scripts/video-intel.py "<URL>"`
  (datos + transcripción sin bajar el video) y `--scan 20` para escanear un canal barato.
- **Memoria entre agentes:** los chats de Claude Code, Codex y Hermes se exportan solos a
  `~/OBSIDIAN/07-Agentes/<Herramienta>/chats/` cada 30 min.

## 8. Tono de marca

Cercano, argentino, honesto, directo. Le habla a un tipo que quiere resolver su afeitado sin
vueltas. El diferencial NO es el precio: es **envío gratis + garantía de 10 días + atención real
por WhatsApp**. Cero urgencia falsa, cero promesas que no se cumplen.

---

## 🔌 CONECTORES DISPONIBLES — actualizado 22/09/2026

**Ya no hay que pedirle datos a Matías para estas cosas. Están conectadas y probadas.**
Las credenciales viven en `~/.hermes/.gonvra-secrets.env` (chmod 600).
**NUNCA copiar un token a un entregable, a un chat ni a Obsidian.**

| Conector | Estado | Qué se puede hacer |
|---|---|---|
| **Shopify Admin API** | ✅ | Leer **pedidos**, clientes, **carritos abandonados**, productos, stock |
| **Gmail** | ✅ | Leer, buscar, etiquetar y redactar desde `gonvra0@gmail.com` |
| **Instagram** | ✅ | Publicar en **@gonvra1** (BUSINESS). Token vence ~20/11/2026 |
| **Search Console** | ✅ | gonvra.com verificado |
| **Ad Library de Meta** | 🟡 | Instalado pero Meta lo bloquea (403). **Espiar a mano** en facebook.com/ads/library |
| TikTok / Meta Ads | ❌ | No conectados a propósito |

### Datos REALES de la tienda (leídos de la API el 22/09 02:40)
- **Pedidos: 0.** Facturado: $0. Sigue sin haber ventas porque **no hubo tráfico**.
- **1 carrito abandonado de $129.475 del 8/09 → es una PRUEBA que hizo Matías.**
  No es un cliente real. **No armar campañas de recuperación con eso ni contarlo como lead.**
- **1 "cliente"** registrado: es la misma prueba. 0 pedidos, $0 gastado.
- Precio vivo: **$36.900** · precio tachado: **$64.737,52** (era el precio viejo).

### Avisos automáticos que ya existen (no rehacerlos)
- **Ventas cada 15 min** → si entra un pedido, Telegram automático. `gonvra-ventas.sh`
- **Salud de la tienda cada 4 h** → `gonvra-guardia.sh` (sin LLM, $0)
- **Panel cada 30 min** → `mission-control`
- **Seguridad cada 30 min** → tapa credenciales que se cuelen en los chats

### Para publicar en Instagram
La API necesita que la imagen/video esté en una **URL pública**. Las placas están en
`~/Claude/gonvra2/creativo/` (local). **Antes de publicar hay que subirlas a algún lado
accesible.** Eso todavía no está resuelto: plantearlo como tarea, no asumir que se puede.

---

## 🚨 LO ÚNICO QUE FALTA PARA VENDER

El sistema está completo y esperando. **No falta ninguna herramienta.**
Falta **publicar contenido**: el video 1 (`~/Claude/gonvra2/videos/`) sigue sin publicar.

Matías **no se graba** y **no tiene el producto físico**: todo contenido debe ser
fotos reales + texto en pantalla + voz en off.
