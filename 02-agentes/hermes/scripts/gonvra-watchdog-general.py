#!/usr/bin/env python3
"""
GONVRA — Watchdog de los watchdogs (idea I).

Vigila que el sistema esté realmente trabajando, no solo "encendido":
  · los 7 servicios activos
  · que cada job de Hermes haya corrido cuando le tocaba
  · ejecuciones falladas de n8n en las últimas horas
  · que los workflows sigan publicados y activos

Si un agente dejó de correr en silencio, te enterás. Hoy no te enterarías.
Silencio si está todo bien.
"""
import json
import os
import sqlite3
import subprocess
import sys
from datetime import datetime, timedelta

SERVICIOS = ["hermes-gateway", "gonvra-n8n", "gonvra-proxy", "gonvra-tunel",
             "gonvra-panel", "gonvra-gmail-auth"]
JOBS = os.path.expanduser("~/.hermes/cron/jobs.json")
N8NDB = os.path.expanduser("~/.n8n/database.sqlite")


def activo(servicio):
    r = subprocess.run(["systemctl", "--user", "is-active", f"{servicio}.service"],
                       capture_output=True, text=True)
    return r.stdout.strip() == "active"


def revisar_servicios():
    return [s for s in SERVICIOS if not activo(s)]


def revisar_jobs():
    """Un job que debió correr en las últimas 26 h y no corrió, es sospechoso."""
    problemas = []
    try:
        jobs = json.load(open(JOBS))["jobs"]
    except Exception:
        return ["no se pudo leer la grilla de agentes"]

    ahora = datetime.now().astimezone()
    for j in jobs:
        if not j.get("enabled"):
            continue
        nombre = j.get("name", "?")
        sched = (j.get("schedule") or {})
        # solo miramos los diarios o más frecuentes
        expr = sched.get("expr", "")
        minutos = sched.get("minutes")
        es_frecuente = bool(minutos) or (expr and not expr.endswith(("* * 1", "* * 3")))
        if not es_frecuente:
            continue

        ultimo = j.get("last_run_at")
        if not ultimo:
            continue  # recién creado
        try:
            f = datetime.fromisoformat(ultimo)
        except ValueError:
            continue
        horas = (ahora - f).total_seconds() / 3600
        limite = 2 if minutos else 26
        if horas > limite:
            problemas.append(f"{nombre[:46]} — última vez hace {int(horas)} h")
        elif j.get("last_status") == "error":
            err = (j.get("last_error") or "")[:70]
            problemas.append(f"{nombre[:46]} — último intento FALLÓ: {err}")
    return problemas


def revisar_n8n():
    problemas = []
    try:
        c = sqlite3.connect(f"file:{N8NDB}?mode=ro", uri=True)
    except Exception:
        return ["no se pudo leer la base de n8n"]

    try:
        inactivos = [r[0] for r in c.execute(
            "select name from workflow_entity where active=0 or activeVersionId is null")]
        for n in inactivos:
            problemas.append(f"workflow APAGADO: {n[:46]}")

        desde = (datetime.now() - timedelta(hours=6)).strftime("%Y-%m-%d %H:%M:%S")
        fallidas = list(c.execute(
            """select w.name, count(*) from execution_entity e
               join workflow_entity w on w.id = e.workflowId
               where e.status not in ('success','running','waiting','new')
                 and e.startedAt > ?
               group by w.name""", (desde,)))
        for nombre, n in fallidas:
            problemas.append(f"{nombre[:40]} — {n} ejecución(es) fallida(s) en 6 h")
    except Exception as e:
        problemas.append(f"error leyendo n8n: {str(e)[:60]}")
    finally:
        c.close()
    return problemas


def main():
    caidos = revisar_servicios()
    jobs = revisar_jobs()
    n8n = revisar_n8n()

    if not caidos and not jobs and not n8n:
        return 0

    print("EL SISTEMA GONVRA TIENE PROBLEMAS")
    print()

    if caidos:
        print("SERVICIOS CAIDOS:")
        for s in caidos:
            print(f"  · {s}")
        print()
        print("  Para levantarlos, en una terminal:")
        for s in caidos:
            print(f"    systemctl --user restart {s}.service")
        print()

    if jobs:
        print("AGENTES QUE DEJARON DE CORRER:")
        for p in jobs[:10]:
            print(f"  · {p}")
        print()

    if n8n:
        print("AUTOMATIZACIONES CON PROBLEMAS:")
        for p in n8n[:10]:
            print(f"  · {p}")
        print()

    print("Mirá el panel: http://localhost:8080/mission-control.html")
    return 0


if __name__ == "__main__":
    sys.exit(main())
