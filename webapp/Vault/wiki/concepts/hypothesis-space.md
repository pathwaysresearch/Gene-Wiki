---
type: concept
aliases: [Hypothesis Space]
summary: The set of functions that a learning algorithm is allowed to select as a potential solution for a given task.
relationships:
  - target: model-capacity
    type: controls
tags: [machine-learning-theory, model-selection, model-capacity]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Hypothesis Space

## Definition
The hypothesis space is the set of functions that a learning algorithm is permitted to select as being the solution to a problem. The choice of hypothesis space imposes constraints on the types of solutions the algorithm can find.

## Role in Controlling Capacity
Choosing the hypothesis space is a primary method for controlling the capacity of a learning algorithm. A more restrictive hypothesis space corresponds to lower capacity, while a larger or more flexible space corresponds to higher capacity. The goal is to choose a hypothesis space that is large enough to contain a good solution but not so large that the model overfits.

## Example with Linear Regression
The linear regression algorithm provides a clear example. Its standard hypothesis space is the set of all linear functions of its input. This space can be expanded to increase the model's capacity. For instance, by including quadratic terms, the hypothesis space is enlarged to include all quadratic functions, allowing the model to fit more complex patterns.

## Relationships

- **controls**: [[model-capacity|Model Capacity]]

---
*Extracted from: Deep+Learning+Ian+Goodfellow*