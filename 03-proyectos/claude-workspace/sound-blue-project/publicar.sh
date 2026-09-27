#!/usr/bin/env bash
# =============================================================
#  Sound Blue Project — dejar la página lista para publicar
# =============================================================
#  Prepara dos caminos y te dice cuál conviene:
#    A) Netlify Drop  → arrastrás el ZIP, sin instalar nada
#    B) GitHub Pages  → si querés que quede en tu cuenta de GitHub
# =============================================================
set -euo pipefail
cd "$(dirname "$0")"

ZIP="sound-blue-project.zip"

echo ""
echo "  ██  SOUND BLUE PROJECT — publicar"
echo "  ═══════════════════════════════════════════════════════"

# ---------- 1. ZIP para arrastrar ----------
# `-FS` sincroniza el ZIP: incorpora archivos nuevos y elimina del paquete
# los que ya no están. Por eso video, STL y documentos se suben siempre.
zip -FSrq "$ZIP" index.html assets \
    -x "*.git*" "_*" "*.zip" "qr-*.png"

requeridos=(
  "index.html"
  "assets/modelo.stl"
  "assets/video/video-proyecto.webm"
  "assets/video/video-proyecto.mp4"
  "assets/documentos/Resumen_General_Sound_Blue.pdf"
  "assets/documentos/Proyecto_Autismo_El_Oso_Milo_y_Palco_Sensorial.docx"
)
contenido_zip="$(unzip -Z1 "$ZIP")"
for archivo in "${requeridos[@]}"; do
  if ! grep -Fxq "$archivo" <<<"$contenido_zip"; then
    echo "  ✘ Falta en el ZIP: $archivo" >&2
    exit 1
  fi
done
echo ""
echo "  ✔ ZIP listo:  $(pwd)/$ZIP  ($(du -h "$ZIP" | cut -f1))"
echo "  ✔ Incluye página, imágenes, video, modelo 3D y documentos"

# ---------- 2. repo git ----------
if [ ! -d .git ]; then
  git init -q
  cat > .gitignore <<'EOF'
*.zip
qr-*.png
__pycache__/
EOF
  git add -A
  git -c user.email="sound.blue@escuela" -c user.name="Sound Blue Project" \
      commit -qm "Sound Blue Project — página de presentación"
  echo "  ✔ Repositorio git inicializado y con el primer commit"
else
  echo "  · Ya existe un repositorio git acá (no lo toco)"
fi

cat <<'TXT'

  ═══════════════════════════════════════════════════════
  OPCIÓN A — Netlify Drop  (la más rápida, 1 minuto)
  ═══════════════════════════════════════════════════════
   1. Entrá a  https://app.netlify.com/drop
   2. Arrastrá el archivo  sound-blue-project.zip  a la ventana
   3. Te da una dirección tipo  https://algo-random.netlify.app
   4. (Opcional) Con una cuenta gratis podés cambiarle el nombre
      a algo como  sound-blue-project.netlify.app

   El ZIP ya lleva todo lo que usa la página: el video, el modelo 3D,
   las imágenes y los documentos. No subas los archivos por separado.

  ═══════════════════════════════════════════════════════
  OPCIÓN B — GitHub Pages  (queda en tu cuenta)
  ═══════════════════════════════════════════════════════
   1. Creá un repo vacío en  https://github.com/new
      Nombre sugerido:  sound-blue-project   (público)
   2. Copiá y pegá acá abajo, cambiando TU-USUARIO:

        git remote add origin https://github.com/TU-USUARIO/sound-blue-project.git
        git branch -M main
        git push -u origin main

   3. En el repo:  Settings → Pages → Branch: main / (root) → Save
   4. A los 2 minutos queda en:
        https://TU-USUARIO.github.io/sound-blue-project/

  ═══════════════════════════════════════════════════════
  DESPUÉS DE PUBLICAR — el QR para el stand
  ═══════════════════════════════════════════════════════
        python3 hacer-qr.py https://LA-DIRECCION-QUE-TE-DIERON/

   Genera  qr-sound-blue.png  a 300 dpi, listo para imprimir.

TXT
