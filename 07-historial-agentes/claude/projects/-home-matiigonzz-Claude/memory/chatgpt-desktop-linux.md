# ChatGPT Community (codex-desktop-linux)

App de escritorio de ChatGPT/Codex para Linux, no oficial: repackagea el .deb firmado
oficial de OpenAI. Repo: https://github.com/ilysenko/codex-desktop-linux
Instalado y funcionando (13-ago-2026), versión codex-desktop-2026.08.13.040946.

## Dónde está
- Checkout: `~/Descargas/codex-desktop-linux`
- RPM generado: `dist/codex-desktop-<version>-1.x86_64.rpm` (~354 MB)
- Se instala en `/opt/codex-desktop`; en el menú es **ChatGPT Community** (nube azul con "C")
- Binario real: `/opt/codex-desktop/ChatGPT`; launcher `/usr/bin/codex-desktop` → `/opt/codex-desktop/start.sh`

## Cómo se construyó
- Fedora 44 ya tenía todo (node 24 vía nvm, rpmbuild, dpkg, gpgv, gcc...) salvo Rust
- Rust instalado en modo usuario con rustup → `~/.cargo/bin` (necesario para el updater)
- `make build-app` (descarga+verifica el paquete oficial) y luego `make rpm`
- NO se usó `make bootstrap-native` porque llama a `sudo dnf` y sudo pide contraseña

## Trampa: sudo
Sudo en esta máquina **pide contraseña**, así que yo no puedo instalar el RPM.
Le paso al usuario: `sudo dnf install -y ~/Descargas/codex-desktop-linux/dist/*.rpm`

## RESUELTO: icono de engranaje al abrir la app
Síntoma: al abrir, en el dock/alt-tab salía un icono genérico de engranaje.
Causa: corre en **Wayland nativo** y Electron ponía un `app_id` distinto de
`StartupWMClass=codex-desktop` del .desktop → GNOME no asociaba ventana ↔ lanzador
→ icono fallback. El PNG correcto SÍ estaba en
`/usr/share/icons/hicolor/256x256/apps/codex-desktop.png`.
Fix (sin root), en `~/.config/codex-desktop/electron-flags.conf`:
```
--class=codex-desktop
```
`start.sh` lee ese archivo (`load_user_electron_args_file`, ignora líneas `#`).
Hay que cerrar la app del todo y reabrirla para que aplique.
El paquete es `openai-codex-electron` / productName `Codex` / desktopName `chatgpt.desktop`
(por eso el app_id no coincidía).

## Verificar / diagnosticar
- Ver flags aplicados: `pgrep -a ChatGPT | grep -v -- '--type='`
- `gdbus ... org.gnome.Shell.Introspect.GetWindows` está **bloqueado** (AccessDenied), no sirve
- `xprop` tampoco sirve: la app no usa XWayland
- Diagnóstico oficial: `/opt/codex-desktop/start.sh --diagnose`
- OJO con `pgrep -f '/opt/codex-desktop/'`: se matchea a sí mismo y da falsos "aún corriendo"

## Actualizar
Con updater incluido: `codex-update-manager status|check-now|install-ready|rollback`
y `systemctl --user enable --now codex-update-manager.service`.
A mano: `export PATH="$HOME/.cargo/bin:$PATH"; cd ~/Descargas/codex-desktop-linux && make rpm`

## Ojo
- Comparte el perfil `~/.codex` con el Codex CLI; no correr la app oficial de ChatGPT y esta a la vez
- Features opcionales (read-aloud, ui-tweaks, etc.) están desactivadas; se eligen con `make setup-native`
- Desinstalar: `sudo dnf remove codex-desktop`
