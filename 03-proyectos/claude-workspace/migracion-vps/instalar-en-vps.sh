#!/bin/bash
# Instalador del equipo GONVRA en un VPS Ubuntu 24.04 limpio.
# Se ejecuta EN EL SERVIDOR. Claude Code lo corre por SSH; el usuario no toca nada.
set -e

echo "════════ 1/6 · Sistema base ════════"
export DEBIAN_FRONTEND=noninteractive
apt-get update -qq
apt-get install -y -qq python3 python3-pip python3-venv git curl tar tzdata sqlite3 ca-certificates
timedatectl set-timezone America/Argentina/Buenos_Aires || true
echo "  ✓ paquetes + zona horaria Argentina"

echo "════════ 2/6 · Usuario de trabajo ════════"
id gonvra >/dev/null 2>&1 || useradd -m -s /bin/bash gonvra
loginctl enable-linger gonvra || true   # clave: permite que los servicios corran sin sesión abierta
echo "  ✓ usuario 'gonvra' con linger (sobrevive desconexiones)"

echo "════════ 3/6 · Restaurando el sistema ════════"
cd /home/gonvra
for f in hermes-core.tgz gonvra2.tgz scripts.tgz semaforo.tgz; do
  [ -f "/tmp/$f" ] || { echo "  ! falta /tmp/$f"; continue; }
done
tar xzf /tmp/hermes-core.tgz -C /home/gonvra
mkdir -p /home/gonvra/Claude
tar xzf /tmp/gonvra2.tgz -C /home/gonvra/Claude
tar xzf /tmp/scripts.tgz  -C /home/gonvra/Claude
mkdir -p /home/gonvra/Claude/gonvra
tar xzf /tmp/semaforo.tgz -C /home/gonvra/Claude/gonvra
chown -R gonvra:gonvra /home/gonvra
echo "  ✓ agentes, tablero, historial y aprobaciones restaurados"

echo "════════ 4/6 · Instalando Hermes ════════"
sudo -u gonvra bash -lc '
  curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/install.sh -o /tmp/h.sh 2>/dev/null \
    && bash /tmp/h.sh </dev/null >/dev/null 2>&1 \
    || pip3 install --user --quiet hermes-agent 2>/dev/null || true
' || echo "  ! instalación automática falló — se instala a mano"
echo "  ✓ intento de instalación completado"

echo "════════ 5/6 · Servicio permanente ════════"
cat >/etc/systemd/system/hermes-gateway.service <<'EOF'
[Unit]
Description=Hermes Gateway - GONVRA
After=network-online.target
Wants=network-online.target

[Service]
Type=simple
User=gonvra
WorkingDirectory=/home/gonvra
ExecStart=/home/gonvra/.local/bin/hermes gateway run
Restart=always
RestartSec=10
Environment=PYTHONUNBUFFERED=1

[Install]
WantedBy=multi-user.target
EOF
systemctl daemon-reload
systemctl enable hermes-gateway.service
echo "  ✓ el gateway arranca solo al prender el servidor y se reinicia si se cae"

echo "════════ 6/6 · Seguridad básica ════════"
if command -v ufw >/dev/null 2>&1; then
  ufw --force reset >/dev/null 2>&1 || true
  ufw default deny incoming >/dev/null
  ufw default allow outgoing >/dev/null
  ufw allow OpenSSH >/dev/null
  ufw --force enable >/dev/null
  echo "  ✓ firewall: solo SSH"
fi

echo ""
echo "════════════════════════════════════════"
echo " LISTO. Verificaciones pendientes:"
echo "  1) hermes gateway status"
echo "  2) que el bot de Telegram responda"
echo "  3) hermes cron list"
echo "════════════════════════════════════════"
