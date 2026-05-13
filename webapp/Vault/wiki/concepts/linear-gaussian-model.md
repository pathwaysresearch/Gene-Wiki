---
type: concept
aliases: [Linear Gaussian Model]
summary: A model for representing conditional distributions in Bayesian networks where a continuous child variable has a Gaussian distribution whose mean is a linear function of its parents.
relationships:
  - target: bayesian-network
    type: is-a-component-of
tags: [cpt-representation, continuous-variables, bayesian-networks]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Linear Gaussian Model

## Definition
The linear Gaussian model is used to represent the conditional probability distribution of a continuous variable given its parents, which can be discrete or continuous. In this model, the child variable's distribution is a Gaussian (normal) distribution where the mean is a linear function of the values of its parent variables.

## How It Works
For a continuous child variable, its conditional distribution is specified as a normal distribution, $N(\mu, \sigma^2)$. The mean, $\mu$, is defined as a linear combination of its parents' values. For example, if a variable *Cost* depends on a continuous parent *Harvest* and a discrete parent *Subsidy*, the mean cost could be expressed as $a_t h + b_t$ when *Subsidy* is true and $a_f h + b_f$ when it is false. The variance, $\sigma^2$, can also be dependent on the discrete parents.

## Applications and Limitations
This model is useful for representing relationships between continuous variables in domains like economics or engineering. It allows for the creation of hybrid Bayesian networks containing both discrete and continuous variables. A key limitation is that the assumption of linearity is often only a reasonable approximation over a limited range of parent values, as it can otherwise lead to unrealistic predictions (e.g., negative costs or prices).

## Relationships

- **is-a-component-of**: [[bayesian-network|Bayesian Network]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*