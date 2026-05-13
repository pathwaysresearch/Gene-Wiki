---
type: concept
aliases: [Karush-Kuhn-Tucker (KKT) Approach]
summary: A general method for solving constrained optimization problems by introducing a new function, the generalized Lagrangian, which incorporates the original objective function and the constraints.
tags: [optimization, constrained-optimization, lagrangian-multipliers]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Karush-Kuhn-Tucker (KKT) Approach

## Overview
The Karush-Kuhn-Tucker (KKT) approach is a comprehensive framework for handling constrained optimization problems. It transforms a constrained problem into an unconstrained one by defining a new function called the generalized Lagrangian or generalized Lagrange function.

## The Generalized Lagrangian
To apply the KKT approach, the feasible region of the solution space must be described by a set of equality constraints ($g^{(i)}(x) = 0$) and inequality constraints ($h^{(j)}(x) \le 0$). For each constraint, a new variable called a KKT multiplier is introduced ($\lambda_i$ for equality constraints, $\alpha_j$ for inequality constraints). The generalized Lagrangian is then constructed as $L(x, \boldsymbol{\lambda}, \boldsymbol{\alpha}) = f(x) + \sum_i \lambda_i g^{(i)}(x) + \sum_j \alpha_j h^{(j)}(x)$, where $f(x)$ is the original objective function.

## Solving the Problem
The original constrained minimization problem, $\min_{x \in \mathbb{S}} f(x)$, can be solved by finding the solution to an unconstrained optimization problem involving the Lagrangian: $\min_x \max_{\boldsymbol{\lambda}} \max_{\boldsymbol{\alpha}, \boldsymbol{\alpha} \ge 0} L(x, \boldsymbol{\lambda}, \boldsymbol{\alpha})$. The solution must satisfy a set of conditions, including that the gradient of the generalized Lagrangian is zero and all constraints on the variables and KKT multipliers are met.

---
*Extracted from: Deep+Learning+Ian+Goodfellow*