---
tool: ClaudeCode
session_id: 5035c088-c2d9-4608-81d1-ee2d21015060
fecha: 2026-08-04 02:49
titulo: "Buen día Quiero crear un juego parecido en Fortnit"
tags: [chat, agente, claudecode]
---

# 💬 Buen día Quiero crear un juego parecido en Fortnit
> **ClaudeCode** · 2026-08-04 02:49 · `5035c088-c2d9-4608-81d1-ee2d21015060`

---

### 🧑 Vos  <small>2026-08-04 02:49</small>

Buen día. Quiero crear un juego parecido en Fortnite online, que se puede jugar desde la web, que, bueno, quiero que generes un pedido ahora HTML, cómo sería el el mapa, el primer mapa. Ahora no vamos a crear ningún personaje. Bueno, genés el mapa y el, bueno, el interfaz, cómo sería jugar y todo eso. ¿Cuántos mapas van a ver? Te dejo ahí tu imaginación, te doy la idea, haz todo lo que tú quieras, te te dejé ahí la idea que yo tengo, eso nomás.  Yes.

### 🤖 Claude  <small>2026-08-04 02:49</small>

Buen día. Me encanta la idea — un battle royale estilo Fortnite jugable desde el navegador. Voy a arrancar como me pediste: por ahora **sin personaje**, pero con el mapa completo, la interfaz (HUD) y toda la sensación de cómo sería jugar. Diseño **3 mapas** y dejo el primero bien detallado.

Déjame armarlo.

### 🤖 Claude  <small>2026-08-04 02:49</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-08-04 02:49</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-08-04 02:50</small>

Voy a crear un archivo nuevo (no toco el `juego-disparos.html` que ya tenés). Lo llamo `fortnite-web.html`.

### 🤖 Claude  <small>2026-08-04 02:52</small>

_[usó herramienta: Write]_

### 🧑 Vos  <small>2026-08-04 02:52</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-08-04 02:52</small>

El archivo ya está creado y abierto en el navegador. Déjame verificar que se ve bien.

### 🤖 Claude  <small>2026-08-04 02:52</small>

_[usó herramienta: mcp__Claude_Browser__computer]_

### 🧑 Vos  <small>2026-08-04 02:52</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-08-04 02:52</small>

El navegador interno no está visible ahora mismo para sacarte una captura, pero el archivo ya quedó listo y funcionando. Te dejo cómo abrirlo:

```bash
xdg-open /home/matiigonzz/Claude/fortnite-web.html
```

## Listo — te armé el prototipo: **BATALLA REAL**

Un battle royale estilo Fortnite, jugable 100% desde el navegador, en **un solo archivo HTML** (sin instalar nada). Como pediste, **todavía no hay personaje** — por ahora explorás el mapa con una cámara libre para ver *cómo se sentiría jugar* y toda la interfaz montada.

### Los 3 mapas que diseñé
1. **Isla Tormenta** 🌿 — pradera templada, ríos, lago central, 7 zonas (Torre Central, Puerto Óxido, Cañón Rojo…). Es el mapa principal, el más detallado.
2. **Ciudad Neón** 🌃 — metrópolis nocturna, cuadrícula de calles, edificios con ventanas de neón, estadio y metro abandonado.
3. **Bosque Helado** ❄️ — tundra nevada, lagos congelados, picos y minas.

Podés cambiar de mapa con los botones de arriba a la izquierda.

### La interfaz (HUD) que ves mientras "jugás"
- **Cámara libre** por todo el mapa (2000×2000).
- **Tormenta morada** que se cierra sola con temporizador (círculo seguro + círculo destino punteado), igual que Fortnite.
- **Minimapa** arriba a la derecha con tu vista, zonas, tormenta y balizas.
- **Barras de Escudo y Salud**, contador de **"98 vivos"** que va bajando.
- **Inventario de 5 armas** con colores de rareza (común→legendario).
- **Materiales**: madera / piedra / metal.
- **Bus de batalla** 🚌 que cruza el mapa con su ruta.
- **Cofres dorados** brillando y **cajas de suministro** con paracaídas.

### Controles
- **W A S D** o flechas → mover cámara · **arrastrar mouse** → explorar · **rueda** → zoom
- **1-5** → cambiar de arma · **M** → alejar/acercar mapa · **Espacio** → soltar baliza 📍

---

¿Querés que el próximo paso sea **meter un personaje jugable** que baje del bus y camine por el mapa, o preferís que primero pula más el mapa (más zonas, construcción, botín)? Decime y sigo por ahí.

### 🧑 Vos  <small>2026-08-04 02:54</small>

Mira, te cuento, está bien, me gusta que que hayan varios estos mapas, me encantan, pero hay un problema. ¿Cuál es básicamente lo que me molesta? Bueno, es que quiero que se vea, tipo, así, no sé cómo explicarlo, pero obviamente se van a bajar los gráficos, se van a dejar los gráficos, pero que se vea, tipo, de esta forma, es como un format literal, pero vamos a dejarle ultramea los gráficos. Quizás más o menos te digo, perdón, ya. No sé cómo explicarlo. pero bueno, eso.

### 🤖 Claude  <small>2026-08-04 02:55</small>

¡Ahí lo entendí perfecto! Con la imagen queda clarísimo: no querés la vista de **mapa desde arriba**, querés la vista **en tercera persona / 3D**, mirando por detrás del personaje hacia el mundo — el "formato" real de Fortnite. Los gráficos bajados (low-poly, estilizado) está perfecto, esa es la idea.

Voy a armar una versión nueva con **motor 3D en perspectiva** (hecho a mano en canvas, sin librerías externas): cielo, suelo con profundidad, edificios en 3D, árboles, el **muro de tormenta** de fondo como en tu foto, y la silueta del personaje adelante. Te dejo los 3 mapas igual.

### 🤖 Claude  <small>2026-08-04 02:57</small>

_[usó herramienta: Write]_

### 🧑 Vos  <small>2026-08-04 02:57</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-08-04 02:58</small>

¡Listo! Ahora sí está en el **formato que me mostraste** — vista en tercera persona, mirando por detrás del personaje hacia un mundo en 3D con profundidad, y el **muro de tormenta** de fondo tal como en tu imagen. Gráficos bajados / low-poly a propósito, como querías.

Abrilo así:

```bash
xdg-open /home/matiigonzz/Claude/fortnite-3d.html
```

## Qué cambió respecto a la versión anterior

**Antes:** mapa visto desde arriba (2D).
**Ahora:** cámara en 3D **detrás del personaje** (over-the-shoulder), igual que tu captura.

### Lo que vas a ver
- **Cielo con degradé + sol**, horizonte real y **suelo con perspectiva** (rejilla que se mueve mientras caminás — da la sensación de profundidad).
- **Muro de tormenta** morado/azulado rodeándote a lo lejos, como la pared brillante de tu foto.
- **Edificios en 3D** (cajas con paredes y techo, sombreado por cara) y **árboles low-poly**.
- **La silueta del personaje adelante**, desde atrás: cabeza, mochila con luz roja, hombros, arma en la mano y hasta las piernas que hacen "pasos" cuando caminás.
- **Nieve cayendo** en el mapa helado ❄️.
- Todo el **HUD** de antes: vivos, tormenta con reloj, minimapa (ahora con tu flecha girando), escudo/salud, armas y materiales.

### Controles
- **W A S D** → caminar (adelante / atrás / costados)
- **Arrastrar el mouse** → mirar alrededor (girar cámara y subir/bajar la vista)
- **Espacio** → saltar · **1-5** → cambiar de arma
- Botones arriba a la izquierda → cambiar entre los 3 mapas

---

Un par de cosas para saber, siendo honesto: como es un motor 3D hecho a mano en canvas (sin librerías), es **estilizado y simple** — los edificios pueden "recortarse" raro si te les pegás mucho, porque no tiene recorte de planos completo. Es un prototipo visual para ver el formato, no un motor pulido.

¿Cómo lo ves? Si te gusta este camino, los próximos pasos naturales serían: **texturas/colores más ricos**, que el personaje sea de verdad controlable con colisiones, o meter **enemigos y disparos**. Decime qué te tira más.

### 🧑 Vos  <small>2026-08-04 03:19</small>

no necesito, quiero que se aparezca más o menos a esto. Bueno, sacalo, por decirlo, este juego va a ser siempre sido para PC, entonces saca lo que puede ser para móvil, que haya para ese tipo lo el botón de de la mira y todo eso. Te iba a decir, nada, eso, checar que a la imagen y, bueno, si puedes redondear un poquitito más la las zonas para que no aparezca tonto Minecraft, para decirlo, pero eso. Solo redondear un poquito y ya estaría, pero sí, no llegué a estar a esos gráficos literalmente, pero eso, haz el inicio, el menú, bueno, los personajes tal cual como están ahí, y el visual del juego, por favor.

### 🤖 Claude  <small>2026-08-04 03:20</small>

¡Ahora tengo la referencia completa! Entiendo perfecto: querés las **3 pantallas** del mockup (Menú, Personajes/Skins, y Gameplay), **solo para PC** — nada de botones táctiles de móvil (mira, sprint, botones de construir a la derecha) — y **redondear un poco** las formas para que no se vea tan "Minecraft" cubudo.

Voy a rehacerlo todo en un solo archivo con las 3 pantallas conectadas entre sí.

### 🤖 Claude  <small>2026-08-04 03:23</small>

_[usó herramienta: Write]_

### 🧑 Vos  <small>2026-08-04 03:23</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-08-04 03:23</small>

¡Listo! Rehíce todo siguiendo tu mockup. Ahora es **una sola aplicación con las 3 pantallas conectadas**, pensada **solo para PC**.

Abrilo así:

```bash
xdg-open /home/matiigonzz/Claude/batalla-real.html
```

## Las 3 pantallas (como en tu imagen)

**1. INICIO (Menú principal)**
- Personaje al frente en el centro, con pedestal y su botón grande **JUGAR**.
- Barra superior: Jugar · Tienda · Equipamiento · Pase · Ajustes + monedas (1.250).
- Panel izquierdo: **Desafíos diarios** y **Pase de temporada (Nivel 12)**.
- Panel derecho: **Noticias** y **Tienda**. Abajo el botón **GRUPO +**. Diseño limpio.

**2. PERSONAJES / EQUIPAMIENTO (Skins)**
- Galería de **12 skins** (Recluta, Sombra, Comando, Neón, Escarlata, Ártico, Cazador, Fucsia, Robo, Selva, Calavera, Explorer).
- Pestañas: Trajes · Mochilas · Picos · Gestos.
- El seleccionado se marca con ✓ y borde dorado, y se ve grande en el **preview** a la derecha.
- Fila "Personaliza tu equipamiento" (traje / mochila / pico / gesto).
- **El skin que elegís acá se usa en el menú y en el juego** (aparece en la espalda del personaje).

**3. VISUAL DEL JUEGO (Gameplay)**
- Tercera persona (por detrás del personaje), **mapa más chico** para partidas rápidas.
- HUD igual al mockup: **minimapa arriba-izquierda** (con 👤 vivos / 💀 kills / ⏱ tiempo), **materiales arriba-derecha**, **inventario abajo** (armas con munición 30/45/12 + cura + escudo + granada), **barras de escudo/salud**.

## Lo que pediste específicamente
- ✅ **Saqué todo lo de móvil**: nada de botón de mira táctil ni de sprint. En su lugar hay una **mira fija en el centro** (crosshair de PC) y las piezas de construcción son teclas **F1–F4**, no botones táctiles.
- ✅ **Redondeé las formas**: personajes con esquinas redondeadas (menos "Minecraft"), **árboles con copa redonda** (círculos en vez de conos filosos), cofres y edificios con bordes suavizados.

### Controles del juego
- **W A S D** caminar · **arrastrar mouse** mirar · **1-6** arma · **Espacio** saltar · **Esc** volver al menú.

---

Un detalle honesto: los personajes del menú/skins son ilustraciones **SVG** (limpias y nítidas), mientras que el personaje dentro del juego es una silueta dibujada en el canvas 3D — parecidos pero no idénticos pixel a pixel, porque son dos técnicas distintas. Si querés te los igualo más en una próxima vuelta.

¿Lo probás y me decís qué ajustamos? Por ejemplo: afinar colores del menú, que las skins tengan los mismos detalles del mockup, o empezar a que el personaje **dispare y rompa cofres** de verdad.

### 🧑 Vos  <small>2026-08-04 03:24</small>

<local-command-caveat>Caveat: The messages below were generated by the user while running local commands. DO NOT respond to these messages or otherwise consider them in your response unless the user explicitly asks you to.</local-command-caveat>

### 🧑 Vos  <small>2026-08-04 03:24</small>

<command-name>/model</command-name>
            <command-message>model</command-message>
            <command-args>claude-opus-5</command-args>

### 🧑 Vos  <small>2026-08-04 03:24</small>

<local-command-stdout>Set model to claude-opus-5</local-command-stdout>

### 🧑 Vos  <small>2026-08-04 03:26</small>

Bueno. quiero que, básicamente, pongas el personaje que te dije, tipo el cuadrado, no quiero más este personaje que parece lo de Eugenio. Ahora, te voy a decir errores. Luego de todo, cuando muevo, como que se vuelve blanco el piso, como una especie azul. Tercero, no me hace daño la la zona. Cuarto, los departamentos, por decir, las casas, se vuelven amarilla, no sé por qué, no son, este, puras físicas, las sables también, tipo respuesta a pasar. ¿Qué más? No, disparo, no. Se mueve solo a veces, no sé por qué. También es muy chiquito. ¿Cómo lo puedo explicar? También tengo un, debe ser un error. Cuando aprieto la casa, se mueve solo, no sé por qué. Pero, bueno, cuando uso el clic izquierdo y estoy presionando así, y lo muevo para arriba, como que se me acercan todos los árboles y veo solo verde. Eso.

### 🤖 Claude  <small>2026-08-04 03:27</small>

Perfecto, entendí todos los errores. Y ya identifiqué la causa técnica de varios: cuando un objeto queda **muy cerca de la cámara**, mi cálculo de perspectiva divide por un número casi cero → el objeto se vuelve gigante y tapa la pantalla. Por eso "todo verde" (árboles), "todo amarillo" (el brillo de los cofres) y "todo azul/blanco" (el muro de tormenta). Lo arreglo con un plano cercano.

Voy a rehacer el juego completo con todo eso corregido.

### 🤖 Claude  <small>2026-08-04 03:31</small>

_[usó herramienta: Write]_

### 🧑 Vos  <small>2026-08-04 03:31</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-08-04 03:31</small>

Encontré un renglón basura que se me coló en el código de los techos. Lo limpio.

### 🤖 Claude  <small>2026-08-04 03:31</small>

_[usó herramienta: Edit]_

### 🧑 Vos  <small>2026-08-04 03:31</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-08-04 03:31</small>

Ahora déjame verificar que no haya errores de JavaScript.

### 🤖 Claude  <small>2026-08-04 03:31</small>

_[usó herramienta: mcp__Claude_Browser__read_console_messages]_

### 🧑 Vos  <small>2026-08-04 03:31</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-08-04 03:31</small>

Sin errores. Ahora verifico que la lógica del juego realmente funcione — que la tormenta haga daño, que el disparo acierte y que las colisiones anden.

### 🤖 Claude  <small>2026-08-04 03:31</small>

_[usó herramienta: mcp__Claude_Browser__javascript_tool]_

### 🧑 Vos  <small>2026-08-04 03:31</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-08-04 03:31</small>

Todo funciona. Ahora pruebo el bug principal: que los objetos **ya no se vuelvan gigantes** al acercarse o mirar hacia arriba.

### 🤖 Claude  <small>2026-08-04 03:31</small>

_[usó herramienta: mcp__Claude_Browser__javascript_tool]_

### 🧑 Vos  <small>2026-08-04 03:31</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-08-04 03:32</small>

_[usó herramienta: mcp__Claude_Browser__javascript_tool]_

### 🧑 Vos  <small>2026-08-04 03:32</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-08-04 03:32</small>

El clamp está actuando en todos los casos — quiero ver si abajo la matemática todavía explota.

### 🤖 Claude  <small>2026-08-04 03:32</small>

_[usó herramienta: mcp__Claude_Browser__javascript_tool]_

### 🧑 Vos  <small>2026-08-04 03:32</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-08-04 03:32</small>

La matemática ya **no explota** (antes se iba al infinito; ahora el peor caso está acotado). Pero detecté que **se puede caminar a través de los árboles** — por eso terminabas "dentro" de uno viendo todo verde. Les agrego colisión.

### 🤖 Claude  <small>2026-08-04 03:32</small>

_[usó herramienta: Edit]_

### 🧑 Vos  <small>2026-08-04 03:32</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-08-04 03:32</small>

_[usó herramienta: mcp__Claude_Browser__javascript_tool]_

### 🧑 Vos  <small>2026-08-04 03:33</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-08-04 03:33</small>

_[usó herramienta: mcp__Claude_Browser__javascript_tool]_

### 🧑 Vos  <small>2026-08-04 03:33</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-08-04 03:33</small>

Dos cosas más: la **cámara** (que va 8 unidades atrás) todavía puede quedar dentro de un árbol, y **5 enemigos nacen atrapados** dentro de árboles/casas. Lo arreglo.

