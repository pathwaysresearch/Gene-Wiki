---
type: concept
aliases: [Data Prefetching]
summary: A performance optimization technique in data input pipelines where the next batch of data is prepared while the current batch is being processed by the model.
relationships:
  - target: tensorflow-data-api
    type: implemented_in
tags: [performance-optimization, tensorflow, tf-data, gpu-utilization]
sourced_from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019
---

# Data Prefetching

## Purpose and Performance Impact

Data prefetching is a crucial technique for optimizing the training speed of machine learning models. It addresses the bottleneck that occurs when the model's processing unit (e.g., a GPU) has to wait for the CPU to load and prepare the next batch of data. By prefetching, the data pipeline works in parallel to the training step, ensuring that the next batch is ready as soon as the model finishes with the current one. This can dramatically improve performance and lead to almost 100% GPU utilization.

## How It Works

In the TensorFlow Data API, prefetching is enabled by calling the `prefetch()` method at the end of the pipeline. Calling `prefetch(1)` creates a dataset that will attempt to always stay one batch ahead of the training algorithm. While the model is executing a training step on one batch, the dataset will be working in parallel to prepare the next batch.

## Usage in TensorFlow

The common practice is to call `prefetch(1)` at the end of the dataset pipeline definition. While prefetching a single batch is generally sufficient, in some cases prefetching more may be beneficial. TensorFlow also provides `tf.data.experimental.AUTOTUNE` as an argument to `prefetch()`, which allows the framework to dynamically determine the optimal number of batches to prefetch.

## Relationships

- **implemented_in**: [[tensorflow-data-api|Tensorflow Data Api]]

---
*Extracted from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019*