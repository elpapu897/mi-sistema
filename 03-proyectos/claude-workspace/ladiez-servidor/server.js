/* ═══════════════════════════════════════════════════════════
   LA DIEZ · servidor de salas online
   Node.js + WebSocket. Sin base de datos: todo vive en memoria.

   Levantarlo local:   npm install && npm start
   Queda escuchando en http://localhost:8080
   ═══════════════════════════════════════════════════════════ */

const http = require('http');
const fs = require('fs');
const path = require('path');
const { WebSocketServer } = require('ws');
const pagos = require('./pagos');

const PUERTO = process.env.PORT || 8080;
const LETRAS = 'ABCDEFGHJKLMNPQRSTUVWXYZ23456789';
const VIDA_SALA_MS = 1000 * 60 * 60;      // una sala vacía muere en 1 hora
const LATIDO_MS = 30000;                   // ping cada 30 s
const ARCHIVO_JUEGO = path.resolve(__dirname, '..', 'ladiez.html');
const DIRECTORIO_ASSETS = path.resolve(__dirname, '..', 'assets');
const ARCHIVO_RANKING = path.resolve(__dirname, 'ranking-comunidad.json');

function cargarRanking() {
  try {
    const datos = JSON.parse(fs.readFileSync(ARCHIVO_RANKING, 'utf8'));
    return Array.isArray(datos) ? datos.slice(0, 5000) : [];
  } catch (_) { return []; }
}

let rankingComunidad = cargarRanking();
const ultimaActualizacion = new Map();

