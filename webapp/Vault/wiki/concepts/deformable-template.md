---
type: concept
aliases: [Deformable Template]
summary: A model used in computer vision to infer the layout of non-rigid objects, such as human bodies, by representing the object as a collection of connected parts.
relationships:
  - target: appearance-model
    type: uses
tags: [computer-vision, object-recognition, human-pose-estimation]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Deformable Template

## Definition
A deformable template is a model used to infer the layout of objects whose parts can move relative to one another, such as the human body. It is particularly useful for tasks that require more detailed information than simply placing a bounding box around an object, like understanding what a person is doing by determining the position of their arms, legs, body, and head.

## Role in Object Recognition
In recognizing complex objects like people, individual body parts (e.g., forearms, shins) can be small and difficult to detect on their own using simple methods like a moving window, due to variations in color, texture, and size. A deformable template provides a powerful representation by encoding what parts are connected to what, allowing the system to use easily found parts to guide the search for smaller, harder-to-detect parts.

## Pictorial Structure Models
A specific type of deformable template is the pictorial structure model. This model evaluates a match between a set of image rectangles and a template (e.g., a "cardboard person") by scoring both the appearance similarity of individual segments and the spatial relationships between them. A good match occurs when image segments have the correct appearance and are positioned correctly relative to each other, with the match often found using dynamic programming.

## Relationships

- **uses**: [[appearance-model|Appearance Model]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*