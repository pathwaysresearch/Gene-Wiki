---
type: concept
aliases: [State Estimation (AI)]
summary: The task of maintaining a representation of the possible current states of the world, known as a belief state, given a sequence of actions and percepts in a partially observable environment.
relationships:
  - target: knowledge-based-agent
    type: is_a_task_for
tags: [state-estimation, belief-state, partial-observability]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# State Estimation (AI)

## The Problem of State Estimation
State estimation is the challenge of keeping track of the current state of a partially observable environment. An agent's knowledge of the world is captured in a belief state, which is the set of all possible world states consistent with the sequence of actions and percepts observed so far. The temporal-projection problem, which determines what holds true after an action sequence, is a special case of state estimation with no percepts.

## Computational Complexity
Exact state estimation can be computationally intractable. The text notes that the number of possible belief states can be doubly exponential in the number of propositional variables (2^(2^n)). This means that representing an exact belief state may require logical formulas whose size is exponential in the number of symbols, making the problem very difficult for many environments.

## Approximate State Estimation
Due to the complexity of exact methods, approximate schemes are often used. One common and natural approach is to represent belief states as conjunctions of literals, which are 1-CNF formulas. This creates a simply representable, conservative approximation to the exact belief state, where the 1-CNF belief state (a simple shape) contains the true, more complex belief state.

## Relationships

- **is_a_task_for**: [[knowledge-based-agent|Knowledge Based Agent]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*