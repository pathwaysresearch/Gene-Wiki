---
type: concept
aliases: [Conditional GAN]
summary: An extension of the Generative Adversarial Network framework that learns to generate samples from a conditional probability distribution p(x|y).
relationships:
  - target: generative-adversarial-network
    type: is_a_type_of
  - target: lapgan
    type: is_used_in
tags: [generative-models, adversarial-training, conditional-models]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Conditional GAN

## Definition
A Conditional GAN (Mirza and Osindero, 2014) is a type of Generative Adversarial Network that is trained to learn a conditional distribution. Instead of sampling from a marginal distribution $p(\boldsymbol{x})$, it learns to sample from $p(\boldsymbol{x} | \boldsymbol{y})$, where $\boldsymbol{y}$ is some conditioning information.

## How It Works
Both the generator and the discriminator in a Conditional GAN are conditioned on the variable $\boldsymbol{y}$. The generator receives both a random noise vector $z$ and the conditioning variable $\boldsymbol{y}$ as input, and must generate a sample $\boldsymbol{x}$ that is plausible given $\boldsymbol{y}$. The discriminator receives both a sample (either real or fake) and the conditioning variable $\boldsymbol{y}$, and must determine if the sample is real given that condition.

## Applications
This framework allows for more controlled generation. For example, a series of conditional GANs can be trained to incrementally add detail to an image. The LAPGAN model uses this technique, where one GAN generates a low-resolution image, and subsequent conditional GANs add higher-resolution details, conditioned on the output of the previous stage.

## Relationships

- **is_a_type_of**: [[generative-adversarial-network|Generative Adversarial Network]]
- **is_used_in**: [[lapgan|Lapgan]]

---
*Extracted from: Deep+Learning+Ian+Goodfellow*