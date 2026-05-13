---
type: concept
aliases: [Expectimax Tree]
summary: A game tree structure for games with chance elements, featuring alternating layers of max nodes (for the player's moves) and chance nodes (for random events).
tags: [game-theory, stochastic-games, search]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Expectimax Tree

## Structure and Definition
An expectimax tree is a model for games involving uncertainty. It is defined as consisting of a max node at the root, followed by alternating layers of chance nodes and max nodes. The chance nodes represent random events, such as dice rolls, where all possible outcomes are assumed to have a non-zero probability.

## Objective
The goal when searching an expectimax tree is to find the value of the root node, which corresponds to the move that maximizes the player's expected utility. This is typically accomplished with a bounded-depth search, as complete trees can be intractably large.

## Pruning Properties
The text investigates whether alpha-beta-style pruning is possible in an expectimax tree. It contrasts this with a standard "max" tree (containing only max nodes), where pruning is possible if leaf values are bounded. The possibility of pruning in an expectimax tree is questioned, even when leaf values are non-negative or bounded within a specific range like [0, 1], because the averaging at chance nodes complicates the bounds used for pruning.

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*