---
type: concept
aliases: [Ground Term]
summary: A term in first-order logic that contains no variables.
relationships:
  - target: universal-instantiation
    type: used-by
  - target: propositionalization
    type: is-relevant-to
tags: [logic, first-order-logic, term]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Ground Term

## Definition
A ground term is formally defined as a term without variables. These terms can be simple constants, like `John` or `Richard`, or they can be complex functional expressions, such as `Father(John)` or `Father(Father(John))`, as long as no variables appear within them.

## Role in Universal Instantiation
Ground terms are central to the inference rule of Universal Instantiation (UI). UI allows for the substitution of any ground term for a universally quantified variable in a sentence. This process generates specific, variable-free instances of a general rule.

## Implications for Inference
The set of possible ground terms can be infinite if the knowledge base includes function symbols (e.g., `Father`). This presents a challenge for inference methods like propositionalization, as it could lead to an infinitely large set of sentences. However, Herbrand's theorem shows that for any entailed sentence, a proof can be found using only a finite subset of these ground term instantiations.

## Relationships

- **used-by**: [[universal-instantiation|Universal Instantiation]]
- **is-relevant-to**: [[propositionalization|Propositionalization]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*