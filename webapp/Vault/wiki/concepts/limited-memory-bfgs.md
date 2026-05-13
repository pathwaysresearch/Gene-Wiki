---
type: concept
aliases: [Limited Memory BFGS (L-BFGS)]
summary: A memory-efficient quasi-Newton optimization algorithm that approximates the inverse Hessian matrix, making it practical for large-scale problems like training modern deep learning models.
relationships:
  - target: conjugate-gradient-method
    type: is-an-alternative-to
tags: [optimization-algorithm, quasi-newton-method, large-scale-optimization]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Limited Memory BFGS (L-BFGS)

## Overview
Limited Memory BFGS (L-BFGS) is an optimization algorithm that addresses the significant memory costs of the standard Broyden–Fletcher–Goldfarb–Shanno (BFGS) algorithm. While BFGS is effective, it must store an inverse Hessian matrix approximation that requires O(n^2) memory, which is impractical for deep learning models with millions of parameters (n).

## How It Works
L-BFGS avoids storing the complete inverse Hessian approximation. Instead, it computes the approximation at each step using the same method as BFGS but begins with the assumption that the previous step's matrix is the identity matrix. It only stores some of the vectors used to update the matrix at each time step, reducing the memory cost to O(n) per step, making it feasible for large models.

## Comparison to Other Methods
Relative to the conjugate gradient method, L-BFGS has the advantage of being less dependent on the line search finding a point very close to the true minimum, meaning it can spend less time refining each line search. Unlike the full BFGS method, its reduced memory footprint makes it a practical choice for most modern deep learning applications. The procedure remains well-behaved even when the line search minimum is only reached approximately.

## Relationships

- **is-an-alternative-to**: [[conjugate-gradient-method|Conjugate Gradient Method]]

---
*Extracted from: Deep+Learning+Ian+Goodfellow*