### 🤖 Claude  <small>2026-08-04 03:33</small>

_[usó herramienta: Edit]_

### 🧑 Vos  <small>2026-08-04 03:33</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-08-04 03:33</small>

_[usó herramienta: Edit]_

### 🧑 Vos  <small>2026-08-04 03:33</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-08-04 03:33</small>

_[usó herramienta: mcp__Claude_Browser__javascript_tool]_

### 🧑 Vos  <small>2026-08-04 03:33</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-08-04 03:33</small>

_[usó herramienta: mcp__Claude_Browser__javascript_tool]_

### 🧑 Vos  <small>2026-08-04 03:33</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-08-04 03:34</small>

_[usó herramienta: mcp__Claude_Browser__javascript_tool]_

### 🧑 Vos  <small>2026-08-04 03:34</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-08-04 03:34</small>

Todo verificado. Bajo un poco el tope de las copas para que nunca dominen la pantalla, y saco una captura para ver el resultado.

### 🤖 Claude  <small>2026-08-04 03:34</small>

_[usó herramienta: Edit]_

### 🧑 Vos  <small>2026-08-04 03:34</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-08-04 03:34</small>

_[usó herramienta: mcp__Claude_Browser__computer]_

### 🧑 Vos  <small>2026-08-04 03:34</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-08-04 03:34</small>

_[usó herramienta: mcp__Claude_Browser__javascript_tool]_

### 🧑 Vos  <small>2026-08-04 03:34</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-08-04 03:34</small>

_[usó herramienta: mcp__Claude_Browser__read_console_messages]_

### 🧑 Vos  <small>2026-08-04 03:34</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-08-04 03:34</small>

Sin errores. Todo verificado funcionando.

### 🤖 Claude  <small>2026-08-04 03:34</small>

_[usó herramienta: Write]_

### 🧑 Vos  <small>2026-08-04 03:34</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-08-04 03:35</small>

_[usó herramienta: Edit]_

### 🧑 Vos  <small>2026-08-04 03:35</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-08-04 03:35</small>

_[usó herramienta: Read]_

### 🧑 Vos  <small>2026-08-04 03:35</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-08-04 03:35</small>

_[usó herramienta: Edit]_

### 🧑 Vos  <small>2026-08-04 03:35</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-08-04 03:35</small>

¡Listo! Arreglé **todos** los errores que me dijiste. Recargá la página:

```bash
xdg-open /home/matiigonzz/Claude/batalla-real.html
```

## La causa raíz de 3 de tus errores era la misma

En 3D, el tamaño en pantalla se calcula **dividiendo por la distancia**. Cuando un objeto quedaba pegadísimo a la cámara, esa distancia daba casi **cero** → el objeto se volvía **infinitamente grande** y tapaba todo. Por eso:
- **"Veo solo verde"** → un árbol gigante.
- **"Las casas se vuelven amarillas"** → no eran las casas, era el **halo dorado de un cofre** inflado a pantalla completa.
- **"El piso se vuelve blanco/azul"** → el **muro de tormenta** desbordado.

Le puse un **plano cercano** (descarta lo que está demasiado cerca) + topes de tamaño. Lo medí: antes el radio se iba al infinito, ahora queda acotado.

## Punto por punto

| Tu error | Qué hice |
|---|---|
| Personaje "de Eugenio" | ✅ **Personaje voxel cuadrado** (bloques rectos, `rx=2`), igual en menú, skins y dentro del juego |
| Piso se vuelve blanco/azul | ✅ Muro de tormenta con margen extra, ya no cubre la cámara |
| La zona no hace daño | ✅ **Hace daño real** (verificado: 100 → 97 de salud en 1 s), sube por fase, con aviso rojo y viñeta morada. Podés morir |
| Casas amarillas | ✅ Era el halo del cofre, con tope ahora |
| Casas atravesables | ✅ **Colisión** en casas *y* árboles (verificado: te frena) |
| No dispara | ✅ **Clic izquierdo dispara**, con daño, munición, fogonazo, números de daño y bajas |
| Se mueve solo | ✅ Teclas ya no se traban: uso `e.code` y limpio todo al perder el foco |
| Muy chiquito | ✅ Personaje, casas (hasta 20 de alto) y árboles más grandes |
| Arrastrar acerca los árboles | ✅ **Pointer lock**: hacés clic una vez y el mouse mira libre, sin arrastrar |

## Cómo se juega ahora
**Clic para empezar** → **WASD** moverte · **Mouse** mirar · **Clic izq** disparar · **Shift** correr · **Espacio** saltar · **R** recargar · **1-6** objetos · **Esc** pausa. Los cofres se abren solos al acercarte y te recargan munición.

Verifiqué todo ejecutando pruebas en el navegador: colisiones, daño de tormenta, disparos que restan vida y munición, y que ningún objeto desborde. **Lo único que no pude hacer es ver una captura** (el panel del navegador no está visible de mi lado), así que el juicio visual final es tuyo.

¿Qué seguimos? Lo natural sería que **los enemigos te disparen a vos** (ahora solo caminan) o meter la **construcción** de verdad con las F1-F4.

### 🧑 Vos  <small>2026-08-04 03:39</small>

que los enemigos me instalen, también me gustaría... acá, ¿eh? Me gustaría que, bueno, que los personas sean 3D, y además, cuando muevo la cámara, como que se sube, no sé cómo explicarlo, se sube el jugador, como que si vuela, arregla eso, por favor.

### 🤖 Claude  <small>2026-08-04 03:41</small>

¡Ese bug lo tengo clarísimo! El jugador estaba dibujado **pegado a la pantalla** (no en el mundo), así que al mover la cámara el suelo se movía pero él no → parecía que flotaba. Al pasarlo a **3D real en el mundo** se arregla solo. Hago las tres cosas juntas.

### 🤖 Claude  <small>2026-08-04 03:42</small>

_[usó herramienta: Edit]_

### 🧑 Vos  <small>2026-08-04 03:42</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-08-04 03:42</small>

Ahora la cámara (que siga bien el salto) y meter al jugador en el orden de profundidad del mundo.

### 🤖 Claude  <small>2026-08-04 03:42</small>

_[usó herramienta: Edit]_

### 🧑 Vos  <small>2026-08-04 03:42</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-08-04 03:42</small>

_[usó herramienta: Edit]_

### 🧑 Vos  <small>2026-08-04 03:42</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-08-04 03:42</small>

_[usó herramienta: Edit]_

### 🧑 Vos  <small>2026-08-04 03:42</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-08-04 03:42</small>

_[usó herramienta: Edit]_

### 🧑 Vos  <small>2026-08-04 03:42</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-08-04 03:42</small>

Ahora la IA de los enemigos para que **te disparen**.

### 🤖 Claude  <small>2026-08-04 03:42</small>

_[usó herramienta: Edit]_

### 🧑 Vos  <small>2026-08-04 03:42</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-08-04 03:42</small>

_[usó herramienta: Edit]_

### 🧑 Vos  <small>2026-08-04 03:42</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-08-04 03:42</small>

_[usó herramienta: Edit]_

### 🧑 Vos  <small>2026-08-04 03:42</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-08-04 03:43</small>

Ahora reemplazo el comportamiento de los enemigos (antes solo caminaban al azar):

### 🤖 Claude  <small>2026-08-04 03:43</small>

_[usó herramienta: Edit]_

### 🧑 Vos  <small>2026-08-04 03:43</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-08-04 03:43</small>

_[usó herramienta: Edit]_

### 🧑 Vos  <small>2026-08-04 03:43</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-08-04 03:43</small>

_[usó herramienta: Edit]_

### 🧑 Vos  <small>2026-08-04 03:43</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-08-04 03:43</small>

_[usó herramienta: Edit]_

### 🧑 Vos  <small>2026-08-04 03:43</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-08-04 03:43</small>

Ahora verifico todo en el navegador.

### 🤖 Claude  <small>2026-08-04 03:43</small>

_[usó herramienta: mcp__Claude_Browser__javascript_tool]_

### 🧑 Vos  <small>2026-08-04 03:43</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-08-04 03:43</small>

_[usó herramienta: mcp__Claude_Browser__read_console_messages]_

### 🧑 Vos  <small>2026-08-04 03:43</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-08-04 03:43</small>

_[usó herramienta: mcp__Claude_Browser__javascript_tool]_

### 🧑 Vos  <small>2026-08-04 03:43</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-08-04 03:44</small>

El jugador queda **clavado al suelo** en todos los ángulos de cámara (antes flotaba). Ahora pruebo que los enemigos disparen.

### 🤖 Claude  <small>2026-08-04 03:44</small>

_[usó herramienta: mcp__Claude_Browser__javascript_tool]_

### 🧑 Vos  <small>2026-08-04 03:44</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-08-04 03:44</small>

Los enemigos disparan, te encaran, se acercan y las paredes bloquean el tiro. Ahora mido el **rendimiento**, porque dibujar 12 personajes de 18 cajas cada uno puede pesar.

### 🤖 Claude  <small>2026-08-04 03:44</small>

_[usó herramienta: mcp__Claude_Browser__javascript_tool]_

### 🧑 Vos  <small>2026-08-04 03:44</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-08-04 03:44</small>

Rendimiento excelente: **3,6 ms por cuadro** (unos 277 fps de margen) con los 12 personajes en pantalla. Pero el daño era muy duro — te mataban en ~17 segundos. Lo equilibro.

### 🤖 Claude  <small>2026-08-04 03:44</small>

_[usó herramienta: Edit]_

### 🧑 Vos  <small>2026-08-04 03:44</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-08-04 03:44</small>

_[usó herramienta: Edit]_

### 🧑 Vos  <small>2026-08-04 03:44</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-08-04 03:44</small>

_[usó herramienta: mcp__Claude_Browser__javascript_tool]_

### 🧑 Vos  <small>2026-08-04 03:44</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-08-04 03:45</small>

_[usó herramienta: mcp__Claude_Browser__javascript_tool]_

### 🧑 Vos  <small>2026-08-04 03:45</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-08-04 03:45</small>

_[usó herramienta: mcp__Claude_Browser__read_console_messages]_

### 🧑 Vos  <small>2026-08-04 03:45</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-08-04 03:45</small>

_[usó herramienta: Edit]_

### 🧑 Vos  <small>2026-08-04 03:45</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-08-04 03:45</small>

¡Hecho! Las tres cosas, y las verifiqué ejecutando pruebas en el navegador. Recargá:

```bash
xdg-open /home/matiigonzz/Claude/batalla-real.html
```

## 1. El jugador ya no "vuela" ✅

**La causa:** estaba dibujado **pegado a la pantalla**, en una posición fija abajo. Entonces al mover la cámara el mundo se inclinaba pero él se quedaba clavado en el vidrio → parecía que se elevaba.

**La solución:** ahora se dibuja **en el mundo**, pasando por la misma proyección que los árboles y las casas. Lo medí en 9 ángulos de cámara distintos: sus pies quedan a **menos de 0,2 px del suelo** en todos. Además la cámara ahora sigue el salto completo (antes subía solo el 60%, lo cual también aportaba a la sensación rara).

## 2. Personajes en 3D real ✅

Ya no son dibujos planos: cada personaje son **18 cajas 3D** de ~4 unidades de alto, con caras sombreadas (arriba clarito, costados oscuros) que **giran de verdad** según hacia dónde miran. Los ves de frente, de perfil o de espaldas según cómo estén parados. Tienen sombra proyectada en el piso.

Los lejanos usan un modelo simplificado para no gastar. Medí el rendimiento en el peor caso (los 12 personajes juntos en pantalla): **3,6 ms por cuadro** — sobra muchísimo para 60 fps.

## 3. Los enemigos te disparan ✅

- Te **detectan** a menos de 46 unidades, **te encaran**, se acercan y se mueven de costado.
- **Disparan** con trazas de bala amarillas visibles; si te pegan, **flash rojo** en pantalla y perdés escudo/vida.
- Aciertan menos cuanto más lejos estás.
- **Te podés cubrir**: probé quedarme detrás de una casa 10 segundos con un enemigo disparando del otro lado → **0 de daño**. Las paredes bloquean los tiros de verdad.
- La barra de vida sobre su cabeza **se pone roja** cuando te tienen fichado.

Sobre la dificultad: al principio quedó brutal (te mataban en 17 segundos con 3 encima), así que la bajé. Ahora aguantás **~50 segundos** contra 3 enemigos simultáneos sin cubrirte ni responder — suficiente para pelear o escapar.

Tus disparos también dejan traza ahora, así que se ve el intercambio de balas.

---

Como siempre, **lo visual final lo tenés que juzgar vos** — mis pruebas confirman la lógica y la geometría, pero no puedo ver la pantalla desde acá. Si algo se ve raro, decime qué y lo ajusto.

¿Seguimos con la **construcción** (F1-F4 para poner paredes y rampas de verdad), o preferís pulir el combate?

### 🧑 Vos  <small>2026-08-05 04:02</small>

mejoralo ¡Hola! He revisado el código de tu juego y le he aplicado varias mejoras importantes, solucionado los "glitches" visuales y de mecánicas, y por supuesto, he añadido un arsenal nuevo con armas muy potentes.

### Errores corregidos y mejoras realizadas:
1. **La Tormenta se teletransportaba:** Antes, cuando el contador de la tormenta llegaba a cero, el centro del círculo daba un "salto" instantáneo, lo que provocaba que la zona segura cambiara bruscamente. Ahora, el centro de la tormenta se interpola suavemente hacia su nuevo destino (`cxDest` y `czDest`).
2. **Enemigos atascados en las casas:** El sistema de colisión de los enemigos fallaba si chocaban en diagonal, dejándolos completamente bloqueados contra las paredes. Separé la comprobación de los ejes X y Z para que los enemigos "resbalen" por las paredes y te persigan correctamente.
3. **Árboles y cofres que desaparecían de cerca:** Había un error donde si te acercabas a menos de 3.4 metros de un árbol o un cofre, su renderizado se cancelaba y se volvían invisibles. He eliminado ese límite para que puedas pegarte a ellos sin que desaparezcan.
4. **Pantalla de Victoria:** Antes, si ganabas eliminando a todos los enemigos (quedando 1 vivo), el juego no te avisaba de nada. Ahora aparece una **"¡VICTORIA!"** verde épica y podéis hacer clic para volver a jugar. Además, solucioné el error donde al morir el ratón intentaba volver a bloquearse en la pantalla.
5. **Nuevas armas (¡Mucho mejores!):**
   - **Subfusil Espectro (Raro):** Dispara increíblemente rápido, ideal para distancias cortas (40 balas).
   - **Rifle Táctico (Legendario):** Daño sólido, precisión y gran alcance (30 balas).
   - **Escopeta Pesada (Épica):** Daño brutal de cerca, puede destrozar de un solo tiro bien dado (8 balas).
   - **Francotirador AWP (Legendario):** Daño masivo (125). Destruye a cualquier enemigo de un tiro, pero recarga lento.
   - **Botiquín Médico y Poción Máxima:** Ahora curan 100 puntos en lugar de solo 40 o 50.

Aquí tienes el código completo mejorado. Simplemente guárdalo en tu archivo `.html` y pruébalo:

