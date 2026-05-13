---
type: concept
aliases: [Online Learning]
summary: A machine learning paradigm where data arrives sequentially and the model is updated incrementally for each new data point, adapting to changes over time.
tags: [machine-learning, sequential-learning, adaptive-systems]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
relationships:
  - target: batch-learning
    type: is_contrasted_with
  - target: learning-rate
    type: has_parameter
---

# Online Learning

## Motivation and Context
Online learning is a machine learning approach designed for scenarios where the standard assumption of independent and identically distributed (i.i.d.) data does not hold. This assumption is often too strong for real-world applications where data can change over time. Online learning addresses the challenge of making predictions when the future may not resemble the past.

## How It Works
The process of online learning is inherently sequential. The text describes the workflow as follows: an agent receives an input $x_j$, makes a prediction for the corresponding output $y_j$, and is then provided with the correct answer. The model learns and updates itself based on this single instance before moving on to the next input, $x_{j+1}$. This allows the model to adapt to evolving data distributions without needing to be retrained on the entire history of data.

## Contrast with Batch Learning
This method stands in contrast to batch learning, where a model is trained on a complete, static dataset. The online approach is essential when it is computationally infeasible to store and retrain on all past data, or when the underlying data-generating process is non-stationary.

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*

---
*Also referenced in: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019*