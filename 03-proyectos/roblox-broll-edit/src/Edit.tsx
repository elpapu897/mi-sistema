import React from 'react';
import { AbsoluteFill, OffthreadVideo, Sequence, staticFile, useVideoConfig } from 'remotion';
import { BROLLS } from './brolls';
import { BrollInsert } from './BrollInsert';
import { Intro, INTRO_SECONDS } from './Intro';

/**
 * Intro animada + video completo del gameplay (audio original intacto de punta
 * a punta) con 14 inserts de B-roll a pantalla completa en los picos de reaccion.
 */
export const Edit: React.FC<{ sourceDurationInFrames: number }> = ({ sourceDurationInFrames }) => {
  const { fps } = useVideoConfig();
  const introFrames = Math.round(INTRO_SECONDS * fps);

  return (
    <AbsoluteFill style={{ backgroundColor: 'black' }}>
      <Sequence durationInFrames={introFrames} layout="none">
        <Intro />
      </Sequence>

      <Sequence from={introFrames} durationInFrames={sourceDurationInFrames} layout="none">
        <AbsoluteFill>
          <OffthreadVideo
            src={staticFile('source.mp4')}
            style={{ width: '100%', height: '100%', objectFit: 'contain' }}
          />

          {BROLLS.map((broll) => (
            <Sequence
              key={broll.file + broll.at}
              from={Math.round(broll.at * fps)}
              durationInFrames={Math.round(broll.dur * fps)}
              layout="none"
            >
              <BrollInsert broll={broll} />
            </Sequence>
          ))}
        </AbsoluteFill>
      </Sequence>
    </AbsoluteFill>
  );
};