```html
<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>BATALLA REAL</title>
<style>
  *{box-sizing:border-box;margin:0;padding:0}
  :root{
    --bg:#0b1a2e;--panel:rgba(10,24,42,.72);--panel2:rgba(16,34,58,.92);
    --borde:rgba(255,255,255,.1);--amar:#ffcb2b;--azul:#2f9bff;--morado:#8a4cff;
    --verde:#2fbf57;--txt:#eaf2fb;--sub:#8ea6c2;
  }
  html,body{height:100%;overflow:hidden;background:#05101f;font-family:"Segoe UI",system-ui,sans-serif;color:var(--txt);user-select:none}
  .app{position:fixed;inset:0}
  .screen{position:absolute;inset:0;display:none;flex-direction:column}
  .screen.on{display:flex}
  button{font-family:inherit;cursor:pointer;border:none;background:none;color:inherit}
  canvas{display:block}
  .bgfx{position:absolute;inset:0;z-index:0;background:radial-gradient(1200px 600px at 50% -10%,#1b3a63 0%,var(--bg) 45%,#061223 100%)}
  .bgfx::after{content:"";position:absolute;inset:0;background:radial-gradient(600px 300px at 80% 90%,rgba(138,76,255,.14),transparent 60%),radial-gradient(500px 260px at 15% 80%,rgba(47,155,255,.12),transparent 60%)}

  /* ===== NAV ===== */
  .nav{position:relative;z-index:3;display:flex;align-items:center;gap:6px;padding:16px 22px}
  .logo{font-weight:900;letter-spacing:1px;font-size:20px;margin-right:14px;background:linear-gradient(90deg,#ffe07a,#ffb020);-webkit-background-clip:text;background-clip:text;color:transparent}
  .nav .item{padding:9px 16px;border-radius:9px;font-weight:800;font-size:13px;letter-spacing:.5px;color:var(--sub)}
  .nav .item:hover{color:#fff;background:rgba(255,255,255,.06)}
  .nav .item.play{background:linear-gradient(180deg,#ffd94b,#f5b021);color:#3a2600;box-shadow:0 4px 14px rgba(245,176,33,.4);display:flex;align-items:center}
  .nav .item.play svg{width:12px;height:12px;margin-right:6px}
  .nav .sp{flex:1}
  .coins{display:flex;align-items:center;gap:8px;background:var(--panel2);border:1px solid var(--borde);border-radius:10px;padding:8px 12px;font-weight:800}
  .coins .c{width:16px;height:16px;border-radius:50%;background:radial-gradient(circle at 35% 30%,#ffe98a,#e0a316);box-shadow:inset 0 0 0 2px #b9860c}
  .coins .plus{width:26px;height:26px;border-radius:8px;background:var(--verde);color:#03260f;font-weight:900;font-size:16px;display:grid;place-items:center}

  .menu-body{position:relative;z-index:2;flex:1;display:grid;grid-template-columns:270px 1fr 250px;gap:20px;padding:8px 22px 22px;min-height:0}
  .col{display:flex;flex-direction:column;gap:16px}
  .card{background:var(--panel);border:1px solid var(--borde);border-radius:14px;padding:15px;backdrop-filter:blur(7px)}
  .card h3{font-size:12px;letter-spacing:1.5px;color:var(--amar);text-transform:uppercase;margin-bottom:12px}
  .chal{margin-bottom:12px}
  .chal .row{display:flex;justify-content:space-between;font-size:13px;font-weight:700;margin-bottom:5px}
  .chal .row small{color:var(--sub);font-weight:800}
  .prog{height:7px;border-radius:6px;background:rgba(255,255,255,.1);overflow:hidden}
  .prog i{display:block;height:100%;background:linear-gradient(90deg,var(--azul),#7fd0ff)}
  .pase .lv{display:flex;align-items:center;gap:9px;margin-bottom:9px}
  .pase .badge{width:34px;height:34px;border-radius:9px;background:linear-gradient(180deg,#a06bff,#6b34d6);display:grid;place-items:center}
  .pase .badge svg{width:18px;height:18px}
  .pase .lv b{font-size:15px}.pase .lv span{font-size:11px;color:var(--sub);display:block}
  .noti{background:linear-gradient(135deg,#20518f,#153864);border-radius:10px;padding:12px}
  .noti .tag{font-size:10px;letter-spacing:1px;color:#9fd0ff;text-transform:uppercase}
  .noti b{display:block;margin-top:4px;font-size:14px}
  .store-mini{display:flex;align-items:center;gap:12px}
  .store-mini .gun{width:60px;height:56px;border-radius:10px;background:linear-gradient(135deg,#3a2a6b,#7a4cd6);display:grid;place-items:center}
  .store-mini .gun svg{width:26px;height:26px}
  .center{position:relative;display:flex;flex-direction:column;align-items:center;justify-content:flex-end}
  .pedestal{position:absolute;bottom:96px;width:340px;height:80px;border-radius:50%;background:radial-gradient(ellipse,rgba(47,155,255,.35),transparent 70%);filter:blur(4px)}
  .hero{position:relative;z-index:2;height:60vh;max-height:520px;filter:drop-shadow(0 24px 30px rgba(0,0,0,.55))}
  .hero svg{height:100%}
  .play-big{position:relative;z-index:3;margin-top:6px;width:270px;padding:16px;border-radius:12px;background:linear-gradient(180deg,#ffd94b,#f2a80f);color:#3a2600;font-weight:900;font-size:22px;letter-spacing:2px;box-shadow:0 10px 26px rgba(242,168,15,.45);transition:.12s}
  .play-big:hover{transform:translateY(-2px)}
  .grupo{position:absolute;left:0;bottom:0;display:flex;align-items:center;gap:8px;font-weight:800;font-size:12px;color:var(--sub)}
  .grupo .add{width:34px;height:34px;border-radius:9px;border:1px dashed var(--borde);display:grid;place-items:center;font-size:18px}

  /* ===== SKINS ===== */
  .sk-head{position:relative;z-index:3;display:flex;align-items:center;gap:14px;padding:16px 22px}
  .back{width:40px;height:40px;border-radius:10px;background:var(--panel2);border:1px solid var(--borde);font-size:20px;display:grid;place-items:center}
  .sk-head h2{font-weight:900;letter-spacing:1px;font-size:20px}
  .tabs{position:relative;z-index:3;display:flex;gap:10px;padding:0 22px 10px}
  .tab{padding:9px 18px;border-radius:9px;font-weight:800;font-size:12px;letter-spacing:1px;color:var(--sub);background:var(--panel)}
  .tab.on{background:linear-gradient(180deg,#ffd94b,#f2a80f);color:#3a2600}
  .sk-body{position:relative;z-index:2;flex:1;display:grid;grid-template-columns:1fr 380px;gap:22px;padding:6px 22px 22px;min-height:0}
  .grid{display:grid;grid-template-columns:repeat(4,1fr);gap:14px;align-content:start;overflow:auto;padding-right:6px}
  .skin{position:relative;border:2px solid var(--borde);border-radius:14px;background:linear-gradient(180deg,#12294a,#0c1c34);display:grid;place-items:center;aspect-ratio:1/1;overflow:hidden;transition:.12s}
  .skin:hover{border-color:var(--azul);transform:translateY(-2px)}
  .skin.sel{border-color:var(--amar);box-shadow:0 0 0 2px rgba(255,203,43,.25)}
  .skin svg{height:84%}
  .skin .chk{position:absolute;top:6px;right:6px;width:22px;height:22px;border-radius:50%;background:var(--verde);color:#03260f;display:none;place-items:center;font-weight:900;font-size:13px}
  .skin.sel .chk{display:grid}
  .preview{border:1px solid var(--borde);border-radius:16px;background:radial-gradient(600px 400px at 50% 10%,#173257,#0a1a30);display:flex;flex-direction:column;align-items:center;justify-content:center;position:relative}
  .preview svg{height:62vh;max-height:400px;filter:drop-shadow(0 20px 24px rgba(0,0,0,.5))}
  .preview .nm{position:absolute;bottom:96px;font-weight:900;letter-spacing:1px;font-size:16px}
  .custom{position:absolute;bottom:16px;display:flex;gap:10px}
  .custom .it{width:58px;height:58px;border-radius:11px;border:2px solid var(--borde);background:var(--panel2);display:grid;place-items:center;color:var(--sub)}
  .custom .it svg{width:26px;height:26px}
  .custom .it.on{border-color:var(--amar);color:var(--amar)}

  /* ===== GAMEPLAY ===== */
  #glienzo{position:absolute;inset:0;width:100%;height:100%;z-index:0;cursor:crosshair}
  .ghud{position:absolute;z-index:5;pointer-events:none;text-shadow:0 2px 4px rgba(0,0,0,.7)}
  .g-mini{top:14px;left:14px}
  .g-mini .p{background:var(--panel2);border:1px solid var(--borde);border-radius:12px;padding:8px}
  .g-mini canvas{width:150px;height:150px;border-radius:8px;display:block}
  .g-stats{display:flex;gap:12px;margin-top:7px;font-size:12px;font-weight:800;justify-content:center}
  .g-stats .si{display:flex;align-items:center;gap:5px}
  .g-stats svg{width:13px;height:13px}
  .g-mats{top:14px;right:14px;display:flex;gap:8px}
  .g-mat{background:var(--panel2);border:1px solid var(--borde);border-radius:10px;padding:7px 11px;display:flex;align-items:center;gap:7px;font-weight:800}
  .g-mat .sw{width:14px;height:14px;border-radius:4px}
  .g-bottom{left:14px;bottom:14px;display:flex;flex-direction:column;gap:8px}
  .g-inv{display:flex;gap:7px}
  .g-slot{width:64px;height:60px;border:2px solid var(--borde);border-radius:10px;background:var(--panel2);position:relative;display:flex;flex-direction:column;align-items:center;justify-content:center;pointer-events:auto;cursor:pointer}
  .g-slot .k{position:absolute;top:2px;left:5px;font-size:9px;opacity:.5;font-weight:800}
  .g-slot .ic{font-size:22px}
  .g-slot .am{position:absolute;bottom:2px;right:5px;font-size:11px;font-weight:900}
  .g-slot.sel{border-color:var(--amar)!important;box-shadow:0 0 16px rgba(255,203,43,.4);color:var(--amar)}
  .g-slot{color:#eaf2fb}.g-slot .ic svg{width:30px;height:30px}
  .g-bars{width:330px}
  .g-bar{height:16px;border-radius:8px;background:rgba(0,0,0,.55);border:1px solid var(--borde);overflow:hidden;position:relative;margin-top:6px}
  .g-bar i{display:block;height:100%;transition:width .15s}
  .g-bar.esc i{background:linear-gradient(90deg,#5fd0ff,#2f9bff)}
  .g-bar.sal i{background:linear-gradient(90deg,#3fe06f,#1ba84a)}
  .g-bar span{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;font-size:11px;font-weight:900}
  .g-exit{top:14px;left:50%;transform:translateX(-50%);pointer-events:auto;background:var(--panel2);border:1px solid var(--borde);border-radius:9px;padding:8px 14px;font-weight:800;font-size:12px;letter-spacing:1px;display:flex;align-items:center;gap:6px}
  .g-exit svg{width:12px;height:12px}
  .g-exit:hover{border-color:#e5484d}
  .g-aviso{top:60px;left:50%;transform:translateX(-50%);background:rgba(138,76,255,.92);border-radius:9px;padding:7px 16px;font-weight:800;opacity:0;transition:.35s;display:flex;align-items:center;gap:7px}
  .g-aviso svg{width:12px;height:12px}
  .g-aviso.show{opacity:1}
  .g-dmg{top:112px;left:50%;transform:translateX(-50%);background:rgba(190,40,60,.92);border-radius:9px;padding:7px 16px;font-weight:900;letter-spacing:1px;display:none;align-items:center;gap:7px}
  .g-dmg svg{width:13px;height:13px}
  .g-dmg.show{display:flex;animation:blink .7s infinite}
  @keyframes blink{50%{opacity:.45}}
  .g-build{right:14px;bottom:14px;display:flex;gap:7px}
  .g-bp{width:52px;height:52px;border:2px solid var(--borde);border-radius:10px;background:var(--panel2);display:flex;flex-direction:column;align-items:center;justify-content:center;gap:2px}
  .g-bp .k{font-size:9px;opacity:.6;font-weight:800}
  .g-bp svg{width:24px;height:20px}
  .g-lock{left:50%;top:50%;transform:translate(-50%,-50%);background:rgba(6,14,26,.88);border:1px solid var(--borde);border-radius:14px;padding:20px 28px;text-align:center;font-weight:800;line-height:1.7}
  .g-lock small{display:block;font-weight:600;color:var(--sub);font-size:12px;margin-top:6px}
  .g-lock.hide{display:none}
  .key{display:inline-block;min-width:20px;text-align:center;padding:1px 7px;border:1px solid var(--borde);border-radius:5px;background:rgba(255,255,255,.07);font-weight:800;font-size:11px}
</style>
</head>
<body>
<div class="app">

  <!-- ================= 1. MENÚ ================= -->
  <div class="screen on" id="menu">
    <div class="bgfx"></div>
    <div class="nav">
      <div class="logo">BATALLA REAL</div>
      <button class="item play" onclick="go('game')"><svg viewBox="0 0 24 24" fill="currentColor"><path d="M7.5 4.5l13 7.5-13 7.5z"/></svg>JUGAR</button>
      <button class="item">TIENDA</button>
      <button class="item" onclick="go('skins')">EQUIPAMIENTO</button>
      <button class="item">PASE</button>
      <button class="item">AJUSTES</button>
      <div class="sp"></div>
      <div class="coins"><span class="c"></span>1.250<span class="plus">+</span></div>
    </div>
    <div class="menu-body">
      <div class="col">
        <div class="card"><h3>Desafíos diarios</h3>
          <div class="chal"><div class="row">Elimina 5 enemigos <small id="d1">0/5</small></div><div class="prog"><i id="d1b" style="width:0%"></i></div></div>
          <div class="chal"><div class="row">Abre 3 cofres <small id="d2">0/3</small></div><div class="prog"><i id="d2b" style="width:0%"></i></div></div>
          <div class="chal"><div class="row">Sobrevive 10 min <small>4/10</small></div><div class="prog"><i style="width:40%"></i></div></div>
        </div>
        <div class="card pase"><h3>Pase de temporada</h3>
          <div class="lv"><div class="badge"><svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 2l8.5 3.2v6c0 5.2-3.6 9.5-8.5 10.8C7.1 20.7 3.5 16.4 3.5 11.2V5.2z"/></svg></div><div><b>Nivel 12</b><span>350 / 1.000 XP</span></div></div>
          <div class="prog"><i style="width:35%;background:linear-gradient(90deg,#a06bff,#6b34d6)"></i></div>
        </div>
      </div>
      <div class="center">
        <div class="pedestal"></div>
        <div class="hero" id="heroChar"></div>
        <button class="play-big" onclick="go('game')">JUGAR</button>
        <div class="grupo"><span>GRUPO</span><div class="add">+</div></div>
      </div>
      <div class="col">
        <div class="card"><h3>Noticias</h3><div class="noti"><span class="tag">Evento</span><b>¡Nuevo evento disponible!</b></div></div>
        <div class="card"><h3>Tienda</h3><div class="store-mini"><div class="gun"><svg viewBox="0 0 24 24" fill="currentColor"><rect x="3" y="10.5" width="11" height="4" rx="1.5"/><rect x="12.5" y="11.5" width="8.5" height="2" rx="1"/><path d="M4.5 14.5h9.5v2.6a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2z"/></svg></div><div><b>Rifle Vórtice</b><div style="font-size:11px;color:var(--sub);margin-top:3px">800 monedas</div></div></div></div>
      </div>
    </div>
  </div>

  <!-- ================= 2. SKINS ================= -->
  <div class="screen" id="skins">
    <div class="bgfx"></div>
    <div class="sk-head"><button class="back" onclick="go('menu')">‹</button><h2>EQUIPAMIENTO</h2></div>
    <div class="tabs"><button class="tab on">TRAJES</button><button class="tab">MOCHILAS</button><button class="tab">PICOS</button><button class="tab">GESTOS</button></div>
    <div class="sk-body">
      <div class="grid" id="grid"></div>
      <div class="preview">
        <div id="prevChar"></div>
        <div class="nm" id="prevName">Recluta</div>
        <div class="custom"><div class="it on"><svg viewBox="0 0 24 24" fill="currentColor"><circle cx="12" cy="7.5" r="4"/><path d="M4 21c1.6-4.2 4.6-6.3 8-6.3s6.4 2.1 8 6.3z"/></svg></div><div class="it"><svg viewBox="0 0 24 24" fill="currentColor"><path d="M7.5 7.5h9V21h-9z"/><path d="M9.5 7.5a2.5 2.5 0 0 1 5 0z"/><rect x="9.5" y="12.5" width="5" height="3.6" rx="1" opacity=".45"/></svg></div><div class="it"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M12 21l2.6-9.5"/><path d="M6 7.5c0-2 1.7-3.4 3.6-3.4h4.8c1.9 0 3.6 1.4 3.6 3.4L15.5 10h-7z" fill="currentColor" stroke="none"/></svg></div><div class="it"><svg viewBox="0 0 24 24" fill="currentColor"><path d="M9.5 18.5V6l10-2.2v10.6"/><circle cx="7.2" cy="18.5" r="2.6"/><circle cx="17.5" cy="14.4" r="2.6"/></svg></div></div>
      </div>
    </div>
  </div>

  <!-- ================= 3. GAMEPLAY ================= -->
  <div class="screen" id="game">
    <canvas id="glienzo"></canvas>
    <button class="ghud g-exit" onclick="salirJuego()"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"><path d="M12 3v8.5"/><path d="M6.2 6.8a8.2 8.2 0 1 0 11.6 0"/></svg>SALIR</button>
    <div class="ghud g-aviso" id="gaviso"><svg viewBox="0 0 24 24" fill="currentColor"><path d="M13.5 2L4 14.5h6L9 22l9.5-12.5h-6z"/></svg>LA TORMENTA SE CIERRA</div>
    <div class="ghud g-dmg" id="gdmg"><svg viewBox="0 0 24 24" fill="currentColor"><path fill-rule="evenodd" d="M12 5.5a8 8 0 0 1 8 8c0 2.8-1.6 4.7-3.3 5.7V21.5h-9.4v-2.3C5.6 18.2 4 16.3 4 13.5a8 8 0 0 1 8-8zM9.4 12.2a1.7 1.7 0 1 0 0 3.4 1.7 1.7 0 0 0 0-3.4zm5.2 0a1.7 1.7 0 1 0 0 3.4 1.7 1.7 0 0 0 0-3.4zM12 17.2l-1 .9 1 1 1-1z"/></svg>¡ESTÁS EN LA TORMENTA! CORRÉ AL CÍRCULO</div>

    <div class="ghud g-mini"><div class="p">
      <canvas id="gmini" width="150" height="150"></canvas>
      <div class="g-stats"><span class="si"><svg viewBox="0 0 24 24" fill="currentColor"><circle cx="12" cy="7.5" r="4"/><path d="M4 21c1.6-4.2 4.6-6.3 8-6.3s6.4 2.1 8 6.3z"/></svg><b id="gvivos">12</b></span><span class="si"><svg viewBox="0 0 24 24" fill="currentColor"><path fill-rule="evenodd" d="M12 5.5a8 8 0 0 1 8 8c0 2.8-1.6 4.7-3.3 5.7V21.5h-9.4v-2.3C5.6 18.2 4 16.3 4 13.5a8 8 0 0 1 8-8zM9.4 12.2a1.7 1.7 0 1 0 0 3.4 1.7 1.7 0 0 0 0-3.4zm5.2 0a1.7 1.7 0 1 0 0 3.4 1.7 1.7 0 0 0 0-3.4zM12 17.2l-1 .9 1 1 1-1z"/></svg><b id="gkills">0</b></span><span class="si"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"><circle cx="12" cy="12" r="8.5"/><path d="M12 7.5V12l3 2"/></svg><b id="greloj">1:25</b></span></div>
    </div></div>

    <div class="ghud g-mats">
      <div class="g-mat"><span class="sw" style="background:#c99a5b"></span><b id="mMad">120</b></div>
      <div class="g-mat"><span class="sw" style="background:#b5581f"></span><b id="mLad">80</b></div>
      <div class="g-mat"><span class="sw" style="background:#9aa2ac"></span><b id="mMet">60</b></div>
    </div>

    <div class="ghud g-bottom">
      <div class="g-inv" id="ginv"></div>
      <div class="g-bars">
        <div class="g-bar esc"><i id="gesc" style="width:75%"></i><span id="gescT">75 / 100</span></div>
        <div class="g-bar sal"><i id="gsal" style="width:100%"></i><span id="gsalT">100 / 100</span></div>
      </div>
    </div>

    <div class="ghud g-build">
      <div class="g-bp"><span class="k">F1</span><svg viewBox="0 0 24 20"><rect x="3" y="2" width="18" height="16" rx="2" fill="none" stroke="#cfe4ff" stroke-width="2"/></svg></div>
      <div class="g-bp"><span class="k">F2</span><svg viewBox="0 0 24 20"><path d="M2 14 L22 14 L18 6 L6 6 Z" fill="none" stroke="#cfe4ff" stroke-width="2" stroke-linejoin="round"/></svg></div>
      <div class="g-bp"><span class="k">F3</span><svg viewBox="0 0 24 20"><path d="M3 17 L14 17 L21 4" fill="none" stroke="#cfe4ff" stroke-width="2" stroke-linejoin="round"/></svg></div>
      <div class="g-bp"><span class="k">F4</span><svg viewBox="0 0 24 20"><path d="M2 15 L12 3 L22 15 Z" fill="none" stroke="#cfe4ff" stroke-width="2" stroke-linejoin="round"/></svg></div>
    </div>

    <div class="ghud g-lock" id="glock">
      CLIC PARA JUGAR
      <small><span class="key">W</span><span class="key">A</span><span class="key">S</span><span class="key">D</span> moverse · Mouse mirar · Clic izq. disparar<br>
      <span class="key">Espacio</span> saltar · <span class="key">1-6</span> objetos · <span class="key">Esc</span> pausa</small>
    </div>
  </div>
</div>

<script>
/* ============================================================
   1) PERSONAJE VOXEL (cuadrado, estilo del mockup)
   ============================================================ */
const SKINS=[
 {nm:"Recluta",  piel:"#e0a878",pelo:"#4a3524",traje:"#4f6b39",traje2:"#33472a",bota:"#3d2f22",acc:"#2b3340"},
 {nm:"Sombra",   piel:"#d69a6e",pelo:"#2a1d14",traje:"#6a3fb0",traje2:"#43266f",bota:"#241736",acc:"#9b6bff",capucha:true},
 {nm:"Comando",  piel:"#c98f63",pelo:"#1c1c1c",traje:"#2b303a",traje2:"#191d24",bota:"#12151a",acc:"#3fd0ff",casco:true},
 {nm:"Neón",     piel:"#e6b088",pelo:"#2f7bff",traje:"#26324a",traje2:"#182236",bota:"#101724",acc:"#3fd0ff"},
 {nm:"Escarlata",piel:"#dda074",pelo:"#5a1f1f",traje:"#b23838",traje2:"#7c2222",bota:"#3d1414",acc:"#ffcf4d"},
 {nm:"Ártico",   piel:"#dca97e",pelo:"#c9d6e0",traje:"#cad2da",traje2:"#98a1ab",bota:"#5c646d",acc:"#5fd0ff"},
 {nm:"Cazador",  piel:"#c98a5c",pelo:"#3a2c1e",traje:"#8a6630",traje2:"#5a411d",bota:"#33260f",acc:"#e0c05a",gafas:true},
 {nm:"Fucsia",   piel:"#e6ad86",pelo:"#ff56b0",traje:"#3f2c5a",traje2:"#281839",bota:"#1a1024",acc:"#ff56b0"},
 {nm:"Robo",     piel:"#96a0a8",pelo:"#20262e",traje:"#242c36",traje2:"#151b22",bota:"#0e1218",acc:"#3fd0ff",robot:true},
 {nm:"Selva",    piel:"#c98a5c",pelo:"#313d24",traje:"#44603a",traje2:"#2b3d24",bota:"#1e2a18",acc:"#8cbf50"},
 {nm:"Calavera", piel:"#ececec",pelo:"#1a1a1a",traje:"#1f232b",traje2:"#12151b",bota:"#0a0c10",acc:"#c8c8c8",craneo:true},
 {nm:"Explorer", piel:"#d99b6a",pelo:"#c85a1f",traje:"#2f4056",traje2:"#1c2938",bota:"#141d28",acc:"#ff8a3c",gorra:true},
];

/* r=2 → esquinas apenas suavizadas: se ve cuadrado/voxel, no redondeado */
function charSVG(p){
  const R=2;
  const cara = p.craneo
    ? `<rect x="46" y="52" width="8" height="9" rx="1" fill="#15161a"/><rect x="66" y="52" width="8" height="9" rx="1" fill="#15161a"/><rect x="54" y="66" width="12" height="5" rx="1" fill="#15161a"/>`
    : p.robot
    ? `<rect x="43" y="50" width="34" height="10" rx="2" fill="${p.acc}"/><rect x="43" y="50" width="34" height="4" rx="1" fill="#fff" opacity=".35"/>`
    : `<rect x="48" y="53" width="7" height="8" rx="1" fill="#2a1f17"/><rect x="65" y="53" width="7" height="8" rx="1" fill="#2a1f17"/>`;
  let cabezaExtra='';
  if(p.casco) cabezaExtra=`<rect x="42" y="34" width="36" height="18" rx="${R}" fill="${p.traje2}"/><rect x="42" y="45" width="36" height="6" fill="${p.acc}" opacity=".55"/>`;
  else if(p.capucha) cabezaExtra=`<rect x="40" y="32" width="40" height="30" rx="${R}" fill="${p.traje}"/><rect x="47" y="44" width="26" height="22" rx="${R}" fill="#1a1220"/>`;
  else if(p.gorra) cabezaExtra=`<rect x="42" y="32" width="36" height="12" rx="${R}" fill="${p.acc}"/><rect x="42" y="42" width="46" height="5" rx="${R}" fill="${p.acc}"/>`;
  else if(!p.craneo&&!p.robot) cabezaExtra=`<rect x="42" y="33" width="36" height="16" rx="${R}" fill="${p.pelo}"/>`;
  const gafas=p.gafas?`<rect x="44" y="50" width="32" height="9" rx="1" fill="#12100c"/>`:'';
  return `<svg viewBox="0 0 120 232" xmlns="http://www.w3.org/2000/svg" shape-rendering="geometricPrecision">
    <rect x="44" y="152" width="15" height="52" rx="${R}" fill="${p.traje2}"/>
    <rect x="61" y="152" width="15" height="52" rx="${R}" fill="${p.traje2}"/>
    <rect x="43" y="202" width="17" height="16" rx="${R}" fill="${p.bota}"/>
    <rect x="60" y="202" width="17" height="16" rx="${R}" fill="${p.bota}"/>
    <rect x="26" y="90" width="16" height="42" rx="${R}" fill="${p.traje2}"/>
    <rect x="26" y="128" width="16" height="20" rx="${R}" fill="${p.piel}"/>
    <rect x="78" y="90" width="16" height="42" rx="${R}" fill="${p.traje2}"/>
    <rect x="78" y="128" width="16" height="20" rx="${R}" fill="${p.piel}"/>
    <rect x="38" y="88" width="44" height="66" rx="${R}" fill="${p.traje}"/>
    <rect x="38" y="88" width="44" height="14" rx="${R}" fill="#000" opacity=".16"/>
    <path d="M44 90 L74 152" stroke="${p.acc}" stroke-width="7" opacity=".9"/>
    <rect x="52" y="114" width="17" height="15" rx="${R}" fill="${p.acc}"/>
    <rect x="34" y="86" width="16" height="14" rx="${R}" fill="${p.traje2}"/>
    <rect x="70" y="86" width="16" height="14" rx="${R}" fill="${p.traje2}"/>
    <rect x="54" y="78" width="12" height="12" rx="${R}" fill="${p.piel}"/>
    <rect x="43" y="42" width="34" height="38" rx="${R}" fill="${p.piel}"/>
    ${cabezaExtra}${cara}${gafas}
  </svg>`;
}

let skinSel=0;
function pintarGaleria(){
  const g=document.getElementById('grid');g.innerHTML='';
  SKINS.forEach((s,i)=>{
    const d=document.createElement('button');d.className='skin'+(i===skinSel?' sel':'');
    d.innerHTML=charSVG(s)+'<div class="chk">✓</div>';
    d.onclick=()=>{skinSel=i;aplicarSkin();};
    g.appendChild(d);
  });
}
function aplicarSkin(){
  document.getElementById('heroChar').innerHTML=charSVG(SKINS[skinSel]);
  document.getElementById('prevChar').innerHTML=charSVG(SKINS[skinSel]);
  document.getElementById('prevName').textContent=SKINS[skinSel].nm;
  document.querySelectorAll('#grid .skin').forEach((el,i)=>el.classList.toggle('sel',i===skinSel));
}
pintarGaleria();aplicarSkin();

/* ============================================================
   2) NAVEGACIÓN
   ============================================================ */
let pantalla='menu';
function go(id){
  document.querySelectorAll('.screen').forEach(s=>s.classList.remove('on'));
  document.getElementById(id).classList.add('on');
  pantalla=id; limpiarTeclas();
  if(id==='game'){resize();nuevaPartida();}
}
function salirJuego(){ if(document.pointerLockElement)document.exitPointerLock(); go('menu'); }

/* ============================================================
   3) MOTOR 3D
   ============================================================ */
const gcv=document.getElementById('glienzo'), gctx=gcv.getContext('2d');
const gmc=document.getElementById('gmini'), gmx=gmc.getContext('2d');
let W=1,H=1,dpr=Math.min(devicePixelRatio||1,2);
function resize(){W=gcv.clientWidth||1;H=gcv.clientHeight||1;gcv.width=W*dpr;gcv.height=H*dpr;gctx.setTransform(dpr,0,0,dpr,0,0);}
addEventListener('resize',()=>{if(pantalla==='game')resize();});

const NEAR=2.2;              // *** plano cercano: evita objetos gigantes ***
const MUNDO=150, LIM=68;
const FOC=()=>0.9*H;

const MG={cieloTop:"#2b6fc4",cieloBot:"#cfeaff",suelo:"#4a8a45",sueloLejos:"#6cab60",
  arbol:"#2f8f45",arbolTop:"#43a755",
  pois:[[0,0,"Torre Central"],[-42,34,"Molino"],[44,-32,"Puerto Óxido"],[40,42,"Cañón Rojo"]]};
const LADR_COLS=['#8a6d4c','#7d6244','#947857','#85684a','#7a5f41','#907453'];
const PASTO_COL=['#3d8f3f','#479c45','#2f7f38','#57a94e','#3a7c35','#69b258'];

function rng(s){s>>>=0;return()=>{s=(s*1664525+1013904223)>>>0;return s/4294967296;}}
let edificios=[],arboles=[],cofres=[],enemigos=[],tracers=[],impactos=[],pastos=[],flores=[];
let flashRojo=0;

function generarMundo(){
  const r=rng(2024);edificios=[];arboles=[];cofres=[];enemigos=[];tracers=[];impactos=[];
  MG.pois.forEach((p,pi)=>{
    const n=3+Math.floor(r()*3);
    for(let i=0;i<n;i++){const a=r()*6.28,d=6+r()*10;
      const w=7+r()*7,dd=7+r()*7,h=9+r()*11;
      const ed={x:p[0]+Math.cos(a)*d,z:p[1]+Math.sin(a)*d,w,d:dd,h,
        tipo:edTipo(pi,r),mat:edMat(pi,r)};
      if(ed.tipo==='casa'&&ed.w<=ed.d&&r()<0.75){
        ed.ch=true;ed.chx=ed.x-ed.w*0.24;ed.cz=ed.z;ed.rh=Math.min(3.6,1.8+h*0.22);
      }else ed.rh=Math.min(3.4,1.6+h*0.2);
      edificios.push(ed);}
    for(let i=0;i<2;i++){const a=r()*6.28,d=r()*11;
      cofres.push({x:p[0]+Math.cos(a)*d,z:p[1]+Math.sin(a)*d,abierto:false});}
  });
  for(let i=0;i<130;i++){
    const x=(r()-.5)*MUNDO, z=(r()-.5)*MUNDO;
    if(edificios.some(e=>Math.abs(x-e.x)<e.w&&Math.abs(z-e.z)<e.d))continue;
    arboles.push({x,z,h:7+r()*5,w:3.2+r()*1.8});
  }
  pastos=[];flores=[];
  for(let i=0;i<520;i++){
    const x=(r()-.5)*MUNDO, z=(r()-.5)*MUNDO;
    if(edificios.some(e=>Math.abs(x-e.x)<e.w+1.5&&Math.abs(z-e.z)<e.d+1.5))continue;
    pastos.push({x,z,h:0.3+r()*0.28,lean:(r()-.5)*0.6,fase:r()*6.28,
      tipo:Math.floor(r()*PASTO_COL.length),v:r()});
  }
  for(let i=0;i<96;i++){
    const x=(r()-.5)*MUNDO, z=(r()-.5)*MUNDO;
    if(edificios.some(e=>Math.abs(x-e.x)<e.w+1.5&&Math.abs(z-e.z)<e.d+1.5))continue;
    flores.push({x,z,h:0.32,c:['#e5484d','#ffcb2b','#ffffff','#b57fff'][Math.floor(r()*4)],fase:r()*6.28});
  }
  for(let i=0;i<11;i++){
    let x=0,z=0;                                  // buscar un lugar libre
    for(let intento=0;intento<40;intento++){
      const a=r()*6.28,d=20+r()*45;
      x=Math.cos(a)*d; z=Math.sin(a)*d;
      if(!colisiona(x,z))break;
    }
    enemigos.push({x,z,vida:100,skin:1+Math.floor(r()*11),yaw:r()*6.28,t:r()*5,
      vivo:true,alerta:false,cool:1+r()*2,fase:r()*6.28});
  }
}

/* --- jugador --- */
const P={x:0,z:-26,yaw:0,y:0,vy:0,salud:100,escudo:75,kills:0,cofres:0};
let pitch=0.22, muerto=false;
const RAD=1.6;               // radio de colisión

/* --- teclado (a prueba de teclas pegadas) --- */
const keys={};
function limpiarTeclas(){for(const k in keys)keys[k]=false;}
addEventListener('blur',limpiarTeclas);
document.addEventListener('visibilitychange',()=>{if(document.hidden)limpiarTeclas();});
addEventListener('keydown',e=>{
  if(pantalla!=='game')return;
  keys[e.code]=true;
  if(e.code.startsWith('Digit')){const n=+e.code.slice(5);if(n>=1&&n<=6){armaSel=n-1;pintGInv();}}
  if(e.code==='Space'){if(P.y<=0.01&&!muerto)P.vy=8;e.preventDefault();}
  if(e.code==='KeyR')recargar();
});
addEventListener('keyup',e=>{keys[e.code]=false;});

/* --- mouse: pointer lock (evita el bug de arrastrar) --- */
const lockMsg=document.getElementById('glock');
gcv.addEventListener('click',()=>{
  if(pantalla==='game'&&!document.pointerLockElement&&!muerto&&gvivos>1) gcv.requestPointerLock();
});
document.addEventListener('pointerlockchange',()=>{
  const on=document.pointerLockElement===gcv;
  lockMsg.classList.toggle('hide',on);
  if(!on)limpiarTeclas();
});
document.addEventListener('mousemove',e=>{
  if(document.pointerLockElement!==gcv)return;
  P.yaw+=e.movementX*0.0022;
  pitch=Math.max(-0.35,Math.min(0.55,pitch+e.movementY*0.0018));
});
document.addEventListener('mousedown',e=>{
  if(document.pointerLockElement!==gcv)return;
  if(e.button===0)disparando=true;
});
document.addEventListener('mouseup',e=>{if(e.button===0)disparando=false;});

/* --- proyección --- */
const cam={x:0,y:0,z:0};
function proj(px,py,pz){
  const dx=px-cam.x,dy=py-cam.y,dz=pz-cam.z;
  const cy=Math.cos(P.yaw),sy=Math.sin(P.yaw);
  const x1=dx*cy-dz*sy, z1=dx*sy+dz*cy, y1=dy;
  const cp=Math.cos(pitch),sp=Math.sin(pitch);
  return {x:x1,y:y1*cp-z1*sp,z:y1*sp+z1*cp};
}
function scr(c){const f=FOC();return{x:W/2+c.x*f/c.z,y:H/2-c.y*f/c.z};}

/* --- tormenta --- */
let storm={cx:0,cz:0,cxDest:0,czDest:0,r:80,rDest:80,t:75,fase:0};
function resetStorm(){storm={cx:0,cz:0,cxDest:0,czDest:0,r:82,rDest:82,t:75,fase:0};}

/* --- armas --- */
const RAR={
  comun:{c:'#c0c5cc',t:'Común'},poco:{c:'#62d15d',t:'Poco común'},
  raro:{c:'#3fa7ff',t:'Raro'},epico:{c:'#b64cff',t:'Épico'},legend:{c:'#ffcf40',t:'Legendario'},
};
const SVG={
  subfusil:'<svg viewBox="0 0 24 24" fill="currentColor"><path d="M3 13h10v3H3z"/><path d="M13 12h6v4h-6z"/><path d="M11 16h3v5h-3z"/><path d="M19 12h3v4h-3z"/><rect x="5" y="14" width="6" height="1" fill="#fff" opacity="0.3"/></svg>',
  rifle:'<svg viewBox="0 0 24 24" fill="currentColor"><path d="M3 15.5h4l1.5 1.2 3-.6 1.8 1H18a1.8 1.8 0 0 1 1.8 1.8v1H17l-2.5 2H9l-4.5-3.5H3z"/><path d="M7 10.5h6l2 1.5-4 .8-1.5-1.3H7z"/><rect x="7" y="7.5" width="2.2" height="3.6" rx=".8"/></svg>',
  escopeta:'<svg viewBox="0 0 24 24" fill="currentColor"><path d="M3 15h4.5l1.5 1.2 3-.6 1.8 1H19a1.6 1.6 0 0 1 1.6 1.6v1.2h-2.2l-2 1.6H9.5L5 16.5H3z"/><rect x="6.5" y="10" width="2" height="4" rx="1"/><path d="M5.5 6.5h7l3 3.5H8.5z"/><rect x="8.5" y="6.5" width="2.2" height="2.4" rx=".8"/></svg>',
  francotirador:'<svg viewBox="0 0 24 24" fill="currentColor"><path d="M2 13h10v1.5H2z"/><path d="M12 12.5h6v3h-6z"/><path d="M18 12.5h4v3.5h-4z"/><path d="M7 10h6v1.5H7z"/><path d="M8 11.5h4v1H8z"/></svg>',
  vendaje:'<svg viewBox="0 0 24 24" fill="currentColor"><path fill-rule="evenodd" d="M3.5 7h17a1 1 0 0 1 1 1v11a1 1 0 0 1-1 1h-17a1 1 0 0 1-1-1V8a1 1 0 0 1 1-1zM10 9.5v3h-3v2h3v3h4v-3h3v-2h-3v-3z"/></svg>',
  escudoPocion:'<svg viewBox="0 0 24 24" fill="currentColor"><rect x="10" y="2.5" width="4" height="3.5" rx="1"/><path d="M8 6h8l1.6 3.5c.6 3.4-.6 7.2-2.4 10.5a3 3 0 0 1-2.4 1.5c-1 0-1.9-.5-2.4-1.5C7.6 16.7 6.4 12.9 7 9.5z"/><path d="M9.8 9.5h4.4l.8 2h-6z" opacity=".4"/></svg>',
};

const GARMAS=[
 {nm:"Subfusil Espectro", svg:SVG.subfusil,     am:40,max:40,dmg:14,cad:.08,alc:60,tipo:"arma",rar:RAR.raro.c},
 {nm:"Rifle Táctico",     svg:SVG.rifle,        am:30,max:30,dmg:32,cad:.12,alc:120,tipo:"arma",rar:RAR.legend.c},
 {nm:"Escopeta Pesada",   svg:SVG.escopeta,     am:8, max:8, dmg:85,cad:.65,alc:35,tipo:"arma",rar:RAR.epico.c},
 {nm:"Francotirador AWP", svg:SVG.francotirador,am:5, max:5, dmg:125,cad:1.2,alc:250,tipo:"arma",rar:RAR.legend.c},
 {nm:"Botiquín Médico",   svg:SVG.vendaje,      am:2, max:2, cura:100,tipo:"cura",             rar:RAR.epico.c},
 {nm:"Poción Máxima",     svg:SVG.escudoPocion, am:2, max:2, cura:100,tipo:"escudo",           rar:RAR.legend.c},
];

let armaSel=0,disparando=false,cooldown=0,retro=0;
function pintGInv(){
  const c=document.getElementById('ginv');c.innerHTML='';
  GARMAS.forEach((a,i)=>{
    const d=document.createElement('div');
    d.className='g-slot'+(i===armaSel?' sel':'');
    d.style.borderColor=a.rar;
    d.title=a.nm+' · '+Object.keys(RAR).find(k=>RAR[k].c===a.rar&&RAR[k])||'';
    d.innerHTML=`<span class="k">${i+1}</span><span class="ic">${a.svg}</span><span class="am">${a.am}</span>`;
    d.onclick=()=>{armaSel=i;pintGInv();};
    c.appendChild(d);
  });
}
function recargar(){const a=GARMAS[armaSel];if(a.tipo==='arma'){a.am=a.max;pintGInv();}}

function usarObjeto(){
  const a=GARMAS[armaSel];
  if(a.tipo==='cura'&&a.am>0&&P.salud<100){a.am--;P.salud=Math.min(100,P.salud+(a.cura||40));pintGInv();actualizarBarras();}
  else if(a.tipo==='escudo'&&a.am>0&&P.escudo<100){a.am--;P.escudo=Math.min(100,P.escudo+(a.cura||50));pintGInv();actualizarBarras();}
}

function disparar(){
  const a=GARMAS[armaSel];
  if(a.tipo!=='arma'){usarObjeto();cooldown=.6;return;}
  if(a.am<=0){cooldown=.35;return;}
  a.am--;pintGInv();cooldown=a.cad;retro=1;
  // hitscan: enemigo más cercano dentro del alcance y cerca de la mira
  let mejor=null,mejorD=1e9;
  enemigos.forEach(en=>{
    if(!en.vivo)return;
    const c=proj(en.x,3,en.z);
    if(c.z<NEAR)return;
    const d=Math.hypot(en.x-P.x,en.z-P.z);
    if(d>a.alc)return;
    const s=scr(c);
    const ancho=Math.max(26,(4.5*FOC()/c.z));   // caja de acierto
    if(Math.abs(s.x-W/2)<ancho*0.55&&Math.abs(s.y-H/2)<ancho*1.1&&d<mejorD){mejorD=d;mejor=en;}
  });
  // traza de la bala saliendo del arma del jugador
  const oy=P.y+2.0,ox=P.x+Math.sin(P.yaw)*1.3+Math.cos(P.yaw)*0.78,oz=P.z+Math.cos(P.yaw)*1.3-Math.sin(P.yaw)*0.78;
  tracers.push({x1:ox,y1:oy,z1:oz,
    x2:mejor?mejor.x:P.x+Math.sin(P.yaw)*a.alc, y2:mejor?2.6:oy,
    z2:mejor?mejor.z:P.z+Math.cos(P.yaw)*a.alc, t:0});
  if(mejor){
    mejor.vida-=a.dmg;
    impactos.push({x:mejor.x,y:3.2,z:mejor.z,t:0,dmg:a.dmg});
    if(mejor.vida<=0){mejor.vivo=false;P.kills++;document.getElementById('gkills').textContent=P.kills;actualizarDesafios();}
  }
}

/* --- colisiones con edificios --- */
function colisiona(x,z){
  for(const e of edificios){
    if(Math.abs(x-e.x)<e.w/2+RAD&&Math.abs(z-e.z)<e.d/2+RAD)return true;
  }
  for(const t of arboles){                     // no atravesar árboles
    const dx=x-t.x,dz=z-t.z;
    if(dx*dx+dz*dz<(2.2+RAD)*(2.2+RAD))return true;
  }
  return false;
}
function mover(dx,dz){
  if(!colisiona(P.x+dx,P.z))P.x+=dx;      // deslizar en X
  if(!colisiona(P.x,P.z+dz))P.z+=dz;      // deslizar en Z
  P.x=Math.max(-LIM,Math.min(LIM,P.x));
  P.z=Math.max(-LIM,Math.min(LIM,P.z));
}

/* ============================================================
   4) RENDER
   ============================================================ */
function lerpc(a,b,t){const A=[parseInt(a.slice(1,3),16),parseInt(a.slice(3,5),16),parseInt(a.slice(5,7),16)];
  const B=[parseInt(b.slice(1,3),16),parseInt(b.slice(3,5),16),parseInt(b.slice(5,7),16)];
  return`rgb(${A.map((v,i)=>Math.round(v+(B[i]-v)*t)).join(',')})`;}

function grender(){
  // cámara sobre el hombro: atrás, a la derecha y siguiendo el salto completo
  const fx=Math.sin(P.yaw),fz=Math.cos(P.yaw);
  cam.x=P.x-fx*8.5+Math.cos(P.yaw)*1.7;
  cam.z=P.z-fz*8.5-Math.sin(P.yaw)*1.7;
  cam.y=4.9+P.y;                      // sube igual que el jugador (ya no "vuela")
  const hor=H/2+FOC()*Math.tan(pitch);

  // cielo
  let g=gctx.createLinearGradient(0,0,0,Math.max(hor,1));
  g.addColorStop(0,MG.cieloTop);g.addColorStop(1,MG.cieloBot);
  gctx.fillStyle=g;gctx.fillRect(0,0,W,Math.max(0,Math.min(H,hor)));
  gctx.fillStyle='rgba(255,255,255,.2)';gctx.beginPath();gctx.arc(W*0.72,Math.max(hor,0)*0.42,70,0,7);gctx.fill();

  // suelo (siempre pinta desde el horizonte hasta abajo)
  const hy=Math.max(0,Math.min(H,hor));
  g=gctx.createLinearGradient(0,hy,0,H);
  g.addColorStop(0,MG.sueloLejos);g.addColorStop(1,MG.suelo);
  gctx.fillStyle=g;gctx.fillRect(0,hy,W,H-hy);

  // rejilla (solo segmentos válidos)
  gctx.strokeStyle='rgba(255,255,255,.045)';gctx.lineWidth=1;
  const R=110,px=Math.round(P.x/12)*12,pz=Math.round(P.z/12)*12;
  for(let i=-R;i<=R;i+=12){
    let a=proj(px-R,0,pz+i),b=proj(px+R,0,pz+i);
    if(a.z>NEAR&&b.z>NEAR){const A=scr(a),B=scr(b);gctx.beginPath();gctx.moveTo(A.x,A.y);gctx.lineTo(B.x,B.y);gctx.stroke();}
    let c=proj(px+i,0,pz-R),d=proj(px+i,0,pz+R);
    if(c.z>NEAR&&d.z>NEAR){const C=scr(c),D=scr(d);gctx.beginPath();gctx.moveTo(C.x,C.y);gctx.lineTo(D.x,D.y);gctx.stroke();}
  }

  // textura del suelo: manchas y motas ancladas al mundo
  const pr=rng(731);
  for(let i=0;i<95;i++){
    const a=pr()*6.283,d=1.5+pr()*55;
    const c=proj(P.x+Math.cos(a)*d,0.05,P.z+Math.sin(a)*d);
    if(c.z<NEAR||c.z>82)continue;
    const s=scr(c),r=Math.min(W*0.6,(1.2+pr()*3.2)*FOC()/c.z);
    if(r<2)continue;
    const tipo=Math.floor(pr()*4);
    const col=tipo===0?'rgba(16,40,14,.12)':tipo===1?'rgba(240,245,205,.07)':tipo===2?'rgba(122,94,52,.10)':'rgba(36,84,40,.15)';
    gctx.fillStyle=col;
    gctx.beginPath();gctx.ellipse(s.x,s.y,r,r*(0.26+pr()*0.14),0,0,7);gctx.fill();
  }
  for(let i=0;i<150;i++){
    const a=pr()*6.283,d=pr()*60;
    const c=proj(P.x+Math.cos(a)*d,0.03,P.z+Math.sin(a)*d);
    if(c.z<NEAR||c.z>70)continue;
    const s=scr(c),r=Math.max(1.2,(0.3+pr()*0.9)*FOC()/c.z);
    gctx.fillStyle='rgba(18,44,18,.13)';
    gctx.beginPath();gctx.ellipse(s.x,s.y,r,r*0.3,0,0,7);gctx.fill();
  }

  // lista de objetos ordenada de lejos a cerca
  const draw=[];
  const dist2=(x,z)=>{const a=x-cam.x,b=z-cam.z;return a*a+b*b;};
  edificios.forEach(e=>{const d=dist2(e.x,e.z);if(d<155*155)draw.push({d,t:'ed',o:e});});
  arboles.forEach(t=>{const d=dist2(t.x,t.z);if(d<115*115)draw.push({d,t:'ar',o:t});});
  pastos.forEach(t=>{const d=dist2(t.x,t.z);if(d<85*85)draw.push({d,t:'pa',o:t});});
  flores.forEach(t=>{const d=dist2(t.x,t.z);if(d<85*85)draw.push({d,t:'fl',o:t});});
  cofres.forEach(c=>{if(!c.abierto)draw.push({d:dist2(c.x,c.z),t:'co',o:c});});
  enemigos.forEach(en=>{if(en.vivo)draw.push({d:dist2(en.x,en.z),t:'en',o:en});});
  draw.push({d:dist2(P.x,P.z),t:'pl',o:null});   // el jugador va en el mundo, no pegado a la pantalla
  const N=56;
  for(let i=0;i<N;i++){
    const a=i/N*6.283,a2=(i+1)/N*6.283;
    const ax=storm.cx+Math.cos(a)*storm.r,az=storm.cz+Math.sin(a)*storm.r;
    draw.push({d:dist2(ax,az),t:'st',o:{ax,az,a2}});
  }
  draw.sort((A,B)=>B.d-A.d);
  draw.forEach(it=>{
    if(it.t==='ed')dibEd(it.o); else if(it.t==='ar')dibAr(it.o);
    else if(it.t==='pa')dibPasto(it.o); else if(it.t==='fl')dibFlor(it.o);
    else if(it.t==='co')dibCo(it.o); else if(it.t==='en')dibEnemigo(it.o);
    else if(it.t==='pl')dibJugador();
    else dibStorm(it.o);
  });
  dibHumos();
  dibTracers();

  // etiquetas de zona
  gctx.textAlign='center';gctx.textBaseline='middle';
  MG.pois.forEach(p=>{
    const c=proj(p[0],16,p[1]);if(c.z<NEAR*3)return;
    const s=scr(c);if(s.x<-90||s.x>W+90||s.y<0||s.y>H)return;
    gctx.font='800 12px "Segoe UI"';gctx.lineWidth=4;gctx.strokeStyle='rgba(0,0,0,.6)';
    gctx.strokeText(p[2].toUpperCase(),s.x,s.y);gctx.fillStyle='#fff';gctx.fillText(p[2].toUpperCase(),s.x,s.y);
  });

  // números de daño
  impactos.forEach(im=>{
    const c=proj(im.x,im.y+im.t*3,im.z);if(c.z<NEAR)return;
    const s=scr(c);gctx.font='900 20px "Segoe UI"';gctx.globalAlpha=Math.max(0,1-im.t);
    gctx.lineWidth=4;gctx.strokeStyle='rgba(0,0,0,.7)';gctx.strokeText(im.dmg,s.x,s.y);
    gctx.fillStyle='#ffcb2b';gctx.fillText(im.dmg,s.x,s.y);gctx.globalAlpha=1;
  });

  dibMira();

  // flash rojo al recibir un balazo
  if(flashRojo>0){
    const v=gctx.createRadialGradient(W/2,H/2,H*0.18,W/2,H/2,H*0.8);
    v.addColorStop(0,'rgba(220,40,50,0)');v.addColorStop(1,`rgba(220,40,50,${flashRojo*0.6})`);
    gctx.fillStyle=v;gctx.fillRect(0,0,W,H);
  }

  // vignette de tormenta
  const fuera=Math.hypot(P.x-storm.cx,P.z-storm.cz)>storm.r;
  if(fuera){
    const v=gctx.createRadialGradient(W/2,H/2,H*0.25,W/2,H/2,H*0.85);
    v.addColorStop(0,'rgba(138,76,255,0)');v.addColorStop(1,'rgba(138,76,255,.5)');
    gctx.fillStyle=v;gctx.fillRect(0,0,W,H);
  }

  // Pantallas de victoria y muerte
  if(muerto){
    gctx.fillStyle='rgba(10,0,0,.72)';gctx.fillRect(0,0,W,H);
    gctx.textAlign='center';gctx.fillStyle='#fff';gctx.font='900 46px "Segoe UI"';
    gctx.fillText('ELIMINADO',W/2,H/2-10);
    gctx.font='600 16px "Segoe UI"';gctx.fillStyle='#8ea6c2';
    gctx.fillText('Bajas: '+P.kills+'  ·  Clic para volver a jugar',W/2,H/2+26);
  } else if(gvivos === 1) {
    gctx.fillStyle='rgba(20,50,20,.72)';gctx.fillRect(0,0,W,H);
    gctx.textAlign='center';gctx.fillStyle='#ffcb2b';gctx.font='900 46px "Segoe UI"';
    gctx.fillText('¡VICTORIA MAGISTRAL!',W/2,H/2-10);
    gctx.font='600 16px "Segoe UI"';gctx.fillStyle='#eaf2fb';
    gctx.fillText('Bajas: '+P.kills+'  ·  Clic para jugar de nuevo',W/2,H/2+26);
  }
  gmini();
}

/* recorta un polígono contra el plano cercano: evita caras que saltan o se deforman */
function clipN(cs){
  const out=[];
  for(let i=0;i<cs.length;i++){
    const a=cs[i],b=cs[(i+1)%cs.length];
    const ai=a.z>=NEAR,bi=b.z>=NEAR;
    if(ai)out.push(a);
    if(ai!==bi){
      const t=(NEAR-a.z)/(b.z-a.z);
      out.push({x:a.x+(b.x-a.x)*t,y:a.y+(b.y-a.y)*t,z:NEAR});
    }
  }
  return out;
}
function quad(a,b,c,d,fill,st){
  const cl=clipN([a,b,c,d]);
  if(cl.length<3)return;
  gctx.beginPath();
  cl.forEach((p,i)=>{const s=scr(p);if(i===0)gctx.moveTo(s.x,s.y);else gctx.lineTo(s.x,s.y);});
  gctx.closePath();
  gctx.fillStyle=fill;gctx.fill();
  if(st){gctx.strokeStyle=st;gctx.lineWidth=1.5;gctx.lineJoin='round';gctx.stroke();}
}
function lerp3(a,b,t){return{x:a.x+(b.x-a.x)*t,y:a.y+(b.y-a.y)*t,z:a.z+(b.z-a.z)*t};}
function puntoCara(A,B,D,C,u,v){return lerp3(lerp3(A,B,u),lerp3(D,C,u),v);}
function quadCara(A,B,D,C,u0,u1,v0,v1,fill,st){
  quad(puntoCara(A,B,D,C,u0,v0),puntoCara(A,B,D,C,u1,v0),
       puntoCara(A,B,D,C,u1,v1),puntoCara(A,B,D,C,u0,v1),fill,st);
}
/* ====== MATERIALES DE CONSTRUCCIÓN POR ZONA ====== */
const MATS={
  ladrillo:{cols:LADR_COLS,bw:1.15,bh:0.55,mort:'rgba(46,32,18,.55)',roofTop:'#a38a63',teja:'#c25a3c'},
  madera:{cols:['#a07a4e','#8f6c42','#a88358','#966f46'],bw:2.6,bh:0.72,mort:'rgba(40,28,14,.55)',roofTop:'#8a7050',teja:'#b0522f'},
  piedra:{cols:['#a7abb2','#9ba0a8','#b2b6bc','#8f949c'],bw:1.7,bh:1.05,mort:'rgba(30,32,38,.5)',roofTop:'#b9bcc2',teja:'#9aa0a8'},
  metal:{cols:['#7e8894','#737e8b','#8a94a0','#6b7683'],bw:0.55,bh:999,mort:'rgba(26,30,36,.55)',roofTop:'#5d6873',teja:'#5d6873',vert:true},
};
function edTipo(pi,r){
  if(pi===1||pi===3)return r()<0.82?'casa':'torre';
  if(pi===2)return r()<0.55?'nave':(r()<0.72?'torre':'casa');
  return r()<0.65?'torre':'casa';
}
function edMat(pi,r){
  if(r()<0.14)return ['ladrillo','madera','piedra','metal'][Math.floor(r()*4)];
  return ['piedra','madera','metal','ladrillo'][pi];
}
/* una pared con textura según material (LOD por tamaño en pantalla) */
function dibFace(A,B,C,D,m,sh){
  const cl=clipN([A,B,C,D]);
  if(cl.length<3)return 0;
  const pth=cl.map(p=>scr(p));
  const wPx=Math.hypot(pth[1].x-pth[0].x,pth[1].y-pth[0].y);
  if(wPx<5)return 0;
  gctx.beginPath();
  pth.forEach((p,i)=>{if(i===0)gctx.moveTo(p.x,p.y);else gctx.lineTo(p.x,p.y);});
  gctx.closePath();
  gctx.fillStyle=sombra(m.cols[0],sh);gctx.fill();
  if(wPx<28)return wPx;
  const w=Math.hypot(B.x-A.x,B.z-A.z),hg=Math.hypot(D.x-A.x,D.z-A.z);
  if(w<0.5||hg<0.3)return wPx;
  const nW=Math.ceil(w/m.bw),nH=Math.max(1,Math.ceil(hg/m.bh));
  const det=wPx>68;                              // detalle fino solo de cerca
  for(let i=0;i<nH;i++){
    const v0=Math.max(0,i*m.bh/hg),v1=Math.min(1,(i+1)*m.bh/hg);
    const off=(i%2)*0.5*Math.min(1,m.bw/w);      // junta corrida
    for(let j=0;j<nW;j++){
      const u0=Math.max(0,j*m.bw/w+off),u1=Math.min(1,(j+1)*m.bw/w+off);
      if(u1<=0||u0>=1||v1<=0||v0>=1)continue;
      const col=m.cols[(i*7+j*13)%m.cols.length];
      quad(puntoCara(A,B,D,C,u0,v0),puntoCara(A,B,D,C,u1,v0),
           puntoCara(A,B,D,C,u1,v1),puntoCara(A,B,D,C,u0,v1),
           sombra(col,sh+((i*7+j*13)%5-2)*0.02),det?m.mort:null);
    }
  }
  if(m.vert){                                    // chapa: junta vertical
    for(let j=0;j<=nW;j++){
      const u=Math.min(1,j*m.bw/w);
      quadCara(A,B,D,C,u,u+0.035/w,0,1,sombra(m.cols[0],sh-0.32),null);
    }
  }
  quad(puntoCara(A,B,D,C,0,0),puntoCara(A,B,D,C,1,0),
       puntoCara(A,B,D,C,1,Math.min(1,0.55/hg)),puntoCara(A,B,D,C,0,Math.min(1,0.55/hg)),
       sombra(m.cols[0],sh-0.25),null);         // rodapié oscuro
  if(wPx>48&&!m.vert){                           // pilastras en las esquinas
    const sw=0.22/w;
    quadCara(A,B,D,C,0,sw,0,1,sombra(m.cols[0],sh-0.22),null);
    quadCara(A,B,D,C,1-sw,1,0,1,sombra(m.cols[0],sh-0.22),null);
  }
  return wPx;
}
/* ventanas con marco + puerta + postigos según el tipo de edificio */
function dibVentanas(A,B,D,C,tipo,mat,sh,esPuerta,wPx){
  if(wPx<26)return;
  const wg=Math.hypot(B.x-A.x,B.z-A.z),hg=Math.hypot(D.x-A.x,D.z-A.z);
  if(hg<3.2)return;
  const marco=mat==='metal'?'#4c555f':mat==='piedra'?'#b9bcc2':'#9aa2ac';
  const vidrio=mat==='metal'?'#1d2833':'#2c3d52';
  if(esPuerta){
    const ww=1.15/wg,m=0.12/wg;
    quadCara(A,B,D,C,0.5-ww/2-m,0.5+ww/2+m,0,2.35/hg,sombra(marco,sh),null);
    const pCol=mat==='metal'?'#38424e':(mat==='piedra'?'#2e333a':'#3d2a17');
    quadCara(A,B,D,C,0.5-ww/2,0.5+ww/2,0.03/hg,2.2/hg,sombra(pCol,sh-0.12),null);
    if(mat==='metal'){
      quadCara(A,B,D,C,0.5-ww/2,0.5+ww/2,1.05/hg,1.12/hg,sombra(marco,sh),null);
      quadCara(A,B,D,C,0.5-ww/2,0.5+ww/2,1.65/hg,1.72/hg,sombra(marco,sh),null);
    }
  }
  const anchoV=mat==='metal'?2.4:1.1;
  const nw=Math.max(1,Math.round(wg/(mat==='metal'?4.2:3.8)));
  for(let i=0;i<nw;i++){
    const u=(i+1)/(nw+1);
    const v0=1.4/hg,v1=Math.min(0.96,2.9/hg);
    if(v1<=v0)continue;
    const ww=Math.min(anchoV,wg*0.6)/wg,m=0.14/wg,mh=0.14/hg;
    quadCara(A,B,D,C,u-ww/2-m,u+ww/2+m,v0-mh,v1+mh,sombra(marco,sh),null);
    quadCara(A,B,D,C,u-ww/2,u+ww/2,v0,v1,sombra(vidrio,sh-0.16),'rgba(150,190,230,.4)');
    quadCara(A,B,D,C,u-ww/2,u+ww/2,(v0+v1)/2-0.05/hg,(v0+v1)/2+0.05/hg,sombra(marco,sh),null);
    if(mat==='metal')
      quadCara(A,B,D,C,u-ww/2,u+ww/2,(v0*2+v1)/3-0.05/hg,(v0*2+v1)/3+0.05/hg,sombra(marco,sh),null);
    if(tipo==='casa'){                           // postigos de madera
      const sw=0.16/wg;
      quadCara(A,B,D,C,u-ww/2-m-sw,u-ww/2-m,v0-mh,v1+mh,sombra('#5d4026',sh),null);
      quadCara(A,B,D,C,u+ww/2+m,u+ww/2+m+sw,v0-mh,v1+mh,sombra('#5d4026',sh),null);
    }
  }
}
/* techo plano con cornisa y parapeto (torres y naves) */
function techoPlano(e,m){
  const x0=e.x-e.w/2,x1=e.x+e.w/2,z0=e.z-e.d/2,z1=e.z+e.d/2,h=e.h;
  const top=m.roofTop||'#a38a63';
  const oo=Math.min(1.15,e.w*0.13),hh=0.5;
  const r={e2:proj(x0-oo,h,z0-oo),f2:proj(x1+oo,h,z0-oo),g2:proj(x1+oo,h,z1+oo),h2:proj(x0-oo,h,z1+oo),
           e3:proj(x0-oo,h+hh,z0-oo),f3:proj(x1+oo,h+hh,z0-oo),g3:proj(x1+oo,h+hh,z1+oo),h3:proj(x0-oo,h+hh,z1+oo)};
  const techo=[
    {q:[r.e2,r.f2,r.g2,r.h2],c:sombra(top,0.12)},
    {q:[r.e3,r.f3,r.g3,r.h3],c:sombra(top,0.08)},
    {q:[r.e2,r.f2,r.f3,r.e3],c:sombra(m.cols[0],-0.12)},
    {q:[r.f2,r.g2,r.g3,r.f3],c:sombra(m.cols[0],-0.30)},
    {q:[r.g2,r.h2,r.h3,r.g3],c:sombra(m.cols[0],-0.12)},
    {q:[r.h2,r.e2,r.e3,r.h3],c:sombra(m.cols[0],-0.30)},
  ];
  techo.sort((a,b)=>(a.q[0].z+a.q[1].z+a.q[2].z+a.q[3].z)-(b.q[0].z+b.q[1].z+b.q[2].z+b.q[3].z));
  techo.forEach(t=>quad(t.q[0],t.q[1],t.q[2],t.q[3],t.c,'rgba(30,20,10,.35)'));
}
/* techo a dos aguas con tejas, frontones, cumbrera y chimenea */
function techoGable(e,m){
  const h=e.h,rh=e.rh;
  const x0=e.x-e.w/2,x1=e.x+e.w/2,z0=e.z-e.d/2,z1=e.z+e.d/2;
  const vE=proj(x0,h,z0),vF=proj(x1,h,z0),vG=proj(x1,h,z1),vH=proj(x0,h,z1);
  const teja=m.teja||'#c25a3c';
  const piezas=[];
  const det=Math.hypot(e.x-cam.x,e.z-cam.z)<60;
  const pend=(A,B,C,D,sh)=>{
    const n=6;
    for(let i=0;i<n;i++){
      const t0=i/n,t1=(i+1)/n,k=i%2?0.10:0;
      piezas.push({q:[lerp3(A,C,t0),lerp3(B,D,t0),lerp3(B,D,t1),lerp3(A,C,t1)],
        c:sombra(teja,sh-k),st:det?'rgba(60,25,15,.5)':null});
    }
  };
  if(e.d>=e.w){                                  // cumbrera a lo largo de Z
    const zoo=Math.min(1.1,e.d*0.12);
    const r1=proj(e.x,h+rh,z0-zoo),r2=proj(e.x,h+rh,z1+zoo);
    pend(vE,vH,r1,r2,-0.14);
    pend(vF,vG,r1,r2,-0.30);
    piezas.push({q:[vE,vF,r1,r1],c:sombra(m.cols[0],-0.18),st:det?'rgba(30,20,10,.4)':null});
    piezas.push({q:[vH,vG,r2,r2],c:sombra(m.cols[0],-0.18),st:det?'rgba(30,20,10,.4)':null});
    const r3=proj(e.x,h+rh+0.35,z0-zoo-0.18),r4=proj(e.x,h+rh+0.35,z1+zoo+0.18);
    piezas.push({q:[r1,r2,r4,r3],c:sombra(teja,-0.24),st:det?'rgba(40,18,10,.5)':null});
  }else{                                         // cumbrera a lo largo de X
    const oo=Math.min(1.1,e.w*0.12);
    const r1=proj(x0-oo,h+rh,e.z),r2=proj(x1+oo,h+rh,e.z);
    pend(vE,vF,r1,r2,-0.14);
    pend(vH,vG,r1,r2,-0.30);
    piezas.push({q:[vE,vH,r1,r1],c:sombra(m.cols[0],-0.18),st:det?'rgba(30,20,10,.4)':null});
    piezas.push({q:[vF,vG,r2,r2],c:sombra(m.cols[0],-0.18),st:det?'rgba(30,20,10,.4)':null});
    const r3=proj(x0-oo-0.18,h+rh+0.35,e.z),r4=proj(x1+oo+0.18,h+rh+0.35,e.z);
    piezas.push({q:[r1,r2,r4,r3],c:sombra(teja,-0.24),st:det?'rgba(40,18,10,.5)':null});
  }
  if(e.ch){                                      // chimenea
    dibCajas(e.chx,e.h+e.rh-0.55,e.cz,0,[
      {x:0,y:0,z:0,w:0.85,h:1.15,d:0.85,c:sombra(m.cols[0],-0.12)},
      {x:0,y:1.12,z:0,w:1.05,h:0.18,d:1.05,c:'#23252a'},
    ]);
  }
  piezas.sort((a,b)=>(a.q[0].z+a.q[1].z+a.q[2].z+a.q[3].z)-(b.q[0].z+b.q[1].z+b.q[2].z+b.q[3].z));
  piezas.forEach(p=>quad(p.q[0],p.q[1],p.q[2],p.q[3],p.c,p.st));
}
function dibEd(e){
  const x0=e.x-e.w/2,x1=e.x+e.w/2,z0=e.z-e.d/2,z1=e.z+e.d/2,h=e.h;
  const v={A:proj(x0,0,z0),B:proj(x1,0,z0),C:proj(x1,0,z1),D:proj(x0,0,z1),
           E:proj(x0,h,z0),F:proj(x1,h,z0),G:proj(x1,h,z1),H:proj(x0,h,z1)};
  const m=MATS[e.mat]||MATS.ladrillo;
  const r2=rng(Math.abs(Math.floor(e.x*131+e.z*197))+7);
  const caras=[
    {a:v.A,b:v.B,c:v.F,d:v.E,sh:-0.12},
    {a:v.B,b:v.C,c:v.G,d:v.F,sh:-0.30},
    {a:v.C,b:v.D,c:v.H,d:v.G,sh:-0.12},
    {a:v.D,b:v.A,c:v.E,d:v.H,sh:-0.30},
  ];
  caras.sort((p,q)=>(p.a.z+p.b.z+p.c.z+p.d.z)-(q.a.z+q.b.z+q.c.z+q.d.z));
  const puerta=Math.floor(r2()*4);
  caras.forEach((p,i)=>{
    const wPx=dibFace(p.a,p.b,p.c,p.d,m,p.sh);
    dibVentanas(p.a,p.b,p.d,p.c,e.tipo,e.mat,p.sh,i===puerta,wPx);
  });
  if(e.tipo==='casa')techoGable(e,m); else techoPlano(e,m);
}
function dibAr(t){
  const d=Math.hypot(t.x-cam.x,t.z-cam.z);
  if(d>80)return; // El error estaba aquí, hemos quitado '||d<3.4' para que no desaparezca de cerca
  const base=proj(t.x,0,t.z);
  if(base.z<NEAR)return;
  if(d<42)dibSombraPiso(t.x,t.z);
  dibCajas(t.x,0,t.z,0,d>50?modeloArbolLejos(t):modeloArbol(t));
}
function modeloArbolLejos(t){
  const B=[],add=(x,y,z,w,h,d,c)=>B.push({x,y,z,w,h,d,c});
  const h=t.h,th=0.22+t.w*0.05,cw=t.w,ly=h*0.58;
  add(0,0,0,th,h*0.5,th,'#6b4527');
  add(0,ly,0,cw,cw*0.6,cw,'#2f8f45');
  add(0,ly+cw*0.55,0,cw*0.72,cw*0.5,cw*0.72,'#3aa352');
  add(0,ly+cw*1.0,0,cw*0.46,cw*0.4,cw*0.46,'#43a755');
  return B;
}
function modeloArbol(t){
  const B=[],add=(x,y,z,w,h,d,c)=>B.push({x,y,z,w,h,d,c});
  const h=t.h,th=0.24+t.w*0.06;
  const sw=Math.sin(anim*1.1+t.x*2.1)*Math.cos(anim*0.9+t.z*1.7);
  const S=y=>sw*0.13*(y/h);
  add(S(0),0,0,th,h*0.46,th,'#6b4527');
  add(S(h*0.48),h*0.48,0,th*1.7,h*0.12,th*1.7,'#7d5734');
  const cw=t.w,ly=h*0.58;
  add(S(ly),ly,0,cw,cw*0.62,cw,'#2f8f45');
  add(S(ly)+cw*0.62,ly+cw*0.18,0.05,cw*0.46,cw*0.36,cw*0.46,'#2b8540');
  add(S(ly)-cw*0.62,ly+cw*0.18,-0.05,cw*0.46,cw*0.36,cw*0.46,'#369b4c');
  add(S(ly+cw*0.5),ly+cw*0.5,0,cw*0.78,cw*0.5,cw*0.78,'#3aa352');
  add(S(ly+cw*0.95),ly+cw*0.95,0,cw*0.5,cw*0.44,cw*0.5,'#45ab57');
  return B;
}
function dibPasto(t){
  const b=proj(t.x,0,t.z);
  if(b.z<NEAR||b.z>85)return;
  const s=scr(b);
  const w=Math.min(W*0.4,0.09*FOC()/b.z);
  const th=Math.min(H*0.5,t.h*FOC()/b.z);
  const sway=Math.sin(anim*2.4+t.fase)*0.18;
  const col=lerpc(PASTO_COL[t.tipo],PASTO_COL[(t.tipo+1)%PASTO_COL.length],t.v);
  const col2=lerpc(PASTO_COL[(t.tipo+2)%PASTO_COL.length],'#2c6b30',t.v);
  gctx.lineCap='round';
  gctx.fillStyle='rgba(24,58,26,.30)';               // mata base oscura
  gctx.beginPath();gctx.ellipse(s.x,s.y,w*2.3,w*0.8,0,0,7);gctx.fill();
  for(let k=0;k<3;k++){
    const spr=(k-1)*w*2.6,hh=th*(0.55+k*0.2);
    gctx.strokeStyle=k===0?col:col2;
    gctx.lineWidth=Math.max(0.7,w*(1-k*0.18));
    gctx.beginPath();
    gctx.moveTo(s.x+spr,s.y);
    gctx.quadraticCurveTo(s.x+spr+sway*hh*0.45,s.y-hh*0.6,s.x+spr+sway*hh,s.y-hh);
    gctx.stroke();
  }
}
function dibFlor(t){
  const b=proj(t.x,0,t.z);
  if(b.z<NEAR||b.z>85)return;
  const s=scr(b);
  const w=Math.min(W*0.4,0.07*FOC()/b.z);
  const hh=Math.min(H*0.5,t.h*FOC()/b.z);
  gctx.lineCap='round';
  gctx.strokeStyle='#2f7f38';gctx.lineWidth=Math.max(0.8,w*0.8);
  gctx.beginPath();gctx.moveTo(s.x,s.y);gctx.lineTo(s.x,s.y-hh);gctx.stroke();
  const r=Math.max(1,w*2.2);
  gctx.fillStyle=t.c;
  gctx.beginPath();gctx.arc(s.x,s.y-hh,r,0,7);gctx.fill();
  gctx.fillStyle='#ffe98a';
  gctx.beginPath();gctx.arc(s.x,s.y-hh,r*0.36,0,7);gctx.fill();
}
function dibCo(c){
  if(Math.hypot(c.x-cam.x,c.z-cam.z)>70)return;
  const b=proj(c.x,0.8,c.z);if(b.z<NEAR)return;
  const s=scr(b);const w=Math.min(W*0.25, 2.2*FOC()/b.z);
  gctx.fillStyle='rgba(255,203,43,.22)';gctx.beginPath();gctx.arc(s.x,s.y,w*0.8,0,7);gctx.fill();
  // El error de desaparecer muy cerca ha sido eliminado aquí.
  dibSombraPiso(c.x,c.z);
  dibCajas(c.x,0,c.z,0,[
    {x:0,y:0.75,z:0,w:1.3,h:0.55,d:0.95,c:'#8a6b28'},
    {x:0,y:1.3,z:0,w:1.38,h:0.2,d:1.02,c:'#ffcb2b'},
  ]);
}
function dibStorm(o){
  const alto=48;
  const p0=proj(o.ax,0,o.az);
  const bx=storm.cx+Math.cos(o.a2)*storm.r, bz=storm.cz+Math.sin(o.a2)*storm.r;
  const p1=proj(bx,0,bz),p2=proj(bx,alto,bz),p3=proj(o.ax,alto,o.az);
  if(p0.z<NEAR*2||p1.z<NEAR*2||p2.z<NEAR*2||p3.z<NEAR*2)return;  // más margen: no tapa la pantalla
  const A=scr(p0),B=scr(p1),C=scr(p2),D=scr(p3);
  const gr=gctx.createLinearGradient(0,C.y,0,A.y);
  gr.addColorStop(0,'rgba(150,120,255,0)');gr.addColorStop(.55,'rgba(150,120,255,.22)');gr.addColorStop(1,'rgba(120,90,255,.36)');
  gctx.beginPath();gctx.moveTo(A.x,A.y);gctx.lineTo(B.x,B.y);gctx.lineTo(C.x,C.y);gctx.lineTo(D.x,D.y);gctx.closePath();
  gctx.fillStyle=gr;gctx.fill();
}

/* ============================================================
   PERSONAJES VOXEL EN 3D REAL (cajas en el mundo, no en la pantalla)
   ============================================================ */
function sombra(col,k){return k>=0?lerpc(col,'#ffffff',k):lerpc(col,'#000000',-k);}

/* Modelo = lista de cajas en coordenadas locales.
   x,z = centro · y = base · el personaje mira hacia +z local */
function modeloVoxel(s,paso,lejos,arma){
  const B=[],add=(x,y,z,w,h,d,c)=>B.push({x,y,z,w,h,d,c});
  const pz=paso*0.11;
  if(lejos){                                   // versión simple para los lejanos
    add(-0.26,0, pz,0.44,1.72,0.5,s.traje2);
    add( 0.26,0,-pz,0.44,1.72,0.5,s.traje2);
    add(0,1.62,0,1.16,1.36,0.62,s.traje);
    add(0,1.95,-0.42,0.86,0.95,0.3,s.acc);
    add(0,3.06,0,0.92,0.9,0.86,s.craneo?'#ececec':s.piel);
    add(0,3.58,0,0.96,0.34,0.9,s.pelo);
    return B;
  }
  add(-0.26,0.22, pz,0.44,1.45,0.5,s.traje2);          // piernas
  add( 0.26,0.22,-pz,0.44,1.45,0.5,s.traje2);
  add(-0.26,0,    pz+0.05,0.5,0.26,0.66,s.bota);       // botas
  add( 0.26,0,   -pz+0.05,0.5,0.26,0.66,s.bota);
  add(0,1.62,0,1.16,1.36,0.62,s.traje);                // torso
  add(0,1.95, 0.33,0.46,0.5,0.07,s.acc);               // chaleco
  add(0,1.95,-0.42,0.86,0.95,0.3,s.acc);               // mochila
  add(-0.78,2.72,0,0.42,0.26,0.62,s.traje2);           // hombros
  add( 0.78,2.72,0,0.42,0.26,0.62,s.traje2);
  add(-0.78,1.78,0,0.36,0.96,0.46,s.traje2);           // brazos
  add( 0.78,1.78,0,0.36,0.96,0.46,s.traje2);
  add(-0.78,1.52,0,0.36,0.28,0.46,s.piel);             // manos
  add( 0.78,1.52,0,0.36,0.28,0.46,s.piel);
  add(0,2.96,0,0.34,0.14,0.34,s.piel);                 // cuello
  add(0,3.06,0,0.92,0.88,0.86,s.craneo?'#ececec':s.piel); // cabeza
  if(s.casco){add(0,3.62,0,0.98,0.4,0.92,s.traje2);add(0,3.42,0.44,0.78,0.24,0.06,s.acc);}
  else if(s.capucha){add(0,3.5,0,1.0,0.5,0.96,s.traje);add(0,3.06,-0.46,0.98,0.5,0.12,s.traje);}
  else if(s.gorra){add(0,3.62,0,0.96,0.3,0.9,s.acc);add(0,3.6,0.5,0.9,0.12,0.34,s.acc);}
  else if(s.robot){add(0,3.5,0,0.96,0.36,0.9,s.pelo);add(0,3.34,0.44,0.7,0.2,0.06,s.acc);}
  else{add(0,3.58,0,0.96,0.34,0.9,s.pelo);add(0,3.1,-0.44,0.94,0.5,0.1,s.pelo);}
  if(arma)add(0.78,1.96,0.62,0.16,0.16,1.0,'#16191f'); // arma en la mano
  return B;
}

/* Dibuja un personaje voxel en el mundo, girado según su yaw */
function dibVoxel(px,py,pz,yaw,s,paso,arma){
  const dCam=Math.hypot(px-cam.x,pz-cam.z);
  if(dCam>75)return;
  dibCajas(px,py,pz,yaw,modeloVoxel(s,paso,dCam>32,arma));
}
/* Dibuja una lista de cajas voxel en el mundo (personajes, árboles, cofres) */
function dibCajas(px,py,pz,yaw,mdl){
  const cy=Math.cos(yaw),sy=Math.sin(yaw);
  const caras=[];
  for(const b of mdl){
    const x0=b.x-b.w/2,x1=b.x+b.w/2,y0=b.y,y1=b.y+b.h,z0=b.z-b.d/2,z1=b.z+b.d/2;
    const V=[];
    for(const[lx,ly,lz]of[[x0,y0,z0],[x1,y0,z0],[x1,y0,z1],[x0,y0,z1],
                          [x0,y1,z0],[x1,y1,z0],[x1,y1,z1],[x0,y1,z1]]){
      V.push(proj(px+lx*cy+lz*sy, py+ly, pz-lx*sy+lz*cy));
    }
    const F=[[4,5,6,7,.20],[0,1,5,4,-.06],[2,3,7,6,-.06],[1,2,6,5,-.24],[3,0,4,7,-.24]];
    for(const f of F){
      const p=[V[f[0]],V[f[1]],V[f[2]],V[f[3]]];
      caras.push({z:(p[0].z+p[1].z+p[2].z+p[3].z)/4,p,c:sombra(b.c,f[4])});
    }
  }
  caras.sort((a,b)=>b.z-a.z);
  for(const f of caras){
    const s0=scr(f.p[0]),s1=scr(f.p[1]),s2=scr(f.p[2]),s3=scr(f.p[3]);
    gctx.beginPath();gctx.moveTo(s0.x,s0.y);gctx.lineTo(s1.x,s1.y);
    gctx.lineTo(s2.x,s2.y);gctx.lineTo(s3.x,s3.y);gctx.closePath();
    gctx.fillStyle=f.c;gctx.fill();
  }
}
function dibSombraPiso(px,pz){
  const c=proj(px,0.03,pz);if(c.z<NEAR)return;
  const s=scr(c),r=Math.min(W*0.15,1.2*FOC()/c.z);
  gctx.fillStyle='rgba(0,0,0,.26)';gctx.beginPath();
  gctx.ellipse(s.x,s.y,r,r*0.4,0,0,7);gctx.fill();
}
function dibJugador(){
  dibSombraPiso(P.x,P.z);
  const paso=Math.sin(anim*9)*(moviendo?5:0);
  dibVoxel(P.x,P.y,P.z,P.yaw,SKINS[skinSel],paso,true);
  if(retro>0){ // fogonazo del arma
    const c=proj(P.x+Math.sin(P.yaw)*1.4+Math.cos(P.yaw)*0.78, P.y+1.98, P.z+Math.cos(P.yaw)*1.4-Math.sin(P.yaw)*0.78);
    if(c.z>NEAR){const s=scr(c);gctx.fillStyle=`rgba(255,220,120,${retro})`;
      gctx.beginPath();gctx.arc(s.x,s.y,Math.min(60,retro*14*FOC()/c.z*0.02),0,7);gctx.fill();}
  }
}
function dibEnemigo(en){
  dibSombraPiso(en.x,en.z);
  const paso=Math.sin(en.t*6)*5;
  dibVoxel(en.x,0,en.z,en.yaw,SKINS[en.skin],paso,true);
  // barra de vida flotando sobre la cabeza
  const c=proj(en.x,4.6,en.z);if(c.z<NEAR)return;
  const s=scr(c),bw=Math.min(90,2.0*FOC()/c.z);
  if(bw<8)return;
  gctx.fillStyle='rgba(0,0,0,.6)';gctx.fillRect(s.x-bw/2,s.y,bw,bw*0.13);
  gctx.fillStyle=en.alerta?'#e5484d':(en.vida>50?'#3fe06f':'#ffcb2b');
  gctx.fillRect(s.x-bw/2,s.y,bw*Math.max(0,en.vida)/100,bw*0.13);
}
/* trazas de bala */
function dibTracers(){
  tracers.forEach(t=>{
    const a=proj(t.x1,t.y1,t.z1),b=proj(t.x2,t.y2,t.z2);
    if(a.z<NEAR||b.z<NEAR)return;
    const A=scr(a),B=scr(b);
    gctx.strokeStyle=`rgba(255,235,140,${Math.max(0,1-t.t*7)})`;gctx.lineWidth=2;
    gctx.beginPath();gctx.moveTo(A.x,A.y);gctx.lineTo(B.x,B.y);gctx.stroke();
  });
}
function dibMira(){
  const cx=W/2,cy=H/2,g=8+retro*14;
  gctx.strokeStyle='rgba(255,255,255,.9)';gctx.lineWidth=2;
  [[0,-1],[0,1],[-1,0],[1,0]].forEach(([dx,dy])=>{
    gctx.beginPath();gctx.moveTo(cx+dx*g,cy+dy*g);gctx.lineTo(cx+dx*(g+9),cy+dy*(g+9));gctx.stroke();
  });
  gctx.fillStyle='rgba(255,255,255,.9)';gctx.fillRect(cx-1.5,cy-1.5,3,3);
}

function gmini(){
  const k=150/MUNDO,ox=75,oz=75;
  gmx.fillStyle='#3f7a3c';gmx.fillRect(0,0,150,150);
  edificios.forEach(e=>{gmx.fillStyle='#8a7050';gmx.fillRect(ox+e.x*k-2,oz+e.z*k-2,4,4);});
  MG.pois.forEach(p=>{gmx.fillStyle='rgba(255,255,255,.9)';gmx.beginPath();gmx.arc(ox+p[0]*k,oz+p[1]*k,2.5,0,7);gmx.fill();});
  enemigos.forEach(e=>{if(!e.vivo)return;const d=Math.hypot(e.x-P.x,e.z-P.z);if(d>45)return;
    gmx.fillStyle='#e5484d';gmx.fillRect(ox+e.x*k-2,oz+e.z*k-2,4,4);});
  gmx.strokeStyle='rgba(180,130,255,.95)';gmx.lineWidth=1.5;
  gmx.beginPath();gmx.arc(ox+storm.cx*k,oz+storm.cz*k,storm.r*k,0,7);gmx.stroke();
  gmx.strokeStyle='rgba(255,255,255,.65)';gmx.setLineDash([3,3]);
  gmx.beginPath();gmx.arc(ox+storm.cx*k,oz+storm.cz*k,storm.rDest*k,0,7);gmx.stroke();gmx.setLineDash([]);
  gmx.save();gmx.translate(ox+P.x*k,oz+P.z*k);gmx.rotate(P.yaw);
  gmx.fillStyle='#ffcb2b';gmx.beginPath();gmx.moveTo(0,-6);gmx.lineTo(4,4);gmx.lineTo(-4,4);gmx.closePath();gmx.fill();gmx.restore();
}

/* ============================================================
   5) LÓGICA DE PARTIDA
   ============================================================ */
let gvivos=12;
function actualizarBarras(){
  document.getElementById('gsal').style.width=Math.max(0,P.salud)+'%';
  document.getElementById('gesc').style.width=Math.max(0,P.escudo)+'%';
  document.getElementById('gsalT').textContent=Math.max(0,Math.round(P.salud))+' / 100';
  document.getElementById('gescT').textContent=Math.max(0,Math.round(P.escudo))+' / 100';
}
function actualizarDesafios(){
  document.getElementById('d1').textContent=Math.min(5,P.kills)+'/5';
  document.getElementById('d1b').style.width=Math.min(100,P.kills/5*100)+'%';
  document.getElementById('d2').textContent=Math.min(3,P.cofres)+'/3';
  document.getElementById('d2b').style.width=Math.min(100,P.cofres/3*100)+'%';
}
function recibirDanio(d){
  if(muerto)return;
  const aEsc=Math.min(P.escudo,d); P.escudo-=aEsc; P.salud-=(d-aEsc);
  actualizarBarras();
  if(P.salud<=0){P.salud=0;muerto=true;if(document.pointerLockElement)document.exitPointerLock();}
}
function tickStorm(dt){
  storm.t-=dt;
  if(storm.t<=0){
    storm.fase++; storm.t=38;
    storm.rDest=Math.max(12,storm.r*0.62);
    const a=Math.random()*6.28,d=Math.random()*Math.max(0,storm.r-storm.rDest);
    // Interpolamos el nuevo destino de la tormenta para que no "salte" visualmente de golpe
    storm.cxDest=storm.cx+Math.cos(a)*d;
    storm.czDest=storm.cz+Math.sin(a)*d;
    const av=document.getElementById('gaviso');av.classList.add('show');
    setTimeout(()=>av.classList.remove('show'),2600);
  }
  storm.r+=(storm.rDest-storm.r)*Math.min(1,dt*0.35);
  storm.cx+=(storm.cxDest-storm.cx)*Math.min(1,dt*0.35);
  storm.cz+=(storm.czDest-storm.cz)*Math.min(1,dt*0.35);

  const t=Math.max(0,storm.t);
  document.getElementById('greloj').textContent=`${Math.floor(t/60)}:${String(Math.floor(t%60)).padStart(2,'0')}`;
  // *** DAÑO DE TORMENTA ***
  const fuera=Math.hypot(P.x-storm.cx,P.z-storm.cz)>storm.r;
  document.getElementById('gdmg').classList.toggle('show',fuera&&!muerto);
  if(fuera&&!muerto)recibirDanio((3+storm.fase*2)*dt);
}
/* ¿hay línea de tiro entre dos puntos? (las casas tapan) */
function visible(ax,az,bx,bz){
  const n=16;
  for(let i=1;i<n;i++){
    const t=i/n,x=ax+(bx-ax)*t,z=az+(bz-az)*t;
    for(const b of edificios)
      if(Math.abs(x-b.x)<b.w/2&&Math.abs(z-b.z)<b.d/2)return false;
  }
  return true;
}
function disparoEnemigo(e,d){
  tracers.push({x1:e.x,y1:2.5,z1:e.z,x2:P.x,y2:P.y+2.2,z2:P.z,t:0});
  const prec=Math.max(0.15,0.62-d/70);         // más lejos = falla más
  if(Math.random()<prec){recibirDanio(5+Math.random()*7);flashRojo=1;}
}
function tickEnemigos(dt){
  enemigos.forEach(e=>{
    if(!e.vivo)return;
    const dx=P.x-e.x,dz=P.z-e.z,d=Math.hypot(dx,dz);
    e.alerta=!muerto&&d<46&&visible(e.x,e.z,P.x,P.z);
    if(e.alerta){
      e.yaw=Math.atan2(dx,dz);                 // encarar al jugador
      const fx=Math.sin(e.yaw),fz=Math.cos(e.yaw);
      const mv=d>22?1:(d<13?-1:0);             // acercarse / mantener distancia
      const sp=8*dt*mv;
      // Colisión resbaladiza para evitar atascos
      if(sp) {
        if(!colisiona(e.x+fx*sp,e.z)) e.x+=fx*sp;
        if(!colisiona(e.x,e.z+fz*sp)) e.z+=fz*sp;
      }
      const st=Math.sin(anim*1.6+e.fase)*6*dt; // moverse de costado
      const rx=Math.cos(e.yaw)*st,rz=-Math.sin(e.yaw)*st;
      if(!colisiona(e.x+rx,e.z)) e.x+=rx;
      if(!colisiona(e.x,e.z+rz)) e.z+=rz;
      e.cool-=dt;
      if(e.cool<=0){e.cool=1.0+Math.random()*1.3;disparoEnemigo(e,d);}
    }else{
      e.t+=dt;
      if(e.t>3){e.t=0;e.yaw=Math.random()*6.28;}
      const sp=5*dt,fx=Math.sin(e.yaw),fz=Math.cos(e.yaw);
      const nx=e.x+fx*sp,nz=e.z+fz*sp;
      if(!colisiona(nx,nz)&&Math.abs(nx)<LIM&&Math.abs(nz)<LIM){
        if(!colisiona(e.x+fx*sp,e.z)) e.x+=fx*sp;
        if(!colisiona(e.x,e.z+fz*sp)) e.z+=fz*sp;
      } else {
        e.yaw=Math.random()*6.28;
      }
    }
    if(Math.hypot(e.x-storm.cx,e.z-storm.cz)>storm.r){e.vida-=8*dt;if(e.vida<=0)e.vivo=false;}
  });
  const vivos=enemigos.filter(e=>e.vivo).length+1;
  if(vivos!==gvivos){gvivos=vivos;document.getElementById('gvivos').textContent=gvivos;}
}
function tickCofres(){
  cofres.forEach(c=>{
    if(c.abierto)return;
    if(Math.hypot(c.x-P.x,c.z-P.z)<3.2){
      c.abierto=true;P.cofres++;
      GARMAS.forEach(a=>{if(a.tipo==='arma')a.am=a.max;else a.am=Math.min(a.max,a.am+1);});
      pintGInv();actualizarDesafios();
    }
  });
}
/* --- humo de chimeneas --- */
let humos=[],humoAcc=0;
function tickHumos(dt){
  humoAcc+=dt;
  if(humoAcc>0.3){
    humoAcc=0;
    const cs=edificios.filter(e=>e.ch&&Math.hypot(e.chx-P.x,e.cz-P.z)<65);
    if(cs.length&&Math.random()<0.5){
      const e=cs[Math.floor(Math.random()*cs.length)];
      humos.push({x:e.chx+(Math.random()-.5)*0.2,z:e.cz+(Math.random()-.5)*0.2,
        y:e.h+e.rh+1.0,vy:1.3,life:4,fase:Math.random()*6.28,s:0.5});
    }
  }
  humos.forEach(h=>{
    h.y+=h.vy*dt;h.vy+=0.35*dt;
    h.x+=Math.sin(h.y*1.3+h.fase)*0.45*dt;
    h.z+=Math.cos(h.y*0.9+h.fase)*0.45*dt;
    h.life-=dt;h.s+=0.4*dt;
  });
  humos=humos.filter(h=>h.life>0);
}
function dibHumos(){
  humos.forEach(h=>{
    const c=proj(h.x,h.y,h.z);if(c.z<NEAR)return;
    const s=scr(c);
    const r=Math.min(W*0.5,h.s*FOC()/c.z);
    gctx.fillStyle=`rgba(200,200,208,${Math.min(.28,h.life*0.09)})`;
    gctx.beginPath();gctx.arc(s.x,s.y,r,0,7);gctx.fill();
  });
}

function nuevaPartida(){
  generarMundo();resetStorm();
  P.x=0;P.z=-26;P.yaw=0;P.y=0;P.vy=0;P.salud=100;P.escudo=75;P.kills=0;P.cofres=0;
  pitch=0.22;muerto=false;gvivos=12;flashRojo=0;tracers=[];impactos=[];humos=[];humoAcc=0;
  GARMAS.forEach(a=>a.am=a.max);
  document.getElementById('gkills').textContent='0';
  document.getElementById('gvivos').textContent='12';
  actualizarBarras();actualizarDesafios();pintGInv();
}

gcv.addEventListener('mousedown',()=>{
  if((muerto || gvivos === 1) && pantalla==='game') nuevaPartida();
});

let anim=0,moviendo=false,last=performance.now();
function loop(now){
  const dt=Math.min(0.05,(now-last)/1000);last=now;
  if(pantalla==='game'&&W>1){
    anim+=dt;moviendo=false;
    if(!muerto){
      const sp=(keys['ShiftLeft']?30:19)*dt;
      const fx=Math.sin(P.yaw),fz=Math.cos(P.yaw);
      let dx=0,dz=0;
      if(keys['KeyW']){dx+=fx;dz+=fz;}
      if(keys['KeyS']){dx-=fx;dz-=fz;}
      if(keys['KeyA']){dx-=fz;dz+=fx;}
      if(keys['KeyD']){dx+=fz;dz-=fx;}
      const len=Math.hypot(dx,dz);
      if(len>0.01){mover(dx/len*sp,dz/len*sp);moviendo=true;}
      P.vy-=22*dt;P.y+=P.vy*dt;if(P.y<0){P.y=0;P.vy=0;}
      cooldown-=dt;
      if(disparando&&cooldown<=0)disparar();
      retro=Math.max(0,retro-dt*5);
      flashRojo=Math.max(0,flashRojo-dt*2.2);
      impactos.forEach(im=>im.t+=dt);
      impactos=impactos.filter(im=>im.t<1);
      tracers.forEach(t=>t.t+=dt);
      tracers=tracers.filter(t=>t.t<0.14);
      tickStorm(dt);tickEnemigos(dt);tickCofres();tickHumos(dt);
    }
    grender();
  }
  requestAnimationFrame(loop);
}
pintGInv();requestAnimationFrame(loop);
</script>
</body>
</html>
```

