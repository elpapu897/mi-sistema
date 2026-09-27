#!/usr/bin/env python3
"""
GONVRA — Saca el token de Facebook/Meta (para Ads y Ad Library).

El token de Instagram NO sirve para esto: son sistemas distintos.
  Instagram Login -> graph.instagram.com
  Facebook Login  -> graph.facebook.com   <- este

Uso:
    python3 sacar-token-meta.py

Te pregunta los datos, abre el navegador, y hace todo solo:
consigue el token, lo prueba, lo convierte en uno de larga duración (60 días)
y lo guarda cerrado.
"""
import http.server
import json
import os
import secrets
import socketserver
import sys
import threading
import urllib.error
import urllib.parse
import urllib.request
import webbrowser

PUERTO = 3457
REDIRECT = f"http://localhost:{PUERTO}/callback"
SECRETS = os.path.expanduser("~/.hermes/.gonvra-secrets.env")
API = "https://graph.facebook.com/v23.0"

# Lo que pedimos. ads_read para leer campañas; el resto para la página e insights.
SCOPES = ",".join([
    "ads_read",
    "business_management",
    "pages_show_list",
    "pages_read_engagement",
    "read_insights",
])

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
            self.wfile.write(b"<h2>Error: el estado no coincide.</h2>")
            return
        if "code" not in q:
            err = q.get("error_description", ["sin detalle"])[0]
            self.wfile.write(f"<h2>Meta rechazo el permiso</h2><pre>{err}</pre>".encode())
            listo.set()
            return
        resultado["code"] = q["code"][0]
        self.wfile.write(
            "<body style='font-family:sans-serif;background:#0d1720;color:#c8e54a;"
            "text-align:center;padding-top:80px'><h1>Listo</h1>"
            "<p style='color:#ddd'>Ya podes cerrar esta pestana.</p></body>".encode())
        listo.set()

    def log_message(self, *a):
        pass


def leer_secreto(nombre):
    try:
        for l in open(SECRETS, encoding="utf-8"):
            if l.startswith(nombre + "="):
                return l.split("=", 1)[1].strip()
    except Exception:
        pass
    return ""


def pedir(url):
    try:
        with urllib.request.urlopen(url, timeout=30) as r:
            return json.loads(r.read().decode())
    except urllib.error.HTTPError as e:
        return {"error": json.loads(e.read().decode() or "{}").get("error", {})}


def main():
    print("\n" + "=" * 70)
    print("  TOKEN DE META (Ads y Ad Library) — GONVRA")
    print("=" * 70)

    cid = leer_secreto("INSTAGRAM_APP_ID")
    csec = leer_secreto("INSTAGRAM_APP_SECRET")

    if cid and csec:
        print(f"\nUso la app que ya tenemos guardada (ID {cid[:6]}...).")
        print("Si querés usar otra, escribí el ID nuevo. Si no, apretá Enter.")
        otro = input("> ").strip()
        if otro:
            cid = otro
            csec = input("Pegá el App Secret de esa app:\n> ").strip()
    else:
        print("\nEstán en developers.facebook.com/apps -> tu app -> Configuración básica")
        cid = input("\nPegá el ID de la app:\n> ").strip()
        csec = input("\nPegá el Secreto de la app:\n> ").strip()

    if len(cid) < 8 or len(csec) < 8:
        print("\n  Esos datos no parecen válidos. Volvé a intentar.")
        return 1

    print(f"""
ANTES DE SEGUIR, en developers.facebook.com -> tu app -> Facebook Login ->
Configuración, agregá esta URL en "URI de redireccionamiento de OAuth válidos"
y guardá:

    {REDIRECT}

Sin eso, Meta no te deja volver.""")
    input("\nCuando lo hayas guardado, apretá Enter...")

    socketserver.TCPServer.allow_reuse_address = True
    srv = socketserver.TCPServer(("127.0.0.1", PUERTO), Callback)
    threading.Thread(target=srv.serve_forever, daemon=True).start()

    url = ("https://www.facebook.com/v23.0/dialog/oauth?" + urllib.parse.urlencode({
        "client_id": cid, "redirect_uri": REDIRECT,
        "state": estado, "scope": SCOPES, "response_type": "code"}))

    print("\n" + "=" * 70)
    print("ABRI ESTE LINK Y DALE PERMISO:\n")
    print(url)
    print("=" * 70 + "\n")
    try:
        webbrowser.open(url)
    except Exception:
        pass

    print("Esperando que aceptes... (5 minutos de límite)")
    if not listo.wait(timeout=300):
        print("\nSe acabó el tiempo. Volvé a correrlo.")
        return 1
    srv.shutdown()

    if "code" not in resultado:
        print("\nNo llegó el código. Fijate qué dijo el navegador.")
        return 1

    # code -> token corto
    d = pedir(f"{API}/oauth/access_token?" + urllib.parse.urlencode({
        "client_id": cid, "client_secret": csec,
        "redirect_uri": REDIRECT, "code": resultado["code"]}))
    if d.get("error"):
        print("\nMeta rechazó el intercambio:", str(d["error"])[:250])
        return 1
    corto = d.get("access_token", "")
    if not corto:
        print("\nNo vino token:", json.dumps(d)[:200])
        return 1

    # corto -> largo (60 días)
    d2 = pedir(f"{API}/oauth/access_token?" + urllib.parse.urlencode({
        "grant_type": "fb_exchange_token", "client_id": cid,
        "client_secret": csec, "fb_exchange_token": corto}))
    largo = d2.get("access_token") or corto
    dias = int(d2.get("expires_in", 0)) // 86400 if d2.get("expires_in") else None

    print(f"\nTOKEN OBTENIDO ({len(largo)} caracteres"
          + (f", dura ~{dias} días" if dias else "") + ")\n")

    print("PROBANDOLO:")
    yo = pedir(f"{API}/me?fields=id,name&access_token={largo}")
    if yo.get("error"):
        print("   perfil        FALLA:", str(yo["error"])[:90])
    else:
        print(f"   perfil        OK · {yo.get('name')}")

    ads = pedir(f"{API}/me/adaccounts?fields=name,account_status,currency"
                f"&access_token={largo}")
    if ads.get("error"):
        print("   cuentas ads   FALLA:", str(ads["error"].get('message',''))[:80])
    else:
        cuentas = ads.get("data", [])
        print(f"   cuentas ads   OK · {len(cuentas)} encontrada(s)")
        for c in cuentas[:5]:
            print(f"      {c.get('id')} · {c.get('name')} · {c.get('currency')}")

    # guardar
    lineas = []
    if os.path.exists(SECRETS):
        lineas = [l for l in open(SECRETS, encoding="utf-8")
                  if not l.startswith(("META_ACCESS_TOKEN=", "META_APP_ID=",
                                       "META_APP_SECRET="))]
    lineas += [f"META_ACCESS_TOKEN={largo}\n",
               f"META_APP_ID={cid}\n",
               f"META_APP_SECRET={csec}\n"]
    os.umask(0o077)
    with open(SECRETS, "w", encoding="utf-8") as f:
        f.writelines(lineas)
    os.chmod(SECRETS, 0o600)

    print(f"\nGuardado en {SECRETS}")
    print("Avisale a Claude que ya está.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
