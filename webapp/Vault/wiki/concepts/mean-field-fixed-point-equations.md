---
type: concept
aliases: [Mean Field Fixed Point Equations]
summary: An iterative optimization technique for fast variational inference that finds a local maximum by repeatedly solving for one variable at a time while holding others fixed.
tags: [optimization, variational-inference, iterative-methods]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Mean Field Fixed Point Equations

## Definition
Mean field fixed point equations are a technique used to rapidly estimate the parameters of a mean field approximating distribution in variational inference. Instead of using gradient descent, this approach seeks a local maximum of the objective function $\mathcal{L}(\boldsymbol{v}, \boldsymbol{\theta}, \boldsymbol{h})$ where the gradient with respect to the latent variables $\boldsymbol{h}$ is zero.

## How It Works
The method operates by iteratively solving for a single variable at a time. For each variable $h_i$, the equation $\frac{\partial}{\partial h_i} \mathcal{L}(\boldsymbol{v}, \boldsymbol{\theta}, \boldsymbol{\hat{h}}) = 0$ is solved while holding all other variables $\boldsymbol{\hat{h}}_{-i}$ fixed. This process is repeated in a cycle for all variables $i = 1, \dots, m$ until a convergence criterion is met. This provides a fast alternative to solving for all of $\boldsymbol{h}$ simultaneously.

## Convergence and Updates
Common convergence criteria for the iterative process include stopping when a full cycle of updates fails to improve the objective function $\mathcal{L}$ by more than a tolerance amount, or when the parameter vector $\boldsymbol{\hat{h}}$ no longer changes significantly. While this method updates one unit at a time, the text also mentions a heuristic called 'damping' that can be used to perform block updates, where all units are moved a small step in their individually optimal directions.

---
*Extracted from: Deep+Learning+Ian+Goodfellow*