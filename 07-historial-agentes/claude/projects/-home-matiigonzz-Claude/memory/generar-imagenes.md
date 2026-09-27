# Generar imágenes (Replicate)

**Cómo generar imágenes para el usuario. Funciona ya, sin setup.**

## Comando

```bash
python ~/Claude/scripts/genimage-replicate.py \
  --prompt "..." \
  --model nano-banana \
  --aspect-ratio 4:5 \
  --output salida.png
```

El token está en `~/.replicate-env` (permisos 600) y `~/.bashrc` lo carga solo.
Si el script dice que falta `REPLICATE_API_TOKEN`, correr primero:
`source ~/.replicate-env`

Después de generar, **siempre leer la imagen con Read** para verificarla antes
de dársela por buena al usuario.

## Modelos

| `--model` | Costo | Cuándo |
|---|---|---|
| `imagen-4-fast` | $0.02 | Default para fotos sueltas |
| `imagen-4` | $0.04 | Más detalle |
| `nano-banana` | $0.039 | **Editar** o usar fotos de referencia (`--images`) |
| `nano-banana-pro` | $0.139 | Texto dentro de la imagen, 2K/4K |

## Trampas ya pisadas

1. **Aspect ratio:** Imagen 4 solo acepta `1:1 9:16 16:9 3:4 4:3`.
   Para **4:5** (Instagram) hay que usar `nano-banana`. El script ya valida y avisa.

2. **Texto fantasma:** si el prompt menciona "space for headline text" o "logo",
   el modelo lo *dibuja* y encima mal escrito (salió un "HEADLNE").
   Terminar SIEMPRE los prompts con:
   `"no text, no words, no letters, no watermark"`

3. **Filtro de contenido (E005):** palabras como "guilty/embarrassed" pueden
   bloquear la generación. Reformular más neutro y reintentar.

4. **No pipear a `tail`:** oculta el mensaje de error real del script.
   Correrlo derecho para ver qué falló.

5. **Texto DENTRO de la imagen:** el usuario lo quiere así, no con placeholders
   para Canva. `nano-banana-pro` a 2K escribe español perfecto, acentos incluidos
   (SILLÓN, DESPUÉS, SACÁ). Cerrar el prompt con:
   `"Render all Spanish text with perfect spelling exactly as written including
   accents. No gibberish, no misspellings, no watermark."`

6. **Producto que se lee mal:** si al pasar un recorte de producto el modelo lo
   dibuja como otra cosa (el guante salía como pantufla), generar primero la foto
   limpia con `nano-banana` y después pasarle **esa foto** a `nano-banana-pro`
   pidiendo "keep it EXACTLY as it is" + el diseño encima. Funciona mucho mejor
   que insistir con el recorte.

## Productos reales de GONVRA

Para creativos de la tienda, bajar la foto real y pasarla como `--images`,
si no la IA inventa un producto que no es el que vende.

```bash
curl -s "https://gonvra.com/products/HANDLE.json" | python -c "
import sys,json
for i in json.load(sys.stdin)['product']['images']: print(i['src'])"
```

**Ojo:** el guante del Combo Chau Pelos es una **manopla de tela negra**,
NO de silicona (la ficha vieja lo decía mal).

## Créditos

Replicate es **prepago**: no alcanza con tener tarjeta cargada, hay que comprar
crédito en replicate.com/account/billing#billing. Cuenta: `elpapu897`.
Si tira `402 Insufficient credit`, se acabó el saldo.

La API de Gemini directa (`GEMINI_API_KEY`) **no sirve** para imágenes:
el proyecto está en free tier y Google da cuota 0 para modelos de imagen.


## Estilo visual que le gusta al usuario

Carrusel tipo agencia (referencias en ~/Descargas, "WhatsApp Image 2026-08-02"):
fondo azul noche casi negro `#0A1628`, acento ámbar dorado `#E8A33D`,
titulares Montserrat ExtraBold MAYÚSCULAS bicolor (blanco + ámbar),
numeración 01-06 en cuadrito de línea fina, reglas finas ámbar,
copy chico gris claro, mucho espacio negativo.

Carrusel ya hecho con este estilo: `~/Claude/gonvra-chaupelos/` (slides `*-txt.png`).


## Plan B sin crédito: fotos libres de Wikimedia Commons

Al 13-ago-2026 la cuenta de Replicate se quedó **sin crédito (402)**. Antes de
generar un lote, probar UNA imagen: si tira 402, no insistir.

Alternativa que ya funcionó (página del Amazonas, `~/Claude/amazonas/`):
bajar fotos reales con licencia CC de Commons vía API.

```python
# buscar: action=query&generator=search&gsrnamespace=6&prop=imageinfo
#         &iiprop=url|extmetadata&iiurlwidth=1800
# bajar:  usar ii['thumburl']; User-Agent propio SIEMPRE
```

Trampas pisadas:
1. **429 de Commons:** bajar de a una, con `sleep 4` entre metadata y archivo
   y `sleep 8-10` entre imágenes. En paralelo tira 429 seguro.
2. **Verificar SIEMPRE con Read:** salieron un esqueleto de museo buscando
   "delfín rosado", grabados del 1800 buscando pueblos indígenas, y fotos con
   watermark del autor. Nunca usar a ciegas.
3. **Criterio ético:** descartada una foto etnográfica de menores desnudas.
   Preferir escenas documentales de actividad (cocinando, navegando).
4. **Poner los créditos** (autor + licencia) en el pie de la página.
5. Fotógrafos confiables en Commons para fauna: **Charles J. Sharp**,
   Bernard DUPONT. Para satélite/aéreo: **NASA Earth Observatory** (dominio público).

Ojo aparte: `imagen-4` **no acepta 21:9** (sólo 16:9, 1:1, 3:4, 4:3, 9:16), y
una vez devolvió una imagen totalmente ajena al prompt (pedí río amazónico y
llegó una mujer en un puente). Verificar con Read también lo generado.
