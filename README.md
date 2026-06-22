# Proprioception — a Claude Code skill

The **feedback organ** of the [agent-nervous-system](https://github.com/thdelmas/agent-nervous-system) suite — and the one that closes the loop the others leave open.

Every other organ runs **open-loop on its own quality**: the [loop](https://github.com/thdelmas/consciousness-loop) decides but never grades its decisions, [playtime](https://github.com/thdelmas/playtime) explores but never measures whether it improved anything, [rem-sleep](https://github.com/thdelmas/rem-sleep) records *what* happened but doesn't judge *how well*. Proprioception is the organ that **turns the agent's output back into its input**: observe your own recent performance, score it against the standard you declared, diagnose the error, write the correction back into how you work — then verify the correction actually helped.

Biologically it's the proprioceptive sense and the cerebellum: compare the movement you *intended* to the one you *made*, learn the delta, execute smoother next time. For an agent, it's the difference between a self-maintenance suite that *runs* and one that actually **gets better at being itself**.

It's also the missing **consumer** of the suite's machine-readable layer — the registry declares a `fitness_signal` for every skill; proprioception is what reads those signals, scores against them, and acts.

## What it is not

- **Not contemplation** — contemplation examines *ends* (is the goal right?); proprioception examines *means* (am I executing it well, and how do I do better?). Contemplation punts performance-tuning; this is where it goes.
- **Not rem-sleep** — memory stores *what* happened (the historian); proprioception grades *how well* and changes behavior (the coach).
- **Not playtime** — playtime builds *new* capability before you need it; proprioception fixes *existing* performance after you've acted.
- **Not the loop's one-line drift-check** — the loop schedules proprioception; proprioception is the rigorous controller it schedules.

## Install

Works with **Claude Code**, **Codex**, and **Cursor**.

```bash
git clone https://github.com/thdelmas/proprioception.git
cd proprioception
```

### Claude Code

```bash
mkdir -p ~/.claude/skills/proprioception
cp SKILL.md ~/.claude/skills/proprioception/
```

Invoke with `/proprioception`, or say *"how am I doing?"* / *"retro on that"* / *"did that actually work?"* / *"recalibrate"*.

### Codex

```bash
mkdir -p ~/.agents/skills/proprioception
cp SKILL.md ~/.agents/skills/proprioception/
```

### Cursor

```bash
mkdir -p ~/.cursor/commands
cp cursor/proprioception.md ~/.cursor/commands/
```

## The proprioception cycle

1. **Sense** — measure intended vs actual; the error is the gap. Be numeric.
2. **Score against the standard, not the vibe** — judge by the declared `fitness_signal` (realized cost/benefit), not by how busy it felt.
3. **Diagnose the error source** — one-off (noise, leave it) vs systematic (a wrong rule/default/check, fix it).
4. **Correct — write it back** — into a param, a rule, a default, a memory; it must change *future* behavior. Route what isn't yours.
5. **Re-test — verify the correction helped** — a fix that changed nothing or regressed is churn; revert it.
6. **Record the delta** — what was wrong, what changed, whether it worked — auditable, so it isn't re-diagnosed from scratch.

See [`SKILL.md`](./SKILL.md) for when to run it and the full principles.

## License

MIT
