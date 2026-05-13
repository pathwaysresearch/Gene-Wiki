---
type: concept
aliases: [Unification]
summary: An algorithm in first-order logic for finding a substitution that makes two logical expressions syntactically identical. The process of finding a substitution for variables in two first-order logic expressions to make them identical, a key step in lifted inference. The process of finding a substitution of terms for variables that makes two logical expressions identical, a fundamental operation in automated reasoning and logic programming. The text discusses it on pages 326-327, 329, and 357.
relationships:
  - target: forward-chaining
    type: used_by
  - target: backward-chaining
    type: used_by
  - target: generalized-modus-ponens
    type: is_used_by
  - target: forward-chaining
    type: is_used_by
  - target: backward-chaining
    type: is_used_by
  - target: j-a-robinson
    type: developed_by
tags: [inference, first-order-logic, algorithm, logic, pattern-matching, automated-reasoning, algorithms]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Unification

## Definition
Unification is the process of finding a substitution, a set of bindings for variables, that makes two logical expressions identical. The algorithm works by comparing the structures of the two inputs, element by element, and building up a substitution `θ` along the way.

## The Unification Algorithm
The algorithm, as presented in Figure 9.1, recursively compares the inputs. If the inputs are identical, it returns the current substitution. If one input is a variable, it attempts to bind the variable to the other input using the `UNIFY-VAR` helper function. If both inputs are compound expressions or lists, it unifies their corresponding components recursively.

## Variable Unification and Checks
The `UNIFY-VAR` function is a critical component. It first checks if the variable is already bound in the current substitution `θ` and unifies the bound value if so. Crucially, it performs an `OCCUR-CHECK?` to ensure a variable is not unified with a term that contains that same variable, which would lead to an infinite structure. If these checks pass, it adds the new binding `{var/x}` to the substitution.

## Relationships

- **used_by**: [[forward-chaining|Forward Chaining]]
- **used_by**: [[backward-chaining|Backward Chaining]]
- **is_used_by**: [[generalized-modus-ponens|Generalized Modus Ponens]]
- **is_used_by**: [[forward-chaining|Forward Chaining]]
- **is_used_by**: [[backward-chaining|Backward Chaining]]
- **developed_by**: [[j-a-robinson|J A Robinson]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*