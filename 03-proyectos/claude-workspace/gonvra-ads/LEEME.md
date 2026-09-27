# GONVRA · Fábrica de anuncios y carruseles

Todo se genera acá, sin depender de nadie. Dos comandos.

```bash
cd ~/Claude/gonvra-ads
```

---

## Carruseles (TikTok / Instagram)

```bash
./carrusel.sh                      # renderiza los tres
./carrusel.sh Carrusel-Problema    # sólo uno
```

Las placas salen en `out/<nombre-del-carrusel>/01.png, 02.png…`, en 1080×1920, listas
para subir en orden.

**Los que ya están armados:**

| Carrusel | Para qué |
|---|---|
| `Carrusel-Problema` | público frío: gancho de problema → solución |
| `Carrusel-Comparativa` | público que ya vio el producto |
| `Carrusel-Como-Se-Usa` | educativo, genera guardados y compartidos |

**Para cambiar textos o armar uno nuevo:** editá `src/carruseles.ts`. Copiás un bloque,
le cambiás los textos y volvés a correr el script. Hay siete tipos de placa:

- `portada` — foto de fondo + título grande
- `texto` — sólo texto sobre color (`tinta`, `papel` o `lima`)
- `imagen` — foto a sangre con cartel blanco encima
- `dato` — un número enorme + explicación
- `lista` — título + foto + ítems con tilde
- `versus` — dos columnas comparando
- `cierre` — producto + precio + botón

El precio y la web salen de `src/campaign.ts`. Lo cambiás en un solo lugar y se actualiza
en todos los carruseles.

---

## Videos para anuncios

```bash
npx remotion render Anuncio-Gancho out/anuncio-gancho.mp4
```

| Video | Duración | Formato | Para qué |
|---|---|---|---|
| `Anuncio-Gancho` | 16 s | carteles tipo TikTok | público frío, es el que más engancha |
| `Anuncio-Problema` | 19,5 s | narrado con títulos | público frío, más explicativo |
| `Anuncio-Producto` | 13,5 s | producto y beneficios | retargeting |
| `Anuncio-Demo` | 12,5 s | demostración pura | retargeting |

Los guiones están en `src/guiones.ts`: cada escena tiene el clip, desde qué segundo
arranca, cuánto dura y el texto. Cambiás eso y volvés a renderizar.

**Para verlo en vivo mientras editás:**

```bash
npx remotion studio
```

---

## Si querés cambiar los clips de origen

Están en `public/clips/`. Reemplazás el archivo con el mismo nombre y listo. Las fotos de
los carruseles están en `public/carrusel/`.
