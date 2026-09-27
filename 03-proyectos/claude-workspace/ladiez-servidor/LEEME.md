# Servidor de LA DIEZ

Servidor de salas para jugar online. Es un Node con WebSocket, sin base de datos.

## Probarlo en tu compu

```bash
cd ladiez-servidor
npm install
npm start
```

Queda escuchando en `http://localhost:8080`. Abrí esa dirección en el navegador:
el servidor entrega el juego y conecta las salas automáticamente.

Para probar, abrí `http://localhost:8080` en dos pestañas. Una crea la sala y la otra
entra con el código. Desde otra computadora de tu casa usá la IP del equipo que ejecuta
el servidor, por ejemplo `http://192.168.0.15:8080`.

## Ponerlo en internet gratis

Para jugar con alguien que está en otra casa, el servidor tiene que estar
en internet. Las tres opciones más simples, todas con plan gratis:

### Render.com
1. Subí esta carpeta a un repositorio de GitHub.
2. Entrá a render.com → New → Web Service → conectá el repo.
3. Build command: `npm install` · Start command: `npm start`.
4. Te queda una dirección tipo `https://ladiez-servidor.onrender.com`.
5. Abrí esa dirección: el juego detecta automáticamente el `wss://` del mismo servidor.

Ojo: el plan gratis de Render duerme el servidor si nadie lo usa por 15 minutos.
La primera conexión después de dormir tarda unos 30 segundos.

### Railway.app
Igual que Render, pero sin dormirse. Tiene unas horas gratis por mes.

### Fly.io
Más técnico pero el plan gratis aguanta más. Necesita instalar `flyctl`.

## Cómo saber si está andando

Entrá con el navegador a la dirección del servidor: tiene que abrir el juego.
La ruta `/servidor` muestra el estado y `/salud` devuelve un JSON
con cuántas salas y jugadores hay conectados.

## Qué hace cada mensaje

| Mensaje | Quién lo manda | Para qué |
|---|---|---|
| `crear` | el que arma la sala | devuelve un código de 4 letras |
| `unir` | el que entra | se mete a la sala con ese código |
| `config` | anfitrión | manda los equipos y el formato del partido |
| `estado` | anfitrión | posiciones de todos, 30 veces por segundo |
| `input` | invitado | qué teclas está apretando |
| `dt` | cualquiera | decisiones del modo entrenador compartido |
| `chat` | cualquiera | mensajes de texto |

El anfitrión corre la física del partido; el invitado solo manda lo que aprieta
y dibuja lo que recibe. Es el mismo esquema que usan los juegos de este tipo.
