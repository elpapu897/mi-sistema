#!/usr/bin/env bash
# GONVRA — Prueba un token de Instagram y, si anda, lo guarda solo.
# Uso:  bash ~/Claude/gonvra2/probar-instagram.sh
# Te pregunta el token. No hay nada que reemplazar.

SECRETS="$HOME/.hermes/.gonvra-secrets.env"

echo "════════════════════════════════════════════════"
echo "  PROBAR TOKEN DE INSTAGRAM — GONVRA"
echo "════════════════════════════════════════════════"
echo
echo "Sacalo de: https://developers.facebook.com/apps"
echo "  tu app -> Instagram -> Configuracion de la API con inicio de sesion de Instagram"
echo "  -> boton 'Generar token' en la cuenta @gonvra1"
echo

read -r -p "Pega el token y apreta Enter:
> " TOKEN
TOKEN=$(echo "$TOKEN" | tr -d '[:space:]')

# Red de seguridad: que no peguen el texto de ejemplo
case "$TOKEN" in
  ""|TU_TOKEN*|PEGA*|token*)
    echo
    echo "  ALTO: eso no es un token real, es el texto de ejemplo."
    echo "  Tiene que ser una tira larga que empieza con IGAA..."
    exit 1;;
esac
if [ ${#TOKEN} -lt 50 ]; then
  echo
  echo "  Ese token es muy corto (${#TOKEN} caracteres). Los de Instagram tienen 150+."
  exit 1
fi

echo
echo "→ Probando..."
RESP=$(curl -s --max-time 25 "https://graph.instagram.com/v23.0/me?fields=id,username,account_type,media_count&access_token=$TOKEN")

if echo "$RESP" | grep -q '"error"'; then
  echo
  echo "  ✗ EL TOKEN NO ANDA. Esto dijo Meta:"
  echo "$RESP" | python3 -c "
import sys,json
try:
    e=json.load(sys.stdin)['error']
    print('     mensaje:', e.get('message'))
    print('     codigo: ', e.get('code'), '/', e.get('error_subcode',''))
    print()
    c=e.get('code')
    msg=(e.get('message') or '').lower()
    if 'access blocked' in msg:
        print('     >> La app esta RESTRINGIDA por Meta, no es el token.')
        print('        Entra al dashboard y fijate si hay un cartel de advertencia arriba.')
    elif c==190:
        print('     >> El token vencio o fue revocado. Genera uno nuevo.')
    elif c==10 or c==200:
        print('     >> Falta un permiso. Revisa que la app tenga instagram_content_publish.')
except Exception:
    print('     (no se pudo leer la respuesta)')"
  exit 1
fi

echo "  ✓ EL TOKEN ANDA:"
echo "$RESP" | python3 -c "
import sys,json;d=json.load(sys.stdin)
print(f\"     cuenta: @{d.get('username')} ({d.get('account_type')})\")
print(f\"     publicaciones: {d.get('media_count')}\")"

IGID=$(echo "$RESP" | python3 -c "import sys,json;print(json.load(sys.stdin)['id'])")

echo
echo "→ Probando si PUEDE PUBLICAR (crea un borrador, no publica nada)..."
IMG="https://cdn.shopify.com/s/files/1/0722/4652/6067/files/rasuradora-integral-hero-v1.png"
PUB=$(curl -s -X POST --max-time 40 "https://graph.instagram.com/v23.0/$IGID/media" \
  -d "image_url=$IMG" -d "caption=prueba tecnica GONVRA" -d "access_token=$TOKEN")

if echo "$PUB" | grep -q '"id"'; then
  echo "  ✓ PUEDE PUBLICAR. Borrador creado (no se publico nada)."
  OK=1
else
  echo "  ✗ Lee la cuenta pero NO puede publicar:"
  echo "$PUB" | head -c 300; echo
  echo "     >> Falta el permiso instagram_content_publish en la app."
  OK=0
fi

echo
echo "→ Probando si puede LEER COMENTARIOS (hace falta para el aviso automatico)..."
MED=$(curl -s --max-time 25 "https://graph.instagram.com/v23.0/$IGID/media?fields=id&limit=1&access_token=$TOKEN" | python3 -c "
import sys,json
d=json.load(sys.stdin).get('data',[])
print(d[0]['id'] if d else '')" 2>/dev/null)
if [ -n "$MED" ]; then
  CT=$(curl -s --max-time 25 "https://graph.instagram.com/v23.0/$MED?fields=comments_count&access_token=$TOKEN" | python3 -c "
import sys,json;print(json.load(sys.stdin).get('comments_count',0))" 2>/dev/null)
  CL=$(curl -s --max-time 25 "https://graph.instagram.com/v23.0/$MED/comments?access_token=$TOKEN" | python3 -c "
import sys,json;print(len(json.load(sys.stdin).get('data',[])))" 2>/dev/null)
  if [ "${CT:-0}" -gt 0 ] 2>/dev/null && [ "${CL:-0}" -eq 0 ] 2>/dev/null; then
    echo "  ✗ NO puede leer comentarios (el post tiene $CT pero lista 0)."
    echo "    >> Falta el permiso instagram_business_manage_comments."
    echo "    >> Sin eso, los comentarios NO disparan el mensaje privado."
  else
    echo "  ✓ Puede leer comentarios."
  fi
else
  echo "  (sin publicaciones para probar)"
fi

echo
echo "→ Guardando el token..."
umask 077
grep -v "^INSTAGRAM_ACCESS_TOKEN=" "$SECRETS" > "$SECRETS.tmp" 2>/dev/null
echo "INSTAGRAM_ACCESS_TOKEN=$TOKEN" >> "$SECRETS.tmp"
mv "$SECRETS.tmp" "$SECRETS"
chmod 600 "$SECRETS"
echo "  ✓ Guardado en $SECRETS"

python3 /home/matiigonzz/Claude/gonvra2/mission-control/generar-datos.py >/dev/null 2>&1
echo "  ✓ Panel actualizado"
echo
[ "${OK:-0}" = "1" ] && echo "LISTO. Avisale a Claude que ya anda." \
                     || echo "El token sirve para leer, pero falta permiso para publicar."
