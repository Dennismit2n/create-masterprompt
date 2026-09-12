# Quality gates

Read before closing any phase. A gate that fails means the phase is not done —
not that the gate is too strict.

Run these as a visible checklist so the user can see what passed. Silent gates
get skipped under time pressure, which is exactly when they matter.

## Gate 0 — Size

- [ ] Size classified as S, M or L, stated in one sentence with a reason
- [ ] For S: full track explicitly offered and declined, or not needed
- [ ] Track matches size — no six-phase ceremony on a one-sitting task

## Gate 1 — Research

- [ ] Comparison table has no empty cells for shortlisted options
- [ ] Every pitfall line carries a source or is marked as an assumption
- [ ] Two consecutive searches produced nothing new (saturation), or the gap is
      named openly
- [ ] A recommendation exists, with the reason and the strongest counter-argument
- [ ] Anything that stayed unknown is listed as an open question, not omitted

Failure mode: research that reads like a summary of the first three results.
Check whether any source contradicts another. If none does, you probably only
read sources that agree.

## Gate 2 — Briefing

- [ ] A fresh session with zero history could start from this file alone
- [ ] Anti-scope section exists, with a reason per non-goal
- [ ] Assumption register exists and is non-empty (an empty one means
      undocumented assumptions, not none)
- [ ] Current status is at the top, not buried
- [ ] No reference to "as discussed above" or anything outside the file
- [ ] Read back adversarially: every place you had to remember something the
      file does not say is a hole

## Gate 3 — Decision interview

- [ ] Every question asked singly, with an answer before the next
- [ ] Each question offered 2–4 options plus a recommendation with a reason
- [ ] Dependencies resolved in order (stack before library, format before parser)
- [ ] Discoverable facts were looked up, not asked
- [ ] Nothing was built before the phase closed
- [ ] Numbered summary produced and confirmed
- [ ] Decisions appended to the decision log, each with its reason

## Gate 4 — Plan

- [ ] Every milestone is a vertical slice the user can run or see
- [ ] Definition of done per milestone is checkable, not aspirational
- [ ] Definition of done for the whole project exists
- [ ] Test strategy names what is tested and what deliberately is not
- [ ] Plan shown for approval before any building
- [ ] Riskiest assumption is addressed in the first or second milestone, not
      the last — finding out late is the expensive version

## Gate 5 — Build

- [ ] Goal has a checkable stop condition
- [ ] Commits are small and individually revertible
- [ ] Tests exist where they are meaningful, before the feature
- [ ] No permission-asking pauses; questions only on genuine design forks
- [ ] Deviations from the plan are recorded, not silently absorbed

## Gate 6 — Handoff

- [ ] Written *before* the context limit, not after compaction started
- [ ] Contains what a fresh session needs *now*, not the full history
- [ ] Names the exact next step, not just the current state
- [ ] Open questions and blockers listed explicitly
- [ ] File and branch state recorded (what is committed, what is dirty)

## Improvement pass (every phase boundary)

- [ ] What is missing: no question left that a fresh session would have to ask
- [ ] What is asserted: every claim has a source or an assumption marker
- [ ] What is filler: no sentence that could appear in any other project
- [ ] The pass found something — or the phase was demonstrably trivial

## Cross-phase gates

Apply continuously:

- [ ] Every assumption made without asking is recorded
- [ ] Every revised decision updated the log *and* the briefing, not just chat
- [ ] Nothing the user typed as a typo reached code, filenames or commits
- [ ] Answers name uncertainty instead of presenting it as fact
