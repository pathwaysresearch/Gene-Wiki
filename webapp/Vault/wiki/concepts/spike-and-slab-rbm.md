---
type: concept
aliases: [Spike and Slab RBM]
summary: A type of Restricted Boltzmann Machine that uses binary 'spike' units and real-valued 'slab' units to model input data covariance.
relationships:
  - target: restricted-boltzmann-machine
    type: is_a
  - target: contrastive-divergence
    type: uses
tags: [generative-model, rbm-variant, covariance-modeling]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Spike and Slab RBM

## Definition
The spike and slab RBM (ssRBM) is a variant of the Restricted Boltzmann Machine that models the covariance of input data through a specialized hidden layer architecture. It is defined by an energy function that incorporates two distinct types of hidden variables to control the presence and intensity of features.

## Architecture
The ssRBM features two sets of hidden units for each feature component. The first is a set of binary 'spike' units (\(\mathbf{h}\)), which act as switches. The second is a set of real-valued 'slab' units (\(\mathbf{s}\)), which determine the magnitude or intensity. A component, defined by a weight matrix column \(W_{:,i}\), is included in the input model only if its corresponding spike unit \(h_i\) is active (\(h_i = 1\)). If active, the corresponding slab variable \(s_i\) modulates the intensity of that component.

## How It Works
This architecture allows the model to capture complex data covariances. The spike variable \(h_i\) determines whether a particular feature or component is present at all. When a spike is active, the associated slab variable \(s_i\) adds variance to the input along the axis defined by the weight vector \(W_{:,i}\). This mechanism provides a flexible way to model the covariance structure of the inputs. The model can be trained effectively using methods like contrastive divergence and persistent contrastive divergence with Gibbs sampling.

## Relationships

- **is_a**: [[restricted-boltzmann-machine|Restricted Boltzmann Machine]]
- **uses**: [[contrastive-divergence|Contrastive Divergence]]

---
*Extracted from: Deep+Learning+Ian+Goodfellow*