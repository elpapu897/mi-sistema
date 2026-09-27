#!/usr/bin/env python3
"""
Empaqueta las skills de ~/.agents/skills en ZIPs listos para subir a
claude.ai (Customize > Skills > "+" > Create skill > Upload a skill).

Las skills de claude.ai se comparten con Cowork: se sube una sola vez.

El frontmatter se corrige SOLO en la copia que va al ZIP.
~/.agents/skills queda intacto.

Uso:
    python3 empaquetar-skills.py [--origen DIR] [--destino DIR] [--solo nombre ...]
"""

import argparse
import csv
import os
import re
import shutil
import sys
import tempfile
import zipfile

import yaml

ORIGEN_DEF = os.path.expanduser("~/.agents/skills")
DESTINO_DEF = os.path.expanduser("~/skills-para-claude-ai")

MAX_NAME = 64
MAX_DESC = 1024
NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
FM_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n?(.*)$", re.S)

EXCLUIR_DIRS = {"__pycache__", ".git", "node_modules", ".venv", "venv", ".pytest_cache"}
EXCLUIR_FILES = {".DS_Store", "Thumbs.db"}
EXCLUIR_EXT = {".pyc", ".pyo"}


def sanear_name(bruto: str) -> str:
    """Convierte cualquier cosa en un name valido: [a-z0-9] y guiones, <=64."""
    s = re.sub(r"<[^>]*>", "", bruto or "")          # sin tags XML
    s = s.strip().lower()
    s = re.sub(r"[^a-z0-9]+", "-", s)
    s = re.sub(r"-{2,}", "-", s).strip("-")
    if len(s) > MAX_NAME:
        s = s[:MAX_NAME].rstrip("-")
    return s


def recortar_desc(bruto: str) -> str:
    """Limpia y recorta la description a <=1024 chars, cortando en frase."""
    s = re.sub(r"<[^>]*>", "", bruto or "")
    s = " ".join(s.split())
    if len(s) <= MAX_DESC:
        return s
    corte = s[:MAX_DESC]
    # preferir cortar en el ultimo final de frase
    for sep in (". ", "; ", ", "):
        idx = corte.rfind(sep)
        if idx > MAX_DESC * 0.6:
            return corte[: idx + 1].strip()
    idx = corte.rfind(" ")
    return (corte[:idx] if idx > 0 else corte).strip()


def desc_desde_cuerpo(cuerpo: str) -> str:
    """Fallback: arma una description con el primer parrafo real del cuerpo."""
    for linea in cuerpo.split("\n"):
        t = linea.strip()
        if t and not t.startswith(("#", ">", "-", "*", "|", "`")):
            return recortar_desc(t)
    return ""


def parsear_frontmatter(texto: str):
    """Devuelve (dict_campos, cuerpo). Parser tolerante: no usa YAML estricto,
    asi sobrevive a frontmatter roto."""
    m = FM_RE.match(texto)
    if not m:
        return {}, texto, False
    crudo, cuerpo = m.group(1), m.group(2)
    try:
        estricto = yaml.safe_load(crudo)
        if isinstance(estricto, dict):
            return estricto, cuerpo, True      # YAML valido: preservamos todo
    except Exception:
        pass
    campos, clave = {}, None
    for linea in crudo.split("\n"):
        km = re.match(r"^([A-Za-z_][\w-]*)\s*:\s*(.*)$", linea)
        if km:
            clave = km.group(1).strip()
            val = km.group(2).strip()
            if len(val) >= 2 and val[0] == val[-1] and val[0] in "\"'":
                val = val[1:-1]
            campos[clave] = val
        elif clave and linea.strip():
            campos[clave] = (campos[clave] + " " + linea.strip()).strip()
    return campos, cuerpo, False


def procesar_skill(origen_skill: str, carpeta: str):
    """Lee SKILL.md, corrige lo minimo, devuelve (texto_corregido, name, desc, arreglos)."""
    ruta = os.path.join(origen_skill, "SKILL.md")
    with open(ruta, encoding="utf-8", errors="replace") as f:
        texto = f.read()

    campos, cuerpo, yaml_ok = parsear_frontmatter(texto)
    arreglos = []
    if not campos:
        arreglos.append("frontmatter ausente/irrecuperable")

    # --- name: la carpeta manda (asi los duplicados desaparecen solos) ---
    name_orig = str(campos.get("name", "") or "")
    name = sanear_name(carpeta)
    if not name:
        name = sanear_name(name_orig) or "skill-sin-nombre"
    if name_orig != name:
        arreglos.append(f"name: {name_orig or '(vacio)'} -> {name}")

    # --- description ---
    desc_orig = str(campos.get("description", "") or "")
    desc = recortar_desc(desc_orig)
    if not desc:
        desc = desc_desde_cuerpo(cuerpo)
        arreglos.append("description generada desde el cuerpo" if desc
                        else "SIN DESCRIPTION (revisar a mano)")
    elif desc != " ".join((desc_orig or "").split()):
        arreglos.append(f"description recortada a {len(desc)} chars")

    # --- reconstruir frontmatter ---
    salida = {"name": name, "description": desc}
    if yaml_ok:
        # el YAML original era valido: conservamos los campos extra tal cual
        for k, v in campos.items():
            if k not in ("name", "description") and v is not None:
                salida[k] = v
    elif any(k not in ("name", "description") for k in campos):
        arreglos.append("campos extra descartados (YAML invalido)")

    fm = yaml.safe_dump(salida, sort_keys=False, allow_unicode=True,
                        default_flow_style=False, width=10 ** 9).rstrip("\n")
    return "---\n" + fm + "\n---\n\n" + cuerpo.lstrip("\n"), name, desc, arreglos


