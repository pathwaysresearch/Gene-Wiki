---
type: concept
aliases: [Energy-Based Model]
summary: A type of undirected probabilistic model where the probability of a configuration is defined via an energy function, with lower energy states corresponding to higher probabilities.
relationships:
  - target: undirected-probabilistic-model
    type: is_a_special_case_of
tags: [probabilistic-models, undirected-models, deep-learning]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Energy-Based Model

## Definition
An energy-based model (EBM) is a specific kind of undirected model that defines an unnormalized probability distribution using an energy function, E(x). The probability of a state x is proportional to the exponent of the negative energy of that state.

## Relationship to Undirected Models
EBMs are a special case of Markov networks. The relationship is established by defining the clique potential functions (φ) as the exponential of the negative energy terms associated with each clique. For example, a potential φ(a, b) can be set to exp(-E(a, b)). The total energy is a sum of per-clique energy functions, which corresponds to a product of clique potentials due to the property exp(a+b) = exp(a)exp(b).

## Interpretation as Product of Experts
An energy-based model with multiple terms in its energy function can be interpreted as a "product of experts," as proposed by Hinton (1999). In this view, each term in the energy function, corresponding to a factor in the probability distribution, acts as an "expert" that contributes to the overall model's definition of the distribution.

## Relationships

- **is_a_special_case_of**: [[undirected-probabilistic-model|Undirected Probabilistic Model]]

---
*Extracted from: Deep+Learning+Ian+Goodfellow*