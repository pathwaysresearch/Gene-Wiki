---
type: concept
aliases: [Decision Trees]
summary: A predictive model that uses a tree-like graph of decisions and their possible consequences, used in classification and regression.
relationships:
  - target: inductive-learning
    type: is_a_method_for
tags: [machine-learning, classification, supervised-learning]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Decision Trees

## Definition and Representation
A decision tree is a model used in machine learning that can represent all Boolean functions. It is a hierarchical structure where internal nodes represent tests on attributes, and leaf nodes represent the final classification or outcome.

## Construction
The recursive construction of decision trees aims to find a simple and consistent tree. The information-gain heuristic is cited as an efficient method for achieving this. If a leaf node still contains a mixed set of positive and negative examples after all attributes have been used, the standard approach is to choose the majority classification, a solution which minimizes the absolute error over the examples at that leaf.

## Expressiveness
Decision trees are a powerful representation. An exercise in the text explores their relationship with decision lists, asking for a proof that a decision list can represent the same function as a decision tree using at most as many rules as the tree has leaves.

## Relationships

- **is_a_method_for**: [[inductive-learning|Inductive Learning]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*