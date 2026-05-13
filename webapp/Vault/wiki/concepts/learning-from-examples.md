---
type: concept
aliases: [Learning from Examples]
summary: A type of machine learning where an agent learns a function or conditional probability distribution from a set of input-output pairs, aiming to generalize to make accurate predictions on new data.
relationships:
  - target: classification
    type: includes
  - target: regression
    type: includes
tags: [machine-learning, supervised-learning]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Learning from Examples

## Core Idea
Learning from examples involves an agent learning a function, denoted as f, from a set of example pairs (x, f(x)). The ultimate goal is for the learned hypothesis, h, to generalize well, meaning it can correctly predict the value of y for novel, unseen examples of x. In some cases, the function f may be stochastic, and the learning task becomes learning a conditional probability distribution, P(Y|x).

## Types of Learning Problems
The nature of the output variable y determines the type of learning problem. When the output y is one of a finite set of values, the problem is called classification. If there are only two possible values, it is known as binary classification. When the output y is a continuous number, such as a temperature, the problem is referred to as regression.

## Hypothesis Space
The set of all possible functions the learning algorithm can choose from is called the hypothesis space. There is a fundamental tradeoff between the expressiveness of a hypothesis space and the complexity of finding a good hypothesis within it. While a highly expressive space like all Turing machines can represent any computable function, finding the right one is computationally complex and may not be efficient to use for prediction, which is why most work focuses on simpler representations.

## Relationships

- **includes**: [[classification|Classification]]
- **includes**: [[regression|Regression]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*