---
type: entity
aliases: [YOLOv3]
summary: An object detection system known for its speed and accuracy, which uses techniques like anchor boxes and multi-scale training.
relationships:
  - target: object-detection
    type: is-an-implementation-of
  - target: anchor-boxes
    type: uses
tags: [object-detection, deep-learning-model, computer-vision]
sourced_from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019
---

# YOLOv3

## Overview
YOLOv3 ("You Only Look Once" version 3) is a well-known object detection system. It is presented as an example of a modern approach to classifying and localizing multiple objects in an image.

## Key Techniques
YOLOv3 incorporates several important techniques. Before training, it uses the K-Means algorithm on the training set's bounding box dimensions to find representative shapes called anchor boxes. Instead of predicting bounding box dimensions directly, the network predicts rescaling factors for these anchor boxes, which improves training stability and prediction quality.

## Multi-Scale Training
A significant feature of YOLOv3 is its training methodology using images of different scales. During training, the network randomly chooses a new image dimension every few batches (from 330 × 330 to 608 × 608 pixels). This strategy enables the trained model to effectively detect objects at various scales in new images and allows the model itself to be used at different input resolutions to trade off speed and accuracy.

## Relationships

- **is-an-implementation-of**: [[object-detection|Object Detection]]
- **uses**: [[anchor-boxes|Anchor Boxes]]

---
*Extracted from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019*