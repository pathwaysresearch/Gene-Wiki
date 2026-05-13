---
type: concept
aliases: [Partially Observable Problem]
summary: A problem formulation in which an agent's perceptions are insufficient to uniquely determine the current state of the environment, requiring the agent to reason about a set of possible states.
relationships:
  - target: belief-state
    type: is-characterized-by
  - target: belief-state-search
    type: is-solved-by
tags: [problem-formulation, search, uncertainty]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Partially Observable Problem

## Definition
A partially observable problem is one where an agent's percepts do not suffice to pin down its exact state in the environment. This uncertainty is a common feature in the vast majority of real-world environments and requires different problem-solving techniques than fully observable problems where the agent's state is always known.

## Nondeterminism from Uncertainty
In a partially observable setting, an action can lead to one of several possible outcomes from the agent's perspective, even if the underlying environment is deterministic. This apparent nondeterminism arises because the agent, being uncertain about its starting state within a set of possibilities, cannot be certain of the outcome state or the subsequent percepts it will receive.

## Core Requirement
For any intelligent system to function effectively in a partially observable environment, it must perform the core function of maintaining its belief state. This process, which involves tracking the set of all possible states the agent might be in, is also known as monitoring, filtering, or state estimation. An agent may start with an initial problem formulation that is nondeterministic and later switch to a partially observable formulation to better explain failures, such as attributing a key not working to an unobservable property of the key.

## Relationships

- **is-characterized-by**: [[belief-state|Belief State]]
- **is-solved-by**: [[belief-state-search|Belief State Search]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*