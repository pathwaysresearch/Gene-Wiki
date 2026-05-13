---
type: concept
aliases: [Teacher Forcing]
summary: A training strategy for recurrent neural networks where the ground-truth output from the previous time step is used as input for the current time step, rather than the model's own prediction.
relationships:
  - target: recurrent-neural-networks
    type: training_technique_for
tags: [deep-learning, neural-networks, rnn, training-techniques]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Teacher Forcing

## Definition
Teacher forcing is a training technique applicable to recurrent neural networks that have connections from their outputs at one time step to their hidden states at the next. During the training phase, instead of feeding the model's own generated output from time `t` back into itself to compute the state at `t+1`, the model is fed the correct target value `y(t)` from the training dataset.

## Rationale
The use of teacher forcing is motivated by the maximum likelihood training criterion. When maximizing the log-likelihood of a sequence, `log p(y(1), y(2) | x(1), x(2))`, the chain rule of probability expands this to `log p(y(2) | y(1), x(1), x(2)) + log p(y(1) | x(1), x(2))`. This decomposition shows that at time `t=2`, the model should be trained to maximize the conditional probability of `y(2)` given the previous *correct* output `y(1)`. Teacher forcing directly implements this by supplying the ground-truth values from the training set as inputs for subsequent steps.

## Contrast with Deployment
This training procedure is distinct from how the model is used at deployment or inference time. When the model is deployed, the true output sequence is not available. In this case, the model must approximate the correct output `y(t)` with its own generated output `o(t)` and feed that back into itself to generate the next element in the sequence. This discrepancy between training and inference can sometimes lead to issues.

## Relationships

- **training_technique_for**: [[recurrent-neural-networks|Recurrent Neural Networks]]

---
*Extracted from: Deep+Learning+Ian+Goodfellow*