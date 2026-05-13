---
type: concept
aliases: [Expressive Power of Deep Networks]
summary: The concept that deep neural networks, particularly those with rectifier or maxout units, can represent complex functions with exponentially more linear regions compared to shallow networks.
relationships:
  - target: maxout-unit
    type: applies_to
tags: [deep-learning-theory, neural-networks, network-architecture]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Expressive Power of Deep Networks

## Geometric Intuition
The expressive power of deep networks with certain activation functions can be understood through a geometric interpretation of "folding" the input space. For instance, an absolute value rectification unit creates a mirror axis of symmetry defined by its weights and bias. A function computed by a subsequent layer is then a mirror image across this axis, effectively folding the space. Each additional layer can add another fold, creating more complex, repeating patterns with each layer.

## Exponential Advantage of Depth
A key theoretical result is that depth allows for an exponential increase in the number of linear regions a network can represent. As shown by Montufar et al. (2014), the number of linear regions carved out by a deep rectifier network is exponential in the depth of the network ($l$). This demonstrates that deep networks can be much more efficient at representing certain families of functions than shallow ones with the same number of parameters.

## Quantitative Bounds
For a deep rectifier network with $d$ inputs, depth $l$, and $n$ units per hidden layer, the number of linear regions is on the order of $O((\frac{n}{d})^{d(l-1)} n^d)$. For maxout networks with $k$ filters per unit, the number of linear regions is on the order of $O(k^{(k^{l-1}-1)+d})$. Both of these bounds formally show an exponential dependence on the network's depth, quantifying the expressive advantage of deep architectures.

## Relationships

- **applies_to**: [[maxout-unit|Maxout Unit]]

---
*Extracted from: Deep+Learning+Ian+Goodfellow*