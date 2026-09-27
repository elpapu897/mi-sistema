<#
=============================================================================
  RESTAURAR  —  Windows nativo (PowerShell)

  Para TomexOS / Windows 10 LTSC sin WSL. Lee scripts/MAPA.tsv, el mismo mapa
  que usa la versión de Linux, así las dos no se desincronizan nunca.

  Uso:
    powershell -ExecutionPolicy Bypass -File scripts\restaurar.ps1 -DryRun
    powershell -ExecutionPolicy Bypass -File scripts\restaurar.ps1
    powershell -ExecutionPolicy Bypass -File scripts\restaurar.ps1 -Solo ic,pr

  Categorías: ic=irremplazable pr=proyectos ng=negocio md=media hi=historial

  OJO: los symlinks necesitan Modo Desarrollador activo o PowerShell como
  administrador. Si no, las 1067 skills quedan como archivos de texto con una
  ruta adentro en vez de enlaces. El script avisa si eso pasa.
=============================================================================
#>
param(
  [switch]$DryRun,
  [string[]]$Solo = @('ic','pr','ng','md','hi')
)

$ErrorActionPreference = 'Stop'
$Repo  = Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Path)
$Mapa  = Join-Path $Repo 'scripts\MAPA.tsv'
$Home_ = $env:USERPROFILE
$Sello = Get-Date -Format 'yyyyMMdd-HHmmss'

if (-not (Test-Path $Mapa)) { Write-Host "Falta $Mapa" -ForegroundColor Red; exit 1 }

function Peso($ruta) {
  try {
    $b = (Get-ChildItem $ruta -Recurse -File -ErrorAction SilentlyContinue |
          Measure-Object -Property Length -Sum).Sum
    if (-not $b) { return '0' }
    foreach ($u in 'B','KB','MB','GB') {
      if ($b -lt 1024) { return ('{0:N0}{1}' -f $b, $u) }
      $b = $b / 1024
    }
    return ('{0:N1}TB' -f $b)
  } catch { return '?' }
}

Write-Host ''
Write-Host '  +------------------------------------------------------------+' -ForegroundColor Cyan
Write-Host '  |  RESTAURACION DEL SISTEMA                                  |' -ForegroundColor Cyan
Write-Host '  +------------------------------------------------------------+' -ForegroundColor Cyan
Write-Host "  Origen : $Repo"
Write-Host "  Destino: $Home_"
if ($DryRun) { Write-Host '  MODO SIMULACION - no se escribe nada' -ForegroundColor Yellow }
Write-Host ''

# --- ¿Bajaron los archivos de LFS o son punteros? -------------------------
$media = Join-Path $Repo '05-media'
if (Test-Path $media) {
  $m = Get-ChildItem $media -Recurse -Include *.mp4,*.mov -File -ErrorAction SilentlyContinue |
       Select-Object -First 1
  if ($m -and $m.Length -lt 1000) {
    Write-Host '  AVISO: los videos son punteros de LFS, no archivos reales.' -ForegroundColor Yellow
    Write-Host '  Corre esto antes de seguir:  git lfs install; git lfs pull' -ForegroundColor Yellow
    Write-Host ''
  }
}

