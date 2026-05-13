---
type: concept
aliases: [Random Search]
summary: A hyperparameter tuning technique that samples hyperparameter combinations from a search space, often proving more efficient than grid search.
relationships:
  - target: grid-search
    type: compared_with
  - target: hyperparameter-tuning
    type: is_a
tags: [hyperparameter-tuning, optimization, methodology]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Random Search

## Definition
Random search is a hyperparameter optimization method that explores a search space by randomly sampling a specified number of points. Unlike grid search, it does not test every possible combination from a predefined grid.

## Advantages over Grid Search
Random search is often more efficient and finds good solutions faster than grid search. The primary reason is that it avoids wasted experimental runs. In grid search, if a particular hyperparameter has little impact on the outcome, multiple runs are wasted exploring its different values while other, more important hyperparameters are held constant. In random search, every trial uses a unique combination of all hyperparameters, ensuring a more diverse and independent exploration of the search space, which is particularly beneficial when some hyperparameters are much more influential than others.

## Practical Application
In practice, random search can be an iterative process. An initial random search can be performed to identify promising regions of the hyperparameter space, followed by subsequent, more focused random searches in those regions to refine the solution.

## Relationships

- **compared_with**: [[grid-search|Grid Search]]
- **is_a**: [[hyperparameter-tuning|Hyperparameter Tuning]]

---
*Extracted from: Deep+Learning+Ian+Goodfellow*