---
type: concept
aliases: [tf.function]
summary: A TensorFlow decorator or function that compiles a Python function into a callable, high-performance TensorFlow graph.
tags: [tensorflow, performance-optimization, graph-mode]
sourced_from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019
---

# tf.function

## Purpose and Benefits
`tf.function` is a transformation tool in TensorFlow that converts a Python function containing TensorFlow operations into a static computation graph. This process, known as 'tracing', allows TensorFlow to perform significant optimizations, such as pruning unused nodes and simplifying expressions. The resulting graph-based function typically executes much faster than the original eager-mode Python code, especially for complex computations, as it can leverage parallel processing and run efficiently on hardware accelerators like GPUs and TPUs.

## Automatic Conversion by Keras
When using Keras, custom functions such as custom loss functions, metrics, or the `call` method of a custom layer or model are automatically converted into TF Functions by default. This means developers often benefit from the performance gains of graph mode without explicitly using the `@tf.function` decorator. This automatic behavior can be disabled by setting `dynamic=True` when creating a custom layer or model, or by setting `run_eagerly=True` in the model's `compile()` method.

## Rules and Limitations
A key rule when writing code intended for `tf.function` is that the TensorFlow graph can only contain TensorFlow constructs (tensors, operations, variables). Any calls to external libraries, like NumPy, or standard Python libraries will only be executed during the initial tracing of the function. They do not become part of the static graph. Therefore, for operations that should be part of the model's computation, TensorFlow equivalents like `tf.reduce_sum()` must be used instead of `np.sum()`.

---
*Extracted from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019*