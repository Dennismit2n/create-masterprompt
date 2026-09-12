# Prompt techniques

Read when a phase is not delivering, when an artefact feels thin, or when the
task shape goes beyond "write me X".

This is **not a catalogue to read through.** The routing table tells you when a
technique applies. The rest is here so you can justify the choice.

## First rule: over-prompting

More technique does not make the output better — past a point it makes it worse.
Every technique costs context, and context is the scarcest resource across a
project. Three symptoms:

- The instruction tells the model something it already does ("think carefully",
  "be precise", "you are an expert")
- Two techniques overlap (chain-of-thought *and* tree-of-thoughts in one prompt)
- The prompt is longer than the expected output without supplying any facts

**Test before adding any technique:** would the model get this wrong without the
instruction? No → leave it out. It is the same test that governs skill writing,
and it cuts more than people expect.

## Routing: task shape → technique

| How you recognise it | Technique | Phase |
|---|---|---|
| Large task that splits into stages, each output feeding the next | **Prompt chaining** | 0–6, this is the method itself |
| Format is hard to describe but easy to show | **Few-shot** | 2, 4 (templates) |
| The result must hold up; being wrong is expensive | **Self-consistency** | 1, 3 |
| Facts are missing before anything can be decided | **Generate-knowledge** | 1 → 2 |
| Several viable paths that constrain each other, backtracking likely | **Tree-of-thoughts** | 3, 4 |
| A first attempt exists and is visibly not good enough | **Reflexion** | every phase boundary |

More than two techniques at once is nearly always over-prompting.

## The six that matter

### Prompt chaining
Split a large task into links, each with its own prompt and a checkable
intermediate result. A mistake in link 2 becomes visible in link 2 rather than
in the final product. That is the entire benefit — not better answers, earlier
visible errors. The six-phase method **is** prompt chaining; the briefing file
is the handover point between links. Cost: none extra.

### Few-shot
Two to five filled-in examples instead of a description of the desired format.
Models match structures more reliably than they implement prose about
structures. "Table with question, option, reason" is ambiguous; one filled row
is not. This is why templates in `assets/` are meant to be copied and filled.
**Trap:** examples sharing one pattern produce uniform output — if variation
matters, make the examples deliberately different. Cost: context.

### Self-consistency
Answer the same question several times independently, then take the majority —
or investigate the disagreement. A single answer does not reveal whether it is
stable; three do. The interesting signal is the spread, not the majority: if
three runs diverge, the question is badly framed or the evidence is thin. Use in
phase 1 on expensive forks only. Cost: 3× time and tokens.

### Generate-knowledge
Produce the relevant facts explicitly first, then decide on that basis, instead
of fusing facts and judgement into one step. Separates "what is true" from "what
follows". Errors in the factual base become visible rather than disappearing
into the conclusion. This is exactly the phase 1 → 2 transition, and why every
pitfall line needs a source. Cost: low.

### Tree-of-thoughts
Pursue several solution paths at once, score each, discard dead ends, jump back
to the fork. When decisions constrain each other, the first choice forecloses
the second — deciding linearly lets ordering determine the outcome. Use in phase
3 when decisions are genuinely interlocked, not for independent questions.
Cost: high. The most expensive of the six.

### Reflexion
After the first attempt, a critique pass against your own output, then a second
attempt that incorporates it. Producing and evaluating are different activities.
The writer cannot see the gap because the missing piece is in their head; a
deliberate switch into the reviewer role finds what was invisible while writing.
Cost: about +30 % per phase, and the best return of the six.

## The improvement pass

At every phase boundary, before showing the result, switch roles. Not as a
formality — three concrete questions:

1. **What is missing?** Not "is it complete", but: which question would a fresh
   session have to ask that this file does not answer?
2. **What is asserted rather than evidenced?** Every claim without a source or
   an assumption marker is a candidate.
3. **What is filler?** Any sentence that could appear in any other project goes.

If the pass finds nothing, it was too lenient — or the phase was trivial. Twice
in a row without a finding means the phase is small enough to skip it.

Run it **silently.** The user sees the revised result, not the critique. The
exception: if the pass surfaces something that touches a decision, that belongs
in front of them.

## The other twelve

Listed for completeness, each with the condition under which it becomes
relevant. None applies to this method by default.

| Technique | When it does matter |
|---|---|
| **Zero-shot** | The normal case. Not a technique, the absence of one |
| **Chain-of-thought** | Only for models without their own reasoning. Redundant on current ones |
| **ReAct** | Alternating reasoning and acting — the default agent loop, no need to request it |
| **Meta-prompting** | Prompts producing prompts. That is this whole skill, not an option inside it |
| **RAG** | Once the product itself retrieves from a corpus |
| **PAL** | Offload arithmetic to code. For numbers in the project, not in the prompt |
| **ART** | Automatic tool-use planning. Already part of agent mode |
| **APE** | Automated prompt optimisation. Covered by `evals/` here |
| **Active-prompt** | Generate examples where the model is least certain. For large eval sets |
| **DSP** | A small model produces hints for a large one. Pipelines, not chats |
| **Multimodal CoT** | Reasoning jointly over image and text. Screenshots, mockups |
| **Graph prompting** | Knowledge as a graph. Research-adjacent, rarely load-bearing in practice |

## Source and boundaries

The full eighteen-technique catalogue comes from the `prompt-generator` skill by
Anselm Hahn (`Anselmoo/universal-creator`, MIT, Python ≥ 3.13, alpha). It ships a
worked `.prompt.md` per technique plus an over-prompting detection script.

```bash
uvx universal-creator menu
```

The descriptions here are independently written and cut down to this method —
deliberately not a reimplementation. The technique names are terms of art from
the literature (chain-of-thought: Wei et al. · ReAct and tree-of-thoughts: Yao
et al. · reflexion: Shinn et al.), not protected material.

If you need the full catalogue, install the original — it runs alongside this
skill without conflict. What you have here is the selection plus routing; what
lives there is completeness plus examples.
