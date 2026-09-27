#!/usr/bin/env python3
"""GONVRA approval broker.

This is deliberately boring: it persists an approval request, freezes the
snapshot shown to Matías, and refuses to treat a click as executable unless
the caller later supplies the current snapshot and it matches exactly.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import sqlite3
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DB = ROOT / "approvals.sqlite3"
ENV = Path.home() / ".hermes" / ".env"
OWNER_ID = "7697535044"


def load_env() -> dict[str, str]:
    out: dict[str, str] = {}
    if ENV.exists():
        for line in ENV.read_text(encoding="utf-8").splitlines():
            if line.strip() and not line.lstrip().startswith("#") and "=" in line:
                k, v = line.split("=", 1)
                out[k.strip()] = v.strip().strip('"').strip("'")
    return out


def canonical(value: object) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def digest(snapshot: object) -> str:
    return hashlib.sha256(canonical(snapshot).encode("utf-8")).hexdigest()


def conn() -> sqlite3.Connection:
    ROOT.mkdir(parents=True, exist_ok=True)
    c = sqlite3.connect(DB)
    c.row_factory = sqlite3.Row
    c.execute("""CREATE TABLE IF NOT EXISTS approvals (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        kind TEXT NOT NULL,
        title TEXT NOT NULL,
        body TEXT NOT NULL,
        snapshot_json TEXT NOT NULL,
        snapshot_hash TEXT NOT NULL,
        status TEXT NOT NULL,
        choice TEXT,
        created_at REAL NOT NULL,
        expires_at REAL NOT NULL,
        resolved_at REAL,
        resolved_by TEXT,
        note TEXT
    )""")
    c.commit()
    return c


def telegram_send(text: str, markup: dict) -> dict:
    env = load_env()
    token = env.get("TELEGRAM_BOT_TOKEN")
    chat_id = env.get("TELEGRAM_HOME_CHANNEL")
    if not token or not chat_id:
        raise RuntimeError("Telegram no está configurado en Hermes")
    payload = urllib.parse.urlencode({
        "chat_id": chat_id,
        "text": text,
        "reply_markup": json.dumps(markup, ensure_ascii=False),
    }).encode()
    req = urllib.request.Request(
        f"https://api.telegram.org/bot{token}/sendMessage",
        data=payload,
        headers={"Content-Type": "application/x-www-form-urlencoded"},
    )
    with urllib.request.urlopen(req, timeout=20) as response:
        return json.loads(response.read().decode())


def create(args: argparse.Namespace) -> int:
    snapshot = json.loads(args.snapshot_json)
    now = time.time()
    expires = now + args.ttl
    c = conn()
    cur = c.execute(
        "INSERT INTO approvals(kind,title,body,snapshot_json,snapshot_hash,status,created_at,expires_at) VALUES(?,?,?,?,?,?,?,?)",
        (args.kind, args.title, args.body, canonical(snapshot), digest(snapshot), "pending", now, expires),
    )
    approval_id = cur.lastrowid
    c.commit()
    text = (
        f"🟡 APROBACIÓN — {args.kind.upper()}\n\n"
        f"{args.title}\n\n{args.body}\n\n"
        "La acción queda congelada al snapshot mostrado. Si cambia precio, stock, presupuesto o destino, "
        "el ✅ se bloquea y vuelve a pedir aprobación."
    )
    markup = {"inline_keyboard": [[
        {"text": "✅ APROBAR", "callback_data": f"gonvra_approval:{approval_id}:approve"},
        {"text": "⏸ DESPUÉS", "callback_data": f"gonvra_approval:{approval_id}:postpone"},
        {"text": "❌ RECHAZAR", "callback_data": f"gonvra_approval:{approval_id}:reject"},
    ]]}
    result = telegram_send(text, markup)
    print(json.dumps({"id": approval_id, "status": "pending", "telegram_ok": result.get("ok", False)}))
    return 0


def resolve(args: argparse.Namespace) -> int:
    c = conn()
    row = c.execute("SELECT * FROM approvals WHERE id=?", (args.id,)).fetchone()
    if not row:
        print(json.dumps({"ok": False, "status": "not_found"}))
        return 2
    if args.user_id != OWNER_ID:
        print(json.dumps({"ok": False, "status": "unauthorized"}))
        return 3
    now = time.time()
    if row["status"] != "pending":
        print(json.dumps({"ok": False, "status": row["status"], "message": "La aprobación ya fue resuelta."}))
        return 0
    if now > row["expires_at"]:
        c.execute("UPDATE approvals SET status='expired', resolved_at=? WHERE id=?", (now, args.id))
        c.commit()
        print(json.dumps({"ok": False, "status": "expired", "message": "La aprobación venció."}))
        return 0
    if args.choice == "postpone":
        c.execute("UPDATE approvals SET status='postponed', choice=?, resolved_at=?, resolved_by=? WHERE id=?", (args.choice, now, args.user_id, args.id))
        c.commit()
        print(json.dumps({"ok": True, "status": "postponed", "message": "Registré: DESPUÉS ⏸"}))
        return 0
    if args.choice == "reject":
        c.execute("UPDATE approvals SET status='rejected', choice=?, resolved_at=?, resolved_by=? WHERE id=?", (args.choice, now, args.user_id, args.id))
        c.commit()
        print(json.dumps({"ok": True, "status": "rejected", "message": "Registré: RECHAZAR ❌"}))
        return 0

    # Approve never executes here. It becomes approved_pending_revalidation.
    # An executor must later provide the current snapshot and pass this same check.
    c.execute("UPDATE approvals SET status='approved_pending_revalidation', choice=?, resolved_at=?, resolved_by=? WHERE id=?", (args.choice, now, args.user_id, args.id))
    c.commit()
    print(json.dumps({"ok": True, "status": "approved_pending_revalidation", "message": "Registré: APROBAR ✅; falta revalidar antes de ejecutar."}))
    return 0


def revalidate(args: argparse.Namespace) -> int:
    c = conn()
    row = c.execute("SELECT * FROM approvals WHERE id=?", (args.id,)).fetchone()
    if not row:
        print(json.dumps({"ok": False, "status": "not_found"}))
        return 2
    current = json.loads(args.current_snapshot_json)
    current_hash = digest(current)
    if current_hash != row["snapshot_hash"]:
        c.execute("UPDATE approvals SET status='blocked_changed', note=?, resolved_at=? WHERE id=?", ("El snapshot cambió antes de ejecutar", time.time(), args.id))
        c.commit()
        print(json.dumps({"ok": False, "status": "blocked_changed", "message": "No ejecuto: cambió el snapshot."}))
        return 4
    if row["status"] != "approved_pending_revalidation":
        print(json.dumps({"ok": False, "status": row["status"], "message": "La aprobación no está lista para ejecutar."}))
        return 0
    c.execute("UPDATE approvals SET status='ready_to_execute', note=?, resolved_at=? WHERE id=?", ("Snapshot revalidado; falta ejecutar mediante un executor autorizado", time.time(), args.id))
    c.commit()
    print(json.dumps({"ok": True, "status": "ready_to_execute", "message": "Snapshot idéntico; habilitada la ejecución autorizada."}))
    return 0


def complete(args: argparse.Namespace) -> int:
    """Consume a revalidated approval and record the executor outcome.

    This prevents an approved action from being replayed accidentally. The note
    must contain concrete evidence (remote ID, message ID, verification result,
    or the blocker that made execution partial/failed).
    """
    c = conn()
    row = c.execute("SELECT * FROM approvals WHERE id=?", (args.id,)).fetchone()
    if not row:
        print(json.dumps({"ok": False, "status": "not_found"}))
        return 2
    if row["status"] != "ready_to_execute":
        print(json.dumps({"ok": False, "status": row["status"], "message": "La aprobación no está en ready_to_execute."}))
        return 3
    status_by_result = {
        "executed": "executed",
        "dispatched_manual": "dispatched_manual",
        "partial": "executed_partial",
        "failed": "execution_failed",
    }
    status = status_by_result[args.result]
    c.execute(
        "UPDATE approvals SET status=?, note=?, resolved_at=? WHERE id=?",
        (status, args.note, time.time(), args.id),
    )
    c.commit()
    print(json.dumps({"ok": True, "id": args.id, "status": status, "result": args.result}, ensure_ascii=False))
    return 0


def main() -> int:
    p = argparse.ArgumentParser()
    sub = p.add_subparsers(dest="command", required=True)
    c = sub.add_parser("create")
    c.add_argument("--kind", required=True)
    c.add_argument("--title", required=True)
    c.add_argument("--body", required=True)
    c.add_argument("--snapshot-json", required=True)
    c.add_argument("--ttl", type=int, default=172800)
    c.set_defaults(fn=create)
    r = sub.add_parser("resolve")
    r.add_argument("--id", type=int, required=True)
    r.add_argument("--choice", choices=["approve", "postpone", "reject"], required=True)
    r.add_argument("--user-id", required=True)
    r.set_defaults(fn=resolve)
    v = sub.add_parser("revalidate")
    v.add_argument("--id", type=int, required=True)
    v.add_argument("--current-snapshot-json", required=True)
    v.set_defaults(fn=revalidate)
    x = sub.add_parser("complete")
    x.add_argument("--id", type=int, required=True)
    x.add_argument("--result", choices=["executed", "dispatched_manual", "partial", "failed"], required=True)
    x.add_argument("--note", required=True)
    x.set_defaults(fn=complete)
    args = p.parse_args()
    return args.fn(args)


if __name__ == "__main__":
    raise SystemExit(main())
