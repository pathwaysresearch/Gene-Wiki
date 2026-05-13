---
type: concept
aliases: [Most Likely Sequence Finding]
summary: The task of finding the single sequence of states most likely to have generated a given sequence of observations in a temporal model.
relationships:
  - target: smoothing-in-temporal-models
    type: related-to
  - target: hidden-markov-model
    type: applied-to
tags: [temporal-models, inference, sequence-analysis, viterbi-algorithm]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Most Likely Sequence Finding

## Definition
The task is to find the weather sequence most likely to explain a given sequence of observations, such as an umbrella appearing or not. This involves finding the sequence of states that maximizes the joint probability of the entire sequence, given the evidence. This is distinct from smoothing, which finds the most likely state at each individual time step by computing marginal distributions.

## Algorithmic Approach
A linear-time algorithm exists for this problem, which relies on the Markov property. The problem can be visualized as finding the most likely path through a graph where nodes represent states at each time step. The solution uses a recursive relationship: the most likely path to any state `x_{t+1}` is an extension of the most likely path to some preceding state `x_t`. By iterating through time and keeping track of the most likely path to each state at each step, the overall most likely sequence can be found efficiently.

## Distinction from Smoothing
It is crucial to understand that the most likely sequence is not necessarily the same as the sequence of the most likely states at each point in time. Finding the most likely sequence considers the joint probability over all time steps, taking into account the likelihood of transitions between states. Smoothing, in contrast, computes distributions over single time steps independently, and assembling the most likely state from each distribution may result in a sequence with very low or even zero probability (e.g., if it contains an impossible transition).

## Relationships

- **related-to**: [[smoothing-in-temporal-models|Smoothing In Temporal Models]]
- **applied-to**: [[hidden-markov-model|Hidden Markov Model]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*