---
type: concept
aliases: [Generalization]
summary: The ability of a machine learning model to perform well on new, previously unseen data after being trained on a finite training set.
relationships:
  - target: model-capacity
    type: is_affected_by
  - target: no-free-lunch-theorem
    type: is_related_to
tags: [machine-learning-theory, overfitting, underfitting, evaluation]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Generalization

## Definition
Generalization is the ability of a machine learning model to perform well on new, previously unobserved inputs, not just on the data on which it was trained. This is described as the central challenge in machine learning, as the ultimate goal is to deploy models that are useful in real-world scenarios with novel data.

## Generalization Error
The performance of a model on unseen data is measured by its generalization error, also known as test error. The core problem in machine learning is to make the training error small while also keeping the gap between training error and generalization error small. These two factors correspond to the challenges of underfitting and overfitting, respectively.

## Factors Affecting Generalization
Statistical learning theory shows that the discrepancy between training error and generalization error is influenced by model capacity and the number of training examples. The gap is bounded from above by a quantity that grows as model capacity increases but shrinks as the number of training examples increases. For non-parametric models, more data generally leads to better generalization until the best possible error is achieved.

## Relationships

- **is_affected_by**: [[model-capacity|Model Capacity]]
- **is_related_to**: [[no-free-lunch-theorem|No Free Lunch Theorem]]

---
*Extracted from: Deep+Learning+Ian+Goodfellow*