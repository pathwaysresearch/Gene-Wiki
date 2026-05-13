---
type: concept
aliases: [Convolutional Networks for Speech Recognition]
summary: An application of convolutional neural networks to speech recognition where the input spectrogram is treated as a 2D image, allowing the network to learn features by replicating weights across both time and frequency.
tags: [speech-recognition, convolutional-neural-networks, deep-learning, asr]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Convolutional Networks for Speech Recognition

## Core Idea
One of the key innovations in deep learning for Automatic Speech Recognition (ASR) is the use of convolutional networks. This approach re-frames the problem by treating the input audio representation, typically a spectrogram, as a two-dimensional image. In this image, one axis corresponds to time and the other axis corresponds to the frequency of different spectral components.

## How It Works
By treating the spectrogram as an image, a convolutional network can apply 2D convolutions. The network's weights (filters) are replicated across both the time and frequency dimensions. This allows the model to learn features, such as specific phonetic patterns, that are invariant to their precise location in the time-frequency plane, which is a powerful property for robust speech recognition.

## Improvement Over Prior Models
This two-dimensional convolutional approach is an improvement over earlier models like time-delay neural networks (TDNNs). While TDNNs also used weight replication, they did so only across the time dimension. By replicating weights across both time and frequency, the 2D convolutional models can capture more complex and robust spectro-temporal patterns, leading to better performance.

---
*Extracted from: Deep+Learning+Ian+Goodfellow*