---
type: concept
aliases: [Eigendecomposition]
summary: A method of decomposing a square matrix into a set of its constituent eigenvectors and corresponding eigenvalues, revealing its functional properties.
relationships:
  - target: singular-value-decomposition
    type: is_related_to
  - target: determinant
    type: is_related_to
tags: [linear-algebra, matrix-decomposition]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Eigendecomposition

## Definition
Eigendecomposition is a widely used form of matrix decomposition that breaks a square matrix A into a set of eigenvectors and eigenvalues. An eigenvector is a non-zero vector v that, when multiplied by A, is only scaled by a scalar λ, known as the eigenvalue, such that Av = λv.

## Mathematical Formulation
The full decomposition allows the original matrix A to be rewritten as A = V diag(λ)V⁻¹, where V is a matrix whose columns are the eigenvectors of A, and diag(λ) is a diagonal matrix with the corresponding eigenvalues on the diagonal.

## Purpose and Properties
Much like decomposing an integer into prime factors reveals its true nature, eigendecomposition shows information about a matrix's functional properties that are not obvious from its raw array of elements. The eigenvalues, for instance, determine if a matrix is positive definite (all eigenvalues > 0) or positive semidefinite (all eigenvalues >= 0).

## Relationships

- **is_related_to**: [[singular-value-decomposition|Singular Value Decomposition]]
- **is_related_to**: [[determinant|Determinant]]

---
*Extracted from: Deep+Learning+Ian+Goodfellow*