#!/usr/bin/env bash
# =============================================================================
#  SUBIR A GITHUB
#
#  Crea el repo privado y empuja en etapas, de lo más importante a lo más
#  reemplazable. Así el segundo cerebro queda a salvo en los primeros minutos,
#  y si el push de los 24,85 GB de video se corta a la hora 2, no arrastra nada
#  crítico con él.
#
#  Uso:  bash scripts/subir.sh [nombre-del-repo]
# =============================================================================
set -uo pipefail

export PATH="$HOME/.local/bin:$PATH"
REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
NOMBRE="${1:-mi-sistema}"
cd "$REPO_DIR"

echo
echo "  ┌────────────────────────────────────────────────────────────┐"
echo "  │  SUBIDA A GITHUB                                           │"
echo "  └────────────────────────────────────────────────────────────┘"
echo

# --- 1. Autenticación -----------------------------------------------------
if ! gh auth status >/dev/null 2>&1; then
  echo "  No estás autenticado. Corré primero:"
  echo
  echo "      gh auth login"
  echo
  echo "  Elegí: GitHub.com -> HTTPS -> Login with a web browser"
  exit 1
fi

USUARIO="$(gh api user --jq .login 2>/dev/null)"
[ -z "$USUARIO" ] && { echo "  No pude leer tu usuario de GitHub."; exit 1; }
echo "  Usuario: $USUARIO"

# --- 2. Identidad de git --------------------------------------------------
EMAIL="$(gh api user --jq '.email // empty' 2>/dev/null)"
[ -z "$EMAIL" ] && EMAIL="${USUARIO}@users.noreply.github.com"
git config user.name  "$USUARIO"
git config user.email "$EMAIL"
echo "  Identidad: $USUARIO <$EMAIL>"

# --- 3. Crear el repo (privado) ------------------------------------------
if gh repo view "$USUARIO/$NOMBRE" >/dev/null 2>&1; then
  echo "  El repo $USUARIO/$NOMBRE ya existe, lo reuso."
else
  echo "  Creando $USUARIO/$NOMBRE (privado)..."
  gh repo create "$NOMBRE" --private \
    --description "Respaldo completo de mi maquina de trabajo: segundo cerebro, agentes, 1235 skills, codigo y media. Fedora 44 -> TomexOS 10." \
    >/dev/null || { echo "  Fallo la creacion del repo."; exit 1; }
fi

URL="https://github.com/$USUARIO/$NOMBRE.git"
git remote remove origin 2>/dev/null
git remote add origin "$URL"
echo "  Remote: $URL"

# --- 4. Poner la URL real en la documentación ----------------------------
if grep -q 'github.com/USUARIO/' README.md 2>/dev/null; then
  sed -i "s|github.com/USUARIO/mi-sistema|github.com/$USUARIO/$NOMBRE|g" README.md RESTAURAR.md
  git add README.md RESTAURAR.md
  git commit -q -m "Poner la URL real del repo en la documentacion" 2>/dev/null
  echo "  URLs de la documentacion actualizadas."
fi

# --- 5. Push por etapas ---------------------------------------------------
echo
echo "  -- Subiendo en etapas ---------------------------------------"
echo "  (la ultima etapa son 20 GB por LFS: puede tardar 2 a 3 horas)"
echo

mapfile -t ENTRADAS < <(git log --reverse --format='%H%x09%s')
TOTAL=${#ENTRADAS[@]}
i=0
for entrada in "${ENTRADAS[@]}"; do
  i=$((i+1))
  SHA="${entrada%%$'\t'*}"
  MSG="${entrada#*$'\t'}"
  printf '  [%d/%d] %s\n' "$i" "$TOTAL" "$MSG"
  if git push origin "$SHA:refs/heads/main" 2>&1 | sed 's/^/        /'; then
    echo "        OK"
  else
    echo
    echo "  Fallo en la etapa $i. Lo que ya subio quedo en GitHub."
    echo "  Volve a correr este script: retoma donde quedo."
    exit 1
  fi
done

git push -u origin main 2>&1 | tail -2 | sed 's/^/  /'

echo
echo "  -- Listo ----------------------------------------------------"
echo
echo "  https://github.com/$USUARIO/$NOMBRE"
echo
gh repo view "$USUARIO/$NOMBRE" --json visibility \
  --template '  Visibilidad: {{.visibility}}{{"\n"}}' 2>/dev/null
echo "  Tiene que decir PRIVATE. Si dice PUBLIC, arreglalo ya:"
echo "      gh repo edit $USUARIO/$NOMBRE --visibility private"
echo
