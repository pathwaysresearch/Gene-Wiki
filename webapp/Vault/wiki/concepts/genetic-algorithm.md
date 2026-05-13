---
type: concept
aliases: [Genetic Algorithm]
summary: An evolutionary computation technique, also known as machine evolution, that generates solutions by applying small, random mutations to a program and using a selection process to preserve beneficial changes. A stochastic search algorithm inspired by biological evolution, using concepts like population, fitness, selection, crossover, and mutation to find solutions to optimization problems. A search heuristic inspired by natural selection that evolves a population of candidate solutions to a problem using operators like selection, crossover, and mutation.
relationships:
  - target: schema-genetic-algorithm
    type: uses
  - target: heuristic-search
    type: is_a
tags: [evolutionary-computation, optimization, early-ai, evolutionary-algorithm, stochastic-search, search]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Genetic Algorithm

## Definition and Method
Based on the belief that an appropriate series of small mutations to a machine-code program can generate a program with good performance, the method involves trying random mutations and applying a selection process to preserve those that seem useful. This approach was originally called machine evolution.

## Early Experiments
Early experiments in this area were conducted by Friedberg (1958) and Friedberg et al. (1959). These experiments were based on the idea of evolving programs through random mutation and selection.

## Historical Limitations
The initial optimism for this approach was dampened by the intractability of the problems. Early experiments failed to scale up, as the sheer number of possible mutation combinations made finding a solution in practice infeasible, even with thousands of hours of computer time. This highlighted the difference between a program being able to find a solution in principle and having the necessary mechanisms to find it in practice.

## Relationships

- **uses**: [[schema-genetic-algorithm|Schema Genetic Algorithm]]
- **is_a**: [[heuristic-search|Heuristic Search]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*