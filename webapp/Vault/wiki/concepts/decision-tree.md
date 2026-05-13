---
type: concept
aliases: [Decision Tree]
summary: A predictive model that represents a function mapping attributes to a conclusion about the target value. It uses a tree-like structure of decisions and their possible consequences.
relationships:
  - target: cart-algorithm
    type: is_trained_by
  - target: classification
    type: is-a-method-for
  - target: decision-tree-learning-algorithm
    type: is-built-by
tags: [machine-learning, classification-model, representation]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Decision Tree

## Representation
A decision tree represents a function as a sequence of attribute tests. Each internal node in the tree corresponds to a test on an attribute, each branch represents an outcome of the test, and each leaf node represents a class label. A path from the root to a leaf represents a classification rule, which is a conjunction of attribute-value tests. The entire tree is equivalent to a disjunctive normal form expression.

## Expressiveness
Decision trees are capable of representing any function in propositional logic. For a wide variety of problems, the decision tree format can yield a concise result. However, their conciseness varies greatly depending on the function being modeled.

## Limitations
Some functions cannot be represented concisely by decision trees. For example, the majority function, which returns true if more than half of its inputs are true, requires an exponentially large decision tree. This illustrates that decision trees are well-suited for some kinds of functions but not others, and no single representation is efficient for all possible functions.

## Relationships

- **is-a-method-for**: [[classification|Classification]]
- **is-built-by**: [[decision-tree-learning-algorithm|Decision Tree Learning Algorithm]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*

---
*Also referenced in: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019*