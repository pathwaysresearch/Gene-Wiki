---
type: concept
aliases: [Semantic Segmentation]
summary: A computer vision task where each pixel in an image is classified according to the class of the object it belongs to, without distinguishing between different instances of the same class.
relationships:
  - target: object-detection
    type: related-to
  - target: skip-connections
    type: uses-technique
tags: [computer-vision, image-processing, deep-learning]
sourced_from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019
---

# Semantic Segmentation

## Definition
In semantic segmentation, the goal is to classify each pixel in an image according to the class of the object it belongs to. For example, every pixel that is part of a car would be labeled 'car', every pixel of the road 'road', and so on, resulting in a pixel-level map of the image's contents.

## Distinction from Object Detection
A key characteristic of semantic segmentation is that it does not distinguish between different objects of the same class. For example, if an image contains multiple bicycles, the output segmentation map will simply show one large region of pixels classified as 'bicycle', rather than identifying each bicycle as a separate instance.

## Technical Challenges and Solutions
A primary difficulty in this task is the gradual loss of spatial resolution that occurs as an image passes through a regular CNN, due to layers with strides greater than one. This makes it hard for the network to make precise, pixel-level predictions. A common solution to recover this lost detail is to use an upsampling network architecture that incorporates skip connections, which bring fine-grained information from earlier, higher-resolution layers to the later, upsampling layers.

## Relationships

- **related-to**: [[object-detection|Object Detection]]
- **uses-technique**: [[skip-connections|Skip Connections]]

---
*Extracted from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019*