---
type: concept
aliases: [End-to-end Deep Learning Speech Recognition]
summary: An approach to Automatic Speech Recognition (ASR) that uses a single deep neural network to directly map speech audio to text, completely removing intermediate components like the Hidden Markov Model (HMM).
tags: [speech-recognition, deep-learning, end-to-end-learning, asr]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# End-to-end Deep Learning Speech Recognition

## Overview
End-to-end deep learning for speech recognition represents a major ongoing push in the field. The central goal of this approach is to replace the complex, multi-component pipelines of traditional systems with a single, unified neural network. Specifically, these systems aim to completely remove the Hidden Markov Model (HMM), which was a core part of previous state-of-the-art systems.

## Historical Context
This research direction gained momentum following a rapid shift in the speech recognition community towards deep learning. This shift was driven by unprecedented breakthroughs in performance, with deep learning models achieving around a 30% relative improvement in word error rate over the traditional Gaussian Mixture Model-Hidden Markov Model (GMM-HMM) technology. This success broke a decade-long period of stagnation and spurred a new wave of research into deep learning architectures for ASR.

## Key Innovations
The first major breakthrough towards end-to-end ASR was achieved by Graves et al. (2013). They successfully trained a deep Long Short-Term Memory (LSTM) Recurrent Neural Network (RNN) to perform tasks that moved significantly closer to a fully end-to-end system, demonstrating the potential of deep learning to handle the entire recognition process.

---
*Extracted from: Deep+Learning+Ian+Goodfellow*