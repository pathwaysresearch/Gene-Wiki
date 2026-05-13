---
type: concept
aliases: [Generalization Error]
summary: A measure of how accurately a machine learning model can predict outcomes for previously unseen data, as opposed to the data it was trained on.
relationships:
  - target: underfitting
    type: related_to
  - target: hyperparameter-tuning
    type: objective_of
  - target: effective-capacity
    type: influenced_by
  - target: overfitting
    type: is-a-measure-of
tags: [machine-learning, model-evaluation, performance-metrics]
sourced_from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019
---

# Generalization Error

## Definition
Generalization error is the error rate of a model on a test set of new, unseen data. A high generalization error indicates that the model is not performing well and may be overfitting the training data.

## Measurement
To estimate the generalization error, a portion of the data is held out as a test set. A common split is 80% for training and 20% for testing. However, the text notes that for very large datasets (e.g., 10 million instances), a smaller percentage for testing (e.g., 1%) can be sufficient to get a good estimate.

## Pitfall in Hyperparameter Tuning
The text warns against using the test set to tune hyperparameters. If you select a hyperparameter value that minimizes error on the test set, your model becomes optimized for that specific set. This leads to an overly optimistic error estimate, and the model will likely perform worse in a real-world production environment (e.g., a measured 5% error might become 15% in production).

## Relationships

- **is-a-measure-of**: [[overfitting|Overfitting]]

---
*Extracted from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019*

---
*Also referenced in: Deep+Learning+Ian+Goodfellow*