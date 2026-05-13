---
type: entity
aliases: [MNIST]
summary: The Modified National Institute of Standards and Technology database, a large dataset of handwritten digits commonly used for training and testing machine learning models.
relationships:
  - target: image-classification
    type: used_for
  - target: deep-boltzmann-machine
    type: used_to_evaluate
tags: [dataset, benchmark, computer-vision]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# MNIST

## Overview
The MNIST dataset is a benchmark dataset in the field of machine learning and computer vision. The index indicates it is mentioned or used in the book on pages 20, 21, and 666.

## Role in Deep Learning
As a standard benchmark, MNIST is frequently used to demonstrate the performance of new models and algorithms. Its presence on early pages (20, 21) suggests it is used for introductory examples of machine learning tasks like image classification.

## Application Context
The reference on page 666 connects the MNIST dataset to the context of Deep Boltzmann Machines. This suggests its use in evaluating or demonstrating the capabilities of generative models, in addition to its common use for supervised classification tasks.

## Relationships

- **used_for**: [[image-classification|Image Classification]]
- **used_to_evaluate**: [[deep-boltzmann-machine|Deep Boltzmann Machine]]

---
*Extracted from: Deep+Learning+Ian+Goodfellow*