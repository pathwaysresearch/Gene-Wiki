---
type: concept
aliases: [Anytime Algorithm]
summary: An algorithm that can be interrupted at any point to return a valid, usable result, with the quality of the result improving the longer it is allowed to run.
relationships:
  - target: decision-theoretic-metareasoning
    type: can-be-controlled-by
tags: [algorithm, real-time-systems, decision-making]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Anytime Algorithm

## Definition
An anytime algorithm is defined in the text as an algorithm "whose output quality improves gradually over time, so that it has a reasonable decision ready whenever it is interrupted." This characteristic is essential for agents operating in real-time environments where decisions must be made under time constraints.

## Control Mechanism
These algorithms are typically controlled by a "metalevel decision procedure" that evaluates whether continuing the computation is worthwhile. This procedure weighs the potential improvement in decision quality against the cost of delaying action, allowing the agent to make a rational trade-off between speed and accuracy.

## Examples in AI
The text provides concrete examples of anytime algorithms to illustrate the concept. These include "iterative deepening in game-tree search and MCMC in Bayesian networks," both of which are methods that can be stopped early to yield a partial or approximate solution that gets refined with more computation time.

## Relationships

- **can-be-controlled-by**: [[decision-theoretic-metareasoning|Decision Theoretic Metareasoning]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*