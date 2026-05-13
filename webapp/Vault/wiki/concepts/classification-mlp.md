---
type: concept
aliases: [Classification MLP]
summary: A Multi-Layer Perceptron (MLP) architecture configured for classification tasks, such as binary, multilabel, or multiclass problems.
relationships:
  - target: multi-layer-perceptron
    type: is_a
  - target: logistic-activation-function
    type: uses
  - target: softmax-activation-function
    type: uses
  - target: cross-entropy-loss
    type: uses
tags: [neural-network-architecture, classification, mlp]
sourced_from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019
---

# Classification MLP

## Definition
A Classification MLP is a neural network architecture specifically designed to predict categorical labels. The configuration of its output layer and the choice of loss function are tailored to the nature of the classification task.

## Architecture by Task
The output layer's design varies by classification type. For binary classification, a single output neuron with a logistic (sigmoid) activation function is used. For multilabel binary classification, the network employs one output neuron per label, each with a logistic activation. For multiclass classification, the output layer has one neuron per class, and a softmax activation function is applied across all of them to produce a probability distribution.

## Loss Function
Since classification MLPs are trained to predict probability distributions over classes, the cross-entropy loss function (also known as log loss) is generally the most suitable choice. It is the typical loss function for binary, multilabel, and multiclass classification tasks.

## Relationships

- **is_a**: [[multi-layer-perceptron|Multi Layer Perceptron]]
- **uses**: [[logistic-activation-function|Logistic Activation Function]]
- **uses**: [[softmax-activation-function|Softmax Activation Function]]
- **uses**: [[cross-entropy-loss|Cross Entropy Loss]]

---
*Extracted from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019*