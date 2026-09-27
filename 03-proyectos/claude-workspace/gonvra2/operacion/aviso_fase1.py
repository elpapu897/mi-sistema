#!/usr/bin/env python3
"""Aviso interno autorizado: solo 4 archivos reales y tarjetas finalizadas."""
import argparse
import json
import sqlite3
from pathlib import Path

ROOT = Path('/home/matiigonzz/Claude/gonvra2')
MANIFEST = ROOT / 'operacion/fase1.json'
EMITTED = ROOT / 'operacion/aviso-fase1-emitido.json'
DB = Path('/home/matiigonzz/.hermes/kanban/boards/gonvra/kanban.db')


def inspect():
    manifest = json.loads(MANIFEST.read_text())
    results = []
    with sqlite3.connect(f'file:{DB}?mode=ro', uri=True) as conn:
        for role, item in manifest.items():
            row = conn.execute('SELECT status FROM tasks WHERE id=?', (item['task'],)).fetchone()
            path = Path(item['path'])
            text = path.read_text() if path.exists() else ''
            results.append({'role': role, 'task': item['task'], 'status': row[0] if row else 'missing',
                            'path': str(path), 'bytes': len(text.encode()),
                            'partial': any(word in text.upper() for word in ('PARCIAL', 'NO VERIFICADO', 'SIN VERIFICAR', 'NO PUDE', 'BLOQUEO DE ACCESO'))})
    return results


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    rows = inspect()
    ready = len(rows) == 4 and all(r['status'] == 'done' and r['bytes'] > 500 for r in rows)
    if args.check:
        print(json.dumps({'ready': ready, 'already_emitted': EMITTED.exists(), 'artifacts': rows}, ensure_ascii=False))
        return
    if not ready or EMITTED.exists():
        return
    # Solo se reconoce finalización, nunca publicación ni éxito de investigación sin evidencia.
    lines = ['GONVRA · Primeros cuatro entregables terminados y guardados.',
             'COPY: textos de landing. TIKTOKER: guiones. INSTAGRAMER: posteos e historias. ESPIA: competencia y evidencia disponible.',
             'Listos para revisión; todavía no se publicó ni gastó dinero.']
    limited = [r['role'].upper() for r in rows if r['partial']]
    if limited:
        lines.append('Hay limitaciones o puntos sin verificar en: ' + ', '.join(limited) + '. No darlos por comprobados; leer el informe.')
    lines.append('Archivos: ~/Claude/gonvra2/<agente>/2026-09-14.md. JEFE consolida a las 21:00 Argentina.')
    EMITTED.write_text(json.dumps({'artifacts': rows, 'meaning': 'emitido al scheduler; verificar last_delivery_error antes de afirmar recepción'}, ensure_ascii=False, indent=2))
    print('\n'.join(lines))


if __name__ == '__main__':
    main()
