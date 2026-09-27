---
tags: [gonvra, resumen, balance]
actualizado: 2026-09-24
---

# 📊 GONVRA — Resumen de todo lo que construimos

> Del 21 al 24 de septiembre de 2026. Todos los números están verificados
> contra el sistema real, no son estimaciones.

---

## 1. DÓNDE EMPEZAMOS

El 21 de septiembre el proyecto estaba así:

| | |
|---|---|
| Servidor | **Caído** (VPS de 1 GB, se ahogó) |
| Agentes | **15 en papel**, pero la "grilla 24/7" **nunca existió** — había 1 solo cron |
| Panel | Datos **congelados hacía un día**, mostraba horarios inventados |
| Conectores | **Ninguno** funcionando |
| Instagram | **0 publicaciones** |
| Contenido | 5 placas y 1 video hechos, **sin publicar** |
| Ventas | 0 |

**El diagnóstico del primer día:** no faltaban herramientas, faltaba que algo
saliera a la calle.

---

## 2. DÓNDE ESTAMOS HOY

```
6 servicios activos, arrancan solos con la compu
30 trabajos programados
8 automatizaciones en n8n
3 conectores (Shopify · Instagram · Gmail)
31 scripts propios
6 publicaciones en Instagram
24 errores documentados con su causa y su arreglo
```

**Ventas: 0.** Sigue siendo el número que importa y todavía no se movió.

---

## 3. LO QUE SE CONECTÓ

| Conector | Estado | Qué destraba |
|---|---|---|
| **Shopify** | ✅ | Pedidos, clientes, carritos, productos, webhooks |
| **Instagram** | ✅ | Publica fotos, carruseles y reels en @gonvra1 |
| **Gmail** | ✅ | 15 herramientas, borradores automáticos |
| **Replicate** | ✅ | Imágenes US$0.003 · video US$0.28 |
| **Search Console** | ✅ | Ya estaba verificado |
| **Túnel público** | ✅ | Webhooks desde internet, con el panel blindado |
| Ad Library | 🟡 | Instalado pero Meta lo bloquea |
| Comentarios IG | 🟡 | Falta un permiso pendiente en Meta |
| Meta Ads | ⬜ | Script listo, falta que corras el OAuth |
| TikTok | ⬜ | Sin auditoría, la cuenta tendría que estar privada |
| WhatsApp | ⬜ | Para mañana |

---

## 4. LO QUE CORRE SOLO

### Contenido
- **6 agentes** escriben todos los días: guiones, copys, carruseles, estrategia
- **Fábrica de placas**: convierte el texto del agente en imágenes reales
- **Cola de publicación**: te avisa, aprobás con un toque desde el celular, se publica
- **Aprendizaje semanal**: cruza qué publicaste con cómo le fue

### Plata
- **Venta instantánea**: webhook de Shopify → Telegram en el momento
- **Carritos abandonados**: 3 toques (2 h, 20 h, 44 h) con el mail redactado
- **Posventa**: gracias, despacho, tips y pedido de reseña
- **Protocolo de primera venta**: muestra qué publicaste los 7 días previos

### Vigilancia
- **Salud de la tienda** cada 4 h (sin IA, $0)
- **Ficha de producto**: alerta si cambia el precio, el link o las fotos
- **Precios de la competencia** dos veces por día
- **CRO visual**: mira la ficha como la ve un cliente, no el HTML
- **Watchdog general**: avisa si un agente dejó de correr en silencio
- **Guardián del túnel**: ping real desde afuera, se repara solo

### Protección
- **Backup diario** de todo (7 días de historial)
- **Tapa credenciales** que se cuelen en los chats
- **Limpieza** de archivos temporales
- **Tope de gasto** en Replicate: US$3 por día

---

## 5. LOS PROBLEMAS QUE ENCONTRAMOS

**24 errores documentados.** Los que más tiempo ahorraron para el futuro:

1. **El panel mentía.** Los datos estaban escritos a mano: mostraba agentes
   trabajando a horas que no existían y herramientas en verde que estaban rotas.
   Ahora 9 de 13 se verifican en vivo.

2. **Casi expongo n8n entero a internet.** Puse el portero en un puerto que ya
   usaba n8n; el portero no arrancó pero systemd decía "active". El túnel quedó
   apuntando al panel con todos los tokens adentro. Lo detecté probando el
   filtro de verdad, no mirando el estado del servicio.

3. **Las instrucciones de Shopify estaban obsoletas.** El menú que te mandé a
   buscar fue eliminado por Shopify. Perdiste tiempo por eso.

4. **20 credenciales tuyas en texto plano** en los chats exportados a Obsidian.

5. **El carrusel fallaba por una coma.** Python codificaba `children=id1,id2`
   como `%2C` e Instagram no lo reconocía.

6. **Los comentarios de Instagram no llegan** porque al token le falta un
   permiso — no porque la configuración esté mal, que es donde estuvimos
   mirando un rato largo.

---

## 6. LO QUE APRENDIMOS A NO HACER

1. **No afirmar sin verificar.** Varias veces di algo por hecho y estaba mal.
2. **`is-active` puede mentir.** Hay que mirar quién tiene el puerto.
3. **Nunca dar comandos con huecos** tipo `TU_CLIENT_ID`: se copian literal.
4. **Los links de OAuth vencen** en minutos: no mandarlos por chat.
5. **Todo dato que se pueda verificar, se verifica.** Nada escrito a mano.
6. **Probar de punta a punta** antes de decir que algo funciona.

---

## 7. LA VERDAD, SIN ADORNOS

Construimos un sistema que publica, vende, avisa, respalda y se repara solo.
**Y no vendió nada.**

No es un fallo del sistema: es que **entraron cero visitas a la tienda**.
Ninguna automatización nueva cambia eso.

Los números de Instagram lo dicen todo:

```
6 publicaciones · 2 interacciones en total
```

Con ese volumen no hay nada que optimizar todavía. **Lo único que mueve la aguja
es publicar seguido.** El sistema ya deja el contenido listo todos los días y
aprobarlo son dos toques desde el celular.

**Si tuvieras que elegir una sola cosa para esta semana: publicá 5 videos.**
No hace falta ninguna herramienta más.

---

## 8. LO QUE FALTA

### Tuyo (10 minutos en total)
- [ ] Correr `sacar-token-meta.py` → destraba Meta Ads y la Ad Library oficial
- [ ] El comando de `sudo` para que la compu no duerma con la tapa cerrada
- [ ] Ver qué pide Meta en "Acciones necesarias" para el permiso de comentarios

### Mío, cuando digas
- [ ] WhatsApp (mañana)
- [ ] Arreglar el **botón de compra invisible en celular** (el hallazgo más
      caro del CRO visual: el cliente ve el precio y no tiene dónde pagar)
- [ ] URL fija con `hooks.gonvra.com` en vez de la temporal

---

## 9. ARCHIVOS PARA ORIENTARSE

| Archivo | Para qué |
|---|---|
| `COMO-FUNCIONA-TODO.md` | Mapa completo del sistema y cómo pedir cosas nuevas |
| `BITACORA-ERRORES.md` | Los 24 errores con causa y arreglo |
| `HACE-ESTO-MATIAS.md` | Lo que solo podés hacer vos |
| `CONECTORES.md` | APIs, links verificados y qué MCP usar |
| `TIKTOK-PASO-A-PASO.md` | Por qué TikTok no conviene todavía |
| `conocimiento/QUE-FUNCIONA.md` | Qué contenido rinde (lo leen los agentes) |
