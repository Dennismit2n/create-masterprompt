# Changelog

## 1.3.0

- Fixed a regression in `references/model-routing.md`: the three-class model
  (Frontier / Mid / Fast) had silently dropped two cases that route by
  operating condition rather than difficulty — a sustained-throughput model
  for multi-hour unattended runs, and an extended-context variant for
  whole-repository sessions. Both restored as an explicit section, with the
  reason each exists.
- Current model names added inline to the class table. The class stays the
  routing key; the name is now visible without a second lookup.

## 1.2.0

- Added two house rules that were previously personal-skill-only: asking
  rather than guessing on unclear abbreviations, and not lingering with
  follow-up questions once a task is done. Generalised, not specific to any
  one user — the typo-teasing convention from the personal variant stays out.

## 1.1.0

- Added `references/prompt-techniques.md` — task-shape-to-technique routing
  across six techniques (out of eighteen surveyed), plus over-prompting
  warning signs.
- Added an improvement pass at every phase boundary — a silent writer-to-
  reviewer switch, three fixed questions. Anchored as a gate in
  `references/quality-gates.md`.

## 1.0.0

- Initial release: six phases, size gate, anti-scope, assumption register,
  rewind and exit rules, gotchas, model routing.
