---
type: concept
aliases: [CART Algorithm]
summary: The Classification and Regression Tree (CART) algorithm is a greedy algorithm used by Scikit-Learn to train Decision Trees by recursively splitting the data to create the purest possible subsets.
relationships:
  - target: decision-tree
    type: trains
  - target: gini-impurity
    type: uses
  - target: scikit-learn
    type: is_implemented_in
tags: [algorithm, decision-trees, greedy-algorithm]
sourced_from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019
---

# CART Algorithm

## Splitting Mechanism
The algorithm works by first splitting the training set into two subsets using a single feature `k` and a threshold `t_k`. It exhaustively searches for the pair (k, t_k) that produces the "purest" subsets, where purity is weighted by the size of the subsets.

## Cost Function for Classification
To find the best split, the algorithm seeks to minimize a cost function. For classification tasks, this function is the weighted average of the Gini impurity of the left and right subsets resulting from the split.

## Recursive and Greedy Nature
After the initial split, the algorithm applies the same logic recursively to the subsets, and then to the sub-subsets, and so on. This process, also called "growing" the tree, stops when a stopping condition is met, such as reaching the `max_depth` hyperparameter or being unable to find a split that reduces impurity. The algorithm is considered greedy because it makes the locally optimal choice at each step rather than searching for a globally optimal tree.

## Relationships

- **trains**: [[decision-tree|Decision Tree]]
- **uses**: [[gini-impurity|Gini Impurity]]
- **is_implemented_in**: [[scikit-learn|Scikit Learn]]

---
*Extracted from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019*