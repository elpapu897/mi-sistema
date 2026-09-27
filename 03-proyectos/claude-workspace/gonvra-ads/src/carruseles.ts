/**
 * Carruseles de GONVRA.
 * Cada objeto de `carruseles` es un carrusel; cada `slide` es una placa.
 * Para agregar uno nuevo: copiá un bloque, cambiá los textos y renderizá.
 */

import {CAMPAIGN} from './campaign';

export type Slide =
  | { tipo: 'portada'; kicker?: string; titulo: string; bajada?: string; imagen: string }
  | { tipo: 'texto'; kicker?: string; titulo: string; cuerpo?: string; fondo?: 'tinta' | 'papel' | 'lima' }
  | { tipo: 'imagen'; imagen: string; sticker?: string; pie?: string }
  | { tipo: 'dato'; numero: string; titulo: string; cuerpo?: string }
  | { tipo: 'lista'; kicker?: string; titulo: string; items: string[]; imagen?: string }
  | { tipo: 'versus'; titulo: string; mia: string[]; otra: string[]; etiquetaMia?: string; etiquetaOtra?: string }
  | { tipo: 'cierre'; titulo: string; bajada?: string; precio?: string; boton: string; imagen: string };

export type Carrusel = {
  id: string;
  formato: 'tiktok' | 'instagram';
  slides: Slide[];
};

export const carruseles: Carrusel[] = [
  {
    // Gancho de problema → solución. El que más funciona en frío.
    id: 'Carrusel-Problema',
    formato: 'tiktok',
    slides: [
      {
        tipo: 'portada',
        kicker: 'Cuidado personal',
        titulo: '¿Un aparato para\ncada parte del cuerpo?',
        bajada: 'Y ninguno hace todo bien',
        imagen: 'carrusel/kit.jpg',
      },
      {
        tipo: 'texto',
        fondo: 'tinta',
        kicker: 'El problema',
        titulo: 'La maquinita arrastra\nla hoja sobre la piel',
        cuerpo: 'Por eso queda ardor, tirones y esa sensación de piel irritada al otro día.',
      },
      {
        tipo: 'imagen',
        imagen: 'carrusel/filo.jpg',
        sticker: 'Esta tiene lámina\nde acero en el medio',
        pie: 'El filo nunca toca la piel directamente.',
      },
      {
        tipo: 'lista',
        kicker: 'Una sola herramienta',
        titulo: 'Rostro, cuerpo\ny zona íntima',
        items: [
          'Peines de 1, 3 y 5 mm: elegís el largo',
          'Se usa en seco, sin espuma ni gel',
          'Se enjuaga bajo la canilla',
          'Carga por USB, con el cable del celu',
        ],
        imagen: 'carrusel/uso.jpg',
      },
      {
        tipo: 'cierre',
        titulo: 'Una sola rasuradora\npara toda tu rutina',
        bajada: 'Envío a todo el país con seguimiento',
        precio: CAMPAIGN.price,
        boton: CAMPAIGN.website,
        imagen: 'carrusel/producto.jpg',
      },
    ],
  },
  {
    // Comparativa. Para público que ya conoce el producto.
    id: 'Carrusel-Comparativa',
    formato: 'tiktok',
    slides: [
      {
        tipo: 'portada',
        kicker: 'Comparación honesta',
        titulo: 'Rasuradora integral\nvs. maquinita común',
        imagen: 'carrusel/producto.jpg',
      },
      {
        tipo: 'versus',
        titulo: 'Lo que cambia',
        etiquetaMia: 'Integral',
        etiquetaOtra: 'Común',
        mia: [
          'Rostro y cuerpo',
          'Peines de 1, 3 y 5 mm',
          'Carga USB',
          'Cabezal reemplazable',
        ],
        otra: ['Solo una zona', 'Un largo fijo', 'A pila', 'Se tira entera'],
      },
      {
        tipo: 'dato',
        numero: '0',
        titulo: 'Cuchillas descartables',
        cuerpo: 'No comprás repuestos todos los meses. El cabezal se cambia cuando hace falta.',
      },
      {
        tipo: 'imagen',
        imagen: 'carrusel/agua.jpg',
        sticker: 'Se limpia\nbajo el agua',
      },
      {
        tipo: 'cierre',
        titulo: 'Probala sin vueltas',
        bajada: 'Si llega fallada, lo resolvemos',
        precio: CAMPAIGN.price,
        boton: CAMPAIGN.website,
        imagen: 'carrusel/producto.jpg',
      },
    ],
  },
  {
    // Educativo: cómo se usa. Bueno para retención y para guardados.
    id: 'Carrusel-Como-Se-Usa',
    formato: 'tiktok',
    slides: [
      {
        tipo: 'portada',
        kicker: 'Guía rápida',
        titulo: 'Cómo se usa\nen 3 pasos',
        imagen: 'carrusel/producto.jpg',
      },
      {
        tipo: 'lista',
        kicker: 'Paso 1',
        titulo: 'Elegí el largo',
        items: ['Peine de 1, 3 o 5 mm', 'Sin peine queda más al ras', 'Se cambia sin herramientas'],
        imagen: 'carrusel/kit.jpg',
      },
      {
        tipo: 'lista',
        kicker: 'Paso 2',
        titulo: 'Pasala en seco',
        items: ['Piel limpia y seca', 'Movimientos suaves', 'En zonas sensibles, probá primero en un área chica'],
        imagen: 'carrusel/uso.jpg',
      },
      {
        tipo: 'lista',
        kicker: 'Paso 3',
        titulo: 'Limpiala y cargala',
        items: ['Enjuagá el cabezal', 'Cepillo incluido en la caja', 'Cargá con cualquier cable USB'],
        imagen: 'carrusel/agua.jpg',
      },
      {
        tipo: 'cierre',
        titulo: 'Rostro y cuerpo,\nun solo equipo',
        bajada: 'Envío a todo el país',
        precio: CAMPAIGN.price,
        boton: CAMPAIGN.website,
        imagen: 'carrusel/producto.jpg',
      },
    ],
  },
];
