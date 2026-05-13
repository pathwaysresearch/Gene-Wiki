---
type: concept
aliases: [Route-Finding Problem]
summary: A class of real-world problems where the goal is to find an optimal path or sequence of transitions between specified locations.
relationships:
  - target: problem-formulation
    type: is-an-example-of
tags: [problem-solving, search, applications]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Route-Finding Problem

## Overview
The route-finding problem is a canonical example of a problem solved by search algorithms. It is formally defined in terms of specified locations, which are the states, and transitions along links between them, which are the actions. The objective is to find a sequence of links that forms a path from a starting location to a destination.

## Real-World Applications
Route-finding algorithms have a wide variety of applications. These range from relatively straightforward uses, such as websites and in-car systems that provide driving directions, to much more complex problems. Examples of complex applications include routing video streams in computer networks, military operations planning, and airline travel-planning systems.

## Formulation Complexity
While the basic concept is simple, formulating a real-world route-finding problem can be highly complex. For instance, in airline travel planning, the state must include not only the current airport but also the current time. Furthermore, the cost of an action (a flight segment) can depend on previous segments and their fare bases, requiring the state to record extra 'historical' information about the journey so far.

## Relationships

- **is-an-example-of**: [[problem-formulation|Problem Formulation]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*