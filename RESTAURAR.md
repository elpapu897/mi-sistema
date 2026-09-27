# Restaurar en la máquina nueva

Guía para **TomexOS 10 21H2 LTSC Pro x64** (Windows 10 modificado). Los pasos
valen igual para cualquier Windows 10/11; donde LTSC se comporta distinto está
marcado.

> **Leé la sección 1 antes de clonar.** Hay dos cosas que se configuran *antes*
> de bajar el repo, y si no lo hacés tenés que clonar de nuevo.

---

## 0. Cuánto va a tardar

| Paso | Tiempo |
|---|---|
| Instalar herramientas | 15 min |
| `git clone` (2 GB de git normal) | ~15 min |
| `git lfs pull` (24,85 GB de media) | 1,5 a 3 h según tu bajada |
| `restaurar.sh` / `restaurar.ps1` | 10 min |
| Re-autenticar agentes | 15 min |

Si tenés apuro: el paso 4 permite restaurar **solo lo irremplazable** primero y
dejar los 24 GB de video para después. Con eso estás trabajando en 40 minutos.

---

## 1. Antes de clonar

### 1.1 Modo Desarrollador — para los symlinks

El sistema usa **3.154 enlaces simbólicos**. Sin esto, git los baja como
archivos de texto con una ruta adentro, y **las 1.067 skills no funcionan**.

`Configuración` → `Privacidad y seguridad` → `Para desarrolladores` →
activar **Modo de desarrollador**.

En LTSC ese panel a veces no aparece. Alternativa por registro, en PowerShell
como administrador:

```powershell
New-ItemProperty -Path "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\AppModelUnlock" `
  -Name AllowDevelopmentWithoutDevLicense -Value 1 -PropertyType DWord -Force
