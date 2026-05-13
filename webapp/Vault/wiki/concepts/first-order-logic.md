---
type: concept
aliases: [First-Order Logic]
summary: A formal representation language that is more expressive than propositional logic, with an ontological commitment to facts, objects, and relations. A formal system of logic that uses quantified variables over objects, allowing for more expressive statements about the world than propositional logic. A formal system of logic with greater expressive power than Aristotelian logic, characterized by its use of quantifiers and multi-place relational predicates to make generalizations over objects.
relationships:
  - target: ontological-commitment
    type: has-property
  - target: epistemological-commitment
    type: has-property
  - target: term-first-order-logic
    type: uses
  - target: axiom
    type: uses
  - target: ontology
    type: used-to-define
  - target: knowledge-engineering
    type: used-in
  - target: gottlob-frege
    type: developed-by
  - target: charles-sanders-peirce
    type: developed-by
  - target: giuseppe-peano
    type: notation-developed-by
  - target: universal-instantiation
    type: has-inference-rule
  - target: generalized-modus-ponens
    type: has-inference-rule
  - target: propositionalization
    type: uses-inference-method
tags: [knowledge-representation, formal-logic, ai, logic, artificial-intelligence, inference]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# First-Order Logic

## Overview
First-order logic is a formal language used in knowledge representation that is sufficiently expressive to represent a good deal of commonsense knowledge. It is presented as a more powerful alternative to propositional logic, which is too limited to represent knowledge of complex environments in a concise way. First-order logic either subsumes or forms the foundation of many other representation languages and has been studied intensively for decades.

## Ontological and Epistemological Commitments
According to the text, first-order logic has an ontological commitment to the existence of facts, objects, and relations in the world. This is a more expansive commitment than that of propositional logic, which only assumes facts. The epistemological commitment of first-order logic is that sentences are taken to be true, false, or unknown, a commitment it shares with propositional and temporal logics.

## Syntax and Semantics
First-order logic builds on the declarative, compositional, context-independent, and unambiguous semantics of propositional logic. Its syntax includes symbols of three kinds: constant symbols, which stand for objects; predicate symbols, which stand for relations; and function symbols, which stand for functions. It also uses variables (lowercase letters) and quantifiers, such as the universal quantifier (∀), to make general assertions about objects. A key syntactic element is the term, a logical expression that refers to an object.

## Models in First-Order Logic
A model in first-order logic consists of a set of objects and an interpretation. The interpretation maps constant symbols to objects, predicate symbols to relations on those objects, and function symbols to functions on those objects. Unlike in propositional logic, the number of possible models is unbounded because they can contain any number of objects from one to infinity. This makes checking for entailment by enumerating all possible models an infeasible method.

## Relationships

- **has-property**: [[ontological-commitment|Ontological Commitment]]
- **has-property**: [[epistemological-commitment|Epistemological Commitment]]
- **uses**: [[term-first-order-logic|Term First Order Logic]]
- **uses**: [[axiom|Axiom]]
- **used-to-define**: [[ontology|Ontology]]
- **used-in**: [[knowledge-engineering|Knowledge Engineering]]
- **developed-by**: [[gottlob-frege|Gottlob Frege]]
- **developed-by**: [[charles-sanders-peirce|Charles Sanders Peirce]]
- **notation-developed-by**: [[giuseppe-peano|Giuseppe Peano]]
- **has-inference-rule**: [[universal-instantiation|Universal Instantiation]]
- **has-inference-rule**: [[generalized-modus-ponens|Generalized Modus Ponens]]
- **uses-inference-method**: [[propositionalization|Propositionalization]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*