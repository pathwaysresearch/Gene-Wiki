---
type: concept
aliases: [Inverse Resolution]
summary: An approach to Inductive Logic Programming that works by inverting the deductive process of resolution to generate new hypotheses from examples and background knowledge.
relationships:
  - target: inductive-logic-programming
    type: is-a-method-in
tags: [ilp, machine-learning, logical-inference]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Inverse Resolution

## Definition
Inverse resolution is a major approach to Inductive Logic Programming (ILP) that constructs hypotheses by inverting the standard deductive proof process of resolution. The core idea is that if the examples (`Classifications`) logically follow from the background knowledge and a hypothesis, then the process can be reversed to derive the hypothesis from the examples and background knowledge.

## How It Works
The process involves taking a known conclusion (an example) and one of the premises (a piece of background knowledge) and working backward to infer the other premise, which becomes the new hypothesis or an intermediate clause. The text illustrates this with a diagram showing how the fact `Grandparent(George,Anne)` can be used with `Parent(Elizabeth,Anne)` to infer the intermediate clause `¬Parent(Elizabeth,y) ∨ Grandparent(George,y)`, which can then be further used in the inverse proof.

## Related Techniques
A related technique is inverse entailment, which reformulates the learning problem from `Background ∧ Hypothesis ∧ Descriptions ⊨ Classifications` to the logically equivalent `Background ∧ Descriptions ∧ ¬Classifications ⊨ ¬Hypothesis`. This allows a process similar to Prolog's Horn-clause deduction to derive the hypothesis. The PROGOL system uses a form of model checking, rather than full theorem proving, to limit the search in a similar bottom-up fashion.

## Relationships

- **is-a-method-in**: [[inductive-logic-programming|Inductive Logic Programming]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*