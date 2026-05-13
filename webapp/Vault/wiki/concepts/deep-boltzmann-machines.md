---
type: concept
aliases: [Deep Boltzmann Machines]
summary: A deep, undirected probabilistic graphical model with multiple layers of latent variables, used for unsupervised learning and generative modeling.
relationships:
  - target: geoffrey-hinton
    type: developed_by
  - target: ruslan-salakhutdinov
    type: developed_by
  - target: boltzmann-machine
    type: extends
  - target: deep-belief-network
    type: related_to
tags: [deep-learning, generative-model, unsupervised-learning, graphical-model]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Deep Boltzmann Machines

## Overview
Deep Boltzmann Machines (DBMs) are a class of deep generative model introduced in a 2009 paper by Ruslan Salakhutdinov and Geoffrey Hinton. The model's importance is highlighted by its early mention in the text (pages 24, 27) and its extensive, detailed treatment in the later chapters on deep generative models (pages 529, 663, 666, 671, 672).

## Key Principles
As an extension of Boltzmann machines, DBMs consist of a multi-layered, undirected graphical model. The work by Salakhutdinov and Hinton (2009a) provides the foundational principles for this architecture. Further works cited, such as Montavon and Muller (2012) on the "centering trick" (page 673), indicate the text covers both the theory and practical techniques for training DBMs effectively.

## Relationship to Other Models
DBMs are presented in the context of other deep architectures. The text contrasts them with models like Deep Belief Networks (DBNs), which have a different, hybrid directed/undirected structure. The citation of Ranzato and Hinton (2010) on factorized third-order Boltzmann machines (page 680) suggests a discussion of variations and extensions to the basic Boltzmann machine framework.

## Relationships

- **developed_by**: [[geoffrey-hinton|Geoffrey Hinton]]
- **developed_by**: [[ruslan-salakhutdinov|Ruslan Salakhutdinov]]
- **extends**: [[boltzmann-machine|Boltzmann Machine]]
- **related_to**: [[deep-belief-network|Deep Belief Network]]

---
*Extracted from: Deep+Learning+Ian+Goodfellow*