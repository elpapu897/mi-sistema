---
tool: ClaudeCode
session_id: e41383bf-fd1f-4f84-90c1-7390b8bb3956
fecha: 2026-09-11 02:12
titulo: "homematiigonzzDescargasSin confirmar 759320crdownl"
tags: [chat, agente, claudecode]
---

# 💬 homematiigonzzDescargasSin confirmar 759320crdownl
> **ClaudeCode** · 2026-09-11 02:12 · `e41383bf-fd1f-4f84-90c1-7390b8bb3956`

---

### 🧑 Vos  <small>2026-09-11 02:12</small>

@"/home/matiigonzz/Descargas/Sin confirmar 759320.crdownload"
descarga davinci en mi pc

### 🤖 Claude  <small>2026-09-11 02:12</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-09-11 02:12</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-11 02:12</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-09-11 02:13</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-11 02:13</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-09-11 02:14</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-11 02:14</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-09-11 02:14</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-11 02:15</small>

La descarga **ya está en curso** — no hace falta que la vuelva a lanzar.

**Estado actual:**

| Dato | Valor |
|---|---|
| Archivo | `Sin confirmar 759320.crdownload` (descarga parcial de Chrome) |
| Tipo | ZIP (coincide con el instalador de Resolve para Linux) |
| Descargado | ~137 MB y subiendo |
| Velocidad | ~2 MB/s (variable) |
| Espacio libre | 378 GB — de sobra |

El instalador de DaVinci Resolve para Linux pesa ~3,5 GB, así que faltan unos **25-30 minutos**. Mientras Chrome esté abierto va a seguir solo.

**Un aviso importante:** estás en Fedora 44, y Resolve no instala limpio ahí. El instalador oficial trae sus propias copias de `libglib`, `libgio` y `libgmodule` que chocan con las del sistema y hacen que la app arranque a pantalla negra o directamente crashee. La solución conocida es borrar esas libs del directorio de instalación después de instalar, para que use las de Fedora. También hay que instalar dependencias (`fuse`, `apr`, `apr-util`, `libxcrypt-compat`) antes de correr el instalador.

¿Querés que te lo deje listo cuando termine la descarga? Puedo:

1. **Monitorear** la descarga y avisarte cuando termine.
2. **Preinstalar las dependencias** ahora mismo con `dnf` (necesita tu contraseña de sudo).
3. **Descomprimir, correr el instalador y aplicar el fix de las libs** cuando el archivo esté completo.

Decime si arranco con los pasos 1 y 2 en paralelo, o si preferís esperar y hacerlo vos a mano.

### 🧑 Vos  <small>2026-09-11 22:37</small>

@"/home/matiigonzz/Descargas/DaVinci_Resolve_21.1_Linux.zip"
instalalo

### 🤖 Claude  <small>2026-09-11 22:37</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-09-11 22:37</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-11 22:37</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-09-11 22:37</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-11 22:38</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-09-11 22:38</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-11 22:38</small>

_[usó herramienta: Bash]_

### 🧑 Vos  <small>2026-09-11 22:39</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-11 22:39</small>

No puedo ejecutar `sudo` directamente (requiere tu contraseña y no hay terminal interactiva). Ya dejé todo preparado y te armé un script único que hace la instalación completa.

Lo que ya hice sin permisos:

### 🤖 Claude  <small>2026-09-11 22:39</small>

_[usó herramienta: Write]_

### 🧑 Vos  <small>2026-09-11 22:39</small>

_[resultado de herramienta]_

### 🤖 Claude  <small>2026-09-11 22:39</small>

Ya verifiqué el ZIP (íntegro), lo descomprimí en `Descargas/resolve-install/` y dejé el `.run` ejecutable.

**Ahora corré esto en una terminal** (te va a pedir tu contraseña):

```bash
sudo bash /home/matiigonzz/Descargas/resolve-install/instalar-resolve.sh
```

En el paso 3 se abre una ventana gráfica del instalador: Next → aceptar licencia → Install.

---

**Antes de que lo corras, tenés que saber una cosa sobre tu hardware.**

Tu GPU es una **AMD Barcelo** — la gráfica integrada de un Ryzen serie 5000. Esto es un problema real con Resolve, no un detalle menor:

- Resolve **exige OpenCL** para procesar. Tu sistema ahora mismo **no tiene ningún driver OpenCL instalado** (`/etc/OpenCL/vendors/` ni siquiera existe). Por eso el script instala `rocm-opencl`.
- ROCm **no soporta oficialmente** las iGPU Vega como la tuya. El workaround es la variable `HSA_OVERRIDE_GFX_VERSION=9.0.0`, que funciona en muchos casos pero no está garantizado.
- Tenés **15 GB de RAM compartidos con la iGPU** y ahora mismo solo **6 GB disponibles**. Resolve es pesado; incluso si arranca, esperá 1080p con timeline entrecortada, no 4K.

Traducción: hay una probabilidad concreta de que tire *"Unsupported GPU processing mode"* y no abra. El script instala todo lo necesario para darle la mejor chance, y el paso 4 aplica el fix de librerías de glib que en Fedora causa pantalla negra.

**Si al abrir falla**, pegame el error y lo resolvemos — el primer intento sería:

```bash
HSA_OVERRIDE_GFX_VERSION=9.0.0 /opt/resolve/bin/resolve
```

Y si Resolve termina no siendo viable en esta máquina, **Kdenlive** o **Shotcut** son alternativas que andan bien con gráficos integrados. Decime cómo te fue y seguimos.
