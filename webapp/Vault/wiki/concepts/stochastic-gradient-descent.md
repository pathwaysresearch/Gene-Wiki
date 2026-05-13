---
type: concept
aliases: [Stochastic Gradient Descent]
summary: A variant of the Gradient Descent algorithm that updates model parameters based on a single, randomly picked training instance at each step, making it faster but more irregular than Batch Gradient Descent.
relationships:
  - target: kernel-trick
    type: is_contrasted_with
  - target: optimization
    type: is_a_type_of
  - target: batch-gradient-descent
    type: is_an_alternative_to
  - target: ill-conditioning
    type: is_affected_by
  - target: cliffs-and-exploding-gradients
    type: is_affected_by
  - target: gradient-descent
    type: is_variant_of
tags: [optimization-algorithm, iterative-method, online-learning]
sourced_from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019
---

# Stochastic Gradient Descent

## Definition
Stochastic Gradient Descent is an optimization algorithm that modifies the standard Batch Gradient Descent approach. Instead of using the entire training set to compute the gradients at every step, it picks a single instance at random from the training set at each step and computes the gradients based only on that single instance. This makes the algorithm much faster per iteration.

## How It Works
The training process involves iterating through the data for a number of rounds, where each round is called an *epoch*. At each step, a random instance is selected, its gradient is computed, and the model's parameters are updated. Because instances are picked randomly, some may be selected multiple times per epoch while others are not. This randomness makes the parameter updates irregular, as shown by the jagged path the algorithm takes toward the minimum.

## Convergence
While Batch Gradient Descent proceeds smoothly toward the minimum, the path taken by Stochastic Gradient Descent is much more erratic. It will eventually get very close to the minimum but will continue to bounce around, never fully settling. An alternative approach to ensure every instance is processed in an epoch is to shuffle the training set and then go through it instance by instance, which generally converges more slowly.

## Relationships

- **is_variant_of**: [[gradient-descent|Gradient Descent]]

---
*Extracted from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019*

---
*Also referenced in: Deep+Learning+Ian+Goodfellow*