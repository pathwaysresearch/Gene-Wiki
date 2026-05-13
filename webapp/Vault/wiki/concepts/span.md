---
type: concept
aliases: [Span]
summary: The set of all points that can be reached by any linear combination of a given set of vectors.
relationships:
  - target: linear-combination
    type: is_defined_by
tags: [linear-algebra, vector-space]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Span

## Definition
The span of a set of vectors is defined as the set of all points that are obtainable by forming a linear combination of those original vectors.

## Role in Linear Equations
The concept of span is crucial for determining whether a system of linear equations of the form Ax = b has a solution. A solution exists if the vector b is within the span of the columns of matrix A.

## Conceptual Link
The span is directly built upon the idea of a linear combination. While a linear combination is a specific operation that produces one new vector, the span is the entire collection of all possible vectors that can be produced from the original set.

## Relationships

- **is_defined_by**: [[linear-combination|Linear Combination]]

---
*Extracted from: Deep+Learning+Ian+Goodfellow*