---
name: social-content-os
description: >-
  Router and onboarding for the Social Content OS pack — a system for planning
  and producing high-performing social media content (Instagram, LinkedIn,
  TikTok, X) based on the Interest Graph / Graffiti playbook (ABC hooks, SGTMS,
  Awareness Funnel, Best of Nine, carousels, ManyChat monetization). Use when the
  user wants help with social media content but hasn't picked a specific task, or
  says "social content os", "pomoz mi z social media", "od czego zaczac z
  contentem", "help me with my social media", "what should I post". Explains the
  system, loads the brand profile, and routes to the right sub-skill: content-plan,
  hook-lab, carousel-builder, caption-writer, or repurpose.
---

# Social Content OS

The entry point and router for the pack. Use it to onboard a user, load their
brand, and send them to the right tool. Default output language: **English**
(switch to the user's language if their topic or audience is in another language).

## The system in one screen

Reach is decided by the **Interest Graph**, not your follower count: every post is
tested on a small audience first and only scales if it performs. So you ship like a
**graffiti artist** — speed and volume over polish — and let data pick winners.
Full reference: `reference/frameworks.md` (read it before doing strategy work).

## The five tools

| You want to... | Use |
|---|---|
| Plan what to post (calendar, topic tree, funnel mapping) | **content-plan** |
| Turn one idea into 10+ ranked scroll-stopping hooks | **hook-lab** |
| Build a 7–10 slide carousel and render the slides | **carousel-builder** |
| Write a caption, IG/LinkedIn post, or CTA | **caption-writer** |
| Break one long-form asset into a batch of posts | **repurpose** |

## How to route

1. **Load the brand.** Read `brand.json` in this skill's directory. If it's still
   the template (brand_name is "Your Brand"), run onboarding (below) first — good
   output needs a real brand profile.
2. **Match intent** to the table above and invoke that skill via the Skill tool.
   If the request is broad ("help me grow on Instagram"), start with **content-plan**.
3. **Chain when useful.** A typical flow: content-plan → hook-lab on the best
   ideas → carousel-builder / caption-writer to produce → repurpose to multiply.

## Onboarding (first run / template brand)

Ask for these, then write `brand.json` (keep it short, one pass):

- Brand name + handle, and the one-liner: what you help people do.
- Audience: who you're stopping mid-scroll.
- Topic Tree: your Niche-of-One angle + 3 broad interests + a few subtopics.
- Voice: 3–5 adjectives.
- Colors: background, accent, ink (hex). Defaults are fine if unsure.
- CTA: the comment-trigger WORD and what ManyChat promises in the DM.
- Platforms in play.

Once saved, confirm and route to the tool that matches what they came for.

## Non-negotiable quality bar

Hook first, always. Clear over clever. One idea, one CTA per asset. Specific beats
generic. Every asset maps to a funnel stage. No AI tells in human-facing copy
(no em-dashes, en-dashes, smart quotes, or "unlock/elevate/dive in/game-changer").
