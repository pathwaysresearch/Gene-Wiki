---
type: concept
aliases: [Reactive Planning]
summary: A planning paradigm that emphasizes fast, reflexive responses to the current state, often using pre-compiled policies or simple rules instead of complex, deliberative planning.
relationships:
  - target: pengi
    type: is-an-example-of
tags: [planning, robotics, agent-architectures]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Reactive Planning

## Overview
Reactive planning systems emerged in the mid-1980s as a response to the slow run times of traditional, deliberative planning systems. These systems are essentially reflex agents that react quickly to their immediate perceptions.

## Mechanisms and Implementations
An early example, PENGI, played a video game using Boolean circuits combined with a "visual" representation of current goals and internal state. Another approach, "universal plans," used a lookup-table method. A universal plan, also known as a policy, contains a pre-computed mapping from any possible state to the action that should be taken in that state.

## Relation to Other Fields
The idea of universal plans or policies, developed in the context of reactive planning, was a rediscovery of a concept that had long been used in the study of Markov decision processes (MDPs).

## Relationships

- **is-an-example-of**: [[pengi|Pengi]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*