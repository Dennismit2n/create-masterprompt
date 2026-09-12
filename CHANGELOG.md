# Changelog

## 1.4.0

- **The M track was self-contradicting.** It listed phases 1, 3, 5 and then asked
  for a briefing file in the next breath — the briefing is phase 2, the only place
  that defines the template, the anti-scope section and the assumption register.
  It also dropped phase 6 entirely, although M is defined as "a few sessions" and
  the handoff is what makes a second session possible. M now runs phases 1–3 and 5,
  plus 6 once the work outlives one session. `references/anti-patterns.md` carried
  a third version of the same answer and has been brought in line.
- **The handoff template had a German file name** — `template-uebergabe.md` among
  three English siblings. Renamed to `template-handoff.md`. Phase 6 also hard-coded
  the German output name `UEBERGABE_vNN.md` while the README promised
  `HANDOFF_vNN.md`; the artifact table now lists the English names once, and the
  rule "name them in the user's language" underneath does the rest.
- **`assets/template-decisions.md` was never referenced** from anywhere, so no agent
  would ever have loaded it. Phase 3 points at it now. Its placeholders were written
  as `<angle brackets>` and were being swallowed as HTML tags by Markdown renderers;
  they are quoted now.
- **The README promised six phases and then listed seven** by counting the size gate
  as one. The gate is a gate.
- **The install instructions copied `.git` into the skills folder** — 43 files instead
  of 15. Shallow clone plus an explicit removal.
- **`.skill` is not a real extension.** Neither the Agent Skills specification nor
  Anthropic's documentation defines one; claude.ai takes a zip. The release asset and
  the README say `.zip` now, with the requirement that the archive has the skill
  folder as its root.
- `references/model-routing.md` referred to "the class above Frontier" without ever
  naming it in a table; it names Fable directly now.
- `evals/trigger-evals.json` claimed all ten negatives were vocabulary-sharing
  near-misses. Four are plainly out-of-scope one-step tasks, which is deliberate —
  the note says so now.

## 1.3.1

- Both special cases added in 1.3.0 corrected. The rules were right, the
  reasons were not.
  - The multi-hour unattended run was justified with throughput — "built for
    sustained throughput", "the Frontier class is too slow to hold the
    distance". That is backwards. The class above Frontier is the more capable
    choice, not the faster one, and what fails over a long unattended run is
    drifting off the brief across many steps, not the duration of any single
    step. Rewritten around instruction-following over the distance.
  - The extended-context case is gone entirely. It assumed a separate Mid-class
    variant with a larger window; Frontier, Mid and the class above Frontier
    now all carry 1M by default, so there is nothing left to route to. What
    survives is the inverse: the Fast class is the only one still on a small
    window, which makes sheer scope an exclusion criterion for that class, not
    a case of its own. Moved under the class table, where a constraint on a
    class belongs.
- With one case left, a section of its own was more structure than the content
  needed. The override is now prose after the class table.
- Added a note on fast mode as a throughput lever, deliberately separate from
  the class question — speed on the same model is not a routing argument.

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
