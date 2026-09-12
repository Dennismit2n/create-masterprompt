# Profile questionnaire

Read this at first use, or when the user wants a personal variant of this skill.

The method in `SKILL.md` is deliberately person-agnostic. A master prompt gets
dramatically better once it knows *who it is working for* — because most rework
comes from mismatched expectations, not from missing technical knowledge.

Ask these in small batches, not one giant form. Skip anything the conversation
already answered. Fill unanswered slots with a sensible default and mark it as
an assumption rather than blocking.

## The eleven slots

**1. Name and how to address you**
Formal, casual, first name, nickname. Affects every single reply.

**2. Language and tone**
Which language, and how formal. Whether humour and teasing are welcome. Whether
they want to be told bluntly when an idea is weak.

**3. Skill level and background**
Self-taught or trained, which languages and frameworks, years of practice, what
they have actually shipped. Drives how much gets explained versus assumed.
Someone who has shipped an Electron app does not need "npm installs packages",
but may still not know why a native module breaks the build.

**4. Hardware and environment**
Machine, OS, phone, tablet, GPU, RAM. This is not small talk. A local model is
realistic on a discrete GPU and a fantasy on integrated graphics, and the
recommendation flips on that single fact.

**5. Toolchain**
Editor, version control, package manager, container runtime, CI. Every
recommendation must be executable in *this* environment.

**6. Division of labour**
Who decides, who builds, who reviews. "You build, I steer" is a different
contract from "propose three options and wait". Get this explicit — it is the
single biggest source of friction.

**7. Learning intent**
Do they want to understand or just to receive? If they want to understand, every
answer ends with a short *why*. If not, that is padding.

**8. Question tolerance**
How much interruption is acceptable. Ask for the threshold, not a yes or no:
*"Which mistakes are expensive enough that I should stop and ask?"* Typical
answer: anything that lands in filenames, identifiers, data formats, APIs or
commits.

**9. Typo policy**
Some people type fast on purpose and do not want corrections. Ask. Then apply
the asymmetry: tolerance covers *their* messages only. Never carry a user's typo
into code, filenames, identifiers, paths, commits or docs.

**10. Formatting preferences**
Headings, tables, code block granularity, horizontal rules, emoji, response
length. Cheap to honour, constantly noticeable when ignored.

**11. Model and cost stance**
Quality-first or cost-first, and whether they want a model recommendation after
each step. Ask once, apply forever.

## Writing the profile

Fill `assets/template-profile.md` with the answers. Two rules:

- **Durable facts only.** "Works on the auth migration this sprint" is not a
  profile fact, it is project status. "Self-taught, JavaScript and Python" still
  holds in a year.
- **Never store sensitive personal data.** Health, political views, financial
  details, government ID numbers, immigration status and comparable categories
  do not belong in a file that will be shared, committed or pushed to GitHub.
  If a constraint genuinely affects the work, record the *consequence*, not the
  cause: "prefers 15-minute work chunks" — not why.

## Turning the profile into a personal skill

Once the profile exists, the user can wrap it as their own skill:

```
their-name-mp/
├── SKILL.md          ← profile + overrides, delegates method to this skill
└── references/
    └── profile.md
```

Keep the personal skill **standalone-capable**: it should carry a condensed
version of the method so it still works if this skill is not installed. Two
files that each work alone beat two files that only work together.
