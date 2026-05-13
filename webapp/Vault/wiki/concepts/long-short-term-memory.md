---
type: concept
aliases: [Long Short-Term Memory]
summary: A type of recurrent neural network (RNN) architecture that uses specialized cells with gating mechanisms to control information flow, enabling it to effectively learn long-term dependencies. A type of recurrent neural network (RNN) architecture designed to learn long-term dependencies by using a system of gates to regulate information flow.
relationships:
  - target: forget-gate
    type: has-component
  - target: leaky-units
    type: related-to
  - target: recurrent-neural-network
    type: is-a
  - target: jurgen-schmidhuber
    type: created_by
  - target: yoshua-bengio
    type: researched_by
  - target: alex-graves
    type: applied_by
tags: [recurrent-neural-networks, sequence-modeling, deep-learning-models, architecture]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Long Short-Term Memory

## Architecture Overview
Long Short-Term Memory (LSTM) recurrent networks are built from "LSTM cells" which replace the standard units of a simple RNN. These cells possess an internal recurrence in the form of a self-loop, in addition to the outer recurrence of the overall network. This internal loop allows information to persist over time. The flow of information into, out of, and within the cell is regulated by a system of gating units.

## Key Components
The most critical component of an LSTM cell is the state unit, which features a linear self-loop similar in principle to the leaky units used in other RNNs. However, in an LSTM, this self-loop's weight is not fixed but is dynamically controlled by a **forget gate**. This gate is a sigmoid unit that, at each time step, determines how much of the previous state to forget (a weight near 0) or retain (a weight near 1), based on the current input and the previous hidden state.

## Architectural Significance
While many architectural variations of the LSTM have been explored, research has shown that few, if any, consistently outperform the standard design across a wide range of tasks. Studies have identified the forget gate as a particularly crucial ingredient for the LSTM's success. A common and effective practice is to initialize the bias of the forget gate to 1, which encourages the network to remember information by default.

## Relationships

- **has-component**: [[forget-gate|Forget Gate]]
- **related-to**: [[leaky-units|Leaky Units]]
- **is-a**: [[recurrent-neural-network|Recurrent Neural Network]]
- **created_by**: [[jurgen-schmidhuber|Jurgen Schmidhuber]]
- **researched_by**: [[yoshua-bengio|Yoshua Bengio]]
- **applied_by**: [[alex-graves|Alex Graves]]

---
*Extracted from: Deep+Learning+Ian+Goodfellow*