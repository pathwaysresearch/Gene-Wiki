---
type: entity
aliases: [MNIST Dataset]
summary: A widely-used dataset of 70,000 small, grayscale images of handwritten digits, often referred to as the "Hello World" of machine learning for classification tasks.
tags: [dataset, image-classification, benchmark]
sourced_from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019
---

# MNIST Dataset

## Overview
The MNIST dataset is a set of 70,000 small images of digits handwritten by high school students and employees of the US Census Bureau. Each image is labeled with the digit it represents. Due to its extensive use in research and education, it is often called the "Hello World" of Machine Learning, serving as a benchmark for new classification algorithms and a common starting point for learners.

## Data Structure
Each image in the MNIST dataset consists of 28x28 pixels, resulting in 784 features per image. The entire dataset contains 70,000 images, leading to a data array of shape (70000, 784). Correspondingly, there is a target array of shape (70000,) containing the label for each image.

## Loading with Scikit-Learn
Scikit-Learn provides helper functions to download popular datasets, including MNIST. Using `fetch_openml('mnist_784', version=1)`, the dataset can be loaded into a dictionary-like object. This object typically includes a `DESCR` key with a description of the dataset, a `data` key containing the feature array (X), and a `target` key containing the labels array (y).

---
*Extracted from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019*