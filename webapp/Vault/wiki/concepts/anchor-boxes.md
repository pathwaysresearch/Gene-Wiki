---
type: concept
aliases: [Anchor Boxes]
summary: Predefined bounding box shapes of representative sizes and aspect ratios, used in object detection models like YOLO to improve prediction accuracy and training speed.
relationships:
  - target: yolov3
    type: is-used-by
  - target: object-detection
    type: is-a-technique-in
tags: [object-detection, computer-vision, deep-learning]
sourced_from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019
---

# Anchor Boxes

## Definition
Anchor boxes, also referred to as bounding box priors, are a set of representative bounding box dimensions used in object detection systems like YOLOv3. These are not predicted by the network but are determined beforehand based on the typical object shapes in the training data.

## Creation
The dimensions of anchor boxes are found by applying the K-Means clustering algorithm to the heights and widths of all the ground-truth bounding boxes in the training dataset. This process identifies the most common object shapes. For example, if a dataset contains many pedestrians, one of the resulting anchor boxes will likely have dimensions similar to that of a typical pedestrian.

## Role in Prediction
Instead of predicting the absolute dimensions of a bounding box from scratch, the neural network predicts how much to rescale each of the anchor boxes for a given grid cell. The network outputs the log of the vertical and horizontal rescaling factors. This approach makes the network more likely to predict reasonably shaped boxes and speeds up training by providing it with a better starting point for what constitutes a reasonable bounding box.

## Relationships

- **is-used-by**: [[yolov3|Yolov3]]
- **is-a-technique-in**: [[object-detection|Object Detection]]

---
*Extracted from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019*