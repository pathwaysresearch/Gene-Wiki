---
type: concept
aliases: [Exploding Gradients Problem]
summary: A difficulty in training deep neural networks where gradients grow exponentially as they are backpropagated, leading to unstable and large weight updates.
relationships:
  - target: vanishing-gradients-problem
    type: related_to
  - target: glorot-initialization
    type: solved_by
tags: [deep-learning, training-problems, backpropagation]
sourced_from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019
---

# Exploding Gradients Problem

## Definition
The exploding gradients problem is a challenge in training deep neural networks that is related to the vanishing gradients problem. It occurs when gradients get larger and larger as they propagate backward through the network, leading to excessively large updates to the network weights and making the training process unstable.

## Causes and Effects
This problem causes the signal to "explode and saturate" during backpropagation. An analogy is setting a chain of microphone amplifiers too high, where the signal becomes saturated and unintelligible. In a neural network, this instability prevents the model from converging to a good solution as the weight updates are too large and erratic.

## Solutions
Like the vanishing gradients problem, the exploding gradients problem can be significantly mitigated by using proper weight initialization schemes. Techniques such as Glorot and He initialization are designed to maintain a stable variance of the signal as it flows forward and backward through the network, preventing both explosion and vanishing of gradients.

## Relationships

- **related_to**: [[vanishing-gradients-problem|Vanishing Gradients Problem]]
- **solved_by**: [[glorot-initialization|Glorot Initialization]]

---
*Extracted from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019*