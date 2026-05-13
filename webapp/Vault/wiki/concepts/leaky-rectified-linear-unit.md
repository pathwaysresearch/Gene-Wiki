---
type: concept
aliases: [Leaky Rectified Linear Unit (Leaky ReLU)]
summary: An activation function that is a variant of ReLU, allowing a small, non-zero gradient when the unit is not active to prevent the 'dying ReLU' problem.
tags: [activation-function, deep-learning, neural-networks]
sourced_from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019
---

# Leaky Rectified Linear Unit (Leaky ReLU)

## Definition

The Leaky ReLU function is defined as LeakyReLU_α(z) = max(αz, z). The hyperparameter α defines how much the function “leaks” by setting the slope of the function for negative input values (z < 0). This value is typically set to a small number, such as 0.01.

## How It Works

Unlike the standard ReLU function which outputs zero for any negative input, Leaky ReLU has a small, non-zero, positive slope for negative inputs. This small slope ensures that neurons using this activation function never completely die (i.e., stop outputting non-zero values and gradients). This allows them to go into a 'long coma' but retain a chance to eventually wake up if gradient descent adjusts the weights of preceding layers appropriately.

## Variants and Performance

A 2015 paper found that leaky variants consistently outperformed the strict ReLU activation function, with a larger leak (α = 0.2) performing better than a smaller one (α = 0.01). Other variants include the Randomized Leaky ReLU (RReLU), where α is chosen randomly from a range during training and fixed to an average value during testing, which can act as a regularizer. Another is the Parametric Leaky ReLU (PReLU), where α is a parameter that is learned during training. In general, the performance hierarchy is often considered to be ELU > Leaky ReLU > ReLU, but Leaky ReLU may be preferred when runtime latency is a major concern.

---
*Extracted from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019*