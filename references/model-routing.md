# Model routing

Read when the user cares about model choice, cost, or asks for a recommendation
after each step.

## Route by class, not by name

Model names churn. Routing that hard-codes them is stale within months. Route
by **class**, and keep the name mapping in one place where it is cheap to
update. The names below are current as of mid-2026 in Anthropic's lineup and
are the part most likely to be out of date — check the current lineup rather
than trusting this table.

| Class | Currently | What it is for |
|---|---|---|
| **Frontier** | Opus | Judgement under ambiguity, architecture, weighing contradictory evidence, security-relevant decisions, anything where being wrong is expensive |
| **Mid** | Sonnet | Well-specified execution against a clear plan — most implementation, refactors, tests, docs |
| **Fast** | Haiku | Mechanical transformation with a verifiable result — renames, format conversion, boilerplate, extraction |

One constraint has nothing to do with difficulty: the Fast class is the only
one still on a small context window — currently 200K, where Frontier, Mid and
Fable all carry 1M. On a large codebase that ceiling is hit
long before the task gets hard. Sheer scope can therefore rule the Fast class
out; it is never a reason to step up a class.

## When the operating condition overrides the class

Class follows difficulty, with one exception that follows the operating
condition instead. For a **multi-hour unattended run**, take the class above
Frontier (Anthropic: **Fable**). What goes wrong over a long unattended stretch
is drifting off the brief across many steps, not any single step taking too
long — and that class is built to follow instructions precisely across sessions
that run for hours without supervision. It is the more capable choice, not the
faster one.

Throughput, if you need it, is a separate lever: Anthropic previews a **fast
mode** that serves the Frontier class at up to roughly 2.5x the output speed for
a premium price, currently on the Claude API only and with its own rate limit.
It buys speed on the same model. It is not an argument for one class over
another, and as a preview it is the part of this page most likely to be gone.

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
per-directory setting, a session-level default, a per-subagent model field —
set it up once rather than announcing a switch every time. An announcement the
user has to act on is a task disguised as information.

Automation has a brake worth knowing about: a rule that drops to a cheaper
class after a planning stage stays there, however hard the execution turns out
to be. When the work is genuinely demanding, step back up and say so rather
than accepting the automatic downgrade.

Where it cannot be automated, two lines suffice after a finished step: which
class fits the next task and why, plus — if different — which class would be
better if cost were no object. That second line matters: it tells the user what
they are trading away, instead of quietly making the trade for them.

## When routing does not apply

- **Long agentic sequences with many tool calls.** Consistency across the run
  beats per-step optimisation. Pick one class and stay. If the run is
  unattended and spans hours, see the override above.
- **Anything touching security, money, data loss or irreversible actions.**
  Frontier, regardless of how simple the task looks. The cost asymmetry is the
  whole argument.
- **Debugging a failure the Mid class already failed to fix.** Stepping up is
  usually cheaper than a third attempt at the same level.
