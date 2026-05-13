---
type: concept
aliases: [Data Interleaving]
summary: A technique in the TensorFlow Data API for reading from multiple data files concurrently by cycling through them and reading one item at a time from each.
relationships:
  - target: tensorflow-data-api
    type: implemented_in
tags: [data-loading, tensorflow, tf-data, performance]
sourced_from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019
---

# Data Interleaving

## Definition

Data interleaving is a method for combining records from multiple datasets, typically files, into a single dataset. In TensorFlow, the `interleave()` method creates a dataset that pulls a specified number of file paths from a source dataset (e.g., a list of filenames) and creates a new sub-dataset for each one (e.g., a `TextLineDataset`). It then cycles through these sub-datasets, reading one line at a time from each in turn.

## Parallel Execution

By default, `interleave()` operates sequentially, reading one line at a time from each file. However, it can be configured to read files in parallel by setting the `num_parallel_calls` argument to the desired number of threads. For dynamic optimization, this can be set to `tf.data.experimental.AUTOTUNE`, which allows TensorFlow to choose the optimal number of threads based on available CPU resources.

## Best Practices

For interleaving to work most effectively, it is preferable to use source files that are of identical or similar length. If file lengths vary significantly, the end of the longest files will not be interleaved with data from other files, as the shorter files will have already been exhausted. This can reduce the randomness and efficiency of the data loading process.

## Relationships

- **implemented_in**: [[tensorflow-data-api|Tensorflow Data Api]]

---
*Extracted from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019*