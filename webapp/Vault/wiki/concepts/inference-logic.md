---
type: concept
aliases: [Inference (Logic)]
summary: The process of deriving new sentences from a set of existing sentences in a knowledge base, which can be evaluated for soundness and completeness.
relationships:
  - target: knowledge-based-agent
    type: is_a_component_of
  - target: entailment-logic
    type: implements
tags: [logic, reasoning, algorithms]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Inference (Logic)

## Definition
Inference is the process of deriving new sentences from a collection of old ones. For a knowledge-based agent, this is the mechanism it uses to generate new knowledge from what it has already stored in its knowledge base.

## Key Properties
Inference algorithms are characterized by two critical properties: soundness and completeness. A sound inference algorithm derives only sentences that are logically entailed by the original knowledge base, ensuring it does not generate false conclusions. A complete algorithm is one that can derive every sentence that is entailed, ensuring it can find all true conclusions.

## Historical Context
The idea of reducing logical inference to a purely mechanical process was envisioned by Wilhelm Leibniz. The first mechanical devices to perform logical inferences were built by Earl Stanhope in the late 18th century and William Stanley Jevons in 1869 with his "logical piano."

## Relationships

- **is_a_component_of**: [[knowledge-based-agent|Knowledge Based Agent]]
- **implements**: [[entailment-logic|Entailment Logic]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*