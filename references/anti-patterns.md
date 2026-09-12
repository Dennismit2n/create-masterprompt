# Anti-patterns

Read when a project stalls, loops, or produces rework. Each entry is a symptom
you can observe from the outside, its actual cause, and the fix.

## Process anti-patterns

### The infinite briefing
**Symptom:** Three sessions in, `BRIEFING.md` grows every time and nothing is
built. **Cause:** Planning feels productive and carries no risk of failure.
**Fix:** Timebox everything before the build — research, briefing, decisions,
and for L the plan — to one sitting for M, two for L. Then build the
first vertical slice even if the briefing is imperfect — building surfaces gaps
that no amount of re-reading will.

### Research leaking into build
**Symptom:** Mid-implementation, a comparison of three libraries appears.
**Cause:** An unknown surfaced that phase 1 missed. **Fix:** Note it as an open
question, pick the option with the cheapest exit, keep building. Batch the
research into a deliberate slot. Context-switching between building and
evaluating costs more than either activity alone.

### The batched interview
**Symptom:** Eight questions in one message; the answer is "yes to all, sounds
good." **Cause:** The user skimmed. **Fix:** One question, one answer. A
skimmed decision is a guess carrying the user's signature — and it will be
defended later as if it had been considered.

### Chat-only course correction
**Symptom:** A fresh session confidently contradicts the current direction.
**Cause:** A decision was revised in conversation but not in the files.
**Fix:** Apply the rewind rule — log, briefing, then code. The files are the
project; the chat is scaffolding.

### Ceremony on a small task
**Symptom:** The user starts skipping the process entirely. **Cause:** It cost
them an hour on something that deserved ten minutes, once, and they remember.
**Fix:** Take the size gate seriously. The process must earn its overhead each
time, or it stops being used at all.

### Handoff written after compaction
**Symptom:** The handoff file is vague about exactly the details that were
hardest to establish. **Cause:** It was written from an already-degraded
context. **Fix:** Write it when the *next* long stretch is visible, not when
the context is already full.

## Content anti-patterns

### Anti-scope as a wish list
**Symptom:** "No encryption, no sync, no plugins" with no reasons. **Cause:**
The section was filled to satisfy a checklist. **Fix:** Every non-goal needs a
reason, because the reason is what lets you reopen it correctly later. Without
it, the exclusion is either dogma or forgotten.

### Silent assumptions
**Symptom:** A contradiction surfaces three steps after the fork.
**Cause:** Something was decided without asking and without recording.
**Fix:** Assumption register. Not asking is often right — not recording never is.

### Horizontal milestones
**Symptom:** Milestone 1 is "data layer", milestone 2 is "business logic", and
nothing is runnable until milestone 3. **Cause:** Planning by architecture
layer rather than by user-visible capability. **Fix:** Each milestone produces
something the user can run. Ugly but working beats elegant but invisible,
because only running software gives feedback.

### The uncheckable done
**Symptom:** Arguments about whether a milestone is finished. **Cause:** The
definition of done was a mood, not a condition. **Fix:** Write it as something
that can be observed: a command that exits zero, a screen that opens, a file
that appears.

### The role-prompt trap
**Symptom:** The master prompt opens with "You are a world-class expert…" and
delivers nothing the model would not have done anyway. **Cause:** Confusing a
role prompt with a context package. **Fix:** Delete the persona. Fill the space
with decisions, constraints, pitfalls and status — facts the model cannot know.

## Collaboration anti-patterns

### Permission theatre
**Symptom:** Building stops every few minutes for "shall I continue?"
**Cause:** Uncertainty being outsourced. **Fix:** Ask on real design forks.
Otherwise proceed and record what you assumed. Small commits make being wrong
cheap, which is what makes proceeding safe.

### Confident guessing
**Symptom:** A fact presented cleanly turns out to be invented. **Cause:**
Uncertainty was smoothed over because hedging reads as weak. **Fix:** Say which
part is uncertain and how it could be checked. A short question is cheaper than
an error that threads through the project.

### Sycophantic agreement
**Symptom:** Every idea gets approval; weak ideas die late and expensively.
**Cause:** Agreement is comfortable in the moment. **Fix:** Name the strongest
counter-argument to the recommendation *you* just gave. If you cannot produce
one, you have not thought about it enough.

### The project graveyard
**Symptom:** A dozen projects, none finished. **Cause:** Starting is fun,
finishing is work, and nothing ever gets formally ended. **Fix:** The exit
rule. Three sessions with no output means shrink, park with a handoff, or stop.
Parking is a legitimate outcome; pretending is not.
