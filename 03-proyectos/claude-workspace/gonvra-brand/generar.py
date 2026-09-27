#!/usr/bin/env python3
"""GONVRA · genera las imágenes que faltan. Saltea las que ya existen.
Uso:  python3 ~/Claude/gonvra-brand/generar.py
"""
import os, subprocess, sys, time

BASE = '/home/matiigonzz/Claude'
G = f'{BASE}/scripts/genimage-replicate.py'
REF = f'{BASE}/product-assets/rasuradora-integral-hero-v1.png'
OUT = f'{BASE}/gonvra-brand/nuevas'
os.makedirs(OUT, exist_ok=True)

COMUN = ("Keep the device identical to the reference image: rounded teardrop matte black body, "
         "lime-green power button inside an oval recess, wide stainless steel foil head with "
         "lime-green frame. No text, no logos, no brand marks, no watermark.")

AD = ("Vertical close-up photograph of the lower abdomen and bikini line of an adult man, cropped "
      "from the navel to the waistband of grey cotton boxer briefs, fixed camera angle from above. "
      "Clean modern bathroom, soft natural window light from the left, blurred background. The shaver "
      "from the reference image rests on the skin at the edge of the frame. Tasteful, clinical, "
      "non-explicit grooming-brand photography. Healthy skin, no redness, no blemishes. " + COMUN)

def comp(zona):
    return ("Vertical split-screen comparison photograph of the same " + zona + ", identical lighting "
            "and identical camera angle on both halves. LEFT HALF: the body hair is trimmed unevenly, "
            "with visible patches, steps and uneven lengths, like a rushed job with a worn out trimmer. "
            "RIGHT HALF: the body hair is trimmed perfectly even at a uniform short length, neat and "
            "clean. Clean modern bathroom, soft natural window light, realistic skin texture, healthy "
            "skin, no redness, no irritation, no blemishes. Documentary product-comparison photography. "
            "No text, no logos, no watermark.")

TAREAS = [
    ('gv-antes.jpg',           '4:5',  AD + ' The skin shows natural, dense body hair.'),
    ('gv-despues.jpg',         '4:5',  AD + ' The skin is evenly trimmed, short and uniform.'),
    ('gv-comparacion-1.jpg',   '4:5',  comp('adult male chest')),
    ('gv-comparacion-2.jpg',   '4:5',  comp('adult male lower abdomen')),
    ('gv-comparacion-3.jpg',   '4:5',  comp('adult male forearm')),
    ('gv-abdomen.jpg',         '9:16',
     "Vertical photograph of a fit adult man in a bright modern bathroom, shirtless, running the shaver "
     "from the reference image down his lower abdomen, seen from a slight side angle. The wide steel foil "
     "head lies FLAT against the skin, black body pointing DOWN in his hand. Natural warm window light, "
     "blurred background, realistic skin texture. " + COMUN),
    ('gv-dedo-cabezal.jpg',    '9:16',
     "Vertical macro photograph of an adult index finger pressing flat and sliding across the wide "
     "stainless steel foil head of the shaver from the reference image, held in the other hand. The finger "
     "is unharmed, skin intact. Shallow depth of field, soft studio light with a highlight on the "
     "perforated steel mesh, dark neutral background. " + COMUN),
    ('gv-hoja-vs-lamina.jpg',  '4:5',
     "Vertical split-screen macro photograph, same forearm, identical lighting, identical angle on both "
     "halves. LEFT HALF: a plain metal razor blade edge pressed directly against the skin, no guard "
     "between the blade and the skin. RIGHT HALF: the shaver from the reference image with its stainless "
     "steel foil head resting flat on the skin, the perforated steel mesh clearly visible between the "
     "blade and the skin. Clean neutral bathroom light, healthy unmarked skin on both halves, no redness, "
     "no blood. Technical product-comparison photography. " + COMUN),
]

def generar(archivo, ratio, prompt, intento=1):
    destino = f'{OUT}/{archivo}'
    if os.path.exists(destino) and os.path.getsize(destino) > 5000:
        print(f'── {archivo}  (ya estaba)')
        return True
    print(f'── {archivo}  (intento {intento})', flush=True)
    r = subprocess.run(
        ['python3', G, '--model', 'nano-banana', '--prompt', prompt,
         '--output', destino, '--images', REF, '--aspect-ratio', ratio],
        capture_output=True, text=True, timeout=300)
    ok = os.path.exists(destino) and os.path.getsize(destino) > 5000
    if not ok:
        cola = (r.stdout + r.stderr).strip().splitlines()
        print('   ✗', cola[-1][:120] if cola else 'sin salida')
        if intento < 3:
            time.sleep(6)
            return generar(archivo, ratio, prompt, intento + 1)
        return False
    print(f'   ✓ {os.path.getsize(destino)//1024} KB')
    time.sleep(3)
    return True

if __name__ == '__main__':
    hechas, fallidas = [], []
    for archivo, ratio, prompt in TAREAS:
        (hechas if generar(archivo, ratio, prompt) else fallidas).append(archivo)
    print('\n' + '═' * 44)
    print(f'Listas: {len(hechas)}/{len(TAREAS)}')
    if fallidas:
        print('No salieron:', ', '.join(fallidas))
    print('Carpeta:', OUT)
