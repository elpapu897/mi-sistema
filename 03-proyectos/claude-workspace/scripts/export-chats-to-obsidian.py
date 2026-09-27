#!/usr/bin/env python3
"""
Exporta los chats de Claude Code, Codex y Hermes a Obsidian como notas markdown.
Así cualquier agente (o vos) puede leer las conversaciones de los otros desde el vault.

Uso:
    python3 export-chats-to-obsidian.py
Corre solo (idempotente): podés ejecutarlo cuando quieras y actualiza lo que cambió.

Salida:
    ~/OBSIDIAN/07-Agentes/ClaudeCode/chats/
    ~/OBSIDIAN/07-Agentes/Codex/chats/
    ~/OBSIDIAN/07-Agentes/Hermes/chats/
"""
import json, os, re, subprocess, sys
from pathlib import Path
from datetime import datetime

HOME = Path.home()
VAULT = HOME / "OBSIDIAN" / "07-Agentes"
CLAUDE_DIR = HOME / ".claude" / "projects"
CODEX_DIR = HOME / ".codex" / "sessions"

def slug(text, maxlen=60):
    text = re.sub(r"\s+", " ", (text or "").strip())
    text = re.sub(r"[^\w\sáéíóúñÁÉÍÓÚÑ-]", "", text)
    text = text.strip().replace(" ", "-")[:maxlen].strip("-")
    return text or "chat"

def fmt_ts(ts):
    if not ts:
        return ""
    try:
        return datetime.fromisoformat(str(ts).replace("Z", "+00:00")).strftime("%Y-%m-%d %H:%M")
    except Exception:
        return str(ts)[:16]

def extract_text(content):
    """Content puede ser string o lista de bloques."""
    if isinstance(content, str):
        return content.strip()
    if isinstance(content, list):
        parts = []
        for b in content:
            if isinstance(b, dict):
                t = b.get("type")
                if t in ("text", "input_text", "output_text") and b.get("text"):
                    parts.append(b["text"])
                elif t == "tool_use":
                    parts.append(f"_[usó herramienta: {b.get('name','?')}]_")
                elif t == "tool_result":
                    parts.append("_[resultado de herramienta]_")
                elif b.get("text"):
                    parts.append(b["text"])
            elif isinstance(b, str):
                parts.append(b)
        return "\n\n".join(p for p in parts if p).strip()
    return ""

def write_md(out_dir, fname, title, tool, session_id, date, lines):
    if not lines:
        return False
    out_dir.mkdir(parents=True, exist_ok=True)
    body = [
        "---",
        f"tool: {tool}",
        f"session_id: {session_id}",
        f"fecha: {date}",
        f'titulo: "{title}"',
        "tags: [chat, agente, " + tool.lower() + "]",
        "---",
        "",
        f"# 💬 {title}",
        f"> **{tool}** · {date} · `{session_id}`",
        "",
        "---",
        "",
    ]
    body.extend(lines)
    path = out_dir / fname
    path.write_text("\n".join(body), encoding="utf-8")
    return True

# ---------- CLAUDE CODE ----------
def export_claude():
    out = VAULT / "ClaudeCode" / "chats"
    n = 0
    files = [p for p in CLAUDE_DIR.rglob("*.jsonl") if "subagents" not in str(p)]
    for f in files:
        try:
            msgs, first_user, ts0, sid = [], None, None, f.stem[:8]
            for line in f.read_text(encoding="utf-8", errors="ignore").splitlines():
                try:
                    d = json.loads(line)
                except Exception:
                    continue
                if d.get("type") not in ("user", "assistant"):
                    continue
                m = d.get("message", {})
                role = m.get("role", d.get("type"))
                txt = extract_text(m.get("content"))
                if not txt:
                    continue
                ts = d.get("timestamp")
                if ts0 is None:
                    ts0 = ts
                if role == "user" and first_user is None:
                    first_user = txt
                who = "🧑 Vos" if role == "user" else "🤖 Claude"
                msgs.append(f"### {who}  <small>{fmt_ts(ts)}</small>\n\n{txt}\n")
            if not msgs:
                continue
            date = fmt_ts(ts0)
            title = slug(first_user, 50).replace("-", " ") or "chat"
            fname = f"{(date[:10] or '0000')}--{slug(first_user,40)}--{sid}.md"
            if write_md(out, fname, title, "ClaudeCode", f.stem, date, msgs):
                n += 1
        except Exception as e:
            print(f"  ! Claude {f.name}: {e}", file=sys.stderr)
    return n

