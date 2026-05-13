---
type: concept
aliases: [Conditional Independence]
summary: A relationship where variables become independent of each other once the value of another variable is known, which is crucial for simplifying probabilistic calculations. A key concept in probability theory where two random variables are independent of each other given knowledge of a third.
relationships:
  - target: independence-of-random-variables
    type: is_a_variant_of
  - target: conditional-probability
    type: builds_on
tags: [probability-theory, probabilistic-reasoning, graphical-models, statistics, bayesian-networks]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Conditional Independence

## Role in Probabilistic Reasoning

Conditional independence is a fundamental concept for simplifying probabilistic reasoning in complex domains. It allows for the decomposition of complex problems, making inference computationally tractable. The text highlights that getting efficient solutions to probabilistic problems requires using independence and conditional independence relationships to simplify the necessary summations, which often align with a natural understanding of the problem's structure.

## Application in the Wumpus World

The text illustrates the power of conditional independence using the wumpus world problem. When calculating the probability of a pit in a specific square, a key insight is that the observed breezes are conditionally independent of distant, unobserved squares (the 'Other' variables), given the state of the squares adjacent to the agent's visited locations (the 'Frontier' variables). This allows for manipulating the query formula to isolate and simplify parts of the calculation, avoiding a summation that would otherwise grow exponentially with the number of unknown squares.

## Formal Representation

Bayesian networks are introduced as a systematic and formal way to represent conditional independence relationships explicitly. The structure, or topology, of a Bayesian network graph directly encodes these relationships. For instance, the text describes a simple network where *Toothache* and *Catch* are conditionally independent given *Cavity*, meaning that once the state of *Cavity* is known, learning about a toothache provides no new information about the probability of the probe catching.

## Relationships

- **builds_on**: [[conditional-probability|Conditional Probability]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*

---
*Also referenced in: Deep+Learning+Ian+Goodfellow*