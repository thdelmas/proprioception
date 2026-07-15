# Proprioception — sense your own performance, correct it, get better

The nervous system's missing feedback loop. Every other organ runs **open-loop on its own quality**: the loop decides but never grades its decisions, playtime explores but never measures whether it improved anything, rem-sleep records *what* happened but doesn't judge *how well*. Proprioception **turns the agent's output back into its input** — the only organ that closes the error → correction → re-test loop on the self. Biologically: proprioception + the cerebellum — compare intended motion to actual, learn the delta, execute smoother next time. It's also the missing consumer of the suite's `fitness_signal`s.

## What it is not

- **Not contemplation** — contemplation examines *ends* (is the goal right?); proprioception examines *means* (am I executing it well, how do I do better?). Contemplation punts performance-tuning; this is where it goes.
- **Not rem-sleep** — memory stores *what* happened (historian); proprioception grades *how well* and changes behavior (coach).
- **Not playtime** — playtime builds *new* capability before you need it; proprioception fixes *existing* performance after you've acted.
- **Not the loop's drift-check** — the loop asks "am I drifting?" in one line and schedules this; proprioception is the rigorous controller.
- **Not vanity metrics** — judge by realized cost/benefit, not stars or how busy it felt.

## When to run it

- After a batch of actions — did they achieve the intended effect, or just look like progress?
- After a failure/near-miss — diagnose the error source before it recurs.
- When the same mistake appears twice — systematic, not bad luck; fix the process.
- Periodically against the declared fitness_signal — is each behavior earning its keep?
- At a handoff — capability gap → playtime, fact → rem-sleep, wrong goal → contemplation.

## The proprioception cycle

1. **Sense — intended vs actual.** Gather recent outputs and what each was meant to achieve; the error is the gap. Be numeric: not "okay" but "set 300s, world changed every 90s, under-watched 3×."
2. **Score against the standard, not the vibe.** Compare to the `fitness_signal` (realized cost/benefit). "I have no measurement for this" is itself a finding.
3. **Diagnose the error source.** First check the store: a finding a prior write-back already diagnosed *and* corrected is settled — cite it and stop; re-diagnosing a closed conclusion is churn that scores zero. For what's genuinely open: one-off (noise — leave it) vs systematic (wrong rule/default/check — fix it). Over-correcting on noise injects error; it's the most common failure mode.
4. **Correct — write it back.** Into a param, a rule, a default, a memory — must change *future* behavior, not just patch this instance. Route what isn't yours (playtime / rem-sleep / contemplation).
5. **Re-test — verify the correction helped.** A fix that changed nothing or regressed is churn — revert it. This is the line between motor-learning and flailing.
6. **Record the delta.** What was wrong, what changed, whether it worked — auditable, so it isn't re-diagnosed from scratch.

## The forecast ledger — proprioception for judgment

The cycle grades actions; the ledger grades **predictions**. Log every "probably" that matters at the moment it's made (falsifiable claim + probability + resolve-by date, append-only, immutable once opened); resolve on the date; score with Brier (0 = perfect, 0.25 = coin-flip). Resolved rows show *where* you're miscalibrated — write that back as a rule like any other correction. `scripts/forecast.py` implements open/list/resolve/score over plain JSONL. Keep the real ledger private; `examples/forecasts.jsonl` is the fabricated shape.

## The attention schema — proprioception for allocation

The cycle grades *actions*, the ledger grades *predictions*; neither asks whether the thing deserved your attention at all. A subtask executed flawlessly can still be forty minutes down a rabbit hole — the cycle measures **aim**, not **where you were pointed**, and perfect aim at the wrong target scores well while being a total loss. Design constraint: **you cannot catch capture from inside capture** (an in-the-moment monitor you must remember to invoke is a smoke alarm you have to remember to press), so grade retrospectively and let the product do the work later. Reconstruct where attention actually went (concrete fractions, and count the **crowded-out**, not just the consumed); compare against what deserved it; **name the pull, not the instance** — nearest-rich-object, recency, novelty, the-thing-I'm-good-at, sunk-cost, legible-over-important — since one rabbit hole is noise but a recurring *kind* is the schema; accumulate pulls into a profile (one session = anecdote, twenty = predictor); **read it at decide-time or don't write it** (the loop's decide step, a session start), as pre-emption: *these are my known pulls; is this one of them?* A schema nothing consults is a diary. Fitness: pulls that actually pre-empted a later capture vs. a profile never read or named so generically it pre-empts nothing. This is **AST-1** from Butlin et al. (*"a predictive model representing and enabling control over the current state of attention"*) in its weak, honest form — learned retrospectively, so it controls the *next* decision, not the current one. AST's further claim that the schema generates *reports of subjective awareness* is **not implemented and not claimed**.

## Principles

- **Close the loop** — output becomes input; verify the correction. An unverified correction is open-loop.
- **Grade allocation, not just aim** — perfect execution of the wrong target scores well and is a total loss.
- **Examine means, not ends** — *am I doing it well*, never *is it the right thing* (that's contemplation).
- **Score by realized outcome, not vibe or stars** — a reproducible cost/benefit signal.
- **Correct systematic error, not noise** — fix what recurs; tell signal from luck before touching anything.
- **A correction that doesn't change future behavior didn't happen** — it must land in a param, rule, default, or memory.
- **Route what isn't yours** — capability → playtime, facts → rem-sleep, goals → contemplation.
- **The organ grades itself too** — including whether its own corrections are landing. The recursion is the point.
- **Functional, not mystical** — a control loop, not introspective theater.
