---
type: concept
aliases: [Background Subtraction]
summary: A technique in computer vision for detecting moving objects by subtracting a static background image from the current video frame.
tags: [computer-vision, video-analysis, motion-detection]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Background Subtraction

## Definition
Background subtraction is a well-understood method used to detect objects, particularly people, in a video stream. The technique works by subtracting a pre-recorded background image from the current frame.

## How It Works
The core principle is that if the absolute value of the difference between the current frame and the background image is large at a particular pixel, it indicates the presence of a foreground object that was not in the background. This method is effective for detecting objects that are relatively small in the video frame.

## Conditions for Use
A key requirement for background subtraction to be effective is that the background must be stable. It is a foundational technique for applications like surveillance and human activity analysis where the camera is stationary and the background does not change significantly.

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*