---
type: concept
aliases: [Model Capacity]
summary: A measure of a machine learning model's ability to fit a wide variety of functions, which influences its tendency to underfit or overfit.
relationships:
  - target: generalization
    type: affects
  - target: hypothesis-space
    type: is_controlled_by
  - target: vc-dimension
    type: is_measured_by
tags: [machine-learning-theory, overfitting, underfitting, model-complexity]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Model Capacity

## Definition
Informally, a model's capacity is its ability to fit a wide variety of functions. It represents the complexity of the patterns a model is able to learn from data. The capacity of a model is a key factor in its ability to generalize to new data.

## The Capacity Trade-Off
Model capacity is central to the trade-off between underfitting and overfitting. Models with low capacity may struggle to fit the training set, resulting in high training error (underfitting). Conversely, models with high capacity can overfit by memorizing properties of the training set, including noise, that do not serve them well on the test set, leading to a large gap between training and generalization error.

## Control and Quantification
One primary way to control the capacity of a learning algorithm is by choosing its hypothesis space—the set of functions it is allowed to select as a solution. For example, increasing the degree of a polynomial regression model increases its capacity. Statistical learning theory provides formal ways to quantify model capacity, with the Vapnik-Chervonenkis (VC) dimension being the most well-known measure for binary classifiers. However, determining the capacity of complex models like deep neural networks is a difficult problem.

## Relationships

- **affects**: [[generalization|Generalization]]
- **is_controlled_by**: [[hypothesis-space|Hypothesis Space]]
- **is_measured_by**: [[vc-dimension|Vc Dimension]]

---
*Extracted from: Deep+Learning+Ian+Goodfellow*