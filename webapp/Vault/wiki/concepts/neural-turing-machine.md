---
type: concept
aliases: [Neural Turing Machine]
summary: A neural network architecture that augments a standard network, such as an RNN, with an explicit external memory bank that it can learn to read from and write to.
relationships:
  - target: content-based-addressing
    type: uses
tags: [neural-network-architecture, memory-augmented-networks, sequence-modeling]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Neural Turing Machine

## Core Concept
Neural networks typically excel at storing implicit knowledge but struggle to memorize explicit facts. The Neural Turing Machine (NTM) architecture addresses this by separating the model into two main parts: a "representation" part, or "task network" (often a recurrent network), and an explicit "memory" part. The task network learns to control the memory, deciding what information to store, where to store it, and what to retrieve.

## Architecture
An NTM consists of a controller network and an external memory bank. The memory is composed of a set of memory cells, which typically store vectors rather than scalars. The controller network interacts with this memory via specialized reading and writing mechanisms. At each step, the controller can issue commands to read from specific memory addresses or write new information to them, allowing the model to perform complex, sequential tasks that require factual recall.

## Memory Access Mechanisms
NTMs can use different strategies for accessing memory. A key innovation is **content-based addressing**, where the network can retrieve information based on a partial match of its content, analogous to a person recalling a song from a few lyrics. This is particularly effective when the memory cells store large, vector-valued objects. This contrasts with simpler **location-based addressing**, which cannot refer to the content of the memory itself.

## Relationships

- **uses**: [[content-based-addressing|Content Based Addressing]]

---
*Extracted from: Deep+Learning+Ian+Goodfellow*