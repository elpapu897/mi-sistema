#!/usr/bin/env python3
"""Latido local sin IA ni mensajes, supervisado fuera del gateway."""
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo
now = datetime.now(ZoneInfo('America/Argentina/Buenos_Aires'))
p = Path('/home/matiigonzz/Claude/gonvra2/supervisor') / (now.date().isoformat() + '.md')
p.parent.mkdir(parents=True, exist_ok=True)
p.write_text(now.isoformat() + '\nsin novedades\n', encoding='utf-8')
