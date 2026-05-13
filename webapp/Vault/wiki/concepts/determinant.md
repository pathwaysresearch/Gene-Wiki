---
type: concept
aliases: [Determinant]
summary: A scalar value derived from a square matrix, equal to the product of its eigenvalues, which measures how the matrix transformation scales volume.
relationships:
  - target: eigendecomposition
    type: uses_property_of
tags: [linear-algebra, matrix-properties]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Determinant

## Definition
The determinant of a square matrix A, denoted det(A), is a function that maps the matrix to a single real scalar value.

## Relationship to Eigenvalues
The determinant is directly related to the matrix's eigenvalues; it is equal to the product of all the eigenvalues of the matrix.

## Geometric Interpretation
The absolute value of the determinant provides a measure of how much the linear transformation represented by the matrix expands or contracts space. If the determinant is 0, space is completely contracted along at least one dimension, losing all volume. If the determinant is 1, the transformation is volume-preserving.

## Relationships

- **uses_property_of**: [[eigendecomposition|Eigendecomposition]]

---
*Extracted from: Deep+Learning+Ian+Goodfellow*