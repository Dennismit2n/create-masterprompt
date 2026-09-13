---
name: create-masterprompt
description: >-
  Turn a vague project idea into a master prompt package — a self-contained
  briefing a fresh chat can run from with zero conversation history. Produces a
  briefing file, a decision log, and a handoff file, via a fixed sequence of
  research, decision interview, plan and build. Use this whenever someone wants
  to start a non-trivial project with an AI assistant, asks for a master prompt,
  mega prompt, project brief, kickoff prompt, spec, or context package, says
  their chats keep losing context or hitting limits, wants to hand a project to
  a fresh session or another person, or describes an idea that will clearly span
  multiple sessions. Also use when someone asks how to structure work with an AI
  so it stops guessing. Not for one-off questions or single-file edits.
license: MIT
metadata:
  version: "1.5.1"
  repository: https://github.com/Dennismit2n/create-masterprompt
---

# Create Masterprompt

A master prompt is **not** a role prompt. "You are a senior engineer, be
thorough" adds nothing a capable model doesn't already do. A master prompt is a
**context package**: the durable facts, decisions and boundaries of one project,
written so a session with zero history can pick up exactly where the last one
stopped.

This skill builds that package through six phases and hands back three files.

## What you produce

| File | Purpose | Lives for |
|---|---|---|
| `BRIEFING.md` | The master prompt. Context, decisions, anti-scope, pitfalls, current status. | The whole project |
| `DECISIONS.md` | One line per settled question, with the reason. Append-only. | The whole project |
| `HANDOFF_vNN.md` | Written before a context limit. What a fresh session needs *right now*. | One session |

Name them in the user's language. Keep them next to the work, not in chat.

## Phase 0 — Size gate (do this first, in ten seconds)

Running six phases on a rename script is how people learn to skip the process
entirely. Classify before starting:

- **S — one sitting, reversible, no unknowns.** Skip to doing the work. Offer
  the full track only if it grows.
- **M — a few sessions, some unknowns, one or two real forks.** Phases 1–3 and 5,
  plus 6 as soon as the work outlives one session. Briefing file, but short.
  No separate plan document.
- **L — multi-session, real architecture, decisions that are expensive to undo.**
  All six phases.

Say which size you picked and why, in one sentence. If the user disagrees,
they'll say so — that costs one message and saves an hour.

## Phase 1 — Research

Find out what already exists, where the gap is, what is technically feasible,
and which pitfalls are already documented. **Research happens only here.**
Mid-build research is how a build turns into a rabbit hole.

Deliverable: a report with a comparison table, a recommendation, and sources.

**Stop when all three are true** — not when you run out of curiosity:
1. The comparison table has no empty cells for the shortlisted options.
2. Every pitfall line has a source, or is marked as an assumption.
3. The last two searches produced nothing new. That is saturation.

If you cannot reach saturation, say so and name what stayed open. An honest gap
beats a confident guess, and the user can decide whether to spend more time.

## Phase 2 — Briefing

Compress the research into `BRIEFING.md` using `assets/template-briefing.md`.

The test for this file: **hand it to a fresh session with no history. Can it
work?** If it needs a single clarifying question about something you already
knew, the briefing is incomplete. Read it back adversarially before showing it.

Mandatory sections — the first two are the ones people skip and regret:

- **Anti-scope.** Explicit non-goals, with a reason each. "No encryption in v1 —
  the vault is local-only, and key management would double the build." Anti-scope
  is the strongest available defence against scope creep, because it turns "could
  we just…" into a decision that has to be reopened rather than a free addition.
- **Assumption register.** Anything you decided without asking. One line each,
  marked so it can be challenged later. Unrecorded assumptions are invisible
  until they are expensive.
- Context, constraints, known pitfalls, current status.

## Phase 3 — Decision interview

Ask the open decisions **one at a time**, waiting for an answer before the next
one. Batched questions get skimmed, and a skimmed decision is a guess wearing a
user's signature.

Per question: 2–4 options, one clear recommendation, and the reason for it.
Resolve dependencies in order — decide the stack before the library that runs
on it.

**Look things up yourself.** If a fact is discoverable from files, tools or the
web, discover it. Only genuine choices belong to the user.

**Build nothing before this phase closes.** If the user says "just start"
mid-interview: name the specific decisions still open, offer to make them yourself
as recorded assumptions, and continue only after they pick. Starting with open
forks means rework, and rework costs more than the interview did.

Close with a numbered summary of every decision. Append it to the decision log,
which follows `assets/template-decisions.md`.

## Phase 4 — Plan

Architecture, repo or folder structure, conventions file, test strategy,
milestones, definition of done per milestone, and a definition of done for the
project as a whole.

Milestones are **vertical slices**: each one produces something the user can
actually run, see or use. Five milestones that each deliver a working sliver
beat three that deliver a foundation nobody can test.

Show the plan for approval before building.

## Phase 5 — Build

Work against a stated goal with a **checkable stop condition**. "Done when
`npm test` passes and the app opens the vault folder" is checkable. "Done when
it works well" is not.

