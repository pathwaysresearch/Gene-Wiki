---
type: concept
aliases: [Entropy (in Information Theory)]
summary: A measure of the uncertainty or impurity in a set of examples, used in decision tree learning to quantify the information content of a random variable, measured in bits.
relationships:
  - target: information-gain
    type: is-a-basis-for
tags: [information-theory, decision-trees, metrics]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Entropy (in Information Theory)

## Definition and Formula
In information theory, the entropy of a random variable V with values v_k, each with probability P(v_k), measures the average level of uncertainty. It is calculated using the formula: H(V) = -Σ_k P(v_k) log₂(P(v_k)). The unit of entropy is bits.

## Example Calculation
For a Boolean random variable that is true with probability q, the entropy is given by B(q) = -(q log₂q + (1-q) log₂(1-q)). A fair coin flip (q=0.5) has an entropy of 1 bit, representing maximum uncertainty. A heavily loaded coin (q=0.99) has a much lower entropy of approximately 0.08 bits, reflecting high predictability.

## Application in Decision Tree Learning
Entropy is used to measure the impurity of a set of training examples. If a training set has p positive and n negative examples, its entropy is B(p/(p+n)). The decision tree learning algorithm uses this measure to calculate information gain, which helps select the best attribute to split the data at each node. The goal is to choose splits that maximally reduce the entropy of the resulting subsets.

## Relationships

- **is-a-basis-for**: [[information-gain|Information Gain]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*