---
type: concept
aliases: [Set of Support Strategy]
summary: A resolution strategy that restricts inference by requiring that every resolution step involve at least one clause from a special, designated set, thereby reducing the search space.
relationships:
  - target: resolution-inference-rule
    type: is-a-strategy-for
tags: [resolution, theorem-proving, search-strategy, optimization]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Set of Support Strategy

## Definition
The set of support is a strategy used to make resolution more efficient by eliminating some potential resolution steps altogether. It works by designating a special subset of clauses, the *set of support*, and enforcing the rule that every resolution step must involve at least one clause from this set. Any new clause (resolvent) generated from such a step is then added to the set of support.

## Goal and Effectiveness
The primary purpose of this strategy is to dramatically reduce the search space for a proof. If the initial set of support is small compared to the entire knowledge base, the number of possible resolutions at each step is significantly constrained, making the search more focused and effective.

## Completeness Condition
While powerful, the set of support strategy is not unconditionally complete; a poor choice for the initial set can prevent a proof from being found. However, the strategy is guaranteed to be complete if the set of support S is chosen such that the remainder of the knowledge base (KB - S) is satisfiable. A common and sound practice is to use the negated query as the initial set of support, which relies on the assumption that the original knowledge base is consistent.

## Relationships

- **is-a-strategy-for**: [[resolution-inference-rule|Resolution Inference Rule]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*