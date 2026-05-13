---
type: concept
aliases: [Variational Approximation]
summary: An approximation method that simplifies complex probabilistic calculations by finding a simpler, parameterized problem that closely resembles the original.
tags: [approximation-methods, probabilistic-inference, statistics]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Variational Approximation

## Definition
Variational approximation methods are a family of techniques used to simplify complex calculations. The fundamental idea is to propose a reduced, simplified version of the original problem that is easier to work with, while ensuring it resembles the original problem as closely as possible.

## How It Works
The reduced problem is described by a set of variational parameters, denoted as λ. These parameters are adjusted to minimize a distance function, D, which measures the dissimilarity between the original and the reduced problem. This optimization is often performed by solving the system of equations ∂D / ∂λ = 0. In many applications, this approach can yield strict upper and lower bounds on the true value being approximated.

## Applications and Variants
Variational methods have a long history of use in statistics. A specific and important variant is the mean-field method, which originated in statistical physics and assumes that the individual variables in the model are completely independent. This technique has been successfully applied to solve large undirected Markov networks and to derive accurate lower-bound approximations for Bayesian networks, such as sigmoid networks.

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*