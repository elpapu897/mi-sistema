/* ═══════════════════════════════════════════════════════════
   LA DIEZ · cobros con Mercado Pago (Checkout Pro)

   IMPORTANTE — leé esto antes de usarlo:

   El juego NUNCA pide el número de tarjeta. Este módulo crea una
   "preferencia de pago" y devuelve un link de Mercado Pago. El jugador
   va a la página de Mercado Pago, paga ahí, y vuelve al juego.
   Esa es la única forma segura y legal de cobrar: los datos de la
   tarjeta jamás pasan por tu servidor ni por el HTML del juego.

   Para que funcione necesitás:
   1. Una cuenta de Mercado Pago a tu nombre (o de tu empresa).
   2. Entrar a mercadopago.com.ar/developers → Tus integraciones →
      crear una aplicación → copiar el Access Token de producción.
   3. Poner ese token en la variable de entorno MP_TOKEN.
   4. Tener el servidor con HTTPS público (Render, Railway, etc.).

   Mientras no configures MP_TOKEN, los endpoints responden
   "pagos no configurados" y el juego muestra la tienda sin compras.
   ═══════════════════════════════════════════════════════════ */

const TOKEN = process.env.MP_TOKEN || '';
const URL_JUEGO = process.env.URL_JUEGO || 'https://tu-juego.com';

// catálogo: los precios los ponés vos, en pesos argentinos
const PRODUCTOS = {
  gemas_100:  { titulo: '100 gemas',   gemas: 100,  precio: 1999 },
  gemas_550:  { titulo: '550 gemas',   gemas: 550,  precio: 8999 },
  gemas_1200: { titulo: '1200 gemas',  gemas: 1200, precio: 17999 },
  pase:       { titulo: 'Pase Leyenda', gemas: 0,   precio: 4999, pase: true },
};

/** compras confirmadas: id de jugador -> lo que le corresponde
 *  En un juego de verdad esto va a una base de datos, no a memoria. */
const acreditado = new Map();

function json(res, code, obj) {
  res.writeHead(code, { 'Content-Type': 'application/json', 'Access-Control-Allow-Origin': '*' });
  res.end(JSON.stringify(obj));
}

async function crearPreferencia(req, res, body) {
  if (!TOKEN) return json(res, 503, { ok: false, error: 'pagos_no_configurados' });

  const prod = PRODUCTOS[body.producto];
  if (!prod) return json(res, 400, { ok: false, error: 'producto_invalido' });
  const jugador = String(body.jugador || '').slice(0, 60);
  if (!jugador) return json(res, 400, { ok: false, error: 'falta_jugador' });

  try {
    const r = await fetch('https://api.mercadopago.com/checkout/preferences', {
      method: 'POST',
      headers: { 'Authorization': 'Bearer ' + TOKEN, 'Content-Type': 'application/json' },
      body: JSON.stringify({
        items: [{
          title: 'LA DIEZ · ' + prod.titulo,
          quantity: 1,
          unit_price: prod.precio,
          currency_id: 'ARS'
        }],
        external_reference: jugador + '::' + body.producto,
        back_urls: {
          success: URL_JUEGO + '?pago=ok',
          failure: URL_JUEGO + '?pago=error',
          pending: URL_JUEGO + '?pago=pendiente'
        },
        auto_return: 'approved',
        notification_url: (process.env.URL_SERVIDOR || '') + '/pagos/webhook'
      })
    });
    const d = await r.json();
    if (!d.init_point) return json(res, 502, { ok: false, error: 'mp_sin_link', detalle: d });
    json(res, 200, { ok: true, link: d.init_point, id: d.id });
  } catch (e) {
    json(res, 502, { ok: false, error: 'mp_no_responde' });
  }
}

/** Mercado Pago avisa acá cuando alguien paga. Verificamos con su API
 *  (nunca confiar en lo que llega en el webhook sin chequear). */
async function webhook(req, res, body) {
  if (!TOKEN) return json(res, 200, { ok: true });
  try {
    const id = body?.data?.id;
    if (!id) return json(res, 200, { ok: true });
    const r = await fetch('https://api.mercadopago.com/v1/payments/' + id, {
      headers: { 'Authorization': 'Bearer ' + TOKEN }
    });
    const pago = await r.json();
    if (pago.status === 'approved') {
      const [jugador, producto] = String(pago.external_reference || '').split('::');
      const prod = PRODUCTOS[producto];
      if (jugador && prod) {
        const actual = acreditado.get(jugador) || { gemas: 0, pase: false, pagos: [] };
        if (!actual.pagos.includes(String(id))) {
          actual.gemas += prod.gemas;
          if (prod.pase) actual.pase = true;
          actual.pagos.push(String(id));
          acreditado.set(jugador, actual);
          console.log('Pago acreditado a', jugador, '->', prod.titulo);
        }
      }
    }
    json(res, 200, { ok: true });
  } catch (e) {
    json(res, 200, { ok: true });
  }
}

/** el juego pregunta cada tanto si le acreditaron algo */
function consultar(req, res, jugador) {
  if (!TOKEN) return json(res, 200, { ok: false, error: 'pagos_no_configurados' });
  const a = acreditado.get(jugador) || { gemas: 0, pase: false };
  acreditado.set(jugador, { gemas: 0, pase: false, pagos: (acreditado.get(jugador)?.pagos) || [] });
  json(res, 200, { ok: true, gemas: a.gemas, pase: a.pase });
}

/** se engancha al servidor HTTP principal */
function manejar(req, res) {
  const u = new URL(req.url, 'http://x');

  if (req.method === 'OPTIONS') {
    res.writeHead(204, {
      'Access-Control-Allow-Origin': '*',
      'Access-Control-Allow-Headers': 'Content-Type',
      'Access-Control-Allow-Methods': 'POST,GET,OPTIONS'
    });
    return res.end(), true;
  }

  if (u.pathname === '/pagos/config') {
    json(res, 200, { ok: true, activo: !!TOKEN, productos: PRODUCTOS });
    return true;
  }
  if (u.pathname === '/pagos/estado') {
    consultar(req, res, u.searchParams.get('jugador') || '');
    return true;
  }
  if (u.pathname === '/pagos/crear' || u.pathname === '/pagos/webhook') {
    let data = '';
    req.on('data', c => { data += c; if (data.length > 1e5) req.destroy(); });
    req.on('end', () => {
      let body = {};
      try { body = JSON.parse(data || '{}'); } catch (_) {}
      if (u.pathname === '/pagos/crear') crearPreferencia(req, res, body);
      else webhook(req, res, body);
    });
    return true;
  }
  return false;
}

module.exports = { manejar, PRODUCTOS, activo: !!TOKEN };
