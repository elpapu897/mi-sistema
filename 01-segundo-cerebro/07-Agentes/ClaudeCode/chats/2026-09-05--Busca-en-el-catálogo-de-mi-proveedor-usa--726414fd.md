---
tool: ClaudeCode
session_id: 726414fd-0479-45a5-9962-3f32cec62c59
fecha: 2026-09-05 02:28
titulo: "Busca en el catálogo de mi proveedor usando el con"
tags: [chat, agente, claudecode]
---

# 💬 Busca en el catálogo de mi proveedor usando el con
> **ClaudeCode** · 2026-09-05 02:28 · `726414fd-0479-45a5-9962-3f32cec62c59`

---

### 🧑 Vos  <small>2026-09-05 02:28</small>

Busca en el catálogo de mi proveedor, usando el conector de AutoDS, productos que:

- Solucionen un problema real en los nichos de salud, belleza o cuidado personal
- No se puedan encontrar en un supermercado o en cualquier tienda física
- Tengan un valor percibido alto, para que se puedan vender por al menos 3 veces su coste
- Cuesten entre 5 y 30 dólares y sean pequeños y fáciles de enviar
- Ya estén generando ventas

Explora más de 1.000 productos y entrégame los 50 mejores en un dashboard interactivo con margen, coste, tiempo de envío, competencia y una nota final para cada uno.

### 🤖 Claude  <small>2026-09-05 02:28</small>

I'll start by checking whether the AutoDS connector is actually available in this session.

### 🤖 Claude  <small>2026-09-05 02:28</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-09-05 02:28</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-05 02:28</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-09-05 02:28</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-05 02:28</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-09-05 02:28</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-05 02:28</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-09-05 02:29</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-05 02:29</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-09-05 02:29</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-05 02:29</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-09-05 02:29</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-05 02:29</small>

Good news: there's prior work here with real scraped data. Let me check the AutoDS connector status definitively, then run the scoring pipeline.

### 🤖 Claude  <small>2026-09-05 02:29</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-09-05 02:29</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-05 02:29</small>

Only 7 of 3,294 pass. Let me diagnose the funnel before trusting that.

### 🤖 Claude  <small>2026-09-05 02:29</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-09-05 02:29</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-05 02:29</small>

The bottleneck is price — only 32 of 3,294 land in $5–30. Let me check the price distribution.

### 🤖 Claude  <small>2026-09-05 02:29</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-09-05 02:29</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-05 02:29</small>

Price data is corrupted — mean price is $97,833. The scraper broke partway. Let me find where.

### 🤖 Claude  <small>2026-09-05 02:29</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-09-05 02:29</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-05 02:30</small>

AliExpress silently switched currency to Argentine pesos after the first 60 items. 3,762 records are ARS, not USD. Let me derive the exact rate from overlapping products.

### 🤖 Claude  <small>2026-09-05 02:30</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-09-05 02:30</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-05 02:30</small>

Rate derived empirically: **1497.4 ARS/USD** (consistent across all 6 overlaps). Let me fix the normalization and re-check the funnel.

### 🤖 Claude  <small>2026-09-05 02:30</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-09-05 02:30</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-05 02:30</small>

Funnel now works: 3,294 → 2,073 in price → 871 with sales → **757 qualified** across 45 product categories. Let me check what fields I actually have (especially shipping).

### 🤖 Claude  <small>2026-09-05 02:30</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-09-05 02:30</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-05 02:30</small>

No shipping field in the data. Let me check the unexplored fields in case shipping info is hiding there.

### 🤖 Claude  <small>2026-09-05 02:30</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-09-05 02:30</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-05 02:31</small>

Found real signals I can use: `sp_sources` flags AliExpress **Choice** (faster tracked shipping) and free shipping, and `launch` gives product age. Let me quantify those.

### 🤖 Claude  <small>2026-09-05 02:31</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-09-05 02:31</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-05 02:31</small>

