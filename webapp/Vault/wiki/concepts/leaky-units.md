---
type: concept
aliases: [Leaky Units]
summary: A type of recurrent unit with a linear self-loop, designed to help recurrent neural networks handle long-term dependencies by integrating information over different time scales.
relationships:
  - target: long-short-term-memory
    type: related-to
  - target: recurrent-neural-network
    type: component-of
tags: [recurrent-neural-networks, rnn-architecture, long-term-dependencies]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Leaky Units

## Definition
Leaky units are a mechanism used in recurrent networks to address the challenge of learning long-term dependencies. They are characterized by an internal linear self-loop, where the weight of this connection acts as a time constant. This structure allows the unit's state to persist over longer periods, facilitating the flow of information across many time steps.

## Setting Time Constants
There are two primary strategies for setting the time constants in leaky units. The first approach is to manually fix them to constant values, for example, by sampling them from a distribution at initialization. The second strategy is to treat the time constants as free parameters that are learned by the model during training. Using leaky units with a variety of different time scales has been shown to be beneficial for capturing long-term dependencies.

## Relationship to Other Models
The concept of leaky units is foundational to other advanced recurrent architectures. The state unit in a Long Short-Term Memory (LSTM) cell, for instance, has a linear self-loop that is functionally similar to a leaky unit, though its weight is dynamically controlled by a forget gate. Leaky units have also been found to be effective in the context of echo state networks.

## Relationships

- **related-to**: [[long-short-term-memory|Long Short Term Memory]]
- **component-of**: [[recurrent-neural-network|Recurrent Neural Network]]

---
*Extracted from: Deep+Learning+Ian+Goodfellow*