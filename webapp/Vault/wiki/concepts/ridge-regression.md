---
type: concept
aliases: [Ridge Regression]
summary: A regularized version of Linear Regression that adds a penalty term proportional to the square of the magnitude of the model's weights to the cost function, helping to prevent overfitting.
relationships:
  - target: linear-regression
    type: is_regularized_version_of
tags: [regularization, linear-regression, tikhonov-regularization]
sourced_from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019
---

# Ridge Regression

## Definition
Ridge Regression, also known as Tikhonov regularization, is a regularized version of Linear Regression. It works by adding a regularization term to the cost function, which forces the learning algorithm to not only fit the data but also to keep the model weights as small as possible. This constraint helps to reduce model complexity and prevent overfitting.

## The Regularization Term
The regularization term added to the cost function is $\alpha \sum_{i=1}^{n} \theta_i^2$. This term is the L2 norm of the model's weight vector. The hyperparameter $\alpha$ controls the degree of regularization; a larger $\alpha$ value increases the penalty on large weights, leading to a simpler model. This term should only be added to the cost function during training.

## Training vs. Evaluation
It is common for the cost function used during training to differ from the performance measure used for testing. In the case of Ridge Regression, the regularization term is part of the training cost function to guide the optimization process. However, once the model is trained, its performance should be evaluated using the unregularized performance measure, such as the standard Mean Squared Error, to reflect its true predictive power on new data.

## Relationships

- **is_regularized_version_of**: [[linear-regression|Linear Regression]]

---
*Extracted from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019*