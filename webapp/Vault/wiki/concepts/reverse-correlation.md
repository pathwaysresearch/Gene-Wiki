---
type: concept
aliases: [Reverse Correlation]
summary: An experimental neuroscience technique used to approximate a biological neuron's weights by fitting a linear model to its activation responses to white noise stimuli.
relationships:
  - target: gabor-function
    type: is_used_to_discover
  - target: david-hubel
    type: builds_on_work_of
  - target: torsten-wiesel
    type: builds_on_work_of
tags: [neuroscience, computational-neuroscience, vision]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Reverse Correlation

## Overview

Reverse correlation is a technique used in computational neuroscience to analyze the function and properties of individual biological neurons. Unlike in an artificial neural network where weights are directly accessible, the internal weights of a biological neuron cannot be directly inspected. Reverse correlation provides a method to infer an approximation of these weights, particularly for neurons in the early visual system like those in the V1 cortex.

## Methodology

The experimental procedure for reverse correlation involves placing an electrode into a neuron to record its activity. The animal is then shown a series of random stimuli, typically samples of white noise images, projected onto its retina. For each image sample, the resulting activation or firing rate of the neuron is recorded. After collecting a sufficient number of stimulus-response pairs, a linear model is fit to the data to estimate the neuron's weights, effectively creating a map of its receptive field.

## Key Findings

The application of reverse correlation to simple cells in the V1 visual cortex has revealed that the weights of most of these neurons are well-described by Gabor functions. This finding provides a strong neuroscientific parallel to the types of edge and orientation detectors that are learned by the filters in the first layer of a convolutional neural network, helping to ground the design of these models in biological principles.

## Relationships

- **is_used_to_discover**: [[gabor-function|Gabor Function]]
- **builds_on_work_of**: [[david-hubel|David Hubel]]
- **builds_on_work_of**: [[torsten-wiesel|Torsten Wiesel]]

---
*Extracted from: Deep+Learning+Ian+Goodfellow*