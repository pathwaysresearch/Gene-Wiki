---
type: concept
aliases: [Sparse Interactions]
summary: A property of convolutional networks where each output unit is connected to only a small, local region of the input units, achieved by using kernels that are smaller than the input.
relationships:
  - target: convolutional-network
    type: is_property_of
  - target: convolution
    type: is_a_result_of
tags: [neural-network-properties, computational-efficiency]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Sparse Interactions

## Definition
Sparse interactions, also known as sparse connectivity or sparse weights, is a core principle of convolutional networks. It contrasts with traditional neural network layers that use dense matrix multiplication, where every output unit interacts with every input unit. In a convolutional layer, each output unit is a function of only a small number of input units, creating a sparse connection pattern.

## Mechanism
This property is achieved by making the kernel significantly smaller than the input. For example, when processing an image that might have thousands or millions of pixels, a convolutional layer can detect small, meaningful features like edges using kernels that cover only tens or hundreds of pixels. The small area of the input that an output unit is connected to is sometimes called its receptive field.

## Advantages
Sparse interactions provide several major advantages. First, they reduce the memory requirements of the model because fewer parameters need to be stored. This in turn improves the model's statistical efficiency, as there are fewer parameters to learn from the data. Second, computing the output requires fewer operations, leading to significant improvements in computational efficiency. For certain tasks like edge detection, using convolution can be thousands or even billions of times more efficient, both computationally and in terms of parameter storage, than an equivalent transformation described by a dense matrix.

## Relationships

- **is_property_of**: [[convolutional-network|Convolutional Network]]
- **is_a_result_of**: [[convolution|Convolution]]

---
*Extracted from: Deep+Learning+Ian+Goodfellow*