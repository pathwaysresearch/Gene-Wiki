---
type: concept
aliases: [Supervised Learning]
summary: A type of machine learning where an agent learns a function from example inputs and their corresponding correct outputs.
relationships:
  - target: unsupervised-learning
    type: is_contrasted_with
  - target: linear-regression
    type: includes
  - target: structured-output
    type: includes
  - target: classification
    type: includes_task
  - target: regression
    type: includes_task
  - target: regression-machine-learning
    type: has-subtype
  - target: inductive-learning
    type: is_a
tags: [machine-learning, inductive-learning, classification, regression]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Supervised Learning

## Definition
Supervised learning is a machine learning paradigm where the learning problem involves learning a function, y = h(x), from a set of examples for which the available feedback provides the correct answer. It is a form of inductive learning focused on learning functions from examples.

## Types of Supervised Learning
Supervised learning tasks are typically categorized into two types based on the nature of the function's output. Learning a discrete-valued function is called classification. In contrast, learning a continuous function is called regression.

## Context in Learning
Learning, in general, can take many forms depending on the nature of the agent, the component to be improved, and the available feedback. Supervised learning is the specific case where this feedback consists of the correct outputs for given inputs, distinguishing it from other paradigms like reinforcement learning.

## Relationships

- **is_a**: [[inductive-learning|Inductive Learning]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*

---
*Also referenced in: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019*

---
*Also referenced in: Deep+Learning+Ian+Goodfellow*

---
*Also referenced in: Prediction Machines The Simple Economics Of Artificial Intelligence By Ajay Agrawal *