$total = 0; $saltados = 0
foreach ($linea in Get-Content $Mapa) {
  if ([string]::IsNullOrWhiteSpace($linea)) { continue }
  $p = $linea -split "`t"
  if ($p.Count -lt 3) { continue }
  $cat, $origen, $destino = $p[0], $p[1], $p[2]
  $desc = if ($p.Count -ge 4) { $p[3] } else { '' }

  if ($Solo -notcontains $cat) { continue }

  $src = Join-Path $Repo ($origen -replace '/','\')
  $dst = Join-Path $Home_ ($destino -replace '/','\')

  if (-not (Test-Path $src)) {
    Write-Host ("  [ ] {0,-34} no esta en el repo" -f $origen) -ForegroundColor DarkGray
    $saltados++; continue
  }

  Write-Host ("  [{0}] {1,-30} -> ~\{2,-26} {3,7}" -f $cat.ToUpper(), $origen, $destino, (Peso $src)) -ForegroundColor Green
  if ($desc) { Write-Host ("       {0}" -f $desc) -ForegroundColor DarkGray }

  if (-not $DryRun) {
    if (Test-Path $dst) {
      Move-Item $dst "$dst.previo-$Sello" -Force
      Write-Host ("       (lo que habia quedo en {0}.previo-{1})" -f $destino, $Sello) -ForegroundColor DarkGray
    }
    $padre = Split-Path -Parent $dst
    if (-not (Test-Path $padre)) { New-Item -ItemType Directory -Path $padre -Force | Out-Null }
    Copy-Item $src $dst -Recurse -Force
  }
  $total++
}

Write-Host ''
Write-Host "  Restauradas: $total   Omitidas: $saltados"
Write-Host ''

if ($DryRun) {
  Write-Host '  Era una simulacion. Para hacerlo de verdad, corre sin -DryRun.'
  Write-Host ''
  exit 0
}

# --- Symlinks: probamos si Windows nos deja crearlos ----------------------
Write-Host '  -- Symlinks -------------------------------------------------'
$prueba = Join-Path $env:TEMP "symtest-$Sello"
$puede = $false
try {
  New-Item -ItemType SymbolicLink -Path $prueba -Target $Home_ -ErrorAction Stop | Out-Null
  Remove-Item $prueba -Force; $puede = $true
} catch { $puede = $false }

if (-not $puede) {
  Write-Host '  Windows no te deja crear symlinks todavia.' -ForegroundColor Yellow
  Write-Host '  Activa Modo Desarrollador (Configuracion > Privacidad y seguridad >' -ForegroundColor Yellow
  Write-Host '  Para desarrolladores) o abri PowerShell como administrador, y volve' -ForegroundColor Yellow
  Write-Host '  a correr este script. Sin eso, las 1067 skills no van a funcionar.' -ForegroundColor Yellow
} else {
  $symMapa = Join-Path $Repo 'scripts\SYMLINKS.tsv'
  $hechos = 0
  if (Test-Path $symMapa) {
    foreach ($l in Get-Content $symMapa) {
      if ([string]::IsNullOrWhiteSpace($l)) { continue }
      $q = $l -split "`t"; if ($q.Count -lt 2) { continue }
      $ruta, $target = $q[0], $q[1]

      $enlace = switch -Wildcard ($ruta) {
        '01-segundo-cerebro/*'       { Join-Path $Home_ ('OBSIDIAN\'  + ($ruta -replace '^01-segundo-cerebro/','')) }
        '02-agentes/claude/*'        { Join-Path $Home_ ('.claude\'   + ($ruta -replace '^02-agentes/claude/','')) }
        '02-agentes/agents-skills/*' { Join-Path $Home_ ('.agents\'   + ($ruta -replace '^02-agentes/agents-skills/','')) }
        '02-agentes/codex/*'         { Join-Path $Home_ ('.codex\'    + ($ruta -replace '^02-agentes/codex/','')) }
        '02-agentes/hermes/*'        { Join-Path $Home_ ('.hermes\'   + ($ruta -replace '^02-agentes/hermes/','')) }
        default { $null }
      }
      if (-not $enlace) { continue }
      $enlace = $enlace -replace '/','\'
      $target = ($target -replace '\$HOME', $Home_) -replace '/','\'

      try {
        $padre = Split-Path -Parent $enlace
        if (-not (Test-Path $padre)) { New-Item -ItemType Directory -Path $padre -Force | Out-Null }
        if (Test-Path $enlace) { Remove-Item $enlace -Recurse -Force }
        New-Item -ItemType SymbolicLink -Path $enlace -Target $target -ErrorAction Stop | Out-Null
        $hechos++
      } catch { }
    }
  }
  Write-Host "  Symlinks creados: $hechos" -ForegroundColor Green
}

Write-Host ''
Write-Host '  -- Siguientes pasos -----------------------------------------'
Write-Host ''
Write-Host '  1) Repos de terceros (necesita git):'
Write-Host '         bash scripts/reclonar-terceros.sh'
Write-Host '     (sin bash, cloná a mano desde 03-proyectos\REPOS-EXTERNOS.md)'
Write-Host ''
Write-Host '  2) Credenciales (necesita gpg - instala Gpg4win):'
Write-Host '         bash scripts/descifrar-secretos.sh'
Write-Host ''
Write-Host '  3) Dependencias:'
Write-Host '         cd ~\g ; npm install'
Write-Host ''
Write-Host "  Lo que habia antes quedo con sufijo .previo-$Sello" -ForegroundColor DarkGray
Write-Host ''
