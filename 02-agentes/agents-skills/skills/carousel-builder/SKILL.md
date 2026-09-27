---
name: carousel-builder
description: >-
  Build a 7–10 slide Instagram/LinkedIn carousel (1080x1350) from a topic or
  script AND render the slides to PNG. Use when the user wants a carousel, slides,
  a slide deck for IG/LinkedIn, or says "zrob karuzele o X", "slajdy na instagram",
  "carousel", "make a carousel", "build slides", "turn this into a carousel". Writes
  slide-by-slide copy (scroll-stop hook, tension+value middle with light/dark rhythm,
  identity CTA), a per-slide JSON background-image prompt, generates the background
  imagery via the fal-media skill, then renders crisp on-brand PNG slides via the
  bundled render_carousel.py (headless Chrome). Outputs the slide PNGs plus a caption.
---

# carousel-builder

Produce a finished, renderable carousel: on-brand copy + real PNG slides. Default
output: **English**. Text is rendered as crisp HTML/CSS (never baked into an image
model, which mangles paragraph text); imagery is the optional background layer.
Reference: carousel mechanics §10, ABC §3, JSON prompting §12 in
`../social-content-os/reference/frameworks.md`. Load `../social-content-os/brand.json`.

## Inputs

- Topic, script, or the winning hook (from hook-lab).
- Slide count (default 8; range 7–10).
- Platform (IG default). Whether to generate background imagery (default yes).

## Build steps

1. **Structure the deck** (ABC across slides):
   - **Slide 1 — Scroll-Stop (hook, dark theme):** the hook on a specific pain
     point. Highest visual energy.
   - **Middle — Tension & Value:** one idea per slide, numbered. Alternate
     `theme` light/dark for the "rhythm check". Match visual energy to narrative
     energy (high contrast on tension, calmer on teaching).
   - **Final — Identity CTA:** align the CTA with who the viewer wants to become,
     plus the comment-trigger ("Comment WORD").
   - Keep each slide to one idea; headline short, body 1–2 lines max.
2. **Write `slides.json`** in a new carousel folder (default
   `./carousels/<slug>/slides.json`). Schema:
   ```json
   {
     "slides": [
       {"n":1,"type":"hook","theme":"dark","eyebrow":"SECTION TAG",
        "headline":"...","body":"","bg_image":"bg-1.png","bg_prompt":"..."},
       {"n":2,"type":"value","theme":"light","eyebrow":"...","headline":"...","body":"..."},
       {"n":8,"type":"cta","theme":"dark","eyebrow":"...","headline":"...","body":"..."}
     ]
   }
   ```
   `type` is `hook` | `value` | `cta`. `bg_prompt` is the JSON-style image brief
   (subject as metaphor, not decoration; brand mood/palette); `bg_image` is the
   filename it will be saved as.
3. **Generate backgrounds (if enabled):** for slides with a `bg_prompt`, invoke the
   **fal-media** skill to generate each background image and save it into the
   carousel folder as the `bg_image` filename. Use a 4:5 / portrait size. Put NO
   hex codes or on-screen text in the image prompt — describe the scene/mood only
   (the typography is added by the renderer). Hero slides (1 and the CTA) benefit
   most; teaching slides can stay solid-color (omit bg_image) for legibility.
4. **Render:** run
   `python3 <this skill dir>/render_carousel.py ./carousels/<slug>` to produce
   `slide-01.png … slide-NN.png` (2160x2700, downscale-safe for IG/LinkedIn).
5. **Write the caption** by handing the topic to the **caption-writer** skill (or
   inline a quick one): hook line + 2–4 value lines + the comment-trigger CTA +
   3–6 hashtags. Remind the user to add music so it also hits the Reels feed.

## Output

- The carousel folder with `slides.json` and the rendered `slide-*.png`.
- The caption.
- A one-line note on what to test next (Best of Nine: recreate this format 3x with
  different hooks).

Keep copy specific and human. No AI tells (no em-dashes, en-dashes, smart quotes,
"unlock/elevate/dive in"). If fal-media or Chrome is unavailable, still write
`slides.json` and the copy, and tell the user what's missing.
