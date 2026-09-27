#!/usr/bin/env bash
# GONVRA — Copia de seguridad diaria de todo lo que costó trabajo.
# Guarda los últimos 7 días y borra los viejos.
# Silencio si sale bien; solo habla si algo falla.

set -u
DESTINO="$HOME/GONVRA-BACKUPS"
HOY=$(date +%Y-%m-%d)
CARPETA="$DESTINO/$HOY"
PROBLEMAS=""

mkdir -p "$CARPETA" || { echo "GONVRA BACKUP: no se pudo crear $CARPETA"; exit 0; }

# 1) Flujos de n8n (lo mas valioso: son horas de armado)
if [ -f "$HOME/.n8n/database.sqlite" ]; then
  python3 - "$CARPETA" <<'PY' 2>/dev/null || PROBLEMAS="${PROBLEMAS}- no se pudieron exportar los flujos de n8n\n"
import json, sqlite3, sys, os
destino = sys.argv[1]
c = sqlite3.connect("file:" + os.path.expanduser("~/.n8n/database.sqlite") + "?mode=ro", uri=True)
flujos = []
for wid, name, nodes, conns, settings in c.execute(
        "select id,name,nodes,connections,settings from workflow_entity"):
    flujos.append({"id": wid, "name": name,
                   "nodes": json.loads(nodes) if nodes else [],
                   "connections": json.loads(conns) if conns else {},
                   "settings": json.loads(settings) if settings else {}})
json.dump(flujos, open(os.path.join(destino, "n8n-flujos.json"), "w"),
          ensure_ascii=False, indent=2)
print(len(flujos))
PY
fi

# 2) Agentes: la grilla de cron y los perfiles
cp "$HOME/.hermes/cron/jobs.json" "$CARPETA/agentes-grilla.json" 2>/dev/null \
  || PROBLEMAS="${PROBLEMAS}- no se pudo copiar la grilla de agentes\n"

# 3) Los SOUL.md (la personalidad de cada agente)
mkdir -p "$CARPETA/almas"
for f in "$HOME"/.hermes/profiles/gonvra-*/SOUL.md; do
  [ -f "$f" ] || continue
  agente=$(basename "$(dirname "$f")")
  cp "$f" "$CARPETA/almas/$agente.md" 2>/dev/null
done

# 4) Scripts propios
mkdir -p "$CARPETA/scripts"
cp "$HOME"/.hermes/scripts/gonvra-*.sh "$CARPETA/scripts/" 2>/dev/null

# 5) Documentos y entregables del proyecto (sin videos, pesan mucho)
tar czf "$CARPETA/gonvra2-documentos.tgz" \
    -C "$HOME/Claude" --exclude="videos" --exclude="*.mp4" --exclude="*.png" \
    --exclude="mission-control/agentes" gonvra2 2>/dev/null \
  || PROBLEMAS="${PROBLEMAS}- fallo el tar de documentos\n"

# 6) Tema de Shopify (la tienda entera)
if [ -d "$HOME/Documents/Codex/tiendas/jm60sa-cp/live-theme" ]; then
  tar czf "$CARPETA/tema-shopify.tgz" \
      -C "$HOME/Documents/Codex/tiendas/jm60sa-cp" live-theme 2>/dev/null \
    || PROBLEMAS="${PROBLEMAS}- fallo el tar del tema\n"
fi

# 7) Borrar los backups de mas de 7 dias
find "$DESTINO" -maxdepth 1 -type d -name "20*" -mtime +7 -exec rm -rf {} + 2>/dev/null

# Verificar que algo quedo de verdad
PESO=$(du -sm "$CARPETA" 2>/dev/null | cut -f1)
if [ -z "$PESO" ] || [ "$PESO" -lt 1 ]; then
  PROBLEMAS="${PROBLEMAS}- el backup de hoy quedo vacio o casi\n"
fi

if [ -n "$PROBLEMAS" ]; then
  echo "GONVRA BACKUP - hubo problemas ($HOY):"
  printf "%b" "$PROBLEMAS"
  echo "Carpeta: $CARPETA"
fi
exit 0
