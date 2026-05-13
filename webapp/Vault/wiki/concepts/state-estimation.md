---
type: concept
aliases: [State Estimation]
summary: The process of maintaining and updating an agent's belief state in a partially observable environment, also known as filtering or monitoring, using a recursive process to incorporate new information.
relationships:
  - target: belief-state
    type: maintains
tags: [filtering, monitoring, robotics, localization]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# State Estimation

## Definition and Synonyms
State estimation is the core function of an intelligent system operating in a partially observable environment. It is the process of maintaining the agent's current belief state over time as new percepts arrive. This function is also commonly referred to as **monitoring** or **filtering**.

## Recursive State Estimation
The update process is typically performed via a recursive state estimator. This means the new belief state is computed from the previous belief state and the most recent percept, rather than by re-examining the entire history of percepts from the beginning. This recursive approach is crucial for efficiency, as it allows the agent's computation to happen as fast as percepts are coming in, preventing the agent from "falling behind."

## Application in Localization
A canonical application of state estimation is **localization**, which is the task of an agent determining its own position in the world. Given a map of the environment, a sequence of actions it has taken, and a sequence of percepts (e.g., from sonar sensors detecting obstacles), the agent uses the state estimation process to maintain a belief state over its possible locations on the map.

## Relationships

- **maintains**: [[belief-state|Belief State]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*