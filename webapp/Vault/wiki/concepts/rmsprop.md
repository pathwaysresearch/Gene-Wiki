---
type: concept
aliases: [RMSProp]
summary: An adaptive learning rate optimization algorithm that modifies AdaGrad by using an exponentially decaying average of squared gradients to prevent the learning rate from monotonically decreasing.
relationships:
  - target: adagrad
    type: is_an_improvement_on
tags: [optimization-algorithm, adaptive-learning-rate]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# RMSProp

## Definition
RMSProp is an adaptive learning rate algorithm designed to resolve the diminishing learning rate problem of AdaGrad. It allows the learning rate to adapt based on recent gradient information rather than the entire history.

## How It Works
Like AdaGrad, RMSProp scales the learning rate based on the magnitude of gradients. However, instead of accumulating all past squared gradients, it uses an exponentially decaying moving average. This mechanism discards history from the distant past, preventing the accumulated sum from growing indefinitely. This allows the algorithm to adapt its learning rate and converge rapidly even after finding a convex-bowl-like structure where AdaGrad's learning rate would have become too small.

## Hyperparameters
Compared to AdaGrad, RMSProp introduces a new hyperparameter, `rho`, which controls the length scale or decay rate of the moving average of squared gradients. This parameter determines how much weight is given to recent versus past gradients in the learning rate adaptation.

## Relationships

- **is_an_improvement_on**: [[adagrad|Adagrad]]

---
*Extracted from: Deep+Learning+Ian+Goodfellow*