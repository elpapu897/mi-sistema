import React from 'react';
import { AbsoluteFill, Easing, Img, interpolate, staticFile, useCurrentFrame, useVideoConfig } from 'remotion';

export const TINTA = '#0d1613';
export const VERDE = '#16241d';
export const LIMA = '#c8e54a';
export const PAPEL = '#f7f6f1';
export const HUMO = '#9aa79a';

export const FUENTE =
  '"Helvetica Neue", Helvetica, "Segoe UI", Inter, system-ui, -apple-system, sans-serif';

/** La curva que usan Apple y Linear. Arranca rápido, frena suave, sin rebote. */
export const SUAVE = Easing.bezier(0.16, 1, 0.3, 1);
/** Para salidas: arranca lento, se va rápido. */
export const SALIDA = Easing.bezier(0.7, 0, 0.84, 0);

export const ease = (
  frame: number,
  desde: number,
  hasta: number,
  a: number,
  b: number,
  curva = SUAVE
) =>
  interpolate(frame, [desde, hasta], [a, b], {
    easing: curva,
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });

/* ─────────────── Texto que se revela con máscara ───────────────
   No aparece con fade: se descubre de abajo hacia arriba, como si
   estuviera detrás de una cortina. Es lo que hace que se vea caro. */
export const Revelar: React.FC<{
  children: React.ReactNode;
  desde?: number;
  duracion?: number;
  estilo?: React.CSSProperties;
}> = ({ children, desde = 0, duracion = 26, estilo }) => {
  const frame = useCurrentFrame();
  const p = ease(frame, desde, desde + duracion, 0, 1);
  return (
    <div style={{ overflow: 'hidden', paddingBottom: '.12em' }}>
      <div
        style={{
          ...estilo,
          transform: `translateY(${(1 - p) * 108}%)`,
          opacity: p < 0.02 ? 0 : 1,
        }}
      >
        {children}
      </div>
    </div>
  );
};

/** Titular. Cada línea entra escalonada, con tracking que se abre al asentarse. */
export const Titular: React.FC<{
  lineas: string[];
  desde?: number;
  tam?: number;
  color?: string;
  resaltar?: number;
  alineado?: 'left' | 'center';
}> = ({ lineas, desde = 0, tam = 104, color = '#fff', resaltar, alineado = 'left' }) => {
  const frame = useCurrentFrame();
  return (
    <div style={{ display: 'grid', gap: '.06em', textAlign: alineado }}>
      {lineas.map((linea, i) => {
        const inicio = desde + i * 7;
        const tracking = ease(frame, inicio, inicio + 40, -0.055, -0.038);
        return (
          <Revelar key={i} desde={inicio}>
            <span
              style={{
                display: 'block',
                fontFamily: FUENTE,
                fontSize: tam,
                fontWeight: 700,
                lineHeight: 1.02,
                letterSpacing: `${tracking}em`,
                color: resaltar === i ? LIMA : color,
              }}
            >
              {linea}
            </span>
          </Revelar>
        );
      })}
    </div>
  );
};

/** Línea fina que crece: separador de marca. */
export const Regla: React.FC<{ desde?: number; color?: string; ancho?: number }> = ({
  desde = 0,
  color = LIMA,
  ancho = 120,
}) => {
  const frame = useCurrentFrame();
  return (
    <div
      style={{
        width: ease(frame, desde, desde + 30, 0, ancho),
        height: 3,
        background: color,
        borderRadius: 3,
      }}
    />
  );
};

/** Bajada en gris, entra después del titular. */
export const Bajada: React.FC<{ texto: string; desde?: number; tam?: number; color?: string }> = ({
  texto,
  desde = 0,
  tam = 40,
  color = HUMO,
}) => (
  <Revelar desde={desde} duracion={30}>
    <p
      style={{
        margin: 0,
        maxWidth: '19ch',
        fontFamily: FUENTE,
        fontSize: tam,
        fontWeight: 400,
        lineHeight: 1.4,
        letterSpacing: '-.01em',
        color,
      }}
    >
      {texto}
    </p>
  </Revelar>
);

