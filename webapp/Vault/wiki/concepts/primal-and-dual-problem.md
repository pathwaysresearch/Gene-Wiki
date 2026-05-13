---
type: concept
aliases: [Primal and Dual Problem]
summary: In constrained optimization for SVMs, the primal problem is the original formulation, while the dual problem is a related problem whose solution provides a lower bound and, in this case, the same solution.
relationships:
  - target: support-vector-machine
    type: is_a_concept_in
  - target: kernel-trick
    type: enables
tags: [optimization, svm, mathematical-programming]
sourced_from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019
---

# Primal and Dual Problem

## Definition
For a given constrained optimization problem, known as the primal problem, it is possible to express a different but closely related problem called its dual problem. The solution to the dual typically gives a lower bound to the solution of the primal.

## Application in SVMs
The SVM optimization problem meets the conditions where the primal and dual problems have the same solution. This allows one to choose to solve either problem. The dual form of the linear SVM objective is expressed in Equation 5-6 of the text.

## Importance for the Kernel Trick
Solving the dual problem is the key to using the kernel trick in SVMs. The dual formulation depends on dot products of the input feature vectors, which can be replaced by a kernel function, whereas the primal problem does not offer this opportunity.

## Relationships

- **is_a_concept_in**: [[support-vector-machine|Support Vector Machine]]
- **enables**: [[kernel-trick|Kernel Trick]]

---
*Extracted from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019*