---
type: concept
aliases: [Kernel Trick]
summary: A method used in machine learning to operate in a high-dimensional feature space without explicitly computing the coordinates of the data in that space.
relationships:
  - target: stochastic-gradient-descent
    type: is_contrasted_with
  - target: support-vector-machine
    type: used_by
  - target: mercers-theorem
    type: is_justified_by
  - target: primal-and-dual-problem
    type: requires
  - target: support-vector-machines
    type: used_by
tags: [machine-learning, kernel-methods, svms]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Kernel Trick

## Definition
The kernel trick is a technique that allows algorithms to implicitly operate in a high-dimensional, or even exponential, feature space. This is done by using a kernel function to compute the inner products between the images of data points in the feature space, thereby avoiding the computationally expensive step of explicitly mapping the data into that space.

## Origin
The foundational ideas behind kernel machines, which includes the kernel trick, were first introduced by Aizerman et al. in 1964.

## Application in Machine Learning
The kernel trick is a core component of Support Vector Machines (SVMs) and related techniques like the voted perceptron. Its power has led to the design of many new kernels that can work with nonnumerical data types such as strings and trees, significantly broadening the applicability of these learning methods.

## Relationships

- **used_by**: [[support-vector-machines|Support Vector Machines]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*

---
*Also referenced in: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019*

---
*Also referenced in: Deep+Learning+Ian+Goodfellow*