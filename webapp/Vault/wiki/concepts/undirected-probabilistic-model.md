---
type: concept
aliases: [Undirected Probabilistic Model]
summary: A type of structured probabilistic model, also known as a Markov Network, that uses an undirected graph to represent dependencies between random variables.
relationships:
  - target: directed-probabilistic-model
    type: can_be_converted_from
  - target: energy-based-model
    type: is_a_generalization_of
  - target: factor-graph
    type: can_be_represented_by
  - target: inference-in-probabilistic-models
    type: is_a_domain_for
tags: [probabilistic-models, graphical-models, markov-network]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Undirected Probabilistic Model

## Definition and Representation
An undirected probabilistic model defines a probability distribution over a set of variables using an undirected graph. The distribution is specified as a product of non-negative functions, called factors or clique potentials (φ), defined over cliques in the graph. This product of factors forms an unnormalized probability distribution, p̃(x).

## Normalization
To obtain a valid probability distribution, the unnormalized distribution must be divided by a normalization constant, Z, also known as the partition function. Z is calculated by summing or integrating the unnormalized probability over all possible joint assignments of the variables. For many models in deep learning, especially those with continuous variables or complex structures, Z is intractable to compute exactly, necessitating the use of approximate algorithms.

## Conditional Independence
Conditional independence properties in an undirected model are determined by graph separation. A set of variables A is conditionally independent of another set B given a third set S, if observing the variables in S blocks all paths between A and B in the graph. This allows for reading dependency structures directly from the model's graphical representation.

## Relationships

- **can_be_converted_from**: [[directed-probabilistic-model|Directed Probabilistic Model]]
- **is_a_generalization_of**: [[energy-based-model|Energy Based Model]]
- **can_be_represented_by**: [[factor-graph|Factor Graph]]
- **is_a_domain_for**: [[inference-in-probabilistic-models|Inference In Probabilistic Models]]

---
*Extracted from: Deep+Learning+Ian+Goodfellow*