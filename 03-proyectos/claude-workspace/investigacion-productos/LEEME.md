# Investigación de productos — salud, belleza y cuidado personal

## Estado

**Entregados los 50 productos.** Salieron de 3.294 productos únicos explorados del
catálogo del proveedor. 451 cumplen los cinco criterios; el dashboard muestra los 50
mejores, con tope de 4 por categoría para que no sean 50 afeitadoras.

```bash
xdg-open ~/Claude/investigacion-productos/dashboard.html
```

## Lo que hay que saber sobre la fuente

**El conector de AutoDS no está disponible en esta sesión.** Está registrado en la
cuenta (`claude.ai autods`) pero figura como "necesita autenticación", y las
herramientas del conector se cargan sólo al arrancar la sesión.

Los datos salen de **AliExpress**, que es el catálogo que AutoDS revende. Los costes
son reales y coinciden con lo que AutoDS mostraría, pero **faltan dos cosas que sólo
AutoDS tiene**: el tiempo de envío real por proveedor y las ventas medidas por AutoDS.

Si querés cruzar con datos de AutoDS, exportá el CSV desde su panel y avisá dónde quedó.

## El bug que hacía fallar todo

AliExpress cambió la moneda de la sesión a **pesos argentinos** después de los primeros
60 productos. El script viejo (`score.py`) leía esos precios como si fueran dólares, así
que un producto de 9.000 ARS lo veía como "9.000 dólares" y lo descartaba por caro.
Por eso sólo pasaban 7 de 3.294.

`seleccion.py` normaliza la moneda a **1.497,4 ARS/USD**, tipo de cambio deducido de 6
productos que quedaron capturados en las dos monedas (las 6 mediciones coinciden entre
1.495 y 1.498, así que el número es sólido). Si el dólar se movió mucho desde entonces,
todos los costes se corren en bloque: cambiá `RATE_ARS` y volvé a correr.

## Validación por título

El buscador devuelve listados que no son lo que se buscó. Buscando "massage gun"
apareció una **pistola dosificadora dental**; buscando "back shaver", **100 cepillos de
profilaxis dental**; buscando "manscaping kit", **cable de silicona**. `seleccion.py`
exige que el título confirme la categoría y bloquea basura y commodities. Eso descarta
142 listados que si no se colaban en el top.

También marca productos con **claims médicos regulados** (hemoglobina, verrugas,
lunares, adelgazamiento) y les baja la nota, porque Meta y Google rechazan esos anuncios
y quemar un lunar puede tapar un melanoma.

## Qué es dato y qué es supuesto mío

Lo más importante antes de comprar stock:

| Columna | Origen | Confiar |
|---|---|---|
| Coste | **Dato real** del catálogo | Sí |
| Vendidos | **Dato real**, contador del proveedor | Sí |
| Rating | **Dato real** de compradores | Sí |
| Envío | Estimado según si es Choice o no | A medias |
| PVP y margen | Múltiplo que asigno por tipo de producto | Es hipótesis |
| Competencia | Saturación de listados + disponibilidad en tienda física | Es hipótesis |
| Nota | Combinación ponderada de todo lo anterior | Es hipótesis |

El PVP dice a cuánto *se podría* vender, no a cuánto se vende hoy en Argentina.
Y el coste es sólo el producto: faltan envío, pasarela, impuestos y publicidad.

## Scripts

| Archivo | Qué hace |
|---|---|
| `seleccion.py` | Filtra y puntúa desde `raw.jsonl` → `productos_top50.json` |
| `dashboard.py` | Genera `dashboard.html` desde el JSON |
| `collect.py` | Recolector lento y reanudable (1 consulta cada varios minutos) |
| `score.py` | **Obsoleto**, tiene el bug de la moneda. Reemplazado por `seleccion.py` |

Para regenerar todo:

```bash
cd ~/Claude/investigacion-productos && python3 seleccion.py && python3 dashboard.py
```

## Ampliar el catálogo

Hoy hay 45 categorías de búsqueda, y están cargadas hacia afeitado/depilación. Para
sumar catálogo hay que correr `collect.py`, que va lento a propósito: AliExpress corta
el acceso cuando detecta muchas consultas seguidas y la IP ya quedó marcada una vez.