def copiar_limpio(src: str, dst: str) -> int:
    """Copia el arbol salteando basura. Devuelve cantidad de archivos."""
    n = 0
    for raiz, dirs, files in os.walk(src):
        dirs[:] = [d for d in dirs if d not in EXCLUIR_DIRS]
        rel = os.path.relpath(raiz, src)
        destino_dir = dst if rel == "." else os.path.join(dst, rel)
        os.makedirs(destino_dir, exist_ok=True)
        for f in files:
            if f in EXCLUIR_FILES or os.path.splitext(f)[1] in EXCLUIR_EXT:
                continue
            if rel == "." and f == "SKILL.md":
                continue  # lo escribimos corregido aparte
            shutil.copy2(os.path.join(raiz, f), os.path.join(destino_dir, f))
            n += 1
    return n


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--origen", default=ORIGEN_DEF)
    ap.add_argument("--destino", default=DESTINO_DEF)
    ap.add_argument("--solo", nargs="*", default=None,
                    help="empaquetar solo estas skills (por nombre de carpeta)")
    args = ap.parse_args()

    origen = os.path.expanduser(args.origen)
    destino = os.path.expanduser(args.destino)
    zips_dir = os.path.join(destino, "zips")

    if not os.path.isdir(origen):
        sys.exit(f"No existe el origen: {origen}")

    carpetas = sorted(
        d for d in os.listdir(origen)
        if os.path.isfile(os.path.join(origen, d, "SKILL.md"))
    )
    if args.solo:
        pedidas = set(args.solo)
        carpetas = [c for c in carpetas if c in pedidas]
        faltan = pedidas - set(carpetas)
        if faltan:
            print(f"AVISO: no encontradas -> {', '.join(sorted(faltan))}\n")

    if os.path.isdir(zips_dir):
        shutil.rmtree(zips_dir)
    os.makedirs(zips_dir, exist_ok=True)

    filas, total_arreglos, fallos = [], 0, []

    for i, carpeta in enumerate(carpetas, 1):
        src = os.path.join(origen, carpeta)
        try:
            skill_md, name, desc, arreglos = procesar_skill(src, carpeta)
        except Exception as e:
            fallos.append((carpeta, repr(e)))
            continue

        try:
            with tempfile.TemporaryDirectory() as tmp:
                raiz = os.path.join(tmp, name)
                os.makedirs(raiz, exist_ok=True)
                n_files = copiar_limpio(src, raiz)
                with open(os.path.join(raiz, "SKILL.md"), "w", encoding="utf-8") as f:
                    f.write(skill_md)

                zpath = os.path.join(zips_dir, f"{name}.zip")
                with zipfile.ZipFile(zpath, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as z:
                    for r, dirs, files in os.walk(raiz):
                        dirs.sort()
                        for fn in sorted(files):
                            full = os.path.join(r, fn)
                            z.write(full, os.path.relpath(full, tmp))
        except Exception as e:
            fallos.append((carpeta, repr(e)))
            continue

        kb = round(os.path.getsize(zpath) / 1024, 1)
        total_arreglos += len(arreglos)
        filas.append({
            "zip": f"{name}.zip",
            "name": name,
            "carpeta_origen": carpeta,
            "archivos": n_files + 1,
            "peso_kb": kb,
            "len_desc": len(desc),
            "arreglos": " | ".join(arreglos),
            "description": desc,
        })
        if i % 200 == 0:
            print(f"  ... {i}/{len(carpetas)}")

    manifiesto = os.path.join(destino, "manifiesto.csv")
    with open(manifiesto, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(filas[0].keys()) if filas else ["zip"])
        w.writeheader()
        w.writerows(filas)

    peso = sum(r["peso_kb"] for r in filas) / 1024
    print("\n" + "=" * 58)
    print(f"ZIPs generados : {len(filas)}")
    print(f"Peso total     : {peso:.1f} MB")
    print(f"Skills tocadas : {sum(1 for r in filas if r['arreglos'])} (arreglos: {total_arreglos})")
    print(f"Fallos         : {len(fallos)}")
    print(f"\nZIPs        -> {zips_dir}")
    print(f"Manifiesto  -> {manifiesto}")
    if fallos:
        print("\n--- fallos ---")
        for c, e in fallos[:20]:
            print(f"  {c}: {e}")


if __name__ == "__main__":
    main()
