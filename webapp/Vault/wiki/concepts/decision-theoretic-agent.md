---
type: concept
aliases: [Decision-Theoretic Agent]
summary: An agent that uses probability theory to represent beliefs about the world and utility theory to select actions that maximize its expected utility.
relationships:
  - target: probability-theory-in-ai
    type: uses
  - target: acting-under-uncertainty
    type: is-a-type-of-agent-for
tags: [agent-architecture, decision-theory, rationality, uncertainty]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Decision-Theoretic Agent

## Agent Architecture
A decision-theoretic agent maintains a belief state that represents not only the set of possible world states but also their associated probabilities. This probabilistic belief state is updated based on the history of percepts, similar to logical agents, but with the crucial addition of probability distributions.

## Decision-Making Process
The agent's core function is to select actions based on the principles of decision theory. It uses its probabilistic belief state to make predictions about the likely outcomes of its actions. By combining these probabilistic outcomes with a utility function (which represents its preferences), the agent can calculate the expected utility of each action and choose the one with the highest value.

## Foundational Components
The functionality of a decision-theoretic agent relies on several key areas of AI. It requires methods for representing and computing with probabilistic information, techniques for updating its belief state over time as new evidence arrives, a formal theory of utility to encode preferences, and algorithms for planning sequences of actions in uncertain environments.

## Relationships

- **uses**: [[probability-theory-in-ai|Probability Theory In Ai]]
- **is-a-type-of-agent-for**: [[acting-under-uncertainty|Acting Under Uncertainty]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*