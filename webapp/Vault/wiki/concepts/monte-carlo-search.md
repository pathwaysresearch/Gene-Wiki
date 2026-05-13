---
type: concept
aliases: [Monte Carlo Search]
summary: A search method used in games with large branching factors, like Go, that relies on random sampling (rollouts) to estimate the value of moves.
relationships:
  - target: go
    type: applied-to
tags: [game-theory, adversarial-search, algorithm, stochastic-methods]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Monte Carlo Search

## Overview
Monte Carlo search is a technique used for game-playing, particularly in games where traditional methods like alpha-beta search are infeasible due to a very large branching factor. Instead of a systematic exploration of the game tree, it uses random sampling to estimate the value of different moves. The text mentions several variants were described by Frank et al. (1998).

## Application in Go
The text identifies Monte Carlo methods as the primary approach for top Go programs, such as MOGO. Go's 19x19 board and high branching factor (starting at 361) make it too daunting for regular alpha-beta search. Monte Carlo methods, often in the form of "rollouts," are used instead. The text notes that rapid advances in computer Go are likely as experimentation with new forms of Monte Carlo search continues.

## How It Works
The core idea is to perform many simulated games (rollouts) from the current position. The text notes that the "trick is to decide what moves to make in the course of the rollout." A specific implementation mentioned is the UCT (upper confidence bounds on trees) method, which initially makes random moves but over time guides the sampling process to favor moves that have previously led to wins.

## Enhancements
The text mentions that some tricks are added to the basic Monte Carlo approach in Go programs. These can include knowledge-based rules that suggest specific moves when certain patterns are detected on the board, as well as limited local search to resolve tactical questions.

## Relationships

- **applied-to**: [[go|Go]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*