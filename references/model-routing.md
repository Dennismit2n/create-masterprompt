# Model routing

Read when the user cares about model choice, cost, or asks for a recommendation
after each step.

## Route by class, not by name

Model names churn. Routing that hard-codes them is stale within months. Route
by **class**, and keep the name mapping in one place where it is cheap to update.

| Class | What it is for |
|---|---|
| **Frontier** | Judgement under ambiguity, architecture, weighing contradictory evidence, security-relevant decisions, anything where being wrong is expensive |
| **Mid** | Well-specified execution against a clear plan — most implementation, refactors, tests, docs |
| **Fast** | Mechanical transformation with a verifiable result — renames, format conversion, boilerplate, extraction |

Name mapping, current as of mid-2026 in Anthropic's lineup: Frontier =
Opus-class; Mid = Sonnet-class; Fast = Haiku-class. Check the current lineup
rather than trusting this line — it is the part most likely to be out of date.

## Per phase

| Phase | Class | Why |
|---|---|---|
| 0 — Size gate | any | A one-line judgement |
| 1 — Research | Frontier | Contradictory sources, weak signals, knowing what is missing. The phase where a shallow read costs the most, because everything downstream inherits it |
| 2 — Briefing | Frontier | Compression with judgement. Deciding what may be omitted is harder than writing everything down |
| 3 — Decision interview | Frontier | Dependency order between decisions, and recommendations that have to be defensible |
| 4 — Plan | Frontier | Architecture. The most expensive class of mistake to reverse |
| 5 — Build | Mid, Frontier at forks | With a good plan, implementation is well-specified work. Step up whenever the plan turns out to be underspecified |
| 6 — Handoff | Mid | Structured summarisation against a template |

## The quality-over-savings rule

Never step down when the more capable model gives the better result. Cheaper is
only correct when the result is **equivalent**, not merely acceptable. When
unsure, stay high and say so.

The arithmetic is simple: one round of rework on wrong architecture costs more
than the entire model-cost difference of a project. Optimising the small number
while inflating the large one is not saving.

## Automate rather than announce

Where the environment can switch automatically — model config per phase, a
per-directory setting, a session-level default — set it up once rather than
announcing a switch every time. An announcement the user has to act on is a
task disguised as information.

Where it cannot be automated, two lines suffice after a finished step: which
class fits the next task and why, plus — if different — which class would be
better if cost were no object. That second line matters: it tells the user what
they are trading away, instead of quietly making the trade for them.

## When routing does not apply

- **Long agentic sequences with many tool calls.** Consistency across the run
  beats per-step optimisation. Pick one class and stay.
- **Anything touching security, money, data loss or irreversible actions.**
  Frontier, regardless of how simple the task looks. The cost asymmetry is the
  whole argument.
- **Debugging a failure the Mid class already failed to fix.** Stepping up is
  usually cheaper than a third attempt at the same level.
