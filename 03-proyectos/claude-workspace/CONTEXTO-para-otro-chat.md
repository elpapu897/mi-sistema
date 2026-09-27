# LA DIEZ — contexto completo del proyecto

Pegá este archivo entero en el chat nuevo. Tiene todo lo necesario para seguir.

---

---

# ⚠️ LO QUE HAY QUE HACER AHORA (pedido del usuario, sin empezar)

Esto es lo primero que hay que atacar en el chat nuevo. Está ordenado por prioridad.

## 1. Arreglar cuatro minijuegos que quedaron confusos — ✅ HECHO (ver sección 20)
El usuario los probó y no se entienden. **No hay que rehacer los otros 14**, solo estos:

- **`corner` (Córner)** — "es medio difícil, no tiene nada que ver con un córner real".
  Hoy se ve el arco de frente y una mira que flota. Debería verse **como un córner de
  verdad**: la pelota en el banderín del córner, el área desde un ángulo que se entienda,
  los compañeros y los rivales agrupados en el área chica, y el centro dibujando una
  curva desde la esquina hasta la zona.
- **`centroP` (Descolgar)** — "no entendí bien esa". Hay que dejar clarísimo que sos el
  arquero y que la pelota viene de un centro: mostrar el área chica marcada, el delantero
  que va a cabecear, y que el arquero sale hacia la pelota, no que aparece un recuadro suelto.
- **`chilena` (Media vuelta)** — "la pelota baja del centro" no se entiende. Aclarar de
  dónde viene la pelota y que estás de espaldas al arco.
- **`sombrero`** — también hay que mejorarlo, no lo detalló.

Los archivos de referencia de cómo se ven hoy están descritos en la sección 18.
Ojo: probarlos **de a uno** (ver la nota de "Cómo probar minijuegos en headless").

## 2. Tarjetas, penales y tiros libres en el MODO DT — ✅ HECHO (sección 21)
Hoy las amarillas, las rojas y los penales existen **solo en el modo jugador**
(`tarjetaEnPartido()`, `hayPenal()`, `tirarPenal()`). El usuario quiere lo mismo
en el modo manager: que sus jugadores vean amarillas y rojas, se pierdan fechas por
suspensión, y que haya penales y tiros libres a favor y en contra durante el partido del DT.

## 3. Las amarillas no se están viendo — ✅ HECHO en el modo DT (falta reforzarlo en el modo jugador)
Dijo "no vi las amarillas". Existen y se generan (medido: 13 amarillas y 2 rojas en
3 temporadas), pero **no se muestran de forma visible**: solo aparece un chip chico en el
hub y una línea en el diario. Hay que darles presencia: avisarlas al terminar el partido,
mostrarlas en el perfil y en la agenda, y avisar cuando estás a una de la suspensión.

## 4. Formato real de cada liga
"Quiero que sea como el formato actual". Hoy **todas las ligas usan el mismo formato**:
todos contra todos a 22 fechas. Habría que respetar el formato real de cada una:
Argentina con Apertura/Clausura y zonas, la MLS con conferencias y playoffs,
México con liguilla, etc. Es un cambio grande en `nuevaTemporada()`, `generarFixture()`
y `finTemporada()`.

## 5. El online sigue sin conectar
El usuario nunca pudo conectar. **La hipótesis más fuerte es que abre el juego como
archivo suelto (`file://`), y ahí el navegador bloquea WebRTC por seguridad.**
Ya está el diagnóstico integrado (`probarConexion()`) que lo detecta y lo explica.
**Lo primero es pedirle que corra "Probar mi conexión" y diga qué le marca el primer punto.**
Si confirma lo del archivo, la solución es ayudarlo a subir el juego a un hosting con https.

---

**20 · Los cuatro minijuegos confusos, rehechos**
- Helpers de dibujo nuevos (arriba de `MG.punteria`): **`dArea3D(x,W,H)`** dibuja el área
  en perspectiva (arco con red arriba, área grande y chica en trapecio, punto de penal,
  tribuna oscura detrás de la línea) y devuelve la geometría; **`dEtiqueta`** (cartelito
  chico pegado a cualquier punto del dibujo), **`dSombra`** y **`dBanderin`**.
  Con las etiquetas se explica la escena adentro del canvas: VOS, TUS COMPAÑEROS,
  EL ARQUERO, ÁREA CHICA, EL ARCO RIVAL, etc.
- **`corner`**: ahora es un córner de verdad. La pelota arranca en el banderín (con el
  arco del córner dibujado), se ve el área en perspectiva, los compañeros agrupados cerca
  del área chica, los rivales marcando y el arquero. Dos toques: **dirección** (el abanico
  barre y la línea punteada muestra la curva del centro y dónde va a caer) y **fuerza**
  (la misma curva se estira y se acorta). La pelota vuela por la curva con sombra en el
  piso y los compañeros saltan. Si la mandás cerca del arquero, sale y la descuelga.
- **`centroP`**: se ve el arco, el **área chica remarcada en verde**, el centro que sale
  desde la punta, **el delantero que corre a cabecear** y vos, el arquero, con la corrida
  punteada que vas a hacer. La ventana para salir está pintada **encima de la trayectoria**
  ("SALÍ CUANDO PASE ACÁ"). Al tocar, el arquero sale hacia la pelota.
- **`chilena`**: vista de costado con el arco rival a la izquierda. El compañero está
  atrás tuyo a la derecha y **la pelota sale de su pie** en parábola; vos estás de espaldas
  al arco (cartel + flecha de giro). Hay que rematar cuando la pelota baja a la
  **franja verde de altura de remate**; después el muñeco gira y la pelota sale al arco.
- **`sombrero`**: el defensor **se acerca de verdad** (antes se teletransportaba), avisa
  con un "SE PREPARA" (se agacha, círculo amarillo) y recién ahí se tira, con rastro y
  círculo rojo de peligro. Si picás durante la barrida, la pelota va por arriba y vos
  esquivás; cuanto antes la picás una vez que se tiró, más puntaje.
- Los cuatro textos de `MG_INFO` se reescribieron. `mgVistos()` tiene una **migración
  `__v2`** que borra los cuatro de `ladiez_mg_vistos`, así el que ya jugaba vuelve a ver
  la explicación nueva una vez.
- **Cómo se probaron**: `/tmp/mkprobe.py` genera una copia del juego con una sonda que
  reemplaza `requestAnimationFrame` y `setTimeout` por colas propias, corre el minijuego
  cuadro a cuadro con un reloj falso que arranca en `performance.now()`, simula los toques
  en los frames que le pidas y va copiando el canvas a una **tira de miniaturas**, así un
  solo screenshot muestra la partida entera y el resultado final.

---

**21 · El bug que trababa el partido, dificultad y reglas en el 11v11**

*(sesión pedida por el usuario: "no me deja continuar el partido")*

**EL BUG (importante, era esto)**
- Se probaron los 18 minijuegos con una sonda automática y **6 nunca llamaban a `done()`**
  si el jugador no tocaba a tiempo: `punteria`, `tiroLibreC`, `unoVuno`, `saqueP`,
  `paredN` y `corner`. El partido quedaba **trabado para siempre, sin botón de continuar**.
- Arreglo en dos capas:
  1. **`mgArrancar()`** envuelve todos los minijuegos: `done` protegido contra doble llamada,
     a los **5 s** aparece un botón *"Seguir el partido ▶"* (en un `#mgSalto` propio, para no
     pisar el `#mgFoot` que usan algunos juegos) y a los **12 s** se resuelve solo con
     puntaje bajo. Pase lo que pase el partido sigue.
  2. `cuentaAtrasMG` tiene un respaldo por `setTimeout` (3,4 s) por si se pierde el
     `setInterval`. **Ojo**: la primera versión de ese respaldo hacía `luego=una` con `una`
     llamando a `luego` → recursión infinita, no arrancaba ningún minijuego. Hay que guardar
     el original (`const _org=luego`). Lo detectó la sonda.
- El `corner` además tiene ahora límite propio de 9,5 s con barra de tiempo.

**DIFICULTAD (`DIFS`, guardada en `ladiez_dif`)**
- Tres niveles: **FÁCIL / NORMAL / DIFÍCIL**, aplicados a todo el juego:
  - minijuegos: `sc*mgMul+mgAdd` dentro del `fin` de `lanzarMG` (una sola línea afecta a los 18)
  - rivales simulados: `DIF.riv` (±4 de media) en `simularUno`, `simEquipo` y `simularDT`
  - motor físico: `DIF.cpu` multiplica `acc` y `kick` **sólo del equipo B en modo cpu**
  - economía del DT: `eco()` multiplica todo por `DIF.eco`
  - tarjetas (`DIF.tarj`), lesiones (`DIF.les`) y gemas por subir de nivel (`DIF.gemas`)
- Pantalla `R.dificultad` con las tres opciones y **la lista de qué cambia cada una**.
  Se entra desde Ajustes, desde la creación de carrera y desde `dtInicio` (`irDificultad(v)`).

**FALTAS, TARJETAS, TIROS LIBRES Y PENALES EN EL 11v11** (lo usa el modo DT)
- La falta sale de la **colisión entre rivales**: si la velocidad relativa supera 2,1 y la
  pelota está cerca, el más rápido comete la falta (`cobrarFalta`). `P.freeze` congela
  1,25 s con el cartel.
- **Tarjetas** según la dureza del choque: amarilla frecuente, roja sólo con entradas muy
  fuertes o segunda amarilla. La roja **saca al jugador de la cancha** (el equipo queda con 10).
- **Penal** si la falta es dentro del área (`enArea`/`areaDe`).
- `armarPelotaParada()` acomoda todo: pelota en el punto, **barrera de 3** si está cerca del
  arco, el resto a 165 px, y **si el equipo beneficiado es el tuyo, el ejecutor sos vos**.
  `P.dead` bloquea que cualquier otro toque la pelota. Si nadie patea en **7 s**, la ejecuta
  la CPU sola (esto evita otro cuelgue).
- Se dibuja: círculo punteado, flecha al arco, barrera marcada en amarillo, ejecutor con aro
  verde, banda fija arriba con el tipo de jugada y barra de tiempo, cartel de falta con la
  **tarjeta dibujada** y la lista de tarjetas del partido en una esquina.
- Al terminar, `finP` guarda `window._ULTPART` y **`resultadoDT` aplica las sanciones**:
  `aplicarTarjetasDT()` lleva amarillas por jugador (**quinta = una fecha**), rojas (1-2 fechas),
  avisa cuando alguien está a una de la suspensión y descuenta una fecha por partido.
  `disponible(j)` ahora mira `j.susp`, así **el once nunca pone a un suspendido**.
- Los partidos **simulados** del DT también generan tarjetas (`tarjetasSimDT`).
  Medido: ~9-14 amarillas y alguna roja cada 8 fechas.
- El modal del final del partido muestra tarjetas, avisos y los que no están para la próxima.

**GRÁFICOS**
- El estadio del 11v11: **tribunas con público animado** de los colores de los dos clubes,
  césped con franjas dobles, área chica, **punto y semicírculo de penal**, arcos de córner,
  y un poco menos de zoom (`*.925`) para que se vean las gradas.

**Cómo se probó** (sondas en `/tmp`, se borran entre sesiones):
- `mkall.py` → corre los 18 minijuegos con 0/1/2/3 toques y dice cuál no resuelve.
- `mkmatch.py` → crea una carrera y juega un partido entero solo, clickeando CONTINUAR.
- `mkfis.py` → corre 3.600 cuadros del 11v11 con reloj virtual (`Date.now` stubeado),
  fuerza un penal y saca capturas de los carteles.
