---
type: concept
aliases: [Tensor (TensorFlow)]
summary: The primary, immutable data structure in TensorFlow, representing a multi-dimensional array of numerical data used for all computations.
relationships:
  - target: tensorflow
    type: core_component_of
  - target: tensorflow-variable
    type: related_to
tags: [data-structure, tensorflow, computation]
sourced_from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019
---

# Tensor (TensorFlow)

## Definition
A TensorFlow Tensor (`tf.Tensor`) is the core data structure used in the library. It is a multi-dimensional array, conceptually similar to a NumPy array, that holds the data for computations within a TensorFlow model or graph.

## Operations
Tensors support a rich set of mathematical operations. Standard Python operators like `+`, `-`, `*`, and `@` (for matrix multiplication, equivalent to `tf.matmul()`) are overloaded to work directly on tensors. The API also provides a wide range of functions analogous to those in NumPy, such as `tf.square()`, `tf.exp()`, `tf.reshape()`, and reduction operations like `tf.reduce_mean()` and `tf.reduce_sum()`.

## Immutability and NumPy Interoperability
A key characteristic of `tf.Tensor` objects is that they are immutable; their values cannot be changed after creation. They interact well with NumPy, and many operations have similar counterparts, though some naming conventions and behaviors differ. For example, in TensorFlow `tf.transpose(t)` is used to transpose a tensor, whereas in NumPy one might use the `t.T` attribute.

## Relationships

- **core_component_of**: [[tensorflow|Tensorflow]]
- **related_to**: [[tensorflow-variable|Tensorflow Variable]]

---
*Extracted from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019*