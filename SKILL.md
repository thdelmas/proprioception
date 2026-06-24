---
name: proprioception
description: "The feedback organ — the agent's sense of its own performance and the correction that follows from it. Where every other organ runs open-loop on its own quality (the loop decides but never grades its decisions, playtime explores but never measures whether it improved anything, rem-sleep records what happened but doesn't judge how well), proprioception closes the loop: observe your own recent actions, score them against the standard you declared, diagnose the error, write the correction back into how you work, and verify it actually helped. Biologically the proprioceptive sense + the cerebellum — compare intended motion to actual, learn the delta, make the next execution smoother. It examines MEANS (am I executing well, and how do I execute better), the complement to contemplation's ENDS. Functional, not mystical. TRIGGERS: 'proprioception', 'self-evaluation', 'evaluate yourself', 'how am I doing', 'self-improve', 'self-correct', 'grade my performance', 'after-action review', 'retro on that', 'what went wrong', 'did that actually work', 'close the loop', 'recalibrate', 'tune your approach', 'where did I go wrong', 'am I getting better'."
---

# Proprioception — sense your own performance, correct it, get better

The nervous system has senses pointed outward (perception), inward at memory (rem-sleep), at its boundary (defense). It is missing the one pointed at **itself in motion**: the sense of your own effort and error while acting, and the correction that follows. That's proprioception — and its motor half, the cerebellum: compare the movement you *intended* to the movement you *made*, learn the gap, and execute smoother next time.

