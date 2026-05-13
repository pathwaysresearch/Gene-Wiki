---
type: concept
aliases: [Gini Impurity]
summary: A metric used by the CART algorithm to measure the impurity or class mixture of a node in a decision tree, where a lower value indicates a more homogeneous set of instances.
relationships:
  - target: cart-algorithm
    type: is_used_by
  - target: decision-tree
    type: is_a_property_of_nodes_in
tags: [decision-trees, metric, classification]
sourced_from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019
---

# Gini Impurity

## Definition
Gini impurity is a measure of how mixed the classes are for the set of training instances at a given node in a decision tree. A node is considered "pure" if all instances it applies to belong to the same class, in which case its Gini score is 0.

## Role in the CART Algorithm
The CART training algorithm uses Gini impurity as the core of its cost function for classification. When searching for the best split (a feature `k` and threshold `t_k`), the algorithm's goal is to find the split that minimizes the weighted average of the Gini scores of the two resulting child nodes.

## Example in a Tree Node
The text provides an example where a node in a decision tree for classifying Iris flowers applies only to Iris-Setosa training instances. This node is pure, and therefore its Gini score is 0. Other nodes that apply to a mix of classes, such as 1 Iris-Versicolor and 45 Iris-Virginica, would have a non-zero Gini score.

## Relationships

- **is_used_by**: [[cart-algorithm|Cart Algorithm]]
- **is_a_property_of_nodes_in**: [[decision-tree|Decision Tree]]

---
*Extracted from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019*