- `mkdt.py` → crea un DT y simula 8 fechas para contar tarjetas y suspensiones.
- **Clave para estas sondas**: hay que stubear `setTimeout`/`setInterval` **respetando los
  delays** (cola con `at:t+ms`), si no los watchdogs disparan al instante y todo da falso.

**Queda pendiente de lo que pidió**: mejorar los gráficos de las pantallas de **Desafíos**
y del hub del jugador (esta sesión sólo se mejoraron los minijuegos y el estadio del 11v11).

---

**22 · Copa arreglada, tarjetas fuera del modo jugador y personalización nueva**

**EL BUG DE LA COPA (se trababa en cuartos/semis ganando)**
- Causa: si `resultadoCH` tiraba una excepción, `finP` ya había hecho `P=null` y
  `cancelAnimationFrame`, así que **la pantalla quedaba congelada en la cancha sin modal**.
  Explotaba cuando `CH.vivos`/`CH.tabla` venían de una partida vieja (undefined) o cuando
  `CH.rival` no era un índice válido de `copaEq(CH.modo)` — eso también explica el cruce
  absurdo tipo *Real Madrid vs Vélez*: índices de una copa aplicados a la lista de otra.
- Arreglos:
  - **`sanearCH()`**: normaliza `modo`, `yo`, `rival`, `vivos`, `top8`, `po`, `tabla`,
    `eliminados` y `camino`; si el rival no existe o sos vos mismo, resortea uno válido
    **de la misma copa**. Se llama en `resultadoCH`, `chJugar`, `chSimular`, `cargarCH` y `R.chHub`.
  - `sortearRivalCH` valida el índice elegido y tiene fallback.
  - **`finP` envuelve el `onFin` en try/catch**: si el cierre falla, igual te saca de la cancha
    y te muestra el resultado. Nunca más se puede quedar atrapado ahí.
- Probado: **75 campañas completas (ucl/lib/mun) ganando siempre 3-0, 0 errores**, más casos
  de estado roto a propósito (rival=99, rival=yo, tabla=null) que ahora se corrigen solos.

**TARJETAS FUERA DEL MODO JUGADOR** (lo pidió el usuario)
- `resolver()` y `simularUno()` ya no llaman a `tarjetaEnPartido()` (la función queda pero
  sin uso). El minijuego `barrida` ya no da roja ni amarilla, sólo falta.
- Se sacaron los chips 🟨/🟥 del hub. **En el modo DT las tarjetas siguen** (ahí sí las quería).

**PERSONALIZACIÓN DEL JUGADOR (el foco de la sesión)**
- `dibujarCara(c,tam,{col})` rehecha: SVG con **hombros con la camiseta del club**, cuello,
  orejas, sombra y luz laterales, párpados, iris con brillo, cejas, nariz y boca separadas.
- Opciones: **8 tonos de piel, 10 colores de pelo, 12 cortes**
  (corto, taper, rulos, afro, largo, mullet, rapado, entradas, tupé, mohicano, colita, trenzas),
  **4 formas de cara**, 6 barbas, 3 cejas, 3 narices, 3 bocas, 6 colores de ojos,
  vincha (toma el color del club), aritos y tatuaje en el cuello.
- **El pelo se dibuja en dos capas** (`{a:atrás, f:adelante}`): lo que cae —trenzas, mullet,
  largo, afro, colita— va **detrás de la cara**. Antes tapaba el rostro.
- `caraOk(c)` completa las caras viejas con los campos nuevos, así no se rompe ningún guardado.
- Editor `R.personalizar` con **retrato grande y 5 pestañas** (`PTAB`):
  CARA / PELO / DETALLES / FICHA / JUEGO (tema y fondo quedaron adentro de JUEGO).
- **Dorsal del 1 al 99** (`G.dorsal`), con atajos y campo libre. Se ve en el hub, sobre la cara.
- **Físico con efecto real**: altura (168/176/185/194) y contextura (delgado/normal/fuerte).
  Alto = +físico −regate −vel; bajo = +vel +regate −físico; fuerte = +físico +marca −vel;
  delgado = +vel −físico. `aplicarFisico()` **revierte el ajuste anterior con `G.fisDelta`**
  en vez de recalcular desde una base, así no borra lo que ganaste subiendo de nivel.
- Todo esto también se elige **al crear el jugador** (bloque de aspecto + dorsal + físico).
- `dJugador` (el muñeco de los minijuegos) mapea los cortes nuevos a los que sabe dibujar.
  **Cuidado**: ahí `c` es `const`, no se puede reasignar (rompió una vez, lo agarró la sonda).

**Pendiente que mencionó el usuario y no se hizo**: la idolatría sigue siendo fácil
("es muy fácil ser querido"), y faltan los gráficos de Desafíos.

---

**23 · Pantalla "TU JUGADOR" estilo consola (pedida con una captura de referencia)**
- `dibujarJugador(c,opt)`: el jugador **de cuerpo entero en SVG**, dibujado por código.
  Camiseta con el **patrón real del club** (`kitDe` → vert, horiz, bandaV/H/D, mitades, diagM,
  mangas), short con el **dorsal estampado**, medias del color del club, botines y sombra.
  Las proporciones responden al físico: `an` (ancho) por contextura y `es` (alto) por altura.
  Canon de coordenadas en el objeto `Y` (cab/cue/hom/cin/sho/mus/med/bot/pie), viewBox 200x430.
- `caraSVG(c)` reutiliza el retrato de `dibujarCara` para la cabeza (le saca hombros y fondo
  con un replace). **Ojo**: si se toca `dibujarCara` hay que revisar esos replaces.
- `R.personalizar` rehecha con el layout de la referencia:
  - `.pjWrap` con fondo de estadio y luces (`.pjLuces`, puro CSS).
  - Arriba a la izquierda el **dorsal gigante + la posición**; al centro el jugador; a la derecha
    la **ficha** (posición, pie hábil, altura, **peso** con `pesoDe()`, nacionalidad con bandera,
    media) y el botón **SORPRENDEME**.
  - Barra de pestañas con íconos (`.pjTabs`) y **columnas de opciones** (`.pjOpts`/`.pjCol`):
    tono de piel y color de ojos en bolitas (los ojos con degradado radial tipo iris),
    **forma de la cara con siluetas SVG**, y cejas/nariz/boca en botones apilados.
  - En móvil pasa a una columna y la figura baja a 290px de alto.
- **Trampa**: el CSS global pone `button{width:100%}`; en `.pjTabs` hay que forzar `width:auto`
  o las pestañas se apilan a pantalla completa.
- **Trampa 2**: `.pjFig` necesita **altura fija**, si no el SVG toma el ancho del celular y
  se estira a 900px de alto.
- La creación de carrera muestra el mismo muñeco de cuerpo entero con la camiseta del club elegido.

---

**24 · 3D de verdad: motor propio, jugador y entrenador**

**MOTOR 3D CASERO** (sin librerías, sigue andando sin internet). Está arriba de `modeloJugador`:
- `M3()` acumula caras; `m3Box`, `m3Cyl` (tronco de cono, acepta **un color por segmento** →
  las rayas verticales de la camiseta salen gratis) y `m3Sph` (esfera con rangos `v0/v1` y
  `u0/u1`, que es lo que permite hacer casquetes de pelo y barbas).
- `m3Draw(x,M,cam)`: rota en Y y X, **descarta caras traseras** (`nz>0.02`), calcula luz difusa
  por normal, ordena por profundidad (algoritmo del pintor) y pinta en canvas 2D.
  `m3col()` aclara/oscurece el color según la luz. Un jugador son ~1.100 caras y va fluido.
- `jugador3D(id,cfg)` monta el canvas, lo hace **girar con el dedo** (con inercia) y anima.

**TRAMPA GRANDE (costó encontrarla)**: con el algoritmo del pintor, dos superficies casi
pegadas (la piel de la cabeza y el casquete de pelo) **pelean por quién se dibuja encima** y
aparecen "gajos" alternados. La solución no es separar más las capas: es **no dibujar la piel
donde va el pelo**. Ahora el pelo define `pV` (hasta dónde tapa adelante) y `pN` (atrás), y la
cabeza se dibuja con `v0:pV-.012` para el frente y `v0:pN-.012` para la nuca. Cero costuras.
- Los rasgos (ojos, cejas, nariz, boca, barba) se posicionan con **`zsup(x,y)`**, que devuelve
  la z exacta de la superficie de la cabeza en ese punto, así nada flota ni se hunde.

**Jugador**: `modeloJugador(cara,opt)` arma cuerpo entero con la camiseta del club (patrón real),
short con dorsal, medias, botines, y **proporciones según altura y contextura**.

**Altura libre**: slider de 150 a 210 cm (`setAltura`) + atajos. `aplicarFisico()` ahora usa una
curva continua (`k=(h-176)/10`) en vez de escalones.

**Barbas rehechas**: se dibujan como casquetes esféricos por fuera de la cabeza (`v0/v1`), y la
boca se vuelve a dibujar **por encima** de la barba, así la chivita y la barba cerrada ya no la tapan.

**ENTRENADOR 3D** (`R.dtLook`, se entra desde una placa del hub del DT):
- Mismo modelo con `opt.dt`: saco/campera, camisa, **corbata**, solapas, cierre, pantalón largo
  y zapatos. Extras: **bufanda, gorro de lana y guantes** (el gorro reemplaza al pelo).
- `ROPA_DT` (6 prendas: traje, traje claro, chomba, buzo, campera deportiva, campera de invierno)
  y `EXTRA_DT`. Los colores salen del club. Lo que no es gratis **se compra con la caja del club**
  (`dtComprar`), y queda guardado en `D.ropaOk` / `D.extraOk` / `D.look`.
- El técnico tiene su propia cara editable (`D.cara`) con las mismas pestañas.

**Pendiente**: poses/animaciones (festejo, brazos cruzados) y que el modelo 3D se use también en
el hub y en los minijuegos (hoy siguen con el retrato 2D, que quedó como cara de perfil).

---

**25 · El modelo 3D rehecho: de piezas sueltas a malla continua**

El usuario mandó una captura: el modelo se veía **desarmado** (hombreras enormes, brazos flotando,
bloques sueltos). La causa: estaba armado con primitivas separadas (esferas de hombro, cilindros
de brazo) que no se fusionan entre sí.

- **`m3Loft(M,secs,seg,opt)`**: nueva primitiva que une **secciones transversales** consecutivas
  (`{y,rx,rz,cx,col}`) formando una superficie continua. Es lo que usa el low-poly de verdad.
  El color puede ser una **función `(i,seg)`** → así salen las rayas verticales de la camiseta.
- `modeloJugador` rehecho con un canon humano (cabeza −92, hombro −68, cintura −26, rodilla 42,
  suela 104; cabeza ≈ 1/8 del cuerpo). Torso, brazos y piernas son lofts; ya no hay bolas de
  hombro ni de rodilla. Cuello de camiseta, escudo, vivo de las medias y botines aparte.
- **BUG QUE COSTÓ**: al reemplazar el bloque viejo quedó **duplicado el cilindro del cuello**
  (`m3Cyl(M,0,-44,0,7.5,7.5,14,10,som)`) en medio del pecho: se veía un cuadrado color piel
  flotando sobre la camiseta. Se encontró listando las caras cuyo centroide caía en el pecho
  (`|x|<9, -62<y<-30, z>6`) y mirando el color (`#b88a62` = `mez(piel,.18,0)`).
  **Lección**: cuando se corta y pega un bloque grande con índices, verificar que el delimitador
  `fin` no quede repetido; conviene un `grep` del patrón después de editar.
