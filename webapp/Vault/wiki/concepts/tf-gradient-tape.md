---
type: concept
aliases: [tf.GradientTape]
summary: A TensorFlow API context manager used to record operations for automatic differentiation, allowing for the computation of gradients.
relationships:
  - target: custom-training-loop
    type: is_used_in
tags: [tensorflow, automatic-differentiation, training]
sourced_from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019
---

# tf.GradientTape

## Overview
`tf.GradientTape` is a core TensorFlow API for automatic differentiation. It operates as a context manager that records operations executed within its scope onto a 'tape'. TensorFlow can then play this tape backward to compute the gradients of a target (like a loss) with respect to a set of sources (like a model's trainable variables) using reverse-mode autodiff.

## Usage and Behavior
To use it, one wraps the forward pass computation inside a `with tf.GradientTape() as tape:` block. After the block, the `tape.gradient(target, sources)` method is called to compute the gradients. By default, the tape is automatically erased immediately after `gradient()` is called, so attempting to call it a second time will raise a `RuntimeError`. To compute multiple gradients, the tape must be made persistent by instantiating it with `tf.GradientTape(persistent=True)`, and it must be manually deleted with `del tape` when no longer needed to free up resources.

## Watched Tensors
By default, `tf.GradientTape` only tracks operations that involve `tf.Variable` objects (i.e., trainable weights). If you need to compute gradients with respect to a non-variable tensor, such as a `tf.constant` or the model's input, you must explicitly instruct the tape to 'watch' that tensor. Otherwise, calling `tape.gradient()` with respect to these tensors will return `None`.

## Relationships

- **is_used_in**: [[custom-training-loop|Custom Training Loop]]

---
*Extracted from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019*