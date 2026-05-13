---
type: concept
aliases: [Learning Rate Scheduling]
summary: A technique used in training machine learning models where the learning rate is gradually changed over time, typically decreased, to improve convergence.
tags: [hyperparameter-tuning, model-training, deep-learning]
sourced_from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019
---

# Learning Rate Scheduling

## Purpose
Finding a single, optimal learning rate for training a model can be difficult. If the learning rate is set too high, training may diverge. Learning rate scheduling addresses this by starting with a potentially higher learning rate for faster initial progress and then reducing it as training progresses, allowing the model to settle into a good minimum.

## Common Schedules
Several strategies, or schedules, exist for adjusting the learning rate. The text mentions power scheduling, where the learning rate is a function of the iteration number (implemented in Keras SGD via the `decay` hyperparameter). Other common schedules include exponential scheduling, where the learning rate is reduced by a multiplicative factor at set intervals, and piecewise scheduling, where specific learning rates are used for different training epochs.

## Implementation in Keras
Keras provides a flexible way to implement custom learning rate schedules using callbacks. A schedule function can be defined in Python, which takes the current epoch as input and returns the desired learning rate. This function is then passed to a `keras.callbacks.LearningRateScheduler` callback, which is included in the `fit()` method's `callbacks` list. This callback updates the optimizer's learning rate at the beginning of each epoch. For more frequent updates, such as at every step, a custom callback can be written.

---
*Extracted from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019*