---
type: concept
aliases: [Truth Maintenance Systems]
summary: Systems designed to manage the dependencies and justifications for beliefs in a knowledge base, enabling consistent belief revision and the generation of explanations.
tags: [knowledge-representation, belief-revision, reasoning]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Truth Maintenance Systems

## Core Purpose

Truth maintenance systems (TMSs) are designed to handle the complications that arise when a belief is retracted from a knowledge base. If other beliefs were inferred from the retracted one, a TMS helps manage these dependencies to maintain a consistent state, especially when a derived belief might have other, independent justifications.

## Explanation Generation

TMSs provide a mechanism for generating explanations for a given sentence. An explanation consists of a set of sentences that logically entails the target sentence. These explanations can include assumptions—propositions not known to be true but that, if true, would suffice to prove the conclusion, such as assuming a car's battery is dead to explain why it won't start.

## Computational Complexity

The underlying problem of truth maintenance is computationally intensive. Its complexity is at least as great as that of propositional inference, making it an NP-hard problem.

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*