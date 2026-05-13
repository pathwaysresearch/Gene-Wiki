---
type: concept
aliases: [Intersection over Union (IoU)]
summary: A common evaluation metric for object detection tasks that measures the overlap between a predicted bounding box and a ground-truth bounding box.
relationships:
  - target: object-detection
    type: is-metric-for
tags: [computer-vision, object-detection, evaluation-metric]
sourced_from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019
---

# Intersection over Union (IoU)

## Definition
Intersection over Union (IoU) is a standard metric used to evaluate how well a model can predict bounding boxes in tasks like object detection. It is considered a better evaluation metric for this purpose than a cost function like Mean Squared Error (MSE) which might be used for training.

## Calculation
The IoU is calculated as the area of the intersection (the overlapping region) between the predicted bounding box and the target bounding box, divided by the area of their union (the total area covered by both boxes combined). A higher IoU value indicates a better prediction, with 1 representing a perfect match and 0 representing no overlap.

## Implementation
In the TensorFlow Keras library, the Intersection over Union metric is implemented by the `tf.keras.metrics.MeanIoU` class, which can be used during model compilation and evaluation.

## Relationships

- **is-metric-for**: [[object-detection|Object Detection]]

---
*Extracted from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019*