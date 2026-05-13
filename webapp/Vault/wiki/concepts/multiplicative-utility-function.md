---
type: concept
aliases: [Multiplicative Utility Function]
summary: A functional form for utility used when attributes are mutually utility independent (MUI), combining individual attribute utilities through both additive and multiplicative terms.
relationships:
  - target: mutually-utility-independent-mui
    type: is_implied_by
tags: [utility-theory, multiattribute-utility, decision-analysis]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Multiplicative Utility Function

## Definition
A multiplicative utility function is a specific mathematical form used to represent an agent's preferences when the attributes of the outcomes are mutually utility independent (MUI). It was described by Keeney (1974).

## Mathematical Form
The function combines the utilities of individual attributes, `U_i(x_i)`, using a series of constants, `k_i`. For three attributes, the general form is given as `U = k_1U_1 + k_2U_2 + k_3U_3 + k_1k_2U_1U_2 + k_2k_3U_2U_3 + k_3k_1U_3U_1 + k_1k_2k_3U_1U_2U_3`.

## Relationship to MUI
This functional form is a direct consequence of the MUI assumption. If an agent's preferences satisfy the MUI property, its behavior can be modeled as if it were maximizing a multiplicative utility function.

## Relationships

- **is_implied_by**: [[mutually-utility-independent-mui|Mutually Utility Independent Mui]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*