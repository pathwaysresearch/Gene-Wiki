---
type: concept
aliases: [Decision Networks]
summary: A graphical formalism for representing and solving decision problems under uncertainty, extending Bayesian networks with nodes for actions and utilities.
relationships:
  - target: bayesian-networks
    type: extends
  - target: ross-shachter
    type: advanced-by
tags: [graphical-models, decision-making, probabilistic-reasoning]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Decision Networks

## Definition
Decision networks, also known as influence diagrams, provide a simple and formal way to express and solve decision problems. They are a natural extension of Bayesian networks, designed to handle decisions under uncertainty.

## Structure
In addition to the chance nodes representing random variables found in Bayesian networks, decision networks include two other types of nodes. Decision nodes represent the choices available to the agent, and utility nodes (also called value nodes) represent the agent's utility function or preferences over outcomes.

## Solving and History
The text credits Ross Shachter (1986) with developing a method for solving decision networks directly, which avoids the need to create an intermediate decision tree of potentially exponential size. This algorithm was also one of the first complete inference methods for multiply connected Bayesian networks.

## Relationships

- **extends**: [[bayesian-networks|Bayesian Networks]]
- **advanced-by**: [[ross-shachter|Ross Shachter]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*