#!/usr/bin/env python3
"""Organ pulse — proprioception for the body's own activity.

An organ that leaves no trace is indistinguishable from one that never ran. This
script keeps the trace: one append-only row per detected organ firing, plus a
`pulse` report (counts, last firing, time since) per organ.

Three ways a row gets written:

  1. Hook (Claude Code): wire this script to PostToolUse (matcher Skill|Bash|Read)
     and SessionStart; it reads the hook JSON on stdin and records skill calls,
     organ-script runs, organ-doc reads, and the wake injection.
  2. Marker (any host): an organ that runs in prose, with no tool trace, records
     itself:   organ-fired.py --mark <organ> "<one-line why>"
  3. Backfill: a host that kept transcripts can reconstruct rows; tag them so a
     reader can tell observed from reconstructed (see detail column).

Row:   ts_utc  session_id  organ  kind  detail        (TSV, append-only)
Kinds: skill (Skill/slash call) · script (organ script via shell) · read (organ's
       SKILL.md opened) · injected (wake reflex fired the organ) · wake (session
       start, no organ attributed) · mark (prose marker) — a detail starting with
       'backfill' means reconstructed, not observed.

Ledger file: $ORGAN_LEDGER, else ~/.organ-fired.tsv. Keep it private — session ids
and command fragments are in it.
Env:  ORGAN_WAKE_INJECTS = comma list of organs your SessionStart reflex injects
      (e.g. corpus-callosum) so the wake row is attributed to them.
      ORGAN_EXTRA = comma list of extra organ/skill names to track.
Never blocks a hook: any failure exits 0 silently.

    organ-fired.py                 # hook mode, reads stdin JSON
    organ-fired.py --mark contemplation "frame check before the land decision"
    organ-fired.py pulse [--days 30]
"""
import sys, os, re, json, datetime, collections

LEDGER = os.path.expanduser(os.environ.get('ORGAN_LEDGER', '~/.organ-fired.tsv'))
SUITE = ['consciousness-loop', 'contemplation', 'corpus-callosum', 'exteroception',
         'immune-check', 'open-source-octopus-investigation', 'playtime',
         'proprioception', 'rem-sleep', 'sunset']
ORGANS = SUITE + [o for o in os.environ.get('ORGAN_EXTRA', '').split(',') if o]
SCRIPTS = [  # (regex over the shell command, organ) — an organ's own helper scripts
    (r'(git|clock|mail|cve)-sweep\.sh', 'exteroception'),
    (r'\bforecast\.py\b', 'proprioception'),
    (r'(^|[\s/;&|(])(argus|gitleaks|trufflehog|detect-secrets)\b', 'immune-check'),
    (r'\borgan-fired\.py\b.*--mark', None),  # a marker call is logged by the call itself
]
FMT = '%Y-%m-%dT%H:%M:%SZ'


def now():
    return datetime.datetime.now(datetime.timezone.utc)


def append(session, organ, kind, detail=''):
    os.makedirs(os.path.dirname(LEDGER) or '.', exist_ok=True)
    detail = re.sub(r'\s+', ' ', str(detail)).strip()[:120]
    with open(LEDGER, 'a') as f:
        f.write(f'{now().strftime(FMT)}\t{session}\t{organ}\t{kind}\t{detail}\n')


def hook(d):
    sess = d.get('session_id', '?')
    if d.get('hook_event_name') == 'SessionStart':
        injects = [o for o in os.environ.get('ORGAN_WAKE_INJECTS', '').split(',') if o]
        if injects:
            for o in injects:
                append(sess, o, 'injected', f"cwd={d.get('cwd', '')}")
        else:
            append(sess, '_session', 'wake', f"cwd={d.get('cwd', '')}")
        wake_brief()
        return
    tool, inp = d.get('tool_name'), d.get('tool_input') or {}
    if tool == 'Skill':
        s = inp.get('skill', '')
        if s in ORGANS:
            append(sess, s, 'skill', inp.get('args', ''))
    elif tool == 'Bash':
        # drop heredoc bodies: a command that merely *mentions* an organ script in a
        # document it writes is not a firing (the first live false positive was one)
        cmd = re.sub(r"<<-?\s*'?\"?(\w+)'?\"?.*?^\1\s*$", '', inp.get('command', ''), flags=re.S | re.M)
        for rx, organ in SCRIPTS:
            m = re.search(rx, cmd)
            if m:
                if organ:
                    append(sess, organ, 'script', m.group(0).strip())
                break
    elif tool == 'Read':
        m = re.search(r'/skills/([a-z0-9-]+)/', inp.get('file_path', ''))
        if m and m.group(1) in ORGANS:
            append(sess, m.group(1), 'read', os.path.basename(inp['file_path']))


