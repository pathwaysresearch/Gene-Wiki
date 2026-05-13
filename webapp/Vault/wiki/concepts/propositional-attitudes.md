---
type: concept
aliases: [Propositional Attitudes]
summary: Mental states that an agent can have towards a proposition, such as believing, knowing, or wanting, which pose challenges for standard logical reasoning due to their referential opacity.
tags: [modal-logic, knowledge-representation, philosophy-of-mind]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Propositional Attitudes

## Definition
Propositional attitudes are predicates that describe an agent's mental stance toward a mental object or proposition. The text provides examples such as `Believes`, `Knows`, `Wants`, `Intends`, and `Informs`. These are used to model the mental states of agents, for instance, to assert that an agent knows a particular fact.

## The Challenge of Referential Transparency
A key difficulty with propositional attitudes is that they do not behave like ordinary logical predicates. Standard logic assumes referential transparency, where one can substitute a term with another term that has the same value (i.e., if `a = b`, then `P(a)` is equivalent to `P(b)`). Propositional attitudes violate this principle.

## The Superman Problem
The text illustrates this challenge with a classic example. If we assert `Knows(Lois, CanFly(Superman))` and it is also true that `Superman = Clark`, standard logical inference would conclude `Knows(Lois, CanFly(Clark))`. However, this conclusion is invalid because Lois Lane does not know that Superman's identity is Clark Kent. This demonstrates that reasoning about knowledge and belief requires a more nuanced logical framework than simple substitution.

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*