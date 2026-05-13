---
type: concept
aliases: [Curse of Dimensionality]
summary: The phenomenon where various problems arise when analyzing and organizing data in high-dimensional spaces, such as data sparsity and counter-intuitive geometric properties.
tags: [machine-learning-theory, dimensionality, data-analysis]
sourced_from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019
relationships:
  - target: linear-regression
    type: is_mitigated_by
  - target: manifold-hypothesis
    type: mitigated_by
---

# Curse of Dimensionality

## Definition
The curse of dimensionality refers to the fact that many aspects of data analysis and machine learning behave very differently and become more difficult in high-dimensional spaces compared to low-dimensional ones.

## Proximity to Borders
In high-dimensional spaces, most data points are very close to the border of the data space. The text gives an example that in a 10,000-dimensional unit hypercube, the probability of a randomly chosen point being very close to a border is greater than 99.999999%, unlike in a 2D unit square where this is highly unlikely.

## Distance Between Points
Another counter-intuitive effect is that the average distance between any two random points in a high-dimensional space becomes very large. For instance, the average distance between two random points in a unit square is about 0.52, but in a 1,000,000-dimensional unit hypercube, it grows to approximately 408.25. This sparsity makes distance-based algorithms less effective and predictions less reliable.

---
*Extracted from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019*

---
*Also referenced in: Deep+Learning+Ian+Goodfellow*

---
*Also referenced in: The Book Of Why  The New Science Of Cause And Effect ( Pdfdrive )*