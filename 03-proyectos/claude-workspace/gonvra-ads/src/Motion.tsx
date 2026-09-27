import React from 'react';
import {
  AbsoluteFill,
  Img,
  Sequence,
  interpolate,
  spring,
  staticFile,
  useCurrentFrame,
  useVideoConfig,
} from 'remotion';
import { CAMPAIGN } from './campaign';

const TINTA = '#101a16';
const VERDE = '#17251e';
const LIMA = '#c8e54a';
const PAPEL = '#f7f6f1';
const fuente = '"Helvetica Neue", Helvetica, "Segoe UI", Inter, system-ui, sans-serif';

/* ---------------- olas de fondo, en movimiento ---------------- */
const Olas: React.FC<{ color?: string; abajo?: boolean }> = ({ color = VERDE, abajo }) => {
  const frame = useCurrentFrame();
  return (
    <div
      style={{
        position: 'absolute',
        left: 0,
        right: 0,
        [abajo ? 'bottom' : 'top']: -4,
        height: 320,
        overflow: 'hidden',
        transform: abajo ? 'none' : 'rotate(180deg)',
      }}
    >
      <svg viewBox="0 0 1440 300" preserveAspectRatio="none" style={{ width: '100%', height: '100%' }}>
        {[0, 1, 2].map((i) => (
          <path
            key={i}
            transform={`translate(${-((frame * (1.6 + i * 0.9)) % 1440)} ${i * 26})`}
            d="M0,150 q90,-58 180,0 t180,0 t180,0 t180,0 t180,0 t180,0 t180,0 t180,0 t180,0 t180,0 t180,0 t180,0 t180,0 t180,0 t180,0 t180,0 L2880,300 L0,300 Z"
            fill={color}
            opacity={0.3 + i * 0.35}
          />
        ))}
      </svg>
    </div>
  );
};

/* ---------------- una línea de texto que entra palabra por palabra ---------------- */
const Linea: React.FC<{
  texto: string;
  desde: number;
  tam?: number;
  color?: string;
  resaltar?: string;
}> = ({ texto, desde, tam = 96, color = '#fff', resaltar }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  return (
    <div style={{ display: 'flex', flexWrap: 'wrap', gap: '0 20px', justifyContent: 'center' }}>
      {texto.split(' ').map((palabra, i) => {
        const s = spring({ frame: frame - desde - i * 3, fps, config: { damping: 16, mass: 0.5, stiffness: 150 } });
        const esClave = resaltar && palabra.toLowerCase().includes(resaltar.toLowerCase());
        return (
          <span
            key={i}
            style={{
              fontFamily: fuente,
              fontSize: tam,
              fontWeight: 800,
              lineHeight: 1.08,
              letterSpacing: '-.035em',
              color: esClave ? LIMA : color,
              opacity: s,
              transform: `translateY(${(1 - s) * 46}px) scale(${0.9 + s * 0.1})`,
              display: 'inline-block',
            }}
          >
            {palabra}
          </span>
        );
      })}
    </div>
  );
};

const Marca: React.FC = () => (
  <div
    style={{
      position: 'absolute',
      bottom: 96,
      left: 0,
      right: 0,
      textAlign: 'center',
      fontFamily: fuente,
      fontSize: 30,
      fontWeight: 850,
      letterSpacing: '.36em',
      color: 'rgba(255,255,255,.5)',
    }}
  >
    GONVRA
  </div>
);

/* ================= 1 · TIPOGRAFÍA CINÉTICA ================= */
export const Kinetico: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const entraProd = spring({ frame: frame - 200, fps, config: { damping: 18, mass: 0.8 } });

  return (
    <AbsoluteFill style={{ backgroundColor: TINTA }}>
      <Olas />
      <Olas abajo />

      <Sequence from={0} durationInFrames={70}>
        <AbsoluteFill style={{ justifyContent: 'center', padding: '0 90px' }}>
          <Linea texto="Una para la barba." desde={0} tam={92} />
          <div style={{ height: 26 }} />
          <Linea texto="Otra para el cuerpo." desde={16} tam={92} />
          <div style={{ height: 26 }} />
          <Linea texto="Otra que ya no corta." desde={32} tam={92} />
        </AbsoluteFill>
      </Sequence>

      <Sequence from={70} durationInFrames={60}>
        <AbsoluteFill style={{ justifyContent: 'center', padding: '0 90px' }}>
          <Linea texto="Y el cajón lleno" desde={0} tam={102} />
          <div style={{ height: 26 }} />
          <Linea texto="de cables." desde={14} tam={102} resaltar="cables" />
        </AbsoluteFill>
      </Sequence>

      <Sequence from={130} durationInFrames={70}>
        <AbsoluteFill style={{ justifyContent: 'center', padding: '0 90px' }}>
          <Linea texto="Con una alcanza." desde={0} tam={118} resaltar="una" />
          <div style={{ height: 34 }} />
          <Linea texto="Rostro, cuerpo y zona íntima." desde={18} tam={62} color="#a8b3a6" />
        </AbsoluteFill>
      </Sequence>

      <Sequence from={200}>
        <AbsoluteFill style={{ alignItems: 'center', justifyContent: 'center', padding: 90 }}>
          <div
            style={{
              width: 760,
              padding: 26,
              borderRadius: 44,
              background: PAPEL,
              boxShadow: '0 46px 100px rgba(0,0,0,.5)',
              opacity: entraProd,
              transform: `translateY(${(1 - entraProd) * 60}px) scale(${0.9 + entraProd * 0.1})`,
            }}
          >
            <Img src={staticFile('carrusel/pack.png')} style={{ width: '100%', display: 'block', borderRadius: 26 }} />
          </div>
          <div style={{ height: 50 }} />
          <Linea texto="Rasuradora integral" desde={214 - 200} tam={76} />
          <div style={{ height: 30 }} />
          <div
            style={{
              padding: '30px 66px',
              borderRadius: 22,
              background: LIMA,
              color: '#1b2410',
              fontFamily: fuente,
              fontSize: 44,
              fontWeight: 800,
              letterSpacing: '.1em',
              opacity: spring({ frame: frame - 226, fps, config: { damping: 200 } }),
            }}
          >
            {CAMPAIGN.price}
          </div>
          <div style={{ height: 22 }} />
          <p
            style={{
              margin: 0,
              fontFamily: fuente,
              fontSize: 36,
              color: '#a8b3a6',
              opacity: spring({ frame: frame - 234, fps, config: { damping: 200 } }),
            }}
          >
            {CAMPAIGN.website}
          </p>
        </AbsoluteFill>
      </Sequence>

      <Marca />
    </AbsoluteFill>
  );
};

