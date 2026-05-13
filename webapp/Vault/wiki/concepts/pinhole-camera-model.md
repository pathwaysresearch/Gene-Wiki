---
type: concept
aliases: [Pinhole Camera Model]
summary: A simple model of image formation where light from a scene passes through a single small aperture (the pinhole) to form an inverted, focused image on a plane.
relationships:
  - target: perspective-projection
    type: is-described-by
tags: [computer-vision, image-formation, optics]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Pinhole Camera Model

## Principle of Operation
The pinhole camera is the simplest method for forming a focused image. It consists of a box with a small opening, the pinhole, at the front and an image plane at the back. The model works by ensuring that photons from a specific point in the scene pass through the pinhole and converge at a corresponding point on the image plane, thus creating a focused image of stationary objects.

## Geometric Model
The geometry of the pinhole camera is described using a three-dimensional coordinate system where the origin is located at the pinhole. A point P in the scene with coordinates (X, Y, Z) is projected onto a point P' on the image plane. The distance from the pinhole to the image plane is denoted as 'f'.

## Image Formation Process
The process that maps the 3D scene to the 2D image in this model is known as perspective projection. The relationship between the scene coordinates (X, Y, Z) and the image coordinates (x, y) is defined by the equations derived from similar triangles: x = -fX/Z and y = -fY/Z. This mathematical relationship is fundamental to understanding image formation in computer vision.

## Relationships

- **is-described-by**: [[perspective-projection|Perspective Projection]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*