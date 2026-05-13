---
type: concept
aliases: [Forget Gate]
summary: A key component of a Long Short-Term Memory (LSTM) cell that dynamically controls the extent to which information from the previous state is retained or forgotten.
relationships:
  - target: long-short-term-memory
    type: component-of
tags: [lstm, gating-mechanism, recurrent-neural-networks]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Forget Gate

## Function and Mechanism
The forget gate is a gating unit within an LSTM cell responsible for controlling the weight of the cell's internal linear self-loop. At each time step, it computes a value between 0 and 1 using a sigmoid activation function. This value multiplies the cell's previous state, effectively deciding how much information to discard. A value of 1 means the state is fully preserved, while a value of 0 means it is completely forgotten.

## Implementation
The output of the forget gate for cell `i` at time step `t`, denoted `f_i^{(t)}`, is calculated based on the current input vector `x^{(t)}`, the previous hidden layer vector `h^{(t-1)}`, and a set of learned parameters: biases `b^f`, input weights `U^f`, and recurrent weights `W^f`. The formula is given by `f_i^{(t)} = σ(b_i^f + Σ_j U_{i,j}^f x_j^{(t)} + Σ_j W_{i,j}^f h_j^{(t-1)})`.

## Significance in Practice
Research has shown that the forget gate is a crucial ingredient for the successful performance of LSTMs. Its ability to selectively manage the cell's memory is essential for learning long-term dependencies. One widely adopted practice that improves performance is to add a bias of 1 to the forget gate's inputs. This initialization encourages the gate to default to remembering, which helps prevent gradients from vanishing early in training.

## Relationships

- **component-of**: [[long-short-term-memory|Long Short Term Memory]]

---
*Extracted from: Deep+Learning+Ian+Goodfellow*