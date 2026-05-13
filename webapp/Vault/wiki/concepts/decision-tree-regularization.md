---
type: concept
aliases: [Decision Tree Regularization]
summary: A set of techniques used to constrain the freedom of a Decision Tree model during training to prevent it from overfitting the data. This is achieved by controlling hyperparameters that restrict the tree's shape and complexity.
relationships:
  - target: overfitting
    type: prevents
  - target: scikit-learn
    type: implemented_in
tags: [machine-learning, regularization, decision-trees]
sourced_from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019
---

# Decision Tree Regularization

## Definition
Regularization for Decision Trees involves restricting the model's freedom during training to avoid overfitting. This is accomplished by adjusting various hyperparameters that control the structure of the tree, such as its maximum depth or the minimum number of samples required to split a node.

## Key Hyperparameters
In Scikit-Learn, the `DecisionTreeClassifier` class provides several hyperparameters for regularization. The `max_depth` parameter limits the maximum depth of the tree. Other parameters restrict the shape of the tree by setting minimums, such as `min_samples_split` (the minimum samples a node must have to be split) and `min_samples_leaf` (the minimum samples a leaf node must have). Conversely, parameters like `max_leaf_nodes` and `max_features` impose maximums on the number of leaf nodes and the features evaluated at each split, respectively.

## Effect of Regularization
Increasing the `min_*` hyperparameters or reducing the `max_*` hyperparameters will regularize the model, thus reducing the risk of overfitting. For example, in a regression task, a Decision Tree with no restrictions will overfit the training set badly, but setting a parameter like `min_samples_leaf=10` can result in a much more reasonable and generalized model. Other algorithms perform regularization by first training an unrestricted tree and then pruning (deleting) unnecessary nodes.

## Relationships

- **prevents**: [[overfitting|Overfitting]]
- **implemented_in**: [[scikit-learn|Scikit Learn]]

---
*Extracted from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019*