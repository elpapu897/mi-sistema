<div align="center">

# MI SISTEMA

### Respaldo completo de la máquina de trabajo — Fedora 44 → TomexOS 10

**19.046 archivos · 5.555 notas · 1.235 skills · 26,85 GB**

`26,85 GB respaldados` · `100+ GB descartados a propósito` · `0 secretos en claro`

</div>

---

## Qué es esto

El contenido entero de una máquina de trabajo, ordenado para poder reconstruirla
desde cero en otro sistema operativo. No es un volcado: cada carpeta está
clasificada, medida y documentada, y hay scripts probados que la devuelven a su
lugar.

El home original pesaba **113 GB**. Acá hay **26,85 GB**. La diferencia no se
perdió: son `node_modules`, cachés, toolchains y binarios que se regeneran con un
`npm install`. Respaldar eso habría sido copiar 100 GB de cosas descargables.

---

## Empezar

```bash
git clone https://github.com/USUARIO/mi-sistema.git
cd mi-sistema
git lfs install && git lfs pull          # baja los 24,85 GB de video y audio
bash scripts/restaurar.sh --dry-run      # ver qué haría, sin tocar nada
bash scripts/restaurar.sh                # hacerlo de verdad
```

En Windows sin WSL, el paso 3 y 4 son:

```powershell
powershell -ExecutionPolicy Bypass -File scripts\restaurar.ps1 -DryRun
powershell -ExecutionPolicy Bypass -File scripts\restaurar.ps1
```

La guía completa, con los tropiezos específicos de TomexOS, está en
**[RESTAURAR.md](RESTAURAR.md)**.

---

## Qué hay adentro

| | Carpeta | Peso | Archivos | Qué es |
|:--:|---|--:|--:|---|
| 🧠 | **[01-segundo-cerebro](01-segundo-cerebro/)** | 17 MB | 388 | El vault de Obsidian completo: notas, diario, zettelkasten, plugins y config. Lo más chico y lo más valioso. |
| 🤖 | **[02-agentes](02-agentes/)** | 319 MB | 8.858 | Claude Code, Codex, Gemini, Hermes, Kimi, OpenCode. Config, prompts y **1.235 skills**. |
| 💻 | **[03-proyectos](03-proyectos/)** | 2,3 GB | 6.512 | Código propio: la app Next.js, el workspace de Claude, edición Roblox, skills empaquetadas. |
| 🛒 | **[04-negocio-gonvra](04-negocio-gonvra/)** | 476 MB | 2.147 | GONVRA: tiendas, auditorías, landings, backups diarios del tema y pipeline de publicación. |
| 🎬 | **[05-media](05-media/)** | 22 GB | 490 | Video y audio vía Git LFS: el proyecto Planetamati, grabaciones originales, entregables. |
| ⚙️ | **[06-dotfiles](06-dotfiles/)** | 1,5 MB | 220 | `.bashrc`, `.zshrc`, `.tmux.conf`, config de GTK, nvim, autostart. |
| 📜 | **[07-historial-agentes](07-historial-agentes/)** | 1,5 GB | 420 | Historial completo de conversaciones con los agentes, más la auto-memoria. |
| 🔐 | **[99-secretos](99-secretos/)** | — | 1 | Credenciales en un `.tar.gpg` cifrado con AES-256. Sin la passphrase no se abre. |

---

## Cómo se decidió qué entra

```
113 GB en el home original
│
├── 26,85 GB  →  ESTE REPO
│   ├── 2,01 GB   git normal   (17.349 archivos: notas, código, config)
│   └── 24,85 GB  Git LFS      (1.678 archivos: video, audio, logs, bases)
│
└── ~86 GB   →  DESCARTADO A PROPÓSITO
    ├── node_modules, .next, dist, build, target ....... regenerable
    ├── .cache, .npm, .rustup, .cargo, .bun, .deno ..... regenerable
    ├── binarios de agentes (bin/, node/, lsp/) ........ se reinstalan
    ├── 15 repos de terceros .......................... ver abajo
    ├── ISOs, APKs e instaladores (~7 GB) ............. se re-descargan
    └── .venv, __pycache__, logs, telemetría .......... ruido
```

### Los repos que no son míos

15 de los repos de la máquina eran clones de terceros. Subir su código habría
duplicado ~1 GB y creado repos anidados, que en git son un problema. En vez de
eso, **[03-proyectos/REPOS-EXTERNOS.md](03-proyectos/REPOS-EXTERNOS.md)** guarda
la URL y el commit exacto de cada uno, y `scripts/reclonar-terceros.sh` los
reconstruye idénticos.

