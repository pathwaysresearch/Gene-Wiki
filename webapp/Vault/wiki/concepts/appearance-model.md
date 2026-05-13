---
type: concept
aliases: [Appearance Model]
summary: In computer vision, a model that describes the visual characteristics, such as color and texture, of an object or its parts, used in conjunction with structural models for recognition.
relationships:
  - target: deformable-template
    type: component_of
tags: [computer-vision, object-recognition, feature-extraction]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Appearance Model

## Definition
An appearance model is a description of what an object, such as a person, looks like. It is a crucial component in object recognition systems, particularly those using deformable templates or pictorial structure models, where it complements the geometric or structural information.

## Function in Recognition
When matching a structural model (like a "cardboard person") to an image, the appearance model provides the criteria for scoring the similarity between the model's body segments and the corresponding image segments. For example, it might use the average colors for hair, head, torso, and limbs to evaluate the match. This score is combined with a score for the spatial relations between parts to find the best overall match.

## Building the Model
The text describes several strategies for building an appearance model. For a single image, one can start with a poorly tuned model, estimate the object's configuration, use that to re-estimate the appearance, and iterate. In video sequences, where many frames of the same person are available, their appearance can be revealed more easily. Another strategy is to use a detector for a fixed, reliable configuration (like a person walking laterally) to find the person and learn the appearance of their torso, arms, legs, and head from that detection.

## Relationships

- **component_of**: [[deformable-template|Deformable Template]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*