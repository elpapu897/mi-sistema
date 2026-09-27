// Plan de B-rolls.
// `at` = segundo del video original donde entra el insert (pico de energia del audio:
// grito / reaccion / puteada, detectado por RMS sobre la pista de voz).
// `trim` = segundo del clip de stock desde el que se empieza a reproducir.
// Todos los clips son de mixkit.co (Mixkit License: uso libre, sin atribucion).

export type Broll = {
  at: number;
  dur: number;
  file: string;
  trim: number;
  label: string;
  why: string;
};

export const BROLLS: Broll[] = [
  { at: 24.0, dur: 1.8, file: 'broll/explosion.mp4', trim: 1.0, label: 'EXPLOSION', why: '"wow que divertido" — sarcasmo' },
  { at: 51.5, dur: 1.8, file: 'broll/lightning.mp4', trim: 1.0, label: 'CAOS', why: '"sali, sali" — caos total' },
  { at: 78.0, dur: 1.8, file: 'broll/fire.mp4', trim: 6.0, label: 'RAGE', why: 'puteada al juego' },
  { at: 130.0, dur: 1.8, file: 'broll/waterfall.mp4', trim: 1.0, label: 'CAIDA', why: '"noooo" — se cae' },
  { at: 155.0, dur: 1.8, file: 'broll/racing.mp4', trim: 1.5, label: 'COMPETENCIA', why: '"cuanto les va a costar este juego"' },
  { at: 201.5, dur: 1.6, file: 'broll/neon.mp4', trim: 0.3, label: 'RESET', why: 'cambio de ronda' },
  { at: 233.0, dur: 2.0, file: 'broll/celebration.mp4', trim: 8.0, label: 'GG', why: '"yeeee, bien boludo" — festejo' },
  { at: 266.5, dur: 2.0, file: 'broll/parkour.mp4', trim: 4.0, label: 'PARKOUR', why: '"son malardos los parkour"' },
  { at: 319.5, dur: 1.8, file: 'broll/speed.mp4', trim: 1.0, label: 'CLUTCH', why: '"mira donde me mori"' },
  { at: 345.5, dur: 1.8, file: 'broll/jumping.mp4', trim: 1.5, label: 'SALTO', why: '"hay que saltar"' },
  { at: 420.5, dur: 1.6, file: 'broll/time.mp4', trim: 3.0, label: 'ESPERANDO', why: 'bajon de ritmo, hay que cortar' },
  { at: 445.5, dur: 1.8, file: 'broll/tunnel.mp4', trim: 3.0, label: 'PA DELANTE', why: '"Franco, avanza para adelante"' },
  { at: 526.0, dur: 1.8, file: 'broll/smoke.mp4', trim: 3.0, label: 'NO SALE', why: '"no puedo sacar esta mierda"' },
  { at: 572.0, dur: 2.2, file: 'broll/particles.mp4', trim: 1.0, label: 'OTRO JUEGO', why: 'cierre — "otro juego pasado"' },
];
