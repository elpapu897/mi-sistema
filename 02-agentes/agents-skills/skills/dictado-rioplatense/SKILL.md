---
name: dictado-rioplatense
description: "Interpretar mensajes dictados por voz en español rioplatense con transcripción defectuosa. Usar SIEMPRE que el mensaje tenga repeticiones, muletillas, palabras comodín ('coso'), autocorrecciones o nombres de productos deformados."
---

# Interpretar dictado en español rioplatense

Este usuario **habla, no escribe**. Sus mensajes llegan de un speech-to-text que
comete errores sistemáticos. Leerlos literalmente lleva a malentendidos.

## Reglas de lectura

1. **"coso" / "cosito" / "eso" = comodín.** Reemplaza cualquier sustantivo que no
   le salió. Resolvelo por contexto; si hay dos candidatos, preguntá cuál.
2. **Las repeticiones NO son énfasis**, son titubeo del habla: "de de la la campaña"
   = "de la campaña". No las trates como insistencia.
3. **Se autocorrige en voz alta.** "quiero azul, perdón, gris" → vale **lo último**.
   Frases tipo "no, mentira", "perdón", "digo" anulan lo anterior.
4. **Nombres propios deformados** — traducción conocida:

| Llega así | Es |
|---|---|
| Open Cloud / Open Co / OpenClaw mal dicho | OpenClaw |
| Germes / Ermes / Hermes | Hermes Agent |
| Cloud Code / Cloudco | Claude Code |
| Gombra / Gonvra | GONVRA (su tienda) |
| Heat Hub / Git Hub | GitHub |
| skins | skills |
| chabón | el youtuber/autor del tutorial que está mirando |

5. **"para el orto", "un quilombo", "trucho"** = algo está mal/feo/falso. Es queja
   concreta sobre calidad, no insulto personal.
6. **"ponele", "tipo", "viste", "bueno", "la verdad"** = muletillas sin contenido.
7. **"te lo pido hace cincuenta años"** = ya lo pidió antes y no se hizo. Es señal
   de frustración acumulada: **revisá el historial y resolvé eso primero**.

## Cómo responder

- **No le pidas que reformule** salvo que sea imposible entender. Le molesta.
- Cuando hay ambigüedad real, **elegí la interpretación más probable, decila
  explícitamente en una línea y seguí**: "Entiendo que querés X — voy con eso".
- Español rioplatense, vos/tenés/querés. **Sin jerga técnica**: es no técnico.
- Pide "todo, todo, todo" con frecuencia: **es entusiasmo, no una spec**. Si el
  alcance real es inviable, decíselo con números concretos antes de arrancar,
  y ofrecé un recorte. Odia que le prometan y no se cumpla.

## Configuración relacionada
En Hermes, `stt.language` debe estar en **`es`** (venía en `en` de fábrica y
transcribía cualquier cosa). Verificar con `hermes config get stt.language`.
