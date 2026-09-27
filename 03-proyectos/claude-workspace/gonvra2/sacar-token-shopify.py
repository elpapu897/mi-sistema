#!/usr/bin/env python3
"""
GONVRA — Saca el token de Shopify (shpat_) por OAuth, sin vueltas.

Como usarlo:
    python3 sacar-token-shopify.py CLIENT_ID CLIENT_SECRET

Hace todo solo:
 1. Levanta un servidor local que espera la respuesta de Shopify
 2. Te imprime el link para autorizar
 3. Cuando autorizas, agarra el codigo y lo cambia por el token
 4. Prueba el token de verdad contra la API (pedidos, clientes, carritos)
 5. Lo guarda en ~/.hermes/.gonvra-secrets.env con permisos cerrados

No imprime el token entero en pantalla.
"""
import http.server, json, os, secrets, socketserver, sys, threading
import urllib.parse, urllib.request, webbrowser

TIENDA = "jm60sa-cp.myshopify.com"
PUERTO = 3456
REDIRECT = f"http://localhost:{PUERTO}/callback"
SCOPES = "read_orders,read_customers,read_checkouts,read_products,read_inventory"
SECRETS = os.path.expanduser("~/.hermes/.gonvra-secrets.env")

estado = secrets.token_hex(16)
resultado = {}
listo = threading.Event()


class Callback(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        q = urllib.parse.parse_qs(urllib.parse.urlparse(self.path).query)
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()
        if q.get("state", [""])[0] != estado:
            self.wfile.write("<h2>Error: el estado no coincide.</h2>".encode())
            return
        if "code" not in q:
            self.wfile.write(f"<h2>Shopify devolvio un error</h2><pre>{q}</pre>".encode())
            return
        resultado["code"] = q["code"][0]
        self.wfile.write(
            "<body style='font-family:sans-serif;background:#0d1720;color:#c8e54a;"
            "text-align:center;padding-top:80px'><h1>Listo</h1>"
            "<p style='color:#ddd'>Ya podes cerrar esta pestana y volver al chat.</p>"
            "</body>".encode())
        listo.set()

    def log_message(self, *a):
        pass


def main():
    print("\n" + "=" * 72)
    print("  SACAR EL TOKEN DE SHOPIFY — GONVRA")
    print("=" * 72)
    print("""
Necesito 2 datos de la app GONVRA Agentes.
Estan en:  https://dev.shopify.com/dashboard
           -> app GONVRA Agentes -> Client credentials / Credenciales

ANTES de seguir, en esa misma pagina agrega esta URL de redireccion
y guarda (si no, Shopify no te deja volver):

    http://localhost:3456/callback
""")
    cid = (sys.argv[1] if len(sys.argv) > 1 else
           input("Pega el CLIENT ID y apreta Enter:\n> ")).strip()
    csecret = (sys.argv[2] if len(sys.argv) > 2 else
               input("\nPega el CLIENT SECRET y apreta Enter:\n> ")).strip()

    # Red de seguridad: detectar que no pegaron el texto de ejemplo
    malos = ("TU_CLIENT_ID", "TU_CLIENT_SECRET", "CLIENT_ID", "CLIENT_SECRET",
             "PEGA", "TEST_ID", "TEST_SECRET", "")
    for valor, nombre in ((cid, "CLIENT ID"), (csecret, "CLIENT SECRET")):
        if valor.upper() in malos or len(valor) < 8:
            print(f"""
  ALTO. El {nombre} que pusiste es '{valor}'.
  Eso es el texto de ejemplo, no tu dato real.

  Tenes que ir a https://dev.shopify.com/dashboard , entrar a la app
  GONVRA Agentes, y copiar el valor de verdad (una tira larga de
  letras y numeros). Despues volve a correr este comando.
""")
            sys.exit(1)

    socketserver.TCPServer.allow_reuse_address = True
    srv = socketserver.TCPServer(("127.0.0.1", PUERTO), Callback)
    threading.Thread(target=srv.serve_forever, daemon=True).start()

    url = (f"https://{TIENDA}/admin/oauth/authorize?"
           + urllib.parse.urlencode({
               "client_id": cid, "scope": SCOPES,
               "redirect_uri": REDIRECT, "state": estado}))

    print("\n" + "=" * 72)
    print("ABRI ESTE LINK Y APRETA 'Instalar app':\n")
    print(url)
    print("=" * 72 + "\n")
    try:
        webbrowser.open(url)
        print("(intente abrirlo solo en tu navegador)\n")
    except Exception:
        pass

    print("Esperando que autorices... (5 minutos de limite)")
    if not listo.wait(timeout=300):
        print("\nSe acabo el tiempo. Volve a correrlo.")
        sys.exit(1)
    srv.shutdown()

    datos = urllib.parse.urlencode({
        "client_id": cid, "client_secret": csecret,
        "code": resultado["code"]}).encode()
    req = urllib.request.Request(
        f"https://{TIENDA}/admin/oauth/access_token", data=datos)
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            tok = json.loads(r.read().decode())
    except urllib.error.HTTPError as e:
        print("\nShopify rechazo el intercambio:", e.read().decode()[:400])
        sys.exit(1)

    access = tok.get("access_token", "")
    if not access:
        print("\nNo vino ningun token:", json.dumps(tok)[:300])
        sys.exit(1)

    print(f"\nTOKEN OBTENIDO: empieza con '{access[:6]}...' ({len(access)} caracteres)")
    print(f"permisos otorgados: {tok.get('scope','?')}\n")

    # --- probarlo de verdad, no confiar ---
    print("PROBANDOLO CONTRA LA API:")
    base = f"https://{TIENDA}/admin/api/2026-01"
    sirve = True
    for ep in ("shop", "orders", "customers", "products"):
        r = urllib.request.Request(f"{base}/{ep}.json?limit=1",
                                   headers={"X-Shopify-Access-Token": access})
        try:
            with urllib.request.urlopen(r, timeout=25) as resp:
                print(f"   {ep:<12} HTTP {resp.status} OK")
        except urllib.error.HTTPError as e:
            print(f"   {ep:<12} HTTP {e.code} <-- FALLA")
            sirve = False

    if not sirve:
        print("\nAlgo quedo sin permiso. Revisa los scopes de la app.")

    # --- guardar ---
    lineas = []
    if os.path.exists(SECRETS):
        lineas = [l for l in open(SECRETS, encoding="utf-8")
                  if not l.startswith("SHOPIFY_ACCESS_TOKEN=")]
    lineas.append(f"SHOPIFY_ACCESS_TOKEN={access}\n")
    os.umask(0o077)
    with open(SECRETS, "w", encoding="utf-8") as f:
        f.writelines(lineas)
    os.chmod(SECRETS, 0o600)
    print(f"\nGuardado en {SECRETS} (solo lo podes leer vos)")
    print("Avisale a Claude que ya esta, y el conecta el MCP.")


if __name__ == "__main__":
    main()
