---
type: concept
aliases: [Classification (Machine Learning)]
summary: A common type of machine learning task where a system is trained to assign an input, represented by a feature vector, to one of a predefined set of categories.
tags: [machine-learning, supervised-learning, task-definition]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Classification (Machine Learning)

## Definition
Classification is a common machine learning task where the goal is for a computer program to specify which of *k* categories a given input belongs to. The input is typically an **example**, which is a collection of quantitatively measured **features** represented as a vector $\boldsymbol{x} \in \mathbb{R}^n$. For instance, the features of an image are usually the values of its pixels.

## How It Works
A learning algorithm for classification is tasked with producing a function, $f : \mathbb{R}^n \rightarrow \{1, ..., k\}$. When this function is applied to an input vector $\boldsymbol{x}$, its output $y = f(\boldsymbol{x})$ is a numeric code that identifies the category to which $\boldsymbol{x}$ is assigned. In some variants, the function $f$ might instead output a probability distribution over the possible classes rather than a single category label.

## Example Application
A common example of a classification task is object recognition. In this scenario, the input is an image, which is described as a set of features (e.g., pixel brightness values). The output is a numeric code that identifies the object present in the image. For instance, the Willow Garage PR2 robot uses classification to act as a waiter that can recognize different objects.

---
*Extracted from: Deep+Learning+Ian+Goodfellow*