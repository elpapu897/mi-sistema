---
name: perfil-apps-citas
description: Optimizar perfiles de apps de citas (Tinder, Bumble, Hinge) - selección de fotos, bio, prompts y estrategia de swipe. Usar cuando el usuario tiene pocos matches, quiere que le revisen el perfil, o está armando uno nuevo.
allowed-tools: Read, Glob, Grep
---

# Perfil de apps de citas

**El 90% de los resultados en apps se define antes de escribir un solo mensaje.**
Si alguien no tiene matches, el problema casi nunca son sus aperturas: son las fotos.
Trabajá el perfil primero.

## Orden de impacto

1. **Foto principal** — decide el 80% de los swipes
2. **Resto de las fotos** — deciden casi todo el resto
3. **Bio / prompts** — filtran y dan material para abrir la charla
4. **Estrategia de swipe** — afecta cuánto te muestra el algoritmo

## Fotos

### Las 6 que hacen un buen perfil

| # | Tipo | Qué tiene que mostrar |
|---|---|---|
| 1 | **Principal: cara clara** | Vos solo, cara visible, sonrisa genuina, buena luz, medio cuerpo |
| 2 | **Cuerpo entero** | De pie, ropa que te quede bien. Su ausencia genera sospecha |
| 3 | **Haciendo algo** | Tu hobby real: tocando, cocinando, escalando, con el perro |
| 4 | **Social** | Con amigos, riéndote. Prueba de vida social |
| 5 | **Interesante/viaje** | Un lugar, un contexto, algo que dé tema |
| 6 | **Personalidad** | Algo raro, gracioso o que te represente |

### Errores que arruinan un perfil

- **Selfie de espejo en el baño** — el clásico. Sacala
- **Foto grupal como principal** — nadie va a adivinar cuál sos
- **Anteojos de sol en todas** — no se te ve la cara
- **Filtros de Snapchat/perritos** — no
- **Solo primeros planos** — genera sospecha sobre el cuerpo
- **Fotos oscuras, borrosas o de 2016**
- **El pescado / el auto / el gimnasio con el torso al aire** — cliché, y la última filtra
  a la mayoría de las mujeres que buscan algo serio
- **Foto con otra mujer sin contexto** — pregunta incómoda instantánea
- **Cero sonrisa en todas** — la cara seria en las 6 lee frío

### Cómo conseguir buenas fotos sin ser fotógrafo

- Un amigo, un celular, **luz natural** (mañana temprano o atardecer), 20 minutos.
- **50 fotos, elegís 5.** El volumen es todo.
- No mires a la cámara en todas. Reírte de algo real > sonrisa forzada.
- Ropa que te quede bien y que sea tuya. Nada de disfraz.
- Fondo limpio, sin desorden atrás.
- **Pedí opinión externa** (una amiga, no un amigo). Vos sos el peor juez de tus fotos.

## Bio

**Corta, específica, con algo para responder.** 2-4 líneas.

### Estructura que funciona
```
[qué hacés, con gracia] + [1-2 cosas específicas tuyas] + [gancho o invitación]
```

**Ejemplos:**
> Diseñador. Cocino bien, canto mal. Busco alguien que me explique por qué la gente corre maratones.

> Argentino en modo permanente de "voy a empezar el gimnasio el lunes". Melómano, perro-dependiente, fanático del café.
> Contame el peor plan que te salió bien.

### Lo que no va
- Vacío ("preguntá") → parece cuenta trucha o desinterés
- Lista de negativos ("no busco nada serio, no me escribas si...") → arranca hostil
- Frase motivacional o de Instagram
- Ironía muy densa que no se entiende
- Altura + signo + emojis y nada más
- Bio de 12 líneas contando tu vida

## Prompts (Hinge)

Elegí prompts que **den una historia**, no una respuesta de una palabra.

| ❌ Débil | ✅ Fuerte |
|---|---|
| "Dato inusual sobre mí: soy zurdo" | "Dato inusual: hice dedo hasta Bariloche con 40 pesos y una guitarra que no sé tocar" |
| "Busco: buena onda" | "Juntos podríamos: probar los 12 lugares de milanesa de mi lista y hacer un ranking serio" |
| "Me hace reír: los memes" | "Confesión: le hablo a mi perro con voz de bebé y no me arrepiento" |

Regla: si tu respuesta puede ser de cualquier persona, cambiala.

## Estrategia de uso

- **Swipe con criterio, no en masa.** Los algoritmos castigan el like indiscriminado
  y te muestran menos.
- **Mejor pocas apps bien hechas** que cinco perfiles a medias.
- **Hinge** premia el comentario en el like: usalo siempre.
- **Bumble** ella escribe primero: tu perfil tiene que dar material para que sepa qué decirte.
- **Refrescá el perfil** cada 4-6 semanas: cambiá la foto principal y mirá si mejora.
- **Testeá:** cambiá una sola cosa por vez y medí. Si cambiando la principal duplicás
  los matches, era la principal.

## Diagnóstico rápido

| Síntoma | Causa probable |
|---|---|
| Casi cero matches | Foto principal. Siempre empezá por ahí |
| Matches pero nadie contesta | Bio vacía + aperturas genéricas |
| Contestan pero se apaga rápido | Ver skill `chat-primeros-mensajes` |
| Matches pero ninguna quiere verse | Estás chateando demasiado tiempo. Ver `invitar-a-salir` |

## Lo más importante

Un perfil optimizado te consigue conversaciones. **No te consigue una relación.**
El perfil es la puerta; lo que pasa adentro depende de vos siendo vos. Que las fotos
y la bio sean reales: exagerar sólo garantiza una primera cita incómoda.

## Referencias

- `references/checklist-fotos.md` — auditoría foto por foto y cómo producir un set
- `references/bios-y-prompts.md` — ejemplos por perfil de persona y errores comunes
