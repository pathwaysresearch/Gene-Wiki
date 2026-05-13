---
type: concept
aliases: [Acting Under Uncertainty]
summary: The fundamental challenge for an agent to make effective decisions when its knowledge of the world is incomplete, due to factors like partial observability or nondeterminism.
relationships:
  - target: probability-theory-in-ai
    type: addressed-by
  - target: decision-theoretic-agent
    type: is-a-problem-for
tags: [agent-architecture, uncertainty, decision-making]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Acting Under Uncertainty

## The Core Problem
Agents often operate in environments where they cannot be certain about their current state or the outcomes of their actions. This uncertainty can arise from partial observability (incomplete sensor data), nondeterminism (unpredictable action effects), or a combination of both.

## Limitations of Logical Agents
Traditional logical agents attempt to manage uncertainty by maintaining a belief state, which is a set of all possible world states consistent with observations. This approach has significant drawbacks. It forces the agent to consider every logically possible explanation, even highly unlikely ones, which leads to extremely large and complex belief-state representations.

## The Need for Probabilistic Reasoning
The failure of purely logical approaches to scale in uncertain environments necessitates a different method. Instead of treating all possibilities as equal, an agent needs a way to quantify its belief in different states or outcomes. This leads to the use of probability theory to represent and reason with degrees of belief.

## Relationships

- **addressed-by**: [[probability-theory-in-ai|Probability Theory In Ai]]
- **is-a-problem-for**: [[decision-theoretic-agent|Decision Theoretic Agent]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*