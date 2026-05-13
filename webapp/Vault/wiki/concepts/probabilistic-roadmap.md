---
type: concept
aliases: [Probabilistic Roadmap]
summary: A motion planning method that builds a graph by randomly sampling configurations in a robot's free space and connecting nearby valid points to find a path.
relationships:
  - target: configuration-space
    type: operates-on
  - target: voronoi-graph
    type: alternative-to
tags: [robotics, motion-planning, path-planning, sampling-based-planning]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Probabilistic Roadmap

## Definition
A probabilistic roadmap is a skeletonization approach to path planning that approximates the connectivity of the free configuration space with a graph.

## Construction
The roadmap is created by generating a large number of random configurations and retaining only those that fall within the free space (i.e., are collision-free). These valid configurations become the nodes of the graph. An edge is created between two nodes if a simple, collision-free path exists between them.

## Advantages
This method is presented as an alternative to Voronoi graphs. It is particularly effective in wide-open spaces where Voronoi graphs can produce inefficient paths. By offering more possible routes through the random sampling, it can often find more direct paths.

## Relationships

- **operates-on**: [[configuration-space|Configuration Space]]
- **alternative-to**: [[voronoi-graph|Voronoi Graph]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*