---
type: concept
aliases: [Recurrent Neural Networks]
summary: A class of neural networks designed for sequence modeling, characterized by cyclical connections that allow information to persist from one time step to the next.
relationships:
  - target: unfolding-computational-graphs
    type: uses_technique
  - target: teacher-forcing
    type: can_be_trained_with
tags: [deep-learning, neural-networks, sequence-modeling]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Recurrent Neural Networks

## Definition
Recurrent Neural Networks (RNNs) are a class of neural networks that utilize computational graphs with cycles. These cycles are designed to model the influence of a variable's value at one time step on its own value at a future time step, making them inherently suited for processing sequences. The core of an RNN is a recurrent formula, such as the classical dynamical system `s(t) = f(s(t-1); θ)`, where the state `s` at time `t` is a function of the state at the previous time step `t-1`.

## How They Work
An RNN processes an input sequence by iterating through a set of update equations for each time step `t`. A typical implementation computes a pre-activation `a(t) = b + Wh(t-1) + Ux(t)` and a hidden state `h(t) = tanh(a(t))`, based on the current input `x(t)` and the previous hidden state `h(t-1)`. An output `o(t)` is then computed from the hidden state via `o(t) = c + Vh(t)`. The weight matrices `U`, `V`, `W` and bias vectors `b`, `c` are shared across all time steps. The total loss for a sequence is calculated by summing the individual losses over all time steps.

## Computational Power
RNNs are computationally very powerful. A recurrent network of a finite size is universal in the sense that it can compute any function that is computable by a Turing machine. This property, established by researchers like Siegelmann and Sontag, means that RNNs can, in principle, perform any discrete computation. The number of time steps required by the RNN is asymptotically linear in the number of steps used by the corresponding Turing machine.

## Design Patterns
Several important design patterns exist for RNNs. Common architectures include networks that produce an output at each time step and have recurrent connections between hidden units; networks that also produce an output at each step but only have recurrent connections from the output of one step to the hidden units of the next; and networks that read an entire input sequence before producing a single, final output.

## Relationships

- **uses_technique**: [[unfolding-computational-graphs|Unfolding Computational Graphs]]
- **can_be_trained_with**: [[teacher-forcing|Teacher Forcing]]

---
*Extracted from: Deep+Learning+Ian+Goodfellow*