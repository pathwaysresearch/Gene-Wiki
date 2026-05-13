---
type: concept
aliases: [Continuation Methods]
summary: A family of optimization strategies that solve a difficult problem by starting with an easier version and gradually transitioning to the more complex, true objective function.
relationships:
  - target: curriculum-learning
    type: includes
tags: [optimization-strategy, numerical-methods, machine-learning]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Continuation Methods

## Definition
Continuation methods are a family of strategies designed to make optimization easier by carefully choosing initial points to ensure that local optimization spends most of its time in well-behaved regions of the parameter space. The core idea is to solve a sequence of problems that gradually increase in difficulty, culminating in the true problem of interest.

## How It Works
To minimize a difficult cost function J(θ), a series of related objective functions {J^(0), ..., J^(n)} is constructed. This series is designed such that J^(0) is easy to minimize, and the final function J^(n) is the true cost function J(θ). The process begins by solving the easy problem, and the solution to each problem J^(i) is used as a good initial point for solving the next, slightly harder problem J^(i+1). This incremental approach guides the optimizer toward a good solution for the final, complex problem.

## Relationship to Other Methods
Traditional continuation methods often involve smoothing the objective function, starting with a heavily smoothed version and gradually reducing the smoothing. This concept is closely related to other optimization strategies. For example, curriculum learning can be seen as a type of continuation method where the difficulty is controlled by the selection of training data.

## Relationships

- **includes**: [[curriculum-learning|Curriculum Learning]]

---
*Extracted from: Deep+Learning+Ian+Goodfellow*