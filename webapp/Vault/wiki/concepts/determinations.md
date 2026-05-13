---
type: concept
aliases: [Determinations]
summary: A form of logical prior knowledge, expressed as P ≻ Q, stating that the truth value of predicate Q is determined by the truth values of the predicates in P.
relationships:
  - target: relevance-based-learning
    type: used-by
tags: [prior-knowledge, logic, relevance]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Determinations

## Definition
A determination, denoted as P ≻ Q, is a statement of prior knowledge asserting that if any two examples match on the set of predicates P, they must also match on the goal predicate Q. It provides a way to formally state which attributes are relevant for predicting a target, effectively functioning as a relevance statement.

## Role in Learning
Determinations are used in relevance-based learning to reduce the size of the hypothesis space. By identifying a determination where P is a small subset of all available attributes, a learner can focus its search on hypotheses constructed only from the predicates in P. This can lead to a dramatic reduction in the number of examples required for learning, from O(2^n) to O(2^d) if P contains d predicates and there are n total attributes.

## Learning Determinations
Since prior knowledge itself often needs to be learned, the text describes an algorithm for learning determinations from data. The algorithm attempts to find the simplest determination that is consistent with a set of examples. A determination is considered consistent if every pair of examples that matches on the left-hand side predicates also matches on the right-hand side (goal) predicate.

## Relationships

- **used-by**: [[relevance-based-learning|Relevance Based Learning]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*