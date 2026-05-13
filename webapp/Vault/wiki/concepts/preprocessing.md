---
type: concept
aliases: [Preprocessing]
summary: The practice of applying transformations to both training and test data to put examples into a more canonical form, reducing variation and potentially improving model performance and efficiency.
tags: [data-preparation, feature-engineering]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Preprocessing

## Goal and Benefits
The primary goal of preprocessing is to reduce the amount of variation in the input data that a model needs to account for. By transforming data into a more standard format, preprocessing can reduce generalization error and decrease the size of the model required to fit the training set. Simpler tasks may be solved by smaller models, and simpler solutions are more likely to generalize well.

## Design Principle
Preprocessing techniques are typically designed by a human to remove specific kinds of variability in the input that are considered irrelevant to the task. For example, in image recognition, variations in overall brightness or contrast might be removed.

## Modern Context
The necessity of extensive, hand-designed preprocessing has diminished with the advent of large datasets and large models. When sufficient data is available, it is often better to let a large model learn which kinds of variability it should become invariant to on its own. For instance, the AlexNet system used only a single, simple preprocessing step: subtracting the mean pixel value across the training set.

---
*Extracted from: Deep+Learning+Ian+Goodfellow*