---
type: concept
aliases: [Filtering (in Temporal Models)]
summary: The task of computing the posterior distribution over the current state, given all evidence observed up to the current time.
relationships:
  - target: prediction-in-temporal-models
    type: uses
  - target: smoothing-in-temporal-models
    type: is-a-component-of
  - target: hidden-markov-model
    type: applied-to
tags: [temporal-models, inference, state-estimation]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Filtering (in Temporal Models)

## Definition
Filtering is an inference task in temporal models that involves maintaining a current state estimate and updating it as new evidence arrives. A key feature of an efficient filtering algorithm is that it updates the state estimate incrementally, without needing to re-process the entire history of observations at each time step. This process computes the belief state, or the posterior distribution over the current state, given all evidence to date, denoted as `P(X_t | e_{1:t})`.

## How It Works
The filtering process consists of a two-step cycle. First, the current state distribution is projected forward one time step to produce a prediction of the next state's distribution, using the transition model. Second, this predicted distribution is updated using the new evidence from the sensor model for that time step. For example, to find the probability of rain on day 2 given umbrella observations on days 1 and 2, one first predicts the rain probability for day 2 based on day 1's evidence, then updates this prediction with the observation of the umbrella on day 2.

## Role in Inference
Filtering is one of the four primary inference tasks for temporal models, alongside prediction, smoothing, and finding the most likely sequence. It is the fundamental process for tracking the state of a system in real-time as new data becomes available. While essential for online tracking, the text notes that for learning model parameters, smoothing is often preferred as it provides better estimates of past states.

## Relationships

- **uses**: [[prediction-in-temporal-models|Prediction In Temporal Models]]
- **is-a-component-of**: [[smoothing-in-temporal-models|Smoothing In Temporal Models]]
- **applied-to**: [[hidden-markov-model|Hidden Markov Model]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*