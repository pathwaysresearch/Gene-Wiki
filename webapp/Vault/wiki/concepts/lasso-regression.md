---
type: concept
aliases: [Lasso Regression]
summary: A regularized linear regression model that adds an L1 penalty term to the cost function, which tends to eliminate the weights of the least important features, performing automatic feature selection.
relationships:
  - target: ridge-regression
    type: is_related_to
  - target: regularization
    type: is_a_method_of
  - target: feature-selection
    type: is_a_method_for
tags: [linear-models, regularization, feature-selection, sparsity]
sourced_from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019
---

# Lasso Regression

## Cost Function
Lasso Regression is a regularized version of linear regression that adds a specific penalty term to the cost function. The cost function is defined as the Mean Squared Error (MSE) of the model's predictions plus a regularization term, which is the hyperparameter α multiplied by the sum of the absolute values of the feature weights (θᵢ). This is also known as the L1 norm of the weight vector.

## Key Characteristic: Sparsity
An important characteristic of Lasso Regression is its tendency to completely eliminate the weights of the least important features by setting them to exactly zero. This is a direct result of the L1 penalty term used in its cost function. For example, when applied to a model with high-degree polynomial features, Lasso can effectively reduce the model to a much simpler, almost linear one by zeroing out the weights of the higher-order terms.

## Automatic Feature Selection
By setting the weights of unimportant features to zero, Lasso Regression automatically performs feature selection. This results in a *sparse model*, which is a model with few nonzero feature weights. This property makes Lasso particularly useful when dealing with datasets that have a large number of features, many of which may be irrelevant.

## Relationships

- **is_related_to**: [[ridge-regression|Ridge Regression]]
- **is_a_method_of**: [[regularization|Regularization]]
- **is_a_method_for**: [[feature-selection|Feature Selection]]

---
*Extracted from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019*