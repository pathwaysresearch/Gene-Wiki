---
type: concept
aliases: [Successor-State Axiom]
summary: A logical sentence that compactly defines the truth value of a fluent at the next time step (t+1) based on the state of the world and actions taken at the current time step (t).
relationships:
  - target: fluent
    type: defines-transition-of
tags: [temporal-logic, knowledge-representation, frame-problem]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Successor-State Axiom

## Purpose and Structure

A successor-state axiom is a logical sentence used to define the transition model of a dynamic world. It specifies the conditions under which a fluent will be true at the next time step, t+1, based on the state of fluents and actions at the current time step, t.

## General Form

The general logical form of a successor-state axiom for a fluent F is: F^{t+1} <=> ActionCausesF^t v (F^t ^ ¬ActionCausesNotF^t). This states that F is true at t+1 if either an action at t made it true, or it was already true at t and no action at t made it false.

## Wumpus World Examples

The text provides a simple successor-state axiom for the `HaveArrow` fluent: HaveArrow^{t+1} <=> (HaveArrow^t ^ ¬Shoot^t). A more complex axiom is given for the agent's location, L_{1,1}^{t+1}, which depends on whether the agent was in an adjacent square and moved toward [1,1], or was already in [1,1] and did not move away.

## Relationships

- **defines-transition-of**: [[fluent|Fluent]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*