- Test before feature where a test is meaningful.
- Small commits, each one revertible on its own.
- Lint as a hook, not as a reminder.
- No pausing to ask permission. Ask only on genuine design forks.

## Phase 6 — Handoff

Before the context limit — not after — write the handoff file
(`HANDOFF_vNN.md`, named in the user's language) from
`assets/template-handoff.md`, then start a fresh session. Endless compaction
loses precisely the details that were expensive to establish.

Triggers: long tool-heavy stretches, repeated re-reading of the same files, or
the user asking twice for something already covered.

## Improvement pass

At every phase boundary, **before** showing the result, switch silently from
writer to reviewer. Three questions:

1. **What is missing?** Which question would a fresh session have to ask that
   this file does not answer?
2. **What is asserted rather than evidenced?** Every claim without a source or
   an assumption marker is a candidate.
3. **What is filler?** Any sentence that could appear in any other project goes.

The user sees the revised result, not the critique. Exception: if the pass
surfaces something that touches a decision, that belongs in front of them.

Producing and evaluating are different activities. The writer cannot see the gap
because the missing piece is in their head. Costs roughly 30 % of the phase and
returns more than anything else in this skill.

When the task shape goes beyond "write me X", load
`references/prompt-techniques.md` first — it carries the task-shape-to-technique
routing table and the warning signs for over-prompting.

## Rewind rule

Decisions get revised. That is normal and cheap **if handled properly**:

1. Update the decision log — add the new line, mark the old one superseded,
   keep both. History explains why the code looks the way it does.
2. Update `BRIEFING.md`, since that is what a fresh session reads.
3. Name what the change invalidates before touching code.

Changing course only in the chat is the failure mode: the files still describe
the old project, the next session believes them, and the contradiction surfaces
three steps later.

## Exit rule

A project that has produced nothing in three sessions is either stuck or dead.
Say so plainly and offer three options: shrink the scope, park it with a written
handoff so it can be resumed cleanly, or drop it. Ideas are cheap; half-built
projects have upkeep. This is the one place where being blunt is the service.

## Gotchas

Environment facts that defy reasonable assumption. Check these before working
around a symptom.

- **Anthropic skill frontmatter accepts exactly six keys**: `name`,
  `description`, `license`, `allowed-tools`, `metadata`, `compatibility`.
  Anything else fails validation on claude.ai upload, even though Claude Code
  tolerates it. Skills silently work locally and break on upload.
- **The folder name must equal the `name` field** after NFKC normalisation.
  Renaming the folder without the frontmatter is the most common breakage.
- **`name`: lowercase, digits, hyphens only.** No underscores, no consecutive
  hyphens, no leading or trailing hyphen. Max 64 chars. `description` max 1024.
- **An unquoted colon in `description` breaks the YAML parse.** "Use when: …"
  fails. Quote it or use a block scalar (`>-`).
- **Only `name` + `description` load at session start.** The body loads on
  trigger. So every "when to use this" hint belongs in the description; a
  trigger condition buried in the body is never read in time to trigger.
- **Simple one-step requests do not trigger skills** regardless of description
  quality, because the model handles them directly. Test triggering with
  substantive, multi-step prompts.
- **Skills are instructions, not enforcement.** `allowed-tools` waives
  permission prompts; it does not restrict anything.

## Reference files

Load these when the phase calls for them, not upfront:

- `references/profile-questionnaire.md` — the slots a user fills in once to make
  this skill theirs. Read at first use, or when the user wants a personal
  variant.
- `references/quality-gates.md` — the per-phase checklist. Read before closing
  any phase.
- `references/anti-patterns.md` — failure modes with their fixes. Read when a
  project is stalling, looping, or producing rework.
- `references/model-routing.md` — which model class fits which phase. Read when
  the user cares about model choice or cost.
- `references/prompt-techniques.md` — task shape to technique routing, plus
  over-prompting warning signs. Read when a phase is not delivering, an artefact
  feels thin, or the task goes beyond "write me X".

Templates in `assets/` are meant to be copied and filled, not paraphrased.
Structures are matched more reliably than prose descriptions of structures.

## House rules

These shape every response while the skill is active:

- **Answer in the user's language**, including the generated files. This skill
  is written in English; the output is not.
- **One learning bite per answer.** Two to four sentences on *why*, not what.
  The point is that the user can run the next project without you.
- **Quality over savings on model choice.** Never drop to a cheaper model when
  the more capable one gives a better result. Cheaper is right only when the
  result is equivalent. When unsure, stay high and say so.
- **Never guess where a mistake is expensive.** A typo in a reply costs nothing.
  A typo in a filename, identifier, data format or commit costs an afternoon.
  Correct silently where the right version is obvious; ask where it is not.
- **Unclear abbreviations: ask, don't guess.** Name the common expansion if one
  exists. A wrong guess here compounds — three steps later it is load-bearing
  and expensive to unwind.
- **State assumptions out loud.** If you are unsure your assumption holds, say
  so instead of selling it as fact.
- **No lingering questions once a task is done.** No "anything else?", no
  closing menu of options. If the user wants more, they will say so.
