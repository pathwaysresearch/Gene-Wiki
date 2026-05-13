---
type: concept
aliases: [Mercer's Theorem]
summary: A theorem in functional analysis that specifies the conditions under which a symmetric, continuous function can be used as a valid kernel in machine learning.
relationships:
  - target: kernel-trick
    type: provides_theory_for
tags: [functional-analysis, kernel-methods, svm, mathematical-theorem]
sourced_from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019
---

# Mercer's Theorem

## Statement of the Theorem
According to Mercer's theorem, if a function K(a, b) respects a few mathematical conditions known as Mercer's conditions (e.g., K must be continuous and symmetric, so K(a, b) = K(b, a)), then there exists a function φ that maps a and b into another space such that K(a, b) = φ(a)ᵀφ(b).

## Significance for the Kernel Trick
This theorem provides the theoretical foundation for the kernel trick. It guarantees that you can use K as a kernel since the mapping function φ is known to exist, even if you don’t know what φ is or if it maps to an infinite-dimensional space, as is the case for the Gaussian RBF kernel.

## Practical Implications
The theorem allows practitioners to use valid kernel functions without needing to explicitly define or compute the feature mapping φ. However, the text notes that some frequently used kernels, like the Sigmoid kernel, do not respect all of Mercer's conditions but can still work well in practice.

## Relationships

- **provides_theory_for**: [[kernel-trick|Kernel Trick]]

---
*Extracted from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019*