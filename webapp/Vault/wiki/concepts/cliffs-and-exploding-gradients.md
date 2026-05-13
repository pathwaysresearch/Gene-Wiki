---
type: concept
aliases: [Cliffs and Exploding Gradients]
summary: A phenomenon in deep or recurrent neural networks where the cost function surface has extremely steep regions, causing gradient updates to move parameters drastically and disrupt learning.
relationships:
  - target: stochastic-gradient-descent
    type: affects
tags: [optimization-challenge, gradient-based-optimization, recurrent-neural-networks]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Cliffs and Exploding Gradients

## Definition
Neural networks with many layers, particularly highly nonlinear deep networks or recurrent neural networks, often have objective functions with extremely steep regions that resemble cliffs. These sharp nonlinearities in parameter space are the result of multiplying several large weights together, which gives rise to very high derivatives, or exploding gradients, in certain places.

## Impact on Gradient Descent
When an optimization algorithm's parameter trajectory approaches a cliff, a single gradient update step can move the parameters an extremely large distance. This can effectively catapult the parameters far away from the current region, potentially jumping off the cliff structure altogether. Such a large, uncontrolled step can undo most of the optimization work that had been previously accomplished, severely disrupting the training process.

## Visualization
The problem is illustrated in the text by a figure adapted from Pascanu et al. (2013), which shows a 3D plot of a cost function with a mostly flat region leading to a sudden, steep drop. The path of an optimization algorithm is shown approaching the cliff, where a single large gradient step sends the parameters far away, demonstrating how this structure can derail learning.

## Relationships

- **affects**: [[stochastic-gradient-descent|Stochastic Gradient Descent]]

---
*Extracted from: Deep+Learning+Ian+Goodfellow*