/* ─────────────── Textura de cine ───────────────
   Grano + viñeta. Es lo que separa un video "hecho con plantilla"
   de uno que parece filmado. Va siempre arriba de todo. */
export const Textura: React.FC<{ grano?: number; vineta?: number }> = ({
  grano = 0.055,
  vineta = 0.5,
}) => {
  const frame = useCurrentFrame();
  return (
    <>
      <AbsoluteFill
        style={{
          background: `radial-gradient(120% 85% at 50% 45%, transparent 42%, rgba(0,0,0,${vineta}) 100%)`,
          pointerEvents: 'none',
        }}
      />
      <AbsoluteFill style={{ opacity: grano, mixBlendMode: 'overlay', pointerEvents: 'none' }}>
        <svg width="100%" height="100%">
          <filter id={`g${frame % 6}`}>
            <feTurbulence type="fractalNoise" baseFrequency="0.85" numOctaves="3" seed={frame % 6} />
          </filter>
          <rect width="100%" height="100%" filter={`url(#g${frame % 6})`} />
        </svg>
      </AbsoluteFill>
    </>
  );
};

/** Zona segura: TikTok tapa la derecha con botones y abajo con la descripción. */
export const SAFE = { top: 190, right: 210, bottom: 340, left: 84 };

/** Foto con push-in lento y grado de color cálido. */
export const Placa: React.FC<{ src: string; desde: number; duracion: number; escala?: [number, number] }> = ({
  src,
  desde,
  duracion,
  escala = [1.16, 1.03],
}) => {
  const frame = useCurrentFrame();
  const z = ease(frame, desde, desde + duracion, escala[0], escala[1], Easing.linear);
  return (
    <AbsoluteFill style={{ transform: `scale(${z})` }}>
      <Img
        src={staticFile(src)}
        style={{
          width: '100%',
          height: '100%',
          objectFit: 'cover',
          filter: 'saturate(1.04) contrast(1.06) brightness(.98)',
        }}
      />
    </AbsoluteFill>
  );
};

/** Velo para que el texto se lea sin matar la foto. */
export const Velo: React.FC<{ fuerza?: number }> = ({ fuerza = 1 }) => (
  <AbsoluteFill
    style={{
      background: `linear-gradient(0deg,
        rgba(13,22,19,${0.94 * fuerza}) 0%,
        rgba(13,22,19,${0.72 * fuerza}) 26%,
        rgba(13,22,19,${0.16 * fuerza}) 58%,
        rgba(13,22,19,${0.34 * fuerza}) 100%)`,
    }}
  />
);

/** Corte con destello: transición entre escenas. */
export const Destello: React.FC<{ en: number }> = ({ en }) => {
  const frame = useCurrentFrame();
  const o = interpolate(frame, [en - 3, en, en + 6], [0, 0.5, 0], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });
  return <AbsoluteFill style={{ background: '#fff', opacity: o, pointerEvents: 'none' }} />;
};

/** Contador de progreso finito arriba, como los stories buenos. */
export const Progreso: React.FC = () => {
  const frame = useCurrentFrame();
  const { durationInFrames } = useVideoConfig();
  return (
    <div style={{ position: 'absolute', top: 84, left: SAFE.left, right: SAFE.right, height: 3 }}>
      <div style={{ position: 'absolute', inset: 0, background: 'rgba(255,255,255,.16)', borderRadius: 3 }} />
      <div
        style={{
          position: 'absolute',
          inset: 0,
          width: `${(frame / durationInFrames) * 100}%`,
          background: 'rgba(255,255,255,.75)',
          borderRadius: 3,
        }}
      />
    </div>
  );
};

/** Firma discreta. Las marcas grandes no gritan el logo en cada cuadro. */
export const Firma: React.FC<{ claro?: boolean }> = ({ claro = true }) => (
  <div
    style={{
      position: 'absolute',
      top: 110,
      left: SAFE.left,
      fontFamily: FUENTE,
      fontSize: 24,
      fontWeight: 600,
      letterSpacing: '.42em',
      color: claro ? 'rgba(255,255,255,.62)' : 'rgba(13,22,19,.5)',
    }}
  >
    GONVRA
  </div>
);
