---
type: concept
aliases: [Planning Domain Definition Language (PDDL)]
summary: A formal language for representing AI planning problems, describing initial states, goal states, and actions with their preconditions and effects.
tags: [planning, representation-language, ai]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Planning Domain Definition Language (PDDL)

## Definition
PDDL, the Planning Domain Definition Language, is a representation for planning problems. It describes the initial and goal states as conjunctions of literals, and defines actions in terms of their preconditions and effects. These effects are typically divided into an "add list" of fluents that become true and a "delete list" of fluents that become false.

## Expressiveness and Limitations
PDDL is designed to carefully balance the expressiveness of the language with the complexity of the algorithms that operate on it. However, this balance means some problems remain difficult to express. For example, a goal with a universal quantifier, such as “move all the cargo from A to B regardless of how many pieces of cargo there are,” cannot be easily represented in PDDL, whereas it can be in first-order logic.

## Role in Planning Systems
PDDL provides a standardized format that allows various planning algorithms to operate on a common problem representation. Planning systems are problem-solving algorithms that use these explicit propositional or relational representations of states and actions to derive effective heuristics and develop powerful, flexible solutions.

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*