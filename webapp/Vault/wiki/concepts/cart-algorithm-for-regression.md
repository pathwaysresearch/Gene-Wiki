---
type: concept
aliases: [CART Algorithm for Regression]
summary: A version of the Classification and Regression Tree (CART) algorithm that builds regression trees by recursively splitting the training set to minimize the Mean Squared Error (MSE).
relationships:
  - target: mean-squared-error
    type: minimizes
  - target: decision-tree-regularization
    type: requires
tags: [machine-learning, decision-trees, regression]
sourced_from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019
---

# CART Algorithm for Regression

## Overview
The Classification and Regression Tree (CART) algorithm can be adapted for regression tasks. Unlike its classification counterpart which aims to minimize impurity, the regression version works by splitting the training set in a way that minimizes the Mean Squared Error (MSE).

## Cost Function
The algorithm seeks to minimize a specific cost function at each split. For a given node `k` and split threshold `t_k`, the cost function is a weighted average of the MSE of the two resulting child subsets (left and right). The weight for each subset is the ratio of its instances to the total instances in the parent node.

## Prediction and Overfitting
Within any given node, the model's prediction is the average value of the training instances in that node. Just like in classification, Decision Trees using the CART algorithm for regression are prone to overfitting if no regularization is applied. Applying constraints, such as setting a minimum number of samples per leaf, is crucial for creating a more generalized model.

## Relationships

- **minimizes**: [[mean-squared-error|Mean Squared Error]]
- **requires**: [[decision-tree-regularization|Decision Tree Regularization]]

---
*Extracted from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019*