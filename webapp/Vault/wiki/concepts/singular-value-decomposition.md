---
type: concept
aliases: [Singular Value Decomposition]
summary: A factorization of any real matrix into singular vectors and singular values, serving as a more general alternative to eigendecomposition.
relationships:
  - target: eigendecomposition
    type: is_an_alternative_to
tags: [linear-algebra, matrix-decomposition]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Singular Value Decomposition

## Definition
The singular value decomposition (SVD) is a method to factorize a matrix into singular vectors and singular values. It provides another way to discover information about a matrix's properties, similar to eigendecomposition.

## Generality
The SVD is more generally applicable than eigendecomposition. While eigendecomposition is only defined for square matrices, every real matrix has a singular value decomposition, making it a crucial tool for analyzing non-square matrices.

## Relationship to Eigendecomposition
SVD is presented as an alternative to eigendecomposition. While eigendecomposition rewrites a matrix A as A = V diag(λ)V⁻¹, SVD provides a similar but distinct factorization that is applicable in more cases.

## Relationships

- **is_an_alternative_to**: [[eigendecomposition|Eigendecomposition]]

---
*Extracted from: Deep+Learning+Ian+Goodfellow*