- Encuadre recalibrado para el canon nuevo: `esc=h*0.0066*mod.es`, `cy0=h*0.52`.

**El técnico** usa el mismo cuerpo con `opt.dt`: saco/campera, camisa, corbata, solapas, pantalón
largo y zapatos. Con pantalón largo el tobillo toma el color del zapato (si no, quedaba un
pedacito de piel entre el pantalón y el calzado).

---

**26 · Balance de tarjetas y afinado del modelo**

**LAS ROJAS (el usuario reportó 4 por partido: injugable)**
- Antes: umbral de falta `vr>2.1` con probabilidad hasta .9, y roja con `dura>6.2`. Cualquier
  choque era falta y media falta era roja.
- Ahora: `vr>3.9`, probabilidad máxima **.30**, la pelota tiene que estar a menos de 120-150 px,
  **mínimo 7 segundos entre faltas** (`P.ultFalta`), amarilla sólo con entradas fuertes,
  **roja casi siempre por doble amarilla** (la directa pide `dura>8.6` y 10%), y **tope de una
  expulsión por equipo por partido** (`P.rojasEq`).
- Medido con 8 partidos completos de 150 s: **3 faltas, 1 amarilla y 0 rojas** por partido.
  (La sonda está en `/tmp/mkbal.py`; **clave**: stubear `pintarP` para que corra rápido y leer
  los datos de `window._ULTPART`, porque al terminar el partido `P` ya es `null`.)
- Las tarjetas de los partidos **simulados** del DT también bajaron (roja 4,5%).

**MODELO**
- Brazos casi rectos y pegados al cuerpo (antes se abrían en diagonal y parecían piezas sueltas).
- Manos compactas (antes eran un palo de piel).
- Zapatos más chicos y proporcionados.
- **El pelo se subió** (`PEL` con v1 de .21 a .28): antes el borde del casquete se juntaba con
  las cejas y quedaba una franja negra sobre los ojos.
- Cejas más finas, torso con más profundidad (de perfil se veía plano) y hombros más marcados.
- `SEG` del torso 14→20 y lofts de brazos/piernas 10→12: se ve más suave.

**LA CARA EN LA FICHA**: se agregó `.pjAvatar`, un retrato circular con la cara del jugador
(o del técnico) al lado del nombre, en las dos pantallas.

**RECOMENDACIÓN PENDIENTE (charla con el usuario)**: el 3D dibujado a mano con polígonos en
canvas 2D tiene un techo y no va a parecerse a un render profesional. Las opciones son
(a) asumir un estilo **muñeco/figurita** bien resuelto, (b) volver al retrato 2D ilustrado
—que quedaba más prolijo— o (c) three.js, que necesitaría internet o incrustar la librería.

---

**27 · 3D REAL con three.js incrustado (el usuario eligió este camino)**

- **`three.min.js` r150 (614 KB) va incrustado dentro del HTML** en su propio `<script id="three3d">`,
  antes del script del juego. Así el 3D **sigue funcionando sin internet**. El archivo pasó de
  3,5 MB a **4,1 MB**. (r128 no sirve: no tiene `CapsuleGeometry`, que apareció en r140.)
- **`armar3D(cara,opt)`** construye el jugador con geometrías de verdad: `LatheGeometry` para el
  torso y el short (perfil revolucionado: hombros, cintura, cadera), `CapsuleGeometry` para brazos
  y piernas, esferas para cabeza/hombros/manos. Materiales `MeshStandardMaterial` con roughness.
- **La camiseta es una textura** (`texKit`): se pinta el patrón real del kit en un canvas
  (rayas verticales/horizontales, bandas, mitades) y se mapea al torso.
- **LA CARA TAMBIÉN ES TEXTURA** (`texCara`): ojos con iris y brillo, párpados, cejas, sombra de
  nariz y boca, todo pintado en un canvas 512×256 y mapeado a la esfera de la cabeza.
  **Esto fue clave**: con geometrías sueltas los ojos quedaban saltones y las cejas flotando.
  - **Dato importante**: en `SphereGeometry` de three.js el **frente cae en u=0.25**, así que la
    cara se dibuja centrada en `x = ancho*0.25` del canvas.
  - En 3D quedan sólo el volumen de la nariz, el pelo, la barba y las orejas.
- Luces: hemisférica + key con **sombra real** (PCFSoftShadowMap) + fill + rim, y un
  `ShadowMaterial` en el piso para la sombra proyectada.
- `jugador3D` prueba WebGL y, si falla, **cae al motor casero** (`jugador3Dcanvas`, que quedó
  como respaldo). Girar con el dedo funciona igual en los dos.
- Cámara: `position (0,.74,2.95)`, `lookAt (0,.72,0)`, FOV 30. El canon del modelo va de y=0
  (suelo) a y≈1.35 (tope de la cabeza), cabeza ≈ 1/6,4 del cuerpo.
- **Para probar 3D en headless**: el canvas WebGL **no sale en el screenshot**. El truco es crear
  el renderer con `preserveDrawingBuffer:true`, renderizar y reemplazar el canvas por un
  `<img src=canvas.toDataURL()>`, que sí se captura. Sonda en `/tmp/mk3js.py`.

**La cara del jugador también aparece** (lo pidió el usuario) en el banco de suplentes, en la
tabla del resto del plantel y en la fila de tu club en la tabla de posiciones (`.miniCara`).

---

**28 · Modelo 3D: canon profesional y dos bugs de render que lo arruinaban**

El usuario mostró su captura: el muñeco se veía mal. Se encontraron **dos bugs concretos**
(no era sólo cuestión de gusto):

1. **La pieza de la nuca del pelo tapaba media cara.** Estaba creada con
   `SphereGeometry(..., phiStart: π*0.55, phiLength: π*0.9)`, y como **el frente (+Z) cae en
   phi = π/2**, esa pieza arrancaba a 9° del frente y cubría la mitad del rostro.
   Correcto: `phiStart: π, phiLength: π` (mitad de atrás).
   **Cómo se detectó**: prueba de calibración con una esfera texturada en 4 colores
   (`/tmp/uv.py`) para ver qué `u` cae al frente → **u = 0.25**, que es donde va la cara.
2. **La mandíbula usaba la misma textura de la cara**, así que dibujaba un segundo par de ojos
   y boca corridos. Ahora es un volumen de piel liso, por dentro.
3. **Colores lavados/pastel**: las `CanvasTexture` necesitan `texture.encoding = sRGBEncoding`
   (r150) o salen aclaradas, y **ACESFilmicToneMapping desatura mucho**: se pasó a
   `NoToneMapping` con luces más bajas (key 1.05, hemi .30, fill .26, rim .48/.26).

**Canon nuevo del modelo (7,5 cabezas, como un humano real)**: suelo 0 · rodilla .46 ·
cadera .83 · pecho 1.28 · hombro 1.42 · mentón 1.55 · coronilla 1.80. Torso y short con
`LatheGeometry` (perfil revolucionado con hombros, cintura y cadera), brazos y piernas con
cápsulas, trapecio que une cuello y hombros, cuello redondo y puños de la camiseta, pies
apuntando levemente hacia afuera. Cámara de retrato (FOV 24, lejos) para que no deforme.

**Sigue pendiente / recomendación**: para llegar exactamente al nivel de la referencia que
mandó el usuario haría falta un **modelo hecho por un modelador 3D** (archivo `.glb`) cargado
con `GLTFLoader` — se puede incrustar en base64 dentro del HTML igual que three.js. Todo lo
que se puede hacer generando geometría por código ya está bastante al límite.

---

**29 · El jugador 3D reconstruido de cero (el modelo estaba roto)**

El usuario mandó su captura: "tiene la cabeza en el piso". **Era literal.** En `armar3DPro`
la cabeza se creaba con `cab.position.y=HY` y después se llamaba **`add(cab)` sin coordenadas**,
y `add(m,x,y,z)` hace `m.position.set(x||0,y||0,z||0)` → **mandaba la cabeza a (0,0,0)**, o sea
al piso, entre los botines. Lección: `add()` pisa la posición; para respetarla hay que usar `put()`.

**Modelo reconstruido con canon anatómico** (objeto `Y` con todas las alturas):
suelo 0 · tobillo .13 · borde de la media .47 · rodilla .50 · short .70 · cadera .87 ·
cintura 1.055 · pecho 1.255 · hombro 1.345 · cuello 1.43 · mentón 1.452 · cabeza 1.572.

**Helpers nuevos**
- **`miembroCurvo3D(puntos,radios,mat,seg,achatarZ)`**: recorre una polilínea con radios
  variables y calcula un marco local por tangente. Con esto el brazo tiene bíceps y la pierna
  tiene pantorrilla; antes eran conos rectos. Genera UV (u alrededor, v a lo largo).
- **`peloCasco3D(HR,FF,mat,yFrente,yNuca,esc)`**: casco de pelo con **línea de nacimiento
  natural** (más alta en la frente, más baja en la nuca). Toma una esfera y **mete hacia adentro
  de la cabeza** los vértices por debajo del límite, así el borde queda continuo y sin costuras.
  Reemplazó al parche casquete+nuca que dejaba un corte recto en la sien.
- **`botin3D`**: bota con anillos (talón, empeine, puntera) + suela + taco.
- **`texPierna3D`**: la pierna entera en **una sola malla** con textura: piel arriba y media
  abajo con dos franjas. Antes la media era una pieza aparte y **desaparecía por z-fighting**.
  **OJO**: la textura necesita **`t.flipY=false`**, si no la media sale en el muslo (three
  voltea las texturas por defecto y `v=0` es la cadera).
- **`texShort3D`**: short con el **dorsal estampado**; el frente cae en u=0.25.
- `materialPro3D(...,plano)` con **`flatShading`** por defecto: da el look facetado low-poly.

**Iluminación**: se sacó `ACESFilmicToneMapping` y `physicallyCorrectLights` (lavaban los
colores del club: el rojo salía rosa). Ahora `NoToneMapping` con key 1.15, hemi .30, fill .26,
rim .72/.34 y sombra PCF suave. Cámara de retrato: FOV 26 a 4.32 m.

**El técnico**: la camisa, la corbata y las solapas estaban **dentro** del torso (z=.09 cuando
la superficie del pecho está en z≈.155). Ahora van en `ZP=.150` y se ven.

**Verificado** (`/tmp/final.html`, 9 pruebas): carrera, partido completo, plantel, tabla,
pantalla 3D del jugador, pantalla 3D del técnico, **72 combinaciones de corte×barba sin un solo
error**, las tres dificultades y una campaña completa de copa.

---

**30 · Animaciones de interfaz y verificación del servidor de Codex**

**EL SERVIDOR ONLINE (lo hizo Codex) FUNCIONA.** Se probó de punta a punta:
- `node server.js` levanta en :8080, sirve el juego entero desde `/`, `/salud` devuelve
  `{ok,salas,jugadores,ranking,arriba,pagos}` y `/api/ranking` el ranking de la comunidad
  (guardado en `ranking-comunidad.json`, con puntaje calculado por partidos, nivel, media y plata).
