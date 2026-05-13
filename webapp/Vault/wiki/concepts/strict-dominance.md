---
type: concept
aliases: [Strict Dominance]
summary: A principle in multiattribute decision-making where one option is chosen over another because it is better on all relevant attributes.
relationships:
  - target: multiattribute-utility-theory
    type: is-a-principle-in
tags: [decision-making, optimization, multi-criteria]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Strict Dominance

## Definition
Strict dominance is a principle used to simplify multiattribute decision problems. An option A strictly dominates an option B if A is at least as good as B on all attributes and strictly better than B on at least one attribute. For example, if airport site S_1 costs less, generates less noise, and is safer than site S_2, then S_1 strictly dominates S_2.

## Application in Decision-Making
The principle of strict dominance is a powerful tool for pruning the set of possible choices. Any option that is strictly dominated by another can be eliminated from consideration without needing to assess complex trade-offs or construct a full multiattribute utility function. This often helps in narrowing the field of choices to a smaller set of non-dominated, or Pareto optimal, contenders.

## Stochastic Dominance
The concept of dominance can be extended to situations with uncertainty, leading to the idea of stochastic dominance. An option stochastically dominates another on a given attribute if it offers a more favorable probability distribution over the possible values of that attribute. This type of qualitative reasoning can be propagated through qualitative probabilistic networks to make rational decisions even without precise numeric values for probabilities or utilities.

## Relationships

- **is-a-principle-in**: [[multiattribute-utility-theory|Multiattribute Utility Theory]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*