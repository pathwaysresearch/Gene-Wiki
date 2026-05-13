---
type: concept
aliases: [VCG Mechanism]
summary: A truth-revealing auction mechanism for allocating goods where each winning agent pays a tax equal to the harm their participation causes to other agents.
relationships:
  - target: mechanism-design
    type: is_an_example_of
tags: [auction-theory, mechanism-design, multi-agent-systems]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# VCG Mechanism

## Definition
The VCG (Vickrey-Clarke-Groves) mechanism is a method for allocating goods to a set of bidders that is designed to be truth-revealing. This means that it is in each agent's best interest to report their true value for receiving an item.

## How It Works
The mechanism operates in four steps. First, a central authority asks each agent to report their value, $b_i$. Second, it allocates the goods to a subset of bidders, $A$, to maximize the total reported utility, $B = \sum_i b_i(A)$. Third, for each agent $i$, it calculates two values: the sum of reported utilities for all other winners ($B_{-i}$) and the maximum possible total utility for all other agents if agent $i$ were not in the game ($W_{-i}$). Finally, each agent $i$ pays a tax equal to $W_{-i} - B_{-i}$.

## Key Properties
The VCG mechanism is truth-revealing because of its payment structure. The payoff for an agent $i$ is their true value minus the tax: $v_i(A) - (W_{-i} - B_{-i})$. This structure ensures an agent's optimal strategy is to bid their true value. In an example provided by the text, this means a winner pays a tax equal to the highest reported value among the losers, representing the value of the opportunity lost by the highest-bidding loser due to the winner's participation.

## Relationships

- **is_an_example_of**: [[mechanism-design|Mechanism Design]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*