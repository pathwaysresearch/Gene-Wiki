---
type: concept
aliases: [Glorot Initialization]
summary: A weight initialization method for neural networks that helps alleviate the vanishing and exploding gradients problems by maintaining signal variance across layers.
relationships:
  - target: vanishing-gradients-problem
    type: is_a_solution_for
  - target: exploding-gradients-problem
    type: is_a_solution_for
tags: [deep-learning, weight-initialization, neural-networks]
sourced_from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019
---

# Glorot Initialization

## Overview
Proposed by Xavier Glorot and Yoshua Bengio, Glorot initialization (also known as Xavier initialization) is a technique to set the initial random weights of a neural network's layers in a way that significantly alleviates the vanishing and exploding gradients problems.

## How It Works
The core principle is to ensure that the signal flows properly in both the forward direction for making predictions and the reverse direction for backpropagating gradients. To achieve this, the method aims to make the variance of the outputs of each layer equal to the variance of its inputs. It also aims for the gradients to have equal variance before and after flowing through a layer in reverse, preventing the signal from either dying out or exploding.

## Practical Implementation
While guaranteeing both conditions is not possible unless a layer's number of inputs (fan-in) and outputs (fan-out) are equal, Glorot and Bengio proposed a practical compromise that works very well. The connection weights for each layer are initialized randomly from a distribution whose parameters are a function of the layer's fan-in and fan-out.

## Relationships

- **is_a_solution_for**: [[vanishing-gradients-problem|Vanishing Gradients Problem]]
- **is_a_solution_for**: [[exploding-gradients-problem|Exploding Gradients Problem]]

---
*Extracted from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019*