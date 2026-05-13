---
type: concept
aliases: [Saddle Points]
summary: A type of critical point in a function's landscape that is a minimum along some dimensions and a maximum along others, which can significantly slow down gradient-based optimization.
relationships:
  - target: local-minima
    type: related_to
tags: [optimization-challenge, non-convex-optimization, cost-function-landscape]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Saddle Points

## Proliferation in High Dimensions
In the high-dimensional, non-convex optimization landscapes of neural networks, saddle points are believed to be a more significant challenge than local minima. Theoretical and empirical evidence suggests that the loss functions of real neural networks contain a proliferation of high-cost saddle points. This is a critical feature of the optimization problem that training algorithms must navigate.

## Theoretical and Empirical Evidence
Early theoretical work by Baldi and Hornik (1989) on shallow linear autoencoders showed they possess saddle points but no high-cost local minima. More recent work has reinforced this view for more complex models. Dauphin et al. (2014) showed experimentally that real neural networks have loss functions with very many high-cost saddle points, and Choromanska et al. (2014) provided further theoretical arguments for this phenomenon in related classes of high-dimensional random functions.

## Implications for Optimization
The prevalence of saddle points has major implications for first-order optimization algorithms that rely solely on gradient information. Near a saddle point, the gradient can become very small, causing the algorithm to slow down or stop, even though a direction of descent exists. This makes navigating the cost surface much more difficult than simply avoiding local minima.

## Relationships

- **related_to**: [[local-minima|Local Minima]]

---
*Extracted from: Deep+Learning+Ian+Goodfellow*