---
type: concept
aliases: [Artificial Neural Network]
summary: A computational model composed of interconnected nodes (units) with weighted links, which computes by propagating activations and applying non-linear activation functions.
relationships:
  - target: artificial-neuron
    type: has_component
  - target: warren-mcculloch
    type: developed_by
  - target: walter-pitts
    type: developed_by
  - target: perceptron
    type: is-a-type-of
  - target: activation-function
    type: uses
  - target: back-propagation
    type: is-trained-by
tags: [machine-learning, deep-learning, computational-model]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Artificial Neural Network

## Structure
Artificial neural networks consist of nodes, called units, connected by directed links. Each link propagates an activation from one unit to another and has an associated numeric weight that determines the connection's strength and sign. Each unit also typically has a dummy input with a corresponding weight, which acts as a bias term.

## Unit Computation
A unit `j` in the network first calculates a weighted sum of its inputs, `in_j = Σ w_ij * a_i`. It then applies a non-linear activation function `g` to this sum to produce its output activation, `a_j = g(in_j)`. This process is repeated through the layers of the network.

## Function Representation
By composing layers of units with non-linear activation functions, neural networks can represent highly complex and non-linear functions. The text explains that a network with one hidden layer can combine soft thresholds to create "ridges" and "bumps" in the input space, enabling it to serve as a powerful tool for non-linear regression.

## Relationships

- **is-a-type-of**: [[perceptron|Perceptron]]
- **uses**: [[activation-function|Activation Function]]
- **is-trained-by**: [[back-propagation|Back Propagation]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*

---
*Also referenced in: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019*