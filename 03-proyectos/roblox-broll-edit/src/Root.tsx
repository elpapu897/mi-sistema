import React from 'react';
import { Composition, staticFile } from 'remotion';
import { getVideoMetadata } from '@remotion/media-utils';
import { Edit } from './Edit';
import { Intro, INTRO_SECONDS } from './Intro';

const FPS = 30;

export const RemotionRoot: React.FC = () => {
  return (
    <>
      {/* Video final: intro + gameplay completo + B-rolls */}
      <Composition
        id="FullEdit"
        component={Edit}
        durationInFrames={30 * FPS}
        fps={FPS}
        width={1920}
        height={1080}
        defaultProps={{ sourceDurationInFrames: 0 }}
        calculateMetadata={async () => {
          const meta = await getVideoMetadata(staticFile('source.mp4'));
          const sourceDurationInFrames = Math.floor(meta.durationInSeconds * FPS);
          return {
            durationInFrames: Math.round(INTRO_SECONDS * FPS) + sourceDurationInFrames,
            props: { sourceDurationInFrames },
          };
        }}
      />

      {/* Solo la intro, para iterar rapido sin cargar los 10 min */}
      <Composition
        id="Intro"
        component={Intro}
        durationInFrames={Math.round(INTRO_SECONDS * FPS)}
        fps={FPS}
        width={1920}
        height={1080}
      />
    </>
  );
};
