# Changelog

## 1.7.0

- **Thirteen translations instead of one.** `SKILL.<lang>.md` now exists for
  es, fr, it, nl, pl, pt, tr, ru, hi, zh, ja and ko alongside de — the same
  fourteen languages the workshop's start page speaks. Each was translated
  from the English original by one agent and then checked against it,
  section by section, by a second one that fixed what it found in place;
  every reviewer found something, from a pronoun with the wrong referent
  (es) to a house rule translated into its own opposite (it). An
  independent script then confirmed for every file: fourteen H2 sections in
  order, all twenty inline-code spans byte-identical to the original, the
  same number of bullets, numbered items and table rows per section, no
  frontmatter, LF line endings. `SKILL.md` remains the only file the
  program reads.
- **Overview images in all fourteen languages** under `docs/`, now generated
  from one template instead of two hand-written pages, so the next version
  bump is one command rather than fourteen edits. All say 1.7.0. The
  template sets `<html lang>`, which is what makes Chromium pick the right
  regional glyphs for Chinese versus Japanese.
- README carries a table of all fourteen; the layout tree shows the pattern
  instead of listing thirteen near-identical lines.

## 1.6.1

- Added a status note to the README and to `SKILL.de.md`: this is an early
  release. The text has had repeated consistency and spec-compliance passes,
  but the skill hasn't run on many real, varied projects yet — the size gate,
  the phase sequence and the templates are still short on real mileage. Says
  so plainly and points at issues rather than letting silence imply more
  confidence than is warranted.

## 1.6.0

- Added `docs/uebersicht-en.png`, an English counterpart to the German
  overview. Both are one-page summaries of what the skill produces and how
  the phases run — for someone deciding whether to install it, not for
  someone already using it.
- `docs/uebersicht-de.png` had "Version 1.4.0" baked into it, stale since
  1.5.0. Both images now say 1.6.0; re-rendered from the same Playwright
  script, palette-quantized the same way.
- README and `SKILL.de.md` now point at both images.

## 1.5.1

- The placeholder quoting from 1.4.0 only ever reached `template-decisions.md`.
  The other three templates still carried bare `<angle brackets>` — 60 of them —
  which Markdown renderers swallow as unknown HTML tags. Quoted now. Multi-line
  placeholders were left alone on purpose: a `<` followed by prose with commas
  and full stops is not a valid open tag, so those already rendered as written.
- `SKILL.de.md` used straight ASCII quotes to close all ten quotations where
  German typography wants “. Fixed.
- The file tree in the README had not been updated for `SKILL.de.md` or `docs/`.
- `references/prompt-techniques.md` routed Few-shot to "phases 2, 4 (templates)".
  Phase 4 has no template; phases 3 and 6 do.
- `references/model-routing.md` contradicted itself: ruling the Fast class out
  *is* a step up, so "never a reason to step up a class" could not be right. It
  now says what was meant — scope moves you to Mid, difficulty decides Frontier.

## 1.5.0

- Added `SKILL.de.md`, a complete German translation of the skill, and
  `docs/uebersicht-de.png`, a one-page German overview of what it produces and
  how the phases run. The skill itself stays English — it is the international
  version and it answers in whatever language it is addressed in. The German
  files exist so that someone who reads no English can still judge what this
  thing does before installing it.
- `SKILL.de.md` deliberately carries **no frontmatter**, so no client mistakes it
  for a second skill definition. `SKILL.md` stays the only machine-read file, and
  the German file says so in its first paragraph.
- `docs/` is marked `export-ignore` in `.gitattributes`: the overview image lives
  in the repository but stays out of the release archive, which has no use for
  90 KB an agent never reads.

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
