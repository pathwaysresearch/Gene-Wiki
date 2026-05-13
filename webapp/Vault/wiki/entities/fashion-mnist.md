---
type: entity
aliases: [Fashion MNIST]
summary: A dataset of 28x28 grayscale images of 10 fashion categories, used as a common benchmark for machine learning models.
relationships:
  - target: keras
    type: is_accessible_via
tags: [dataset, image-classification, benchmark]
sourced_from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019
---

# Fashion MNIST

## Overview
Fashion MNIST is a dataset comprising grayscale images of 10 different types of clothing and accessories. It is used in the text as a practical example for building and training an image classification MLP. It is noted as one of the common datasets that Keras can fetch and load directly.

## Data Format and Loading
When loaded using the `keras.datasets.fashion_mnist.load_data()` utility, the dataset is pre-split into a training set (60,000 images) and a test set (10,000 images). A key difference from loading with Scikit-Learn is that each image is represented as a 28×28 NumPy array, not a flattened 1D array. The pixel intensities are stored as integers (dtype 'uint8') ranging from 0 to 255.

## Preprocessing Steps
The text outlines the necessary preprocessing steps before using Fashion MNIST to train a neural network. First, a validation set is created by partitioning the full training set (e.g., using the first 5,000 samples). Second, because the network will be trained with Gradient Descent, the input features must be scaled. A simple and effective scaling method shown is to divide all pixel intensities by 255.0, which scales them to the 0-1 range and converts their data type to float.

## Relationships

- **is_accessible_via**: [[keras|Keras]]

---
*Extracted from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019*