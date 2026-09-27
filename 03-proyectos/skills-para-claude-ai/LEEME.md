# Skills listas para subir a claude.ai

**1139 ZIPs** en `zips/`, 21 MB en total. Cada uno contiene `<nombre>/SKILL.md`
en la raíz, que es exactamente lo que pide el uploader de claude.ai.

Origen: `~/.agents/skills` (1124) + `~/OBSIDIAN/03-Recursos/n8n-skills` (15).
Ninguna de las dos carpetas fue modificada: los arreglos se hicieron solo
sobre la copia que va adentro del ZIP.

## Cómo subirlas

1. claude.ai → **Customize > Skills**
2. Botón **"+"** → **"+ Create skill"** → **"Upload a skill"**
3. Subir el `.zip`

**No hace falta repetirlo para Cowork.** claude.ai chat y Cowork comparten la
misma lista de skills. Se sube una sola vez.

Requisito previo: **Settings > Capabilities > Code execution and file creation**
tiene que estar activado, si no la sección Skills no aparece.

## Importante: subir ≠ activar

Cada skill tiene su toggle on/off en la lista. Solo las **activas** gastan
contexto (~100 tokens de `name` + `description` cada una, siempre presentes en
el system prompt).

Con las 1139 activas serían ~114k tokens quemados antes de escribir nada, y la
propia doc de Anthropic avisa que con demasiadas skills Claude elige mal o
directamente se saltea la correcta. La API topea en 20 skills por request.

**Recomendación: subí las que quieras tener a mano, pero dejá activas ~15-25
por vez** y andá cambiando según en qué estés trabajando.

## Manifiesto

`manifiesto.csv` — una fila por skill:

| columna | qué es |
|---|---|
| `zip` | nombre del archivo |
| `name` | el `name` del frontmatter (= nombre del ZIP) |
| `carpeta_origen` | carpeta original, por si el name se renombró |
| `archivos` | cantidad de archivos adentro |
| `peso_kb` | peso del ZIP |
| `len_desc` | largo de la description (límite 1024) |
| `arreglos` | qué se corrigió respecto del original |
| `description` | la description final, para buscar y decidir qué activar |

Útil para elegir qué subir primero:

```bash
python3 -c "import csv;[print(r['zip'],'|',r['description'][:90]) for r in csv.DictReader(open('manifiesto.csv')) if 'n8n' in r['name']]"
```

## Arreglos aplicados (167 skills tocadas, 972 intactas)

- **108** — `name` no coincidía con la carpeta (ej. `muapi-blog-header` → `blog-header`).
  Se fuerza `name` = nombre de carpeta, lo que además elimina los 41 nombres duplicados.
- **59** — `description` pasaba los 1024 caracteres. Recortada en el último fin de frase.
- **2** — frontmatter ausente o irrecuperable, reconstruido.
- **2** — `description` generada desde el primer párrafo del cuerpo.
- **2** — campos extra descartados porque su YAML era inválido (se conservaron
  `name` y `description`).

## Regenerar

```bash
python3 ~/Claude/scripts/empaquetar-skills.py --destino ~/skills-para-claude-ai
```

Opciones: `--origen DIR`, `--destino DIR`, `--solo nombre1 nombre2 ...`

Ojo: borra y rehace `zips/`. Las 15 de n8n van en una corrida aparte con
`--origen ~/OBSIDIAN/03-Recursos/n8n-skills`.
