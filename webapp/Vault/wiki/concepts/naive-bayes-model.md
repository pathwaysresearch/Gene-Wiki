---
type: concept
aliases: [Naive Bayes Model]
summary: A probabilistic classifier based on the simplifying assumption that effect variables are conditionally independent given a single cause.
relationships:
  - target: conditional-independence
    type: assumes
  - target: bayesian-networks
    type: is-a-special-case-of
tags: [probabilistic-model, classifier, machine-learning]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Naive Bayes Model

## Definition

A Naive Bayes model is a probability distribution where a single cause variable directly influences a number of effect variables, all of which are assumed to be conditionally independent given the cause. The full joint distribution is expressed as P(Cause, Effect_1, ..., Effect_n) = P(Cause) * Π_i P(Effect_i | Cause). This model is often used as a classifier, sometimes referred to as a Bayesian classifier or, more critically, the "idiot Bayes model."

## The "Naive" Assumption

The model is termed "naive" because it operates on the simplifying assumption that the effect variables are conditionally independent of each other, given the cause. This assumption is often not true in real-world scenarios, where effects may have complex interdependencies. However, this simplification makes the model computationally tractable and efficient.

## Practical Performance

Despite the often-violated independence assumption, Naive Bayes systems can perform surprisingly well in practice. Their effectiveness even in domains where the assumptions are clearly false has been a subject of study. The text notes that methods exist for learning Naive Bayes distributions directly from observations.

## Relationships

- **assumes**: [[conditional-independence|Conditional Independence]]
- **is-a-special-case-of**: [[bayesian-networks|Bayesian Networks]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*