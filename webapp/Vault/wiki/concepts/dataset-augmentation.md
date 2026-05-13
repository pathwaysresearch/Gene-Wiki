---
type: concept
aliases: [Dataset Augmentation]
summary: A technique to reduce generalization error by creating additional synthetic training data from existing data through various transformations.
relationships:
  - target: regularization
    type: related_to
tags: [data-preprocessing, generalization, overfitting]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Dataset Augmentation

## Definition and Purpose
Dataset augmentation is a powerful technique used to reduce the generalization error of a machine learning model. It works by artificially enlarging the training dataset by creating modified copies of existing data or generating new synthetic data from it. These transformations are designed to expose the model to a wider variety of input variations, making it more robust and less prone to overfitting.

## Importance in Controlled Experiments
The use of hand-designed dataset augmentation schemes can dramatically improve a model's performance. This makes it a critical variable to control when comparing different machine learning algorithms. To ensure a fair comparison between two algorithms, it is necessary to evaluate both using the exact same augmentation schemes. An apparent performance advantage of one algorithm might actually be due to a more effective set of data transformations it was paired with, rather than the algorithm itself.

## Classification of Augmentation Techniques
A subjective distinction is often made between different types of augmentation. Operations that are generally applicable across many domains, such as adding Gaussian noise to the input, are frequently considered an intrinsic part of the machine learning algorithm itself. In contrast, operations that are highly specific to one application domain, such as randomly cropping or rotating an image, are typically treated as separate, external pre-processing steps.

## Relationships

- **related_to**: [[regularization|Regularization]]

---
*Extracted from: Deep+Learning+Ian+Goodfellow*