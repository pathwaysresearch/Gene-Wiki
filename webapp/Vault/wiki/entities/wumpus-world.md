---
type: entity
aliases: [Wumpus World]
summary: A classic grid-based cave environment used in artificial intelligence to illustrate the challenges and operation of knowledge-based agents that must reason under uncertainty.
relationships:
  - target: knowledge-based-agents
    type: is-a-testbed-for
tags: [ai-environment, knowledge-representation, reasoning]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Wumpus World

## Overview
The wumpus world is a canonical environment used in AI to demonstrate the capabilities of knowledge-based agents. The world is a cave consisting of rooms connected by passageways. The agent's goal is to navigate this cave to find a treasure while avoiding deadly hazards.

## Environment Rules and Hazards
The cave contains several dangers. A terrible wumpus resides in one room and will eat anyone who enters. Some rooms contain bottomless pits that will trap anyone who wanders into them. The agent is equipped with a single arrow, which can be used to shoot and kill the wumpus. The agent's knowledge comes from percepts: it perceives a stench in rooms adjacent to the wumpus and a breeze in rooms adjacent to a pit.

## Agent Operation and Reasoning
A knowledge-based agent operates in the wumpus world by maintaining a knowledge base of what it knows about the environment. Starting with only the rules of the game, the agent uses its percepts to make logical inferences about the state of adjacent, unvisited rooms. For example, upon perceiving a breeze in a square, the agent can infer that a pit must exist in one of the neighboring squares. A prudent agent will only move into squares that it has inferred to be safe.

## Relationships

- **is-a-testbed-for**: [[knowledge-based-agents|Knowledge Based Agents]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*