/* ================= 2 · LOS 3 PASOS, ANIMADO ================= */
const Paso: React.FC<{ n: string; titulo: string; texto: string; imagen: string; desde: number }> = ({
  n,
  titulo,
  texto,
  imagen,
  desde,
}) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const s = spring({ frame: frame - desde, fps, config: { damping: 20, mass: 0.7 } });
  const zoom = interpolate(frame - desde, [0, 110], [1.14, 1.02], { extrapolateRight: 'clamp' });
  return (
    <AbsoluteFill style={{ opacity: s }}>
      <AbsoluteFill style={{ transform: `scale(${zoom})` }}>
        <Img src={staticFile(imagen)} style={{ width: '100%', height: '100%', objectFit: 'cover' }} />
      </AbsoluteFill>
      <AbsoluteFill
        style={{
          background: 'linear-gradient(0deg, rgba(16,26,22,.94) 12%, rgba(16,26,22,.25) 52%, rgba(16,26,22,.5) 100%)',
        }}
      />
      <AbsoluteFill style={{ justifyContent: 'flex-end', padding: '0 84px 300px' }}>
        <div
          style={{
            display: 'grid',
            placeItems: 'center',
            width: 96,
            height: 96,
            borderRadius: 99,
            background: LIMA,
            color: '#1b2410',
            fontFamily: fuente,
            fontSize: 48,
            fontWeight: 800,
            transform: `scale(${s})`,
          }}
        >
          {n}
        </div>
        <h2
          style={{
            margin: '30px 0 0',
            fontFamily: fuente,
            fontSize: 88,
            fontWeight: 800,
            lineHeight: 1.03,
            letterSpacing: '-.04em',
            color: '#fff',
            transform: `translateY(${(1 - s) * 34}px)`,
          }}
        >
          {titulo}
        </h2>
        <p style={{ margin: '22px 0 0', fontFamily: fuente, fontSize: 42, lineHeight: 1.35, color: '#c9d2c6', maxWidth: '20ch' }}>
          {texto}
        </p>
      </AbsoluteFill>
    </AbsoluteFill>
  );
};

