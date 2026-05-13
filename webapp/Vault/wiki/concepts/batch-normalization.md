---
type: concept
aliases: [Batch Normalization]
summary: A technique used in deep neural networks to standardize the inputs of a layer for each mini-batch, which stabilizes and accelerates training.
tags: [deep-learning, regularization, optimization, neural-network-layers]
sourced_from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019
---

# Batch Normalization

## How It Works During Training

During training, a Batch Normalization (BN) layer standardizes its inputs for each mini-batch, and then rescales and offsets them. This process involves four parameter vectors that are learned for each BN layer. The output scale vector (γ) and the output offset vector (β) are learned through regular backpropagation. The final input mean vector (μ) and the final input standard deviation vector (σ) are estimated during training, typically using a moving average of the layer's input means and standard deviations from each batch.

## Behavior During Inference

At test time, making predictions for individual instances poses a challenge, as there is no batch to compute input means and standard deviations from. Even with a small batch, the statistics might be unreliable. The solution is to use the 'final' statistics (μ and σ) that were estimated and saved during training. The Keras implementation handles this distinction with a `training` argument in its `call()` method, which behaves differently during training versus inference.

## Significance and Context

Batch Normalization has become one of the most widely used layers in deep neural networks, to the point that its inclusion is often assumed after every layer in modern architectures. However, recent research has explored alternatives. For example, a paper by Hongyi Zhang et al. demonstrated that a novel weight initialization technique called 'fixup' could successfully train very deep networks (10,000 layers) without using Batch Normalization, achieving state-of-the-art results.

---
*Extracted from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019*

---
*Also referenced in: Deep+Learning+Ian+Goodfellow*