---
type: concept
aliases: [Generative Adversarial Networks]
summary: A class of machine learning frameworks where two neural networks, a generator and a discriminator (a feedforward classifier), contest with each other in a zero-sum game to generate realistic data.
tags: [generative-models, unsupervised-learning, neural-networks]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Generative Adversarial Networks

## Framework Overview
Generative Adversarial Networks (GANs) are an approach where a generative model is trained to compete against a feedforward classifier, often called a discriminator. The generator's objective is to produce samples that are so realistic they can fool the discriminator, while the discriminator's objective is to distinguish between real samples from the training set and fake samples from the generator.

## The Adversarial Process
The training process is a contest between the two networks. The feedforward classifier attempts to recognize all samples from the generative model as fake and all samples from the training set as real. In response, the generative model is trained to produce samples that the classifier fails to identify as fake. This adversarial dynamic pushes the generator to create increasingly structured and realistic patterns that mimic the true data distribution.

## Application in Learning Salience
GANs provide a powerful method for a model to learn what is salient in data, moving beyond simple metrics like mean squared error which can fail to capture subtle but important features. In the GAN framework, any structured pattern that the feedforward network can recognize is considered highly salient. For example, models trained to generate images of human heads using an adversarial framework can successfully generate features like ears, which might be omitted by models trained with mean squared error because they are not as prominent in terms of pixel brightness or darkness.

---
*Extracted from: Deep+Learning+Ian+Goodfellow*