export const TresPasos: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const fin = spring({ frame: frame - 380, fps, config: { damping: 18 } });
  return (
    <AbsoluteFill style={{ backgroundColor: TINTA }}>
      <Sequence from={0} durationInFrames={70}>
        <AbsoluteFill style={{ justifyContent: 'center', padding: '0 90px' }}>
          <Olas />
          <Olas abajo />
          <Linea texto="Cómo se usa" desde={4} tam={116} />
          <div style={{ height: 26 }} />
          <Linea texto="en 3 pasos" desde={18} tam={116} resaltar="3" />
        </AbsoluteFill>
      </Sequence>

      <Sequence from={70} durationInFrames={110}>
        <Paso n="1" titulo="Elegí el largo" texto="Peine de 1, 3 o 5 mm. Sin peine queda más al ras." imagen="carrusel/kit.jpg" desde={0} />
      </Sequence>
      <Sequence from={180} durationInFrames={110}>
        <Paso n="2" titulo="Pasala en seco" texto="Piel limpia y seca, movimientos suaves. Sin espuma." imagen="carrusel/uso.jpg" desde={0} />
      </Sequence>
      <Sequence from={290} durationInFrames={110}>
        <Paso n="3" titulo="Limpiala y cargala" texto="El cabezal se enjuaga. Carga con cualquier cable USB." imagen="carrusel/agua.jpg" desde={0} />
      </Sequence>

      <Sequence from={380}>
        <AbsoluteFill style={{ backgroundColor: TINTA, alignItems: 'center', justifyContent: 'center', padding: 90 }}>
          <Olas />
          <Olas abajo />
          <div
            style={{
              width: 720,
              padding: 26,
              borderRadius: 44,
              background: PAPEL,
              boxShadow: '0 46px 100px rgba(0,0,0,.5)',
              opacity: fin,
              transform: `scale(${0.92 + fin * 0.08})`,
            }}
          >
            <Img src={staticFile('carrusel/pack.png')} style={{ width: '100%', display: 'block', borderRadius: 26 }} />
          </div>
          <div style={{ height: 46 }} />
          <Linea texto="Rostro y cuerpo, un solo equipo" desde={392 - 380} tam={68} />
          <div style={{ height: 34 }} />
          <div
            style={{
              padding: '28px 60px',
              borderRadius: 22,
              background: LIMA,
              color: '#1b2410',
              fontFamily: fuente,
              fontSize: 40,
              fontWeight: 800,
              letterSpacing: '.12em',
              opacity: spring({ frame: frame - 404, fps, config: { damping: 200 } }),
            }}
          >
            {CAMPAIGN.website.toUpperCase()}
          </div>
        </AbsoluteFill>
      </Sequence>
      <Marca />
    </AbsoluteFill>
  );
};

/* ================= 3 · LOS PACKS ================= */
const PackCard: React.FC<{ imagen: string; titulo: string; sub: string; precio: string; desde: number; destacado?: boolean }> = ({
  imagen,
  titulo,
  sub,
  precio,
  desde,
  destacado,
}) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const s = spring({ frame: frame - desde, fps, config: { damping: 16, mass: 0.6, stiffness: 140 } });
  return (
    <div
      style={{
        display: 'grid',
        gridTemplateColumns: '190px 1fr auto',
        alignItems: 'center',
        gap: 26,
        padding: '26px 32px',
        borderRadius: 26,
        background: destacado ? TINTA : '#fff',
        border: destacado ? `3px solid ${LIMA}` : '3px solid #e2e5dd',
        opacity: s,
        transform: `translateX(${(1 - s) * 70}px)`,
      }}
    >
      <Img src={staticFile(imagen)} style={{ width: 190, height: 150, objectFit: 'contain' }} />
      <div>
        <p style={{ margin: 0, fontFamily: fuente, fontSize: 46, fontWeight: 800, color: destacado ? '#fff' : TINTA }}>{titulo}</p>
        <p style={{ margin: '8px 0 0', fontFamily: fuente, fontSize: 32, color: destacado ? LIMA : '#6b7570' }}>{sub}</p>
      </div>
      <p style={{ margin: 0, fontFamily: fuente, fontSize: 44, fontWeight: 800, color: destacado ? '#fff' : TINTA }}>{precio}</p>
    </div>
  );
};

export const Packs: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const cta = spring({ frame: frame - 210, fps, config: { damping: 200 } });
  return (
    <AbsoluteFill style={{ backgroundColor: PAPEL }}>
      <Sequence from={0} durationInFrames={60}>
        <AbsoluteFill style={{ justifyContent: 'center', padding: '0 90px', backgroundColor: TINTA }}>
          <Olas />
          <Olas abajo />
          <Linea texto="Cuantas más llevás," desde={4} tam={92} />
          <div style={{ height: 24 }} />
          <Linea texto="menos pagás." desde={18} tam={92} resaltar="menos" />
        </AbsoluteFill>
      </Sequence>

      <Sequence from={60}>
        <AbsoluteFill style={{ justifyContent: 'center', padding: '0 70px' }}>
          <h2
            style={{
              margin: '0 0 46px',
              fontFamily: fuente,
              fontSize: 74,
              fontWeight: 800,
              letterSpacing: '-.04em',
              color: TINTA,
              textAlign: 'center',
            }}
          >
            Elegí tu pack
          </h2>
          <div style={{ display: 'grid', gap: 22 }}>
            <PackCard imagen="carrusel/pack1.png" titulo="Individual" sub="Para probarla" precio={CAMPAIGN.price} desde={10} />
            <PackCard imagen="carrusel/pack2.png" titulo="Dúo" sub="Ahorrás 10%" precio={CAMPAIGN.duo} desde={26} destacado />
            <PackCard imagen="carrusel/pack.png" titulo="Pack x3" sub="Ahorrás 20%" precio={CAMPAIGN.pack3} desde={42} />
          </div>
          <div
            style={{
              margin: '54px auto 0',
              padding: '30px 66px',
              borderRadius: 22,
              background: TINTA,
              color: '#fff',
              fontFamily: fuente,
              fontSize: 40,
              fontWeight: 800,
              letterSpacing: '.12em',
              opacity: cta,
              transform: `scale(${0.9 + cta * 0.1})`,
            }}
          >
            {CAMPAIGN.website.toUpperCase()}
          </div>
        </AbsoluteFill>
      </Sequence>
    </AbsoluteFill>
  );
};
