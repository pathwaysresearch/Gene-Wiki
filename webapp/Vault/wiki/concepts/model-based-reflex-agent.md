---
type: concept
aliases: [Model-Based Reflex Agent]
summary: An agent that maintains an internal state, or model, to track aspects of the world it cannot currently see, using this model to make decisions in partially observable environments.
relationships:
  - target: simple-reflex-agent
    type: is_an_extension_of
tags: [agent-architecture, ai, state-representation]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Model-Based Reflex Agent

## Definition
A model-based reflex agent is an agent that handles partial observability by maintaining an internal state that depends on the percept history. This internal model represents the agent's knowledge about the current state of the world, which allows it to make more informed decisions than a simple reflex agent when the environment is not fully visible.

## How It Works
This agent keeps track of the world's state using its internal model. When a new percept arrives, the agent updates its internal state based on its previous state, the action it just took, and the new percept. It then chooses an action in the same way as a simple reflex agent, by matching a rule against its updated internal state description. The model is responsible for creating the new internal state description.

## Handling Partial Observability
In a partially observable environment, it is often impossible for the agent to determine the exact current state. The internal model represents the agent's "best guess" about the state of the world. For example, an automated taxi that cannot see around a large truck must guess about the cause of a traffic holdup. This ability to maintain a belief about the world's state allows the agent to function effectively despite uncertainty and incomplete information.

## Relationships

- **is_an_extension_of**: [[simple-reflex-agent|Simple Reflex Agent]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*