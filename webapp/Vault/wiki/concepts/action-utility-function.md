---
type: concept
aliases: [Action-Utility Function]
summary: A simplified representation of a decision problem, often in a diagram, where chance nodes for final outcomes are factored out, directly mapping actions to a utility value.
tags: [decision-networks, decision-modeling, utility]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Action-Utility Function

## Overview
An action-utility function, represented in an action-utility diagram, is a simplified model of a decision problem that omits an explicit description of the final outcome state. Instead, it directly links actions to their expected utility.

## Structure
In this simplified form, chance nodes corresponding to final outcomes (like *Noise* or *Deaths* in an airport siting problem) are factored out. The model might still contain intermediate chance nodes (like *Air Traffic* or *Litigation*), but the final utility is calculated more directly from the action and these intermediates.

## Limitations
The text highlights that this simplified representation is less flexible than a more general decision network. For example, a change in the world (like new aircraft noise levels) and a change in preferences (the weight given to noise) must both be reflected by altering the action-utility table, whereas in a full model they could be changed independently in the probability and utility models, respectively.

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*