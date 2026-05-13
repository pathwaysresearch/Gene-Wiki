---
type: concept
aliases: [Disparity (Computer Vision)]
summary: The difference in image location of the same 3D point when projected onto two different images, typically from a stereo camera pair.
relationships:
  - target: correspondence-problem
    type: depends_on
tags: [computer-vision, 3d-vision, depth-perception]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Disparity (Computer Vision)

## Definition
In the context of binocular vision, disparity refers to the difference in the image location of a single 3D scene feature when it is projected onto two different image planes (e.g., from a left and a right camera). If the two images are superimposed, disparity is the measurable shift between the feature's position in one image versus the other. For example, the nearest point of a pyramid will appear shifted to the left in the right image and to the right in the left image.

## Role in Depth Perception
Disparity is the primary cue used to determine depth in binocular stereopsis. The magnitude of the disparity is inversely related to the depth of the object; closer objects exhibit greater disparity than objects that are farther away. Measuring disparity is therefore the central computational step in recovering 3D structure from stereo images.

## Measurement Challenge
To measure disparity, one must first solve the correspondence problem: for a given point in one image, the corresponding point in the other image that arises from the same scene point must be located. Simple approaches to solving this problem involve comparing blocks of pixels around a point in one image to find the best match in the other image.

## Relationships

- **depends_on**: [[correspondence-problem|Correspondence Problem]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*