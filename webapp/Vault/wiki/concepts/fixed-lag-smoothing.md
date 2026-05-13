---
type: concept
aliases: [Fixed-Lag Smoothing]
summary: An online smoothing algorithm that computes the smoothed estimate for a state at a fixed time interval `d` behind the current time `t`.
relationships:
  - target: smoothing-in-temporal-models
    type: is-a
tags: [temporal-models, inference, online-algorithms]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Fixed-Lag Smoothing

## Definition
Fixed-lag smoothing is a specific type of online smoothing where the goal is to compute the smoothed estimate `P(X_{t-d} | e_{1:t})` for a fixed lag `d`. As the current time `t` advances with each new observation, the algorithm must keep up, continuously providing a smoothed estimate for the time slice `d` steps in the past.

## Algorithmic Challenge
The standard forward-backward algorithm for smoothing is not ideal for online settings like fixed-lag smoothing. A naive approach of re-running the entire algorithm over the relevant window for each new observation is inefficient. The challenge is to develop an algorithm that can update the smoothed estimate in constant time per new observation, independent of the lag `d`.

## Incremental Computation Approach
The text outlines an approach for an efficient, incremental algorithm. While the forward message can be updated easily via the standard filtering process, updating the backward message is more complex. The proposed method involves defining a matrix "transformation operator" `B` that relates backward messages at different points in time. This allows for a more efficient, incremental update of the required backward message as new observations arrive, avoiding a full re-computation.

## Relationships

- **is-a**: [[smoothing-in-temporal-models|Smoothing In Temporal Models]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*