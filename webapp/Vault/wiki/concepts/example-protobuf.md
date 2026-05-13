---
type: concept
aliases: [Example Protobuf]
summary: The primary Protocol Buffer message type used within TFRecord files to represent a single data instance, containing a collection of named features.
relationships:
  - target: tfrecord-format
    type: used_by
tags: [protocol-buffers, tensorflow, data-structure]
sourced_from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019
---

# Example Protobuf

## Definition

The `Example` protobuf is the main data structure used in TensorFlow's TFRecord format to represent one instance (or example) in a dataset. It is defined using Protocol Buffers and provides a standardized way to structure features for a single data point.

## Structure

An `Example` message contains a list of named features. Each feature within the `Example` can be one of three types, corresponding to a specific list structure: `BytesList` for a list of byte strings, `FloatList` for a list of floating-point values, and `Int64List` for a list of 64-bit integers. This structure allows for storing various types of data associated with a single training example.

## Flexibility and Use Cases

The `BytesList` feature type is particularly flexible, as it can contain any arbitrary binary data. This allows for storing complex data types within an `Example` proto. For instance, an entire image can be encoded into JPEG format using `tf.io.encode_jpeg()` and the resulting byte string can be stored in a `BytesList`. Similarly, any TensorFlow tensor can be serialized using `tf.io.serialize_tensor()` and stored in the same way, to be parsed later with `tf.io.parse_tensor()`.

## Relationships

- **used_by**: [[tfrecord-format|Tfrecord Format]]

---
*Extracted from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019*