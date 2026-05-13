---
type: concept
aliases: [Adam Optimizer]
summary: An adaptive learning rate optimization algorithm that computes individual adaptive learning rates for different parameters from estimates of first and second moments of the gradients.
relationships:
  - target: rmsprop
    type: builds_on
  - target: momentum-optimization
    type: builds_on
tags: [optimization-algorithm, adaptive-learning-rate]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Adam Optimizer

## Definition
Adam is an optimization algorithm that combines the ideas of momentum and RMSProp. It computes adaptive learning rates for each parameter by using estimates of both the first moment (the mean, like momentum) and the second moment (the uncentered variance, like RMSProp) of the gradients.

## How It Works
Adam maintains two moving averages for each parameter: an exponentially decaying average of past gradients (the first moment estimate, `s`) and an exponentially decaying average of past squared gradients (the second moment estimate, `v`). The parameter update is then calculated using these two estimates, effectively providing a per-parameter learning rate that is also influenced by the consistent direction of the gradient.

## Hyperparameters
The algorithm requires several hyperparameters: a step size `epsilon` (with a suggested default of 0.001), exponential decay rates for the moment estimates `rho1` and `rho2` (with suggested defaults of 0.9 and 0.999, respectively), and a small constant `delta` for numerical stabilization. The text notes that the choice of optimization algorithm often depends on the user's familiarity with tuning these hyperparameters.

## Relationships

- **builds_on**: [[rmsprop|Rmsprop]]
- **builds_on**: [[momentum-optimization|Momentum Optimization]]

---
*Extracted from: Deep+Learning+Ian+Goodfellow*