- **Prueba real de WebSocket con dos clientes** (`/tmp/testws.js` con el `ws` del propio servidor):
  `crear` → `sala_creada` con código de 4 letras, `unir` → `unido` + `rival_entro` al anfitrión,
  y pasan `config`, `estado`, `input`, `chat` y `dt`. **Los 8 mensajes del protocolo andan.**
  Ojo: el mensaje de respuesta es **`sala_creada`** (no `creada`) y el campo es **`code`** (no `cod`).

**ANIMACIONES (todo CSS + un poco de JS, sin librerías)**
- **Entrada de pantalla** con `pantIn` y **bloques escalonados** (`.screen.on>*` con delays por
  `nth-child`, de 20 a 350 ms).
- **Dirección de la transición**: `ir()` compara la posición del destino en `ORDEN_PANT` /
  `ORDEN_DT` y agrega `tabIzq` o `tabDer`, así al cambiar de pestaña la pantalla entra por el
  lado correcto, como en el FIFA.
- **Listas y tarjetas** entran una tras otra (`itemIn`, `tileIn`, `menuIn`).
- **Agenda**: los días entran de costado con el delay tomado de la variable `--orden` que ya
  traía cada uno (`calc(min(var(--orden),14) * 28ms)`), el próximo partido tiene un **barrido de
  luz**, el chip de HOY late, y el partido recién jugado se resalta (`_fechaRecien` + clase `recien`).
- **Números que cuentan**: `animarNumeros()` recorre los `[data-n]` y cuenta desde 0 con easing.
  **Importante**: el HTML trae el valor final escrito, así si el JS no corre igual se ve bien.
- **`ponerNum()`**: la plata y las gemas de la barra saltan en dorado cuando suben.
- **Marcador del partido**: `marcador()` detecta el cambio y dispara la clase `golazo`.
- Flechas `▶` animadas y **brillo que barre** en los botones de jugar (`.btnPulso`, `.flecha-anim`).
- Tipografía: más tracking en los `eyebrow`, `tabular-nums` en todos los números y mejor interlínea.
- **`@media (prefers-reduced-motion:reduce)`** desactiva todo para quien lo tenga configurado.

**Cómo fotografiar animaciones en headless**: el screenshot se toma antes de que terminen y
sale todo en blanco (las animaciones usan `both`, o sea que arrancan invisibles). La solución es
`document.getAnimations().forEach(a=>a.finish())` antes de la captura.

**Verificado** (10 pruebas): carrera, navegación por las 7 pestañas, números animados, partido
completo, marcador con animación de gol, modo DT, las dos pantallas 3D, copa y menú.

---

**31 · Convocatoria manual, penales jugables, entretiempo y planteo en vivo**

**BUG DEL PATRIMONIO (lo reportó el usuario: "está todo junto")**
La cabecera de la Oficina usaba `.row` con tres bloques y en pantalla angosta **"GEMAS" y
"PATRIMONIO" se pisaban**. Ahora es `.ofiCaja`, un grid de 3 columnas (1.45fr / 1fr / 1.15fr)
con `ellipsis` y tamaños que bajan en móvil.

**SELECCIÓN: quién juega para quién**
- **`SEL_REAL`**: tabla de jugadores que representan a un país distinto del de nacimiento.
  Arregla el caso que marcó el usuario: **Retegui ya no está en Argentina, está en Italia**.
  `natDeJugador(j)` es lo que usa `selPlantel` en vez de `natN(j.nat)`.
- **`SEL_HISTORICOS`**: Messi, Cristiano, Modrić, Neymar, etc. entran a la lista aunque la curva
  de edad les haya bajado la media (Messi tiene **69** con 39 años, por eso antes quedaba afuera).
  Si la lista está llena, se saca al peor que no sea histórico.

**CONVOCATORIA Y ONCE A MANO** (`R.convocatoria`, se entra desde la pantalla de Selección)
- Buscador por nombre o club, filtros por puesto, y la lista completa de compatriotas.
- Se marcan hasta 23; **los primeros 11 son el once titular**, con botones ↑ al once / ↓ banco.
- Se guarda en `G.selLista` + `G.selManual`. `selConvocados()` devuelve tu lista si la armaste,
  y **`fuerzaSel()` usa tu once**, así que elegir bien cambia el rendimiento del equipo.
- Botón para devolverle la lista al técnico.

**PENALES JUGABLES** (`tandaPenales(...)` + `R.penales`)
- Arco dibujado con red y **6 rincones**: pateás eligiendo uno y **atajás eligiendo para dónde
  te tirás**. El resultado depende de si coincidís con el arquero (misma zona = 25% de gol,
  mismo lado = 72%, lado cambiado = 93%) más un 10% de tiro afuera si va arriba.
- Marcador con bolitas verdes/rojas, 5 rondas y **muerte súbita**.
- Enganchado en **las tres copas** (`resultadoCH` con `porPenales`), en la **copa internacional
  del modo jugador** (`resolverInterJ`), en el **Mundial de Clubes** (`resolverMC`) y en las
  **llaves de la selección** (`resolverSel`). Antes todo eso se resolvía con `Math.random()`.

**ENTRETIEMPO Y GOL DE ORO** (motor físico)
- A la mitad del tiempo el partido se para solo y se abre el **entretiempo**: marcador, cómo vas,
  tarjetas y la elección de planteo para el segundo tiempo.
- En las llaves (`cfg.eliminatoria`), si terminan empatados hay **alargue de 20 segundos con gol
  de oro** (`P.golOro`): el primer gol define y se va derecho a la pantalla de festejo.
  Si nadie convierte, **penales**.

**PLANTEO EN VIVO** (lo pidió para el modo DT)
- Barra debajo de la cancha: **DEFENDER / PAREJO / ATACAR** (`setTactica`).
- Afecta de verdad a la IA de **tu** equipo (`P.miEq`): mueve la posición base ±11% del ancho de
  la cancha hacia el arco rival o hacia el propio, y cambia la presión del segundo hombre.
- Sale un cartel en la cancha al cambiarlo y también se puede elegir en el entretiempo.

**Verificado** (9 pruebas): carrera, Oficina/Patrimonio, convocatoria manual con Messi y Retegui,
tanda de penales completa (4-2), los tres planteos, entretiempo, alargue con gol de oro que
termina el partido, campaña de copa completa y menú.

---

**32 · Publicar el juego: por qué fallaba en Netlify y cómo quedó**

**EL PROBLEMA**: el juego dejó de ser un solo archivo. Ahora usa **24 imágenes .webp
(1,4 MB) en `assets/menu/`** (las bajó Codex) referenciadas como rutas relativas en
`TILE_FOTOS` y `MAIL_FOTOS`. Al subir **sólo `ladiez.html`** a Netlify, esas rutas
apuntan a la nada y las placas del menú y los correos salen vacíos.

**LO QUE SE ARMÓ**

1. **`ladiez-web/`** — carpeta lista para arrastrar a Netlify:
   - `index.html` (copia de `ladiez.html`), `assets/menu/` con las 24 fotos
   - **`netlify.toml`**: redirect SPA (`/* → /index.html` 200) y caché
   - **`_headers`**: `assets/*` con caché de un año (immutable) y **`index.html` con
     `max-age=0, must-revalidate`** → esto arregla el "subo una versión nueva y sigo
     viendo la vieja", que era caché del navegador.
   - `LEEME-SUBIR.md` con el paso a paso, incluido lo del dominio.
2. **`ladiez-un-archivo.html`** (6,7 MB) — el juego con **las 21 imágenes incrustadas en
   base64**. No depende de nada: se puede mandar por WhatsApp, abrir sin internet o subir
   suelto a cualquier hosting.

**Verificado**: servido con `python3 -m http.server`, el index responde 200 y **las 24
imágenes responden 200**; el menú se ve completo desde `http://` igual que desde `file://`.

**Sobre el dominio**: Netlify da gratis `algo.netlify.app` y el nombre se cambia en
*Site configuration → Change site name*. Un dominio propio hay que comprarlo aparte
(nic.ar para `.com.ar`, o Namecheap/Porkbun para `.com`/`.app`) y después conectarlo en
*Domain management → Add a domain*.

**Para el futuro**: si se agregan más imágenes, hay que **regenerar las dos salidas**.
El script que incrusta está en el historial: busca `assets/menu/*.webp` en el HTML,
lee cada archivo y reemplaza la ruta por `data:image/webp;base64,...` entre comillas
simples, dobles y paréntesis.

---

## Qué es

Juego de fútbol web, **un solo archivo HTML** que funciona sin internet.
Está en `/home/matiigonzz/Claude/ladiez.html` (~2,5 MB).
Hablo en español rioplatense (vos, no tú).

Hay además una carpeta `/home/matiigonzz/Claude/ladiez-servidor/` con el servidor
online (Node + WebSocket) y el módulo de cobros de Mercado Pago.

---

## Estado actual (lo que YA está hecho y funcionando)

### Datos reales
- **33 ligas** de 20 países, agrupadas en América (12 primeras + 5 segundas) y Europa (8 + 8)
- **614 clubes**, todos con plantel real
- **~16.500 jugadores reales** con nombre, edad real, puesto y nacionalidad
- **608 escudos oficiales** incrustados en base64 WebP
- **19 logos de liga propios**; el resto usa la bandera del país
- **542 técnicos reales** por club

**Países cubiertos**: Argentina (1ª y 2ª), Brasil (1ª y 2ª), Uruguay (1ª y 2ª),
Colombia (1ª y 2ª), México (1ª y 2ª), Estados Unidos, **Paraguay**, **Perú**,
**Bolivia**, **Ecuador**, **Venezuela**, **Chile**, España (1ª y 2ª),
Inglaterra (1ª y 2ª), Italia (1ª y 2ª), Alemania (1ª y 2ª), Francia (1ª y 2ª),
Portugal (1ª y 2ª), Países Bajos (1ª y 2ª), Turquía (1ª y 2ª).

Clubes grandes verificados presentes: Olimpia, Cerro Porteño, Alianza Lima,
Barcelona SC, Colo-Colo, Bolívar, Caracas, Paris Saint-Germain, Boca, River, etc.

**De dónde salieron los datos** (por si hay que actualizarlos):
- Planteles: Wikipedia en inglés, plantilla `{{fs player}}` del artículo de cada club.
  Se piden 20 artículos por request con `action=query&prop=revisions&rvprop=content`.
- Listas de clubes por liga: artículo de temporada (ej. "2026 Primera Nacional"),
  extrayendo `name_XXX=` de la plantilla Sports table.
- Edad y notoriedad: Wikidata por SPARQL (POST, lotes de 700 nombres).
  Wikidata limita a **1 consulta por minuto**, hay que ir por lotes grandes.
- Escudos y técnicos: TheSportsDB API gratuita (clave "3") + infobox de Wikipedia.
- **Las medias las calculo yo** con un modelo de percentiles sobre la cantidad de
  idiomas en que cada jugador tiene artículo de Wikipedia, corregido por edad y club.
  No existe fuente pública de medias tipo FIFA.

### Modos de juego
1. **Carrera Jugador** — creás futbolista, elegís liga y club, temporadas, minijuegos,
   agenda, técnico, prensa, copas internacionales, mercado de pases, retiro
2. **Carrera DT** — te contrata un club, presupuesto, fichajes con negociación,
   formación y titulares, lesiones, cansancio, sala de prensa, redes sociales,
   Libertadores/Champions, ascensos y descensos
3. **Partido rápido** — 11v11 físico tipo Haxball, a 5 goles, local o vs CPU
4. **Desafíos** — 11 juegos de conocimiento (Impostor, Grilla, Conexiones, Mentiroso,
   Tasador, Presupuesto, El once del club, etc.) + duelo online 1v1
