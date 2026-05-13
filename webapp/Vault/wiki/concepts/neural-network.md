---
type: concept
aliases: [Neural Network]
summary: A computational model inspired by the structure of biological brains, consisting of interconnected nodes (neurons) that process and transmit signals.
relationships:
  - target: perceptron
    type: is_a_type_of
tags: [machine-learning, deep-learning, computational-model]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Neural Network

## Overview
Neural networks are a class of machine learning models inspired by neuroscience. They are composed of a network of simple processing units called `neurons`, which are organized in layers. Each connection between neurons has an associated weight, which is adjusted during the learning process. These models are highly effective at finding complex patterns in data.

## Architectures
The text discusses several fundamental architectures. The simplest is the `perceptron`, a single-layer neural network that can only learn linearly separable patterns. More powerful are `multilayer` networks, which contain one or more hidden layers of neurons between the input and output layers. These networks are capable of learning complex, non-linear relationships. The most common structure is the `feed-forward` network, where information flows in one direction from the input layer, through the hidden layers, to the output layer, without any cycles.

## Learning Process
Learning in a neural network involves an iterative process of adjusting the connection weights to minimize the error between the network's predicted output and the actual target values in the training data. The most common algorithm for training multilayer networks is back-propagation, which calculates the gradient of the error with respect to the weights and updates the weights to move in the direction that reduces the error.

## Relationships

- **is_a_type_of**: [[perceptron|Perceptron]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*