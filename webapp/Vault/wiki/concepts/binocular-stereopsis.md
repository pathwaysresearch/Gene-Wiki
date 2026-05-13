---
type: concept
aliases: [Binocular Stereopsis]
summary: A process for depth perception that uses two images of the same scene taken from slightly different viewpoints, similar to how predator animals use two forward-facing eyes.
relationships:
  - target: disparity-computer-vision
    type: measures
  - target: correspondence-problem
    type: depends_on
tags: [computer-vision, 3d-vision, depth-perception]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Binocular Stereopsis

## Definition
Binocular stereopsis is a technique for recovering depth from images by using two or more views of a scene separated in space. This method is analogous to motion parallax, which uses images separated in time. It is a key mechanism for depth perception in animals with forward-facing eyes, such as predators.

## Core Principle
The fundamental principle of stereopsis is that a feature in the 3D scene will be projected onto a different horizontal position in each of the two image planes. This difference in position between the left and right images is called disparity. By measuring the disparity for various features, it is possible to calculate their depth relative to the cameras.

## The Correspondence Problem
A critical prerequisite for measuring disparity is solving the correspondence problem. This involves identifying, for a point in the left image, the corresponding point in the right image that is the projection of the same 3D scene point. This is a challenging subproblem that must be solved to enable depth estimation via stereopsis.

## Relationships

- **measures**: [[disparity-computer-vision|Disparity Computer Vision]]
- **depends_on**: [[correspondence-problem|Correspondence Problem]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*