5. **Online** — salas con código, por PeerJS (directo) o por servidor propio

### Lo último que se agregó (última sesión)
- **La energía ya NO bloquea los partidos**, solo sirve para entrenar. Se recarga
  cada 3 minutos. Esto era importante: bloqueaba el juego.
- **Idolatría por club**: 5 niveles (Uno más → Querido → Referente → Ídolo → Leyenda).
  Sube con goles, asistencias, victorias, títulos y **temporadas en el mismo club**
  (cada año vale más). **Si te vas del club, vuelve a cero.** La estatua solo se gana
  con lealtad.
- **Prensa del jugador**: preguntas post-partido con tres tonos de respuesta
  (humilde / firme / arrogante), cada uno con efectos distintos en DT, fama e idolatría.
- **Objetivos del técnico por temporada** según tu puesto, con panel de progreso en
  el hub y evaluación al cierre.
- **Eventos grises** (11): el suplemento dudoso que puede dar antidoping positivo,
  el tipo que te ofrece plata por jugar mal, el abuelo de otra nacionalidad, la
  investigación fiscal, el juvenil que te compite el puesto, el tatuaje, el tío en
  redes, los estudios, infiltrarse para la final, el superequipo, la bronca de la
  tribuna. Varios tienen riesgo real de castigo (suspensión de fechas).
- **Logros** (16): estatua, Balón de Oro, 300 goles, De Ushuaia al Darién, bandera
  de un club, retirarse sin títulos, Pibe Maravilla (1 en 1000 carreras), etc.
- **Ligas agrupadas por región** en los selectores.
- **PSG arreglado** (estaba como "Paris SG").
- **6 ligas americanas nuevas**: Paraguay, Perú, Bolivia, Ecuador, Venezuela, Chile.
- **Ligas agrupadas por región** en el selector de carrera y en el de DT.
- **Hub del modo jugador rediseñado estilo FIFA**: cabecera azul con escudo, nombre y
  media grande; pestañas CENTRAL / PLANTILLA / AGENDA / TEMPORADA / OFICINA; panel
  "CONTINUAR" con calendario de la semana; tarjetas de entrenador, entrenamiento,
  tabla y estadísticas de la temporada.
- **Bug del selector primera/segunda arreglado**: al cambiar de división ahora
  se selecciona automáticamente una liga de esa división (antes quedaba la anterior
  y mostraba los clubes equivocados).
- **Escudo de cada club** en la lista de selección.

---


### Lo que se agregó en la sesión del 6/8 (4 bloques)

**1 · Selección nacional y torneos internacionales**
- 93 selecciones con confederación y bandera. La convocatoria se arma con
  **jugadores reales**: se filtra el índice por nacionalidad y se ordena por media
  (Argentina te da Julián Álvarez, Lautaro, Enzo Fernández; Brasil, Vinícius y Raphinha).
- **Nacionalidad separada de la liga**: se elige en la creación del jugador, agrupada
  por confederación. Define qué selección podés representar.
- Entrás en la lista según tu media comparada con los mejores de tu país **en tu puesto**
  (`CUPOS` por grupo: POR 1/3, DEF 4/8, MED 3/7, DEL 3/7). Si no entrás, te dice
  cuántos puntos de media te faltan.
- Calendario real por año: `año%4===2` Mundial (2026, 2030, 2034), `%4===0` torneo
  continental (Copa América / Eurocopa / Copa Oro / CAN / Copa Asiática),
  `%4===3` Eliminatorias, `%4===1` **Finalissima** solo si ganaste la continental el
  año anterior y sos de Conmebol o UEFA.
- El torneo se juega **al cerrar la temporada**, antes del mercado de pases. Fase de
  grupos con puntos + llaves con penales. Se puede jugar con minijuegos o simular.
- **Mundial de Clubes**: si ganás la Libertadores/Champions, la temporada siguiente
  aparece una tarjeta en el hub con cuartos, semi y final.
- Pestaña **SELECCIÓN** nueva en el hub, con la lista de 23, tu estado, el camino en
  el torneo y la vitrina. 4 logros nuevos.

**2 · Economía y tienda rehechas**
- Se sacaron los packs de gemas falsos, las ofertas relámpago con reloj y el
  Pase Leyenda pago. El pase ahora es **gratis** ("Camino a la leyenda") y da gemas al jugar.
- Sueldo **por fecha** con curva coherente: `sueldoDe(r,fama)=1.075^(r-55)*900+fama*25`
  (≈1.900 en un club chico, ≈14.000 en un grande). Se cobra en cada partido.
- **Staff propio** (5 roles × 3 niveles) con costo de contratación **y sueldo por
  temporada**: nutricionista (−40% desgaste), kinesiólogo (sanciones más cortas),
  psicólogo (−45% caída de moral), preparador (retrasa el declive hasta 3 años),
  representante (+26% de sueldo y más ofertas). **Si no podés pagarles, se van todos.**
- **Patrimonio** (8 items, de 30.000 a 1.050.000): depto, auto, casa, cancha de fútbol 5,
  restaurante, quinta, escuelita, mansión. Algunos dejan renta anual. Sale en el retiro.
- Oficina con 4 secciones: Finanzas (balance real de la temporada), Mi gente, Patrimonio, Tienda.
- Entrenar ahora cuesta `280+media*22` en vez de 350 fijos.

**3 · Minijuegos nuevos, sin un solo emoji**
- Motor propio en **canvas** (`mgUI`, `mgLoop`, `mgTap`, `mgFin`) con dibujo de cancha,
  arco con red, jugadores y pelota. Cero emojis, todo SVG y canvas.
- 12 juegos: **punteria** (6 zonas del arco, ángulos ×1.5, arquero que se mueve),
  **tiroLibreC** (mira en movimiento, barrera y efecto), **unoVuno** (el arquero achica,
  timing + colocación), **cabezaN** (salto sobre la trayectoria del centro),
  **controlG** (aguja rotatoria, 3 rondas, rival que te cierra), **lectura** (encontrar
  al compañero libre en 3 segundos), **pasePres** (meterla en el pasillo entre centrales),
  **anticipo** (leer el amague y salir a cruzarlo), **atajadaZ** (leer el perfil del
  pateador y volar), **salidaP** (ventana de achique), **saqueP** (potencia del saque
  largo), **reflejoP** (dos tapadas seguidas).
- `MGPOS` y `STAT_MG` repuntados a los nuevos. Los viejos quedan como red de seguridad.

**4 · Modo DT: agenda, ojeadores y curvas ocultas**
- **Agenda** con fechas reales agrupadas por mes, escudo del rival, local/visitante,
  resultados y clásicos marcados. Tira de la semana en el hub, igual que el jugador.
- **Dos ojeadores**: Rubén Ortiz (±3, tarda 5 fechas) y Fede Sosa (±7, tarda 2).
  Los mandás a una liga con una franja de edad; vuelven con 4 informes que dan un
  **rango de media, nunca el número exacto**. Al fichar se revela la media real.
- **Curvas de crecimiento ocultas**: cada jugador tiene edad de pico (24-32), velocidad
  de declive y techo, derivados del hash de su nombre. No se ven. Lo único visible es
  la columna **Evol** (▲/▼) con lo que cambió en la última pretemporada.
- Cada pretemporada **suben 1 o 2 pibes de inferiores** con su curva propia: ahí está
  el pibe que explota.
- Se arregló el cupo del plantel: estaba en 28 cuando los planteles reales traen 29+,
  así que **el mercado no dejaba fichar a nadie**. Ahora es 34.


**5 · Menú principal nuevo, estilo consola (FIFA 19)**
- Barra superior con la marca, el nombre del jugador guardado, las monedas y el sonido.
- **Cuatro pestañas**: INICIO / JUGAR / ONLINE / AJUSTES (`MTAB`, se cambia con `mtab()`).
- Grilla de **placas** con `grid-template-areas`. En PC: 4 columnas × 2 filas
  (`"a b c d" / "e e f g"`), igual que la referencia. En móvil pasa a 2 columnas
  (`"a a" "b b" "c d" "e e" "f g"`) con placas más bajas y textos cortos.
- Cada placa acepta un texto largo y uno corto (`ds` y `dsm`): en móvil usa el corto.
- Placas de JUGAR: Carrera de jugador (hero, con tres cartitas), Carrera de DT
  (con un pizarrón SVG 4-3-3), **Continuar carrera** (lee el guardado sin cargarlo:
  escudo del club, media, próximo rival), **Continuar DT** (escudo, posición en la
  tabla, títulos), Partido rápido (ancha, con los dos escudos de `MC`), Desafíos y Online.
- `ojearGuardado()` lee los dos localStorage sin tocar `G` ni `D`. `ovrDe(pos,st)`
  calcula la media de un guardado sin cargarlo.
- En el menú, `#app` pasa a `max-width:1180px` (clase `ancho`) y el `body` toma la clase
  `en-menu`, que **aclara `#bgfx`** para que se vea la hinchada y el césped del fondo.
- AJUSTES reemplaza a los botoncitos viejos: dispositivo móvil/PC, orientación, sonido,
  borrar partidas guardadas, ayuda y "sobre el juego".
- Barra de pie con ligas, clubes y el modo actual (se toca para ir a Ajustes).


**6 · Modo Champions**
- `UCL`: los **36 equipos reales** de la Copa de Europa, resueltos contra los datos con
  `uclEq()`. Ojo con los nombres exactos: en los datos son *Athletic Bilbao*, *Inter Milan*,
  *Roma*, *Bayern Munich*, *Monaco*, *Porto*, *PSV Eindhoven* (no *Athletic Club*, *Inter*,
  *AS Roma*, *Bayern München*, *Mónaco*, *FC Porto*, *PSV*).
- **Formato nuevo de la UEFA**: fase de liga de 8 partidos con los 36 en una sola tabla.
  Del 1 al 8 van derecho a octavos, del 9 al 24 juegan un playoff sembrado (9º vs 24º,
  10º vs 23º…), del 25 para abajo quedan afuera. Después octavos, cuartos, semi y final.
- Cada jornada se simulan los otros 17 partidos (`restoJornadaCH`). Los partidos tuyos se
  juegan con el **motor físico 11v11** (`iniciarFisico`) o se simulan.
- El sorteo está **sembrado**: en octavos los ocho primeros cruzan con los que vienen del
  playoff. `CH.eliminados` evita que te toque dos veces el mismo rival (era un bug).
- Balance medido sobre 40 campañas por equipo: City 12%, Arsenal 15%, Real Madrid 18%,
  Ajax casi nunca, Galatasaray queda afuera en fase de liga 36 de 40 veces.
- Se guarda en `ladiez_ch_v1` y las copas ganadas se acumulan en `ladiez_ch_pal`.
- Pantallas: `chInicio` (elegir equipo por liga), `chHub`, `chTabla`.

**7 · Los dos hubs rehechos estilo FIFA 19**
- Clases nuevas `.hgrid` / `.htile`: placas grandes en azul de carrera, 3 columnas en PC
  y 2 en móvil, con variantes `oroh`, `verd`, `roja`, `uclh` y `ancha` (ocupa dos columnas).
- **Hub del jugador**: las tarjetitas chicas se reemplazaron por 6 placas —
  Entrenamiento, Tu entrenador, Tablas (con mini tabla), Oficina (caja y patrimonio),
  Tu temporada y Selección. El Mundial de Clubes y el parte médico aparecen como placas
  cuando corresponde.
