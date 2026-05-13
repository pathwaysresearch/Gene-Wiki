---
type: entity
aliases: [Jacques Herbrand]
summary: A French mathematician known for a famous 1930 theorem in mathematical logic that is fundamental to automated theorem proving.
relationships:
  - target: propositionalization
    type: provided-foundational-theorem-for
tags: [mathematician, logician, automated-reasoning]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Jacques Herbrand

## Overview
Jacques Herbrand (1930) was a mathematician who made major contributions to mathematical logic that had a profound impact on the development of computational logic.

## Herbrand's Theorem
Herbrand is most famous for a theorem that addresses a key problem in first-order inference. When a knowledge base includes function symbols, the set of possible ground terms becomes infinite, making methods like propositionalization seem intractable. Herbrand's theorem states that if a sentence is entailed by a first-order knowledge base, then there exists a proof involving just a finite subset of the propositionalized knowledge base.

## Significance for AI
This theorem is a cornerstone of automated deduction and inference in artificial intelligence. It guarantees that for any provable statement, a proof can be found in a finite number of steps by incrementally generating and testing ground instances. This makes the propositionalization approach to first-order inference a complete procedure, despite the potential for infinite domains.

## Relationships

- **provided-foundational-theorem-for**: [[propositionalization|Propositionalization]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*