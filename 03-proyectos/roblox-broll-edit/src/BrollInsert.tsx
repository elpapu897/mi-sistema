import React from 'react';
import { AbsoluteFill, OffthreadVideo, interpolate, staticFile, useCurrentFrame, useVideoConfig } from 'remotion';
import type { Broll } from './brolls';

/**
 * Un insert de B-roll a pantalla completa.
 * El audio original nunca se corta: este componente se dibuja ENCIMA del gameplay
 * y el clip de stock va muteado.
 */
export const BrollInsert: React.FC<{ broll: Broll }> = ({ broll }) => {
  const frame = useCurrentFrame();
  const { fps, durationInFrames } = useVideoConfig();

  const fadeIn = 5;
  const fadeOut = 7;

  const opacity = interpolate(
    frame,
    [0, fadeIn, durationInFrames - fadeOut, durationInFrames],
    [0, 1, 1, 0],
    { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' },
  );

  // Zoom lento: le da vida al clip de stock en un insert tan corto.
  const scale = interpolate(frame, [0, durationInFrames], [1.06, 1.14]);

  // Flash blanco corto en la entrada, para que el corte pegue con el grito.
  const flash = interpolate(frame, [0, 4], [0.55, 0], { extrapolateRight: 'clamp' });

  const labelX = interpolate(frame, [3, 14], [-40, 0], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });
  const labelOpacity = interpolate(
    frame,
    [3, 14, durationInFrames - fadeOut, durationInFrames],
    [0, 1, 1, 0],
    { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' },
  );

  return (
    <AbsoluteFill style={{ opacity }}>
      <AbsoluteFill style={{ overflow: 'hidden', backgroundColor: 'black' }}>
        <OffthreadVideo
          src={staticFile(broll.file)}
          startFrom={Math.round(broll.trim * fps)}
          muted
          style={{ width: '100%', height: '100%', objectFit: 'cover', transform: `scale(${scale})` }}
        />
      </AbsoluteFill>

      {/* Vinieta para que el texto se lea siempre */}
      <AbsoluteFill
        style={{
          background: 'linear-gradient(to top, rgba(0,0,0,0.65) 0%, rgba(0,0,0,0) 38%)',
        }}
      />

      {/* Etiqueta */}
      <AbsoluteFill
        style={{
          justifyContent: 'flex-end',
          alignItems: 'flex-start',
          padding: 72,
        }}
      >
        <div
          style={{
            transform: `translateX(${labelX}px)`,
            opacity: labelOpacity,
            display: 'flex',
            alignItems: 'center',
            gap: 18,
          }}
        >
          <div style={{ width: 10, height: 58, backgroundColor: '#00E5A0', borderRadius: 5 }} />
          <div
            style={{
              fontFamily: 'Arial Black, Arial, Helvetica, sans-serif',
              fontSize: 54,
              fontWeight: 900,
              letterSpacing: 2,
              color: 'white',
              textShadow: '0 4px 18px rgba(0,0,0,0.85)',
            }}
          >
            {broll.label}
          </div>
        </div>
      </AbsoluteFill>

      {/* Flash de entrada */}
      <AbsoluteFill style={{ backgroundColor: 'white', opacity: flash }} />
    </AbsoluteFill>
  );
};
