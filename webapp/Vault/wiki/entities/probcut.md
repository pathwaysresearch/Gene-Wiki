---
type: entity
aliases: [PROBCUT]
summary: A forward-pruning algorithm, based on alpha-beta search, that prunes nodes that are probably, not just provably, outside the search window.
relationships:
  - target: alpha-beta-pruning
    type: is-a-variant-of
tags: [search-algorithm, pruning, ai-in-games]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# PROBCUT

## Overview
PROBCUT, short for probabilistic cut, is a forward-pruning version of the alpha-beta search algorithm. Unlike standard alpha-beta, which only prunes subtrees that are *provably* outside the current (α, β) search window, PROBCUT also prunes nodes that are *probably* outside the window based on statistical evidence.

## How It Works
The algorithm operates by first conducting a shallow search from a given node to compute a backed-up value, *v*. It then uses statistics gathered from prior experience to estimate the probability that a score of *v* at that particular depth (*d*) would ultimately result in a value outside the current (α, β) window. If this probability is sufficiently high, the node and its entire subtree are pruned from the search.

## Purpose and Risk
The goal of PROBCUT is to achieve more aggressive pruning than standard alpha-beta, potentially speeding up the search. However, this performance gain comes with a risk. Because the pruning is based on probabilities rather than certainty, the text warns that "there is no guarantee that the best move will not be pruned away."

## Relationships

- **is-a-variant-of**: [[alpha-beta-pruning|Alpha Beta Pruning]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*