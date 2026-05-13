---
type: entity
aliases: [Street View Transcription System]
summary: A real-world deep learning application used as a case study for demonstrating practical model development methodology.
relationships:
  - target: convolutional-neural-network
    type: uses
  - target: softmax-function
    type: uses
  - target: rectified-linear-unit
    type: uses
tags: [case-study, computer-vision, application]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Street View Transcription System

## Overview
The Street View transcription system is a project that serves as a practical example of an iterative deep learning development process. The goal of the system is to transcribe sequences of characters, such as house numbers, from images captured by Street View cars.

## Initial Baseline Model
Following the recommended methodology for vision tasks, the project's first baseline was a convolutional network with rectified linear units. To handle the sequence output, the initial implementation used a simple approach: the output layer consisted of 'n' different softmax units to predict a sequence of 'n' characters. Each softmax unit was trained independently, as in a standard classification task.

## Iterative Refinement
The initial baseline was refined based on a theoretical understanding of the system's performance metric (coverage) and data structure. The first major change involved replacing the ad-hoc output layer, which simply multiplied softmax outputs together. A new, specialized output layer and cost function were developed to compute a principled log-likelihood for the output sequence. This principled approach allowed the system's example rejection mechanism, which discards low-confidence predictions, to function much more effectively.

## Relationships

- **uses**: [[convolutional-neural-network|Convolutional Neural Network]]
- **uses**: [[softmax-function|Softmax Function]]
- **uses**: [[rectified-linear-unit|Rectified Linear Unit]]

---
*Extracted from: Deep+Learning+Ian+Goodfellow*