- **Hub del DT**: ahora tiene cabecera propia (`cabeceraDT()`, escudo + liga + media +
  caja + puesto) y **pestañas** (`dtTabs()`: CENTRAL / PLANTEL / FICHAJES / OJEO / AGENDA /
  TABLA) que se repiten en todas las pantallas del modo. Los botones sueltos pasaron a ser
  6 placas con datos en vivo.
- En el menú, la placa que decía "banco de suplentes" se reemplazó por **MODO CHAMPIONS**
  (justo donde el FIFA pone la de la UCL) y el continuar del DT se integró en la placa
  "Carrera de DT".


**8 · Tres modos de copa con carrusel, datos completos y tutorial**
- `MODOS_COPA`: **Champions** (36 clubes, fase de liga), **Libertadores** (32 clubes,
  grupo de 4 ida y vuelta) y **Mundial** (32 selecciones armadas desde `SELE`, grupo de 3).
  Todo comparte el mismo motor (`nuevoCH(modo,k)`, `resultadoCH`, `sortearRivalCH`).
  `copaEq(m)` cachea los participantes; `chEsc(e,t)` dibuja escudo o bandera.
- El motor físico ahora acepta `cfg.A.obj` para equipos que no salen de una liga (selecciones).
- **Carrusel** en la placa `d` del menú: rota solo cada 5,2 s, tiene puntitos clicables,
  se desliza con el dedo (`touchstart/move/end`) y con trackpad (`wheel` horizontal).
  Se arma en `carruselCopas()` y se anima en `R.menu_after`.
- **Tutorial de minijuegos**: `MG_INFO` con los 12 explicados (qué hay que hacer + truco).
  La primera vez que te toca cada uno aparece la explicación, y después siempre va una
  **cuenta atrás 3-2-1-¡YA!**. Lo visto se guarda en `ladiez_mg_vistos`.
  Pantalla nueva `R.comoJuego` con los 12 agrupados por puesto, accesible desde Ajustes.

**Datos completados en esta sesión**
- **614 de 614 escudos (100%)**: se bajaron los 6 que faltaban (Atlético de Madrid,
  Nottingham Forest, The Strongest, Unión Española, Ñublense, Deportes Iquique).
- **31 de 33 logos de liga**: se bajaron 9 (Paraguay, Uruguay 2ª, Colombia 2ª, México 2ª,
  España 2ª, Portugal 2ª, Ecuador, Venezuela, Perú). Faltan **Bolivia y Chile**.
- Fuentes que funcionaron: TheSportsDB `searchteams.php` para escudos de club y
  **Wikipedia `prop=pageimages&piprop=original`** (es y en) para los logos de liga.
  Ojo: `all_leagues.php` de TheSportsDB ahora devuelve solo 5 ligas con la clave gratuita.
- El **PSG sí estaba** todo el tiempo (fra1, índice 14, con plantel y Luis Enrique).
  Lo que falla es buscar "PSG" en el buscador del mercado, que compara contra el nombre
  completo. Falta agregar alias de búsqueda.


**9 · Liga árabe, escudos corregidos y once inicial**
- **Saudi Pro League** (`ksa1`, zona nueva `ASI`): 18 clubes, **602 jugadores reales**
  bajados de la Wikipedia en inglés con la plantilla `{{fs player}}`. Cristiano Ronaldo
  queda en 93, Benzema 91, Darwin Núñez y Théo Hernandez 92. Fuerzas: Al-Hilal 89,
  Al-Nassr 88, Al-Ahli y Al-Ittihad 85.
  - Las **medias** salen de una curva logarítmica sobre la cantidad de idiomas en que el
    jugador tiene artículo (`prop=langlinks`), corregida por edad y por club.
  - Las **edades y nacionalidades** salen de Wikidata (`wbgetentities`, P569 y P27).
  - **Ojo con el parser**: `re.split('|')` rompe los enlaces `[[A|B]]`. Hay que proteger
    las barras dentro de `[[...]]` y `{{...}}` antes de partir por `|`.
  - Al agregar una zona nueva hay que agregarla también a `REGIONES`, `ligasPorRegion`,
    `DIV1`, `COPAS`, `ECO`, `NAT_LIGA` y sobre todo a **`NOM`** (nombres y apellidos para
    generar juveniles): si falta `NOM[zona]`, `plantel()` explota con "arr is undefined".

**Bugs encontrados y arreglados**
- **El escudo del PSG era el del Torcy**, un club amateur francés: TheSportsDB devolvió el
  equipo equivocado en la búsqueda difusa. Se reemplazó por el de Wikipedia. Lección: al
  bajar escudos hay que **verificar el nombre que devuelve la API**, no confiar en el primero.
  Se auditaron visualmente los 60 clubes más fuertes generando un montaje con `magick montage`.
- **La cancha del plantel del modo jugador nunca funcionó**: faltaba por completo el CSS de
  `#pitch` y `.ppos`, así que los once jugadores caían apilados debajo del campo.
- El escudo de Al-Ittihad no existe en ninguna fuente libre (queda el dibujado).
- Los logos de liga de **Bolivia y Chile** no están en Wikipedia ni en TheSportsDB.

**Plantilla del modo jugador rehecha**
- El once respeta `esTitular()`: si el técnico te pone, tu puesto es tuyo. Si tu posición no
  está en el 4-3-3, entrás por el más flojo de tu grupo.
- Debajo de la cancha: cartel de si jugás o no, **banco de 7 suplentes** y el resto del plantel.


**10 · Camisetas por equipo en el motor físico**
- Antes todos los jugadores eran un círculo de color plano con las mismas rayas genéricas.
  Ahora cada club tiene su **camiseta**: `KITS` con **150 clubes hechos a mano**
  (`patrón|color de fondo|color del detalle`) y el resto se genera del hash del nombre
  más el color del club, así queda estable partido a partido.
- Patrones: `lisa`, `vert` (rayas verticales), `horiz`, `bandaH`, `bandaV`, `bandaD`
  (diagonal), `diagM` (media diagonal, para el Monaco), `mitades`, `mangas`.
  Se dibujan con `dibKit(c,x,y,r,kit)` recortando sobre el círculo del jugador.
- `kitsPartido(A,B,la,lb)` compara la luminosidad de las dos camisetas y, si se parecen
  demasiado, le pone la **suplente** al visitante.
- El **arquero** usa `kitPortero()`: elige entre cuatro colores el que más contraste con
  la camiseta de su propio equipo.
- Cuidado con los **nombres repetidos entre ligas**: hay dos "Barcelona" (esp1 y ecu1),
  dos "Nacional" (uru1 y par1) y dos "Everton" (eng1 y chi1). `KITS` acepta la clave
  `liga|club` además del nombre suelto, y `kitDe(club,lid)` la prioriza.


**11 · Medias calibradas por edad y camisetas de selección**
- **Las medias no penalizaban la edad**: Cristiano tenía 93 con 41 años y Benzema 91 con 39,
  porque el modelo se basa en la notoriedad (idiomas en Wikipedia) y ellos son los más
  famosos del mundo. Se aplicó una **curva de edad** a los datos de los 17.000 jugadores:
  penalización de -1 a los 33 hasta -10 a los 41+, más un **tope duro** por edad
  (34→90, 36→88, 38→85, 40→83, 41+→82). Cambiaron 2.246 jugadores.
  Cristiano quedó en 82 y Benzema en 83, en línea con el FIFA. Los menores de 33 no se tocaron.
- **No se pueden traer las medias oficiales del FIFA/EA FC**: SoFIFA devuelve 403 a cualquier
  acceso automático, no hay API oficial de EA y los datasets públicos de GitHub son de
  FIFA 23 o anteriores (desactualizados respecto a los planteles 2025/26).
- Las **selecciones salían todas de verde** porque `chJugar()` tenía el color hardcodeado.
  Ahora hay `KITS_SEL` con las camisetas de 60 selecciones (Argentina a rayas celestes,
  Países Bajos naranja, Croacia a cuadros rojos) y `kitSel(nat)` para el resto.
- Las camisetas generadas ya no salen lisas: `PATS` no incluye `'lisa'`, así que todo club
  sin camiseta cargada a mano igual tiene rayas, banda o mangas.
- **Logo de la liga de Bolivia** agregado (`File:Ligabolivia.png` de Commons).
  Siguen sin logo **Chile** (el de "Liga de Primera itaú" no está en ninguna fuente libre)
  y la **Saudi Pro League**.


**12 · Ronda de bugs y balance reportados por el usuario**
- **La jugada que salía bien no terminaba en gol.** `resolver()` calculaba
  `eff=(score*.62+st*.34+...)*rendimientoBase()`, o sea que el multiplicador de fatiga
  aplastaba todo y la media del jugador pesaba casi igual que la ejecución. Con puntaje 80
  el minijuego decía "GOLAZO DE TIRO LIBRE" y el partido daba **asistencia el 81% de las veces**.
  Ahora `eff=score*.86+(st-62)*.40+...-desgaste`, con el desgaste **restando** en vez de
  multiplicar. Puntaje 92+ es gol prácticamente seguro y la media sigue importando sin anular.
- Además los textos de los minijuegos ya **no prometen el resultado**: describen la ejecución
  ("LE PEGASTE PERFECTO") y el resultado lo narra el partido con `GOL_TXT`/`ASI_TXT`,
  que tienen una frase distinta por cada jugada.
- **Simular una fecha de copa internacional la salteaba**: `simularFecha()` no miraba
  `fx.inter`, así que jugaba un partido de liga y se perdía la ronda de la Libertadores
  sin avisar. Ahora simula la copa. `simularHasta()` frena antes de una fecha internacional.
- **La agenda ponía un cartel genérico "INTERNACIONAL"** y el escudo del rival de liga
  (que no es el rival real, porque se sortea al entrar). Ahora muestra el nombre de la copa,
  la ronda y avisa "rival por sortear". El botón del hub dice "JUGAR LA COPA LIBERTADORES".
- **Ser leyenda era demasiado fácil** (3 temporadas). Los umbrales pasaron de
  0/120/340/700/1300 a **0/340/1100/2600/5200**, los goles sueltos pesan menos, la lealtad
  pesa mucho más (`90+temps^1.55*55`) y además hay un **mínimo de temporadas en el club**
  por escalón (`IDOL_ANIOS=[0,1,3,5,8]`). Medido: se llega a Leyenda en la **temporada 8**.
- **La confianza del técnico se ganaba sola** (+5 por partido decente, de 55 a 100 en nueve
  partidos). Ahora sube de a 2-3 solo con partidos muy buenos, baja rápido con los malos,
  y tiene piso 18 para que la carrera no se trabe.
- **Sobraba plata en los clubes grandes.** Se agregaron **impuestos progresivos**
  (8% hasta 90k, 38% arriba de 700k) y **mantenimiento del patrimonio** (6% anual),
  que se cobran al empezar cada temporada. Al que juega en un club chico casi no le pega;
  al que gana millones le saca un tercio. Se ve todo en la pestaña Finanzas.

**13 · Online: por qué no conectaba**
- El broker de PeerJS estaba bien (200 OK). El problema era que la config de ICE tenía
  **solo servidores STUN**. En wifi alcanza, pero **en datos móviles el operador usa NAT
  simétrico** y hace falta un **TURN** que haga de intermediario. Sin eso no conecta nunca.
- Se agregaron 4 TURN de OpenRelay (`openrelay.metered.ca`, puertos 80/443/tcp/tls) más los
  3 STUN. También `BROKERS`, una lista de porteros alternativos, y `nuevoPeer()` que
  **reintenta solo** con el siguiente si uno no abre en 7 segundos.
