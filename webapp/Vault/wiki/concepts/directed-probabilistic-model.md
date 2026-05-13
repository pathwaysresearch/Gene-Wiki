---
type: concept
aliases: [Directed Probabilistic Model]
summary: A type of structured probabilistic model, also known as a Bayesian Network, that uses a directed acyclic graph to represent conditional dependencies between random variables.
relationships:
  - target: undirected-probabilistic-model
    type: can_be_converted_to
  - target: d-separation
    type: uses
  - target: moralization
    type: is_an_input_to
  - target: inference-in-probabilistic-models
    type: is_a_domain_for
tags: [probabilistic-models, graphical-models, bayesian-network]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Directed Probabilistic Model

## Overview
A directed probabilistic model, or directed graphical model, represents a probability distribution over a set of variables using a directed graph. The structure of the graph encodes conditional independence assumptions, making it a powerful tool for representing complex distributions efficiently. No probabilistic model is inherently directed or undirected; rather, it is a choice of description language.

## Conditional Independence and d-Separation
Conditional independences in a directed model are determined by a criterion called d-separation. Two sets of variables are considered d-separated if there are no "active paths" between them, given a set of observed variables. The rules for determining if a path is active are more complicated than simple graph separation in undirected models and depend on the direction of the edges and whether nodes along the path are observed.

## Comparison and Conversion
Neither directed nor undirected models are universally superior; the best choice depends on which representation can more compactly capture the independences of a given probability distribution using the fewest edges. It is possible to convert a directed model to an undirected one through a process called moralization, which can sometimes result in the loss of some independence information.

## Relationships

- **can_be_converted_to**: [[undirected-probabilistic-model|Undirected Probabilistic Model]]
- **uses**: [[d-separation|D Separation]]
- **is_an_input_to**: [[moralization|Moralization]]
- **is_a_domain_for**: [[inference-in-probabilistic-models|Inference In Probabilistic Models]]

---
*Extracted from: Deep+Learning+Ian+Goodfellow*