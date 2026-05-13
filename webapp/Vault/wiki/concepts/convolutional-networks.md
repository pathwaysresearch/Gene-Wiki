---
type: concept
aliases: [Convolutional Networks]
summary: A class of deep neural networks specialized for processing data with a grid-like topology, such as images, which were instrumental in the popularization of deep learning.
tags: [deep-learning, neural-networks, computer-vision]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Convolutional Networks

## Overview
Convolutional networks, also known as ConvNets or CNNs, are a type of deep learning model designed to specialize neural networks for data that has a clear grid-structured topology. They were among the first working deep networks to be successfully trained with back-propagation. Their success was pivotal in carrying the torch for the rest of deep learning and paving the way for the general acceptance of neural networks.

## Historical Success
The precise reasons for the early success of convolutional networks, at a time when general fully connected networks were considered to have failed, are not definitively known. One hypothesis is that they were more computationally efficient than fully connected networks, which made it easier for researchers to run multiple experiments and tune their implementations and hyperparameters. It is also possible that the larger networks enabled by this efficiency were simply easier to train. Whatever the case, their strong performance decades ago was a critical catalyst for the field.

## Key Purpose
The primary function of convolutional networks is to provide an effective way to scale neural network models to work with data that has a grid-like structure. This specialization makes them exceptionally well-suited for tasks involving images (which can be seen as a 2D grid of pixels) and other forms of grid-structured data.

---
*Extracted from: Deep+Learning+Ian+Goodfellow*