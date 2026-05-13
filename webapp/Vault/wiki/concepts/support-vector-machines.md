---
type: concept
aliases: [Support Vector Machines (SVMs)]
summary: A class of supervised learning models that use kernel methods to find an optimal hyperplane for classification and regression tasks.
relationships:
  - target: kernel-trick
    type: uses
  - target: vladimir-vapnik
    type: developed_by
  - target: corinna-cortes
    type: developed_by
tags: [machine-learning, classification, kernel-methods, supervised-learning]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Support Vector Machines (SVMs)

## Overview
Support Vector Machines (SVMs) are a popular and effective class of supervised learning algorithms. The theoretical foundations for SVMs come from kernel machines, with the ideas originating from Aizerman et al. (1964) and the full theory developed by Vladimir Vapnik and his colleagues.

## Key Developments
SVMs were made practical for real-world problems through several key innovations. The soft-margin classifier, introduced by Cortes and Vapnik in 1995, enabled the handling of noisy data. The Sequential Minimal Optimization (SMO) algorithm, developed by Platt in 1999, provided an efficient method for solving the underlying quadratic programming problem. These methods leverage the kernel trick to operate in high-dimensional feature spaces.

## Applications and Performance
SVMs have proven effective for a variety of tasks, including text categorization, computational genomics, and natural language processing tasks like handwritten digit recognition. In a comparison of algorithms for digit recognition, a standard SVM achieved a 1.1% error rate, while a variant called a Virtual SVM achieved 0.56%.

## Relationships

- **uses**: [[kernel-trick|Kernel Trick]]
- **developed_by**: [[vladimir-vapnik|Vladimir Vapnik]]
- **developed_by**: [[corinna-cortes|Corinna Cortes]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*