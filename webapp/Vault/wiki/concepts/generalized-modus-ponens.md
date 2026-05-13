---
type: concept
aliases: [Generalized Modus Ponens]
summary: A "lifted" inference rule for first-order logic that combines variable substitution with the Modus Ponens principle to derive conclusions without full propositionalization.
relationships:
  - target: first-order-logic
    type: inference-rule-in
  - target: universal-instantiation
    type: is-based-on
tags: [inference-rule, first-order-logic, lifted-inference]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Generalized Modus Ponens

## Definition
Generalized Modus Ponens is a sound inference rule for first-order logic that raises the propositional Modus Ponens rule to handle variables and quantifiers directly. It allows for the deduction of a new fact `SUBST(θ, q)` from a set of atomic sentences `p₁', ..., pₙ'` and an implication `p₁ ∧ ... ∧ pₙ ⇒ q`, provided there is a substitution `θ` such that `SUBST(θ, pᵢ) = pᵢ'` for all `i`.

## How It Works
The rule identifies an implication in the knowledge base and a set of known facts that match the premise of the implication under some consistent substitution for the variables. For example, given the facts `King(John)` and `Greedy(y)` and the rule `King(x) ∧ Greedy(x) ⇒ Evil(x)`, Generalized Modus Ponens finds the substitution `θ = {x/John, y/John}`. It then applies this substitution to the conclusion `Evil(x)` to infer the new fact `Evil(John)`.

## Soundness and Significance
The rule's soundness is based on Universal Instantiation. Since `p ⊨ SUBST(θ, p)` for any universally quantified sentence `p`, the premises and the implication can be instantiated with the substitution `θ`. This results in a standard propositional Modus Ponens application, proving that `SUBST(θ, q)` follows logically. This "lifted" approach forms the basis for lifted versions of forward chaining, backward chaining, and resolution algorithms.

## Relationships

- **inference-rule-in**: [[first-order-logic|First Order Logic]]
- **is-based-on**: [[universal-instantiation|Universal Instantiation]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*