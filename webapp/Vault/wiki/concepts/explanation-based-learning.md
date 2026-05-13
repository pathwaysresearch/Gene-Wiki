---
type: concept
aliases: [Explanation-Based Learning (EBL)]
summary: A machine learning method that uses prior knowledge to derive a general rule from a single training example by first constructing an explanation of the example and then generalizing that explanation.
relationships:
  - target: operationality
    type: uses-concept
tags: [machine-learning, inductive-learning, single-example-learning]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Explanation-Based Learning (EBL)

## Core Idea
The fundamental principle of Explanation-Based Learning (EBL) is to learn a general rule from a single observation. The process begins by using prior knowledge to construct an explanation for the observation, detailing why it is an instance of a particular concept. This explanation can be a logical proof or any other well-defined reasoning process.

## Generalization from Explanation
Once an explanation is constructed for a specific example, EBL generalizes this explanation to define a broader class of cases for which the same explanation structure is valid. This generalized definition forms the basis of a new rule that covers all cases in that class. This allows the system to move from a specific instance to a general principle, a behavior seen in commonsense reasoning, such as concluding all Brazilians speak Portuguese after meeting one who does.

## The Operationality Challenge
A key challenge in EBL is ensuring that the derived rules are efficient and useful. This is often addressed by enforcing an operationality criterion on the subgoals within the rule, meaning they must be easy to solve. However, this introduces a tradeoff, as more specific subgoals are generally easier to solve (more operational) but cover fewer cases (less general). Optimizing this tradeoff is a complex problem, as the cost of solving a subgoal depends on the entire knowledge base.

## Relationships

- **uses-concept**: [[operationality|Operationality]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*