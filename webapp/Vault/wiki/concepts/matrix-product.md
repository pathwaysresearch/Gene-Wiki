---
type: concept
aliases: [Matrix Product]
summary: A fundamental operation in linear algebra that produces a third matrix from two matrices, where the dimensions of the input matrices must be compatible.
tags: [linear-algebra, mathematics]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Matrix Product

## Definition
The matrix product of two matrices, A and B, is a third matrix, C = AB. This operation is one of the most important involving matrices and is distinct from an element-wise product (or Hadamard product).

## How It Works
For the product C = AB to be defined, the number of columns in matrix A must be equal to the number of rows in matrix B. If A has shape m × n and B has shape n × p, the resulting matrix C will have shape m × p. Each element Cᵢ,ⱼ is calculated by the sum of products of corresponding elements from the i-th row of A and the j-th column of B, formally defined as Cᵢ,ⱼ = ∑ₖ Aᵢ,ₖ Bₖ,ⱼ.

## Contrast with Element-wise Product
The standard matrix product should not be confused with the element-wise product, also known as the Hadamard product. The element-wise product is a separate operation that involves simply multiplying the corresponding individual elements of two matrices.

---
*Extracted from: Deep+Learning+Ian+Goodfellow*