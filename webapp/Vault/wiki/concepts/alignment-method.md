---
type: concept
aliases: [Alignment Method]
summary: A method in computer vision for determining the pose of a rigid object by aligning features from an image with a known 3D model of the object.
tags: [computer-vision, object-recognition, pose-estimation]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Alignment Method

## Definition
The alignment method is a solution for determining the pose (position and orientation) of a known rigid object with respect to a viewer based on an image. It is applicable to both three-dimensional and two-dimensional objects and is described as a simple and well-defined solution for this problem.

## How It Works
The method represents the object using a set of M distinguished features or points, such as the vertices of a polyhedron, measured in a coordinate system natural to the object. By establishing correspondences between these model points and points in an image, the system can determine the camera parameters that produced the image. This process effectively finds the object's position and orientation.

## Application and Verification
The alignment method has significant applications, such as in industrial manipulation where a robot arm needs to know an object's pose before it can be picked up. The method can also be used to verify a hypothesis that a set of image points corresponds to a specific object model. This is done by using some point correspondences to determine the camera parameters, then projecting other model points into the image and checking if they land near observed image points.

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*