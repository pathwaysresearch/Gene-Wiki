---
type: concept
aliases: [Universal Instantiation]
summary: An inference rule in first-order logic that allows for the substitution of a ground term for a universally quantified variable.
relationships:
  - target: first-order-logic
    type: inference-rule-in
  - target: ground-term
    type: uses
  - target: generalized-modus-ponens
    type: is-foundation-for
tags: [inference-rule, first-order-logic, quantifiers]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Universal Instantiation

## Definition
The rule of Universal Instantiation (UI) states that from a universally quantified sentence, one can infer any sentence obtained by substituting a ground term (a term without variables) for the variable. This rule is fundamental for applying general axioms to specific instances.

## How It Works
Given a universally quantified axiom, such as `∀ x King(x) ∧ Greedy(x) ⇒ Evil(x)`, Universal Instantiation permits the inference of specific sentences by replacing the variable `x` with any ground term. For example, one can substitute `John`, `Richard`, or even a functional term like `Father(John)` for `x` to produce sentences like `King(John) ∧ Greedy(John) ⇒ Evil(John)` or `King(Father(John)) ∧ Greedy(Father(John)) ⇒ Evil(Father(John))`. 

## Role in Inference
Universal Instantiation is a key step in connecting general first-order knowledge to specific cases, effectively removing quantifiers to create ground sentences. This process is a precursor to methods like propositionalization, where a first-order knowledge base is converted into a set of propositional sentences. It is also a foundational principle for more advanced rules like Generalized Modus Ponens, which relies on the validity of substituting terms for variables.

## Relationships

- **inference-rule-in**: [[first-order-logic|First Order Logic]]
- **uses**: [[ground-term|Ground Term]]
- **is-foundation-for**: [[generalized-modus-ponens|Generalized Modus Ponens]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*