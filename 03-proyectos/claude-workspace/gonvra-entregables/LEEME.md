# GONVRA · Entregables

Todo listo para subir. Generado el 2026-09-11.

```
01-videos/         3 anuncios verticales 1080x1920, 24 fps, ~15 s
02-carruseles/     3 carruseles de Instagram, 6 slides cada uno, 1080x1350
03-subtitulos/     .srt de cada anuncio (subilos a TikTok como texto accesible)
04-proyecto-editable/  .fcpxml (lo editable de verdad) + .edl + .drp + manifiesto
NOTA-DE-EDICION.md     decisiones, descartes y pendientes
```

## Antes de publicar

**Los videos no tienen sonido.** Es a propósito: los clips de Flow no traían ambiente
utilizable (medido: −65 dB el del cepillo, −38/−50 dB el del agua). Amplificarlo era
publicar siseo. Falta una pista instrumental de ~20 s, 90-100 BPM, sin voces — con una
sola cubrís los tres. Pasámela y los remezclo.

Los carruseles sí están listos para publicar tal cual.

## Orden sugerido de publicación

| Pieza | Público | Por qué |
|---|---|---|
| `2-la-lamina` | frío | Es el más sólido de los tres: todos los tiempos tienen cartel y el macro de la lámina cae justo sobre el cartel que la nombra |
| `1-el-cajon` | frío | Buen gancho de problema, pero arranca en material de 360p (se ve blando los primeros 4 s) |
| `3-que-trae` | retargeting | Abajo del embudo, para quien ya te vio |

Los carruseles funcionan como refuerzo del anuncio del mismo nombre.

## Pie de publicación

> Rasuradora integral recargable. Rostro, cuerpo y zona íntima con el mismo equipo.
> Peines de 1, 3 y 5 mm, se usa en seco, se enjuaga bajo la canilla y se carga por USB.
> Envío a todo el país con seguimiento. gonvra.com

`#cuidadopersonal #afeitadora #rutinamasculina #argentina #envioatodoelpais`

## Para reabrir y editar

Importá el **`.fcpxml`** en Resolve (`Archivo > Importar > Línea de tiempo`). Cada corte
entra como clip separado en pista 1 y los carteles en pista 2, apuntando a los originales
en `~/Descargas` — no se duplicó material. El `.drp` abre el anuncio ya aplanado; el
`.edl` es respaldo simple.

Si movés los originales, `04-proyecto-editable/manifiesto-rutas.json` tiene la ruta,
el tamaño y el hash de cada fuente para reubicarlas.
