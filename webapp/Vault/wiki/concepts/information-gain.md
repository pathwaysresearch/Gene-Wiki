---
type: concept
aliases: [Information Gain]
summary: A metric used in decision tree learning to select the best attribute for splitting a set of examples. It measures the expected reduction in entropy achieved by partitioning the examples according to an attribute.
relationships:
  - target: entropy-information-theory
    type: is-based-on
  - target: decision-tree-learning-algorithm
    type: is-used-by
tags: [decision-trees, metrics, attribute-selection]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Information Gain

## Role in Decision Tree Learning
Information gain is the criterion used by the `IMPORTANCE` function within the decision tree learning algorithm to select the best attribute at each node. The algorithm greedily chooses the attribute that provides the highest information gain, as this is expected to lead to the smallest tree.

## Connection to Entropy
Information gain is calculated based on the concept of entropy. It measures the difference between the entropy of the original set of examples and the weighted-average entropy of the subsets created after splitting on a particular attribute. A higher information gain signifies a greater reduction in uncertainty after the split.

## Potential Issues
The standard information gain measure can be biased towards attributes with many possible values. In an extreme case, an attribute with a unique value for every example would yield the highest possible information gain but would likely result in a tree that does not generalize well. To counteract this, alternatives like the gain ratio can be used.

## Relationships

- **is-based-on**: [[entropy-information-theory|Entropy Information Theory]]
- **is-used-by**: [[decision-tree-learning-algorithm|Decision Tree Learning Algorithm]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*