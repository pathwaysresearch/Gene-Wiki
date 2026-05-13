---
type: concept
aliases: [Decision Tree Learning Algorithm]
summary: A recursive, greedy algorithm that builds a decision tree by selecting the most important attribute at each step to split the data, aiming to correctly classify the training examples.
relationships:
  - target: decision-tree
    type: builds
  - target: information-gain
    type: uses
tags: [algorithm, machine-learning, greedy-algorithm]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Decision Tree Learning Algorithm

## Core Idea
The decision tree learning algorithm operates recursively by starting with a set of examples and choosing the best attribute to split them into smaller subsets. This process, often described as a greedy approach, is repeated for each resulting subset until a stopping condition is met, such as all examples in a subset belonging to the same class.

## Algorithm Steps
The algorithm handles four main cases in its recursive calls: 1. If all remaining examples share the same classification, it returns that classification as a leaf node. 2. If there are no examples left for a branch, it returns the most common classification from the parent's set of examples. 3. If there are no attributes left but examples are mixed, it returns the most common classification among the current examples. 4. Otherwise, it chooses the best attribute A, creates a root node for that attribute, and recursively calls the algorithm on the subsets of examples corresponding to each value of A.

## Attribute Selection
A critical step in the algorithm is choosing the 'best' attribute to split the data. This is done by selecting the attribute that maximizes an IMPORTANCE function. This function measures how well the attribute separates the examples into subsets that are predominantly of one class. A common metric for importance is information gain.

## Relationships

- **builds**: [[decision-tree|Decision Tree]]
- **uses**: [[information-gain|Information Gain]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*