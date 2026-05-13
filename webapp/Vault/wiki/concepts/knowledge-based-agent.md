---
type: concept
aliases: [Knowledge-Based Agent]
summary: An intelligent agent that uses an internal knowledge base of sentences and an inference mechanism to reason about the world and decide on actions.
relationships:
  - target: inference-logic
    type: uses
  - target: propositional-logic
    type: can_use
tags: [agent-architecture, artificial-intelligence]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Knowledge-Based Agent

## Composition
A knowledge-based agent is composed of a knowledge base and an inference mechanism. The knowledge base contains a set of sentences expressed in a formal knowledge representation language, which represent the agent's knowledge about the world.

## Operation
The agent operates by storing sentences about the world in its knowledge base. It then uses its inference mechanism to infer new sentences from the existing knowledge. These new, inferred sentences are then used by the agent to decide what action to take to achieve its goals.

## Example Application
The text describes a hybrid agent for the wumpus world that uses a propositional knowledge base to infer the state of the world. This agent uses logical inference, by Asking questions of its knowledge base, to determine which squares are safe and which have yet to be visited. Based on these inferences, it constructs plans, such as grabbing gold, exploring new squares, or shooting at a potential wumpus location.

## Relationships

- **uses**: [[inference-logic|Inference Logic]]
- **can_use**: [[propositional-logic|Propositional Logic]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*