import React from 'react';
import {
  AbsoluteFill,
  Easing,
  OffthreadVideo,
  interpolate,
  spring,
  staticFile,
  useCurrentFrame,
  useVideoConfig,
} from 'remotion';

export const INTRO_SECONDS = 4.5;

/** Cambiar aca el nombre que muestra la intro. */
export const INTRO_NAME = 'CHAVONES';

const TEAL = '#00E5A0';
const MAGENTA = '#FF2D95';

/** Grilla en perspectiva que se desplaza hacia la camara. */
const NeonGrid: React.FC<{ progress: number }> = ({ progress }) => {
  const scroll = (progress * 260) % 130;
  return (
    <AbsoluteFill style={{ perspective: 640, overflow: 'hidden' }}>
      <div
        style={{
          position: 'absolute',
          left: '-60%',
          width: '220%',
          top: '52%',
          height: '110%',
          transform: 'rotateX(72deg)',
          transformOrigin: 'top center',
          backgroundImage: `
            linear-gradient(to right, ${TEAL}55 2px, transparent 2px),
            linear-gradient(to bottom, ${TEAL}55 2px, transparent 2px)`,
          backgroundSize: '130px 130px',
          backgroundPosition: `0px ${scroll}px`,
          maskImage: 'linear-gradient(to bottom, rgba(0,0,0,0.9), transparent 62%)',
          WebkitMaskImage: 'linear-gradient(to bottom, rgba(0,0,0,0.9), transparent 62%)',
        }}
      />
    </AbsoluteFill>
  );
};

export const Intro: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps, durationInFrames } = useVideoConfig();

  const letters = INTRO_NAME.split('');

  // Camara: arranca lejos y termina con un empuje fuerte hacia adelante.
  const settle = interpolate(frame, [0, 55], [1.18, 1], {
    extrapolateRight: 'clamp',
    easing: Easing.out(Easing.cubic),
  });
  const punchIn = interpolate(frame, [durationInFrames - 14, durationInFrames], [0, 0.55], {
    extrapolateLeft: 'clamp',
  });
  const camScale = settle + punchIn;

  // Barrido de luz sobre el texto.
  const sweep = interpolate(frame, [38, 72], [-140, 240], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });

  // Flash de salida: corta seco al gameplay.
  const outFlash = interpolate(frame, [durationInFrames - 8, durationInFrames - 2], [0, 1], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });

  const bgOpacity = interpolate(frame, [0, 12], [0, 1], { extrapolateRight: 'clamp' });

  const barWidth = interpolate(frame, [46, 66], [0, 620], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
    easing: Easing.out(Easing.cubic),
  });
  const barOpacity = interpolate(frame, [46, 56], [0, 1], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' });

  return (
    <AbsoluteFill style={{ backgroundColor: '#04060D' }}>
      <AbsoluteFill style={{ transform: `scale(${camScale})` }}>
        {/* Fondo: particulas de stock, oscurecidas y tenidas */}
        <AbsoluteFill style={{ opacity: bgOpacity * 0.55 }}>
          <OffthreadVideo
            src={staticFile('broll/particles.mp4')}
            startFrom={30}
            muted
            style={{ width: '100%', height: '100%', objectFit: 'cover' }}
          />
        </AbsoluteFill>
        <AbsoluteFill
          style={{
            background: `radial-gradient(ellipse at 50% 55%, ${MAGENTA}22 0%, transparent 55%), radial-gradient(ellipse at 50% 100%, ${TEAL}33 0%, transparent 60%)`,
          }}
        />

        <NeonGrid progress={frame / fps} />

        {/* Vinieta */}
        <AbsoluteFill
          style={{
            background: 'radial-gradient(ellipse at center, transparent 30%, rgba(0,0,0,0.85) 100%)',
          }}
        />

        {/* Nombre */}
        <AbsoluteFill style={{ justifyContent: 'center', alignItems: 'center' }}>
          <div style={{ position: 'relative', display: 'flex', gap: 4 }}>
            {letters.map((ch, i) => {
              const s = spring({
                frame: frame - 10 - i * 3,
                fps,
                config: { damping: 13, mass: 0.7, stiffness: 130 },
              });
              return (
                <span
                  key={i}
                  style={{
                    display: 'inline-block',
                    fontFamily: 'Arial Black, Arial, Helvetica, sans-serif',
                    fontSize: 168,
                    fontWeight: 900,
                    letterSpacing: 6,
                    color: 'white',
                    opacity: s,
                    transform: `translateY(${(1 - s) * 90}px) rotate(${(1 - s) * (i % 2 ? 8 : -8)}deg) scale(${0.6 + s * 0.4})`,
                    textShadow: `0 0 34px ${TEAL}cc, 4px 0 0 ${MAGENTA}90, -4px 0 0 ${TEAL}90, 0 14px 40px rgba(0,0,0,0.9)`,
                  }}
                >
                  {ch}
                </span>
              );
            })}

            {/* Barrido de luz */}
            <div
              style={{
                position: 'absolute',
                inset: -20,
                overflow: 'hidden',
                pointerEvents: 'none',
                mixBlendMode: 'screen',
              }}
            >
              <div
                style={{
                  position: 'absolute',
                  top: 0,
                  bottom: 0,
                  left: `${sweep}%`,
                  width: '22%',
                  background: 'linear-gradient(100deg, transparent, rgba(255,255,255,0.75), transparent)',
                  filter: 'blur(6px)',
                }}
              />
            </div>
          </div>

          {/* Barra neon debajo del nombre */}
          <div
            style={{
              marginTop: 26,
              width: barWidth,
              height: 8,
              borderRadius: 4,
              opacity: barOpacity,
              background: `linear-gradient(90deg, ${TEAL}, ${MAGENTA})`,
              boxShadow: `0 0 26px ${TEAL}aa`,
            }}
          />
        </AbsoluteFill>
      </AbsoluteFill>

      {/* Flash de corte al gameplay */}
      <AbsoluteFill style={{ backgroundColor: 'white', opacity: outFlash }} />
    </AbsoluteFill>
  );
};
