---
type: concept
aliases: [Belief Propagation]
summary: An algorithm used in graphical models like Bayesian networks for performing inference by passing messages between nodes.
relationships:
  - target: bayesian-networks
    type: is_a_method_for
  - target: turbo-codes
    type: is_used_by
tags: [algorithm, inference, graphical-models, message-passing]
sourced_from: The Book Of Why  The New Science Of Cause And Effect ( Pdfdrive )
---

# Belief Propagation

## Core Idea

Belief propagation is a message-passing algorithm used for inference in Bayesian networks. The author realized that in such a network, the messages being passed were conditional probabilities in one direction and likelihood ratios in the other, allowing the network to update its beliefs in response to new evidence.

## Application in Turbo Codes

The text explains that turbo codes, a powerful error-correction technique, use belief propagation for decoding. The Bayesian network representation of a turbo code involves two processors, each observing a noisy version of a codeword. The decoding proceeds by iteratively passing information between these processors, with each one using information from the other to improve its guess of the original hidden message.

## Independent Discovery

The text notes that the inventors of turbo codes, such as Claude Berrou, discovered the belief propagation algorithm independently, without initially realizing its connection to the formal framework of Bayesian networks.

## Relationships

- **is_a_method_for**: [[bayesian-networks|Bayesian Networks]]
- **is_used_by**: [[turbo-codes|Turbo Codes]]

---
*Extracted from: The Book Of Why  The New Science Of Cause And Effect ( Pdfdrive )*