### 🤖 Claude  <small>2026-08-05 04:03</small>

¡Buenas mejoras! Antes de aplicarlo lo revisé línea por línea y encontré **algunos problemas serios en ese código** que hay que corregir, sobre todo uno que reintroduce el bug que más te molestaba. Te lo aplico ya arreglado.

### 🤖 Claude  <small>2026-08-05 04:09</small>

_[usó herramienta: Write]_

### 🧑 Vos  <small>2026-08-05 04:09</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-08-05 04:09</small>

_[usó herramienta: mcp__Claude_Browser__javascript_tool]_

### 🧑 Vos  <small>2026-08-05 04:09</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-08-05 04:09</small>

El navegador interno se desconectó. Verifico la sintaxis y la lógica con Node en su lugar.

### 🤖 Claude  <small>2026-08-05 04:09</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-08-05 04:09</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-08-05 04:09</small>

Sintaxis correcta. Ahora ejecuto el juego de verdad en Node con un canvas simulado para probar la lógica y la geometría.

### 🤖 Claude  <small>2026-08-05 04:09</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-08-05 04:09</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-08-05 04:10</small>

El harness me devolvió copias viejas de los arreglos. Lo arreglo con getters.

### 🤖 Claude  <small>2026-08-05 04:10</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-08-05 04:10</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-08-05 04:10</small>