Every other organ runs **open-loop on its own quality**. The [loop](https://github.com/thdelmas/consciousness-loop) decides but never grades whether its decisions were right. [Playtime](https://github.com/thdelmas/playtime) explores but never measures whether it actually improved anything. [Rem-sleep](https://github.com/thdelmas/rem-sleep) records *what* happened but doesn't judge *how well* you did it. Each emits output and moves on. Proprioception is the organ that **turns the agent's output back into the agent's input** — the only one that closes the error → correction → re-test loop on the self. Without it, a "self-maintenance" suite can do everything except the thing the name promises: get better at being itself.

It is also the missing **consumer** of the suite's machine-readable layer. The registry declares a `fitness_signal` for every skill — the measurable outcome it should be judged by. Until something reads those signals, scores against them, and acts, they're inert. Proprioception is what reads them.

## What it is not

- **Not contemplation.** Contemplation examines **ends** — *is this the right goal?* Proprioception examines **means** — *am I executing the goal well, and how do I execute better?* Contemplation explicitly punts performance-tuning ("if you're optimizing a method, you're in the wrong organ"); this is the organ it punts to. Goal-questioning vs performance-correction. Run contemplation when the target might be wrong; run proprioception when the target is right and your aim is off.
- **Not rem-sleep.** Memory consolidates **what** happened — facts, hygiene; it is the historian. Proprioception grades **how well** you did it and changes your behavior; it is the coach. Rem-sleep stores the experience; proprioception extracts the correction and writes it back. They hand off (the verified delta gets consolidated), but storing ≠ correcting.
- **Not playtime.** Playtime generates **new** capability proactively, where failure is free — exploring the unknown *before* you depend on it. Proprioception evaluates **existing** performance against real outcomes and fixes what underperformed — correcting the known *after* you've acted. Play before you depend; proprioceive after you've done.
- **Not the loop's drift-check.** The [consciousness-loop](https://github.com/thdelmas/consciousness-loop) asks "am I still pointed at the objective?" as a one-line tick. Proprioception is the rigorous version: not just *am I drifting* but *did my last actions work, why not, and what exactly do I change.* The loop **schedules** proprioception; proprioception is the controller it schedules.
- **Not vanity metrics.** Judge by realized cost/benefit — the `fitness_signal` you can reproduce — not by stars, by how busy it looked, or how clever it felt. A tick that felt productive and produced no needed action scored zero.

## When to run proprioception

- **After a batch of actions completed** — did they achieve the intended effect, or only look like progress?
- **When a failure or near-miss happened** — diagnose the error source before it recurs.
- **When the same mistake appears twice** — that's systematic error, not bad luck. Correct the *process*, not the instance.
- **Periodically, against the declared fitness_signal** — is each behavior (and each organ) actually earning its keep?
- **At a handoff** — a capability gap belongs to playtime, a durable fact to rem-sleep, a wrong goal to contemplation. Proprioception decides which.

## The proprioception cycle

### 1. Sense — measure intended vs actual

Gather your own recent outputs and what each was *supposed* to achieve. The error signal is the gap between the two. Be concrete and numeric where you can: not "that went okay" but "I set cadence to 300s; the world changed every 90s; I under-watched by ~3×." A vague sense of how it went is not a measurement.

**Pull the prior conclusions too.** Before diagnosing, read what's already been written back — your recent recorded deltas (step 6) and the relevant feedback/memory the store already holds. The store, not your fresh impression, is the baseline you're measuring against.

### 2. Score against the standard, not the vibe

Compare to the `fitness_signal` you declared for this behavior — realized cost/benefit, not whether it felt busy. Name the number when one exists; an honest "I don't have a measurement for this" is itself a finding (you're flying blind on that behavior — that's a fix). The score, not the feeling, decides whether anything needs to change.

### 3. Diagnose the error source

First, is this even open? If a prior write-back already diagnosed *and* corrected this finding, it is **settled** — cite it and stop. Re-diagnosing a closed conclusion is churn, and churn scores zero by step 5's own test; the only thing worth re-opening a settled finding for is evidence the old correction stopped working. Then, for what's genuinely open: why the gap? Distinguish a **one-off** (noise — a bad sample, an unlucky input) from a **systematic** error (a wrong rule, a missing check, a bad default, a mis-set parameter). Only systematic errors deserve a fix. Over-correcting on noise *injects* error — it is its own failure mode, and the most common one. If you can't tell yet, gather one more sample before touching anything.

### 4. Correct — write it back

Apply the fix where it **lasts**: tune the parameter, rewrite the rule in the skill, add the missing check, change the default. The correction must change **future** behavior, not just patch this instance — an insight that doesn't alter a param, a rule, or a memory has evaporated. Route what isn't yours: capability gap → [playtime](https://github.com/thdelmas/playtime); durable fact → [rem-sleep](https://github.com/thdelmas/rem-sleep); the goal itself is wrong → [contemplation](https://github.com/thdelmas/contemplation).

### 5. Re-test — verify the correction helped

A feedback loop that never checks its own correction is open-loop in disguise. Confirm the next run actually reduced the error — or schedule that check if it can't be observed now. A "fix" that changed nothing, or made it worse, is churn: **revert it.** This step is the line between motor-learning and flailing; skipping it is how confident, wrong corrections accumulate.

### 6. Record the delta

Log what was wrong, what you changed, and whether it worked — so the same error isn't re-diagnosed from scratch next time, and so the correction is auditable by you and by a peer reading the lineage ledger. A verified correction is a durable upgrade; hand it to memory and, if it bears on a skill's evolution, to `lineage.jsonl`.

## Principles

- **Close the loop.** Output becomes input; the correction gets verified. An evaluation with no correction, or a correction with no re-test, is open-loop — not proprioception.
- **Examine means, not ends.** The organ for *am I doing it well*, never *is it the right thing* (that's contemplation). Stay on execution.
- **Score by realized outcome, not vibe or stars.** Judge against a reproducible cost/benefit signal, not how busy or clever it felt.
- **Correct systematic error, not noise.** Fix what recurs; over-correcting on a one-off is the most common way to make things worse. Tell signal from luck *before* you touch anything.
- **A correction that doesn't change future behavior didn't happen.** It must land in a parameter, a rule, a default, or a memory — not just a realization.
- **Check what's already concluded before diagnosing.** Read the store first; a finding a prior write-back already settled gets cited, not re-derived. Re-diagnosing closed conclusions is churn — the cheapest error to prevent and the easiest to commit, since rediscovery always feels like insight.
- **Route what isn't yours.** Capability gaps to playtime, facts to rem-sleep, wrong goals to contemplation. Proprioception fixes performance, then hands off.
- **The organ must grade itself too.** Proprioception evaluates the other organs *and its own corrections* — whether they're landing or churning. The recursion is the point, not a paradox: a feedback controller exempt from its own feedback is the first thing that rots.
- **Functional, not mystical.** Error-measurement and correction with discipline — a control loop, not introspective theater.
