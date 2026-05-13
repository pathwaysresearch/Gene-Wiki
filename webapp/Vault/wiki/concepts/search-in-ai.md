---
type: concept
aliases: [Search (in AI)]
summary: The process an agent uses to find a sequence of actions (a solution) to achieve a goal in a known, deterministic, and observable environment.
relationships:
  - target: problem-formulation-in-ai
    type: requires
  - target: state-space
    type: explores
  - target: uninformed-search
    type: has_method
  - target: a-star-search
    type: has_method
  - target: local-search
    type: has_method
tags: [problem-solving, algorithms, ai-core-concepts]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Search (in AI)

## Definition
In the context of artificial intelligence, search is the process an agent uses to construct sequences of actions that achieve its goals. This approach is applicable in environments that are deterministic, observable, static, and completely known. A path through the problem's state space from an initial state to a goal state constitutes a solution.

## Algorithmic Approaches
Search algorithms can be broadly categorized. A general TREE-SEARCH algorithm considers all possible paths to find a solution, which can be inefficient. In contrast, a GRAPH-SEARCH algorithm improves upon this by avoiding the consideration of redundant paths, which is crucial in state spaces with many repeated states. These algorithms typically treat states and actions as atomic units, without considering their internal structure.

## Evaluation Criteria
Search algorithms are judged on four key criteria: completeness, which is whether the algorithm is guaranteed to find a solution if one exists; optimality, which is whether it finds the best possible solution according to the path cost function; time complexity, which measures how long it takes to find a solution; and space complexity, which measures how much memory is required. These complexities are often expressed in terms of the branching factor of the state space ($b$) and the depth of the shallowest solution ($d$).

## Relationships

- **requires**: [[problem-formulation-in-ai|Problem Formulation In Ai]]
- **explores**: [[state-space|State Space]]
- **has_method**: [[uninformed-search|Uninformed Search]]
- **has_method**: [[a-star-search|A Star Search]]
- **has_method**: [[local-search|Local Search]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*