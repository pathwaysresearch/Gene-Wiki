---
type: entity
aliases: [FitNets]
summary: A deep learning training approach where a shallow, wide 'teacher' network guides the training of a deeper, thinner 'student' network by providing intermediate-level hints.
relationships:
  - target: supervised-pretraining
    type: is-an-example-of
tags: [deep-learning-model, training-strategy, knowledge-distillation]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# FitNets

## Overview
FitNets is a training approach, described by Romero et al. (2015), designed to facilitate the training of deep and thin neural networks, which are often difficult to optimize with standard methods. The core concept is a teacher-student paradigm where a simpler network helps train a more complex one.

## Teacher-Student Architecture
The method involves two networks. First, a 'teacher' network is trained, which is designed to be shallow and wide, making it relatively easy to train. This teacher network then guides the training of a 'student' network, which is much deeper and thinner and would be difficult to train under normal circumstances.

## Hint-Based Training
The key innovation in FitNets is the use of hints from the teacher to aid the student's learning. The student network is trained not only to predict the final output for the original task but also to predict the value of a middle layer of the teacher network. This additional task provides a set of hints about how the hidden layers should be used, which simplifies the optimization problem for the deep student network.

## Relationships

- **is-an-example-of**: [[supervised-pretraining|Supervised Pretraining]]

---
*Extracted from: Deep+Learning+Ian+Goodfellow*