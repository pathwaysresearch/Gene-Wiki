---
type: entity
aliases: [TensorFlow Datasets (TFDS)]
summary: A Google project and Python library that provides a collection of common machine learning datasets, simplifying the process of downloading and preparing data for use with TensorFlow.
tags: [tensorflow, data-management, machine-learning]
sourced_from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019
---

# TensorFlow Datasets (TFDS)

## Overview
TensorFlow Datasets (TFDS) is a project that makes it trivial to download and use common datasets for machine learning. The library provides access to a wide range of data, including image datasets (from MNIST to ImageNet), text datasets, audio, and video. The full list and descriptions are available on the project's website.

## Installation and Usage
TFDS is not included in the standard TensorFlow installation and must be installed as a separate library, for example, using `pip install tensorflow-datasets`. The primary function is `tfds.load()`, which is called with the name of the desired dataset. This function handles the download process (caching the data for future use) and returns the data as a dictionary of `tf.data.Dataset` objects.

## Data Structure
The data is typically returned already split into sets like 'train' and 'test'. For example, loading the MNIST dataset with `tfds.load(name="mnist")` returns a dictionary containing `mnist_train` and `mnist_test` datasets. These `Dataset` objects can then be directly integrated into a TensorFlow training pipeline, where transformations like batching, repeating, and prefetching can be applied.

---
*Extracted from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019*