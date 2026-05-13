---
type: concept
aliases: [Entailment]
summary: A fundamental relationship in logic where a sentence is a necessary consequence of a knowledge base, meaning it is true in every model where the knowledge base is true.
relationships:
  - target: inference-in-logic
    type: is-the-goal-of
  - target: model-in-logic
    type: is-defined-by
  - target: soundness-of-inference
    type: is-a-precondition-for
tags: [logic, reasoning, knowledge-representation]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Entailment

## Definition
Entailment describes the logical relationship where a sentence α follows from a knowledge base (KB). This means that in every model in which the KB is true, α is also true. The text illustrates this with the analogy of a needle (α) being in a haystack (the set of all consequences of KB).

## Relationship to Models
The formal definition of entailment is based on models. A knowledge base KB entails a sentence α if and only if the set of models in which KB is true is a subset of the set of models in which α is true. An inference procedure can then check this condition to determine entailment.

## Entailment vs. Inference
Entailment is a property of the logic itself, representing what conclusions are logically guaranteed. It is distinct from inference, which is the procedural act of deriving conclusions. Entailment is the state of the needle being in the haystack, while inference is the process of actually finding it. An inference algorithm's goal is to find entailed sentences.

## Relationships

- **is-the-goal-of**: [[inference-in-logic|Inference In Logic]]
- **is-defined-by**: [[model-in-logic|Model In Logic]]
- **is-a-precondition-for**: [[soundness-of-inference|Soundness Of Inference]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*