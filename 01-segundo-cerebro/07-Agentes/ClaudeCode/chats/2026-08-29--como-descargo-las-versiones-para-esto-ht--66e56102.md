---
tool: ClaudeCode
session_id: 66e56102-c647-4796-b19e-e11daecff8cf
fecha: 2026-08-29 16:23
titulo: "como descargo las versiones para esto httpswwwyout"
tags: [chat, agente, claudecode]
---

# 💬 como descargo las versiones para esto httpswwwyout
> **ClaudeCode** · 2026-08-29 16:23 · `66e56102-c647-4796-b19e-e11daecff8cf`

---

### 🧑 Vos  <small>2026-08-29 16:23</small>

como descargo las versiones para esto https://www.youtube.com/watch?v=2wGLhVNlFJA&t=502s

### 🤖 Claude  <small>2026-08-29 16:23</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-08-29 16:23</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-08-29 16:23</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-08-29 16:23</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-08-29 16:24</small>

El video es **"¡Minecraft Bedrock en Linux para todos, premium y no premium!"** de JavierC — o sea, el **mcpelauncher (Minecraft Bedrock Launcher)**. Todavía no lo tenés instalado en esta máquina (no hay flatpak ni `~/.var/app/io.mrarm.mcpelauncher`).

Las "versiones" no se bajan aparte a mano: las descarga el propio launcher desde Google Play, con la cuenta que tiene comprado Minecraft.

**Cómo se hace (camino legítimo):**

1. Instalá el launcher (Flatpak es lo más simple en Fedora):

```bash
flatpak install flathub io.mrarm.mcpelauncher
```

2. Abrilo y andá a la pestaña **Versions**.
3. Tocá **Sign in to Google Play** e iniciá sesión con la cuenta de Google que tiene la licencia de Minecraft Bedrock (Android).
4. Te aparece la lista de versiones disponibles; elegís la que querés (ej. 1.21.x) y le das **Download / Install**. Quedan guardadas en `~/.var/app/io.mrarm.mcpelauncher/data/mcpelauncher/versions/`.
5. Volvés a **Launch** y arrancás con la versión elegida.

**Detalles que suelen trabar:**
- Si sos de CPU x86_64 (tu caso), en Settings tenés que dejar activado el soporte ARM (**libhoudini / ndk-translation**); sin eso las versiones nuevas ni arrancan.
- Si el login de Google falla, probá borrar `~/.var/app/io.mrarm.mcpelauncher/data/mcpelauncher/` y reintentar.
- La opción de **importar un APK** existe (botón "Import"), pero sirve para un APK que hayas obtenido legítimamente de tu propia compra; no te voy a ayudar a bajar copias pirata, que es la parte "no premium" del video.

¿Querés que te lo instale y configure ahora?

### 🧑 Vos  <small>2026-08-29 17:50</small>

cmo descargo las versiones

### 🤖 Claude  <small>2026-08-29 17:50</small>

Dentro del launcher, así:

**1. Instalalo (si aún no):**

```bash
flatpak install -y flathub io.mrarm.mcpelauncher
```

**2. Abrilo:**

```bash
flatpak run io.mrarm.mcpelauncher
```

**3. Descargar versiones (dentro de la app):**

1. Arriba a la derecha, botón **⚙ / Settings** → activá **Show all versions** (si no, solo ves la última).
2. Andá a la pestaña **Versions** (o al desplegable de versión al lado del botón *Play*).
3. La primera vez te va a pedir **Sign in with Google** → iniciás sesión con la cuenta de Google que tiene comprado *Minecraft: Bedrock Edition* para Android. Ese login es lo que habilita la lista de descargas.
4. Ya logueado, se llena la lista de versiones (1.21.x, 1.20.x, etc.). Al lado de cada una hay un ícono de **descarga (↓)**. Clic ahí y espera: baja el APK desde Play y lo extrae solo.
5. Cuando termina, la versión queda marcada como instalada; la seleccionás y le das **Play**.

