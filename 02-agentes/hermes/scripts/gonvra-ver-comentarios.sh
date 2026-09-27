#!/usr/bin/env bash
# GONVRA — Muestra los comentarios de Instagram que llegaron al webhook,
# con autor y texto, para saber si son REALES o pruebas técnicas.
#
# Uso:  bash ~/.hermes/scripts/gonvra-ver-comentarios.sh

echo "════════════════════════════════════════════════════"
echo "  COMENTARIOS QUE LLEGARON DESDE INSTAGRAM"
echo "════════════════════════════════════════════════════"
echo

python3 - <<'PY'
import json
import os
import sqlite3

DB = os.path.expanduser("~/.n8n/database.sqlite")
c = sqlite3.connect(f"file:{DB}?mode=ro", uri=True)

# n8n guarda las ejecuciones en formato "flatted": un array donde los strings
# que son numeros apuntan a otra posicion del mismo array.
def resolver(arr, v):
    vistos = 0
    while isinstance(v, str) and v.isdigit() and vistos < 10:
        idx = int(v)
        if idx >= len(arr):
            return None
        v = arr[idx]
        vistos += 1
    return v


def sacar_comentario(blob):
    try:
        arr = json.loads(blob)
    except Exception:
        return None, None
    if not isinstance(arr, list):
        return None, None
    for item in arr:
        if isinstance(item, dict) and "comentario_id" in item and "texto" in item:
            autor = resolver(arr, item.get("autor"))
            texto = resolver(arr, item.get("texto"))
            if isinstance(autor, str) or isinstance(texto, str):
                return autor, texto
    return None, None


q = """select e.id, e.status, e.startedAt, d.data
       from execution_entity e
       join workflow_entity w on w.id = e.workflowId
       left join execution_data d on d.executionId = e.id
       where w.name like '%Comentario%'
       order by e.id desc limit 15"""

filas = list(c.execute(q))
if not filas:
    print("  Todavia no llego NADA.")
    print()
    print("  Probá así:")
    print("   1) Abrí un post de @gonvra1")
    print("   2) Comentá la palabra:  precio")
    print("   3) Esperá 30 segundos y volvé a correr esto")
    raise SystemExit

PRUEBA = {"cliente_test", "test", ""}
reales, pruebas, sin_dato = 0, 0, 0
salida = []

for eid, estado, cuando, datos in filas:
    autor, texto = (None, None)
    if datos:
        autor, texto = sacar_comentario(datos)

    if autor is None:
        tipo, sin_dato = "sin dato", sin_dato + 1
    elif str(autor).lower() in PRUEBA:
        tipo, pruebas = "PRUEBA", pruebas + 1
    else:
        tipo, reales = "REAL", reales + 1

    salida.append((eid, estado, str(cuando)[:19], tipo, autor, texto))

print(f"  {len(filas)} evento(s)  ·  REALES: {reales}  ·  pruebas mías: {pruebas}"
      + (f"  ·  sin dato: {sin_dato}" if sin_dato else ""))
print()
for eid, estado, cuando, tipo, autor, texto in salida:
    icono = "OK" if estado == "success" else "!!"
    print(f"  {icono}  {tipo:<8} #{eid}  {cuando}")
    if autor:
        print(f"        de @{autor}")
    if texto:
        print(f'        "{str(texto)[:88]}"')
print()

if reales:
    print("  ✅ LLEGO UN COMENTARIO REAL.")
    print("     El circuito funciona con la app en modo Desarrollo:")
    print("     NO hace falta publicarla.")
else:
    print("  Todavía no llegó ningún comentario real (solo pruebas técnicas).")
    print()
    print("  OJO: tiene que ser desde OTRA cuenta, no desde @gonvra1.")
    print("  Instagram NO avisa cuando el dueño comenta en su propio post.")
    print()
    print("  1) Abrí un post de @gonvra1")
    print("  2) Desde tu cuenta personal (u otra), comentá:  precio")
    print("  3) Esperá 30 segundos y volvé a correr esto")
    print()
    print("  Si aún así no aparece, hay que publicar la app en Meta.")
PY
