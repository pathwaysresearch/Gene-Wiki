---
type: concept
aliases: [Model Parameters]
summary: Configurable variables internal to a machine learning model whose values are learned from the training data.
relationships:
  - target: model-based-learning
    type: is_component_of
tags: [machine-learning, model-component]
sourced_from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019
---

# Model Parameters

## Definition
Model parameters are the internal variables of a model that are learned from the training data. By tweaking these parameters, a model can be adjusted to represent different functions. For example, in a linear model, the parameters θ₀ and θ₁ define the intercept and slope of the line.

## Role in Training
The central task of a learning algorithm is to find the optimal values for the model parameters. This is typically done by minimizing a cost function, which measures the error between the model's predictions and the actual data. The resulting parameter values define the trained model.

## Notation
By convention, the Greek letter θ (theta) is frequently used in machine learning literature to represent model parameters.

## Relationships

- **is_component_of**: [[model-based-learning|Model Based Learning]]

---
*Extracted from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019*