---
type: concept
aliases: [Description Logics]
summary: A family of knowledge representation formalisms that emphasize the tractability of reasoning, particularly for testing if one category is a subset of another (subsumption).
tags: [knowledge-representation, logic, tractability]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Description Logics

## Emphasis on Tractability

The primary thrust of description logics is to ensure that key inference problems, such as subsumption-testing, can be solved in time that is polynomial in the size of the descriptions. This is a deliberate design choice to provide predictable performance for common reasoning tasks.

## Contrast with First-Order Logic

Unlike standard first-order logic systems where predicting solution time can be impossible and may require user intervention to avoid long-running computations, description logics are designed to avoid such issues by carefully constraining their expressive power. The goal is to provide a framework where a problem instance is solved by describing it and then asking if it is subsumed by a solution category.

## Inherent Trade-offs

This focus on tractability has consequences. It can mean that either very hard problems cannot be stated at all within the logic, or they require exponentially large descriptions to be represented, highlighting a trade-off between expressive power and computational efficiency.

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*