---
type: concept
aliases: [Correspondence Problem]
summary: A fundamental challenge in computer vision that involves identifying features in different images that are projections of the same feature in the three-dimensional world.
tags: [computer-vision, 3d-vision, feature-matching]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Correspondence Problem

## Definition
The correspondence problem is the task of identifying features in different images that are projections of the same single feature in the three-dimensional world. It is a fundamental challenge that must be addressed in many multi-view computer vision applications.

## Role in Binocular Stereopsis
In binocular stereopsis, solving the correspondence problem is a necessary first step before depth can be computed. One must determine, for a point in the left image, which point in the right image corresponds to the same physical point in the scene. Once this correspondence is established, the disparity can be measured.

## Role in Multiple-View Geometry
The correspondence problem is one of three key subproblems in the general framework of using multiple views to recover 3D shape. The other two subproblems are determining the relative orientation (rotation and translation) between cameras and the final depth estimation. The development of robust matching procedures to solve the correspondence problem has been a major success in the field of computer vision.

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*