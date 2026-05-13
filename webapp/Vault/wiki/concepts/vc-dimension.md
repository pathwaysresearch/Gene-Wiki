---
type: concept
aliases: [Vapnik-Chervonenkis Dimension]
summary: A measure of the capacity of a binary classification model, defined as the maximum number of points that the model can shatter (label in all possible ways).
relationships:
  - target: model-capacity
    type: measures
tags: [statistical-learning-theory, model-capacity, classification]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Vapnik-Chervonenkis Dimension

## Definition
The Vapnik-Chervonenkis (VC) dimension is a well-known measure from statistical learning theory that quantifies the capacity of a binary classifier. It is defined as the largest possible number of points, *m*, for which there exists a training set of *m* different points that the classifier can label in all 2^*m* possible ways. This ability to perfectly classify any labeling of *m* points is called 'shattering' the set of points.

## Role in Statistical Learning Theory
The VC dimension is a cornerstone of statistical learning theory. Key results show that the discrepancy between training error and generalization error is bounded from above by a quantity that grows with the model's capacity (as measured by VC dimension) but shrinks as the number of training examples increases. These bounds provide a theoretical justification for why machine learning algorithms are able to generalize from a finite training set.

## Practical Limitations in Deep Learning
Despite their theoretical importance, bounds based on VC dimension are rarely used in the practice of deep learning. There are two main reasons for this. First, the bounds are often mathematically loose, providing a worst-case guarantee that is not tight enough to be useful for model selection. Second, it is extremely difficult to determine the capacity, and thus the VC dimension, of deep learning algorithms, especially because their effective capacity is also limited by the optimization algorithm used.

## Relationships

- **measures**: [[model-capacity|Model Capacity]]

---
*Extracted from: Deep+Learning+Ian+Goodfellow*