---
type: concept
aliases: [Tangent Propagation]
summary: A regularization technique that encourages a model's output to be invariant to known transformations of the input by penalizing the derivatives of the output with respect to those transformations.
relationships:
  - target: regularization
    type: is_a_type_of
  - target: dataset-augmentation
    type: related_to
tags: [regularization, invariance, neural-networks]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Tangent Propagation

## Definition
Tangent propagation is a regularization method that analytically encourages a model to be robust against known transformations of the input that should not alter the output. Instead of generating new data points, it regularizes the model by penalizing the gradient of the model's output with respect to infinitesimal perturbations along the directions (tangents) of these transformations.

## Relationship to Dataset Augmentation
This technique is closely related to dataset augmentation, as both methods encode prior knowledge about task invariances into the model. The key difference is the scale of the transformation. Dataset augmentation explicitly trains the model on new, distinct inputs created by applying finite, often large, transformations. Tangent propagation, in contrast, is an analytical approach that only regularizes the model to resist infinitesimal perturbations.

## Limitations
Tangent propagation has two major drawbacks described in the text. First, its focus on infinitesimal changes means it confers less resistance to larger perturbations compared to explicit dataset augmentation. Second, the analytical approach poses difficulties for models based on rectified linear units (ReLUs). Unlike sigmoid or tanh units, which can shrink their derivatives by saturating, ReLUs can only reduce their derivatives by turning off or shrinking their weights, which limits the effectiveness of this regularization method. Dataset augmentation works well with ReLUs because different transformed inputs can activate different subsets of units.

## Relationships

- **is_a_type_of**: [[regularization|Regularization]]
- **related_to**: [[dataset-augmentation|Dataset Augmentation]]

---
*Extracted from: Deep+Learning+Ian+Goodfellow*