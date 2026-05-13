---
type: concept
aliases: [Global Contrast Normalization]
summary: An image preprocessing technique that standardizes the contrast across an entire image, but may fail to highlight local features in scenes with large, uniformly lit or dark areas.
relationships:
  - target: contrast-normalization
    type: is-a-type-of
  - target: whitening
    type: is-related-to
tags: [computer-vision, preprocessing, image-processing]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Global Contrast Normalization

## Definition
Global Contrast Normalization (GCN) is a preprocessing method that adjusts the contrast of an image based on statistics computed over the entire image. One form of GCN, also known as sphering or whitening, transforms the data so that each input feature has zero mean and equal variance.

## How It Works
As illustrated in the provided text, GCN can map input data points onto a sphere, effectively removing variations in their norm. A regularized version of GCN can draw examples toward this sphere without completely discarding all norm information.

## Limitations
GCN can fail to highlight important image features like edges and corners in certain scenarios. For example, in an image with a large dark area and a large bright area, GCN will ensure a significant difference between the two main areas but may not enhance the visibility of edges within the dark region itself. This limitation motivates the use of local contrast normalization.

## Relationships

- **is-a-type-of**: [[contrast-normalization|Contrast Normalization]]
- **is-related-to**: [[whitening|Whitening]]

---
*Extracted from: Deep+Learning+Ian+Goodfellow*