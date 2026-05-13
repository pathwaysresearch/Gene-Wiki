---
type: concept
aliases: [Lottery (Decision Theory)]
summary: A formal representation of an uncertain choice, defined as a set of possible outcomes, each with an associated probability.
relationships:
  - target: utility-function
    type: evaluated-by
  - target: preference-elicitation
    type: used-in
tags: [decision-theory, uncertainty, probability]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Lottery (Decision Theory)

## Definition
In decision theory, an action with uncertain outcomes is formally represented as a lottery. A lottery L with possible outcomes S_1, ..., S_n that occur with probabilities p_1, ..., p_n is written as L = [p_1, S_1; p_2, S_2; ...; p_n, S_n]. The outcomes S_i can be atomic states of the world or, recursively, other lotteries.

## Role in Utility Theory
Lotteries are a foundational concept for understanding how preferences between complex, uncertain choices are related to preferences between the underlying certain outcomes. Utility theory establishes a set of constraints, or axioms, that any reasonable preference relation between lotteries must obey in order to ensure rational decision-making.

## Axioms of Preference
Rational preferences between lotteries must satisfy several axioms. These include Orderability, which requires that for any two lotteries A and B, an agent must either prefer A to B, prefer B to A, or be indifferent between them (A ≻ B, B ≻ A, or A ~ B). Another key axiom is Transitivity, which states that if an agent prefers lottery A to B and B to C, then they must also prefer A to C.

## Relationships

- **evaluated-by**: [[utility-function|Utility Function]]
- **used-in**: [[preference-elicitation|Preference Elicitation]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*