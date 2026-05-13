---
type: concept
aliases: [Vanishing Gradients Problem]
summary: A difficulty in training deep neural networks where gradients become extremely small as they are backpropagated, preventing weights in lower layers from being updated effectively.
relationships:
  - target: exploding-gradients-problem
    type: related_to
  - target: glorot-initialization
    type: solved_by
tags: [deep-learning, training-problems, backpropagation]
sourced_from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019
---

# Vanishing Gradients Problem

## Definition
The vanishing gradients problem is a significant challenge that affects deep neural networks, making the lower layers (those closer to the input) very difficult to train. It occurs during backpropagation when the gradients of the loss function with respect to the weights become increasingly small as they are propagated backward from the output layer to the input layer.

## Causes and Effects
This issue arises because the gradient signal can die out as it travels backward through the network's layers. This is often related to the choice of activation functions, such as the logistic function, which saturate at their extremes and have gradients close to zero in those regions. When these small gradients are multiplied across many layers, they effectively "vanish," meaning the weights of the initial layers are not updated significantly, and these layers fail to learn meaningful features.

## Solutions
One significant approach to alleviate this problem is through careful weight initialization. Techniques like Glorot and He initialization were specifically designed to ensure the signal flows properly in both the forward (predictions) and reverse (gradients) directions, preventing it from dying out.

## Relationships

- **related_to**: [[exploding-gradients-problem|Exploding Gradients Problem]]
- **solved_by**: [[glorot-initialization|Glorot Initialization]]

---
*Extracted from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019*