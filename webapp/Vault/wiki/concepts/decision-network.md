---
type: concept
aliases: [Decision Network]
summary: A graphical formalism, also known as an influence diagram, that extends Bayesian networks to support rational decision-making by incorporating actions and utilities.
relationships:
  - target: decision-theory
    type: is-an-implementation-of
  - target: bayesian-network
    type: extends
tags: [graphical-models, decision-making, ai-systems]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Decision Network

## Overview
A decision network, also known as an influence diagram, is a formalism used for the implementation of decision-making systems. It provides a graphical model that represents the variables, actions, and utilities involved in a decision problem under uncertainty.

## Relation to Bayesian Networks
Decision networks are a direct extension of Bayesian networks. They build upon the probabilistic inference capabilities of Bayesian networks by adding two new types of nodes: action nodes, which represent the choices available to the agent, and utility nodes, which represent the agent's preferences over outcomes.

## Function
The primary role of a decision network is to provide a structured framework for applying the principles of decision theory. By explicitly modeling actions and their consequences on uncertain variables, and by associating utilities with final outcomes, the network allows for the calculation of the expected utility for each possible action. This enables the system to identify and select the optimal course of action.

## Relationships

- **is-an-implementation-of**: [[decision-theory|Decision Theory]]
- **extends**: [[bayesian-network|Bayesian Network]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*