---
type: concept
aliases: [Simple Reflex Agent]
summary: The simplest kind of agent program, which selects actions based only on the current percept, ignoring the rest of the percept history. An agent that selects actions based solely on the current percept, ignoring the rest of the percept history, by using a set of condition-action rules.
relationships:
  - target: rational-agent
    type: is-an-implementation-of
  - target: model-based-reflex-agent
    type: is_a_simpler_form_of
tags: [agent-architectures, reflex-agents, agent-programs, agent-architecture, ai]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Simple Reflex Agent

## Definition
A simple reflex agent is one of the four basic types of agent programs. Its defining characteristic is that it makes decisions based solely on the current percept, without maintaining any internal state or memory of past percepts.

## How It Works
These agents function by using a set of condition-action rules. When the agent receives a percept, its program checks for a rule whose condition matches the current state and then executes the corresponding action. The text provides an example program for a vacuum-cleaner agent that returns the action `Suck` if the current status is `Dirty`, or moves `Right` or `Left` based on its location if the status is `Clean`.

## Role and Limitations
Simple reflex agents represent a fundamental approach to creating rational behavior from a compact program, as opposed to an impractically large lookup table (a `TABLE-DRIVEN-AGENT`) that maps every possible percept history to an action. While efficient, their inability to consider percept history makes them unsuitable for environments where the optimal action depends on more than just the current observation.

## Relationships

- **is-an-implementation-of**: [[rational-agent|Rational Agent]]
- **is_a_simpler_form_of**: [[model-based-reflex-agent|Model Based Reflex Agent]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*