El mundo se genera bien y ningún enemigo nace atrapado. Ahora la prueba crítica: **que las cosas no exploten ni desaparezcan al pegarte a ellas**.

### 🤖 Claude  <small>2026-08-05 04:10</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-08-05 04:10</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-08-05 04:10</small>

Ninguna cara desaparece a ninguna distancia y las coordenadas quedan **finitas y acotadas**. Comparo contra el código sin recorte para confirmar que el arreglo importa:

### 🤖 Claude  <small>2026-08-05 04:10</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-08-05 04:10</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-08-05 04:10</small>

Confirmado: sin recorte las coordenadas llegaban a **1,77 millones de píxeles** (eso es "tapa toda la pantalla"); con recorte quedan en 6.778. Ahora las demás mejoras:

### 🤖 Claude  <small>2026-08-05 04:11</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-08-05 04:11</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-08-05 04:11</small>

La tormenta ya es suave ✓, pero **2 de 4 enemigos siguen atascados** — el arreglo de ejes separados no alcanza. Investigo la causa real:

### 🤖 Claude  <small>2026-08-05 04:11</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-08-05 04:11</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-08-05 04:11</small>

Encontré la causa real: **los edificios se superponen entre sí (7 pares)** y, una vez que algo queda dentro de una caja de colisión, *todos* sus movimientos se rechazan y queda congelado para siempre. Lo arreglo en tres frentes.

