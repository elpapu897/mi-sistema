#!/usr/bin/env python3
"""
GONVRA — Portero de los webhooks.

Se para delante de n8n y SOLO deja pasar las rutas de webhook.
Todo lo demas (el panel, la API, los ajustes) devuelve 404 como si no existiera.

Asi n8n puede recibir avisos de Instagram/Shopify/WhatsApp desde internet
sin que nadie pueda entrar al panel ni ver los tokens guardados.

Escucha en 127.0.0.1:8099 y reenvia a n8n en 127.0.0.1:5678.
"""
import http.server
import socketserver
import urllib.error
import urllib.request

PUERTO_PROPIO = 8099
N8N = "http://127.0.0.1:5678"

# Unicas rutas que pasan. Todo lo demas no existe para afuera.
PERMITIDAS = ("/webhook/", "/webhook-test/", "/webhook-waiting/")

MAX_CUERPO = 8 * 1024 * 1024  # 8 MB, de sobra para un webhook


class Portero(http.server.BaseHTTPRequestHandler):
    protocol_version = "HTTP/1.1"
    server_version = "gonvra"
    sys_version = ""

    def _permitido(self):
        return any(self.path.startswith(p) for p in PERMITIDAS)

    def _rechazar(self):
        cuerpo = b"Not Found"
        self.send_response(404)
        self.send_header("Content-Type", "text/plain")
        self.send_header("Content-Length", str(len(cuerpo)))
        self.end_headers()
        self.wfile.write(cuerpo)

    def _reenviar(self, metodo):
        if not self._permitido():
            self._rechazar()
            return

        largo = int(self.headers.get("Content-Length") or 0)
        if largo > MAX_CUERPO:
            self._rechazar()
            return
        cuerpo = self.rfile.read(largo) if largo else None

        cabeceras = {}
        for k, v in self.headers.items():
            if k.lower() in ("host", "content-length", "connection",
                             "accept-encoding"):
                continue
            cabeceras[k] = v

        req = urllib.request.Request(N8N + self.path, data=cuerpo,
                                     headers=cabeceras, method=metodo)
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                datos = r.read()
                self.send_response(r.status)
                ct = r.headers.get("Content-Type", "application/json")
                self.send_header("Content-Type", ct)
                self.send_header("Content-Length", str(len(datos)))
                self.end_headers()
                self.wfile.write(datos)
        except urllib.error.HTTPError as e:
            datos = e.read()
            self.send_response(e.code)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(datos)))
            self.end_headers()
            self.wfile.write(datos)
        except Exception:
            cuerpo = b'{"error":"upstream"}'
            self.send_response(502)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(cuerpo)))
            self.end_headers()
            self.wfile.write(cuerpo)

    def do_GET(self):
        self._reenviar("GET")

    def do_POST(self):
        self._reenviar("POST")

    def do_PUT(self):
        self._reenviar("PUT")

    def do_HEAD(self):
        self._reenviar("HEAD")

    def do_DELETE(self):
        self._rechazar()

    def log_message(self, *a):
        pass


class Servidor(socketserver.ThreadingTCPServer):
    allow_reuse_address = True
    daemon_threads = True


if __name__ == "__main__":
    with Servidor(("127.0.0.1", PUERTO_PROPIO), Portero) as s:
        s.serve_forever()
