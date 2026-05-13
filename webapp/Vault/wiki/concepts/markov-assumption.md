---
type: concept
aliases: [Markov Assumption]
summary: The assumption that the future state of a process depends only on a finite, fixed number of previous states, not on the entire history.
relationships:
  - target: transition-model
    type: is-a-property-of
tags: [stochastic-processes, probabilistic-models, time-series]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Markov Assumption

## Definition
The Markov assumption is a simplifying condition used in modeling processes that evolve over time. It posits that the current state depends on only a finite, fixed number of previous states. This avoids the complexity of conditioning the current state on an infinitely growing history of past states.

## Application in Transition Models
This assumption is critical for creating tractable transition models in probabilistic reasoning over time. Instead of needing to define a probability distribution P(Xₜ | X₀:ₜ₋₁), the Markov assumption allows the model to be simplified. For example, a first-order Markov process assumes P(Xₜ | X₀:ₜ₋₁) = P(Xₜ | Xₜ₋₁).

## Order of Markov Processes
The 'finite fixed number' of previous states determines the order of the Markov process. A first-order Markov process assumes the current state depends only on the immediately preceding state. A second-order Markov process assumes the current state depends on the two immediately preceding states, and so on.

## Relationships

- **is-a-property-of**: [[transition-model|Transition Model]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*