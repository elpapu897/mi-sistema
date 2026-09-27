import React from 'react';
import { AbsoluteFill, Img, staticFile, useCurrentFrame } from 'remotion';
import type { Slide } from './carruseles';

const TINTA = '#101a16';
const LIMA = '#c8e54a';
const PAPEL = '#f7f6f1';
const OLIVA = '#6d8b1c';
const MUTED = '#6b7570';

const fuente =
  '"Helvetica Neue", Helvetica, "Segoe UI", Inter, system-ui, -apple-system, sans-serif';

/* Ola estática de la marca, para el pie de las placas */
const Ola: React.FC<{ color: string; alto?: number }> = ({ color, alto = 120 }) => (
  <svg
    viewBox="0 0 1440 150"
    preserveAspectRatio="none"
    style={{ position: 'absolute', bottom: -2, left: 0, width: '100%', height: alto, display: 'block' }}
  >
    <path
      d="M0,70 q90,-40 180,0 t180,0 t180,0 t180,0 t180,0 t180,0 t180,0 t180,0 L1440,150 L0,150 Z"
      fill={color}
      opacity=".35"
    />
    <path
      d="M0,95 q90,-38 180,0 t180,0 t180,0 t180,0 t180,0 t180,0 t180,0 t180,0 L1440,150 L0,150 Z"
      fill={color}
    />
  </svg>
);

const Marca: React.FC<{ claro?: boolean }> = ({ claro }) => (
  <div
    style={{
      position: 'absolute',
      top: 62,
      left: 72,
      fontFamily: fuente,
      fontSize: 30,
      fontWeight: 850,
      letterSpacing: '.34em',
      color: claro ? '#fff' : TINTA,
    }}
  >
    GONVRA
  </div>
);

const Paso: React.FC<{ n: number; total: number; claro?: boolean }> = ({ n, total, claro }) => (
  <div
    style={{
      position: 'absolute',
      top: 62,
      right: 72,
      display: 'flex',
      gap: 10,
      alignItems: 'center',
    }}
  >
    {Array.from({ length: total }).map((_, i) => (
      <span
        key={i}
        style={{
          width: i === n ? 28 : 10,
          height: 10,
          borderRadius: 99,
          background: i === n ? LIMA : claro ? 'rgba(255,255,255,.35)' : 'rgba(16,26,22,.2)',
        }}
      />
    ))}
  </div>
);

const Kicker: React.FC<{ texto: string; claro?: boolean }> = ({ texto, claro }) => (
  <p
    style={{
      margin: '0 0 22px',
      fontFamily: fuente,
      fontSize: 27,
      fontWeight: 850,
      letterSpacing: '.18em',
      textTransform: 'uppercase',
      color: claro ? LIMA : OLIVA,
    }}
  >
    {texto}
  </p>
);

