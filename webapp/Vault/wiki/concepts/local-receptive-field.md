---
type: concept
aliases: [Local Receptive Field]
summary: A fundamental concept in both neuroscience and convolutional neural networks, referring to the specific, limited region of the input space (e.g., visual field or previous layer) that a neuron responds to.
relationships:
  - target: convolutional-layer
    type: inspired
  - target: pooling-layer
    type: inspired
  - target: david-h-hubel
    type: discovered_by
  - target: torsten-wiesel
    type: discovered_by
tags: [neuroscience, computer-vision, cnn-architecture]
sourced_from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019
---

# Local Receptive Field

## Definition
A local receptive field is the limited region of an input space to which a single neuron is connected and to which it will react to stimuli. In biological systems, this refers to a region of the visual field; in artificial neural networks, it refers to a small patch of neurons in the preceding layer.

## Origin in Neuroscience
The concept was a key finding from the 1958 and 1959 experiments by David H. Hubel and Torsten Wiesel on the visual cortex of cats. They discovered that many neurons in the visual cortex would only activate in response to visual stimuli within a small, specific area. They also noted that the receptive fields of different neurons often overlap, and together they cover the entire visual field. This organization allows for the detection of local features like edges and lines.

## Application in Convolutional Neural Networks
This biological principle is a core design element of convolutional and pooling layers in CNNs. Instead of connecting every neuron to every neuron in the previous layer (a fully connected layer), neurons in a convolutional layer are only connected to a small rectangular group of neurons in the layer before it. This architectural choice drastically reduces the number of parameters in the network, making it more computationally efficient and less prone to overfitting, while enabling the detection of local patterns in the input data.

## Relationships

- **inspired**: [[convolutional-layer|Convolutional Layer]]
- **inspired**: [[pooling-layer|Pooling Layer]]
- **discovered_by**: [[david-h-hubel|David H Hubel]]
- **discovered_by**: [[torsten-wiesel|Torsten Wiesel]]

---
*Extracted from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019*