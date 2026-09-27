---
name: juego-batalla-real
description: "Juego battle royale web del usuario (batalla-real.html) — solo PC, estilo voxel cuadrado, nunca controles móviles"
metadata: 
  node_type: memory
  type: project
  originSessionId: 4504473e-bbff-45b1-b209-71f46b0cb272
  modified: 2026-08-04T03:45:23.085Z
---

El usuario está construyendo **BATALLA REAL**, un battle royale estilo Fortnite jugable en el navegador, en un solo archivo HTML autónomo: `/home/matiigonzz/Claude/batalla-real.html`. Motor 3D escrito a mano en canvas 2D (sin librerías). Tiene 3 pantallas conectadas: menú principal, galería de skins y gameplay en tercera persona.

Restricciones que el usuario pidió explícitamente (2026-08-04):
- **Es un juego solo para PC.** No agregar controles táctiles/móviles (botón de mira, botón de sprint, botones de construir tocables). Teclado + mouse con pointer lock.
- **Estilo visual voxel/cuadrado**, tipo Minecraft-suave: bloques rectos con esquinas apenas suavizadas (`rx=2`). Rechazó explícitamente el personaje de silueta redondeada anterior.
- Los árboles sí van con copa redonda (esa parte no debe ser cúbica).

Trampa técnica del motor: al proyectar en perspectiva se divide por la profundidad `z`, así que cualquier objeto cerca de la cámara se volvía gigante y tapaba la pantalla (árboles = todo verde, halo de cofres = todo amarillo, muro de tormenta = todo azul). La solución fue un plano cercano `NEAR=2.2` que descarta objetos, más clamps de tamaño y colisión en árboles/edificios para que el jugador no pueda meterse dentro. Si se agregan objetos nuevos al render, hay que aplicarles el mismo chequeo de `NEAR`.

Segunda trampa (2026-08-04): dibujar al jugador en **coordenadas de pantalla** (posición fija abajo del canvas) hace que parezca que *flota o vuela* cuando se mueve la cámara, porque el mundo se inclina con el pitch y él no. Todo personaje tiene que dibujarse en coordenadas del **mundo** y pasar por la misma proyección que el resto. Los personajes son cajas voxel 3D reales (18 cajas, ~3.94 unidades de alto) que rotan con su `yaw`, con nivel de detalle reducido a más de 32 unidades.

Convención de rotación del motor: el frente local del modelo es `+z`, y `forward = (sin(yaw), cos(yaw))`, `right = (cos(yaw), -sin(yaw))`. Hay que respetarla o los personajes miran para el lado equivocado.

Tercera trampa (2026-08-04): en el renderizado de cajas hay que **recortar** los polígonos contra el plano cercano (`clipN`), no descartarlos. Descartar la cara entera hace que las cosas desaparezcan al pegarte; no hacer nada hace que exploten (medido: coordenadas de 1,77 millones de píxeles). Recortar resuelve las dos cosas a la vez y permite bajar `NEAR` a 0.6.

Cuarta trampa: si una entidad queda **dentro** de una caja de colisión, todos sus movimientos se rechazan y queda congelada para siempre. Pasaba porque los edificios se generaban superpuestos. Hay tres defensas: no generar edificios que se pisen, `puedeIr()` (permite moverse si el origen ya está bloqueado) y `despegar()` (empuja fuera). Aplica igual al jugador y a los enemigos.

Detalles de render: el orden del pintor debe ser **descendente por z** (lejos primero) o se ve el interior de los edificios. Las paredes traseras se descartan comparando la posición de la cámara contra el plano de cada cara — sin eso se dibujaba el doble de ladrillos para nada (~5.265 ops/cuadro; con descarte ~3.576).

Archivos previos ya superados: `fortnite-web.html` (mapa 2D cenital) y `fortnite-3d.html` (primer intento 3D).
