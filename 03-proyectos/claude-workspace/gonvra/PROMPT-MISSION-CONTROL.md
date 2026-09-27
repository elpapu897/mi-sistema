# ▼▼▼ PEGAR ESTO EN HERMES ▼▼▼

Ya tenemos el canal de Telegram andando (el bot me reconoce, responde en español y este chat es el
canal principal). Y arreglaste los botones (funcionó). Ahora sí quiero armar el sistema completo.

## Lo que quiero construir: un "Mission Control" para GONVRA

Un **centro de control de agentes** corriendo **24/7**, donde el equipo de agentes de IA con
personalidad propia trabaja, **se comunica entre sí**, resuelve tareas **de forma autónoma** y se
va **mejorando solo** — todo con un objetivo: **que gonvra.com genere plata** (tienda Shopify de
artículos para mascotas, Argentina).

**Antes de arrancar, leé estos archivos (ya están escritos):**
- `~/Claude/gonvra/CONTEXTO.md` → todo sobre el negocio, catálogo dinámico, bloqueantes.
- `~/Claude/gonvra/PEGAR-EN-HERMES.md` → el diseño de los 30 agentes + SEMÁFORO, sus personalidades,
  herramientas, horarios y cómo se pasan trabajo.
- `~/Claude/gonvra/RESPUESTAS-A-HERMES.md` → mis reglas operativas ya definidas.

No reinventes nada: **usá las piezas que Hermes ya tiene** y conectalas en un solo sistema:
- **`hermes kanban`** → tablero de tareas (crear, asignar, dependencias, en proceso / revisión /
  completadas). Es el "centro de control" donde yo creo tareas y monitoreo.
- **`hermes kanban swarm`** → varios agentes en paralelo → verificador → sintetizador. Justo lo que
  quiero: agentes que colaboran y se revisan entre sí.
- **`hermes kanban watch` / `tail`** → ver en vivo qué está pasando.
- **`hermes dashboard`** → el panel web visual.
- **`hermes cron`** → los agentes que corren solos en horarios (24/7).
- **El gateway de Telegram** → ya configurado, para aprobar y recibir avisos desde el celular.
- **Las 1146 skills que ya tenés instaladas** → usá las que sirvan (paid-ads-tiktok,
  short-video-scripter, social-content-os, muapi-youtube-shorts, etc.). No instales de más.

## Infraestructura: NATIVO ahora, VPS después

- Corremos **nativo en mi laptop por ahora** (es gratis y ya está todo conectado). Es una laptop, así
  que la voy a dejar enchufada; ya la configuramos para que no se suspenda enchufada.
- **Dejá todo listo para migrar a un VPS más adelante**, cuando la tienda empiece a vender (ahí un
  servidor de ~$5/mes se paga solo). No hardcodees rutas raras que impidan mudarlo.
- Nada de contratar el VPS ahora. Regla de plata: gratis primero, pagar solo cuando se paga solo.

## Memoria compartida (YA ESTÁ HECHA, usala)

Ya montamos una memoria común: los chats de Claude Code, Codex y Hermes se exportan solos a Obsidian
cada 30 min en `~/OBSIDIAN/07-Agentes/<Herramienta>/chats/` (ver
`~/OBSIDIAN/07-Agentes/COMO-LEER-CHATS.md`). **El agente BIBLIOTECARIO tiene que leer de ahí** para
no repetir errores ni perder contexto entre herramientas.

## Herramienta de espionaje de videos (YA ESTÁ HECHA, AHORRA TOKENS)

Armamos `~/Claude/scripts/video-intel.py` — el "conector" para YouTube, TikTok e Instagram que
**ahorra tokens**: en vez de bajar y mirar un video entero, saca solo los datos y la transcripción.
Los agentes ESPÍA, TIKTOKER, INSTAGRAMER y SCOUT lo tienen que usar SIEMPRE que analicen videos:

