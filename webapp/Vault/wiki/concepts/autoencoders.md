---
type: concept
aliases: [Autoencoders]
summary: A class of neural networks for representation learning, encompassing variants like undercomplete and regularized models, and analyzed in terms of their representational power, size, and depth.
relationships:
  - target: undercomplete-autoencoders
    type: has_variant
  - target: regularized-autoencoders
    type: has_variant
  - target: representation-learning
    type: is_a_type_of
tags: [neural-networks, representation-learning, unsupervised-learning]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Autoencoders

## Overview
Autoencoders are a major topic in deep learning, presented as the subject of Chapter 14. They are a type of artificial neural network used to learn efficient data representations, typically in an unsupervised manner.

## Key Variants
The text outlines specific categories of autoencoders. These include undercomplete autoencoders, which are discussed in section 14.1, and regularized autoencoders, which are covered in section 14.2. These variants represent different approaches to constraining the network to learn useful features.

## Properties and Architecture
A key part of the discussion on autoencoders involves their fundamental properties and architectural choices. The text dedicates a section to their representational power, as well as the effects of layer size and depth on their performance and ability to learn meaningful representations from data.

## Relationships

- **has_variant**: [[undercomplete-autoencoders|Undercomplete Autoencoders]]
- **has_variant**: [[regularized-autoencoders|Regularized Autoencoders]]
- **is_a_type_of**: [[representation-learning|Representation Learning]]

---
*Extracted from: Deep+Learning+Ian+Goodfellow*