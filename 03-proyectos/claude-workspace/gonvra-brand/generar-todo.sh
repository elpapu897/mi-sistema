#!/usr/bin/env bash
# GONVRA · genera TODAS las imágenes que faltan, de una.
# Requisito: tener crédito en Replicate (o cuota en Gemini).
#   Replicate:  https://replicate.com/account/billing   (con US$5 sobra)
# Uso:  bash ~/Claude/gonvra-brand/generar-todo.sh
set -u

source /home/matiigonzz/.replicate-env
G="/home/matiigonzz/Claude/scripts/genimage-replicate.py"
REF="/home/matiigonzz/Claude/product-assets/rasuradora-integral-hero-v1.png"
OUT="/home/matiigonzz/Claude/gonvra-brand/nuevas"
mkdir -p "$OUT"

gen () {  # gen <archivo> <ratio> <prompt>
  if [ -s "$OUT/$1" ]; then echo "── $1 (ya estaba, salteo)"; return; fi
  echo "── $1"
  python3 "$G" --model nano-banana --prompt "$3" --output "$OUT/$1" --images "$REF" --aspect-ratio "$2" 2>&1 | tail -2
  sleep 3
}

COMUN="Keep the device identical to the reference image: rounded teardrop matte black body, lime-green power button inside an oval recess, wide stainless steel foil head with lime-green frame. No text, no logos, no brand marks, no watermark."

# ── 1 y 2 · ANTES y DESPUÉS de zona íntima (mismo encuadre) ────────────────
BASE_AD="Vertical close-up photograph of a man's lower abdomen and bikini line, cropped from the navel to the top of grey cotton boxer briefs, fixed camera angle from above. Clean modern bathroom, soft natural window light from the left, blurred background. The shaver from the reference image rests on the skin at the edge of the frame. Tasteful, clinical, non-explicit grooming-brand photography. Healthy skin, no redness, no blemishes. $COMUN"
gen "gv-antes.jpg"   "4:5" "$BASE_AD The skin shows natural, dense body hair."
gen "gv-despues.jpg" "4:5" "$BASE_AD The skin is evenly trimmed, short and uniform."

# ── 3, 4 y 5 · CORTE DISPAREJO vs PAREJO (para el carrusel) ────────────────
BASE_CP="Vertical split-screen comparison photograph of the same ZONA, same lighting, same camera angle on both halves. LEFT HALF: the hair is cut unevenly, with visible patches, steps and uneven lengths, like a rushed job with a cheap trimmer. RIGHT HALF: the hair is cut perfectly even at a uniform short length, neat and clean. Clean modern bathroom, soft natural window light, realistic skin texture, no redness, no irritation, no blemishes. Documentary product-comparison photography. No text, no logos, no watermark."
gen "gv-comparacion-1.jpg" "4:5" "${BASE_CP/ZONA/man's chest}"
gen "gv-comparacion-2.jpg" "4:5" "${BASE_CP/ZONA/man's lower abdomen and bikini line}"
gen "gv-comparacion-3.jpg" "4:5" "${BASE_CP/ZONA/man's forearm}"

# ── 6 · ABDOMINALES ────────────────────────────────────────────────────────
gen "gv-abdomen.jpg" "9:16" "Vertical photograph of a fit man in his late twenties in a bright modern bathroom, shirtless, running the shaver from the reference image down his lower abdomen, seen from a slight side angle. The wide steel foil head lies FLAT against the skin, black body pointing DOWN in his hand. Natural warm window light, blurred background, realistic skin texture. $COMUN"

# ── 7 · EL DEDO SOBRE EL CABEZAL (demo de seguridad) ───────────────────────
gen "gv-dedo-cabezal.jpg" "9:16" "Vertical macro photograph of a man's index finger pressing flat and sliding across the wide stainless steel foil head of the shaver from the reference image, held in his other hand. The finger is unharmed, skin intact. Shallow depth of field, soft studio light with a highlight on the perforated steel mesh, dark neutral background. $COMUN"

# ── 8 · HOJA vs LÁMINA (el mecanismo, sin prometer nada) ───────────────────
gen "gv-hoja-vs-lamina.jpg" "4:5" "Vertical split-screen macro photograph, same forearm, same lighting, same angle on both halves. LEFT HALF: a plain metal razor blade edge pressed directly against the skin, no guard between the blade and the skin. RIGHT HALF: the shaver from the reference image with its stainless steel foil head resting flat on the skin, the perforated steel mesh clearly visible between the blade and the skin. Clean neutral bathroom light, healthy unmarked skin on both halves, no redness, no blood. Technical product-comparison photography. $COMUN"

echo
echo "════════════════════════════════════════════"
echo "Listo. Quedaron en: $OUT"
ls -la "$OUT"
echo
echo "Ahora avisale a Claude y las instala en la tienda."
