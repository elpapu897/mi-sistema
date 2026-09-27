import React from 'react';
import { AbsoluteFill, Img, Sequence, staticFile, useCurrentFrame } from 'remotion';
import {
  Bajada,
  Destello,
  ease,
  Firma,
  FUENTE,
  HUMO,
  LIMA,
  PAPEL,
  Placa,
  Progreso,
  Regla,
  Revelar,
  SAFE,
  Textura,
  TINTA,
  Titular,
  Velo,
} from './estilo';
import { CAMPAIGN } from './campaign';

/* ═══════════ escena: foto + una sola frase ═══════════ */
const Escena: React.FC<{
  imagen: string;
  lineas: string[];
  bajada?: string;
  duracion: number;
  resaltar?: number;
  tam?: number;
}> = ({ imagen, lineas, bajada, duracion, resaltar, tam = 92 }) => {
  const frame = useCurrentFrame();
  const salida = ease(frame, duracion - 12, duracion, 1, 0);
  return (
    <AbsoluteFill style={{ backgroundColor: TINTA, opacity: salida }}>
      <Placa src={imagen} desde={0} duracion={duracion} />
      <Velo />
      <AbsoluteFill
        style={{
          justifyContent: 'flex-end',
          padding: `0 ${SAFE.right}px ${SAFE.bottom}px ${SAFE.left}px`,
        }}
      >
        <Titular lineas={lineas} desde={6} tam={tam} resaltar={resaltar} />
        {bajada && (
          <>
            <div style={{ height: 30 }} />
            <Regla desde={6 + lineas.length * 7 + 10} ancho={96} />
            <div style={{ height: 26 }} />
            <Bajada texto={bajada} desde={6 + lineas.length * 7 + 14} />
          </>
        )}
      </AbsoluteFill>
    </AbsoluteFill>
  );
};

/* ═══════════ escena de texto puro, fondo tinta ═══════════ */
const Declaracion: React.FC<{ lineas: string[]; bajada?: string; duracion: number; resaltar?: number }> = ({
  lineas,
  bajada,
  duracion,
  resaltar,
}) => {
  const frame = useCurrentFrame();
  const salida = ease(frame, duracion - 12, duracion, 1, 0);
  const deriva = ease(frame, 0, duracion, 0, -26, (t) => t);
  return (
    <AbsoluteFill style={{ backgroundColor: TINTA, opacity: salida }}>
      <AbsoluteFill
        style={{
          justifyContent: 'center',
          padding: `0 ${SAFE.right}px 0 ${SAFE.left}px`,
          transform: `translateY(${deriva}px)`,
        }}
      >
        <Titular lineas={lineas} desde={4} tam={104} resaltar={resaltar} />
        {bajada && (
          <>
            <div style={{ height: 34 }} />
            <Bajada texto={bajada} desde={4 + lineas.length * 7 + 12} />
          </>
        )}
      </AbsoluteFill>
    </AbsoluteFill>
  );
};

/* ═══════════ cierre: producto sobre pedestal ═══════════ */
const Cierre: React.FC<{ duracion: number }> = ({ duracion }) => {
  const frame = useCurrentFrame();
  const sube = ease(frame, 4, 44, 90, 0);
  const opac = ease(frame, 4, 34, 0, 1);
  const zoom = ease(frame, 0, duracion, 1.04, 1.0, (t) => t);
  return (
    <AbsoluteFill style={{ backgroundColor: TINTA }}>
      {/* halo detrás del producto */}
      <AbsoluteFill
        style={{
          background: 'radial-gradient(58% 38% at 50% 40%, rgba(200,229,74,.14) 0%, transparent 70%)',
        }}
      />
      <AbsoluteFill style={{ alignItems: 'center', justifyContent: 'center', paddingBottom: 180 }}>
        <div
          style={{
            width: 620,
            opacity: opac,
            transform: `translateY(${sube}px) scale(${zoom})`,
          }}
        >
          <Img
            src={staticFile('carrusel/pack.png')}
            style={{
              width: '100%',
              display: 'block',
              filter: 'drop-shadow(0 60px 70px rgba(0,0,0,.55))',
            }}
          />
        </div>
        <div style={{ height: 54 }} />
        <div style={{ textAlign: 'center' }}>
          <Titular
            lineas={['Una sola rasuradora', 'para toda tu rutina']}
            desde={30}
            tam={62}
            alineado="center"
          />
          <div style={{ height: 30 }} />
          <Revelar desde={50}>
            <p style={{ margin: 0, fontFamily: FUENTE, fontSize: 38, color: HUMO, letterSpacing: '-.01em' }}>
              Envío a todo el país · {CAMPAIGN.price}
            </p>
          </Revelar>
          <div style={{ height: 40 }} />
          <Revelar desde={62}>
            <p
              style={{
                margin: 0,
                fontFamily: FUENTE,
                fontSize: 34,
                fontWeight: 700,
                letterSpacing: '.32em',
                color: LIMA,
              }}
            >
              {CAMPAIGN.website.toUpperCase()}
            </p>
          </Revelar>
        </div>
      </AbsoluteFill>
    </AbsoluteFill>
  );
};

