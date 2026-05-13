---
type: concept
aliases: [Early Stopping]
summary: A regularization technique for iterative learning algorithms that stops training as soon as the validation error reaches a minimum to prevent overfitting.
relationships:
  - target: gradient-descent
    type: is_used_with
  - target: regularization
    type: is_a_method_of
  - target: overfitting
    type: prevents
tags: [regularization, training-technique, overfitting, gradient-descent]
sourced_from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019
---

# Early Stopping

## Definition
Early stopping is a regularization technique applicable to iterative learning algorithms like Gradient Descent. The fundamental principle is to monitor the model's performance on a separate validation set during training and to halt the training process at the optimal point to avoid overfitting. The text notes that Geoffrey Hinton called it a “beautiful free lunch” for its simplicity and effectiveness.

## How It Works
As an iterative algorithm trains, its prediction error (e.g., RMSE) on the training set consistently decreases. The error on the validation set also decreases initially but will eventually reach a minimum and start to rise. This increase in validation error indicates that the model has begun to overfit the training data. Early stopping works by simply stopping the training process as soon as the validation error reaches this minimum point.

## Application
This technique is used to find a good model without having to train for a fixed number of epochs and then select the best model. It provides an implicit form of regularization by constraining the model complexity through the duration of training. It is a very different approach to regularization compared to methods that add a penalty term to the cost function, like Ridge or Lasso Regression.

## Relationships

- **is_used_with**: [[gradient-descent|Gradient Descent]]
- **is_a_method_of**: [[regularization|Regularization]]
- **prevents**: [[overfitting|Overfitting]]

---
*Extracted from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019*

---
*Also referenced in: Deep+Learning+Ian+Goodfellow*