---
type: concept
aliases: [Logistic Activation Function]
summary: A sigmoid (S-shaped) activation function used in the output layer of binary and multilabel classification neural networks.
relationships:
  - target: classification-mlp
    type: used_in
  - target: activation-function
    type: is_a
tags: [activation-function, classification, neural-networks]
sourced_from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019
---

# Logistic Activation Function

## Definition
The logistic activation function, commonly known as the sigmoid function, is a mathematical function that produces an S-shaped curve. It maps any real-valued input into a value between 0 and 1, making it suitable for interpreting outputs as probabilities.

## Application in MLPs
In Multi-Layer Perceptrons (MLPs), the logistic function is the standard activation for the output layer in both binary and multilabel binary classification tasks. For binary classification, a single output neuron with a logistic activation outputs the probability of the positive class. For multilabel tasks, each output neuron uses a logistic activation to independently predict the probability for its corresponding label.

## Historical Context
The text notes that biological neurons seem to implement a roughly sigmoid activation function, which led early ANN researchers to favor it for a long time. However, it also points out that for hidden layers in modern ANNs, other functions like ReLU have been found to generally work better, highlighting a case where the biological analogy was misleading.

## Relationships

- **used_in**: [[classification-mlp|Classification Mlp]]
- **is_a**: [[activation-function|Activation Function]]

---
*Extracted from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019*