/* ═══════════════════ 1 · MANIFIESTO ═══════════════════ */
export const Manifiesto: React.FC = () => (
  <AbsoluteFill style={{ backgroundColor: TINTA }}>
    <Sequence from={0} durationInFrames={82}>
      <Escena
        imagen="carrusel/kit.jpg"
        lineas={['Una para la barba.', 'Otra para el cuerpo.']}
        bajada="Y un cajón lleno de cables que ya no usás."
        duracion={82}
        tam={84}
      />
    </Sequence>

    <Sequence from={78} durationInFrames={72}>
      <Declaracion lineas={['Con una', 'alcanza.']} resaltar={0} duracion={72} />
    </Sequence>

    <Sequence from={146} durationInFrames={78}>
      <Escena
        imagen="carrusel/filo.jpg"
        lineas={['Lámina de acero', 'entre el filo', 'y tu piel.']}
        duracion={78}
        tam={76}
        resaltar={0}
      />
    </Sequence>

    <Sequence from={220} durationInFrames={78}>
      <Escena
        imagen="carrusel/uso.jpg"
        lineas={['Rostro, cuerpo', 'y zona íntima.']}
        bajada="Peines de 1, 3 y 5 mm. Se usa en seco."
        duracion={78}
        tam={80}
      />
    </Sequence>

    <Sequence from={294}>
      <Cierre duracion={120} />
    </Sequence>

    <Destello en={78} />
    <Destello en={146} />
    <Destello en={220} />
    <Destello en={294} />
    <Firma />
    <Progreso />
    <Textura />
  </AbsoluteFill>
);

/* ═══════════════════ 2 · RITUAL (los 3 pasos) ═══════════════════ */
const Paso: React.FC<{ n: string; imagen: string; titulo: string; detalle: string; duracion: number }> = ({
  n,
  imagen,
  titulo,
  detalle,
  duracion,
}) => {
  const frame = useCurrentFrame();
  const salida = ease(frame, duracion - 12, duracion, 1, 0);
  return (
    <AbsoluteFill style={{ backgroundColor: TINTA, opacity: salida }}>
      <Placa src={imagen} desde={0} duracion={duracion} />
      <Velo />
      <AbsoluteFill
        style={{ justifyContent: 'flex-end', padding: `0 ${SAFE.right}px ${SAFE.bottom}px ${SAFE.left}px` }}
      >
        <Revelar desde={4}>
          <span
            style={{
              fontFamily: FUENTE,
              fontSize: 26,
              fontWeight: 700,
              letterSpacing: '.34em',
              color: LIMA,
            }}
          >
            PASO {n}
          </span>
        </Revelar>
        <div style={{ height: 22 }} />
        <Titular lineas={[titulo]} desde={12} tam={86} />
        <div style={{ height: 26 }} />
        <Regla desde={26} ancho={80} />
        <div style={{ height: 24 }} />
        <Bajada texto={detalle} desde={30} />
      </AbsoluteFill>
    </AbsoluteFill>
  );
};

export const Ritual: React.FC = () => (
  <AbsoluteFill style={{ backgroundColor: TINTA }}>
    <Sequence from={0} durationInFrames={64}>
      <Declaracion lineas={['Toda tu rutina', 'en tres pasos.']} resaltar={1} duracion={64} />
    </Sequence>
    <Sequence from={60} durationInFrames={86}>
      <Paso n="1" imagen="carrusel/kit.jpg" titulo="Elegí el largo" detalle="Peine de 1, 3 o 5 mm. Sin peine queda más al ras." duracion={86} />
    </Sequence>
    <Sequence from={142} durationInFrames={86}>
      <Paso n="2" imagen="carrusel/uso.jpg" titulo="Pasala en seco" detalle="Piel limpia y seca. Sin espuma, sin gel, sin cortes." duracion={86} />
    </Sequence>
    <Sequence from={224} durationInFrames={86}>
      <Paso n="3" imagen="carrusel/agua.jpg" titulo="Enjuagá y cargá" detalle="El cabezal va bajo la canilla. Carga por USB." duracion={86} />
    </Sequence>
    <Sequence from={306}>
      <Cierre duracion={120} />
    </Sequence>
    <Destello en={60} />
    <Destello en={142} />
    <Destello en={224} />
    <Destello en={306} />
    <Firma />
    <Progreso />
    <Textura />
  </AbsoluteFill>
);

