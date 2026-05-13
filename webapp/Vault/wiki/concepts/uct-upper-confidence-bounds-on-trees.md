---
type: concept
aliases: [UCT (Upper Confidence bounds on Trees)]
summary: A specific Monte Carlo search algorithm, widely used in Go programs, that balances exploration of new moves with exploitation of moves that have proven successful.
relationships:
  - target: monte-carlo-search
    type: is-a-type-of
  - target: mogo
    type: used-by
tags: [game-theory, adversarial-search, algorithm]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# UCT (Upper Confidence bounds on Trees)

## Definition
UCT, which stands for "upper confidence bounds on trees," is a method used in Monte Carlo search for game-playing. The text identifies it as the basis for Monte Carlo methods in many recent Go programs, citing the work of Kocsis and Szepesvari (2006).

## How It Works
The UCT method works by iteratively building a search tree. In the initial iterations, it makes random moves to explore the game space. As it gathers data from these random "rollouts," it begins to guide the sampling process. The algorithm prefers to select moves that have led to wins in previous samples, effectively balancing the need to explore new possibilities with exploiting known good moves.

## Application in Go
The text explicitly states that many recent Go programs have adopted Monte Carlo methods based on the UCT scheme. The program MOGO, described as the strongest Go program as of 2009, is based on this approach. This method helps overcome the challenges of Go's massive branching factor and difficult-to-craft evaluation functions.

## Significance
The adoption of UCT-based Monte Carlo search is presented as a major reason for the rapid advances in computer Go. The text notes that up to 1997 there were no competent Go programs, but by 2009, programs using this method were playing at a master level.

## Relationships

- **is-a-type-of**: [[monte-carlo-search|Monte Carlo Search]]
- **used-by**: [[mogo|Mogo]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*