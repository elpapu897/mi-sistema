# GONVRA 24×7 — tokens y costos estimados

Consulta: **2026-09-19T16:58:13.379550-03:00**. Alcance: investigación de solo lectura; no se creó, activó ni cambió ningún cron, modelo o perfil. Las únicas entregas son este informe y `costs.json`.

## Resumen para decidir

- **Plan pedido: 16 sesiones por día; 17 los viernes; 113 por semana.** Una sesión no es una llamada: presupuestamos 3–10 llamadas LLM por sesión.
- **Gemini con cache efectiva:** USD **0.1317–0.3555 por día común**; viernes **0.1376–0.3705**. Equivalente de 30 días: **USD 3.9763–10.7306**. Punto central: **USD 6.71/30 días**.
- **Sin aciertos de cache Gemini**, manteniendo la misma cantidad de texto y turnos: USD **0.2829–1.3478/día común**, o **8.5431–40.7006/30 días**. Es la referencia prudente hasta medir Gemini real.
- **Alternativa liviana:** USD **2.32–6.64/30 días con cache**, o **4.91–24.26 sin cache**. Conserva margen diario para producción, aunque se omite cuando no hay novedades.
- **Estos USD son solamente API Gemini, NO el costo total del equipo.** COPY, CRO y JEFE consumen la suscripción/los límites de Codex. No hay una tarifa pública por token verificada acá para `gpt-5.6-sol`; no la invento ni convierto sus tokens a USD. `null` en JSON significa no determinado, nunca “gratis”.

## 1. Calendario solicitado

| Rol | Modelo / proveedor | Frecuencia | Sesiones/semana |
|---|---|---|---:|
| GUARDIA | `gemini-2.5-flash-lite/gemini` | 7/día: 00, 04, 08, 12, 16, 20, 22 | 49 |
| ANALISTA | `gemini-2.5-flash-lite/gemini` | 1/día | 7 |
| CAZADOR | `gemini-2.5-flash-lite/gemini` | 1/día | 7 |
| LEGAL | `gemini-2.5-flash-lite/gemini` | Viernes | 1 |
| ESPIA | `gemini-2.5-flash/gemini` | 1/día | 7 |
| TIKTOKER | `gemini-2.5-flash/gemini` | 1/día | 7 |
| INSTAGRAMER | `gemini-2.5-flash/gemini` | 1/día | 7 |
| CREATIVO | `gemini-2.5-flash/gemini` | 1/día | 7 |
| COPY | `gpt-5.6-sol/openai-codex` | 1/día | 7 |
| CRO | `gpt-5.6-sol/openai-codex` | 1/día | 7 |
| JEFE | `gpt-5.6-sol/openai-codex` | 1/día | 7 |

Desglose: día común = 9 Lite + 4 Flash + 3 Sol. Viernes = 10 Lite + 4 Flash + 3 Sol. Semana = 64 Lite + 28 Flash + 21 Sol. No se agregaron PRECIOS, TIENDA ni otros roles al calendario: sus sesiones se usan solamente como referencia histórica.

## 2. Evidencia real: no estamos partiendo de prompts diminutos

Se abrieron las cuatro `state.db` con URI SQLite `mode=ro` y `PRAGMA query_only=ON`. Muestra: hasta seis sesiones con consumo por perfil, ordenadas por inicio descendente; se encontraron estas filas:

| Perfil / sesión | Modelo histórico | Llamadas | Entrada sin cache | Cache leída | Salida |
|---|---|---:|---:|---:|---:|
| gonvra-cro / `20260919_163719_81bc9c` | gpt-5.6-luna | 15 | 53.442 | 524.800 | 5.875 |
| gonvra-tienda / `20260919_163720_169899` | gpt-5.6-luna | 11 | 51.915 | 372.736 | 4.654 |
| gonvra-tienda / `20260918_113606_4afb20` | gpt-5.6-luna | 7 | 45.147 | 200.704 | 1.550 |
| gonvra-tienda / `20260918_111503_9a8e02` | gpt-5.6-luna | 17 | 124.838 | 1.413.120 | 14.723 |
| gonvra-tienda / `20260817_023102_362251` | gpt-5.6-luna | 11 | 65.478 | 446.464 | 5.018 |
| gonvra-precios / `20260919_164120_2196dd` | gpt-5.6-luna | 7 | 45.465 | 208.896 | 4.560 |
| gonvra-precios / `20260919_163719_45548a` | gpt-5.6-luna | 12 | 46.266 | 374.272 | 4.986 |
| gonvra-jefe / `20260918_111503_d0fc5d` | gpt-5.6-luna | 9 | 48.064 | 282.624 | 2.938 |
| gonvra-jefe / `20260918_000833_a54f1a` | gpt-5.6-luna | 12 | 51.423 | 418.304 | 2.741 |
| gonvra-jefe / `20260817_023359_83d930` | gpt-5.6-luna | 7 | 55.053 | 229.376 | 3.616 |