- Analizar 1 video (datos + guion en texto):
  `python3 ~/Claude/scripts/video-intel.py "<URL>"`
- Escanear un canal o hashtag barato (solo metadata, ordena por vistas):
  `python3 ~/Claude/scripts/video-intel.py "<URL_canal>" --scan 20`

Está probado y funciona (usa yt-dlp, que ya está instalado). Sirve para ver **cómo hace los videos
la competencia**: qué dicen, qué hooks usan, cuántas vistas tienen, qué hashtags.

## REGLA DE ORO DE TOKENS (importante, la pediste)

Quiero que el sistema sea **barato en tokens**. Instruí a TODOS los agentes:
1. **Nunca procesar un video entero** si alcanza con la transcripción (usar `video-intel.py`).
2. **Escanear primero barato** (`--scan`) y solo profundizar en lo que rinde.
3. **Leer las notas de Obsidian** en vez de re-investigar algo que ya se investigó.
4. **Resumir y guardar a disco**, no arrastrar todo el contexto entre corridas.
5. Usar el **modelo más barato que sirva** para cada tarea (las tareas simples no necesitan el
   modelo caro). Configurá los cron/kanban con el modelo adecuado por tipo de tarea.
6. Cada agente escribe su entregable a `~/Claude/gonvra/<agente>/` y el JEFE solo lee resúmenes.

## Qué quiero que haga el Mission Control

1. **Tablero (kanban)** con los 30 agentes + SEMÁFORO como perfiles/asignados, cada uno con su
   personalidad, herramientas y objetivo (todo está en PEGAR-EN-HERMES.md).
2. **Que se pasen tareas entre sí solos** (las cadenas ya están en el brief).
3. **Swarm** para las tareas grandes (varios atacan → verificador → sintetizador).
4. **Verlo en tiempo real desde la PC y desde el celular** (dashboard web + Telegram). Guiame para
   entrar de forma segura desde el celular (con contraseña o lo más seguro que tengas).
5. **Centro de control para mí:** crear tareas, monitorear las que están en proceso, revisar las
   completadas antes de que se ejecute algo que gaste plata o salga público.
6. **Que busque ideas de contenido y productos todo el tiempo**, sin que yo lo pida.

## Reglas que NO se negocian

1. **Construir todo AHORA, prender por fases.** Montá el sistema completo y dejalo corriendo 24/7,
   pero la **pauta de Meta (gastar plata) queda BLOQUEADA** hasta resolver los dos bloqueantes
   (checkout que cobre + píxel sano). Ese orden ya lo acordamos.
2. **Ningún agente gasta un peso, publica algo, manda un mensaje o publica un tema sin mi OK por el
   SEMÁFORO (Telegram).** Armar campañas en pausa sí; prenderlas no.
3. **El catálogo es dinámico:** ningún agente hardcodea productos; todo se lee en vivo de Shopify.
4. **Español rioplatense**, hablame como a alguien no técnico.
5. **Plata gratis primero:** nada de herramientas pagas sin preguntarme (regla de las 3 ventas).
6. **Yo leo un solo resumen por día** (21:00). El resto queda en el tablero.

## Qué quiero que me devuelvas (sin ejecutar todavía la parte de plata)

1. Un **plan concreto** de cómo vas a montar el Mission Control con las piezas de Hermes, en criollo.
2. **Qué prendés hoy** y qué queda esperando los bloqueantes.
3. **Cómo entro al panel desde la PC y desde el celular**, paso a paso, seguro.
4. Confirmación de que los agentes van a usar `video-intel.py` y la memoria de Obsidian.
5. Si algo **no se puede** con Hermes tal como está, decímelo de frente y ofrecé la alternativa más
   parecida. No me prometas nada que no puedas cumplir.

Arrancá cuando quieras. Si necesitás que haga algo (permisos, prender algo en el celular), pedímelo
de a un paso por vez.

# ▲▲▲ FIN ▲▲▲
