---
type: concept
aliases: [Cross Entropy]
summary: A cost function commonly used in multiclass classification that measures how well a set of estimated class probabilities match the target classes.
relationships:
  - target: log-loss
    type: generalizes
  - target: softmax-regression
    type: is_cost_function_for
tags: [cost-function, classification, information-theory, softmax-regression]
sourced_from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019
---

# Cross Entropy

## Definition and Objective
Cross entropy is a cost function frequently used to measure how well a set of estimated class probabilities match the target classes, particularly in multiclass classification problems (e.g., with Softmax Regression). The objective of minimizing the cross entropy cost function is to train a model that estimates a high probability for the target class and, consequently, low probabilities for all other classes. It achieves this by penalizing the model when it estimates a low probability for a target class.

## Origins
The concept of cross entropy originated from information theory. It provides a way to measure the difference between two probability distributions—in machine learning, this is typically the distribution of the true labels and the distribution of the model's predicted probabilities.

## Relationship to Log Loss
Cross entropy is a general cost function that encompasses Log Loss. The text explicitly states that when there are just two classes (K=2), the cross entropy cost function is equivalent to the Log Loss cost function used in Logistic Regression.

## Relationships

- **generalizes**: [[log-loss|Log Loss]]
- **is_cost_function_for**: [[softmax-regression|Softmax Regression]]

---
*Extracted from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019*

---
*Also referenced in: Deep+Learning+Ian+Goodfellow*