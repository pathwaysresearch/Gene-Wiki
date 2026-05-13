---
type: entity
aliases: [Go]
summary: An Asian board game with a 19x19 board, known for its strategic depth and extremely high branching factor, posing a significant challenge for AI.
tags: [game, board-game, ai-benchmark]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Go

## Overview
Go is described as the most popular board game in Asia. It is a deterministic game played on a 19x19 board where players place stones to control territory.

## Challenges for AI
The game presents formidable challenges for traditional game-playing AI. Its branching factor starts at 361, which is described as too daunting for standard alpha-beta search methods. Furthermore, creating an effective heuristic evaluation function is very difficult because the control of territory can be unpredictable until the endgame.

## AI Approaches
Due to these challenges, top Go programs have largely abandoned alpha-beta search. Instead, they employ Monte Carlo methods, such as rollouts, guided by algorithms like UCT (upper confidence bounds on trees). Some programs also incorporate techniques from combinatorial game theory to analyze endgames, which has led to the discovery of optimal solutions that surprised professional players.

## State of the Art (as of 2009)
As of the text's writing, the best programs, like MOGO, played most moves at a master level but were prone to making serious blunders. On a full-size board, MOGO was estimated to be at a low-end advanced amateur level (2-3 dan), though it achieved a win against a top professional with a significant handicap. On a smaller 9x9 board, MOGO played at a professional level.

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*