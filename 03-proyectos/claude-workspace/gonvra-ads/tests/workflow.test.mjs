import assert from 'node:assert/strict';
import {readFile, stat} from 'node:fs/promises';
import path from 'node:path';
import test from 'node:test';

const projectRoot = path.resolve(import.meta.dirname, '..');

const videos = [
  'Anuncio-Gancho',
  'Anuncio-Problema',
  'Anuncio-Producto',
  'Anuncio-Demo',
];

const carousels = [
  'Carrusel-Problema',
  'Carrusel-Comparativa',
  'Carrusel-Como-Se-Usa',
];

const readPngSize = async (file) => {
  const buffer = await readFile(file);
  const pngSignature = '89504e470d0a1a0a';

  assert.equal(buffer.subarray(0, 8).toString('hex'), pngSignature, `${file} no es PNG`);

  return {
    width: buffer.readUInt32BE(16),
    height: buffer.readUInt32BE(20),
  };
};

test('exporta los cuatro videos MP4 del workflow', async () => {
  for (const id of videos) {
    const file = path.join(projectRoot, 'out', 'videos', `${id}.mp4`);
    const info = await stat(file);
    const header = await readFile(file);

    assert.ok(info.size > 250_000, `${file} parece incompleto`);
    assert.equal(header.subarray(4, 8).toString('ascii'), 'ftyp', `${file} no es MP4`);
  }
});

test('exporta tres carruseles de cinco placas 1080x1920', async () => {
  for (const id of carousels) {
    for (let slide = 1; slide <= 5; slide += 1) {
      const file = path.join(
        projectRoot,
        'out',
        'carruseles',
        id,
        `${String(slide).padStart(2, '0')}.png`,
      );
      const dimensions = await readPngSize(file);

      assert.deepEqual(dimensions, {width: 1080, height: 1920}, `${file} tiene dimensiones incorrectas`);
    }
  }
});

