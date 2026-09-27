export type Escena = {
  clip: string;
  desde: number;      // segundo del clip donde arranca
  frames: number;     // duración en cuadros (30 fps)
  titulo?: string;
  bajada?: string;
  posicion?: 'arriba' | 'abajo';
  sticker?: string;   // cartel blanco tipo TikTok
  sticker2?: string;  // segundo cartel, entra más tarde
  zoom?: number;      // 1 = sin zoom extra
};

export type Cierre = {
  titulo: string;
  bajada: string;
  boton: string;
  precio: string;
  imagen: string;
};

export type AnuncioGuion = {
  id: string;
  escenas: Escena[];
  cierre: Cierre;
};

import {CAMPAIGN} from './campaign';

const CIERRE: Cierre = {
  titulo: 'Rostro y cuerpo,\nun solo equipo',
  bajada: 'Envío a todo el país con seguimiento',
  boton: CAMPAIGN.website,
  precio: CAMPAIGN.price,
  imagen: 'carrusel/producto.jpg',
};

export const anuncios: AnuncioGuion[] = [
  {
    // 14 s · la lámina: el argumento técnico, con el macro del filo
    id: 'Anuncio-Lamina',
    escenas: [
      { clip: 'filo.mp4', desde: 1.0, frames: 90, zoom: 1.0,
        sticker: 'MIRÁ EL CABEZAL\nDE CERCA 👀' },
      { clip: 'filo.mp4', desde: 3.2, frames: 75, zoom: 1.15,
        sticker: 'ESA LÁMINA VA ENTRE\nEL FILO Y LA PIEL' },
      { clip: 'rostro.mp4', desde: 0.6, frames: 90, titulo: 'Por eso no\narrastra el filo', posicion: 'abajo' },
      { clip: 'agua.mp4', desde: 0.6, frames: 75, titulo: 'Y se enjuaga\nbajo la canilla', posicion: 'abajo' },
    ],
    cierre: CIERRE,
  },
  {
    // 13 s · la mesada: producto puro, para retargeting
    id: 'Anuncio-Mesada',
    escenas: [
      { clip: 'mesada.mp4', desde: 0.3, frames: 90, titulo: 'Una sola\nrasuradora', bajada: 'Rostro, cuerpo y zona íntima', posicion: 'abajo' },
      { clip: 'caja.mp4', desde: 0.8, frames: 90, titulo: '3 peines, cabezales,\nUSB y cepillo', bajada: 'Todo en la caja', posicion: 'abajo' },
      { clip: 'brazo.mp4', desde: 1.2, frames: 90, titulo: 'Se usa en seco', bajada: 'Sin espuma ni gel', posicion: 'abajo' },
    ],
    cierre: CIERRE,
  },

  {
    // 17 s · formato TikTok: gancho de problema con carteles
    id: 'Anuncio-Gancho',
    escenas: [
      {
        clip: 'brazo.mp4', desde: 1.4, frames: 75, zoom: 1.35,
        sticker: '¿LA MAQUINITA TE\nDEJA LA PIEL ARDIENDO? 😖',
      },
      {
        clip: 'rostro.mp4', desde: 0.5, frames: 75, zoom: 1.3,
        sticker: 'EL PROBLEMA NO SOS VOS',
        sticker2: 'ES LA HOJA PEGADA A LA PIEL',
      },
      {
        clip: 'orbita.mp4', desde: 0.4, frames: 90, zoom: 1.05,
        sticker: 'ESTA TIENE LÁMINA\nDE ACERO EN EL MEDIO 👀',
      },
      {
        clip: 'cuerpo.mp4', desde: 2.2, frames: 90,
        sticker: 'NO ARRASTRA EL FILO\nSOBRE LA PIEL',
      },
      {
        clip: 'agua.mp4', desde: 0.6, frames: 75,
        sticker: 'Y SE LAVA\nBAJO LA CANILLA 💧',
      },
    ],
    cierre: CIERRE,
  },
  {
    // 18 s · gancho del problema → solución → demostración → cierre
    id: 'Anuncio-Problema',
    escenas: [
      { clip: 'cajon.mp4', desde: 0.2, frames: 105, titulo: '¿Un aparato\npara cada zona?', bajada: 'Y ninguno hace todo', posicion: 'arriba' },
      { clip: 'orbita.mp4', desde: 0.3, frames: 90, titulo: 'Una sola\nrasuradora', bajada: 'Rostro + cuerpo', posicion: 'abajo' },
      { clip: 'rostro.mp4', desde: 0.4, frames: 105, titulo: 'La barba,\nal largo que quieras', posicion: 'abajo' },
      { clip: 'cuerpo.mp4', desde: 2.0, frames: 105, titulo: 'Y el cuerpo,\ncon la misma', posicion: 'abajo' },
      { clip: 'caja.mp4', desde: 0.8, frames: 105, titulo: 'Peines, cabezales,\nUSB y cepillo', bajada: 'Todo incluido', posicion: 'abajo' },
    ],
    cierre: CIERRE,
  },
  {
    // 12 s · directo al producto, para retargeting
    id: 'Anuncio-Producto',
    escenas: [
      { clip: 'orbita.mp4', desde: 0.2, frames: 75, titulo: 'Rasuradora\nintegral', bajada: 'Recargable por USB', posicion: 'abajo' },
      { clip: 'rostro.mp4', desde: 0.4, frames: 90, titulo: 'Barba y patillas', posicion: 'abajo' },
      { clip: 'brazo.mp4', desde: 0.3, frames: 90, titulo: 'Brazos, pecho\ny piernas', posicion: 'abajo' },
      { clip: 'agua.mp4', desde: 0.5, frames: 75, titulo: 'Se enjuaga\nbajo el agua', posicion: 'abajo' },
    ],
    cierre: CIERRE,
  },
  {
    // 10 s · demostración pura, sin promesas
    id: 'Anuncio-Demo',
    escenas: [
      { clip: 'rostro.mp4', desde: 0.4, frames: 105, titulo: 'Mirá cómo queda', posicion: 'abajo' },
      { clip: 'cuerpo.mp4', desde: 2.2, frames: 105, posicion: 'abajo' },
      { clip: 'caja.mp4', desde: 0.8, frames: 90, titulo: 'Todo lo que trae', posicion: 'abajo' },
    ],
    cierre: CIERRE,
  },
];
