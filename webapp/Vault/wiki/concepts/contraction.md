---
type: concept
aliases: [Contraction]
summary: A mathematical function that, when applied to any two points in a metric space, brings them closer together by at least a constant factor, used to prove convergence of algorithms like value iteration.
relationships:
  - target: value-iteration
    type: proves_convergence_of
tags: [mathematical-concept, fixed-point-theorems, algorithm-analysis]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Contraction

## Definition
A contraction is a function of one argument that, when applied to two different inputs, produces two output values that are closer together by at least some constant factor than the original inputs. For example, the function 'divide by two' is a contraction because the difference between any two numbers is halved after the function is applied to both.

## Key Properties
A contraction has two important properties that ensure convergence. First, a contraction has only one fixed point—a value that is unchanged by the application of the function. If there were two fixed points, they would not get closer together, which would violate the definition. Second, when the function is applied to any argument, the value must get closer to the fixed point, so repeated application guarantees convergence to that point.

## Application to Value Iteration
The concept of a contraction is used to formally prove that the value iteration algorithm converges to a unique set of utilities for an MDP. The Bellman update, which is applied repeatedly in the algorithm, is a contraction mapping. This property guarantees that the algorithm will converge to the unique fixed point, which corresponds to the true optimal utility function.

## Relationships

- **proves_convergence_of**: [[value-iteration|Value Iteration]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*