export const Carrusel: React.FC<{ slides: Slide[] }> = ({ slides }) => {
  const frame = useCurrentFrame();
  const s = slides[Math.min(frame, slides.length - 1)];
  const total = slides.length;

  const marco: React.CSSProperties = {
    fontFamily: fuente,
    padding: '150px 180px 300px 72px',
    justifyContent: 'center',
  };

  if (s.tipo === 'portada') {
    return (
      <AbsoluteFill style={{ backgroundColor: TINTA }}>
        <AbsoluteFill>
          <Img src={staticFile(s.imagen)} style={{ width: '100%', height: '100%', objectFit: 'cover' }} />
        </AbsoluteFill>
        <AbsoluteFill
          style={{
            background:
              'linear-gradient(180deg, rgba(16,26,22,.72) 0%, rgba(16,26,22,.25) 38%, rgba(16,26,22,.92) 100%)',
          }}
        />
        <Marca claro />
        <Paso n={0} total={total} claro />
        <AbsoluteFill style={{ ...marco, justifyContent: 'flex-end' }}>
          {s.kicker && <Kicker texto={s.kicker} claro />}
          <h1
            style={{
              margin: 0,
              fontSize: 104,
              fontWeight: 800,
              lineHeight: 1,
              letterSpacing: '-.04em',
              color: '#fff',
              whiteSpace: 'pre-line',
            }}
          >
            {s.titulo}
          </h1>
          {s.bajada && (
            <p style={{ margin: '30px 0 0', fontSize: 40, lineHeight: 1.35, color: '#c9d2c6' }}>{s.bajada}</p>
          )}
        </AbsoluteFill>
      </AbsoluteFill>
    );
  }

  if (s.tipo === 'texto') {
    const fondo = s.fondo === 'lima' ? LIMA : s.fondo === 'papel' ? PAPEL : TINTA;
    const claro = s.fondo !== 'papel' && s.fondo !== 'lima';
    return (
      <AbsoluteFill style={{ backgroundColor: fondo }}>
        <Marca claro={claro} />
        <Paso n={frame} total={total} claro={claro} />
        <AbsoluteFill style={marco}>
          {s.kicker && <Kicker texto={s.kicker} claro={claro} />}
          <h2
            style={{
              margin: 0,
              fontSize: 92,
              fontWeight: 800,
              lineHeight: 1.04,
              letterSpacing: '-.04em',
              color: claro ? '#fff' : TINTA,
              whiteSpace: 'pre-line',
            }}
          >
            {s.titulo}
          </h2>
          {s.cuerpo && (
            <p
              style={{
                margin: '38px 0 0',
                maxWidth: '22ch',
                fontSize: 42,
                lineHeight: 1.45,
                color: claro ? '#a8b3a6' : MUTED,
              }}
            >
              {s.cuerpo}
            </p>
          )}
        </AbsoluteFill>
        {claro && <Ola color="#17251e" />}
      </AbsoluteFill>
    );
  }

  if (s.tipo === 'imagen') {
    return (
      <AbsoluteFill style={{ backgroundColor: TINTA }}>
        <AbsoluteFill>
          <Img src={staticFile(s.imagen)} style={{ width: '100%', height: '100%', objectFit: 'cover' }} />
        </AbsoluteFill>
        <AbsoluteFill
          style={{
            background: 'linear-gradient(180deg, rgba(16,26,22,.5) 0%, rgba(16,26,22,0) 40%, rgba(16,26,22,.8) 100%)',
          }}
        />
        <Marca claro />
        <Paso n={frame} total={total} claro />
        {s.sticker && (
          <AbsoluteFill style={{ justifyContent: 'center', alignItems: 'center', padding: 80 }}>
            <div
              style={{
                fontFamily: fuente,
                padding: '34px 46px',
                borderRadius: 20,
                background: 'rgba(255,255,255,.96)',
                boxShadow: '0 18px 60px rgba(0,0,0,.35)',
                fontSize: 68,
                fontWeight: 800,
                lineHeight: 1.1,
                letterSpacing: '-.02em',
                color: '#111',
                textAlign: 'center',
                whiteSpace: 'pre-line',
                transform: 'rotate(-1.4deg)',
              }}
            >
              {s.sticker}
            </div>
          </AbsoluteFill>
        )}
        {s.pie && (
          <AbsoluteFill style={{ justifyContent: 'flex-end', padding: '0 180px 300px 72px' }}>
            <p style={{ margin: 0, fontSize: 38, lineHeight: 1.4, color: '#d5dbd2' }}>{s.pie}</p>
          </AbsoluteFill>
        )}
      </AbsoluteFill>
    );
  }

  if (s.tipo === 'dato') {
    return (
      <AbsoluteFill style={{ backgroundColor: PAPEL }}>
        <Marca />
        <Paso n={frame} total={total} />
        <AbsoluteFill style={marco}>
          <b style={{ fontSize: 380, fontWeight: 800, lineHeight: .8, letterSpacing: '-.06em', color: OLIVA }}>
            {s.numero}
          </b>
          <h2 style={{ margin: '30px 0 0', fontSize: 76, fontWeight: 800, lineHeight: 1.05, letterSpacing: '-.035em', color: TINTA }}>
            {s.titulo}
          </h2>
          {s.cuerpo && (
            <p style={{ margin: '26px 0 0', maxWidth: '24ch', fontSize: 40, lineHeight: 1.45, color: MUTED }}>
              {s.cuerpo}
            </p>
          )}
        </AbsoluteFill>
        <Ola color="#e3e8d6" alto={140} />
      </AbsoluteFill>
    );
  }

  if (s.tipo === 'lista') {
    return (
      <AbsoluteFill style={{ backgroundColor: PAPEL }}>
        <Marca />
        <Paso n={frame} total={total} />
        <AbsoluteFill style={{ ...marco, justifyContent: 'center' }}>
          {s.kicker && <Kicker texto={s.kicker} />}
          <h2 style={{ margin: 0, fontSize: 84, fontWeight: 800, lineHeight: 1.04, letterSpacing: '-.04em', color: TINTA, whiteSpace: 'pre-line' }}>
            {s.titulo}
          </h2>
          {s.imagen && (
            <div style={{ margin: '44px 0 10px', borderRadius: 26, overflow: 'hidden', height: 620 }}>
              <Img src={staticFile(s.imagen)} style={{ width: '100%', height: '100%', objectFit: 'cover' }} />
            </div>
          )}
          <ul style={{ margin: '30px 0 0', padding: 0, listStyle: 'none', display: 'grid', gap: 22 }}>
            {s.items.map((item, i) => (
              <li key={i} style={{ display: 'grid', gridTemplateColumns: '46px 1fr', gap: 20, alignItems: 'start' }}>
                <span
                  style={{
                    display: 'grid',
                    placeItems: 'center',
                    width: 46,
                    height: 46,
                    borderRadius: 99,
                    background: TINTA,
                    color: LIMA,
                    fontSize: 24,
                    fontWeight: 900,
                  }}
                >
                  ✓
                </span>
                <span style={{ fontSize: 38, lineHeight: 1.32, color: TINTA }}>{item}</span>
              </li>
            ))}
          </ul>
        </AbsoluteFill>
      </AbsoluteFill>
    );
  }

  if (s.tipo === 'versus') {
    const Col: React.FC<{ etiqueta: string; items: string[]; oscura?: boolean }> = ({ etiqueta, items, oscura }) => (
      <div
        style={{
          flex: 1,
          padding: '38px 30px',
          borderRadius: 26,
          background: oscura ? TINTA : '#fff',
          border: oscura ? 'none' : '2px solid #e2e5dd',
        }}
      >
        <p
          style={{
            margin: '0 0 26px',
            fontSize: 30,
            fontWeight: 850,
            letterSpacing: '.12em',
            textTransform: 'uppercase',
            color: oscura ? LIMA : MUTED,
          }}
        >
          {etiqueta}
        </p>
        <ul style={{ margin: 0, padding: 0, listStyle: 'none', display: 'grid', gap: 22 }}>
          {items.map((t, i) => (
            <li key={i} style={{ display: 'grid', gridTemplateColumns: '38px 1fr', gap: 14, alignItems: 'start' }}>
              <span style={{ fontSize: 32, color: oscura ? LIMA : '#b9c1b4' }}>{oscura ? '✓' : '✕'}</span>
              <span style={{ fontSize: 32, lineHeight: 1.3, color: oscura ? '#fff' : MUTED }}>{t}</span>
            </li>
          ))}
        </ul>
      </div>
    );
    return (
      <AbsoluteFill style={{ backgroundColor: PAPEL }}>
        <Marca />
        <Paso n={frame} total={total} />
        <AbsoluteFill style={{ ...marco, justifyContent: 'center' }}>
          <h2 style={{ margin: '0 0 46px', fontSize: 82, fontWeight: 800, lineHeight: 1.04, letterSpacing: '-.04em', color: TINTA }}>
            {s.titulo}
          </h2>
          <div style={{ display: 'flex', gap: 22, alignItems: 'stretch' }}>
            <Col etiqueta={s.etiquetaMia ?? 'Esta'} items={s.mia} oscura />
            <Col etiqueta={s.etiquetaOtra ?? 'Otras'} items={s.otra} />
          </div>
        </AbsoluteFill>
      </AbsoluteFill>
    );
  }

  // cierre
  return (
    <AbsoluteFill style={{ backgroundColor: TINTA, alignItems: 'center', justifyContent: 'center', padding: 90, fontFamily: fuente }}>
      <Marca claro />
      <Paso n={total - 1} total={total} claro />
      <div style={{ width: 700, height: 700, padding: 26, borderRadius: 40, background: PAPEL, boxShadow: '0 40px 90px rgba(0,0,0,.45)' }}>
        <Img src={staticFile(s.imagen)} style={{ width: '100%', height: '100%', objectFit: 'cover', objectPosition: 'center 48%', borderRadius: 22 }} />
      </div>
      <h2
        style={{
          margin: '54px 0 0',
          fontSize: 84,
          fontWeight: 800,
          lineHeight: 1.04,
          letterSpacing: '-.04em',
          color: '#fff',
          textAlign: 'center',
          whiteSpace: 'pre-line',
        }}
      >
        {s.titulo}
      </h2>
      {s.bajada && <p style={{ margin: '26px 0 0', fontSize: 38, color: '#a8b3a6', textAlign: 'center' }}>{s.bajada}</p>}
      {s.precio && (
        <p style={{ margin: '18px 0 0', fontSize: 62, fontWeight: 800, color: LIMA }}>{s.precio}</p>
      )}
      <div
        style={{
          marginTop: 44,
          padding: '30px 66px',
          borderRadius: 22,
          background: LIMA,
          color: '#1b2410',
          fontSize: 40,
          fontWeight: 800,
          letterSpacing: '.12em',
          textTransform: 'uppercase',
        }}
      >
        {s.boton}
      </div>
      <Ola color="#16241d" alto={150} />
    </AbsoluteFill>
  );
};
