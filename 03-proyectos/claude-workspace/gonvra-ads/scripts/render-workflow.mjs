import {bundle} from '@remotion/bundler';
import {getCompositions, openBrowser, renderMedia, renderStill} from '@remotion/renderer';
import {mkdir} from 'node:fs/promises';
import path from 'node:path';

const projectRoot = path.resolve(import.meta.dirname, '..');
const requestedMode = process.argv[2] ?? 'all';
const validModes = new Set(['all', 'videos', 'carousels']);

if (!validModes.has(requestedMode)) {
  throw new Error(`Modo inválido: ${requestedMode}. Usá all, videos o carousels.`);
}

const wantsVideos = requestedMode === 'all' || requestedMode === 'videos';
const wantsCarousels = requestedMode === 'all' || requestedMode === 'carousels';

const printProgress = (label) => {
  let lastShown = -1;

  return ({progress}) => {
    const percent = Math.floor(progress * 10) * 10;

    if (percent !== lastShown) {
      lastShown = percent;
      process.stdout.write(`${label}: ${percent}%\n`);
    }
  };
};

process.stdout.write('Preparando Remotion…\n');
const serveUrl = await bundle({
  entryPoint: path.join(projectRoot, 'src', 'index.ts'),
  onProgress: (progress) => {
    const percent = Math.round(progress);
    if (percent % 20 === 0) process.stdout.write(`Bundle: ${percent}%\n`);
  },
});

const browser = await openBrowser('chrome', {logLevel: 'warn'});

try {
  const compositions = await getCompositions({serveUrl, puppeteerInstance: browser});
  const videos = compositions.filter(({id}) => id.startsWith('Anuncio-'));
  const carousels = compositions.filter(({id}) => id.startsWith('Carrusel-'));

  if (wantsVideos) {
    const videosDir = path.join(projectRoot, 'out', 'videos');
    await mkdir(videosDir, {recursive: true});

    for (const composition of videos) {
      const outputLocation = path.join(videosDir, `${composition.id}.mp4`);
      process.stdout.write(`\nRenderizando ${composition.id}\n`);
      await renderMedia({
        composition,
        serveUrl,
        puppeteerInstance: browser,
        outputLocation,
        codec: 'h264',
        pixelFormat: 'yuv420p',
        crf: 18,
        muted: true,
        overwrite: true,
        logLevel: 'warn',
        onProgress: printProgress(composition.id),
      });
      process.stdout.write(`Listo: ${path.relative(projectRoot, outputLocation)}\n`);
    }
  }

  if (wantsCarousels) {
    for (const composition of carousels) {
      const carouselDir = path.join(projectRoot, 'out', 'carruseles', composition.id);
      await mkdir(carouselDir, {recursive: true});

      process.stdout.write(`\nExportando ${composition.id}\n`);
      for (let frame = 0; frame < composition.durationInFrames; frame += 1) {
        const output = path.join(carouselDir, `${String(frame + 1).padStart(2, '0')}.png`);
        await renderStill({
          composition,
          serveUrl,
          puppeteerInstance: browser,
          output,
          frame,
          imageFormat: 'png',
          overwrite: true,
          logLevel: 'warn',
        });
        process.stdout.write(`Placa ${frame + 1}/${composition.durationInFrames}\n`);
      }
    }
  }
} finally {
  await browser.close({silent: true});
}

process.stdout.write('\nWorkflow terminado.\n');
