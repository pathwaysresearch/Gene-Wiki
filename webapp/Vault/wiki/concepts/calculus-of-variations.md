---
type: concept
aliases: [Calculus of Variations]
summary: A field of mathematical analysis that deals with maximizing or minimizing functionals, which are mappings from a set of functions to the real numbers, and is a key tool in variational learning.
tags: [mathematics, optimization, functional-analysis]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Calculus of Variations

## Role in Variational Learning
Calculus of variations is introduced as an important set of mathematical tools used in variational learning. Unlike ordinary calculus which finds points that optimize a function, calculus of variations is used to find functions that optimize a functional. This is fundamental to variational inference, which seeks an optimal probability distribution function from within a family of functions.

## Application in Maximum Entropy
The text provides a detailed example of using calculus of variations to find the probability distribution that maximizes entropy subject to constraints on its mean and variance. By setting up a Lagrangian functional and finding its critical points, the method analytically derives that the normal distribution, $\mathcal{N}(x; \mu, \sigma^2)$, is the functional form that maximizes entropy. This demonstrates how the method can derive a distribution's form without prior assumption.

## Deriving Approximating Distributions
This mathematical tool is also applied to derive the functional form of the approximating distribution $q$ in variational inference. By maximizing the evidence lower bound with respect to the function $q$, calculus of variations can determine its optimal form. The text shows an example where this procedure automatically derives that the approximating distribution $\tilde{q}$ must have the functional form of a Gaussian.

---
*Extracted from: Deep+Learning+Ian+Goodfellow*