---
type: concept
aliases: [Contrast Normalization]
summary: A type of image preprocessing designed to remove variations in contrast, which is the magnitude of the difference between bright and dark pixels in an image.
relationships:
  - target: preprocessing
    type: is-a-type-of
  - target: global-contrast-normalization
    type: has-subtype
  - target: local-contrast-normalization
    type: has-subtype
tags: [computer-vision, preprocessing, image-processing]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Contrast Normalization

## Definition
Contrast normalization is a preprocessing technique applied to images to remove a common source of variation: the amount of contrast. In the context of deep learning, contrast refers to the magnitude of the difference between the bright and dark pixels. Removing this variation can simplify the learning task for a model.

## Rationale
This technique is based on the assumption that the overall contrast level of an image is not relevant to the underlying recognition task. By standardizing the contrast, the model does not need to learn to be invariant to these changes, which can reduce generalization error and the required model size.

## Types
There are different methods for performing contrast normalization. The text distinguishes between global contrast normalization, which considers the image as a whole, and local contrast normalization, which operates on local regions of the image to highlight features like edges and corners.

## Relationships

- **is-a-type-of**: [[preprocessing|Preprocessing]]
- **has-subtype**: [[global-contrast-normalization|Global Contrast Normalization]]
- **has-subtype**: [[local-contrast-normalization|Local Contrast Normalization]]

---
*Extracted from: Deep+Learning+Ian+Goodfellow*