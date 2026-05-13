---
type: concept
aliases: [Scaled Orthographic Projection]
summary: An approximation of perspective projection used for distant objects with little depth variation, where the scaling factor due to distance is treated as a constant.
relationships:
  - target: perspective-projection
    type: is-an-approximation-of
tags: [computer-vision, 3d-graphics, image-formation]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Scaled Orthographic Projection

## Definition
Scaled orthographic projection is a simplified projection model that serves as an approximation to perspective projection. It is valid in scenarios where perspective effects are not pronounced, such as when viewing objects where the variation in depth is small compared to the overall distance from the camera.

## The Approximation
The model is based on the assumption that if the depth Z of points on an object varies within a small range $Z_0 \pm \Delta Z$ (where $\Delta Z$ is much less than $Z_0$), the perspective scaling factor $1/Z$ can be approximated by a constant, $s = 1/Z_0$. This effectively treats all points on the object as being at the same distance for scaling purposes.

## Projection Equations and Applications
Under scaled orthographic projection, the complex equations of perspective projection simplify to x = sX and y = sY. This model is only a valid approximation for parts of a scene with minimal internal depth variation. A common example is modeling the features on the front of a distant building, where the difference in distance to various points on the facade is negligible compared to the building's total distance from the viewer.

## Relationships

- **is-an-approximation-of**: [[perspective-projection|Perspective Projection]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*