```

### 1.2 Rutas largas y symlinks en git

```powershell
git config --global core.longpaths true
git config --global core.symlinks true
```

La ruta más larga del repo es de 164 caracteres, así que estás cómodo bajo el
límite de 260. `core.longpaths` es por si después agregás cosas.

### 1.3 Herramientas

| Qué | Para qué | Dónde |
|---|---|---|
| **Git for Windows** | git, git-lfs y bash de una | [git-scm.com](https://git-scm.com/download/win) |
| **Node LTS** | `npm install` de los proyectos | [nodejs.org](https://nodejs.org) |
| **Gpg4win** | abrir el paquete de secretos | [gpg4win.org](https://gpg4win.org) |
| **Obsidian** | el segundo cerebro | [obsidian.md](https://obsidian.md) |

Git for Windows trae **Git Bash**, y eso significa que podés usar los scripts
`.sh` sin necesitar WSL. Es el camino más corto.

> **LTSC no trae Microsoft Store.** Si querés WSL, no lo instales desde ahí.
> Ver la sección 6.

---

## 2. Clonar

```bash
git clone https://github.com/USUARIO/mi-sistema.git
cd mi-sistema
```

Esto baja **2 GB**: notas, código, config y los punteros de LFS. Los videos
todavía no.

Verificá que los symlinks quedaron bien:

```bash
ls -la 02-agentes/claude/skills | head -3
```

Si ves `->` apuntando a algún lado, perfecto. Si ves archivos comunes de ~40
bytes, el Modo Desarrollador no estaba activo: activalo y corré
`git checkout -- .` de nuevo.

---

## 3. Bajar la media (24,85 GB)

```bash
git lfs install
git lfs pull
```

Si se corta, volvé a correr `git lfs pull`: retoma donde quedó, no empieza de
cero.

**Para saltear esto por ahora** y restaurar solo lo importante:

```bash
git lfs install
git lfs pull --include="01-segundo-cerebro/**,02-agentes/**,99-secretos/**"
```

---

## 4. Restaurar

Siempre **simulá primero**. No toca nada y te muestra exactamente qué haría:

```bash
bash scripts/restaurar.sh --dry-run
```

Si te convence:

```bash
bash scripts/restaurar.sh
```

Sin Git Bash, en PowerShell:

```powershell
powershell -ExecutionPolicy Bypass -File scripts\restaurar.ps1 -DryRun
powershell -ExecutionPolicy Bypass -File scripts\restaurar.ps1
```

### Restaurar por partes

```bash
bash scripts/restaurar.sh --solo ic        # solo lo irremplazable (500 MB)
bash scripts/restaurar.sh --solo ic,pr     # + proyectos
bash scripts/restaurar.sh --solo md        # solo la media, después
```

| Código | Qué trae | Peso |
|---|---|--:|
| `ic` | Obsidian, agentes, 1.235 skills | 336 MB |
| `pr` | Código propio | 2,3 GB |
| `ng` | GONVRA | 476 MB |
| `md` | Video y audio | 22 GB |
| `hi` | Historial de conversaciones | 1,5 GB |

**Nada se sobrescribe.** Si el destino ya existe, se renombra a
`<nombre>.previo-<fecha>`.

---

## 5. Los cuatro pasos que faltan

### 5.1 Symlinks

```bash
bash scripts/rehacer-symlinks.sh
```

Correlo **después** de restaurar todo. Si lo corrés antes, algunos enlaces
apuntan a carpetas que todavía no existen (el script te lo dice y no es grave:
volvé a correrlo al final y tiene que dar 0 rotos).

### 5.2 Repos de terceros

```bash
bash scripts/reclonar-terceros.sh
```

Trae los 15 repos externos en su commit exacto. Si alguno falla es porque lo
borraron de GitHub, no porque el backup esté mal.

### 5.3 Credenciales

```bash
bash scripts/descifrar-secretos.sh
```

Te pide la passphrase. Devuelve las claves SSH con permisos 600 (si no, SSH las
rechaza) y los tokens de los agentes a su lugar.

Probalo:

```bash
ssh -i ~/.ssh/gonvra_vps <usuario>@<host>
```

### 5.4 Dependencias

```bash
cd ~/g && npm install
cd ~/planetamati-edit/motion && npm install
```

Los 527 MB de `node_modules` de Remotion no se respaldaron a propósito.

---

## 6. WSL, solo si lo querés

Los agentes CLI andan en Git Bash. WSL es más cómodo pero **en LTSC da trabajo**
porque no hay Microsoft Store.

PowerShell como administrador:

```powershell
dism /online /Enable-Feature /FeatureName:Microsoft-Windows-Subsystem-Linux /All /NoRestart
dism /online /Enable-Feature /FeatureName:VirtualMachinePlatform /All /NoRestart
```

Reiniciá, y después:

```powershell
wsl --install -d Ubuntu
```

Si `wsl --install` no existe en tu build, bajá el kernel y la distro a mano
desde [aka.ms/wsl2kernel](https://aka.ms/wsl2kernel) y
[docs.microsoft.com/windows/wsl/install-manual](https://learn.microsoft.com/windows/wsl/install-manual).

Con WSL andando, restaurá **dentro** de WSL, no en `/mnt/c`: el rendimiento del
sistema de archivos entre Windows y Linux es malísimo y Obsidian con 5.555 notas
se arrastra.

---

## 7. Si algo sale mal

| Síntoma | Causa | Qué hacer |
|---|---|---|
| Las skills son archivos de texto con una ruta adentro | Modo Desarrollador apagado al clonar | Activalo, `git checkout -- .`, después `rehacer-symlinks.sh` |
| Los videos pesan 130 bytes | No corriste `git lfs pull` | `git lfs install && git lfs pull` |
| `Permission denied (publickey)` al VPS | Permisos de la clave SSH | `chmod 600 ~/.ssh/gonvra_vps` |
| `gpg: decryption failed` | Passphrase incorrecta | No hay recuperación posible. Regenerá las credenciales siguiendo [CREDENCIALES.md](CREDENCIALES.md) |
| Claude Code no reconoce las skills | Symlinks rotos | `bash scripts/rehacer-symlinks.sh` y revisá que diga 0 rotos |
| `Filename too long` | `core.longpaths` sin configurar | `git config --global core.longpaths true` y clonar de nuevo |
| El clone tarda muchísimo | Está bajando LFS junto con git | `GIT_LFS_SKIP_SMUDGE=1 git clone ...` y después `git lfs pull` |

---

## 8. Checklist final

```
[ ] Modo Desarrollador activo
[ ] core.longpaths y core.symlinks configurados
[ ] git clone completo
[ ] git lfs pull terminado
[ ] restaurar.sh (o .ps1) sin errores
[ ] rehacer-symlinks.sh -> 0 rotos
[ ] reclonar-terceros.sh -> 15 clonados
[ ] descifrar-secretos.sh -> SSH al VPS funciona
[ ] Obsidian abre el vault y ve 5.555 notas
[ ] Claude Code lista las 1.235 skills
[ ] npm install en los proyectos que vayas a usar
[ ] Borrar los .previo-<fecha> cuando confirmes que todo anda
```
