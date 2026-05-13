---
type: concept
aliases: [ReLU (Rectified Linear Unit)]
summary: An activation function that outputs the input directly if it is positive, and zero otherwise, which generally works better than sigmoid functions in ANNs.
relationships:
  - target: activation-function
    type: is_a
  - target: regression-mlp
    type: used_in
  - target: wide-and-deep-neural-network
    type: used_in
tags: [activation-function, deep-learning]
sourced_from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019
---

# ReLU (Rectified Linear Unit)

## Definition
The Rectified Linear Unit (ReLU) is a non-linear activation function defined as f(x) = max(0, x). It passes the input value directly if it is positive and outputs zero for any negative input. This simple, computationally efficient operation helps mitigate the vanishing gradient problem.

## Performance Advantage
The text highlights that while early researchers favored sigmoid functions due to their similarity to biological neurons, it has been discovered that ReLU generally works better in Artificial Neural Networks (ANNs). This is presented as an example where following the biological analogy was misleading for engineering effective systems.

## Applications
ReLU is a standard choice for the activation function in the hidden layers of many neural network architectures, including the Wide and Deep network example provided. Additionally, it can be used in the output layer of a regression MLP specifically when the goal is to guarantee that the model's output will always be a positive value.

## Relationships

- **is_a**: [[activation-function|Activation Function]]
- **used_in**: [[regression-mlp|Regression Mlp]]
- **used_in**: [[wide-and-deep-neural-network|Wide And Deep Neural Network]]

---
*Extracted from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019*