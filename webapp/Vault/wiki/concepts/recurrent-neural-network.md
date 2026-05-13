---
type: concept
aliases: [Recurrent Neural Network]
summary: A class of artificial neural networks designed for sequence modeling, which uses internal state (memory) to process variable-length sequences of inputs through recurrent connections.
relationships:
  - target: vanishing-and-exploding-gradient-problem
    type: is-affected-by
tags: [sequence-modeling, neural-networks]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Recurrent Neural Network

## Definition and Structure
A Recurrent Neural Network (RNN) is a type of neural network specialized for processing sequences. Unlike feedforward networks, RNNs have connections that form directed cycles, allowing them to maintain a hidden state that acts as a memory of past inputs. The core idea is to share parameters across different time steps, making the model efficient for variable-length sequences. This parameter sharing relies on the assumption that the conditional probability distribution is stationary, meaning the rules for transitioning from one time step to the next do not change over time.

## How It Works
An RNN processes a sequence one element at a time. At each step `t`, the network takes the input for that step and the hidden state from the previous step, `h^(t-1)`, to compute the new hidden state, `h^(t)`. This new state is then used to produce an output for the current step, `y^(t)`. The same set of weights is used for this computation at every time step. This chain-like structure allows information to persist, enabling the network to model dependencies between elements in the sequence, such as predicting the next word based on the words seen so far.

## Key Challenges
A primary difficulty in training RNNs is the vanishing and exploding gradient problem. Because gradients are propagated backward through time via repeated multiplication of the same weight matrices, they can either shrink exponentially to zero (vanish) or grow exponentially large (explode). This makes it difficult for the model to learn long-term dependencies. The text notes that for an RNN to store memories robustly against small perturbations, it must operate in a parameter region where gradients tend to vanish, creating a fundamental trade-off.

## Relationships

- **is-affected-by**: [[vanishing-and-exploding-gradient-problem|Vanishing And Exploding Gradient Problem]]

---
*Extracted from: Deep+Learning+Ian+Goodfellow*