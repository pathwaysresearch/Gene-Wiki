---
type: concept
aliases: [Decentralized Planning]
summary: A planning problem for multiple agents or bodies where communication constraints prevent the formation of a common world state estimate, requiring decoupled execution.
relationships:
  - target: joint-action
    type: coordinates
tags: [multi-agent-systems, planning, distributed-ai]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Decentralized Planning

## Definition
Decentralized planning addresses problems involving multiple physically decoupled units, such as a fleet of robots, where communication constraints make it impossible to pool all sensor information to form a single, common estimate of the world state. While the term suggests a decentralized planning *phase*, it often refers to problems where planning may be centralized but the *execution* phase is at least partially decoupled.

## Context within Multiagent Systems
Decentralized planning exists on a spectrum of multi-effector problems. It is more complex than multieffector planning (one agent, multiple concurrent effectors) or multibody planning (multiple bodies with pooled information). The key challenge arises when the multiple bodies cannot maintain a shared world view during execution, forcing their individual subplans to include explicit coordination actions.

## Key Challenges
The primary difficulty in decentralized planning stems from the decoupled execution. Each agent or body must act based on its local information, which may be incomplete or out of sync with others. This necessitates building subplans that are robust to this uncertainty and that explicitly manage interaction and information sharing to achieve the collective goal.

## Relationships

- **coordinates**: [[joint-action|Joint Action]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*