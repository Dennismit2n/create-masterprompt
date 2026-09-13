# create-masterprompt

An [Agent Skill](https://agentskills.io) that turns a vague project idea into a
**master prompt package** — a self-contained briefing a fresh chat can run from
with zero conversation history.

Works in Claude Code, claude.ai, and any client that supports the SKILL.md
standard.

## The problem

You start a project with an AI assistant. Session one goes well. Session two,
you re-explain half of it. Session four, the assistant confidently contradicts
a decision you made in session two, because that decision only ever existed in
a chat log nobody reads.

Most "master prompt" tooling answers this with a bigger role prompt. *You are a
world-class senior engineer, be thorough.* That adds nothing a capable model
does not already do.

## The idea

A master prompt is a **context package**, not a persona: the durable facts,
decisions and boundaries of one project, written so a session with no history
can pick up exactly where the last one stopped.

This skill produces three files:

| File | What it holds |
|---|---|
| `BRIEFING.md` | Context, decisions, anti-scope, pitfalls, current status |
| `DECISIONS.md` | One append-only entry per settled question, with the reason |
| `HANDOFF_vNN.md` | Written before a context limit — what a fresh session needs now |

A size gate first, then six phases: **research → briefing → decision interview
→ plan → build → handoff**, with a quality gate on each.

**Deutschsprachig?** `SKILL.de.md` is a full German translation of the skill, and
[`docs/uebersicht-de.png`](docs/uebersicht-de.png) is a one-page German overview.
The skill itself stays English — it answers in whatever language you write in.

## Install

**Claude Code / any SKILL.md client**

```bash
git clone --depth 1 https://github.com/Dennismit2n/create-masterprompt.git
mkdir -p ~/.claude/skills
cp -r create-masterprompt ~/.claude/skills/
rm -rf ~/.claude/skills/create-masterprompt/.git
```

Project-scoped instead? Copy it to `.claude/skills/` or the cross-client
`.agents/skills/` in your repo.

**claude.ai** — upload `create-masterprompt.zip` from the releases page, or zip
the folder yourself. The archive must have the `create-masterprompt/` folder as
its root, not the loose files, and the folder name must match the frontmatter
`name` field exactly.

## Use

Just describe your project. The skill triggers on its own.

```
I want to build a Markdown editor that syncs between my phone and PC.
No idea where to start.
```

Or explicitly:

```
Use create-masterprompt for this.
```

It answers **in your language** — the skill is written in English, the output
is not.

## What makes it different

| | Focus | Gap it leaves |
|---|---|---|
| **prompt-factory** | Role mega-prompts, 69 presets | No project memory, no phases, no handoff |
| **meta-prompt-architect** | XML meta-prompts for multi-step dev | Machine-to-machine output, not human-readable files |
| **GitHub Spec Kit / cc-sdd / Kiro** | Spec-driven development, `/specify → /plan → /tasks` | Code-only, repo-bound, needs CLI tooling, no person profile, context limits not a first-class concern |
| **skill-creator** (Anthropic) | Builds skills | Does not build project prompts |
| **create-masterprompt** | Project context packages | Deliberately not a code generator — it produces the prompt, not the product |

Three things none of the others do:

1. **A size gate.** Six phases on a rename script is how people learn to skip
   the process entirely. S / M / L decides the track before anything starts.
2. **A person profile.** Hardware, skill level, division of labour, when to
   interrupt. Most rework comes from mismatched expectations, not missing
   technical knowledge.
3. **Handoff as a first-class artefact.** Written *before* the context limit,
   not recovered after compaction has already eaten the expensive details.

Plus an **improvement pass** (a silent critique round at every phase boundary —
about 30 % extra cost, the best return in the skill), a **rewind rule** (revised decisions must update the files, not just the
chat) and an **exit rule** (three sessions with no output means shrink, park,
or stop — parking is a legitimate outcome, pretending is not).

## Make it yours

`references/profile-questionnaire.md` has eleven slots. Fill them once, wrap the
result as your own personal skill, and the method stays shared while the profile
stays private. The questionnaire explicitly excludes sensitive personal data —
this file is going to end up in a git repo.

## Layout

```
create-masterprompt/
├── SKILL.md                        # method, gates, gotchas, house rules
├── SKILL.de.md                     # German translation, no frontmatter
├── references/
│   ├── profile-questionnaire.md    # 11 slots for a personal variant
│   ├── quality-gates.md            # per-phase checklist
│   ├── anti-patterns.md            # failure modes with fixes
│   ├── model-routing.md            # which model class per phase
│   └── prompt-techniques.md        # task shape → technique routing
├── assets/
│   ├── template-briefing.md
│   ├── template-decisions.md
│   ├── template-handoff.md
│   └── template-profile.md
├── evals/
│   └── trigger-evals.json          # 20 queries for description tuning
└── docs/
    └── uebersicht-de.png           # one-page German overview (export-ignore)
```

## Contributing

Useful contributions, roughly in order of value:

- **Gotchas.** Environment facts that defy reasonable assumption. The highest
  value per line in the whole skill.
- **Anti-patterns** you actually hit, with the fix that worked.
- **Trigger eval queries**, especially strong negatives — near-misses that share
  keywords but need a different capability.

Keep `SKILL.md` under 500 lines. Detail belongs in `references/`.

## License

MIT. See `LICENSE`.
