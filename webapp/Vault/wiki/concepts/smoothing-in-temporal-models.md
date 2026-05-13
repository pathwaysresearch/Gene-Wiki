---
type: concept
aliases: [Smoothing (in Temporal Models)]
summary: The process of computing the probability distribution over a past state, given all evidence observed up to the current time.
relationships:
  - target: filtering-in-temporal-models
    type: uses
  - target: fixed-lag-smoothing
    type: is-a-generalization-of
  - target: hidden-markov-model
    type: applied-to
tags: [temporal-models, inference, state-estimation, machine-learning]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Smoothing (in Temporal Models)

## Definition
Smoothing is an inference task that computes the posterior distribution of a state at a past time `k`, given a complete sequence of observations from time 1 up to a later time `t`. This is expressed as `P(X_k | e_{1:t})` for `0 ≤ k < t`. It provides a more accurate estimate of a past state than filtering, as it incorporates evidence that occurred after time `k`.

## The Forward-Backward Algorithm
Smoothing is typically implemented using a recursive message-passing approach known as the forward-backward algorithm. The computation is divided into two parts. A "forward" message, `f_{1:k}`, is computed by filtering from time 1 to `k`, summarizing the evidence `e_{1:k}`. A "backward" message, `b_{k+1:t}`, is computed by a recursive process running backward from time `t`, summarizing the evidence `e_{k+1:t}`. The final smoothed estimate for state `X_k` is proportional to the pointwise product of these two messages: `α * f_{1:k} * b_{k+1:t}`.

## Importance for Learning
Smoothing is particularly important for learning the parameters of a temporal model, such as the transition and sensor models. Because it provides better estimates of the states a process went through, it is a necessary component for learning algorithms like Expectation-Maximization (EM). The text notes that attempting to learn with filtering alone can fail to converge correctly, as it lacks the benefit of hindsight provided by later observations.

## Relationships

- **uses**: [[filtering-in-temporal-models|Filtering In Temporal Models]]
- **is-a-generalization-of**: [[fixed-lag-smoothing|Fixed Lag Smoothing]]
- **applied-to**: [[hidden-markov-model|Hidden Markov Model]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*