function textoSeguro(valor, largo) {
  return String(valor || '').replace(/[<>&"'`\u0000-\u001f]/g, '').replace(/\s+/g, ' ').trim().slice(0, largo);
}

function numeroSeguro(valor, min, max) {
  const n = Number(valor);
  return Number.isFinite(n) ? Math.max(min, Math.min(max, Math.round(n))) : min;
}

function puntosComunidad(j) {
  return Math.round(j.partidos * 120 + j.nivel * 900 + j.media * 80 + Math.log10(j.dinero + 1) * 1200);
}

function rankingOrdenado(orden) {
  const lista = rankingComunidad.map(j => ({ ...j, puntos: puntosComunidad(j) }));
  if (orden === 'partidos') lista.sort((a, b) => b.partidos - a.partidos || b.puntos - a.puntos);
  else if (orden === 'dinero') lista.sort((a, b) => b.dinero - a.dinero || b.puntos - a.puntos);
  else lista.sort((a, b) => b.puntos - a.puntos || b.partidos - a.partidos);
  return lista.slice(0, 100);
}

function guardarRanking() {
  try {
    const temporal = ARCHIVO_RANKING + '.tmp';
    fs.writeFileSync(temporal, JSON.stringify(rankingComunidad, null, 2));
    fs.renameSync(temporal, ARCHIVO_RANKING);
  } catch (e) { console.error('No se pudo guardar el ranking:', e.message); }
}

function responderJSON(res, estado, datos) {
  const cuerpo = JSON.stringify(datos);
  res.writeHead(estado, {
    'Content-Type': 'application/json; charset=utf-8',
    'Content-Length': Buffer.byteLength(cuerpo),
    'Cache-Control': 'no-store',
    'X-Content-Type-Options': 'nosniff'
  });
  res.end(cuerpo);
}

function actualizarRanking(req, res) {
  let cuerpo = '', terminado = false;
  req.on('data', trozo => {
    if (terminado) return;
    cuerpo += trozo;
    if (cuerpo.length > 8192) {
      terminado = true;
      responderJSON(res, 413, { ok: false, error: 'demasiado_grande' });
      req.destroy();
    }
  });
  req.on('end', () => {
    if (terminado) return;
    let d;
    try { d = JSON.parse(cuerpo || '{}'); } catch (_) { return responderJSON(res, 400, { ok: false, error: 'json_invalido' }); }
    const id = textoSeguro(d.id, 64).replace(/[^a-zA-Z0-9_-]/g, '');
    if (id.length < 8) return responderJSON(res, 400, { ok: false, error: 'id_invalido' });
    const ahora = Date.now(), anterior = ultimaActualizacion.get(id) || 0;
    if (ahora - anterior < 1500) return responderJSON(res, 429, { ok: false, error: 'muy_rapido' });
    ultimaActualizacion.set(id, ahora);
    const nuevo = {
      id,
      nombre: textoSeguro(d.nombre, 26) || 'Jugador de LA DIEZ',
      club: textoSeguro(d.club, 36) || 'Sin club',
      partidos: numeroSeguro(d.partidos, 0, 1000000),
      dinero: numeroSeguro(d.dinero, 0, 999999999999),
      nivel: numeroSeguro(d.nivel, 1, 999),
      media: numeroSeguro(d.media, 1, 99),
      actualizado: ahora
    };
    const i = rankingComunidad.findIndex(x => x.id === id);
    if (i >= 0) rankingComunidad[i] = nuevo;
    else rankingComunidad.push(nuevo);
    if (rankingComunidad.length > 5000) rankingComunidad.sort((a, b) => b.actualizado - a.actualizado).length = 5000;
    guardarRanking();
    responderJSON(res, 200, { ok: true, puntos: puntosComunidad(nuevo) });
  });
}

/** salas: code -> { code, host, invitados:Set, creada, modo, datos } */
const salas = new Map();

function codigoNuevo() {
  let c;
  do {
    c = Array.from({ length: 4 }, () => LETRAS[Math.floor(Math.random() * LETRAS.length)]).join('');
  } while (salas.has(c));
  return c;
}

function enviar(ws, obj) {
  if (ws && ws.readyState === 1) {
    try { ws.send(JSON.stringify(obj)); } catch (_) {}
  }
}

function difundir(sala, obj, excepto) {
  if (sala.host && sala.host !== excepto) enviar(sala.host, obj);
  for (const c of sala.invitados) if (c !== excepto) enviar(c, obj);
}

function gente(sala) {
  return (sala.host ? 1 : 0) + sala.invitados.size;
}

function cerrarSala(sala, motivo) {
  difundir(sala, { t: 'sala_cerrada', motivo });
  salas.delete(sala.code);
}

// ── servidor HTTP (salud + página simple) ──
const servidor = http.createServer((req, res) => {
  let url;
  try { url = new URL(req.url, 'http://localhost'); }
  catch (_) { res.writeHead(400); return res.end('Pedido inválido'); }
  const ruta = url.pathname;
  // cobros (solo responde si configuraste MP_TOKEN)
  if (ruta.startsWith('/pagos') || req.method === 'OPTIONS') {
    if (pagos.manejar(req, res)) return;
  }
  if (ruta === '/api/ranking' && req.method === 'GET') {
    const orden = ['general', 'partidos', 'dinero'].includes(url.searchParams.get('orden')) ? url.searchParams.get('orden') : 'general';
    return responderJSON(res, 200, { ok: true, orden, jugadores: rankingOrdenado(orden), actualizado: Date.now() });
  }
  if (ruta === '/api/ranking' && req.method === 'POST') return actualizarRanking(req, res);
  if (ruta === '/salud' || ruta === '/health') {
    res.writeHead(200, { 'Content-Type': 'application/json' });
    return res.end(JSON.stringify({
      ok: true,
      salas: salas.size,
      jugadores: [...salas.values()].reduce((a, s) => a + gente(s), 0),
      ranking: rankingComunidad.length,
      arriba: Math.round(process.uptime()),
      pagos: pagos.activo
    }));
  }
  if ((req.method === 'GET' || req.method === 'HEAD') && ruta.startsWith('/assets/')) {
    let relativo;
    try { relativo = decodeURIComponent(ruta.slice('/assets/'.length)); }
    catch (_) { res.writeHead(400); return res.end('Ruta inválida'); }
    const archivo = path.resolve(DIRECTORIO_ASSETS, relativo);
    if (!relativo || (archivo !== DIRECTORIO_ASSETS && !archivo.startsWith(DIRECTORIO_ASSETS + path.sep))) {
      res.writeHead(403); return res.end('Acceso denegado');
    }
    let stat;
    try { stat = fs.statSync(archivo); } catch (_) { res.writeHead(404); return res.end('No encontrado'); }
    if (!stat.isFile()) { res.writeHead(404); return res.end('No encontrado'); }
    const tipo = { '.webp': 'image/webp', '.png': 'image/png', '.jpg': 'image/jpeg', '.jpeg': 'image/jpeg', '.svg': 'image/svg+xml' }[path.extname(archivo).toLowerCase()] || 'application/octet-stream';
    res.writeHead(200, { 'Content-Type': tipo, 'Content-Length': stat.size, 'Cache-Control': 'public, max-age=604800, immutable', 'X-Content-Type-Options': 'nosniff' });
    if (req.method === 'HEAD') return res.end();
    return fs.createReadStream(archivo).pipe(res);
  }
  // El mismo servidor entrega el juego. Abrirlo por HTTP evita las limitaciones de file://
  // y permite que el WebSocket use automáticamente el mismo host.
  if ((req.method === 'GET' || req.method === 'HEAD') && (ruta === '/' || ruta.startsWith('/juego'))) {
    if (!fs.existsSync(ARCHIVO_JUEGO)) {
      res.writeHead(500, { 'Content-Type': 'text/plain; charset=utf-8' });
      return res.end('No se encontró ladiez.html junto a la carpeta ladiez-servidor.');
    }
    const stat = fs.statSync(ARCHIVO_JUEGO);
    res.writeHead(200, {
      'Content-Type': 'text/html; charset=utf-8',
      'Content-Length': stat.size,
      'Cache-Control': 'no-store',
      'X-Content-Type-Options': 'nosniff'
    });
    if (req.method === 'HEAD') return res.end();
    return fs.createReadStream(ARCHIVO_JUEGO).pipe(res);
  }
  if (ruta !== '/servidor') {
    res.writeHead(404, { 'Content-Type': 'text/plain; charset=utf-8' });
    return res.end('Ruta no encontrada');
  }
  res.writeHead(200, { 'Content-Type': 'text/html; charset=utf-8' });
  res.end(`<!doctype html><html lang="es"><meta charset="utf-8">
  <title>LA DIEZ · servidor</title>
  <body style="background:#070b0f;color:#eef4f8;font-family:system-ui;padding:40px;text-align:center">
  <h1 style="color:#12e07f">LA DIEZ · servidor de salas</h1>
  <p>Está funcionando. Salas activas: <b>${salas.size}</b></p>
  <p><a style="color:#31b9e9" href="/">Abrir LA DIEZ</a></p>
  <p style="color:#8298a4;font-size:14px">Juego y salas están funcionando en el mismo servidor.</p>
  </body></html>`);
});

const wss = new WebSocketServer({ server: servidor });

wss.on('connection', (ws, req) => {
  ws.vivo = true;
  ws.sala = null;
  ws.rol = null;

  ws.on('pong', () => { ws.vivo = true; });

  ws.on('message', (raw) => {
    let m;
    try { m = JSON.parse(raw); } catch (_) { return; }

    switch (m.t) {

      // ── crear una sala ──
      case 'crear': {
        if (ws.sala) return;
        const code = codigoNuevo();
        const sala = {
          code, host: ws, invitados: new Set(),
          creada: Date.now(), modo: m.modo || 'partido', datos: m.datos || null
        };
        salas.set(code, sala);
        ws.sala = code; ws.rol = 'host';
        enviar(ws, { t: 'sala_creada', code, modo: sala.modo });
        break;
      }

      // ── entrar a una sala ──
      case 'unir': {
        const code = String(m.code || '').toUpperCase().trim();
        const sala = salas.get(code);
        if (!sala) return enviar(ws, { t: 'error', causa: 'no_existe' });
        if (sala.invitados.size >= 3) return enviar(ws, { t: 'error', causa: 'llena' });
        sala.invitados.add(ws);
        ws.sala = code; ws.rol = 'invitado';
        enviar(ws, { t: 'unido', code, modo: sala.modo, datos: sala.datos });
        enviar(sala.host, { t: 'rival_entro', jugadores: gente(sala) });
        break;
      }

      // ── el host arranca el partido y manda la configuración ──
      case 'config': {
        const sala = salas.get(ws.sala);
        if (!sala || sala.host !== ws) return;
        sala.datos = m.datos || null;
        difundir(sala, { t: 'config', datos: sala.datos }, ws);
        break;
      }

      // ── estado del partido: host → invitados (30 veces por segundo) ──
      case 'estado': {
        const sala = salas.get(ws.sala);
        if (!sala || sala.host !== ws) return;
        difundir(sala, { t: 'estado', d: m.d }, ws);
        break;
      }

      // ── input del invitado → host ──
      case 'input': {
        const sala = salas.get(ws.sala);
        if (!sala) return;
        enviar(sala.host, { t: 'input', d: m.d, de: m.de || 1 });
        break;
      }

      // ── mensajes libres del modo DT compartido (fichajes, decisiones) ──
      case 'dt': {
        const sala = salas.get(ws.sala);
        if (!sala) return;
        difundir(sala, { t: 'dt', d: m.d }, ws);
        break;
      }

      // ── chat ──
      case 'chat': {
        const sala = salas.get(ws.sala);
        if (!sala) return;
        difundir(sala, { t: 'chat', txt: String(m.txt || '').slice(0, 200), de: ws.rol });
        break;
      }

      case 'ping': enviar(ws, { t: 'pong' }); break;

      case 'salir': {
        const sala = salas.get(ws.sala);
        if (!sala) return;
        if (sala.host === ws) cerrarSala(sala, 'el anfitrión se fue');
        else { sala.invitados.delete(ws); enviar(sala.host, { t: 'rival_salio' }); }
        ws.sala = null;
        break;
      }
    }
  });

  ws.on('close', () => {
    const sala = salas.get(ws.sala);
    if (!sala) return;
    if (sala.host === ws) cerrarSala(sala, 'se cayó la conexión del anfitrión');
    else { sala.invitados.delete(ws); enviar(sala.host, { t: 'rival_salio' }); }
  });
});

// ── mantenimiento: latidos y limpieza de salas viejas ──
setInterval(() => {
  wss.clients.forEach((ws) => {
    if (!ws.vivo) return ws.terminate();
    ws.vivo = false;
    try { ws.ping(); } catch (_) {}
  });
  const ahora = Date.now();
  for (const sala of [...salas.values()]) {
    if (gente(sala) === 0 || ahora - sala.creada > VIDA_SALA_MS) {
      salas.delete(sala.code);
    }
  }
}, LATIDO_MS);

servidor.listen(PUERTO, () => {
  console.log('LA DIEZ · servidor de salas escuchando en el puerto ' + PUERTO);
});
