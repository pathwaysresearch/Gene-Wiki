---
type: concept
aliases: [No Free Lunch Theorem]
summary: A theorem in machine learning stating that no single model is universally the best for all problems, and the choice of model depends on the assumptions made about the data.
tags: [machine-learning-theory, model-selection]
sourced_from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019
relationships:
  - target: generalization
    type: is_related_to
---

# No Free Lunch Theorem

## Core Principle
The No Free Lunch (NFL) theorem, based on a 1996 paper by David Wolpert, states that if you make absolutely no assumptions about your data, there is no reason to prefer one model over any other. For some datasets a linear model is best, while for others a neural network is superior.

## The Importance of Assumptions
Models are simplified versions of observations, and creating them requires making assumptions to decide what data to keep and what to discard as noise. For instance, a linear model assumes the data is fundamentally linear. The NFL theorem formalizes the idea that without such assumptions, no model is a priori guaranteed to work better.

## Practical Implications
Since evaluating every possible model is not feasible, practitioners must make reasonable assumptions about the data to select a few candidate models to evaluate. For example, one might try linear models with various levels of regularization for simple tasks and various neural networks for complex problems. The only way to know for sure which model is best for a specific dataset is to evaluate them.

---
*Extracted from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019*

---
*Also referenced in: Deep+Learning+Ian+Goodfellow*