# ---------- CODEX ----------
def export_codex():
    out = VAULT / "Codex" / "chats"
    n = 0
    for f in CODEX_DIR.rglob("rollout-*.jsonl"):
        try:
            msgs, first_user, ts0, sid = [], None, None, "?"
            for line in f.read_text(encoding="utf-8", errors="ignore").splitlines():
                try:
                    d = json.loads(line)
                except Exception:
                    continue
                typ = d.get("type")
                pl = d.get("payload", {}) if isinstance(d.get("payload"), dict) else {}
                if typ == "session_meta":
                    sid = pl.get("session_id", sid)
                    ts0 = ts0 or d.get("timestamp")
                    continue
                role = pl.get("role")
                if role in ("user", "assistant") and pl.get("content"):
                    txt = extract_text(pl.get("content"))
                    if not txt or txt.startswith("<"):
                        continue
                    ts = d.get("timestamp")
                    ts0 = ts0 or ts
                    if role == "user" and first_user is None:
                        first_user = txt
                    who = "🧑 Vos" if role == "user" else "🤖 Codex"
                    msgs.append(f"### {who}  <small>{fmt_ts(ts)}</small>\n\n{txt}\n")
            if not msgs:
                continue
            date = fmt_ts(ts0)
            title = slug(first_user, 50).replace("-", " ") or "chat"
            fname = f"{(date[:10] or '0000')}--{slug(first_user,40)}--{sid[:8]}.md"
            if write_md(out, fname, title, "Codex", sid, date, msgs):
                n += 1
        except Exception as e:
            print(f"  ! Codex {f.name}: {e}", file=sys.stderr)
    return n

# ---------- HERMES ----------
def hermes_session_ids():
    """Lista todos los IDs de sesión de Hermes."""
    try:
        r = subprocess.run(["hermes", "sessions", "list", "--limit", "9999"],
                           capture_output=True, text=True, timeout=60)
        ids = []
        for line in r.stdout.splitlines():
            m = re.search(r"(\d{8}_\d{6}_[0-9a-f]+)\s*$", line.strip())
            if m:
                ids.append(m.group(1))
        return ids
    except Exception as e:
        print(f"  ! Hermes list: {e}", file=sys.stderr)
        return []

def export_hermes():
    out = VAULT / "Hermes" / "chats"
    out.mkdir(parents=True, exist_ok=True)
    ids = hermes_session_ids()
    n = 0
    for sid in ids:
        try:
            r = subprocess.run(
                ["hermes", "sessions", "export", "--format", "md", str(out),
                 "--session-id", sid, "--yes"],
                capture_output=True, text=True, timeout=120,
            )
            if "Exported 1" in r.stdout or "Exported" in r.stdout:
                n += 1
        except Exception as e:
            print(f"  ! Hermes {sid}: {e}", file=sys.stderr)
    return n

# ---------- INDICE ----------
def build_index(counts):
    idx = [
        "---", "tags: [indice, chats, agentes]", "---", "",
        "# 🧠 Chats de todos los agentes",
        f"> Actualizado: {datetime.now().strftime('%Y-%m-%d %H:%M')}",
        "",
        "Todas las conversaciones de tus agentes, en un solo lugar. Cualquier agente puede leer acá.",
        "",
        "| Agente | Chats | Carpeta |",
        "|---|---:|---|",
    ]
    for tool, c in counts.items():
        idx.append(f"| {tool} | {c} | [[{tool}/chats]] |")
    idx += ["", "← Volver a [[README]]"]
    (VAULT / "CHATS-INDICE.md").write_text("\n".join(idx), encoding="utf-8")

def main():
    print("Exportando chats a Obsidian…")
    counts = {}
    counts["ClaudeCode"] = export_claude(); print(f"  ✓ Claude Code: {counts['ClaudeCode']} chats")
    counts["Codex"] = export_codex();       print(f"  ✓ Codex: {counts['Codex']} chats")
    counts["Hermes"] = export_hermes();     print(f"  ✓ Hermes: {counts['Hermes']} chats")
    build_index(counts)
    print(f"\nListo. Índice: {VAULT/'CHATS-INDICE.md'}")

if __name__ == "__main__":
    main()
