---
type: concept
aliases: [Learning Rate]
summary: A key parameter in online learning systems that controls the speed at which the model adapts to new data. A hyperparameter in iterative optimization algorithms like Gradient Descent that controls the step size at each iteration while moving toward a minimum of a cost function.
relationships:
  - target: online-learning
    type: is_parameter_of
  - target: gradient-descent
    type: is_hyperparameter_for
tags: [machine-learning, hyperparameter, online-learning, optimization, gradient-descent]
sourced_from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019
---

# Learning Rate

## Definition
The learning rate is an important parameter in online learning systems that dictates how fast they should adapt to changing data. It controls the magnitude of the updates to the model's parameters during the learning process.

## Impact of High Learning Rate
Setting a high learning rate causes the system to adapt rapidly to new data. However, a major drawback is that it will also tend to quickly forget the old data. For example, a spam filter with a high learning rate might only recognize the most recent types of spam it has seen.

## Impact of Low Learning Rate
Conversely, a low learning rate gives the system more inertia. This means it will learn more slowly, but it will also be less sensitive to noise in new data or to sequences of nonrepresentative data points, also known as outliers. This can lead to a more stable but less adaptive model.

## Relationships

- **is_parameter_of**: [[online-learning|Online Learning]]
- **is_hyperparameter_for**: [[gradient-descent|Gradient Descent]]

---
*Extracted from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019*