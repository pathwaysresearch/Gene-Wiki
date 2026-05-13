---
type: concept
aliases: [L1 Norm]
summary: A function that measures the size of a vector by summing the absolute values of its elements, often used in machine learning to distinguish between zero and small non-zero values.
relationships:
  - target: l2-norm
    type: is_an_alternative_to
tags: [linear-algebra, machine-learning, regularization, sparsity]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# L1 Norm

## Definition
The L¹ norm is a function used to measure the size of a vector. It is calculated by summing the absolute values of all the elements in the vector, as given by the formula ||x||₁ = ∑ᵢ |xᵢ|.

## Applications in Machine Learning
The L¹ norm is commonly used in machine learning, particularly in situations where the distinction between elements that are exactly zero and elements that are small but nonzero is important. It is chosen as an alternative to the L² norm, whose squared form grows very slowly near the origin.

## Key Properties
Unlike the squared L² norm, the L¹ norm grows at the same rate in all locations. This property makes it suitable for applications that require sensitivity to small values, while still retaining mathematical simplicity.

## Relationships

- **is_an_alternative_to**: [[l2-norm|L2 Norm]]

---
*Extracted from: Deep+Learning+Ian+Goodfellow*