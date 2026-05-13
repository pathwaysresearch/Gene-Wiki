---
type: concept
aliases: [Overfitting]
summary: A modeling error in machine learning that occurs when a model learns the training data too well, including its noise and details, which negatively impacts its performance on new, unseen data. A modeling error that occurs when a machine learning model learns the training data too well, including its noise and random fluctuations, leading to poor performance on new, unseen data.
relationships:
  - target: regularization
    type: is-prevented-by
  - target: generalization-error
    type: is-indicated-by-high
  - target: cross-validation
    type: is_mitigated_by
tags: [machine-learning, model-evaluation, error-analysis, machine-learning-problem]
sourced_from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019
---

# Overfitting

## Definition
Overfitting occurs when a model performs very well on its training data but has a high generalization error, meaning it fails to perform well on new, unseen data. It essentially learns the noise and specific instances in the training set rather than the underlying general patterns.

## Identification
A model is considered to be overfitting if its training error is low (i.e., it makes few mistakes on the training set) while its generalization error is high. This discrepancy indicates the model has not learned to generalize.

## Mitigation
The text implies that overfitting can be addressed through techniques like regularization. Applying some regularization helps to avoid overfitting by constraining the model's complexity.

## Relationships

- **is-prevented-by**: [[regularization|Regularization]]
- **is-indicated-by-high**: [[generalization-error|Generalization Error]]
- **is_mitigated_by**: [[cross-validation|Cross Validation]]

---
*Extracted from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019*