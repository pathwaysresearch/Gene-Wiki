---
type: concept
aliases: [Lambert's Cosine Law]
summary: A principle stating that the brightness of a diffuse surface is proportional to the cosine of the angle between the light source direction and the surface normal.
tags: [computer-vision, computer-graphics, shading, physics]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Lambert's Cosine Law

## Definition
Lambert's cosine law describes the relationship between the orientation of a diffuse surface and its apparent brightness. It posits that the brightness of a surface patch is determined by the intensity of the light source, the material properties of the surface, and the angle at which the light strikes the surface.

## The Formula
The law is expressed mathematically as $I = p I_0 \cos \theta$. In this equation, 'I' is the resulting image brightness, 'p' is the diffuse albedo (a property of the surface), $I_0$ is the intensity of the light source, and $\theta$ is the angle between the direction of the light source and the surface normal vector.

## Application in Shape from Shading
This principle is a crucial cue for inferring 3D shape from 2D image shading. The law predicts that surface patches that directly face the light source (where $\theta$ is small and $\cos \theta$ is high) will appear bright. Conversely, patches that are illuminated at a grazing angle (where $\theta$ is large and $\cos \theta$ is low) will appear dark. Analyzing these shading variations allows a vision system to deduce information about the surface's shape.

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*