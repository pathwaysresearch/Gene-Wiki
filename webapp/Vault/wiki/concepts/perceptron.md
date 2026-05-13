---
type: concept
aliases: [Perceptron]
summary: A type of neural network unit or a single-layer network of such units that uses a hard threshold activation function, capable of learning only linearly separable functions. An early algorithm for supervised learning of binary classifiers, introduced by Frank Rosenblatt, which forms a basis for artificial neural networks.
relationships:
  - target: artificial-neuron
    type: uses
  - target: artificial-neural-network
    type: is-a-component-of
  - target: activation-function
    type: uses
  - target: frank-rosenblatt
    type: developed_by
tags: [neural-networks, linear-classifier, machine-learning-history, machine-learning, classification-algorithm]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Perceptron

## Definition
A perceptron is a neural network unit that uses a hard threshold (a step function) as its activation function. A network of these units is also called a perceptron network. It represents a linear classifier.

## Learning Capability
Perceptrons can represent linear decision boundaries in the input space. The perceptron learning rule is an algorithm that updates the weights of the perceptron and is guaranteed to converge to a perfect linear separator if the data is linearly separable.

## Limitations
The text highlights a major limitation of perceptrons: their inability to learn functions that are not linearly separable. The classic example given is the XOR (exclusive OR) function, which a single-layer perceptron cannot learn. This limitation was a significant setback in the early history of neural network research.

## Relationships

- **is-a-component-of**: [[artificial-neural-network|Artificial Neural Network]]
- **uses**: [[activation-function|Activation Function]]
- **developed_by**: [[frank-rosenblatt|Frank Rosenblatt]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*

---
*Also referenced in: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019*