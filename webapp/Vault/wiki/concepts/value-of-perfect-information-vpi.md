---
type: concept
aliases: [Value of Perfect Information (VPI)]
summary: A measure of the expected increase in utility an agent would receive from obtaining perfect, cost-free information about an uncertain variable before making a decision.
tags: [decision-theory, information-value, expected-utility]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Value of Perfect Information (VPI)

## Definition
The Value of Perfect Information (VPI) is defined as the difference in expected utility between the best course of action with the information and the best course of action without it. It quantifies the worth of resolving uncertainty for a specific random variable before a decision is made.

## Rationale
The value of information derives from the ability to change one's course of action to suit the actual situation revealed by the information. Without the information, an agent must choose the action that is best on average across all possible situations, whereas with information, the agent can discriminate.

## General Formula
The text provides a mathematical formulation for VPI. The expected utility of the current best action `α` given evidence `e` is `EU(α|e) = max_a Σ_{s'} P(RESULT(a)=s'|a,e)U(s')`. After obtaining new evidence `E_j = e_{jk}`, the new expected utility is `EU(α_{e, e_{jk}}|e, e_{jk}) = max_a Σ_{s'} P(RESULT(a)=s'|a,e,e_{jk})U(s')`. The VPI of `E_j` is the expected value of this gain, averaged over all possible outcomes of `E_j`.

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*