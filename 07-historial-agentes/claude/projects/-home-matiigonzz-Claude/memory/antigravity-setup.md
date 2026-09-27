---
name: antigravity-setup
description: "Google Antigravity en Fedora — instalado en ~/Aplicaciones/antigravity, sin traducción al español; el idioma se controla con reglas globales"
metadata: 
  node_type: memory
  type: project
  originSessionId: d34cdcf7-6b5e-4a1f-b8fb-ddc7834d80aa
  modified: 2026-08-14T01:54:25.304Z
---

Google Antigravity (Manager/hub, **v2.8.1**) está instalado como tarball en
`~/Aplicaciones/antigravity/antigravity`. El IDE aparte (producto distinto,
"Antigravity IDE", v2.5.5) NO está instalado.

## Reinstalación del 2026-08-13
La carpeta vieja `~/Descargas/Antigravity/` **desapareció sola** (el .desktop,
el icono en hicolor y `~/.config/Antigravity` sobrevivieron). Se reinstaló en
`~/Aplicaciones/antigravity` para que no se pierda entre las descargas, y se
actualizó el `Exec=` del .desktop a la ruta nueva.

**Cómo conseguir el enlace de descarga** (la página es JS puro, sin `<a href>`):
```
curl -sL --compressed https://antigravity.google/download | grep -oE 'https?://[a-zA-Z0-9./_?=&:%-]*' | grep -i linux
```
Ojo: `curl` sin `--compressed` devuelve binario ilegible. Salen dos productos:
`antigravity-public/antigravity-hub/...` (el Manager, el que usamos) y
`edgedl.me.gvt1.com/.../Antigravity IDE.tar.gz` (el IDE).

Trampa: `antigravity --version` **no imprime la versión, abre la app** (Electron
ignora el flag). Verificar la versión por la URL de descarga, no por el binario.

## Hechos verificados el 2026-08-01 (siguen valiendo)
- **La interfaz solo existe en inglés.** La UI la sirve el binario
  `resources/bin/language_server` en `http://127.0.0.1:<puerto dinámico>`;
  el HTML es `<html lang="en">` y el bundle no tiene i18n ni selector de
  idioma (los cientos de "Language" del bundle son lenguajes de programación).
  El locale del sistema ya es `es_ES.UTF-8` y aun así la UI sale en inglés.
- **El único control real de idioma** es que el *agente* responda en español:
  regla global en `~/.gemini/config/GEMINI.md` (creada).
- El paquete no trae `.desktop` ni icono: creado
  `~/.local/share/applications/antigravity.desktop` (app_id/StartupWMClass
  `antigravity`, protocolo `antigravity://`) e icono extraído de
  `resources/app.asar` → `/icon.png` (512x512) en `~/.local/share/icons/hicolor/`.

## Trampa: la app se queda sin ventana y no se puede reabrir

Síntoma: "no puedo entrar a Antigravity". El proceso sigue vivo pero
`curl http://127.0.0.1:$(head -1 ~/.config/Antigravity/DevToolsActivePort)/json/list`
devuelve `[ ]` (cero ventanas). Causa: con `runInBackground` activo la app se
esconde en la bandeja del sistema, pero **GNOME 50 no tiene bandeja**, y el
handler `second-instance` de `main.js` solo hace `show()` si ya existe una
ventana — con cero ventanas no crea ninguna y la instancia nueva se cierra sola.

Solución aplicada: `"runInBackground": "false"` en
`~/.config/Antigravity/app_storage.json` (sobrevivió a la reinstalación).
Para desatascarlo en caliente: matar el proceso + `pkill -f
Antigravity-x64/resources/bin/language_server`, borrar
`~/.config/Antigravity/Singleton*` y relanzar con `gtk-launch antigravity`.

**Cómo aplicarlo:** si el usuario pide cambios de idioma en Antigravity, editar
`~/.gemini/config/GEMINI.md`, no buscar ajustes en la app. Relacionado:
[[macos-desktop-theme]], [[cursor-setup]].
