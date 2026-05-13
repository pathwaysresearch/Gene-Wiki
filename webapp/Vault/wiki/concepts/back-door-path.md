---
type: concept
aliases: [Back-door Path]
summary: In a causal diagram, a non-causal path between an exposure X and an outcome Y that begins with an arrow pointing into X, which can create spurious correlation.
relationships:
  - target: confounding
    type: is_mechanism_for
tags: [causal-inference, graphical-models, dag]
sourced_from: The Book Of Why  The New Science Of Cause And Effect ( Pdfdrive )
---

# Back-door Path

## Definition
A back-door path is a concept from graphical causal models used to identify sources of confounding. It is defined as any path between a variable X (exposure) and a variable Y (outcome) that starts with an arrow pointing into X. These paths represent non-causal connections that can create a spurious association between X and Y.

## Role in Deconfounding
The key to removing confounding between X and Y (deconfounding) is to block every back-door path. This is typically done by "controlling for" or "adjusting for" a set of variables Z that lie on these paths. By blocking all such paths, the spurious correlation is eliminated, leaving only the true causal effect of X on Y to be estimated.

## Rules for Application
To successfully deconfound X and Y, one must choose a set of variables Z to control for that blocks all back-door paths. A crucial additional rule is that no variable in the chosen set Z can be a descendant of X on a causal path. Controlling for such a variable could inadvertently block or partially block the very causal effect one is trying to measure. The text presents this as a simple game with clear rules that can be solved algorithmically.

## Relationships

- **is_mechanism_for**: [[confounding|Confounding]]

---
*Extracted from: The Book Of Why  The New Science Of Cause And Effect ( Pdfdrive )*