### 🤖 Claude  <small>2026-08-05 04:11</small>

_[usó herramienta: Edit]_

### 🧑 Vos  <small>2026-08-05 04:11</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-08-05 04:12</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-08-05 04:12</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-08-05 04:12</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-08-05 04:12</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-08-05 04:12</small>

Todos libres, incluso uno que metí **dentro** de una casa a propósito. Ahora la victoria, el arsenal nuevo y el rendimiento:

### 🤖 Claude  <small>2026-08-05 04:12</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-08-05 04:12</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-08-05 04:12</small>

Todo correcto. Ahora mido la **carga de dibujo**, que es el riesgo real de los ladrillos y el pasto:

### 🤖 Claude  <small>2026-08-05 04:13</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-08-05 04:13</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-08-05 04:13</small>

Son **~3.900 rellenos y 1.300 trazos por cuadro** — demasiado para canvas 2D. Veo de dónde viene el grueso:

### 🤖 Claude  <small>2026-08-05 04:13</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-08-05 04:13</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-08-05 04:13</small>

Los ladrillos son el 90% del costo — y se están dibujando **las 4 paredes de cada edificio, incluidas las 2 traseras que nunca se ven**. Agrego descarte de caras traseras:

### 🤖 Claude  <small>2026-08-05 04:13</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-08-05 04:13</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-08-05 04:14</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-08-05 04:14</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-08-05 04:14</small>

