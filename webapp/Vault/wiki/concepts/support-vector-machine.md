---
type: concept
aliases: [Support Vector Machine]
summary: A supervised learning model that finds an optimal hyperplane, known as the maximum margin separator, to classify data points and maximize generalization.
relationships:
  - target: kernel-trick
    type: uses
  - target: svm-regression
    type: can_be_used_for
  - target: primal-and-dual-problem
    type: optimization_involves
  - target: kernel-method
    type: uses
tags: [supervised-learning, classification, optimization]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Support Vector Machine

## Core Principle
Support Vector Machines (SVMs) are a machine learning method for classification that focuses on minimizing expected generalization loss rather than empirical loss on the training data. The core idea is to find a decision boundary that is as far away as possible from any of the data points in the training set. This approach is based on the principle from computational learning theory that a larger margin between the separator and the examples leads to better generalization performance on unseen data.

## Maximum Margin Separator
The optimal decision boundary sought by an SVM is called the maximum margin separator. The margin is defined as the region bounded by two parallel hyperplanes that pass through the closest points of each class, with the separator lying exactly in the middle. These closest points, which lie on the edge of the margin, are called the support vectors because they alone "support" or define the position of the separator. All other points could be removed without changing the final result.

## Handling Noisy Data with Soft Margins
In real-world scenarios, data is often noisy and not perfectly linearly separable. To handle this, SVMs can be modified to use a soft margin classifier. This variation allows some data points to fall on the wrong side of the decision boundary or within the margin. It introduces a penalty for these misclassified points that is proportional to the distance they would need to move to be on the correct side, providing a more robust model for non-ideal datasets.

## Relationships

- **uses**: [[kernel-method|Kernel Method]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*

---
*Also referenced in: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019*