#!/usr/bin/env python3
"""Forecast ledger — proprioception for judgment calls.

Log a probability when you make a claim, resolve it when reality answers,
score your calibration with Brier. Append-only spirit: claims and
probabilities are immutable after opening; resolution only fills fields.

Usage:
  forecast.py open "<falsifiable claim>" <p> <resolve-by YYYY-MM-DD> [source] [notes]
  forecast.py                                # list open forecasts, flag due ones
  forecast.py resolve <id> <true|false> [date]
  forecast.py score                          # Brier over resolved forecasts

Ledger file: $FORECAST_LEDGER, else ./forecasts.jsonl
Keep real ledgers private — forecasts are about people and money more
often than not. See examples/forecasts.jsonl for the shape.
"""
import json
import os
import sys
from datetime import date
from pathlib import Path

LEDGER = Path(os.environ.get("FORECAST_LEDGER", "forecasts.jsonl"))


def load():
    if not LEDGER.exists():
        return []
    return [json.loads(l) for l in LEDGER.read_text().splitlines() if l.strip()]


def save(rows):
    LEDGER.write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in rows))


def main():
    rows = load()
    args = sys.argv[1:]

    if not args or args[0] == "list":
        today = date.today().isoformat()
        open_rows = [r for r in rows if r["resolution"] is None]
        if not open_rows:
            print("No open forecasts.")
        for r in open_rows:
            due = "  ** DUE **" if r["resolve_by"] <= today else ""
            print(f'{r["id"]}  p={r["p"]:.2f}  by {r["resolve_by"]}{due}  {r["claim"]}')
        return

    if args[0] == "open" and len(args) >= 4:
        claim, p, by = args[1], float(args[2]), args[3]
        if not 0.0 < p < 1.0:
            sys.exit("p must be strictly between 0 and 1 — certainty isn't a forecast")
        fid = f"f{len(rows) + 1:03d}"
        rows.append({
            "id": fid,
            "opened": date.today().isoformat(),
            "claim": claim,
            "p": p,
            "resolve_by": by,
            "source": args[4] if len(args) > 4 else "",
            "resolution": None,
            "resolved": None,
            "notes": args[5] if len(args) > 5 else "",
        })
        save(rows)
        print(f"{fid} opened: p={p:.2f} that {claim} (resolve by {by})")
        return

    if args[0] == "resolve" and len(args) >= 3:
        fid, outcome = args[1], args[2].lower() in ("true", "1", "yes")
        when = args[3] if len(args) > 3 else date.today().isoformat()
        for r in rows:
            if r["id"] == fid:
                if r["resolution"] is not None:
                    sys.exit(f"{fid} already resolved — resolutions are final")
                r["resolution"] = outcome
                r["resolved"] = when
                save(rows)
                print(f"{fid} resolved {outcome} on {when} (was p={r['p']:.2f})")
                return
        sys.exit(f"No forecast {fid}")

    if args[0] == "score":
        done = [r for r in rows if r["resolution"] is not None]
        if not done:
            print("Nothing resolved yet.")
            return
        brier = sum((r["p"] - (1.0 if r["resolution"] else 0.0)) ** 2 for r in done) / len(done)
        for r in done:
            print(f'{r["id"]}  p={r["p"]:.2f}  outcome={r["resolution"]}  {r["claim"]}')
        print(f"\nBrier over {len(done)} resolved: {brier:.3f}  (0 = perfect, 0.25 = coin-flip calibration)")
        return

    sys.exit(__doc__)


if __name__ == "__main__":
    main()
