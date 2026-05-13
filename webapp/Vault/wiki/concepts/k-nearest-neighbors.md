---
type: concept
aliases: [k-Nearest Neighbors (k-NN)]
summary: A non-parametric supervised learning algorithm that classifies or predicts a new data point by finding the k-closest training examples and aggregating their outputs.
relationships:
  - target: supervised-learning
    type: is_a_type_of
tags: [supervised-learning, non-parametric-methods, classification, regression]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# k-Nearest Neighbors (k-NN)

## Algorithm Description
k-Nearest Neighbors is a family of non-parametric supervised learning techniques used for both classification and regression. A key characteristic of the k-NN algorithm is that it does not have a distinct training or learning process. Instead, it directly uses the training data at test time to make predictions.

## Prediction Mechanism
When a prediction is needed for a new test input `x`, the algorithm finds the `k` nearest neighbors to `x` within the stored training data. The output is then computed based on these neighbors. For regression, the prediction is typically the average of the corresponding `y` values of the neighbors. For classification, the algorithm can average over one-hot encoded vectors of the neighbors' classes, which can be interpreted as a probability distribution over the possible classes.

## Properties and Use Cases
As a non-parametric learning algorithm, k-NN is not restricted to a fixed number of parameters and can achieve very high capacity. It is considered a useful learning algorithm, alongside decision trees, particularly when computational resources are constrained. It also serves as a useful baseline for building intuition about more sophisticated algorithms.

## Relationships

- **is_a_type_of**: [[supervised-learning|Supervised Learning]]

---
*Extracted from: Deep+Learning+Ian+Goodfellow*