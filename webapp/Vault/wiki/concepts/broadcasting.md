---
type: concept
aliases: [Broadcasting]
summary: A notational shorthand used in deep learning where a vector is implicitly copied and added to each row of a matrix.
tags: [linear-algebra, deep-learning, notation]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Broadcasting

## Definition
Broadcasting is a convention used in deep learning that allows for the addition of a matrix and a vector, resulting in another matrix. It is considered a less conventional notation in standard linear algebra.

## How It Works
When adding a matrix A and a vector **b** to get a matrix C (i.e., C = A + **b**), broadcasting implicitly copies the vector **b** and adds it to each row of the matrix A. The formal operation is Cᵢ,ⱼ = Aᵢ,ⱼ + bⱼ.

## Purpose
This shorthand is used for convenience, as it eliminates the need to explicitly define a new matrix where the vector **b** is copied into each row before performing the addition.

---
*Extracted from: Deep+Learning+Ian+Goodfellow*