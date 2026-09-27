---
name: hook-lab
description: >-
  Generate and rank scroll-stopping hooks for a single content idea. Use when the
  user wants hooks, openers, first lines, video first-3-seconds, thumbnail text, or
  says "wymysl hooki", "hook na X", "10 wariacji haka", "scroll-stopper", "give me
  hooks", "first line for this post", "how should I open this". Takes one idea and
  produces 10+ hook variations across the full taxonomy (Curiosity Gap, Pattern
  Interrupt, Challenge a Common Belief, Negation, Number/Result, Before/After),
  each tagged with its technique and why it works, then ranks them and recommends a
  top 3 with the visual/written/audio treatment for the winner.
---

# hook-lab

One idea in, a batch of ranked hooks out. This is the **G(enerate)** step of SGTMS
applied to attention. Default output: **English**.
Reference: hook taxonomy + Triple-Threat in `../social-content-os/reference/frameworks.md` §4.
Load `../social-content-os/brand.json` for voice and audience.

## Inputs

- The one idea / insight / claim (rooted in an audience problem).
- Platform + format (Reel hook, carousel slide 1, LinkedIn first line, X post).
- Optional: the specific pain point or belief to attack.

## Method

Generate **at least 10** hooks, spread across the taxonomy so the user has real
variety to test (not 10 versions of the same technique):

- **Curiosity Gap** — open a loop the brain must close.
- **Pattern Interrupt** — contrast / unexpected pairing.
- **Challenge a Common Belief** — negate industry dogma (strongest trigger).
- **Negation** — "Why you should NOT do X."
- **Number / Result** — concrete outcome in concrete time.
- **Before / After** — transformation.

Rules for every hook:
- Clear over clever. A specific pain or bold promise beats wordplay.
- First words do the work — front-load the tension, no warm-up.
- No fluff, no jargon, no AI tells (no em-dashes, no "unlock/elevate/dive in").
- Keep them short enough to survive as on-screen text in a "safe zone".

## Output

1. A numbered list of 10+ hooks. Each line: the hook, then `— [technique]` and a
   3–6 word note on the psychological trigger.
2. **Top 3 ranked**, with one sentence each on why it will out-test the others for
   this audience.
3. For the #1 pick, the **Triple-Threat treatment**: the Visual (decluttered frame
   / focal point), the Written (the on-screen text), and the Audio (the spoken
   first line or sonic cue).
4. Offer the next step: send the winner to **carousel-builder** (slide 1) or
   **caption-writer** (post body), or run **Best of Nine** (recreate 3 formats x3).
