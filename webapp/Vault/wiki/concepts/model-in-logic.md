---
type: concept
aliases: [Model (in logic)]
summary: A mathematical abstraction of a "possible world" that assigns a definitive true or false value to every relevant sentence in a logical system.
relationships:
  - target: semantics-in-logic
    type: is-a-formalization-of-possible-world-in
  - target: entailment
    type: is-used-to-define
  - target: model-checking
    type: is-enumerated-by
tags: [logic, semantics, knowledge-representation]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Model (in logic)

## Definition
In logic, a model is a formal structure used in place of the more informal "possible world." While a possible world can be thought of as a potential state of a real environment, a model is a mathematical abstraction that simply fixes the truth value (true or false) for every sentence under consideration.

## Function in Semantics
Models are central to defining a logic's semantics. For a sentence α to be evaluated, a model m provides the necessary context. If α is true in model m, we say that m satisfies α, or that m is a model of α. The set of all models in which a sentence α is true is denoted as M(α).

## Example
In propositional logic, a model is an assignment of true or false to every proposition symbol. For a knowledge base concerning the wumpus world with seven proposition symbols, there are 2^7 = 128 possible models. An inference process like model checking involves enumerating these models to determine logical entailment.

## Relationships

- **is-a-formalization-of-possible-world-in**: [[semantics-in-logic|Semantics In Logic]]
- **is-used-to-define**: [[entailment|Entailment]]
- **is-enumerated-by**: [[model-checking|Model Checking]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*