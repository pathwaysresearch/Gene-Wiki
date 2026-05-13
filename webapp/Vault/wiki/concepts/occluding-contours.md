---
type: concept
aliases: [Occluding Contours]
summary: Lines in a 2D image or drawing, such as an object's outline, that represent the boundary where a 3D surface turns away from the viewer, providing a strong cue for 3D shape.
tags: [computer-vision, 3d-perception, line-drawing-interpretation]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Occluding Contours

## Definition
Occluding contours are a type of generic constraint used to perceive three-dimensional shape and layout from two-dimensional line drawings. They typically appear as the outlines of objects, such as the outlines of hills in a landscape drawing.

## Role in 3D Perception
The key information provided by an occluding contour is the relative depth of the surfaces it separates. One side of the contour is understood to be nearer to the viewer, while the other side is farther away. This helps establish the 3D structure of the scene from a simple 2D representation.

## Additional Cues
Along with the basic near/far distinction, other features associated with occluding contours, such as local convexity and symmetry, can provide further cues for interpreting the 3D shape of the object being depicted. These constraints contribute to the vivid perception of 3D shape that humans experience when viewing line drawings.

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*