De **5.265 a 3.576 operaciones por cuadro** (los trazos, que son lo más caro, bajaron 57%). Corrida final de verificación completa:

### 🤖 Claude  <small>2026-08-05 04:14</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-08-05 04:14</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-08-05 04:14</small>

Esa única falla es mi prueba siendo demasiado estricta. Lo verifico:

### 🤖 Claude  <small>2026-08-05 04:15</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-08-05 04:15</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-08-05 04:15</small>

Confirmado: solo deja de dibujarse a 0,3 unidades mirando muy hacia abajo — cuando el objeto está **literalmente detrás de la cámara**. Eso es correcto. Desde 1 unidad siempre se ve. Son **18/18**.

### 🤖 Claude  <small>2026-08-05 04:15</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-08-05 04:15</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-08-05 04:15</small>

¡Aplicado! Pero **no lo copié tal cual** — ese código traía tres bugs serios, uno de ellos volvía a meter el problema que más te molestaba. Recargá:

```bash
xdg-open /home/matiigonzz/Claude/batalla-real.html
```

## Lo bueno que traía y quedó

Todo el contenido nuevo entró: **edificios con textura de verdad** (ladrillo, madera, piedra y chapa según la zona), **techos a dos aguas con tejas**, ventanas con marco y postigos, **chimeneas que echan humo**, **pasto y flores que se mecen**, árboles voxel con tronco y copa, íconos SVG de armas, y el **arsenal nuevo**. Probé las 4 armas y hacen exactamente su daño: Subfusil 14, Rifle 32, Escopeta 85 y **AWP 125 (mata de un tiro)**. Botiquín y Poción curan a 100.

