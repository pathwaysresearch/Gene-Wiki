---
type: concept
aliases: [AdaGrad]
summary: An adaptive learning rate optimization algorithm that scales down the gradient vector along the steepest dimensions to improve convergence in elongated cost functions.
tags: [optimization-algorithm, adaptive-learning-rate]
sourced_from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019
---

# AdaGrad

## Definition
AdaGrad is an optimization algorithm designed to improve the convergence of Gradient Descent, particularly in cases where the cost function has an "elongated bowl" shape. In such scenarios, standard Gradient Descent starts by moving quickly down the steepest slope but then progresses very slowly along the bottom of the valley.

## How It Works
The core idea behind AdaGrad is to correct the update direction to point more directly toward the global optimum. It achieves this by adapting the learning rate on a per-parameter basis. Specifically, the algorithm scales down the gradient vector along the dimensions that are the steepest. This means it reduces the learning rate for parameters associated with large partial derivatives, effectively balancing the update steps and preventing overshooting in steep directions while accelerating progress in flatter directions.

## Algorithm
The AdaGrad algorithm maintains a vector `s` that accumulates the square of the gradients for each parameter over time. The update rule then divides the gradient by the square root of this accumulated value (plus a small smoothing term), which scales the update for each parameter adaptively.

---
*Extracted from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019*

---
*Also referenced in: Deep+Learning+Ian+Goodfellow*