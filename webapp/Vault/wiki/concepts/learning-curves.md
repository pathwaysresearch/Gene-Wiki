---
type: concept
aliases: [Learning Curves]
summary: A plot of a model's performance on the training and validation sets as a function of the training set size, used to diagnose problems like underfitting or overfitting.
relationships:
  - target: linear-regression
    type: is_used_to_evaluate
  - target: polynomial-regression
    type: is_used_to_evaluate
tags: [model-evaluation, diagnostics, underfitting, overfitting]
sourced_from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019
---

# Learning Curves

## Definition
Learning curves are plots that visualize a model's performance on the training set and the validation set as a function of the training set size. They are a valuable tool for diagnosing how a model is learning and whether it is suffering from issues such as being too simple (underfitting) or too complex (overfitting).

## Interpretation for Underfitting
For an underfitting model, such as a plain Linear Regression model applied to non-linear data, the learning curves exhibit a distinct pattern. The training error starts low and rises to a plateau. The validation error starts high, decreases, and then plateaus at a level very close to the training error. Both errors plateau at a relatively high value, indicating that the model is unable to capture the underlying data structure.

## Diagnostic Value
When both the training and validation error curves are high and close together, it is a clear sign of underfitting. This situation implies that the model is too simple for the data, and simply adding more training examples will not improve its performance. The curves show that the model has reached its performance limit given its inherent constraints.

## Relationships

- **is_used_to_evaluate**: [[linear-regression|Linear Regression]]
- **is_used_to_evaluate**: [[polynomial-regression|Polynomial Regression]]

---
*Extracted from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019*