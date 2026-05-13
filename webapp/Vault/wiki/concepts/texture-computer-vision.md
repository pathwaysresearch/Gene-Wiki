---
type: concept
aliases: [Texture (Computer Vision)]
summary: A property of a multi-pixel image patch referring to a spatially repeating visual pattern on a surface, which can be periodic or statistical.
tags: [computer-vision, image-features]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Texture (Computer Vision)

## Definition
In computational vision, texture refers to a spatially repeating pattern on a surface that is visually perceivable. Unlike brightness, which is a property of a single pixel, texture is a characteristic of a multi-pixel patch. Examples include periodic patterns like stitches on a sweater and statistically regular patterns like pebbles on a beach.

## Characterization using Orientation Histograms
A texture within an image patch can be characterized by computing the orientation at each pixel and then creating a histogram of these orientations. The shape of this histogram reveals the nature of the texture. For instance, the texture of a brick wall would produce a histogram with two distinct peaks (one for vertical and one for horizontal orientations), whereas the texture of a leopard's spots would result in a more uniform distribution of orientations.

## Key Properties
A significant advantage of using orientation-based features to describe texture is their invariance to changes in illumination. This robustness makes texture an important and reliable clue for various computer vision tasks, such as image segmentation and object recognition.

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*