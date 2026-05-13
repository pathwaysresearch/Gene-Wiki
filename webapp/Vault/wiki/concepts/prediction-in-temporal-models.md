---
type: concept
aliases: [Prediction (in Temporal Models)]
summary: The task of computing the posterior distribution over a future state, given all evidence observed up to the current time.
relationships:
  - target: filtering-in-temporal-models
    type: is-a-component-of
  - target: hidden-markov-model
    type: applied-to
tags: [temporal-models, inference, forecasting]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Prediction (in Temporal Models)

## Definition
Prediction is an inference task in temporal models that computes the probability distribution over a future state `X_{t+k}` given evidence up to the current time `t`, denoted `P(X_{t+k} | e_{1:t})`. It can be understood as the process of filtering forward in time without the addition of new evidence. The filtering process itself inherently includes a one-step prediction as part of its update cycle.

## Recursive Computation
Prediction over multiple time steps can be performed via a recursive computation. The distribution for a state at time `t+k+1` is derived from the predicted distribution for the state at `t+k`. The formula for this is given as `P(X_{t+k+1}|e_{1:t}) = Σ_{x_{t+k}} P(X_{t+k+1}|x_{t+k})P(x_{t+k}|e_{1:t})`. This process essentially chains together one-step predictions to project the state distribution further into the future.

## Key Properties
A crucial property of the prediction task is that its computation relies solely on the transition model of the system. Unlike filtering, it does not involve the sensor model, because it is projecting the evolution of the state based on its internal dynamics, without incorporating new observations from the future.

## Relationships

- **is-a-component-of**: [[filtering-in-temporal-models|Filtering In Temporal Models]]
- **applied-to**: [[hidden-markov-model|Hidden Markov Model]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*