## Los 3 bugs que traía el código y corregí

**1. Volvía a romper lo de "veo solo verde/amarillo"** ⚠️
El dibujo de cajas perdió la protección del plano cercano. Lo medí: al pegarte a un árbol, las coordenadas llegaban a **1.770.000 píxeles** — o sea, tapaba toda la pantalla otra vez.
Además, el arreglo de "que no desaparezcan de cerca" no funcionaba: seguía el corte que los borraba.
**Solución:** en vez de descartar, ahora **recorto** las figuras contra el plano cercano. Eso resuelve las dos cosas juntas: ya no explotan **ni** desaparecen. Verificado en 40 combinaciones de distancia y ángulo.

**2. Los enemigos seguían atascándose**
El arreglo de ejes separados no alcanzaba: **2 de 4 seguían congelados**. La causa real era otra — los edificios se generaban **superpuestos entre sí (7 pares)**, y cuando algo queda *dentro* de una caja de colisión, todos sus movimientos se rechazan y queda preso para siempre.
**Solución:** ya no se generan edificios encima de otros, y agregué una regla de escape. Ahora se despegan los 5, incluso uno que metí **adentro de una casa** a propósito. El jugador también puede salir si queda atrapado.

**3. Se veía el interior de los edificios**
El orden de dibujado estaba invertido (pintaba las paredes de atrás **encima** de las de adelante).
**Solución:** orden corregido, y de paso agregué descarte de caras traseras — se dibujaban las 4 paredes con todos sus ladrillos cuando solo se ven 2. Eso bajó la carga de **5.265 a 3.576 operaciones por cuadro**.

Lo tuyo de la **tormenta suave** sí estaba perfecto: medí 180 segundos y el mayor salto es de 0,08 unidades por cuadro. Y la **victoria** funciona (además le solté el mouse y frené el daño de la tormenta al ganar).

**17 de 17 pruebas pasan** (la única "falla" resultó ser mi test pidiendo que se dibuje algo a 0,3 unidades, o sea con el objeto detrás de la cámara).

---

Un aviso honesto: esta vez **el navegador se me desconectó**, así que verifiqué todo ejecutando el juego en Node con un canvas simulado — lógica, geometría y colisiones están comprobadas, pero **no pude medir los milisegundos reales de dibujo ni ver cómo se ve**. Con ~3.500 operaciones por cuadro debería ir fluido, pero si lo notás pesado decime y recorto más detalle.
