---
type: concept
aliases: [Markov Process]
summary: A stochastic model where the probability of a future state depends only on the current state, not on the sequence of events that preceded it.
relationships:
  - target: hidden-markov-model
    type: is-a-component-of
tags: [temporal-models, stochastic-processes, state-space-models]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Markov Process

## Definition
A Markov process is a model for a sequence of random variables where the future is independent of the past, given the present. The first-order Markov assumption, a common simplification, states that the state variables at a given time contain all the information needed to characterize the probability distribution for the next time slice. In other words, the probability of the next state depends only on the current state.

## The First-Order Assumption
The text illustrates the first-order Markov assumption with two examples. In some cases, the assumption is exactly true, such as a particle executing a random walk where its next position depends only on its current position. In other cases, it is an approximation. For instance, modeling rain probability based only on whether it rained the previous day is an approximation, as other factors could be influential.

## Improving Model Accuracy
When the first-order Markov assumption is only an approximation, its accuracy can be improved in two primary ways. The first is to increase the order of the model; for example, a second-order model for rain prediction would consider the weather from the two previous days (`Rain_{t-2}`), which might capture patterns like the rarity of rain lasting more than two consecutive days. The second method is to increase the set of state variables, incorporating additional relevant information such as the season, temperature, humidity, and atmospheric pressure to build a more physically grounded model.

## Relationships

- **is-a-component-of**: [[hidden-markov-model|Hidden Markov Model]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*