- Tanto crear como entrar a una sala muestran ahora el error concreto y un botón de reintentar.


**14 · Buscador, selecciones en modo DT y online rehecho**
- **Buscador tipo Copero** (`abrirBuscador(cfg)`): modal con lupa, filtrado en vivo,
  chips por región y lista con escudo, liga y media. Reemplaza las listas gigantes.
  Se usa en la creación de carrera, en `dtInicio` y al elegir equipo de copa.
  - `itemsClubes()` indexa los 632 clubes, `itemsSelecciones()` las 93 selecciones.
  - **`APODOS_CLUB` y `APODOS_SEL`**: la gente busca "psg", "barca", "juve", "xeneize",
    "cr7", "chivas", "la roja". Sin esto, buscar "PSG" no devolvía nada (bug que reportó
    el usuario dos veces). Los apodos se suman al campo `tags` que mira el filtro.
  - Ojo: el input **no se vuelve a dibujar** al escribir (`pintarLista()` solo actualiza
    la lista), si no se pierde el foco en cada tecla.
- **DT puede dirigir selecciones**: botón en `dtInicio` que abre el buscador de las 93
  selecciones y arranca el Modo Mundial con esa selección.
- **Online rehecho de cero**. Antes tenía dos caminos (P2P directo y "servidor propio")
  y era confuso. Ahora:
  - Un solo botón: **CREAR LA SALA Y COMPARTIR**.
  - **Enlace de invitación**: `linkSala(cod)` arma `...#sala=ABCD`; `verSalaEnURL()` corre
    al abrir el juego, detecta el hash y **entra solo** sin escribir el código.
    `compartirCodigo()` usa `navigator.share` y cae a copiar al portapapeles.
  - **`probarConexion()`**: diagnóstico que le dice al jugador qué falla en SU dispositivo
    (internet, servicio de salas, soporte del navegador y si la red deja pasar la conexión).
    El último paso mira los candidatos ICE: si aparece `typ relay` funciona con datos
    móviles, si solo hay `srflx` funciona por wifi, si no hay nada la red lo bloquea.
- **Logos de liga: 34 de 34.** Se bajó el de la Saudi Pro League de Commons y, como el de
  la "Liga de Primera itaú" de Chile no existe en ninguna fuente libre, se **generó uno
  propio en SVG** con el estilo del real (escudo blanco, borde azul marino, figura naranja).

**Nota sobre probar WebRTC**: no se puede testear end-to-end en este entorno. Firefox
headless se cierra al tomar la captura y el sandbox le bloquea el acceso a `localhost`,
así que un servidor de logs local tampoco sirve. Lo verificable es la configuración
(broker responde 200, ICE con TURN); la prueba real la tiene que hacer el usuario.


**15 · Ranuras de carrera, desplegable, animación y liga belga**
- **Varias carreras a la vez** (`NRAN=4` de jugador y 4 de DT). Las claves son
  `ladiez_v1`, `ladiez_v1_1`, `ladiez_v1_2`… (la ranura 0 mantiene la clave vieja para no
  romper las partidas que ya existían). `SLOT_J`/`SLOT_D` guardan cuál está en uso en
  `ladiez_slotJ`/`ladiez_slotD`. `guardar()`, `cargar()`, `guardarDT()`, `cargarDT()` y el
  retiro usan `keyJ(SLOT_J)`/`keyD(SLOT_D)`. `panelRanuras(tipo)` dibuja la lista con
  escudo, media, temporada y títulos, más un botón de borrar por ranura.
- **Se fueron todos los `confirm()` del navegador.** Ahora hay `confirmar({tit,txt,detalle,
  si,no,peligro,ok})`, un modal con la cara del juego, ícono rojo y botón de peligro.
  Se borraron también `menuCarreraViejo`/`menuDTViejo`, que eran código muerto con `confirm()`.
- **Desplegable** (`regDesp(id,cfg)` + `despAbrir/despLista/despElegir`): un cuadro con
  flecha que se abre **hacia abajo**, con lupa, chips por región y lista con scroll.
  Reemplaza las listas larguísimas de ligas en la creación de carrera y en `dtInicio`.
  Es distinto del buscador modal: este es inline, como pidió el usuario.
- **Animación del carrusel**: al pasar de copa, la placa entra con `copaEntra`
  (escala + brillo), el título con `copaTT` y el pie con `copaPie`, más un `destello`
  que barre en diagonal. `pintarCarru(anim)` acepta `false` para el primer dibujado.
- **Liga belga** (`bel1`, Jupiler Pro League): 16 clubes, **478 jugadores reales**,
  16 técnicos (Ivan Leko en Brujas) y 13 escudos. **Las fuerzas se pusieron a mano**
  porque el artículo del Anderlecht tiene el plantel en otro formato y solo se parsearon
  2 jugadores, lo que daba fuerzas absurdas. Total: **35 ligas, 648 clubes**.
- **Aviso de `file://` en el diagnóstico del online**: si el juego se abre como archivo
  suelto, el navegador **bloquea WebRTC por seguridad**. Probablemente sea la causa real
  de que el usuario nunca pueda conectar. El diagnóstico ahora lo detecta y lo explica.


**16 · Desplegables de liga y país, ranking mundial y ciclo mundialista**
- **Un solo desplegable con las 35 ligas**, en vez de los chips "Primera/Segunda" que
  confundían. Cada liga aparece con **su nombre real** (LaLiga Hypermotion, Primera
  Nacional, EFL Championship) y el subtítulo aclara *país · categoría · cantidad de clubes*.
  `paisDeLiga(id)` traduce el prefijo del id al país. Filtros por categoría y por región.
- **La nacionalidad también es desplegable**: antes eran 93 chips apilados, ahora es un
  cuadro con lupa (`itemsPaises()`, ordenado alfabéticamente).
- **Ranking mundial de selecciones** (`R.ranking`, guardado en `ladiez_ranking`):
  - Los puntos de arranque salen de `fuerzaSel()` con una curva (`rankBase`), así que el
    orden inicial es realista (Francia, Argentina, Brasil, España…).
  - `rankResultado(a,b,ga,gb,peso)` usa un **Elo**: la expectativa sale de la diferencia de
    puntos, el K varía según la diferencia de goles y la importancia del partido.
    Ganarle a uno de arriba te hace subir mucho; perder con uno de abajo te hunde.
  - Se engancha en `resolverSel()` (torneos de la carrera) y en `resultadoCH()` cuando la
    copa es de selecciones. `fotoRank()` guarda las posiciones para mostrar flechas ▲▼.
  - Se entra desde la pantalla de Selección, desde el Modo Mundial y desde Ajustes.
- **Ciclo mundialista** en la pantalla de Selección: una línea de tiempo de 4 años que
  muestra qué se juega cada temporada y cuánto falta para el Mundial, con el año actual
  resaltado en verde y el del Mundial en dorado.
- **Cancha de posiciones rehecha**: clases `.canchaPos` y `.posBtn` con césped en franjas,
  áreas, semicírculos, córners y redes dibujadas en SVG; el puesto elegido late con un
  pulso. Antes eran estilos sueltos escritos a mano en el HTML.


**17 · Personalización, vida afuera de la cancha y vestuario**
- **Personalizar** (`R.personalizar`, guardado en `ladiez_pref`):
  - **7 temas de color** (`TEMAS`) que reescriben `--ac`, `--ac2`, `--oro` y `--cesped`
    con `documentElement.style.setProperty`, así cambia todo el juego de una.
  - **4 fondos** (`FONDOS`): estadio animado, estadio quieto, liso y césped.
    Se aplican con clases en el `body` (`fondo-quieto`, `fondo-liso`, `fondo-cancha`).
  - **Rostro del jugador** dibujado en SVG por código (`dibujarCara(c,tam)`): piel, corte
    (6 opciones), color de pelo, barba y ojos. Se guarda en `G.cara` y aparece en la
    cabecera del hub, donde se toca para editarlo.
- **Tarjetas**: `tarjetaEnPartido()` corre tanto en `resolver()` (partido jugado) como en
  `simularUno()` (simulado). La probabilidad depende del puesto (defensor 19%, delantero 9%),
  sube en clásicos, con moral baja y con desgaste. A la quinta amarilla te suspenden;
  una de cada siete amarillas es roja directa. Medido: 13 amarillas y 2 rojas en 3 temporadas.
- **Penales**: `hayPenal()` te da la chance según el puesto (16% de las jugadas para un
  delantero). `tirarPenal()` abre cinco opciones de dónde ponerla, incluida la vaselina,
  que solo sale bien si el arquero se tira.
- **Préstamos**: `evaluarPrestamo()` se dispara si sos juvenil y no jugás, o si el técnico
  no te quiere (`G.dt<32`). Te ofrece **tres destinos** más flojos que tu club; al terminar
  la temporada `volverDePrestamo()` te devuelve, y si rendiste bien el técnico te mira distinto.
- **Eventos de vida** (`EV_VIDA`, 8 eventos): Josefina, el auto 0km, la casa de la vieja,
  el cumpleaños del amigo, el tatuaje, el representante trucho, el picadito en el potrero
  y el negocio del primo. Varios tienen **riesgo real** (fotos a las cinco de la mañana,
  multa del club, perder la plata) y otros dan idolatría o moral. Se disparan al simular fecha.
- **Cartas del vestuario en modo DT** (`R.dtCartas`): los suplentes mandan mensajes
  ("Míster, quiero jugar"), y si los ignorás tres veces piden irse. Se responde prometiendo
  titularidad (queda anotado en `j.prometido` y te lo cobran), pidiendo paciencia, marcando
  la cancha o poniéndolo en la lista de transferibles. Medido: 11 mensajes por temporada.


**18 · Seis minijuegos más, agendas rehechas y copas más cortas**
- **6 minijuegos nuevos** (total **18**): `paredN` (pared con doble timing), `sombrero`
  (esperar que el defensor se tire), `chilena` (media vuelta sobre el centro),
  `corner` (mandarla al círculo donde saltan los tuyos + fuerza), `barrida`
  (con franja roja: si entrás ahí es **roja directa** y suma a `G.tRoja`) y `centroP`
  (el arquero sale a descolgar). Todos con su entrada en `MG_INFO`, `STAT_MG`,
  `GOL_TXT`, `ASI_TXT` y repartidos en `MGPOS`.
  - **Cuidado con los nombres**: ya existía un `MG.pared` de los minijuegos viejos y
    el nuevo lo pisaba (o al revés, según el orden en el archivo). Por eso el mío se
    llama `paredN`. Antes de agregar uno, revisar duplicados con
    `re.findall(r'MG\.(\w+)\s*=', html)` y un `Counter`.
- **Las dos agendas rehechas** (`R.agenda` y `R.dtAgenda`), con las mismas clases
  (`agResumen`, `agProx`, `agMes`, `agDia`): barra de ganados/empatados/perdidos,
  panel de estado, tarjeta grande del próximo partido, agrupado por mes con contador
  y cada partido con marcador de color. Las fechas de copa llevan **borde de color según
  la copa** y el trofeo en vez del escudo del rival (que se sortea).
- **Copas más cortas**: la copa internacional de la carrera pasó de 4 llaves a **3**
  (`RONDAS_J`) y se siembra cada 6 fechas; el Mundial de Clubes pasó de 3 a **2**
  (`RONDAS_MC`: Semifinal y LA FINAL).
