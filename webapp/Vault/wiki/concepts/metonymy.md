---
type: concept
aliases: [Metonymy]
summary: A figure of speech in which a thing or concept is referred to by the name of something closely associated with it, rather than by its own name.
tags: [natural-language-processing, linguistics, semantics]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Metonymy

## Definition
Metonymy is a figure of speech where one object or entity is used to stand in for another that it is associated with. It is a common feature in natural language that requires sophisticated handling in language understanding systems. For example, when a news report says "Chrysler announced...", it is understood that a spokesperson for the Chrysler organization made the announcement, not the abstract organization itself.

## Formal Representation
In a logical framework for language understanding, metonymy can be represented with a predicate, such as `Metonymy(m, x)`, which states that a metonymic object `m` (the one mentioned) is in a metonymy relation with the literal object `x` (the one intended). The relationship can be defined by rules. A simple case is identity, `∀ m, x (m = x) ⇒ Metonymy(m, x)`. A more complex rule for the Chrysler example would be that an organization can stand for its spokesperson: `∀ m, x x ∈ Organizations ∧ Spokesperson(m, x) ⇒ Metonymy(m, x)`.

## Common Examples
The text provides several examples of metonymy beyond an organization standing for its spokesperson. These include an author being used to refer to their works (e.g., "I read Shakespeare"), a producer for their product (e.g., "I drive a Honda"), and a part for the whole (e.g., "The Red Sox need a strong arm"). Some metonymies are more novel and context-dependent, such as "The ham sandwich on Table 4 wants another beer," where the food order stands for the customer who placed it.

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*