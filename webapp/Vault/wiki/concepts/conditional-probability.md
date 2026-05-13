---
type: concept
aliases: [Conditional Probability]
summary: The probability of an event occurring given that another event, the evidence, has already occurred. It is also known as posterior probability and is fundamental for reasoning under uncertainty.
relationships:
  - target: bayes-rule
    type: is_central_to
  - target: full-joint-probability-distribution
    type: can_be_derived_from
tags: [probability-theory, probabilistic-reasoning, uncertainty]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Conditional Probability

## Definition
Conditional probability, also known as posterior probability, is the probability of a proposition given some evidence that has already been observed. It is written as $P(A \mid B)$, pronounced "the probability of A given B." For example, while the unconditional probability of a dental patient having a cavity might be $P(cavity) = 0.2$, the conditional probability given the evidence of a toothache is much more relevant for diagnosis, such as $P(cavity \mid toothache) = 0.6$.

## Role in Agent Reasoning
When an intelligent agent makes decisions, it must condition on all the evidence it has observed to make the most informed choice. Unconditional probabilities, like the general prevalence of a condition, are still valid but are not as useful as posterior probabilities that incorporate specific, known evidence. For instance, the general probability of rolling doubles is less useful than the probability of rolling doubles given that the first die has already landed on 5.

## Distinction from Logical Implication
It is important to distinguish conditional probability from logical implication. The statement $P(cavity \mid toothache) = 0.6$ does not mean "whenever toothache is true, conclude that cavity is true with probability 0.6." Instead, it means that among all the situations where toothache is true and no other information is available, the proportion of those situations that also include a cavity is 0.6.

## Relationships

- **is_central_to**: [[bayes-rule|Bayes Rule]]
- **can_be_derived_from**: [[full-joint-probability-distribution|Full Joint Probability Distribution]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*