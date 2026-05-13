---
type: concept
aliases: [Fully Convolutional Network (FCN)]
summary: A type of neural network architecture that consists only of convolutional and pooling layers, allowing it to process images of any size.
relationships:
  - target: semantic-segmentation
    type: used-in
tags: [deep-learning, neural-network-architecture, computer-vision]
sourced_from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019
---

# Fully Convolutional Network (FCN)

## Definition
A Fully Convolutional Network (FCN) is a neural network architecture that contains only convolutional layers and pooling layers, with no dense (fully connected) layers. This structure gives it unique properties compared to traditional CNNs with dense layers.

## Key Property
The primary advantage of an FCN is its ability to be trained and executed on images of any size. While a dense layer expects a specific input size because it has one weight per input feature, a convolutional layer can process inputs of varying spatial dimensions as long as the number of channels is consistent. This makes FCNs highly flexible for various computer vision tasks.

## Conversion from CNNs
It is possible to convert a standard CNN with dense layers into an FCN by replacing the dense layers with equivalent convolutional layers. The weights from the original dense layers can be copied to the new convolutional layers, potentially avoiding the need for retraining. This allows a model trained for classification on fixed-size images to be applied to larger images for tasks like object detection or segmentation.

## Relationships

- **used-in**: [[semantic-segmentation|Semantic Segmentation]]

---
*Extracted from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019*