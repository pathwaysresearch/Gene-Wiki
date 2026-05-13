---
type: concept
aliases: [TFRecord Format]
summary: TensorFlow's preferred binary file format for storing large amounts of data and reading it efficiently, particularly when data loading and parsing is a training bottleneck.
relationships:
  - target: example-protobuf
    type: uses
tags: [data-format, tensorflow, data-storage, performance]
sourced_from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019
---

# TFRecord Format

## Overview

The TFRecord format is a simple record-oriented binary format designed for efficient storage and reading of large datasets in TensorFlow. It is particularly useful when the training process is bottlenecked by loading and parsing data from less efficient formats like CSV. TFRecords are well-suited for handling large or complex data structures, such as images or audio.

## Structure

A TFRecord file is a sequence of binary records. Each record typically contains a serialized `Example` protocol buffer. The `Example` protobuf is a flexible data structure that represents a single instance in a dataset. It contains a dictionary of named features, where each feature can be a list of byte strings (`BytesList`), a list of floats (`FloatList`), or a list of 64-bit integers (`Int64List`).

## Usage and Parsing

To use TFRecords, data must first be converted into `Example` protos and then written to a TFRecord file. The `BytesList` feature is highly versatile and can store any binary data, including serialized tensors (via `tf.io.serialize_tensor()`) or JPEG-encoded images (via `tf.io.encode_jpeg()`). When reading the data, a `tf.data.TFRecordDataset` is used to stream the records. The serialized `Example` protos are then parsed using TensorFlow operations like `tf.io.parse_single_example()` for individual records or `tf.io.parse_example()` for batches.

## Relationships

- **uses**: [[example-protobuf|Example Protobuf]]

---
*Extracted from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019*