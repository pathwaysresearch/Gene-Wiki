---
type: concept
aliases: [Edge Detection]
summary: A computer vision technique for identifying points in a digital image where image brightness changes sharply, corresponding to the boundaries of objects.
tags: [computer-vision, image-processing]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Edge Detection

## Definition
Edge detection is a process in computer vision that identifies locations in an image where the brightness undergoes a sharp change. These locations typically correspond to the edges of objects. The output of an edge-detection algorithm is often a set of curves or lines, but this output can be imperfect, containing gaps where edges were missed or 'noise' edges that do not correspond to significant features in the scene.

## How It Works
A straightforward approach to finding edges is to differentiate the image and look for places where the magnitude of the derivative is large. A sharp change in brightness results in a peak in the derivative. However, this method is highly sensitive to noise present in the image, which can cause numerous spurious peaks that are not true edges.

## Improving Robustness with Smoothing
To counteract the effects of noise, a common practice is to smooth the image before applying the differentiation step. Smoothing the image intensity profile diminishes the spurious peaks caused by noise, making the peaks corresponding to true edges more distinct and easier to detect. This combined operation of smoothing and differentiation can be performed in a single step by convolving the image with the derivative of a smoothing kernel, such as a Gaussian ($I * G'_{\sigma}$).

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*