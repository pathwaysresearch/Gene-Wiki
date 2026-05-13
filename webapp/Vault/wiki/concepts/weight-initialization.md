---
type: concept
aliases: [Weight Initialization]
summary: The process of setting the initial values for the weight parameters in a neural network before training begins, which is crucial for effective optimization and generalization.
tags: [model-training, hyperparameters, neural-networks]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Weight Initialization

## Motivation
Weight initialization is motivated by the need to break symmetry between different units in a neural network. If all units start with the same parameters, they will compute the same function and follow the same update trajectory, making them redundant. Random initialization from a high-entropy distribution, such as a Gaussian or uniform distribution, is a computationally cheap and effective way to ensure units learn different functions.

## The Role of Scale
The scale of the initial weight distribution is a critical hyperparameter that has a large effect on both optimization and generalization. Larger initial weights produce a stronger symmetry-breaking effect. However, improper scaling can lead to the vanishing and exploding gradients problem, where gradients become too small or too large as they propagate through the network. Modern initialization schemes are designed to preserve the norm of signals during forward and back-propagation, though the theoretically optimal values may not always yield the best performance in practice.

## Initialization of Other Parameters
Besides weights, other parameters also require initialization. Biases are typically set to heuristically chosen constants. For units that act as gates, such as the forget gate in an LSTM, the bias is often initialized to a value like 1 to ensure the gate is open at the start of training. Variance or precision parameters in probabilistic models are often initialized to 1 or to the marginal variance of the output in the training set.

---
*Extracted from: Deep+Learning+Ian+Goodfellow*