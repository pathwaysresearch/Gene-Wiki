---
type: concept
aliases: [Generative Adversarial Network]
summary: A generative modeling framework where a generator network and a discriminator network are trained simultaneously in a competitive game.
relationships:
  - target: differentiable-generator-network
    type: uses
  - target: conditional-gan
    type: is_generalized_by
  - target: lapgan
    type: is_a_type_of
tags: [generative-models, adversarial-training]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Generative Adversarial Network

## Definition
A Generative Adversarial Network (GAN) is a framework for training generative models that pairs a differentiable generator network with a discriminator network. The two networks are trained in a zero-sum game.

## Training Process
The training process involves a simultaneous competition between the two networks. The discriminator is trained to correctly classify samples as either real (from the training data) or fake (from the generator). Concurrently, the generator is trained to produce samples that fool the discriminator into believing they are real. The main motivation for this design is that the learning process does not require approximate inference or the approximation of a partition function gradient.

## Convergence and Properties
At convergence, the generator's samples are indistinguishable from the real data, and the discriminator's output is 0.5 for all inputs. After training, the discriminator can be discarded. A notable capability of the GAN training procedure is its ability to fit probability distributions that assign zero probability to the training points themselves. Instead of maximizing the log-probability of data points, the generator learns to trace a manifold of points that resemble the training data.

## Relationships

- **uses**: [[differentiable-generator-network|Differentiable Generator Network]]
- **is_generalized_by**: [[conditional-gan|Conditional Gan]]
- **is_a_type_of**: [[lapgan|Lapgan]]

---
*Extracted from: Deep+Learning+Ian+Goodfellow*