---
type: concept
aliases: [Softmax Activation Function]
summary: An activation function used in the output layer of a multiclass classification neural network to produce a probability distribution over the classes.
relationships:
  - target: classification-mlp
    type: used_in
  - target: activation-function
    type: is_a
tags: [activation-function, classification, neural-networks]
sourced_from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019
---

# Softmax Activation Function

## Definition
The softmax function is an activation function that takes a vector of arbitrary real-valued scores and transforms them into a vector of values that represents a probability distribution. Each component of the output vector is in the range (0, 1), and all the components sum to 1.

## Application in MLPs
In the context of Multi-Layer Perceptrons (MLPs), the softmax activation function is specifically used in the output layer for multiclass classification problems. It is not typically used for binary or multilabel classification.

## Role in Architecture
For a multiclass classification task, the MLP's output layer is designed with one neuron for each class. The softmax function is applied across the outputs of all these neurons. This ensures that the model's final output is a set of probabilities, where each probability corresponds to the model's confidence that the input instance belongs to a particular class.

## Relationships

- **used_in**: [[classification-mlp|Classification Mlp]]
- **is_a**: [[activation-function|Activation Function]]

---
*Extracted from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019*