/* ═══════════════════ 3 · LA OFERTA ═══════════════════ */
const Fila: React.FC<{ imagen: string; titulo: string; sub: string; precio: string; desde: number; destacada?: boolean }> = ({
  imagen,
  titulo,
  sub,
  precio,
  desde,
  destacada,
}) => {
  const frame = useCurrentFrame();
  const p = ease(frame, desde, desde + 32, 0, 1);
  return (
    <div
      style={{
        display: 'grid',
        gridTemplateColumns: '150px 1fr auto',
        alignItems: 'center',
        gap: 24,
        padding: '24px 30px',
        borderRadius: 22,
        background: destacada ? '#fff' : 'rgba(255,255,255,.05)',
        border: destacada ? `2px solid ${LIMA}` : '1px solid rgba(255,255,255,.12)',
        opacity: p,
        transform: `translateY(${(1 - p) * 40}px)`,
      }}
    >
      <Img src={staticFile(imagen)} style={{ width: 150, height: 120, objectFit: 'contain', mixBlendMode: destacada ? 'multiply' : 'normal' }} />
      <div>
        <p style={{ margin: 0, fontFamily: FUENTE, fontSize: 42, fontWeight: 700, letterSpacing: '-.02em', color: destacada ? TINTA : '#fff' }}>
          {titulo}
        </p>
        <p style={{ margin: '6px 0 0', fontFamily: FUENTE, fontSize: 28, color: destacada ? '#6d8b1c' : HUMO }}>{sub}</p>
      </div>
      <p style={{ margin: 0, fontFamily: FUENTE, fontSize: 38, fontWeight: 700, letterSpacing: '-.02em', color: destacada ? TINTA : '#fff' }}>
        {precio}
      </p>
    </div>
  );
};

export const Oferta: React.FC = () => {
  const frame = useCurrentFrame();
  return (
    <AbsoluteFill style={{ backgroundColor: TINTA }}>
      <AbsoluteFill
        style={{ background: 'radial-gradient(70% 40% at 50% 22%, rgba(200,229,74,.1) 0%, transparent 70%)' }}
      />
      <Sequence from={0} durationInFrames={56}>
        <Declaracion lineas={['Cuantas más llevás,', 'menos pagás.']} resaltar={1} duracion={56} />
      </Sequence>
      <Sequence from={52}>
        <AbsoluteFill style={{ justifyContent: 'center', padding: `0 ${SAFE.left}px` }}>
          <Titular lineas={['Elegí tu pack']} desde={4} tam={66} />
          <div style={{ height: 40 }} />
          <div style={{ display: 'grid', gap: 18 }}>
            <Fila imagen="carrusel/pack1.png" titulo="Individual" sub="Para probarla" precio={CAMPAIGN.price} desde={16} />
            <Fila imagen="carrusel/pack2.png" titulo="Dúo" sub="Ahorrás 10%" precio={CAMPAIGN.duo} desde={30} destacada />
            <Fila imagen="carrusel/pack.png" titulo="Pack x3" sub="Ahorrás 20%" precio={CAMPAIGN.pack3} desde={44} />
          </div>
          <div style={{ height: 54 }} />
          <div style={{ opacity: ease(frame - 52, 62, 86, 0, 1) }}>
            <p style={{ margin: 0, fontFamily: FUENTE, fontSize: 32, letterSpacing: '.3em', fontWeight: 700, color: LIMA }}>
              {CAMPAIGN.website.toUpperCase()}
            </p>
            <p style={{ margin: '14px 0 0', fontFamily: FUENTE, fontSize: 28, color: HUMO }}>
              Envío a todo el país con seguimiento
            </p>
          </div>
        </AbsoluteFill>
      </Sequence>
      <Destello en={52} />
      <Firma />
      <Progreso />
      <Textura vineta={0.42} />
    </AbsoluteFill>
  );
};
