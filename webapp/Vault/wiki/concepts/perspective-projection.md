---
type: concept
aliases: [Perspective Projection]
summary: The process by which a three-dimensional scene is projected onto a two-dimensional image plane, where the size of an object's image is inversely proportional to its distance from the camera.
relationships:
  - target: pinhole-camera-model
    type: describes
  - target: scaled-orthographic-projection
    type: is-approximated-by
tags: [computer-vision, 3d-graphics, image-formation]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Perspective Projection

## Definition
Perspective projection is the image-formation process that mathematically describes how a 3D scene is mapped onto a 2D image plane, as exemplified by the pinhole camera model. It defines the geometric relationship between points in the world and their corresponding points in an image.

## Mathematical Formulation
Using a coordinate system with the origin at the camera's pinhole, a point in the scene at (X, Y, Z) is projected to a point (x, y) on the image plane. The governing equations are x = -fX/Z and y = -fY/Z, where 'f' is the distance from the pinhole to the image plane. The negative signs indicate that the image is inverted.

## Key Property and Ambiguity
A fundamental characteristic of perspective projection is the scaling effect caused by the distance 'Z' in the denominator of the equations. This means that the farther an object is from the camera, the smaller its image will be. This property can create ambiguity, as a small nearby object may project an image of the same size as a large, distant object.

## Relationships

- **describes**: [[pinhole-camera-model|Pinhole Camera Model]]
- **is-approximated-by**: [[scaled-orthographic-projection|Scaled Orthographic Projection]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*