---
type: concept
aliases: [Restricted Boltzmann Machines (RBMs)]
summary: An undirected probabilistic graphical model, also known as a harmonium, with a bipartite structure consisting of one layer of visible variables and one layer of latent variables.
relationships:
  - target: boltzmann-machines
    type: is_a_variant_of
tags: [generative-models, graphical-models, unsupervised-learning]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Restricted Boltzmann Machines (RBMs)

## Definition and Origin
Restricted Boltzmann Machines (RBMs), originally invented under the name 'harmonium', are described as one of the most common building blocks of deep probabilistic models. They are a specific type of Boltzmann machine with structural constraints.

## Bipartite Structure
An RBM is an undirected probabilistic graphical model with a distinct bipartite graph structure. It contains a layer of observable (visible) variables and a single layer of latent (hidden) variables. The key restriction is that no connections are permitted between any two variables within the same layer; connections only exist between visible and hidden units.

## Role in Deep Models
RBMs are fundamental components for building more complex architectures. The text explicitly states that RBMs can be stacked one on top of another. This stacking process is used to form deeper models, such as Deep Belief Networks.

## Relationships

- **is_a_variant_of**: [[boltzmann-machines|Boltzmann Machines]]

---
*Extracted from: Deep+Learning+Ian+Goodfellow*