---
type: concept
aliases: [Adam Optimization]
summary: An adaptive learning rate optimization algorithm that combines ideas from Momentum optimization and RMSProp, using estimates of both the first and second moments of the gradients.
tags: [optimization-algorithm, adaptive-learning-rate, deep-learning]
sourced_from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019
---

# Adam Optimization

## Overview
Adam, which stands for "Adaptive Moment Estimation," is a method for stochastic optimization proposed by D. Kingma and J. Ba in 2015. The name derives from its use of estimations of the first moment (the mean) and the second moment (the uncentered variance) of the gradients.

## How It Works
The Adam algorithm computes an exponentially decaying average of past gradients (the first moment, `m`) and an exponentially decaying average of past squared gradients (the second moment, `s`). This gives it a close similarity to both Momentum optimization and RMSProp. The algorithm then computes bias-corrected estimates for both moments to counteract their initial bias towards zero at the beginning of training. Finally, the parameter update is performed by moving in the direction of the corrected first moment estimate, scaled by the inverse of the square root of the corrected second moment estimate.

## Algorithm Steps
The core steps of the Adam algorithm at iteration `t` are:
1. Update the decaying average of past gradients: $\mathbf{m} \leftarrow \beta_1 \mathbf{m} - (1 - \beta_1)\nabla_{\boldsymbol{\theta}}J(\boldsymbol{\theta})$
2. Update the decaying average of past squared gradients: $\mathbf{s} \leftarrow \beta_2 \mathbf{s} + (1 - \beta_2)\nabla_{\boldsymbol{\theta}}J(\boldsymbol{\theta}) \otimes \nabla_{\boldsymbol{\theta}}J(\boldsymbol{\theta})$
3. Compute bias-corrected first moment estimate: $\hat{\mathbf{m}} \leftarrow \frac{\mathbf{m}}{1 - \beta_1^t}$
4. Compute bias-corrected second moment estimate: $\hat{\mathbf{s}} \leftarrow \frac{\mathbf{s}}{1 - \beta_2^t}$
5. Update parameters: $\boldsymbol{\theta} \leftarrow \boldsymbol{\theta} + \eta \hat{\mathbf{m}} \oslash \sqrt{\hat{\mathbf{s}} + \boldsymbol{\epsilon}}$

---
*Extracted from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019*