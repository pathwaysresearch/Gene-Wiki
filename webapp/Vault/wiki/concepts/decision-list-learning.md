---
type: concept
aliases: [Decision List Learning]
summary: A machine learning algorithm that produces a model in the form of an ordered set of if-then rules to perform classification.
tags: [machine-learning, classification, rule-based-systems]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Decision List Learning

## Definition
Decision list learning is an algorithm that constructs a classifier as a sequence of tests. Each test is associated with an outcome (e.g., 'Yes' or 'No'). When classifying a new example, the tests are applied in order, and the first one that matches determines the classification.

## How It Works
The algorithm recursively builds the list. In each step, it searches for a test that matches a subset of the remaining training examples, all of which belong to the same class. Once such a test is found, a rule is created, and the examples it covers are removed. The algorithm then repeats the process on the remaining examples to form the rest of the list.

## Performance
Learning curves show that the performance of a decision list learner, measured by the proportion of correct classifications on a test set, improves as the size of the training set increases. On the restaurant dataset mentioned in the text, the decision list learning algorithm performed slightly better than a decision tree learning algorithm.

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*