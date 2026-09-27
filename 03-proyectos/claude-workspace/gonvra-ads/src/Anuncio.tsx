import React from 'react';
import {
  AbsoluteFill,
  OffthreadVideo,
  Sequence,
  interpolate,
  spring,
  staticFile,
  useCurrentFrame,
  useVideoConfig,
  Img,
} from 'remotion';
import type { Escena, Cierre } from './guiones';

const TINTA = '#101a16';
const LIMA = '#c8e54a';
const PAPEL = '#f7f6f1';
const CIERRE_FRAMES = 75;

const fuente =
  '"Helvetica Neue", Helvetica, "Segoe UI", Inter, system-ui, -apple-system, sans-serif';

/* ---------- Ola animada, igual que la de la web ---------- */
const Ola: React.FC<{ color: string; abajo?: boolean; opacidad?: number }> = ({
  color,
  abajo,
  opacidad = 1,
}) => {
  const frame = useCurrentFrame();
  const x = (frame * 2.4) % 1440;
  return (
    <div
      style={{
        position: 'absolute',
        left: 0,
        right: 0,
        [abajo ? 'bottom' : 'top']: -2,
        height: 150,
        overflow: 'hidden',
        transform: abajo ? 'none' : 'rotate(180deg)',
        opacity: opacidad,
      }}
    >
      <svg
        viewBox="0 0 1440 150"
        preserveAspectRatio="none"
        style={{ width: '100%', height: '100%', display: 'block' }}
      >
        <path
          transform={`translate(${-x} 0)`}
          d="M0,70 q90,-40 180,0 t180,0 t180,0 t180,0 t180,0 t180,0 t180,0 t180,0 t180,0 t180,0 t180,0 t180,0 t180,0 t180,0 t180,0 t180,0 L2880,150 L0,150 Z"
          fill={color}
        />
      </svg>
    </div>
  );
};

/* ---------- Texto que entra por palabras ---------- */
const Titulo: React.FC<{ texto: string; retraso?: number }> = ({ texto, retraso = 0 }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  return (
    <h1
      style={{
        margin: 0,
        fontFamily: fuente,
        fontSize: 86,
        fontWeight: 800,
        lineHeight: 1.02,
        letterSpacing: '-0.035em',
        color: '#fff',
        textShadow: '0 4px 34px rgba(0,0,0,.5)',
        whiteSpace: 'pre-line',
      }}
    >
      {texto.split('\n').map((linea, i) => {
        const s = spring({
          frame: frame - retraso - i * 5,
          fps,
          config: { damping: 200, mass: 0.6 },
        });
        return (
          <span
            key={i}
            style={{
              display: 'block',
              opacity: s,
              transform: `translateY(${(1 - s) * 42}px)`,
            }}
          >
            {linea}
          </span>
        );
      })}
    </h1>
  );
};


/* ---------- Cartel blanco estilo TikTok ---------- */
const Sticker: React.FC<{ texto: string; retraso?: number; abajo?: boolean; giro?: number }> = ({
  texto,
  retraso = 0,
  abajo = false,
  giro = 0,
}) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const s = spring({ frame: frame - retraso, fps, config: { damping: 14, mass: 0.5, stiffness: 180 } });
  if (frame < retraso) return null;
  return (
    <div
      style={{
        alignSelf: 'center',
        maxWidth: 760,
        marginTop: abajo ? 18 : 0,
        padding: '22px 34px',
        borderRadius: 14,
        backgroundColor: 'rgba(255,255,255,.96)',
        boxShadow: '0 10px 40px rgba(0,0,0,.28)',
        fontFamily: fuente,
        fontSize: 58,
        fontWeight: 800,
        lineHeight: 1.12,
        letterSpacing: '-0.02em',
        color: '#111',
        textAlign: 'center',
        whiteSpace: 'pre-line',
        opacity: Math.min(s * 1.4, 1),
        transform: `scale(${0.82 + s * 0.18}) rotate(${giro}deg)`,
      }}
    >
      {texto}
    </div>
  );
};

