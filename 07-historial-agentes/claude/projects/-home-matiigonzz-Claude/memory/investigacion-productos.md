---
name: investigacion-productos
description: "Pipeline de búsqueda de productos ganadores (salud/belleza/cuidado personal); AutoDS no conectado, AliExpress rate-limitea"
metadata: 
  node_type: memory
  type: project
  modified: 2026-08-23T22:43:18.201Z
  originSessionId: ce94d2a5-8cac-49f3-81e6-b499254a8b72
---

Proyecto en **`~/Claude/investigacion-productos/`**: buscar productos ganadores de salud, belleza y cuidado personal (coste 5-30 USD, vendibles a 3x, chicos, que ya vendan) y mostrarlos en un dashboard interactivo.

## Acceso a datos — lo que hay que saber antes de intentar de nuevo

**El conector de AutoDS NO está disponible.** Figura en la cuenta de claude.ai como `claude.ai autods` (id `mcpsrv_01UqhDTK25QpDR7opXsU8ADc`) pero aparece en `~/.claude/mcp-needs-auth-cache.json` = sesión OAuth caída. Las herramientas MCP se cargan **sólo al arrancar la sesión**, así que reconectar a mitad de sesión no sirve: hay que reconectar y **después** abrir una sesión nueva. En `~/.hermes/profiles/gonvra-autods/` hay un perfil de Hermes con ese nombre, pero **es sólo una personalidad de agente, no tiene credenciales ni API de AutoDS**.

**Plan B = AliExpress** (es el catálogo que alimenta a AutoDS). Dos aprendizajes caros:
- **La cabecera `Cookie` dispara el muro anti-bot** (`_____tmd_____/punish`, respuesta de ~2,4 KB en vez de ~650 KB). El pedido *limpio* (sólo User-Agent + Accept-Language + Accept) pasa. Por eso no se puede forzar USD por cookie; los precios vienen en **ARS con `taxRate` 0.21 incluido** y hay que convertir (`ars / (1+tax) / fx`).
- **La concurrencia mata**: 4 workers en paralelo dejaron la IP marcada. Hay que ir **secuencial y lento** (≥5 min entre pedidos). La IP residencial se bloquea rápido y tarda en soltar.

## Qué campos existen y cuáles no

Del buscador salen **datos reales**: precio, `trade.tradeDesc` (ventas, sólo en ~73% de los items), `evaluation.starRating` (sólo ~46%), descuento, `lunchTime`, y los tags de la tarjeta (`choice_atm` = AliExpress Choice, free shipping, "Top ventas").

**NO existe el tiempo de envío** en los resultados de búsqueda. Tampoco la competencia. Si alguien pide esas columnas, se estiman y **se marcan como estimación** — no se inventan.

## Archivos

`collect.py` (recolector lento y reanudable, guarda estado en `collect_state.json`), `pipeline.py` (normaliza + filtra + puntúa; acepta `--csv` de una exportación de AutoDS y autodetecta columnas), `build_dashboard.py` → `dashboard.html`, `raw.jsonl` (crudo), `products.json` (procesado), `LEEME.md`.

## Criterio de honestidad (importante para este usuario)

El dashboard separa explícitamente **DATO real** (coste, ventas, rating, Choice) de **MODELO/supuesto** (PVP, margen, competencia, nicho, tipo). El multiplicador de precio es **editable en el dashboard** para que el margen no sea un número inventado por el asistente. Los productos **sin dato de ventas se descartan**, no se asumen. Esto está alineado con el SOUL.md de GONVRA: "no inventes reseñas, escasez, descuentos, stock, promesas ni resultados".

**La vía rápida y correcta es que el usuario exporte el CSV desde AutoDS** (tiene costo y envío reales) y correr `python3 pipeline.py --csv archivo.csv`.

## Criterios nuevos del usuario (2026-08-23, ronda 2)

Rechazó las dos primeras recomendaciones. Lo que pide ahora:

- **Urgencia real, no "compra boluda".** Que el comprador sienta "con esto no puedo vivir" / "me cambia la vida". El antifaz Bluetooth lo bochó con una objeción válida: *"para escuchar música me pongo unos auriculares comunes"* — cero urgencia.
- **Público amplio.** No nichos chicos. Le da igual que el público sea femenino, pero tiene que ser masivo.
- **Sin riesgo de daño físico.** Bochó el limpiador de oídos por chico y peligroso, y desconfía de los aparatos eléctricos sobre el cuerpo ("me puedo electrocutar").
- Ideas que trajo él: **relojes/pulseras que miden ritmo cardíaco y pasos**, **cosas para bebés**, y (de sus amigos) planchitas/rizadores/difusores.
- **Pidió explícitamente que NO le dé siempre la razón.** Quiere contra-argumentos, no complacencia.

**Reencuadre que le di:** los productos de verdad imprescindibles se venden en el supermercado o la farmacia baratos — eso choca con sus propios criterios 2 y 3. Lo que convierte no es *necesidad* sino **dolor agudo + solución visible + alternativa cara** (dentista, kinesiólogo, dermatólogo). Ese es el filtro correcto.

Archivo `urgencia.txt` = 35 consultas nuevas (dolor crónico, bebés, wearables, herramientas de pelo) para tener datos sobre lo que él propuso.
