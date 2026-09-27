#!/usr/bin/env bash
# =============================================================================
#  DESCIFRAR SECRETOS  —  en la máquina nueva.
#
#  Abre 99-secretos/secretos.tar.gpg y devuelve cada credencial a su lugar,
#  con los permisos correctos (las claves SSH necesitan 600 o SSH las rechaza).
#
#  Uso:  bash scripts/descifrar-secretos.sh
# =============================================================================
set -euo pipefail

REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SRC="$REPO/99-secretos/secretos.tar.gpg"
STAGE="$(mktemp -d)"
trap 'rm -rf "$STAGE"' EXIT

[ -f "$SRC" ] || { echo "No existe $SRC"; exit 1; }

echo
echo "  RESTAURACIÓN DE SECRETOS"
echo "  ========================"
echo
echo "  Escribí la passphrase que usaste al cifrar:"
gpg -d "$SRC" 2>/dev/null | tar x -C "$STAGE" || {
  echo
  echo "  Passphrase incorrecta o archivo dañado. No se restauró nada."
  exit 1
}

echo
echo "  Paquete abierto. Restaurando:"

restaurar() {
  local src="$1" dst="$2" perm="$3"
  if [ -e "$STAGE/$src" ]; then
    mkdir -p "$(dirname "$HOME/$dst")"
    if [ -e "$HOME/$dst" ]; then
      cp -a "$HOME/$dst" "$HOME/$dst.antes-de-restaurar" 2>/dev/null || true
      printf '  [~] %-36s (el anterior quedó como .antes-de-restaurar)\n' "$dst"
    else
      printf '  [+] %s\n' "$dst"
    fi
    cp -a "$STAGE/$src" "$HOME/$dst"
    chmod "$perm" "$HOME/$dst"
  fi
}

# SSH: 700 el directorio, 600 las privadas, 644 las públicas
mkdir -p "$HOME/.ssh"; chmod 700 "$HOME/.ssh"
restaurar "ssh/gonvra_server"       ".ssh/gonvra_server"       600
restaurar "ssh/gonvra_vps"          ".ssh/gonvra_vps"          600
restaurar "ssh/gonvra_server.pub"   ".ssh/gonvra_server.pub"   644
restaurar "ssh/gonvra_vps.pub"      ".ssh/gonvra_vps.pub"      644
restaurar "ssh/config"              ".ssh/config"              600
restaurar "ssh/known_hosts"         ".ssh/known_hosts"         644

# Tokens de agentes
restaurar "claude/.credentials.json" ".claude/.credentials.json" 600
restaurar "claude/.env"              ".claude/.env"              600
restaurar "codex/auth.json"          ".codex/auth.json"          600
restaurar "hermes/.env"              ".hermes/.env"              600
restaurar "hermes/auth.json"         ".hermes/auth.json"         600
restaurar "gemini/oauth_creds.json"  ".gemini/oauth_creds.json"  600
restaurar "otros/.npmrc"             ".npmrc"                    600
restaurar "otros/.git-credentials"   ".git-credentials"          600
restaurar "otros/.netrc"             ".netrc"                    600

# Claves de sesión de Claude
if [ -d "$STAGE/claude/sessions" ]; then
  mkdir -p "$HOME/.claude/sessions"
  cp -a "$STAGE/claude/sessions/." "$HOME/.claude/sessions/"
  chmod 600 "$HOME"/.claude/sessions/*.key 2>/dev/null || true
  echo "  [+] .claude/sessions/*.key"
fi

echo
echo "  Listo. Probá el acceso al VPS:"
echo "      ssh -i ~/.ssh/gonvra_vps <usuario>@<host>"
echo
echo "  Si algún token fue revocado (pasa cuando cambiás de máquina),"
echo "  mirá CREDENCIALES.md: ahí está qué re-autenticar y cómo."
echo