Now I have everything I need. Let me write an improved selector that fixes the currency bug, enforces all 5 criteria, and uses the real Choice/launch signals.

### 🤖 Claude  <small>2026-09-05 02:32</small>

_[usó herramienta: Write]_

### 🧑 Vos  <small>2026-09-05 02:32</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-05 02:32</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-09-05 02:32</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-05 02:32</small>

593 qualify across 18 categories. Let me sanity-check the top entries before building the dashboard.

### 🤖 Claude  <small>2026-09-05 02:32</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-09-05 02:32</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-05 02:32</small>

Results are real, but I spot a quality problem: some listings don't match their search category (e.g. #12 is a wooden roller scored as a TENS device), and a few are regulated medical-claim products. Let me add title validation and a risk flag.

### 🤖 Claude  <small>2026-09-05 02:32</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-09-05 02:32</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-05 02:33</small>

Confirmed — the search engine returned genuinely wrong products: **#25 is a dental mixing gun**, **#41 is 100 dental prophy brushes**, **#42 is silicone cable**. Plus regulated medical devices (#7 hemoglobin monitor, #2 "venous insufficiency"). Let me add a title validation layer.

### 🤖 Claude  <small>2026-09-05 02:33</small>

_[usó herramienta: Read]_

### 🧑 Vos  <small>2026-09-05 02:33</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-05 02:34</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-09-05 02:34</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-05 02:34</small>

The blocklist regex has an empty alternation (`||`) from my line-splitting, which matches everything. Let me fix it properly.

### 🤖 Claude  <small>2026-09-05 02:34</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-09-05 02:34</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-05 02:34</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-09-05 02:34</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-05 02:34</small>

