---
type: concept
aliases: [Histogram of Gradient Orientations (HOG)]
summary: A feature descriptor used in computer vision for object detection, which counts occurrences of gradient orientation in localized portions of an image.
tags: [computer-vision, object-detection, feature-descriptor]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Histogram of Gradient Orientations (HOG)

## Definition
The Histogram of Gradient orientations (HOG) is a feature descriptor used in computer vision, particularly for object detection tasks like pedestrian detection. The feature is constructed by dividing an image window into a grid of small spatial regions called cells, and for each cell, compiling a histogram of gradient orientations for the pixels within that cell.

## Feature Construction
To build the HOG feature, the contribution of each pixel's gradient orientation to its cell's histogram is weighted. A common weighting scheme uses the gradient magnitude at a pixel relative to the sum of all gradient magnitudes within the cell. This method gives greater weight to gradients that are strong compared to their local neighbors, enhancing the feature's distinctiveness.

## Application in Object Detection
HOG features are central to many object detection systems. A typical detector works by sweeping a window of a fixed size across an image at various scales. For each window, it computes the HOG feature and passes it to a trained classifier to determine if the object of interest (e.g., a pedestrian) is present. The final output is often refined using non-maximum suppression to eliminate multiple detections of the same object.

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*