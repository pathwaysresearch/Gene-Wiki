---
type: concept
aliases: [Possible Worlds Semantics]
summary: A framework for modeling an agent's knowledge and belief by defining a set of possible worlds and accessibility relations between them.
tags: [modal-logic, knowledge-representation, epistemic-logic]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Possible Worlds Semantics

## Core Concept
Possible worlds semantics provides a model for an agent's mental state by considering a set of 'possible worlds.' Each world represents a complete and consistent way things could be. An agent's knowledge is defined by the subset of these worlds that are consistent with the information the agent has.

## Accessibility Relations
The model uses accessibility relations, depicted as arrows between worlds, to represent what an agent considers possible. If world `w₂` is accessible from world `w₁` for a given agent, it means that when the actual world is `w₁`, the agent cannot rule out the possibility that the world is `w₂`. Different agents can have different accessibility relations, reflecting their different states of knowledge.

## Modeling Knowledge and Uncertainty
The text's Figure 12.4 illustrates this by modeling the knowledge of Superman (solid arrows) and Lois (dotted arrows). For example, if Lois has seen the weather report, then from a world where it predicts rain, all worlds she considers possible must also have a rain prediction. This framework allows for precise modeling of what an agent knows, doesn't know, and knows about another agent's knowledge.

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*