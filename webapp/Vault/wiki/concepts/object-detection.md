---
type: concept
aliases: [Object Detection]
summary: A computer vision task that involves identifying and localizing multiple objects within an image by drawing bounding boxes around them.
relationships:
  - target: intersection-over-union
    type: uses-metric
  - target: semantic-segmentation
    type: related-to
  - target: yolov3
    type: is-example-of
  - target: anchor-boxes
    type: uses-technique
tags: [computer-vision, deep-learning, image-processing]
sourced_from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019
---

# Object Detection

## Definition
The task of classifying and localizing multiple objects within a single image is called object detection. It extends single-object classification and localization to more complex scenes where several distinct objects may be present, such as multiple flowers in one picture.

## Traditional Approach
Until a few years ago, a common approach to object detection was to take a Convolutional Neural Network (CNN) trained to classify and locate a single object and then slide it across the image. For example, an image could be divided into a grid, and the CNN would be applied to all possible sub-regions (e.g., all 3x3 regions) to find objects.

## Modern Systems
Modern object detection systems like YOLOv3 provide more integrated and efficient solutions. The choice of a detection system depends on various factors such as speed, accuracy, training time, and complexity. The ultimate goal is to produce a set of bounding boxes, each with a corresponding class label, for all objects of interest in an image.

## Relationships

- **uses-metric**: [[intersection-over-union|Intersection Over Union]]
- **related-to**: [[semantic-segmentation|Semantic Segmentation]]
- **is-example-of**: [[yolov3|Yolov3]]
- **uses-technique**: [[anchor-boxes|Anchor Boxes]]

---
*Extracted from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019*