Las corridas recientes confirman entradas frescas cercanas a **45–55 mil** y cache de **200–525 mil**, con salidas de alrededor de **3–6 mil** en varios workers. No todas entran en esa banda: hay salidas menores y un caso TIENDA de 17 llamadas, 124.838 entradas frescas y 1.413.120 cacheadas. **No lo escondemos:** el rango proyectado no cubre investigaciones largas, loops, reintentos ilimitados o sesiones que superen el límite de turnos. Todas las filas consultadas tenían `ended_at = null`: son contadores al momento de lectura, no prueba de cierre ni un p95 estadístico. El modelo histórico es **Luna/Codex**, no Gemini ni Sol.

### ¿Entrada y cache se suman o se pisan?

**En los buckets canónicos de Hermes se suman: son disjuntos.** Verificado en el código local:

- `~/.hermes/hermes-agent/agent/usage_pricing.py:1271–1319`: `normalize_usage` toma el total que devuelve Codex y resta `cache_read_tokens` y `cache_write_tokens` para obtener `input_tokens`.
- `~/.hermes/hermes-agent/agent/conversation_loop.py:3930–3934`: acumula entrada, salida, cache y razonamiento por separado.
- Todas las muestras tienen `cache_write_tokens = 0`. Entrada procesada = entrada fresca + cache leída. Los tokens de razonamiento son un desglose de la salida, **no se vuelven a sumar**.

No confundas esos buckets con el campo bruto `input_tokens` de una respuesta Codex: el bruto sí incluye cache. Esta verificación es de la semántica del código actual y la coherencia de los registros, no una conciliación de facturas históricas.

## 3. Supuestos por sesión nueva y acotada

Se usa la misma envolvente conservadora para cada rol, incluso GUARDIA: sin pruebas específicas no le asignamos un consumo mágico de 500 tokens. Minimizar herramientas no elimina por sí solo el catálogo enorme de skills ni el prefijo base.

| Escenario pareado | Turnos LLM | Entrada sin cache | Cache leída si hay aciertos | Salida total, incluido thinking |
|---|---:|---:|---:|---:|
| bajo | 3 | 45.000 | 80.000 | 1.500 |
| central | 6 | 55.000 | 250.000 | 4.000 |
| alto | 10 | 65.000 | 525.000 | 8.000 |

Son sumas de todas las llamadas de una sesión, no el tamaño de una única ventana ni tokens únicos escritos. El escenario bajo corresponde a una tarea corta de tres llamadas; el central a seis; el alto a diez con mayor devolución de herramientas. Conservan una entrada fresca grande y relectura acumulada del contexto. El recorte inferior de cache frente a los workers históricos se explica por menos turnos, **no por suponer que desaparecieron las skills**. No son percentiles ni una predicción garantizada.

Condiciones: sesión nueva por disparo, sólo herramientas indispensables, respuestas de herramientas resumidas/filtradas, sin subagentes ni generación multimedia, salidas y thinking dentro del presupuesto de sesión. El límite de salida por respuesta no limita la suma de toda la sesión: habría que medir ambas cosas. No se aplicó ningún cambio.

La cache implícita de Gemini es automática pero **sin garantía de ahorro**. La tasa de aciertos observada en Codex no se puede trasladar como un hecho a Gemini. Cada sesión arranca fría; tampoco se presupone reutilización entre roles ni entre horarios separados por horas. Para el escenario sin cache, toda la entrada prevista como cacheada se cobra a tarifa normal, sin duplicar tokens.

## 4. Precios oficiales y fórmula

