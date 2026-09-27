#!/usr/bin/env python3
"""Avisa una sola vez cuando PRECIOS y CREATIVO están realmente listos."""
from pathlib import Path
import json
import sqlite3

DB = Path('/home/matiigonzz/.hermes/kanban/boards/gonvra/kanban.db')
MARKER = Path('/home/matiigonzz/Claude/gonvra2/operacion/aviso-precios-creativo-emitido.json')
TASKS = {
    'PRECIOS': ('t_8ae087fc', Path('/home/matiigonzz/Claude/gonvra2/precios/2026-09-18.md')),
    'CREATIVO': ('t_899adaba', Path('/home/matiigonzz/Claude/gonvra2/creativo/2026-09-18.md')),
}

if MARKER.exists() or not DB.exists():
    raise SystemExit(0)

con = sqlite3.connect(DB)
con.row_factory = sqlite3.Row
ready = {}
for label, (task_id, artifact) in TASKS.items():
    row = con.execute('SELECT status FROM tasks WHERE id = ?', (task_id,)).fetchone()
    ready[label] = bool(row and row['status'] == 'done' and artifact.exists() and artifact.stat().st_size > 0)

if not all(ready.values()):
    raise SystemExit(0)

MARKER.parent.mkdir(parents=True, exist_ok=True)
MARKER.write_text(json.dumps({'tasks': {k: v[0] for k, v in TASKS.items()}, 'artifacts': {k: str(v[1]) for k, v in TASKS.items()}}, ensure_ascii=False, indent=2))
print('✅ GONVRA: PRECIOS y CREATIVO terminaron y sus entregables reales ya están listos.\n\n• PRECIOS: ~/Claude/gonvra2/precios/2026-09-18.md\n• CREATIVO: ~/Claude/gonvra2/creativo/2026-09-18.md\n\nNo se publicó, gastó ni activó ninguna campaña. MEDIABUYER sigue en pausa.')
