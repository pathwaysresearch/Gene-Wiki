---
type: concept
aliases: [Feature Selection]
summary: The process of selecting a subset of relevant features for use in model construction, often to reduce computational expense, improve model performance, and avoid overfitting.
relationships:
  - target: n-gram-model
    type: can-be-applied-to
tags: [machine-learning, feature-engineering, text-categorization]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Feature Selection

## Definition
Feature selection is a process used to keep only the features that best discriminate between classes, particularly when dealing with a very large feature vector. It is often employed to manage the computational expense of running algorithms on high-dimensional data and to improve the model's generalization performance.

## Application in Text Categorization
In tasks like spam detection, the feature vector can be very large, including n-grams and other metadata. Feature selection helps by identifying and retaining only the most discriminative features. For example, a common bigram like "of the" might be equally frequent in spam and ham messages, making it a poor discriminator and a candidate for removal.

## Importance
The choice of features is often the most important part of creating a good classifier, sometimes more so than the choice of the learning algorithm itself. This is especially true when large amounts of training data are available, as the data can accurately determine the utility of a proposed feature. In adversarial tasks like spam detection, features must be constantly updated.

## Relationships

- **can-be-applied-to**: [[n-gram-model|N Gram Model]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*