def rows():
    out = []
    if not os.path.exists(LEDGER):
        return out
    for line in open(LEDGER):
        p = line.rstrip('\n').split('\t')
        if len(p) < 4:
            continue
        try:
            ts = datetime.datetime.strptime(p[0], FMT).replace(tzinfo=datetime.timezone.utc)
        except ValueError:
            continue
        out.append((ts, p[1], p[2], p[3], p[4] if len(p) > 4 else ''))
    return out


def pulse(days=30):
    t = now(); rs = rows()
    by = collections.defaultdict(list)
    for r in rs:
        by[r[2]].append(r)
    names = [o for o in ORGANS if o != '_session'] + sorted(k for k in by if k not in ORGANS and k != '_session')
    print(f"{'organ':34} {'7d':>4} {days:>3}d  last (UTC)        since   kinds({days}d)")
    for o in names:
        v = sorted(by.get(o, []))
        if not v:
            print(f"{o:34} {0:4} {0:4}  never             -       untraced"); continue
        c7 = sum(1 for r in v if (t - r[0]).days < 7)
        cN = [r for r in v if (t - r[0]).days < days]
        kinds = ','.join(f'{k}:{n}' for k, n in collections.Counter(r[3] for r in cN).most_common())
        since = t - v[-1][0]
        s = f'{since.days}d' if since.days else f'{since.seconds // 3600}h'
        print(f"{o:34} {c7:4} {len(cN):4}  {v[-1][0]:%Y-%m-%d %H:%M}  {s:6}  {kinds}")
    print(f"-- organ-pulse: {len(rs)} rows, {len({r[1] for r in rs})} sessions, {LEDGER} --")


def wake_brief():
    """Printed at SessionStart: hook stdout reaches the agent, so this is the reflex
    that makes prose organs record themselves without recall."""
    t = now(); rs = rows(); last = {}
    for r in rs:
        if r[2] in ORGANS and (r[2] not in last or r[0] > last[r[2]][0]):
            last[r[2]] = r
    quiet = [o for o in SUITE if o not in last or (t - last[o][0]).days >= 14]
    print('=== Organ pulse (proprioception) ===')
    print('- ' + ' · '.join(f"{o}:{(t - last[o][0]).days}d" if o in last else f"{o}:never" for o in SUITE))
    if quiet:
        print(f"- quiet >=14d or untraced: {', '.join(quiet)} — untraced ≠ dormant; decide which.")
    print(f'- If you run an organ\'s cycle in prose (no skill call), mark it: '
          f'`{os.path.abspath(__file__)} --mark <organ> "<why>"`. Full table: `... pulse`.')


def main():
    a = sys.argv[1:]
    if a and a[0] == '--mark':
        append(os.environ.get('CLAUDE_SESSION_ID', 'manual'), a[1], 'mark', ' '.join(a[2:])); return
    if a and a[0] == 'pulse':
        days = int(a[a.index('--days') + 1]) if '--days' in a else 30
        pulse(days); return
    if a and a[0] in ('-h', '--help'):
        print(__doc__); return
    hook(json.load(sys.stdin))


if __name__ == '__main__':
    try:
        main()
    except Exception as e:  # never block a hook
        if sys.argv[1:] and sys.argv[1] != '':
            print(f'organ-fired: {e}', file=sys.stderr)
    sys.exit(0)
