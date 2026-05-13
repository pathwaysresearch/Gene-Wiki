---
type: concept
aliases: [Extensive Form]
summary: A comprehensive game representation that models sequential decisions and can handle partial observability, making it suitable for complex, multiagent, and stochastic environments.
tags: [game-theory, game-representation]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Extensive Form

## Overview
Extensive form is a powerful representation for games that goes beyond the simple game trees used for games of perfect information. Its key distinguishing feature is the ability to model partial observability, where players may not have complete information about the state of the game or the previous actions of other players.

## Key Features
This representation is highly versatile and can model a wide range of environment properties, including partially observable, multiagent, stochastic, sequential, and dynamic settings. It can represent simultaneous moves by imposing an arbitrary order on players but specifying that an earlier player's actions are not observable to subsequent players. The model also incorporates a "chance" player to handle stochastic events and assumes players have *perfect recall*, meaning they remember all their own past actions.

## Limitations and Solving
While extensive form is one of the most complete game representations, a standard method for solving it involves converting the game to its normal-form matrix representation. However, the size of the normal form is exponential in the number of a player's information sets, making this approach computationally infeasible for large games like Texas hold'em poker, which can have on the order of 10^18 states. This contrasts with alpha-beta search, which is effective for perfect-information games but does not work well for games with imperfect information.

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*