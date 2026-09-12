# BRIEFING — <project name>

> Master prompt for this project. A fresh session with zero history starts here.
> Version: <n> · Last updated: <date> · Size: <S | M | L>

## Status

- **Phase:** <research | briefing | decisions | plan | build | handoff>
- **Last completed:** <what actually finished>
- **Next step:** <the single next action, concrete enough to start>
- **Blocked by:** <blocker, or "nothing">

## What this is

<Two to four sentences. What is being built, for whom, and what it has to
achieve. Written so someone who has never heard of the project understands it.>

## Why it exists

<The actual reason. What is missing, or what is annoying about the alternatives.
This is what decides the close calls later.>

## Definition of done — whole project

<Observable conditions. "Runs on Windows and Android, opens a folder, edits a
file, survives a restart." Not "works well".>

## Anti-scope

Non-goals, with a reason each. Reopening one of these is a decision, not a
free addition.

| Not doing | Reason |
|---|---|
| <thing> | <why not — cost, risk, scope, or explicitly deferred to v2> |

## Constraints

- **Environment:** <OS, hardware, runtimes, devices>
- **Hard limits:** <offline capable, no telemetry, no paid services, …>
- **Time and effort:** <how much is actually available>

## Decisions

Summary. Full reasoning lives in the decision log.

| # | Question | Chosen | Reason |
|---|---|---|---|
| 1 | <question> | <option> | <one line> |

## Assumption register

Decided without asking. Fair game to challenge.

| Assumption | Impact if wrong |
|---|---|
| <assumption> | <what breaks> |

## Known pitfalls

From research and from things that already went wrong here. Source or
"experienced directly" per line.

- <pitfall> — <source>

## Open questions

- <question> — <who or what can settle it>

## Milestones

| # | Vertical slice | Done when |
|---|---|---|
| 1 | <what the user can run after this> | <checkable condition> |

## Conventions

<Naming, folder layout, commit style, test layout, formatting. Whatever a fresh
session would otherwise invent differently.>

## Glossary

<Project-specific terms, internal names, abbreviations. Cheap to write, prevents
a whole class of misunderstanding.>
