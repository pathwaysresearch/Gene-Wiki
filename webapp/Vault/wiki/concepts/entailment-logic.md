---
type: concept
aliases: [Entailment (Logic)]
summary: The relationship between sentences where one sentence logically follows from another, meaning it is true in all possible worlds where the first sentence is true.
relationships:
  - target: inference-logic
    type: is_goal_of
  - target: propositional-logic
    type: is_a_property_of
tags: [logic, reasoning, semantics]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Entailment (Logic)

## Definition
Entailment is a fundamental relationship between sentences in logic. A sentence α entails another sentence β if β is true in all possible worlds, or models, where α is true. This relationship is crucial for understanding logical reasoning, as it formalizes the idea that one statement is a necessary consequence of another.

## Equivalent Formulations
The text provides several equivalent ways to define entailment. The statement that α entails β is equivalent to asserting that the sentence (α ⇒ β) is valid (true in all models). It is also equivalent to asserting that the sentence (α ∧ ¬β) is unsatisfiable (false in all models).

## Role in Reasoning
Entailment is the core concept that inference procedures aim to capture. For a knowledge-based agent, the goal of its inference mechanism is to derive sentences that are entailed by its knowledge base. For example, an agent might use an ASK function to determine if its knowledge base entails that a certain location is safe before moving there.

## Relationships

- **is_goal_of**: [[inference-logic|Inference Logic]]
- **is_a_property_of**: [[propositional-logic|Propositional Logic]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*