---

## Las tres trampas que este backup ya resolvió

Un `git push` ingenuo de esta máquina fallaba. Estos son los problemas reales que
aparecieron al armarlo, y cómo quedaron resueltos:

<table>
<tr><th>#</th><th>El problema</th><th>La solución</th></tr>
<tr>
<td><b>1</b></td>
<td>

**1.067 de las 1.139 skills eran symlinks**, no carpetas. Un `cp` ingenuo se
llevaba 72 y parecía haber funcionado. Y en Windows git rompe los symlinks
salvo que tengas Modo Desarrollador activo.

</td>
<td>

La biblioteca real (1.125 skills) se respalda una sola vez en
`02-agentes/agents-skills/`. Los 3.154 enlaces quedan mapeados en
[`scripts/SYMLINKS.tsv`](scripts/SYMLINKS.tsv) con `$HOME` en lugar de rutas
absolutas, y `rehacer-symlinks.sh` los reconstruye sin depender de git.

</td>
</tr>
<tr>
<td><b>2</b></td>
<td>

**69 archivos pasaban los 90 MB**, y dos superaban el límite duro de 100 MB de
GitHub: un log de sesión de 241 MB y una base de 235 MB. El push se habría
caído recién a la hora 2, con todo a medio subir.

</td>
<td>

[`.gitattributes`](.gitattributes) manda 34 tipos de archivo a Git LFS,
incluidos `.jsonl`, `.sqlite` y `.raw` que no son obvios. Verificado con
`git check-attr` sobre los 69 archivos: **cero fugas**.

</td>
</tr>
<tr>
<td><b>3</b></td>
<td>

**6 archivos de credenciales y 2 claves SSH privadas** estaban entre los datos.
En un repo, aunque sea privado, GitHub revoca los tokens que detecta y el VPS
queda expuesto.

</td>
<td>

75 reglas en [`.gitignore`](.gitignore) los bloquean, verificado con
`git check-ignore` uno por uno. Van cifrados con AES-256 en
`99-secretos/secretos.tar.gpg`, con una passphrase que solo conoce su dueño.
El inventario de qué re-autenticar está en [CREDENCIALES.md](CREDENCIALES.md).

</td>
</tr>
</table>

---

## Los scripts

Todos leen la misma fuente de verdad, [`scripts/MAPA.tsv`](scripts/MAPA.tsv), así
que la versión de Linux y la de PowerShell no se pueden desincronizar.

| Script | Qué hace |
|---|---|
| [`restaurar.sh`](scripts/restaurar.sh) | Devuelve cada carpeta a su lugar. Acepta `--dry-run` y `--solo ic,pr`. Nunca sobrescribe: renombra a `.previo-<fecha>`. |
| [`restaurar.ps1`](scripts/restaurar.ps1) | Lo mismo en PowerShell, para Windows sin WSL. Detecta si Windows te deja crear symlinks y avisa si no. |
| [`rehacer-symlinks.sh`](scripts/rehacer-symlinks.sh) | Reconstruye los 3.154 enlaces simbólicos desde el manifiesto. |
| [`reclonar-terceros.sh`](scripts/reclonar-terceros.sh) | Vuelve a clonar los 15 repos externos en su commit exacto. |
| [`cifrar-secretos.sh`](scripts/cifrar-secretos.sh) | Junta las credenciales y las cifra con AES-256. El `.tar` en claro se destruye con `shred`. |
| [`descifrar-secretos.sh`](scripts/descifrar-secretos.sh) | Las devuelve a su lugar con los permisos correctos (600 en las claves SSH, o SSH las rechaza). |

---

## Documentos

| | |
|---|---|
| **[RESTAURAR.md](RESTAURAR.md)** | La guía paso a paso, con los problemas específicos de TomexOS 10 LTSC. |
| **[INVENTARIO.md](INVENTARIO.md)** | Tabla completa origen → destino, con pesos y qué se excluyó de cada carpeta. |
| **[CREDENCIALES.md](CREDENCIALES.md)** | Qué credencial hay, dónde va y cómo re-autenticar si fue revocada. |
| **[03-proyectos/REPOS-EXTERNOS.md](03-proyectos/REPOS-EXTERNOS.md)** | Los 15 repos de terceros con URL y commit. |

---

<div align="center">

**Repo privado.** Contiene notas personales, código de negocio e historial de
conversaciones. El paquete de secretos está cifrado, el resto no.

</div>
