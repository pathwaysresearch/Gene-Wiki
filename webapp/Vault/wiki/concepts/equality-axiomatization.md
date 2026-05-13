---
type: concept
aliases: [Equality Axiomatization]
summary: An approach to handling equality in logical inference by explicitly adding axioms that define its properties (reflexivity, symmetry, transitivity) and substitution rules to the knowledge base.
tags: [first-order-logic, axiomatization, equality-reasoning]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Equality Axiomatization

## Overview
One method for enabling a logical inference system to handle assertions of equality (e.g., $x = y$) is to explicitly axiomatize the equality relation. This involves adding a set of sentences to the knowledge base that formally define the properties of equality, allowing a standard inference procedure like resolution to perform equality reasoning.

## Fundamental Axioms
This approach requires three basic axioms that define the core properties of the equality relation. These are reflexivity ($\forall x \ x=x$), symmetry ($\forall x,y \ x=y \Rightarrow y=x$), and transitivity ($\forall x,y,z \ x=y \wedge y=z \Rightarrow x=z$). These axioms establish that equality is an equivalence relation.

## Substitution Axioms
In addition to the fundamental axioms, the principle of substitution must be encoded. This requires adding an axiom for each predicate and function in the knowledge base. For each predicate $P$, an axiom like $\forall x,y \ x=y \Rightarrow (P(x) \Leftrightarrow P(y))$ is needed. For each function $F$, an axiom like $\forall w,x,y,z \ w=y \wedge x=z \Rightarrow (F(w,x) = F(y,z))$ is required to state that if the arguments are equal, the function's value is the same.

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*