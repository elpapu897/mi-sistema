/**
 * GONVRA · Asistente de la tienda
 * Cloudflare Worker que habla con Gemini y responde SOLO con datos reales de la tienda.
 *
 * Variables de entorno (se cargan en Cloudflare, NUNCA en el tema):
 *   GEMINI_API_KEY  → la clave de Google AI Studio
 */

const ORIGENES = ['https://gonvra.com', 'https://www.gonvra.com', 'https://jm60sa-cp.myshopify.com'];

// ─────────────────────────────────────────────────────────────
// TODO LO QUE EL ASISTENTE PUEDE DECIR. Si no está acá, no lo dice.
// Actualizá estos datos cuando cambie algo en la tienda.
// ─────────────────────────────────────────────────────────────
const TIENDA = `
MARCA: GONVRA (gonvra.com). Tienda argentina de cuidado personal.

PRODUCTO ÚNICO: Rasuradora Integral Recargable — Rostro y Cuerpo.
- Sirve para barba, patillas, pecho, brazos, piernas y zona íntima.
- Trae 3 peines guía para elegir el largo. Sin peine el acabado queda más al ras.
- Cabezal ancho de acero con lámina: el filo no va apoyado directo sobre la piel.
- Se carga por USB con el cable que viene en la caja (se enchufa a cualquier cargador o notebook).
- Se usa en seco, sobre piel limpia. No hace falta espuma ni gel.
- El cabezal se enjuaga bajo la canilla. No sumergirla ni cargarla mojada.
- Qué viene en la caja: rasuradora, 3 peines guía, cabezales de repuesto, cable USB y cepillo de limpieza.
- Color: negro y verde lima.

PRECIOS (si no coinciden con la web, vale lo que diga la web):
- Individual: consultar en la página.
- Packs: Dúo (2 unidades) y Pack x3 (3 unidades), más baratos por unidad.
- Se puede pagar en 3 cuotas con Mercado Pago.

PAGOS: Mercado Pago, Visa, Mastercard, American Express y Diners, en el checkout de Shopify.

ENVÍOS: a todo el país. Despacho en 24 a 48 horas hábiles. Entrega estimada de 12 a 20 días
según la zona. Se manda el código de seguimiento por mail cuando sale el paquete.
El seguimiento suele tardar unos días en mostrar movimientos: es normal.

CAMBIOS Y DEVOLUCIONES: si el producto llega fallado se coordina cambio o devolución
según la Ley 24.240 de Defensa del Consumidor. Se pide foto o video y el número de pedido.

CONTACTO HUMANO: WhatsApp +54 9 11 5376 7293.
`;

const INSTRUCCION = `
Sos el asistente de la tienda GONVRA. Atendés a clientes argentinos.

REGLAS QUE NO PODÉS ROMPER:
1. Respondé ÚNICAMENTE con la información de la ficha de abajo. Si te preguntan algo que no
   está ahí, decí que no lo tenés y ofrecé el WhatsApp. Nunca inventes datos, plazos,
   precios, descuentos, stock ni promociones.
2. No des consejos médicos ni dermatológicos. No prometas que evita irritación, foliculitis,
   pelos encarnados ni ningún resultado sobre la piel. Es una rasuradora de recorte: el
   resultado es temporal y varía según el tipo y grosor del vello.
3. No compares con marcas por nombre ni digas que es mejor que otro producto.
4. No prometas fechas exactas de entrega. Usá siempre el rango de 12 a 20 días.
5. Si te preguntan por el estado de un pedido, pedí el número de orden y derivá al WhatsApp:
   no tenés acceso a los pedidos.

CÓMO HABLÁS:
- Español rioplatense, de vos. Cercano y directo, sin exagerar.
- Máximo 3 oraciones. Sin emojis salvo que el cliente use.
- Si la consulta es de compra o reclamo, cerrá invitando al WhatsApp.

FICHA DE LA TIENDA:
${TIENDA}
`;

function cors(origen) {
  const permitido = ORIGENES.includes(origen) ? origen : ORIGENES[0];
  return {
    'Access-Control-Allow-Origin': permitido,
    'Access-Control-Allow-Methods': 'POST, OPTIONS',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '86400',
  };
}

export default {
  async fetch(request, env) {
    const origen = request.headers.get('Origin') || '';
    const cabeceras = { ...cors(origen), 'Content-Type': 'application/json; charset=utf-8' };

    if (request.method === 'OPTIONS') return new Response(null, { headers: cors(origen) });
    if (request.method !== 'POST') {
      return new Response(JSON.stringify({ respuesta: 'Método no permitido.' }), { status: 405, headers: cabeceras });
    }

    let mensaje = '';
    try {
      const cuerpo = await request.json();
      mensaje = String(cuerpo.mensaje || '').slice(0, 500).trim();
    } catch (_) {
      mensaje = '';
    }
    if (!mensaje) {
      return new Response(JSON.stringify({ respuesta: 'Contame tu consulta y te ayudo.' }), { headers: cabeceras });
    }

    try {
      const r = await fetch(
        'https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key=' + env.GEMINI_API_KEY,
        {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            system_instruction: { parts: [{ text: INSTRUCCION }] },
            contents: [{ role: 'user', parts: [{ text: mensaje }] }],
            generationConfig: { temperature: 0.3, maxOutputTokens: 220 },
            safetySettings: [
              { category: 'HARM_CATEGORY_SEXUALLY_EXPLICIT', threshold: 'BLOCK_ONLY_HIGH' },
            ],
          }),
        }
      );

      const data = await r.json();
      const texto = data?.candidates?.[0]?.content?.parts?.[0]?.text;

      return new Response(
        JSON.stringify({
          respuesta: texto
            ? texto.trim()
            : 'No pude procesar eso. Escribime por WhatsApp y te respondo yo.',
        }),
        { headers: cabeceras }
      );
    } catch (_) {
      return new Response(
        JSON.stringify({ respuesta: 'Se me cortó la conexión. Probá por WhatsApp y te contesto.' }),
        { headers: cabeceras }
      );
    }
  },
};
