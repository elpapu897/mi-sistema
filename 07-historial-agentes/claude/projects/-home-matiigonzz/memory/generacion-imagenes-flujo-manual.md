---
name: generacion-imagenes-flujo-manual
description: "Las imágenes se generan a mano en la app de Gemini, no por API — la key de Gemini no tiene cuota de imagen"
metadata: 
  node_type: memory
  type: project
  originSessionId: 80bb80cd-6451-4216-8e37-363ea38f7c99
  modified: 2026-08-05T03:56:17.829Z
---

Para generar imágenes, el flujo es manual: yo escribo los prompts, el usuario los pega en gemini.google.com (tiene Google One / AI Pro), y guarda los PNG en `~/imagenes/generadas/`. Yo trabajo desde ahí.

**Why:** La suscripción de Google One da Nano Banana solo en la app, no cuota de API. La key en `~/.claude/.env` es válida y sirve para texto, pero todos los modelos de imagen devuelven `429 limit: 0` porque el free tier de la API no incluye imágenes. El usuario decidió no activar facturación pay-as-you-go.

**How to apply:** No intentar llamar a `gemini-*-image` por API — va a fallar. Escribir los prompts en `~/imagenes/prompts/` y esperar a que el usuario traiga los archivos. Los scripts de la skill `design` (logo, icono, CIP) tampoco funcionan por el mismo motivo. Si en algún momento activa billing, todo lo demás ya está listo (`google-genai` instalado, key configurada).
