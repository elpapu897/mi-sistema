#!/usr/bin/env bash
# =============================================================================
#  CIFRAR SECRETOS  —  corré esto VOS, en tu terminal.
#
#  Junta tus credenciales, las mete en un .tar y lo cifra con AES-256 usando
#  una passphrase que escribís vos. El .tar sin cifrar se destruye al final.
#  Nadie más que vos conoce la passphrase: no queda en ningún chat ni archivo.
#
#  Uso:  bash scripts/cifrar-secretos.sh
# =============================================================================
set -euo pipefail

REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
DEST="$REPO/99-secretos/secretos.tar.gpg"
STAGE="$(mktemp -d)"
trap 'rm -rf "$STAGE"' EXIT

echo
echo "  CIFRADO DE SECRETOS"
echo "  ==================="
echo

# --- Qué se guarda: origen -> nombre dentro del paquete -------------------
copiar() {
  local src="$1" dst="$2"
  if [ -e "$HOME/$src" ]; then
    mkdir -p "$STAGE/$(dirname "$dst")"
    cp -a "$HOME/$src" "$STAGE/$dst"
    printf '  [+] %s\n' "$src"
    echo "$dst" >> "$STAGE/.lista"
  else
    printf '  [ ] %s  (no existe, se omite)\n' "$src"
  fi
}

echo "Juntando credenciales:"
# Claves SSH (las privadas son lo más crítico de todo el backup)
copiar ".ssh/gonvra_server"          "ssh/gonvra_server"
copiar ".ssh/gonvra_server.pub"      "ssh/gonvra_server.pub"
copiar ".ssh/gonvra_vps"             "ssh/gonvra_vps"
copiar ".ssh/gonvra_vps.pub"         "ssh/gonvra_vps.pub"
copiar ".ssh/config"                 "ssh/config"
copiar ".ssh/known_hosts"            "ssh/known_hosts"
# Tokens de agentes
copiar ".claude/.credentials.json"   "claude/.credentials.json"
copiar ".claude/.env"                "claude/.env"
copiar ".codex/auth.json"            "codex/auth.json"
copiar ".hermes/.env"                "hermes/.env"
copiar ".hermes/auth.json"           "hermes/auth.json"
copiar ".gemini/oauth_creds.json"    "gemini/oauth_creds.json"
# Otros
copiar ".npmrc"                      "otros/.npmrc"
copiar ".git-credentials"            "otros/.git-credentials"
copiar ".netrc"                      "otros/.netrc"

# Claves de sesión de Claude (varias, con nombre aleatorio)
if compgen -G "$HOME/.claude/sessions/*.key" > /dev/null; then
  mkdir -p "$STAGE/claude/sessions"
  cp -a "$HOME"/.claude/sessions/*.key "$STAGE/claude/sessions/"
  printf '  [+] .claude/sessions/*.key (%s archivos)\n' \
    "$(ls "$HOME"/.claude/sessions/*.key | wc -l)"
fi

N=$(find "$STAGE" -type f ! -name .lista | wc -l)
if [ "$N" -eq 0 ]; then
  echo; echo "  No se encontró ningún secreto. Nada que cifrar."; exit 1
fi

echo
echo "  $N archivos listos. Peso: $(du -sh "$STAGE" | cut -f1)"
echo

# --- Cifrado --------------------------------------------------------------
mkdir -p "$(dirname "$DEST")"
TAR="$STAGE/../secretos-$$.tar"
tar cf "$TAR" -C "$STAGE" --exclude=.lista .

echo "  Ahora elegí una passphrase. Anotala en tu gestor de contraseñas:"
echo "  SIN ELLA ESTE PAQUETE ES IRRECUPERABLE. No hay forma de resetearla."
echo
gpg --batch --yes --symmetric --cipher-algo AES256 \
    --s2k-mode 3 --s2k-count 65011712 --s2k-digest-algo SHA512 \
    -o "$DEST" "$TAR"

# Destruir el .tar en claro
command -v shred >/dev/null && shred -u "$TAR" 2>/dev/null || rm -f "$TAR"

echo
echo "  LISTO -> ${DEST/#$HOME/~}"
echo "  Tamaño cifrado: $(du -h "$DEST" | cut -f1)"
echo
echo "  Verificá que se puede abrir ANTES de confiar en él:"
echo "      gpg -d '$DEST' | tar t | head"
echo
