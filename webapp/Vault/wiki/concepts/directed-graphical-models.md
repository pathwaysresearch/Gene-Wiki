---
type: concept
aliases: [Directed Graphical Models]
summary: A type of structured probabilistic model that uses a directed acyclic graph to represent conditional dependencies and a factorization of a joint probability distribution.
relationships:
  - target: structured-probabilistic-models
    type: is_a
tags: [graphical-models, bayesian-networks, probabilistic-models]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Directed Graphical Models

## Definition
Directed graphical models are a type of structured probabilistic model that uses a graph with directed edges to represent a probability distribution. Each node in the graph corresponds to a random variable in the distribution.

## Factorization of Probability
These models represent a factorization of the joint probability distribution into a product of conditional probability distributions. The joint distribution $p(\text{x})$ over all variables is expressed as a product of the conditional probability of each variable $x_i$ given its parents in the graph, denoted $\text{Pa}_{\mathcal{G}}(x_i)$.

## Mathematical Formulation
The factorization represented by a directed graphical model is given by the formula:
$p(\text{x}) = \prod_i p(x_i | \text{Pa}_{\mathcal{G}}(x_i))$.
This formula shows that the value of a variable is directly influenced only by its parent variables, encoding conditional independence assumptions that simplify the model.

## Relationships

- **is_a**: [[structured-probabilistic-models|Structured Probabilistic Models]]

---
*Extracted from: Deep+Learning+Ian+Goodfellow*