/* ---------- Una escena ---------- */
const EscenaClip: React.FC<{ escena: Escena; duracion: number }> = ({ escena, duracion }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const entrada = interpolate(frame, [0, 8], [0, 1], { extrapolateRight: 'clamp' });
  const salida = interpolate(frame, [duracion - 8, duracion], [1, 0], {
    extrapolateLeft: 'clamp',
  });
  const base = escena.zoom ?? 1;
  const zoom = interpolate(frame, [0, duracion], [1.06 * base, 1.14 * base]);
  const arriba = escena.posicion === 'arriba';
  const s = spring({ frame: frame - 6, fps, config: { damping: 200 } });

  return (
    <AbsoluteFill style={{ backgroundColor: TINTA, opacity: Math.min(entrada, salida) }}>
      <AbsoluteFill style={{ transform: `scale(${zoom})` }}>
        <OffthreadVideo
          src={staticFile(`clips/${escena.clip}`)}
          startFrom={Math.round(escena.desde * 30)}
          muted
          style={{ width: '100%', height: '100%', objectFit: 'cover' }}
        />
      </AbsoluteFill>

      {/* velo para que el texto se lea */}
      <AbsoluteFill
        style={{
          background: escena.sticker
            ? 'linear-gradient(180deg, rgba(16,26,22,.28) 0%, rgba(16,26,22,0) 38%, rgba(16,26,22,0) 100%)'
            : arriba
            ? 'linear-gradient(180deg, rgba(16,26,22,.82) 0%, rgba(16,26,22,.3) 42%, rgba(16,26,22,.15) 100%)'
            : 'linear-gradient(0deg, rgba(16,26,22,.88) 0%, rgba(16,26,22,.32) 46%, rgba(16,26,22,.05) 100%)',
        }}
      />

      {!escena.sticker && <Ola color={TINTA} abajo={!arriba} opacidad={0.9} />}

      {escena.sticker && (
        <AbsoluteFill style={{ justifyContent: 'flex-start', padding: '260px 60px 0', display: 'flex' }}>
          <Sticker texto={escena.sticker} giro={-1.2} />
          {escena.sticker2 && <Sticker texto={escena.sticker2} retraso={16} abajo giro={1} />}
        </AbsoluteFill>
      )}

      {(escena.titulo || escena.bajada) && (
        <AbsoluteFill
          style={{
            justifyContent: arriba ? 'flex-start' : 'flex-end',
            padding: '150px 170px 300px 80px',
          }}
        >
          <div>
            {escena.titulo && <Titulo texto={escena.titulo} />}
            {escena.bajada && (
              <p
                style={{
                  margin: '26px 0 0',
                  fontFamily: fuente,
                  fontSize: 40,
                  fontWeight: 600,
                  color: LIMA,
                  opacity: s,
                  transform: `translateY(${(1 - s) * 26}px)`,
                }}
              >
                {escena.bajada}
              </p>
            )}
          </div>
        </AbsoluteFill>
      )}
    </AbsoluteFill>
  );
};

/* ---------- Cierre con el pack ---------- */
const Cierre: React.FC<{ cierre: Cierre }> = ({ cierre }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const s = spring({ frame, fps, config: { damping: 200, mass: 0.7 } });
  const sImg = spring({ frame: frame - 6, fps, config: { damping: 200, mass: 0.9 } });

  return (
    <AbsoluteFill
      style={{
        backgroundColor: TINTA,
        alignItems: 'center',
        justifyContent: 'center',
        padding: 80,
      }}
    >
      <Ola color="#16241d" opacidad={0.5} />
      <Ola color="#16241d" abajo opacidad={0.5} />

      <div
        style={{
          width: 720,
          height: 600,
          padding: 26,
          borderRadius: 40,
          backgroundColor: PAPEL,
          boxShadow: '0 40px 90px rgba(0,0,0,.45)',
          opacity: sImg,
          transform: `translateY(${(1 - sImg) * 40}px) scale(${0.94 + sImg * 0.06})`,
        }}
      >
        <Img
          src={staticFile(cierre.imagen)}
          style={{width: '100%', height: '100%', objectFit: 'cover', objectPosition: 'center 48%', borderRadius: 22}}
        />
      </div>

      <h1
        style={{
          margin: '10px 0 0',
          fontFamily: fuente,
          fontSize: 90,
          fontWeight: 800,
          lineHeight: 1.02,
          letterSpacing: '-0.04em',
          color: '#fff',
          textAlign: 'center',
          whiteSpace: 'pre-line',
          opacity: s,
          transform: `translateY(${(1 - s) * 30}px)`,
        }}
      >
        {cierre.titulo}
      </h1>

      <p
        style={{
          margin: '24px 0 0',
          fontFamily: fuente,
          fontSize: 66,
          fontWeight: 800,
          color: LIMA,
          opacity: s,
        }}
      >
        {cierre.precio}
      </p>

      <p
        style={{
          margin: '18px 0 0',
          fontFamily: fuente,
          fontSize: 38,
          color: '#a8b3a6',
          textAlign: 'center',
          opacity: s,
        }}
      >
        {cierre.bajada}
      </p>

      <div
        style={{
          marginTop: 32,
          padding: '30px 62px',
          borderRadius: 22,
          backgroundColor: LIMA,
          color: '#1b2410',
          fontFamily: fuente,
          fontSize: 40,
          fontWeight: 800,
          letterSpacing: '0.12em',
          textTransform: 'uppercase',
          opacity: s,
          transform: `scale(${0.9 + s * 0.1})`,
        }}
      >
        {cierre.boton}
      </div>
    </AbsoluteFill>
  );
};

/* ---------- Barra de progreso ---------- */
const Progreso: React.FC = () => {
  const frame = useCurrentFrame();
  const { durationInFrames } = useVideoConfig();
  return (
    <AbsoluteFill style={{ justifyContent: 'flex-end' }}>
      <div style={{ height: 8, backgroundColor: 'rgba(255,255,255,.18)' }}>
        <div
          style={{
            height: '100%',
            width: `${(frame / durationInFrames) * 100}%`,
            backgroundColor: LIMA,
          }}
        />
      </div>
    </AbsoluteFill>
  );
};

export const Anuncio: React.FC<{ escenas: Escena[]; cierre: Cierre }> = ({
  escenas,
  cierre,
}) => {
  let cursor = 0;
  return (
    <AbsoluteFill style={{ backgroundColor: PAPEL }}>
      {escenas.map((escena, i) => {
        const desde = cursor;
        cursor += escena.frames;
        return (
          <Sequence key={i} from={desde} durationInFrames={escena.frames}>
            <EscenaClip escena={escena} duracion={escena.frames} />
          </Sequence>
        );
      })}
      <Sequence from={cursor} durationInFrames={CIERRE_FRAMES}>
        <Cierre cierre={cierre} />
      </Sequence>
      <Progreso />
    </AbsoluteFill>
  );
};
