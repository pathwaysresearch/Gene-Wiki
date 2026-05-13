---
type: concept
aliases: [St. Petersburg Paradox]
summary: A paradox in decision theory where a game with an infinite expected monetary value has a very low subjective value to most people, highlighting the difference between monetary value and utility.
relationships:
  - target: exponential-utility-function
    type: illustrates_need_for
tags: [paradox, decision-theory, utility-theory, economics]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# St. Petersburg Paradox

## The Puzzle
Stated by Nicolas Bernoulli in 1713, the St. Petersburg paradox describes a game of chance involving a fair coin. The coin is tossed repeatedly until it comes up heads. If the first heads appears on the *n*-th toss, the player wins $2^n$ dollars.

## The Paradox
The paradox arises from the calculation of the game's expected monetary value. The probability of the first heads occurring on toss $n$ is $(1/2)^n$, and the corresponding payoff is $2^n$. The expected value is the sum of (probability × payoff) over all possible outcomes, which is an infinite sum: $\sum_{n=1}^{\infty} (1/2)^n \cdot 2^n = \sum_{n=1}^{\infty} 1 = \infty$. Despite this infinite expected payout, most people would only be willing to pay a small, finite amount to play the game.

## Resolution via Utility Theory
Nicolas's cousin, Daniel Bernoulli, resolved the paradox in 1738 by proposing that the value of money should be measured by its utility, not its nominal amount. He suggested that the utility of money is logarithmic (e.g., $U(S_n) = a \log_2 S_n + b$). Under such a utility function, the expected *utility* of the game is finite, which explains why a rational person would only be willing to risk a small, finite sum to play.

## Relationships

- **illustrates_need_for**: [[exponential-utility-function|Exponential Utility Function]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*