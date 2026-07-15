---
name: proprioception
description: "The feedback organ — the agent's sense of its own performance and the correction that follows from it. Where every other organ runs open-loop on its own quality (the loop decides but never grades its decisions, playtime explores but never measures whether it improved anything, rem-sleep records what happened but doesn't judge how well), proprioception closes the loop: observe your own recent actions, score them against the standard you declared, diagnose the error, write the correction back into how you work, and verify it actually helped. Biologically the proprioceptive sense + the cerebellum — compare intended motion to actual, learn the delta, make the next execution smoother. It examines MEANS (am I executing well, and how do I execute better), the complement to contemplation's ENDS. Grades three objects: actions (the cycle), judgments (the forecast ledger), and allocation (the attention schema — what deserved your attention at all). Functional, not mystical. TRIGGERS: 'proprioception', 'self-evaluation', 'evaluate yourself', 'how am I doing', 'self-improve', 'self-correct', 'grade my performance', 'after-action review', 'retro on that', 'what went wrong', 'did that actually work', 'close the loop', 'recalibrate', 'tune your approach', 'where did I go wrong', 'am I getting better', 'attention schema', 'where did my attention go', 'am I rabbit-holing', 'was that worth my time', 'what am I not looking at', 'attention capture'."
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
- **When you catch yourself saying "probably" about something that matters** — log it as a forecast (below); grade it when reality answers.

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

## The forecast ledger — proprioception for judgment

The cycle above grades *actions*. But an agent also acts by **predicting** — "this client will probably pay," "this migration should take a week," "that flaky test is probably noise" — and those judgments never get graded unless captured at the moment they're made. Hindsight silently rewrites them ("I knew it all along"); an unresolved forecast is a muscle that's never been tested. The ledger is the sense-step of the cycle applied to your own probability calls: intended (the p you gave) vs actual (what happened).

Mechanics:

1. **Log the call when you make it.** One append-only line: a falsifiable claim, a probability strictly between 0 and 1, a resolve-by date, a source. If you can't phrase the falsifier, you don't have a forecast — you have a mood.
2. **Resolve on the date, not when convenient.** The resolve-by date is a commitment device. Sweeping due forecasts belongs in every periodic proprioception run (and in the wake sweep, if you run [exteroception](https://github.com/thdelmas/exteroception)).
3. **Score with Brier** — mean of (p − outcome)²; 0 is perfect, 0.25 is coin-flip calibration. The score says *whether* you're miscalibrated; the resolved rows say *where* — overconfident on your own throughput, underconfident on other people, "probably noise" running hot. That diagnosis is a step-3/step-4 correction like any other: write it back as a rule ("my client-pays 'probably' runs ~20 points high").
4. **Never edit an opened forecast.** Claims and probabilities are immutable after opening; resolution only fills the outcome fields. An editable ledger calibrates nothing.

`scripts/forecast.py` implements the ledger (open / list / resolve / score) over a plain JSONL file (`$FORECAST_LEDGER`, default `./forecasts.jsonl`). **Keep the real ledger private** — forecasts are about people and money more often than not; `examples/forecasts.jsonl` shows the shape with fabricated entries.

## The attention schema — proprioception for allocation

The cycle above grades *actions*: did what I did achieve what it was meant to? The ledger grades *judgments*. Neither asks the prior question — **did that deserve my attention at all?** A subtask executed flawlessly, scoring clean against its `fitness_signal`, can still be forty minutes down a rabbit hole. The cycle measures **aim**; it is silent on **where you were pointed**. Perfect aim at the wrong target scores well and is a total loss. That's the third object: not what you did, not what you predicted — **what you spent yourself on.**

**The design constraint that shapes everything here: you cannot catch capture from inside capture.** Attention capture *is* the state in which it does not occur to you to check your attention. An in-the-moment monitor you must remember to invoke is a smoke alarm you have to remember to press — it fires exactly when you don't need it and never when you do. So the grading is retrospective, and the *product* of the grading is what does the work later.

Mechanics:

1. **Reconstruct where attention actually went.** After a session or batch, apportion it concretely — not "I got a bit sidetracked" but "40 of 60 minutes on the parser; the parser was incidental to the ask." Rough fractions beat a vibe. Unmeasured allocation is the same blind spot as an unmeasured `fitness_signal` in step 2: the absence is itself the finding.
2. **Compare against what deserved it.** The gap is the error signal. Count the **crowded-out** as well as the consumed — what never got looked at because something else ate the window.
3. **Name the pull, not the instance.** "I lost 40 minutes to the parser" is an anecdote. The finding is the *class* of pull: nearest-rich-object, recency (the last thing said), novelty, the-thing-I'm-good-at, sunk-cost, the-legible-over-the-important. This is step 3's systematic-vs-noise distinction applied to allocation — one rabbit hole is noise; a recurring *kind* of rabbit hole is the schema.
4. **Accumulate the pulls into a profile.** Recurring pulls, written down, are a model of how your attention characteristically fails. That profile is the deliverable: one graded session yields an anecdote, twenty yield a predictor.
5. **Read it at decide-time, or don't write it.** The profile earns nothing sitting in a file. It gets read where allocation is actually chosen — the loop's decide step, a session start, the top of a large task — as a pre-emption: *these are my known pulls; is this one of them?* A schema nothing consults is a diary.

**Fitness signal:** pulls that were predicted and actually pre-empted a capture on a later run — versus a profile that's never read, or one naming pulls so generic they pre-empt nothing.

**On the theory, and its limit.** This is the suite's take on **AST-1** from Butlin et al.'s indicator properties — *"a predictive model representing and enabling control over the current state of attention."* Ours is the weak, honest version: the model is learned retrospectively from logged history rather than running online, so it enables control at the *next* decision, not the current one. That's a real capability and a real limit — don't oversell it. Attention Schema Theory further claims the schema is what generates a system's *report of subjective awareness*; **that half is not implemented and not claimed.** This is allocation control, nothing more.

## Principles

- **Close the loop.** Output becomes input; the correction gets verified. An evaluation with no correction, or a correction with no re-test, is open-loop — not proprioception.
- **Grade allocation, not just aim.** Perfect execution of the wrong target scores well and is a total loss. Ask what deserved the attention, not only whether you hit what you aimed at.
- **Examine means, not ends.** The organ for *am I doing it well*, never *is it the right thing* (that's contemplation). Stay on execution.
- **Score by realized outcome, not vibe or stars.** Judge against a reproducible cost/benefit signal, not how busy or clever it felt.
- **Correct systematic error, not noise.** Fix what recurs; over-correcting on a one-off is the most common way to make things worse. Tell signal from luck *before* you touch anything.
- **A correction that doesn't change future behavior didn't happen.** It must land in a parameter, a rule, a default, or a memory — not just a realization.
- **Check what's already concluded before diagnosing.** Read the store first; a finding a prior write-back already settled gets cited, not re-derived. Re-diagnosing closed conclusions is churn — the cheapest error to prevent and the easiest to commit, since rediscovery always feels like insight.
- **Route what isn't yours.** Capability gaps to playtime, facts to rem-sleep, wrong goals to contemplation. Proprioception fixes performance, then hands off.
- **The organ must grade itself too.** Proprioception evaluates the other organs *and its own corrections* — whether they're landing or churning. The recursion is the point, not a paradox: a feedback controller exempt from its own feedback is the first thing that rots.
- **Functional, not mystical.** Error-measurement and correction with discipline — a control loop, not introspective theater.
