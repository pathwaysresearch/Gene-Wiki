---
type: concept
aliases: [Local Contrast Normalization]
summary: An image preprocessing technique that normalizes contrast within local regions of an image, designed to highlight features like edges and corners that global methods might miss.
relationships:
  - target: contrast-normalization
    type: is-a-type-of
  - target: global-contrast-normalization
    type: is-an-alternative-to
tags: [computer-vision, preprocessing, image-processing]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Local Contrast Normalization

## Motivation
Local contrast normalization is motivated by the limitations of global contrast normalization (GCN). GCN may fail to make features like edges and corners stand out, especially within large regions of uniform brightness or darkness (e.g., an area in shadow).

## Goal
The purpose of local contrast normalization is to enhance features within local neighborhoods of an image. By operating on smaller regions independently, it can highlight details that would be washed out by a global statistical adjustment.

## Application
This technique is useful for tasks where fine-grained details and local structures are important for the model's performance. It addresses the problem where a global method might correctly separate large bright and dark areas but fail to reveal the structure within them.

## Relationships

- **is-a-type-of**: [[contrast-normalization|Contrast Normalization]]
- **is-an-alternative-to**: [[global-contrast-normalization|Global Contrast Normalization]]

---
*Extracted from: Deep+Learning+Ian+Goodfellow*