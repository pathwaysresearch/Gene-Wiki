---
type: concept
aliases: [Back-Propagation through Random Operations]
summary: A general method for training generative models by augmenting a deterministic neural network with random inputs, allowing gradients to be computed via standard back-propagation.
relationships:
  - target: back-propagation
    type: extends
  - target: reparameterization-trick
    type: is_also_known_as
tags: [training-algorithm, generative-model, stochastic-networks]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Back-Propagation through Random Operations

## Core Idea
To create a stochastic neural network from a deterministic one, the network can be augmented with extra inputs, \(z\), which are sampled from a simple probability distribution like a uniform or Gaussian distribution. The network then performs a deterministic computation on its standard inputs \(x\) and the random inputs \(z\). The resulting function, \(f(x, z)\), appears stochastic to an observer who does not have access to \(z\).

## Training Mechanism
This formulation allows for gradient-based training using standard back-propagation. Provided that the function \(f\) is continuous and differentiable with respect to its parameters and inputs (including \(z\)), the gradients of a cost function with respect to the model parameters can be computed as usual. This technique effectively reparameterizes the stochasticity, moving it from the network's operations to its inputs.

## Example
An example of this process is generating samples \(y\) from a Gaussian distribution with a learned mean \(\mu\) and variance \(\sigma^2\). Instead of directly sampling from \(\mathcal{N}(\mu, \sigma^2)\), one can sample a noise variable \(\epsilon\) from a standard normal distribution \(\mathcal{N}(0, 1)\) and then compute \(y = \mu + \sigma \epsilon\). This is a deterministic function of \(\mu\), \(\sigma\), and \(\epsilon\), allowing gradients to flow back to \(\mu\) and \(\sigma\).

## Relationships

- **extends**: [[back-propagation|Back Propagation]]
- **is_also_known_as**: [[reparameterization-trick|Reparameterization Trick]]

---
*Extracted from: Deep+Learning+Ian+Goodfellow*