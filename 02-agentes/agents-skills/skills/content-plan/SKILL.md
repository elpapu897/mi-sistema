---
name: content-plan
description: >-
  Build a social media content plan / calendar from a niche or business. Use when
  the user asks to plan content, build a content calendar, decide what to post,
  map a month of posts, or says "content plan", "plan tresci", "zaplanuj miesiac
  postow", "what should I post this week/month", "content calendar", "posting
  schedule". Builds a Topic Tree (Niche of One + 3 interests + subtopics), then a
  2–4 week calendar where every post is tagged with format, Awareness Funnel stage,
  funnel layer (ToF/MoF/BoF), hook angle, and CTA, following SGTMS cadence. Outputs
  a markdown plan plus a table and an importable CSV.
---

# content-plan

Turn a niche/business into a structured posting plan. Default output: **English**.
Read `../social-content-os/reference/frameworks.md` for the strategy basis
(Topic Tree §9, Awareness Funnel §7, funnel layers §8, SGTMS §5, Best of Nine §6).
Load `../social-content-os/brand.json` for voice, audience, platforms, CTA.

## Inputs to confirm (ask only what's missing)

- Niche / business and the audience you want to stop mid-scroll.
- Platforms (default to brand.json).
- Time span: default **4 weeks**. Posting frequency per platform (default 4–5/wk IG, 3/wk LinkedIn).
- Primary business goal for the period (leads? launch? audience growth?).
- Whether there's an offer/launch to build toward (sets the funnel weighting).

## Method

1. **Topic Tree.** Establish the Niche of One (the user's unique angle), 3 broad
   interests, and 6–12 subtopics. Broad topics feed ToF growth; narrow ones feed
   MoF/BoF conversion.
2. **Funnel weighting.** Default mix per week: ~60% ToF (Discovery), ~30% MoF
   (Nurture), ~10% BoF (Conversion). Shift toward BoF in a launch week.
3. **Map the Awareness stages.** Spread posts across Unaware → Problem-aware →
   Consideration → Decision so the feed nurtures, not just sells.
4. **Assign formats** per platform: Reels/Shorts (ToF hooks), carousels (MoF
   value/dwell time), text/LinkedIn (authority), stories (BoF/offers).
5. **Best of Nine cadence.** Schedule at least one repeatable format recreated 3x
   across the span so the user can spot a winning pattern, not a one-off spike.
6. **Each row gets:** date, platform, format, working title/idea, hook angle (name
   the technique from the taxonomy §4), funnel stage, funnel layer, CTA.

## Output

1. A short strategy header: the Topic Tree + the funnel weighting + the one
   "north-star" metric for the period (saves / leads / watch-time).
2. A **calendar table** (one row per post) with all tags above.
3. An importable **CSV** saved to the working directory
   (`content-plan-<brand>-<span>.csv`) with the same columns, so it drops into
   Notion / Sheets / a scheduler.
4. A closing "what to do next" line: which 3–5 ideas to send to **hook-lab** first,
   and which to build as carousels via **carousel-builder**.

Keep titles concrete and specific. No filler ideas like "share a motivational
quote" — every row must have a real angle tied to a subtopic and a funnel job.
