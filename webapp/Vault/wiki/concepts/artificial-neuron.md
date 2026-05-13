---
type: concept
aliases: [Artificial Neuron]
summary: A simple computational model of a biological neuron, proposed by McCulloch and Pitts, with one or more binary inputs and a single binary output that activates when a threshold of active inputs is met.
relationships:
  - target: warren-mcculloch
    type: developed_by
  - target: walter-pitts
    type: developed_by
tags: [neural-networks, computational-model]
sourced_from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019
---

# Artificial Neuron

## Definition
The artificial neuron, as proposed by Warren McCulloch and Walter Pitts, is a very simple model of a biological neuron. It serves as the fundamental computational unit within an artificial neural network.

## How It Works
This model features one or more binary (on/off) inputs and a single binary output. The neuron's activation rule is straightforward: it activates its output, sending an "on" signal, only when more than a certain number of its inputs are simultaneously active.

## Computational Power
McCulloch and Pitts demonstrated that even with such a simplified model, it is possible to construct a network of these artificial neurons that can compute any logical proposition. For instance, by configuring the connections and activation thresholds, one can build networks that perform logical operations like AND, OR, and identity functions.

## Relationships

- **developed_by**: [[warren-mcculloch|Warren Mcculloch]]
- **developed_by**: [[walter-pitts|Walter Pitts]]

---
*Extracted from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019*