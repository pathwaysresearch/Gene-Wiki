---
type: concept
aliases: [L2 Norm]
summary: A function that measures the size of a vector, also known as the Euclidean norm, corresponding to the Euclidean distance from the origin to the point identified by the vector.
relationships:
  - target: l1-norm
    type: is_an_alternative_to
tags: [linear-algebra, machine-learning, regularization]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# L2 Norm

## Definition
The L² norm, also called the Euclidean norm, is a specific type of Lᵖ norm where p=2. It measures the size of a vector by calculating its Euclidean distance from the origin. In machine learning contexts, it is so common that it is often denoted simply as ||x|| without the subscript.

## Squared L2 Norm
It is very common to work with the squared L² norm, calculated as xᵀx. This form is often more convenient both mathematically and computationally. For example, its derivatives with respect to each element of x depend only on that corresponding element, whereas the derivatives of the L² norm itself depend on the entire vector.

## Properties and Limitations
A key property of the squared L² norm is that it increases very slowly near the origin. This can be undesirable in some machine learning applications where it is important to distinguish between elements that are exactly zero and those that are small but nonzero. In such cases, other norms like the L¹ norm may be preferred.

## Relationships

- **is_an_alternative_to**: [[l1-norm|L1 Norm]]

---
*Extracted from: Deep+Learning+Ian+Goodfellow*