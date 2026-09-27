---
name: macos-desktop-theme
description: "User's Fedora GNOME desktop is themed to look like dark macOS/MacBook"
metadata:
  node_type: memory
  type: project
  originSessionId: 91912b4c-9c1e-498e-bdca-ba2c89ff2b58
  modified: 2026-08-10T02:24:18.100Z
---

El usuario corre **Fedora 44, GNOME Shell 50, Wayland**. Look "MacBook/macOS oscuro". El usuario quiere que se parezca lo más posible a una MacBook. Estado actual (2026-08-09):
- Tema GTK (ventanas): **WhiteSur-Dark-solid** (vinceliuice/WhiteSur-gtk-theme) en `~/.themes`.
- Tema del Shell (barra superior): **WhiteSur-Dark** (macOS). OJO: el usuario había subido/probado **Material-Expressive-Shell** y el valor se revirtió solo a Material más de una vez; hay que verificar en `dconf read /org/gnome/shell/extensions/user-theme/name`. El esquema user-theme NO es global (usar `--schemadir` o dconf).
- Iconos oscuros: **Silvery-Dark-Icons** (l4k1) en `~/.icons`. El usuario NO quería los iconos típicos de macOS; el color le gusta como está.
- Fuente: **Inter** (equivalente libre de San Francisco) en `~/.local/share/fonts/Inter`; interfaz 'Inter 11', títulos 'Inter Semi-Bold 11', hinting slight.
- Cursor: WhiteSur-cursors. Wallpaper: Sonoma-dark.jpg en `~/Pictures/Wallpapers`. Botones de ventana a la izquierda (close,minimize,maximize:).
- **Dock: dash2dock-lite@icedman.github.com** (Dash2Dock Animated), NO dash-to-dock (lo reemplazamos por la magnificación al pasar el mouse). Config: icon-size 0 (auto/normal), animation-magnify 0.35, animate-icons true, autohide, fondo transparente alpha 0.12.
- **blur-my-shell** activo pero el usuario NO quiere blur en el panel superior → `panel blur=false`. Overview blur off (rendimiento).
- Fuentes de build clonadas en `~/.mac-theme-build/`.

**Trampas aprendidas:**
- dash2dock-lite `icon-size` NO es en píxeles: valores como 24/48 lo mandan al MÁXIMO (gigante). 0 = normal. Lo que el usuario llamaba "iconos grandes" al pasar el mouse era la MAGNIFICACIÓN (animation-magnify), no el tamaño base.
- WhiteSur install.sh falla (exit 1) por la animación del spinner; neutralizar `start_animation`/`stop_animation` en `libs/lib-core.sh` con `return 0`.
- En Wayland las extensiones nuevas solo se activan tras cerrar y reabrir sesión; los cambios de gsettings SÍ se ven en vivo una vez la extensión está corriendo.
- Revertir: `gsettings reset` de gtk-theme/icon-theme/cursor-theme/font-name y volver a 'Adwaita'.
