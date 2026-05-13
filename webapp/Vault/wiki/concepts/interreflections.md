---
type: concept
aliases: [Interreflections]
summary: The phenomenon in computer vision and graphics where surfaces are illuminated not just by primary light sources, but also by light reflected from other surfaces in the scene.
tags: [computer-vision, shading, 3d-reconstruction, illumination]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Interreflections

## Definition
Interreflections, also known as mutual illumination, occur when surfaces in a scene are illuminated by light that has been reflected from other surfaces. These other surfaces effectively act as secondary light sources, a common occurrence in typical indoor scenes.

## The Challenge for Shape from Shading
This effect poses a significant difficulty for algorithms that attempt to determine an object's shape from its shading. The relationship between a surface's normal (its orientation) and its brightness in an image becomes unpredictable. For example, two surface patches with the exact same orientation might have very different brightness levels if one is illuminated by a large white wall while the other faces a dark bookcase.

## Significance in Vision
The effects of interreflections are quite significant. While human perception seems capable of ignoring these effects to get a useful perception of shape from shading, creating algorithms that can do the same has proven to be a frustratingly difficult problem in computer vision.

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*