- **Identidad por copa** (`COPA_ID`): Libertadores verde, Sudamericana dorada, Champions
  azul, Europa League naranja, las de Asia turquesa y violeta. Se usa en la placa del hub
  (`.htile.copaT.<cls>`), en el encabezado del partido (`.copaHead`) y en la agenda.

**Cómo probar minijuegos en headless (aprendido a los golpes)**
- El screenshot se toma apenas carga, así que un minijuego recién montado casi no alcanza
  a pintar. Hay que **forzar los cuadros a mano**: interceptar `requestAnimationFrame`,
  lanzar el juego y recién después correr el bucle con un reloj que **arranque en
  `performance.now()` tomado justo antes**, porque `mgLoop` guarda `t0=performance.now()`
  al crearse y si el reloj falso va atrasado el `dt` sale negativo y nada avanza.
- No se pueden montar varios minijuegos a la vez en el mismo documento: `mgUI` busca
  `$('mgc')` por id y todos escriben en el primero. Hay que probarlos de a uno.


**19 · Tu cara en los minijuegos**
- `dJugador(x,cx,cy,s,col,lean,brazos,yo)` acepta un octavo parámetro. Si `yo` es
  verdadero, en vez de la cabeza plana dibuja **tu piel y tu pelo** (`miCara()`),
  con los seis cortes reproducidos en miniatura. Se marcaron las 10 llamadas donde
  el muñequito verde grande sos vos.

**Bugs preexistentes arreglados**
- `escudoSVG`: cuando el hash del club daba negativo, `formas[forma]` era `undefined`
  y el escudo dibujado salía con un `path` roto. Ahora se normaliza con `((x%n)+n)%n`.
- El cupo de 28 del plantel del DT (ver arriba).

**Nota para las pruebas**: en screenshots headless de Firefox el texto dentro de `<b>`
a veces no aparece aunque esté en el DOM. No es un bug del juego: se verificó con
`getComputedStyle` y agregando un `outline`. Para probar la lógica conviene inyectar
un reloj virtual que reemplace `requestAnimationFrame` y `setTimeout`.

---

## Arquitectura del archivo

Todo en un `<script>` gigante al final del HTML. Secciones en orden:

1. Utilidades (`$`, `rnd`, `ri`, `pick`, `clamp`, `toast`, `modal`, `seeded`, `hash`)
2. Fondo de estadio animado en canvas
3. Audio sintetizado (bombo, palmas, coro de hinchada, trompeta) — sin archivos
4. Íconos SVG (`ic()`) + `iconify()` que reemplaza emojis automáticamente
5. Escudos (`escudo()` usa imagen real, `escudoSVG()` es el respaldo dibujado)
6. `const REAL = {p, c, b, l, t}` — planteles, cedidos, escudos, logos de liga, técnicos
   - Clave de plantel: `"liga|Club"` (ej. `"arg1|Boca Juniors"`)
   - Formato de jugador: `nombre|puesto|media|edad|nacionalidad` separados por `;`
7. `const LIGAS` + `DIV1` + `DIV2` + `ASCENSO`
8. `plantel(ligaId, clubIdx, año)` — devuelve el plantel con envejecimiento y juveniles
9. Estado `G` (jugador) y `D` (DT), router `R` con una función por pantalla
10. Motor de partido físico (`iniciarFisico`, `fisicaP`, `pintarP`, `iaP`, `patearA`)
11. Modos: carrera jugador, carrera DT, desafíos, online

**Patrón del router**: `R.nombrePantalla = () => 'html'` y se navega con `ir('nombre')`.
`render()` pinta la pantalla actual y pasa todo por `iconify()`.

---

## Cómo trabajar con el archivo

Es muy grande para editarlo a mano. El método que funcionó todo el proyecto:

```bash
python3 - <<'EOF'
p='ladiez.html'; s=open(p,encoding='utf-8').read()
s=s.replace("texto viejo exacto","texto nuevo")
open(p,'w',encoding='utf-8').write(s)
EOF
```

Y **siempre verificar la sintaxis** después de cada cambio:

```bash
python3 -c "
import re;h=open('ladiez.html',encoding='utf-8').read()
open('/tmp/l.js','w').write(re.findall(r'<script>(.*?)</script>',h,re.S)[-1])" && node --check /tmp/l.js
```

Para probar de verdad (esto encontró muchos bugs):

```bash
# inyectar un script de prueba y sacar screenshot
firefox --headless --screenshot /tmp/t.png --window-size=1080,500 "file:///tmp/test.html"
```

**Ojo con dos trampas conocidas:**
- No declarar variables `R`, `P`, `M`, `G`, `D`, `V` en los scripts de prueba: ya
  existen en el juego y `const` redeclarado tira SyntaxError silencioso.
- Los archivos temporales en `/tmp` se borran entre sesiones.

---

## LO QUE FALTA — lista priorizada por el usuario

El usuario ya decidió qué quiere. Esto es lo que pidió, ordenado:

### Ligas y datos
- [x] ~~Paraguay, Perú, Bolivia, Ecuador, Venezuela, Chile~~ — HECHO
- [x] ~~Completar Paraguay~~ — 11 clubes (falta solo Recoleta)
- [x] ~~Completar Chile~~ — 17 clubes
- [x] ~~Atlético de Madrid~~ — estaba faltando en LaLiga, ya está (fuerza 83)
- [ ] Faltan todavía: Recoleta (Paraguay), Real Oruro (Bolivia),
      Universidad de Concepción (Chile). Sus artículos no tienen plantel.

**IMPORTANTE — cómo bajar clubes latinoamericanos**: la Wikipedia en inglés no tiene
los planteles de la mayoría. La **Wikipedia en español sí**, y además trae
nacionalidad y fecha de nacimiento. Usa la plantilla `{{Jugador de fútbol}}` con los
campos `nombre`/`name`, `pos` (POR/DEF/MED/DEL), `nac`/`nat`, `num`/`no` y
`edad={{edad|dd|mm|aaaa}}`. Hay un parser hecho en `/tmp/fb/es_parser.py`
(si se borró, está descrito acá).
- [ ] **Logos propios de las segundas divisiones y de las ligas nuevas**. Solo se
      consiguieron 4 correctos (Championship, 2.Bundesliga, Ligue 2, Brasileirão B).
      El endpoint `searchleagues.php` de TheSportsDB da 404 en la clave gratuita y los
      IDs de `lookupleague.php` devuelven ligas equivocadas. Habría que sondear IDs
      uno por uno verificando el nombre devuelto, o buscar otra fuente.

### Modo Jugador
- [x] ~~Mundial, Copa América, Eurocopa, Finalissima con la Selección~~ — HECHO
- [x] ~~Mundial de Clubes~~ — HECHO
- [ ] **Atributos con costo**: que subir Velocidad aumente el riesgo de lesión y
      Resistencia alargue la carrera (idea de El Ídolo)
- [ ] **Calificación en vivo durante el partido**: nota que arranca en 6.0 y sube o
      baja con cada jugada, visible todo el partido (idea de FIFA)
- [x] ~~Minijuegos nuevos y más profesionales, sin emojis~~ — HECHO (12 en canvas)
- [x] ~~Staff personal con efectos permanentes~~ — HECHO (5 roles × 3 niveles)
- [ ] **Rasgos desbloqueables** que cambien cómo funcionan los minijuegos
- [x] ~~Nacionalidad separada de la liga~~ — HECHO
- [ ] **Dorsal del 1 al 99**
- [ ] **Barra de titularidad** visible que sube y baja con cada partido
- [ ] **Imagen compartible del palmarés** al retirarte
- [ ] **Carrera del Día** con semilla fija (necesita el servidor para el ranking)
- [x] ~~Arreglar la tienda y la economía completa~~ — HECHO (staff, patrimonio, sueldo por fecha)

### Modo DT
- [x] ~~Agenda (calendario) igual que la del modo jugador~~ — HECHO
- [x] ~~Ojeadores con informes por rango~~ — HECHO (dos: ±3/5 fechas y ±7/2 fechas)
- [x] ~~Curvas de crecimiento ocultas~~ — HECHO (+ pibes de inferiores cada pretemporada)
- [ ] **Presupuesto partido en dos**: fichajes y masa salarial
- [ ] **Cláusulas en la negociación**: bonus por partidos, por goles, porcentaje de
      futura venta, cesión con opción de compra
- [ ] **Expectativas de la hinchada** separadas de las de la junta directiva
- [ ] **Conversaciones individuales** con jugadores: prometer minutos, pedir
      esfuerzo, avisar que está en el mercado
- [ ] **Academia de juveniles** con potencial oculto
- [ ] **Mundial de Clubes** también en modo DT
- [x] ~~Modo Champions con los 36 equipos reales~~ — HECHO

### Premios
- [ ] Máximo goleador, máximo asistidor y mejor jugador **de cada liga** (no solo del
      jugador). Balón de Oro y Bota de Oro con votación entre todos los jugadores.

### Online
- [ ] Que ande bien con datos móviles
- [ ] Modo DT compartido (dos personas dirigiendo el mismo club). El servidor ya
      tiene los mensajes `dt` listos, falta la pantalla.

---

## Decisiones ya tomadas (no volver a preguntar)

- **La energía NO bloquea partidos.** Solo entrenamiento. Ya está aplicado.
- **Nada de emojis en la interfaz.** Hay un set de íconos SVG (`ic()`), usarlo.
  El `iconify()` convierte emojis automáticamente pero es mejor no ponerlos.
- **Nombres reales de jugadores y clubes**, verificados. El usuario detecta al toque
  si hay un nombre inventado.
- **Escudos oficiales**, no dibujados. Si no se consigue el correcto, es preferible
  dejar el dibujado antes que poner uno de otro club.
- **Pagos**: nunca un formulario propio que pida tarjeta. Se usa Checkout Pro de
  Mercado Pago (link externo). El módulo ya está escrito en `ladiez-servidor/pagos.js`
  y solo necesita que el usuario ponga su `MP_TOKEN`.
- **El servidor online** funciona y está probado, pero hay que desplegarlo en Render
  o Railway (el usuario todavía no lo hizo).

---

## Referencias que el usuario quiere copiar

| Juego | Qué copiar |
|---|---|
| **El Ídolo** (potrerofutbol.ar) | Idolatría por club ✅ hecho · atributos con costo · staff · tienda de patrimonio · eventos por país |
| **Copero** (copero.com.ar) | Eventos grises ✅ hecho · logros de carrera larga ✅ hecho |
| **FIFA / EA FC** | Nota en vivo · objetivos del DT ✅ hecho · ojeadores · cláusulas · junta con objetivos múltiples |
| **PES** | Curvas de crecimiento ocultas · Master League |

Hay un análisis detallado en `/home/matiigonzz/Claude/IDEAS-modo-carrera.md`.

---

## Otros archivos del proyecto

- `ladiez.html` — el juego
- `ladiez-servidor/server.js` — servidor de salas (probado, funciona)
- `ladiez-servidor/pagos.js` — Mercado Pago Checkout Pro
- `ladiez-servidor/LEEME.md` — cómo levantarlo y cómo subirlo gratis
- `IDEAS-modo-carrera.md` — investigación de los 4 juegos de referencia
- `crack.html`, `potrero-leyenda.html` — versiones viejas, se pueden borrar

---

## Advertencia importante

Las partidas guardadas **se rompen** cada vez que cambian los identificadores de liga
o la estructura de `G` / `D`. Ya pasó una vez (cuando `arg` pasó a ser `arg1`).
Si se cambia algo estructural, avisarle al usuario que va a tener que empezar de nuevo.
