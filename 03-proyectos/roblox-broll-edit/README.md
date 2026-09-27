# roblox-broll-edit

Edición en Remotion del gameplay de Roblox (`Screen Recording - Made with FlexClip (1).webm`):
**intro animada + video completo + 14 inserts de B-roll** en los picos de reacción.

## Cómo se decidió dónde van los B-rolls

No se eligieron a ojo. El proceso fue:

1. Se extrajo el audio y se transcribió con `faster-whisper` (español, 202 segmentos).
2. Se calculó el RMS del audio en ventanas de 0.5s, suavizado a 3s, para encontrar los
   **picos de energía** = gritos, puteadas, festejos.
3. Se tomaron los 14 picos más altos con separación mínima de 25s (para que no se
   amontonen), y se cruzó cada uno con lo que se dice en la transcripción en ese momento.
4. A cada pico se le asignó un B-roll temático. Ejemplos:
   - `266.5s` — dicen *"son malardos los parkour"* → clip de parkour
   - `233.0s` — *"yeeee, bien boludo"* → clip de festejo
   - `526.0s` — *"no puedo sacar esta mierda"* → clip de humo

El mapa completo está en [`src/brolls.ts`](src/brolls.ts) con el motivo de cada uno.

## Decisiones de edición

- **El audio original nunca se corta.** Los B-rolls se dibujan *encima* del gameplay y van
  muteados. Se escucha la reacción mientras se ve el insert: es lo que hace que el corte pegue.
- Cada insert dura **1.6–2.2s**, con flash blanco de entrada (4 frames), fade de salida,
  zoom lento y una etiqueta con el "chiste" del corte.
- La intro dura **4.5s** y termina con flash + punch-in que corta seco al gameplay.

## Fuentes de los B-rolls

Los 14 clips son de **[Mixkit](https://mixkit.co/free-stock-video/)**
(Mixkit License: uso libre, comercial incluido, **sin atribución obligatoria**).
Descargados a 720p, que es el máximo gratuito; se escalan a 1080p — al ser inserts de ~2s
no se nota.

> Nota: Pexels y Pixabay quedaron descartados porque su API exige key y el scraping directo
> devuelve 403.

## Estructura

```
public/
  source.mp4        gameplay transcodificado a H.264 (el .webm VP9 original es lentísimo de decodificar)
  broll/*.mp4       los 14 clips de Mixkit
src/
  Root.tsx          composiciones: FullEdit (todo) e Intro (solo la intro, para iterar rápido)
  Edit.tsx          timeline: intro + gameplay + inserts
  Intro.tsx         intro animada
  BrollInsert.tsx   un insert de B-roll
  brolls.ts         el mapa de timestamps → clips
out/edit-final.mp4  resultado
```

## Comandos

Previsualizar en el navegador (mover un B-roll de lugar es cambiar un número y ver el
resultado al instante):

```bash
cd ~/proyectos/roblox-broll-edit && npx remotion studio src/index.ts
```

Renderizar todo:

```bash
cd ~/proyectos/roblox-broll-edit && npx remotion render src/index.ts FullEdit out/edit-final.mp4 --concurrency=6 --crf=20
```

Renderizar solo la intro (~30 segundos):

```bash
cd ~/proyectos/roblox-broll-edit && npx remotion render src/index.ts Intro out/intro.mp4 --concurrency=8
```

## Qué se toca para ajustar

| Quiero... | Dónde |
|---|---|
| Cambiar el nombre de la intro | `INTRO_NAME` en `src/Intro.tsx` |
| Mover / borrar / acortar un B-roll | `src/brolls.ts` (`at`, `dur`, `trim`) |
| Cambiar los colores neon | `TEAL` / `MAGENTA` en `src/Intro.tsx` y `BrollInsert.tsx` |
| Sacar las etiquetas de texto de los inserts | borrar el bloque "Etiqueta" en `src/BrollInsert.tsx` |
| Cambiar cuánto dura la intro | `INTRO_SECONDS` en `src/Intro.tsx` |
