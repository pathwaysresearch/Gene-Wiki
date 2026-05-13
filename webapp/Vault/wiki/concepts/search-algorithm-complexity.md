---
type: concept
aliases: [Search Algorithm Complexity]
summary: A set of metrics used to evaluate the performance of search algorithms, primarily time and space complexity, expressed in terms of branching factor (b), solution depth (d), and maximum path length (m).
tags: [performance-metric, computer-science, search-algorithm]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Search Algorithm Complexity

## Key Metrics
In the context of AI, the complexity of search algorithms is expressed in terms of three key quantities. The **branching factor (b)** is the maximum number of successors of any node. The **depth (d)** is the number of steps along the path from the root to the shallowest goal node. The **maximum length (m)** is the maximum length of any path in the state space.

## Time and Space Measurement
Time complexity is typically measured by the number of nodes generated during the search. Space complexity is measured by the maximum number of nodes stored in memory at any one time. This approach is used because in AI, the state space graph is often represented implicitly by the initial state and actions, and can be infinite, making traditional measures based on the size of an explicit graph less applicable.

## Cost Evaluation
The effectiveness of a search algorithm can be assessed using two cost measures. The **search cost** typically depends on the time complexity but can also include a term for memory usage. The **total cost** is a broader measure that combines the search cost with the path cost of the solution found.

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*