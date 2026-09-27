import { Composition } from 'remotion';
import { Anuncio } from './Anuncio';
import { anuncios } from './guiones';
import { Carrusel } from './Carrusel';
import { carruseles } from './carruseles';
import { Kinetico, TresPasos, Packs } from './Motion';
import { Manifiesto, Ritual, Oferta } from './Cine';

export const RemotionRoot: React.FC = () => {
  return (
    <>
      {anuncios.map((a) => (
        <Composition
          key={a.id}
          id={a.id}
          component={Anuncio}
          durationInFrames={a.escenas.reduce((total, e) => total + e.frames, 0) + 75}
          fps={30}
          width={1080}
          height={1920}
          defaultProps={{ escenas: a.escenas, cierre: a.cierre }}
        />
      ))}

      {carruseles.map((c) => (
        <Composition
          key={c.id}
          id={c.id}
          component={Carrusel}
          durationInFrames={c.slides.length}
          fps={1}
          width={1080}
          height={c.formato === 'instagram' ? 1350 : 1920}
          defaultProps={{ slides: c.slides }}
        />
      ))}
      <Composition id="Cine-Manifiesto" component={Manifiesto} durationInFrames={414} fps={30} width={1080} height={1920} />
      <Composition id="Cine-Ritual" component={Ritual} durationInFrames={426} fps={30} width={1080} height={1920} />
      <Composition id="Cine-Oferta" component={Oferta} durationInFrames={200} fps={30} width={1080} height={1920} />
      <Composition id="Motion-Kinetico" component={Kinetico} durationInFrames={270} fps={30} width={1080} height={1920} />
      <Composition id="Motion-TresPasos" component={TresPasos} durationInFrames={470} fps={30} width={1080} height={1920} />
      <Composition id="Motion-Packs" component={Packs} durationInFrames={270} fps={30} width={1080} height={1920} />
    </>
  );
};
