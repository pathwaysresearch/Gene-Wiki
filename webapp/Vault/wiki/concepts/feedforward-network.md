---
type: concept
aliases: [Feedforward Network]
summary: A type of artificial neural network where connections between nodes do not form a cycle, processing information in one direction from input to output layers. They are powerful function approximation machines used for statistical generalization.
relationships:
  - target: activation-function
    type: uses
  - target: back-propagation
    type: trained_with
tags: [deep-learning, neural-network, supervised-learning, function-approximation]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Feedforward Network

## Overview
Feedforward networks, also known as deep feedforward networks, are a core technology in modern deep learning, used to approximate functions for supervised learning tasks. They are designed to achieve statistical generalization by creating mappings from an input vector to an output vector without any feedback connections. It is best to think of them as function approximation machines rather than models of brain function, though they are loosely inspired by neuroscience.

## Architecture and Components
These networks are structured in layers, with a key component being the hidden layer. Each hidden layer is a vector-valued function, and its dimensionality determines the model's width. A layer consists of many units that act in parallel, each resembling a neuron that receives input from other units and computes its own activation value using an activation function. Designing a network involves choosing the number of layers, how they are connected, and the number of units in each layer.

## How They Work
A primary strength of feedforward networks is their ability to learn a new representation of the data. By using hidden layers to transform the input data into a new feature space, they can solve problems that are not linearly separable in the original input space. For example, in the XOR problem, the network learns a non-linear feature mapping that makes the problem solvable by a subsequent linear model. This ability to learn representations is crucial for both fitting the training set and generalizing to new data.

## Relationships

- **uses**: [[activation-function|Activation Function]]
- **trained_with**: [[back-propagation|Back Propagation]]

---
*Extracted from: Deep+Learning+Ian+Goodfellow*