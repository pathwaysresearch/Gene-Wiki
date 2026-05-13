---
type: concept
aliases: [Augmented Grammar]
summary: A grammar formalism where syntactic categories are enhanced with additional parameters or features to handle linguistic phenomena like agreement.
relationships:
  - target: probabilistic-context-free-grammar
    type: can-be-combined-with
tags: [grammar-formalism, computational-linguistics, parsing]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Augmented Grammar

## Definition
An augmented grammar is a type of formal grammar in which the nonterminal symbols (syntactic categories) are supplemented with arguments or features. These augmentations carry additional information that is used to enforce constraints that are difficult to express in a simple context-free grammar.

## How It Works
Categories are written with parameters, such as `NP(e, pn, head)`, where `e` could be case, `pn` person and number, and `head` the head word. Grammar rules can then place constraints on these parameters. For example, a rule forming a sentence might require that the person and number of the subject NP must be identical to the person and number of the VP. This mechanism allows the grammar to enforce subject-verb agreement and case agreement.

## Example
The text provides a rule `S(head) -> NP(Sbj, pn, h) VP(pn, head)` to illustrate subject-verb agreement. This rule states that a sentence `S` can be formed from a noun phrase `NP` and a verb phrase `VP` only if the `NP` is in the subjective case (`Sbj`) and its person/number feature (`pn`) matches that of the `VP`. The head of the resulting sentence is inherited from the `VP`.

## Relationships

- **can-be-combined-with**: [[probabilistic-context-free-grammar|Probabilistic Context Free Grammar]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*