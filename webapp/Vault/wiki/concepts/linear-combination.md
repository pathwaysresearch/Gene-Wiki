---
type: concept
aliases: [Linear Combination]
summary: An expression constructed from a set of vectors by multiplying each vector by a scalar and adding the results.
relationships:
  - target: span
    type: defines
  - target: vector
    type: is_an_operation_on
tags: [linear-algebra, mathematics]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Linear Combination

## Formal Definition
A linear combination of a set of vectors {v⁽¹⁾, ..., v⁽ⁿ⁾} is an operation given by multiplying each vector v⁽ⁱ⁾ by a corresponding scalar coefficient cᵢ and then summing the results: ∑ᵢ cᵢ v⁽ⁱ⁾.

## Relation to Matrix-Vector Products
The matrix-vector product Ax can be interpreted as a linear combination of the columns of matrix A. In this view, each element xᵢ of the vector x acts as the scalar coefficient for the corresponding column vector A:,ᵢ of the matrix A.

## Geometric Interpretation
When analyzing a system of linear equations like Ax = b, the concept of a linear combination is used to view the problem geometrically. The columns of A specify different directions one can travel from the origin, and the elements of x specify how far to travel in each of those directions to reach the point b.

## Relationships

- **defines**: [[span|Span]]
- **is_an_operation_on**: [[vector|Vector]]

---
*Extracted from: Deep+Learning+Ian+Goodfellow*