**Dónde quedan guardadas:**
`~/.var/app/io.mrarm.mcpelauncher/data/mcpelauncher/versions/`

**Si no aparece la lista o falla la descarga:**
- Verificá que la cuenta de Google realmente tenga la compra (probá abrir Play Store en el navegador con esa cuenta y ver Minecraft como "comprado").
- En Settings, activá el soporte ARM (**ndk-translation / libhoudini**); sin eso descarga pero no arranca en CPU Intel/AMD.
- Reset del login: cerrá la app y borrá `~/.var/app/io.mrarm.mcpelauncher/data/mcpelauncher/` (perdés las versiones bajadas, no los mundos si hiciste backup).

La parte "no premium" del video usa APKs pirateados: eso no te lo voy a armar. Con la compra en Google Play, el flujo de arriba te da todas las versiones.

¿Te lo instalo y lo dejo abierto para que hagas el login?

### 🧑 Vos  <small>2026-08-29 17:51</small>

sistem o user??

### 🤖 Claude  <small>2026-08-29 17:51</small>

Es la pregunta del `flatpak install` cuando Flathub está configurado en los dos ámbitos. **Elegí `user`.**

- **user** → se instala en `~/.local/share/flatpak`, no pide contraseña de root, y los datos van a `~/.var/app/io.mrarm.mcpelauncher/` (que es la ruta que te pasé para las versiones y mundos). Es lo ideal en una máquina de un solo usuario.
- **system** → en `/var/lib/flatpak`, pide sudo, y sirve para todas las cuentas del equipo. Igual los datos de tu usuario siguen yendo a `~/.var/app/...`.

Para evitar la pregunta directamente:

```bash
flatpak install --user -y flathub io.mrarm.mcpelauncher
```

Y para lanzarlo:

```bash
flatpak run io.mrarm.mcpelauncher
```

### 🧑 Vos  <small>2026-08-29 17:54</small>

https://www.youtube.com/watch?v=DTUVXVyU1DU y en este??

### 🤖 Claude  <small>2026-08-29 17:54</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-08-29 17:54</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-08-29 17:55</small>

Es el mismo software: **mcpelauncher (Minecraft Bedrock Launcher)**. Ese video de *xeyt* es básicamente la misma receta que el de JavierC, solo que suele mostrar la instalación vía **AppImage** en lugar de Flatpak. El mecanismo para bajar versiones es idéntico.

**Diferencia entre los dos caminos:**

| | Flatpak (recomendado) | AppImage |
|---|---|---|
| Instalación | `flatpak install --user -y flathub io.mrarm.mcpelauncher` | descargás el `.AppImage`, `chmod +x`, doble clic |
| Actualizaciones | automáticas | a mano, bajando el archivo nuevo |
| Datos/versiones | `~/.var/app/io.mrarm.mcpelauncher/data/mcpelauncher/versions/` | `~/.local/share/mcpelauncher/versions/` |

**Descargar las versiones (igual en ambos):**

1. Abrís el launcher.
2. Settings → activás **Show all versions** y el soporte ARM (**ndk-translation / libhoudini**), obligatorio en CPU Intel/AMD.
3. Pestaña **Versions** → **Sign in with Google** con la cuenta que tiene comprado *Minecraft: Bedrock Edition* (Android).
4. Clic en el ícono ↓ de la versión que quieras (1.21.x, 1.20.x…). El launcher baja el APK desde Play y lo extrae solo.
5. Seleccionás la versión instalada → **Play**.

Sin ese login con una cuenta que tenga la compra, la lista queda vacía: es el único requisito real. La parte "no premium" que muestran esos videos es descargar el APK pirateado, y con eso no te ayudo.

Si querés, te dejo el Flatpak instalado y abierto para que hagas el login:

```bash
flatpak install --user -y flathub io.mrarm.mcpelauncher && flatpak run io.mrarm.mcpelauncher
```
