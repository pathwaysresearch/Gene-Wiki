---
type: concept
aliases: [Declarative Bias]
summary: A field in machine learning concerned with how prior knowledge can be explicitly stated and used to constrain the hypothesis space, making learning more efficient and effective.
relationships:
  - target: relevance-based-learning
    type: includes-method
tags: [machine-learning, learning-theory, prior-knowledge]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Declarative Bias

## Definition
Declarative bias is a field of study that aims to understand how prior knowledge can be used to identify the appropriate hypothesis space within which a learning algorithm should search for the correct target definition. By providing this bias, the learner can avoid considering a vast number of irrelevant or incorrect hypotheses, making the learning problem more tractable.

## Role in Learning
The central idea is that by restricting the hypothesis space, learning can be made significantly easier and faster. For example, if a learner has `n` Boolean features, the hypothesis space can be as large as O(2^(2^n)), requiring O(2^n) examples. With prior knowledge in the form of a determination that restricts the relevant features to a subset of size `d`, the number of examples required can be reduced to O(2^d).

## Forms of Prior Knowledge
The text discusses determinations as one form of declarative bias. A determination specifies which attributes are relevant for predicting a goal predicate. The field of declarative bias seeks to understand how various kinds of prior knowledge, beyond just determinations, can be used to guide the learning process, including handling noise, continuous variables, and general first-order theories.

## Relationships

- **includes-method**: [[relevance-based-learning|Relevance Based Learning]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*