#!/usr/bin/env python3
"""
Tapa credenciales en los chats exportados a Obsidian.

Los chats se exportan solos cada 30 min y arrastran cualquier token que se
haya pegado en la conversacion. Esto los deja legibles pero sin el secreto.

Deja visibles los primeros caracteres para saber de cual se trataba.
"""
import re
import sys
from pathlib import Path

BOVEDA = Path.home() / "OBSIDIAN" / "07-Agentes"

PATRONES = [
    (re.compile(r"\bshpat_[A-Za-z0-9]{10,}"),            "shpat_[TAPADO]"),
    (re.compile(r"\bshpca_[A-Za-z0-9]{10,}"),            "shpca_[TAPADO]"),
    (re.compile(r"\bshppa_[A-Za-z0-9]{10,}"),            "shppa_[TAPADO]"),
    (re.compile(r"\batkn_[A-Za-z0-9._\-]{20,}"),         "atkn_[TAPADO]"),
    (re.compile(r"\bGOCSPX-[A-Za-z0-9_\-]{10,}"),        "GOCSPX-[TAPADO]"),
    (re.compile(r"\bIGAA[A-Za-z0-9_\-]{40,}"),           "IGAA[TAPADO]"),
    (re.compile(r"\bEAA[A-Za-z0-9]{60,}"),               "EAA[TAPADO]"),
    (re.compile(r"\bsk-[A-Za-z0-9\-_]{20,}"),            "sk-[TAPADO]"),
    (re.compile(r"\bghp_[A-Za-z0-9]{20,}"),              "ghp_[TAPADO]"),
    (re.compile(r"\bxox[baprs]-[A-Za-z0-9\-]{10,}"),     "xox-[TAPADO]"),
]


def main():
    if not BOVEDA.exists():
        print("No existe", BOVEDA)
        return 0
    tocados = 0
    total = 0
    for f in BOVEDA.rglob("*.md"):
        try:
            texto = f.read_text(encoding="utf-8", errors="ignore")
        except Exception:
            continue
        nuevo = texto
        encontrados = 0
        for patron, reemplazo in PATRONES:
            nuevo, n = patron.subn(reemplazo, nuevo)
            encontrados += n
        if encontrados:
            try:
                f.write_text(nuevo, encoding="utf-8")
                print("  %-52s %d tapada(s)" % (f.name[:52], encontrados))
                tocados += 1
                total += encontrados
            except Exception as e:
                print("  no se pudo escribir", f.name, e)
    if tocados:
        print("\n%d archivo(s) limpiados, %d credencial(es) tapadas." % (tocados, total))
    else:
        print("Nada que tapar.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