Tarifas **Gemini Developer API, modalidad Standard pagada**, USD por millón de tokens, consultadas en [Google Pricing](https://ai.google.dev/gemini-api/docs/pricing). La página mostraba actualización 2026-09-16.

| Modelo | Entrada texto sin cache | Entrada texto cacheada | Salida, incluye thinking |
|---|---:|---:|---:|
| Gemini 2.5 Flash-Lite | 0,10 | 0,01 | 0,40 |
| Gemini 2.5 Flash | 0,30 | 0,03 | 2,50 |
| GPT-5.6-Sol / Codex | No determinada | No determinada | No determinada |

`USD = (entrada_sin_cache × tarifa_entrada + entrada_cacheada × tarifa_cache + salida_incluido_thinking × tarifa_salida) / 1.000.000`

Sin cache: reemplazar entrada_sin_cache por la suma de ambas entradas y poner cacheada en cero. No se aplican descuentos Batch/Flex, free tier ni créditos promocionales. No se incluye grounding pago, imágenes, video, audio, tarifas de herramientas/buscadores/navegador, hosting, electricidad, impuestos, cambio a ARS ni suscripciones.

La **cache explícita** cuesta además **USD 1 por millón de tokens almacenados por hora** para ambos Gemini. No se crea ni se asume cache explícita en estos números. Si después se usa, habrá que sumar su almacenamiento y cualquier consumo de creación que corresponda; no confundir lecturas acumuladas con tamaño almacenado.

## 5. Tokens diarios y costo Gemini

### Todo el equipo, incluidos los roles de suscripción

| Día / escenario | Entrada fresca | Entrada cacheada* | Salida | Total procesado |
|---|---:|---:|---:|---:|
| Común / bajo | 720.000 | 1.280.000 | 24.000 | 2.024.000 |
| Común / central | 880.000 | 4.000.000 | 64.000 | 4.944.000 |
| Común / alto | 1.040.000 | 8.400.000 | 128.000 | 9.568.000 |
| Viernes / bajo | 765.000 | 1.360.000 | 25.500 | 2.150.500 |
| Viernes / central | 935.000 | 4.250.000 | 68.000 | 5.253.000 |
| Viernes / alto | 1.105.000 | 8.925.000 | 136.000 | 10.166.000 |

*Cache condicional. Con cero aciertos Gemini, su parte se reclasifica como entrada fresca; el total de tokens procesados no cambia. Para Sol no se cotiza ningún supuesto sobre cache. Los desgloses por modelo están en `costs.json`.

| Período | Gemini con cache (bajo–alto) | Central con cache | Gemini sin cache (bajo–alto) |
|---|---:|---:|---:|
| Día común | USD 0.1317–0.3555 | USD 0.2224 | USD 0.2829–1.3478 |
| Viernes | USD 0.1376–0.3705 | USD 0.2320 | USD 0.2960–1.4100 |
| Semana | USD 0.9278–2.5038 | USD 1.5664 | USD 1.9934–9.4968 |
| 30 días, promedio semanal | USD 3.9763–10.7306 | USD 6.7131 | USD 8.5431–40.7006 |
| 30 días con 4 viernes | USD 3.9746–10.7263 | USD 6.7104 | USD 8.5394–40.6828 |
| 30 días con 5 viernes | USD 3.9805–10.7413 | USD 6.7200 | USD 8.5525–40.7450 |

**Sólo COPY + CRO + JEFE:** 379.500–1.794.000 tokens/día procesados; central 927.000. Consumen capacidad de la suscripción; el precio incremental en dinero depende del plan, límites y eventuales créditos extra. No se verificó saldo/cuota en la cuenta ni se buscó acceso a credenciales. No corresponde sumar “USD 0” como si fuera un costo total comprobado.

## 6. Alternativa liviana, sin activar

1. **GUARDIA determinista en los siete horarios, sin LLM jamás en ese job:** chequeos de salud/deltas con reglas; aviso por plantilla. Incluso ante error, el guardia no llama al modelo. Una investigación humana o un job separado requeriría su propio presupuesto. Hermes documenta `no_agent` para esta modalidad.
2. **ESPIA y CRO: cada uno 2–3 veces por semana**, no diario. Trabajan sólo sobre novedades o cambios medibles, sin repetir auditorías resueltas.
3. **TIKTOKER, INSTAGRAMER, CREATIVO y COPY:** producir sólo cuando existe un ítem nuevo verificable. El filtro de novedades debe ocurrir **antes de arrancar el LLM**, de forma determinista; pedirle a un modelo que diga “sin novedades” ya gasta contexto. Para no inventar una tasa de novedades, la tabla mantiene la reserva de una corrida diaria por cada productor. Si hay menos ítems, se descuenta su consumo real, sin prometer un ahorro adicional no medido.
4. ANALISTA y CAZADOR siguen diarios; LEGAL los viernes; JEFE diario. Ninguna publicación, cambio LIVE o gasto se activa por esta propuesta.

| Variante | Sesiones LLM/semana | Chequeos GUARDIA sin LLM/semana | Gemini/día promedio con cache | Gemini/30 días con cache | Gemini/30 días sin cache |
|---|---:|---:|---:|---:|---:|
| ESPIA/CRO 2 cada uno/semana | 54 | 49 | USD 0.0772–0.2136 | USD 2.3162–6.4071 | USD 4.9082–23.4171 |
| ESPIA/CRO 3 cada uno/semana | 56 | 49 | USD 0.0800–0.2215 | USD 2.4004–6.6439 | USD 5.0850–24.2614 |

Tokens de todo el equipo liviano, promedio por día (la realidad varía según el día de ESPIA/CRO/LEGAL):

| Variante / escenario | Entrada fresca | Cache leída | Salida | Total |
|---|---:|---:|---:|---:|
| 2/semana / bajo | 347.143 | 617.143 | 11.571 | 975.857 |
| 2/semana / central | 424.286 | 1.928.571 | 30.857 | 2.383.714 |
| 2/semana / alto | 501.429 | 4.050.000 | 61.714 | 4.613.143 |
| 3/semana / bajo | 360.000 | 640.000 | 12.000 | 1.012.000 |
| 3/semana / central | 440.000 | 2.000.000 | 32.000 | 2.472.000 |
| 3/semana / alto | 520.000 | 4.200.000 | 64.000 | 4.784.000 |

No alcanza con bajar el modelo: la reducción importante de tokens/quota viene de no abrir una sesión innecesaria. Un “sin novedades” generado por LLM no equivale a `no_agent`.

## 7. Riesgos y confianza

- **Precios y aritmética: confianza alta.** Precios oficiales y cuentas ejecutadas en Python; asserts de 16/17 sesiones y 113 semanales. El equivalente mensual es semana × 30/7, no un mes calendario exacto; arriba también hay 4/5 viernes.
- **Uso histórico: real, pero muestra chica y no cerrada.** Refleja workers Kanban con Luna. No son pruebas nuevas ni un benchmark del cron Gemini/Sol.
- **Proyección de tokens/cache: confianza media-baja.** Cambian tokenizer, reasoning, herramientas y aciertos. El rango alto no es techo duro: un loop o una respuesta enorme puede superarlo. La alternativa usa el mismo costo por sesión para no inventar mejoras en los prompts.
- **Cuotas:** Google aplica RPM, TPM y RPD por proyecto, no por clave. La cache no elimina la carga de contexto ni los límites. Hay que consultar los límites efectivos de AI Studio; no se presupone que el free tier alcance. Escalonar corridas evita ráfagas. En el plan común son 48–160 llamadas LLM/día; viernes 51–170, antes de reintentos. De esas, Gemini representa 39–130 comunes / 42–140 viernes; Codex 9–30 diarias.
- **Suscripción:** estar marcado `subscription_included` en la muestra no prueba disponibilidad ilimitada ni gasto total cero. Sol puede tener límites distintos de Luna. No se verificó precio por token ni conversión de tokens a cupo, y no se hizo ninguna llamada de prueba paga.
- **Antes de comprometer un presupuesto:** medir unas corridas autorizadas por modelo con entrada, cache, salida/thinking y número de llamadas; contrastar con la facturación y cuota real. Hasta entonces, usar el escenario sin cache para caja y dejar margen aparte para reintentos. No se instaló instrumentación ni se activaron esas corridas.

## Fuentes

- [Google Gemini Developer API pricing — Standard](https://ai.google.dev/gemini-api/docs/pricing#gemini-2.5-flash): Flash 0.30/0.03/2.50; Flash-Lite 0.10/0.01/0.40 USD por millón; almacenamiento explícito 1 USD/M tokens-hora.
- [Google context caching](https://ai.google.dev/gemini-api/docs/generate-content/caching): Cache implícita automática sin garantía de acierto; explícita cobra almacenamiento; cache cuenta para límites.
- [Google rate limits](https://ai.google.dev/gemini-api/docs/rate-limits): RPM, TPM y RPD por proyecto; verificar cuota real en AI Studio.
- [Hermes cron](https://hermes-agent.nousresearch.com/docs/user-guide/features/cron/): Sesiones nuevas y no_agent sin intervención LLM.
- [Codex con suscripción](https://help.openai.com/en/articles/11369540-using-codex-with-your-chatgpt-plan): Uso sujeto al plan y límites; no aporta tarifa verificada por token para gpt-5.6-sol.
- Evidencia local: `~/.hermes/profiles/gonvra-{cro,tienda,precios,jefe}/state.db`, consultas sólo lectura; código `agent/usage_pricing.py` y `agent/conversation_loop.py`. IDs y contadores de la muestra quedan en `costs.json`.