Much cleaner — the dental gun, cables and prophy brushes are gone. Two remaining issues: weight-loss claims (#33) and hand-warmers miscategorized as menstrual (#17, #24). Let me tighten those.

### 🤖 Claude  <small>2026-09-05 02:34</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-09-05 02:34</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-05 02:34</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-09-05 02:35</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-05 02:35</small>

The list is clean and coherent now. Let me build the interactive dashboard.

### 🤖 Claude  <small>2026-09-05 02:36</small>

_[usó herramienta: Write]_

### 🧑 Vos  <small>2026-09-05 02:36</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-05 02:36</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-09-05 02:36</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-05 02:36</small>

Let me verify the dashboard actually renders and the interactions work.

### 🤖 Claude  <small>2026-09-05 02:36</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-09-05 02:36</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-05 02:36</small>

_[usó herramienta: mcp__Claude_Browser__navigate]_

### 🧑 Vos  <small>2026-09-05 02:36</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-05 02:36</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-09-05 02:36</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-05 02:37</small>

Data validates. Let me check the JavaScript for syntax errors and test the filter/sort logic.

### 🤖 Claude  <small>2026-09-05 02:37</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-09-05 02:37</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-05 02:37</small>

All logic tests pass. Let me clean up and update the project README.

### 🤖 Claude  <small>2026-09-05 02:37</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-09-05 02:37</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-05 02:37</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-09-05 02:37</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-05 02:37</small>

_[usó herramienta: Write]_

### 🧑 Vos  <small>2026-09-05 02:37</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-05 02:37</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-09-05 02:37</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-05 02:38</small>

Listo. Abrí el dashboard: **[dashboard.html](dashboard.html)**

## Primero, lo que tenés que saber

**No pude usar el conector de AutoDS.** Está registrado en tu cuenta pero figura como "necesita autenticación", y los conectores se cargan sólo al arrancar la sesión — así que aunque lo reconectes ahora, esta sesión no lo va a ver.

Fui al catálogo que está **debajo** de AutoDS: AliExpress, que es lo que AutoDS revende. Los costes son reales. Lo que perdés respecto a AutoDS son dos cosas: el tiempo de envío real por proveedor y las ventas medidas por AutoDS.

## Dos bugs que encontré y arreglé

**La moneda.** Había trabajo previo en esta carpeta que entregaba 7 productos de 3.294. El motivo: AliExpress cambió la moneda de la sesión a pesos argentinos después de los primeros 60 productos, y el script viejo leía esos precios como dólares. Un producto de 9.000 ARS lo descartaba como "9.000 dólares, muy caro". Deduje el tipo de cambio de 6 productos que quedaron capturados en ambas monedas: 1.497,4 ARS/USD, con las 6 mediciones coincidiendo entre 1.495 y 1.498.

**Listados que no eran lo que se buscó.** Buscando "massage gun" apareció una pistola dosificadora dental; buscando "back shaver", 100 cepillos de profilaxis dental; buscando "manscaping kit", cable de silicona. Estaban rankeando alto. Agregué validación por título, que descartó 142 listados.

## El resultado

3.294 productos únicos explorados → 451 cumplen los cinco criterios → top 50, con tope de 4 por categoría para que no fueran 50 afeitadoras.

- Coste medio **$13,28**, todos entre $5,44 y $23,35
- Múltiplo medio **3,7x** (ninguno baja de 3x, era tu criterio)
- Mediana de **1.000 unidades vendidas**
- 43 de 50 con competencia baja, 44 con envío Choice
- 9 nichos: dolor (15), piel (10), sueño (6), salud bebé (6), higiene (4)

Arriba de todo quedan los limpiadores de oído con cámara (~$7,78, se venden a 4x, difíciles de conseguir en tienda física) y los dispositivos TENS.

## Lo que no te puedo garantizar

El dashboard separa en el pie qué columna es dato y cuál es supuesto mío. Resumido: **coste, vendidos y rating son datos reales**. **PVP, margen, competencia y nota son estimaciones mías** — el PVP dice a cuánto *se podría* vender según el tipo de producto, no a cuánto se vende hoy en Argentina. Validá contra competencia local antes de comprar volumen.

Y el coste es sólo el producto: faltan envío al cliente, pasarela, impuestos y publicidad. En dropshipping la publicidad se come buena parte del margen bruto, así que ese 73% promedio no es 73% en tu bolsillo.

También marqué los productos con claims médicos regulados (verrugas, lunares, adelgazamiento, hemoglobina) y les bajé la nota: Meta rechaza esos anuncios, y con tu cuenta de Meta Ads eso te importa.

**Si querés los datos reales de envío y ventas de AutoDS**, exportá el CSV desde su panel y decime dónde quedó — el pipeline lo absorbe y regenera el dashboard.

### 🧑 Vos  <small>2026-09-05 02:39</small>

QUIERO Q VOS ELIGAS EL MEJOR PRODUCTO, YO CONFIO EN TI, QUE ME GARANTIZE VENTAS Bueno, además que me garantice ventas que sea muy promocionable, que esté viral últimamente, que es un producto que, mire, al futuro va a ser yendo, que toda la gente en TikTok, Instagram y redes sociales siempre hablen de él, pero que no haya muchos competidores, y nada de eso.

### 🤖 Claude  <small>2026-09-05 02:39</small>

Antes de elegir, dejame hacer un análisis que no hice todavía: **velocidad de venta** (unidades por día desde que se publicó el listado). Eso es lo más cerca que puedo estar de "está explotando ahora" con datos reales.

### 🤖 Claude  <small>2026-09-05 02:40</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-09-05 02:40</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-05 02:40</small>

Ahora tengo lo que me faltaba. Dejame ver en detalle los candidatos finales.

### 🤖 Claude  <small>2026-09-05 02:40</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-09-05 02:40</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-05 02:41</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-09-05 02:41</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-05 02:41</small>

Elegí. Pero antes, dos cosas que te tengo que decir de frente, porque si no la elección no te sirve.

**No existe un producto que garantice ventas.** Nadie te puede prometer eso — ni yo, ni un curso, ni un proveedor. Lo que sí puedo hacer es elegir el que tiene mejores probabilidades y, sobre todo, el que si sale mal te hace perder poco. Eso es lo que hice.

**Y "que todos hablen de él en TikTok" + "que no haya competidores" no pueden pasar juntos.** Si todo el mundo lo muestra, hay competencia; es la misma cosa vista de dos lados. Lo que sí se puede conseguir es un producto con *formato* viral probado que todavía no está saturado. Eso es lo que busqué.

Último aviso: **no tengo datos de TikTok ni Instagram.** Nada de lo que digo sobre viralidad sale de medir redes. Sale de la velocidad de venta real del catálogo y de las características del producto.

---

## Mi elección: limpiador de oídos con cámara (otoscopio)

**[Ver el producto](https://www.aliexpress.com/item/1005009734016590.html)** — $7,78 el costo

| | |
|---|---|
| Costo | **$7,78** |
| PVP sugerido | **~$31** (4x) |
| Margen bruto | $23,34 (75%) |
| Vendidos | 10.000 unidades · 4,7★ |
| Velocidad | **25,9 unidades/día** — la más alta de todo lo que no es maquinita de afeitar |
| Envío | 15-25 días (Choice) |
| Competencia | Baja |

### Por qué este y no otro

**El video es el producto.** Una cámara metida en un oído sacando cera es el género "oddly satisfying", uno de los formatos más duraderos que existe en TikTok. No necesitás ser creativo, ni salir en cámara, ni tener buena luz: la grabación se vende sola. Cuando me pedís "muy promocionable", esto es literalmente lo que significa en la práctica. Y cada limpieza es un video nuevo — el contenido es infinito y gratis.

**La gente ya paga caro por esto, y lo puedo probar.** En el mismo catálogo, este producto se vende desde $7,40 hasta $26,70. La versión "Generación-2" a $23,35 tiene 1.000 vendidas con 4,7★. O sea: no estoy inventando que se puede cobrar 4x — hay gente pagando 3x el precio base *dentro de AliExpress*, que es el lugar más barato del mundo. Ese es el dato que más me convenció.

**No lo conseguís en el Carrefour ni en una farmacia.** Es el producto con menor disponibilidad en tienda física de toda mi lista (0,05 sobre 1). No tenés un precio de góndola contra el cual competir, y eso es exactamente lo que te deja poner $31.

**Y esto es lo más importante para vos:** no hace ninguna afirmación médica. Es una herramienta de limpieza, no un tratamiento. Los otros productos que puntuaban alto — TENS, lápiz de luz azul, quita-verrugas — son claims regulados y **Meta te rechaza los anuncios o te suspende la cuenta**. Vos manejás Meta Ads. Elegir uno de esos era ponerte a jugar con la cuenta publicitaria de garantía.

### Lo que puede salir mal

**El wifi y la app.** Es la falla número uno de estos endoscopios baratos: la cámara se desconecta, la app es mala, anda en Android pero no en iPhone. Si eso pasa te llueven las devoluciones y las reseñas malas. **Es el riesgo real de este producto y no lo puedo verificar desde acá.**

**No es nuevo.** Bebird lo hizo popular alrededor de 2020-2021. Esto es "probado y todavía funcionando", no "nadie lo descubrió". Si buscabas algo que nadie vio nunca, no es este — y te diría que desconfíes de cualquiera que te ofrezca eso con ventas ya probadas, porque las dos cosas juntas no existen.

**Mis 60 listados no son la competencia mundial.** Es baja *comparada con las otras categorías que medí*, no baja en términos absolutos.

### Qué hacer ahora

Comprá **una sola unidad** ($7,78) y probala vos: la app en tu teléfono, la batería, si la imagen se ve bien. Con esa misma unidad filmás los primeros 5 o 10 videos. Recién si la app funciona bien, comprás volumen.

Esa es la única garantía que te puedo dar de verdad: que si me equivoqué, te enteraste por $8 y no por $800.

¿Querés que arme la ficha de producto y los ángulos de video para arrancar?
