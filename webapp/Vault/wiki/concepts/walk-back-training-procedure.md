---
type: concept
aliases: [Walk-Back Training Procedure]
summary: A training method for denoising autoencoders that accelerates generative training convergence by using multiple encode-decode steps and penalizing reconstructions.
relationships:
  - target: generalized-denoising-autoencoder
    type: is_training_method_for
  - target: denoising-autoencoder
    type: is_training_method_for
  - target: contrastive-divergence
    type: related_to
tags: [training-algorithm, generative-model, autoencoder]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Walk-Back Training Procedure

## Purpose and Origin
The walk-back training procedure was proposed by Bengio et al. (2013c) as a method to speed up the convergence when training denoising autoencoders to be generative. It addresses the challenge of efficiently training these models to learn the underlying data distribution for generation tasks.

## How It Works
Instead of performing a standard one-step encode-decode reconstruction, the walk-back procedure consists of multiple, alternative stochastic encode-decode steps. This sequence of steps forms a generative Markov chain that is initialized at a given training example. The training objective involves penalizing the probabilistic reconstructions generated at the end of this chain, or alternatively, all of the reconstructions generated along the way.

## Relationship to Other Algorithms
The procedure shares similarities with the contrastive divergence algorithm, particularly in its initialization from a training example. By running a multi-step Markov chain starting from the data, it aims to train the model to have the correct stationary distribution. For example, a Generative Stochastic Network (GSN) can be trained with this procedure to perform tasks like conditional generation, as shown by resampling one half of an MNIST digit while clamping the other half.

## Relationships

- **is_training_method_for**: [[generalized-denoising-autoencoder|Generalized Denoising Autoencoder]]
- **is_training_method_for**: [[denoising-autoencoder|Denoising Autoencoder]]
- **related_to**: [[contrastive-divergence|Contrastive Divergence]]

---
*Extracted from: Deep+Learning+Ian+Goodfellow*