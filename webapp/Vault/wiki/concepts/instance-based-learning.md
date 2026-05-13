---
type: concept
aliases: [Instance-Based Learning]
summary: A machine learning paradigm where the model stores training examples and makes predictions for new instances by comparing them to the stored data, rather than building an explicit general model.
tags: [machine-learning, nonparametric-model, lazy-learning]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Instance-Based Learning

## Definition
Instance-based learning, also called memory-based learning, is a learning method where the hypothesis consists of the entire set of training examples. Instead of creating an abstract model, it makes predictions for new data points by directly referencing these stored instances.

## Nonparametric Nature
This approach is a form of a nonparametric model. This means the model's complexity is not fixed in advance but grows with the number of training examples, as the effective number of parameters (the stored instances) is unbounded.

## Simplest Form and Limitations
The most basic form of instance-based learning is table lookup. In this method, if a new input `x` is found in the stored table of examples, its corresponding output `y` is returned. The text points out a significant weakness: this simple method fails to generalize to new inputs that are not explicitly present in the training data, as it can only return a default value.

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*