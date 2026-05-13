---
type: concept
aliases: [Vector]
summary: A mathematical object defined as an ordered sequence of values, supporting fundamental operations like addition, scalar multiplication, and dot product.
tags: [linear-algebra, mathematics]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
relationships:
  - target: linear-combination
    type: is_an_operation_on
---

# Vector

## Definition and Notation
A vector is defined as an ordered sequence of values, such as x = (3, 4) in a two-dimensional space. The elements of a vector are accessed using subscripts, for example z = (z_1, z_2, ..., z_n). The text notes that different subfields use various notations for vectors, including (1, 2), [1, 2], or <1, 2>, and may refer to them as vectors, lists, or tuples.

## Fundamental Operations
The two fundamental operations on vectors are vector addition and scalar multiplication. Vector addition is an elementwise sum; for example, given x = (3, 4) and y = (0, 2), their sum is x + y = (3+0, 4+2) = (3, 6). Scalar multiplication involves multiplying each element of the vector by a constant; for example, 5x = (5 * 3, 5 * 4) = (15, 20).

## Key Calculations
Two common calculations involving vectors are determining their length and computing the dot product. The length of a vector x, denoted |x|, is the square root of the sum of the squares of its elements, such as |(3,4)| = sqrt(3^2 + 4^2) = 5. The dot product (or scalar product) of two vectors, x · y, is the sum of the products of their corresponding elements, such as (3,4) · (0,2) = (3 * 0) + (4 * 2) = 8.

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*

---
*Also referenced in: Deep+Learning+Ian+Goodfellow*