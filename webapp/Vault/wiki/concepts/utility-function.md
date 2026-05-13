---
type: concept
aliases: [Utility Function]
summary: A mathematical representation of an agent's preferences, assigning a numerical value (utility) to each possible outcome or state of the world.
relationships:
  - target: decision-theory
    type: foundational-to
  - target: preference-elicitation
    type: determined-by
  - target: multiattribute-utility-theory
    type: extended-by
tags: [decision-theory, preferences, rationality]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Utility Function

## Definition
A utility function is a core component of decision theory that quantifies an agent's preferences. It assigns a single real number to each state of the world, representing its desirability to the agent. The central idea is that the behavior of any rational agent can be modeled as if it is maximizing the expected value of its utility function.

## Assessment and Scaling
The process of determining an agent's utility function is called preference elicitation. Since there is no absolute scale for utility, a relative scale is established by fixing the utility of a "best possible prize" at U(S) = u_T and a "worst possible catastrophe" at U(S) = u_⊥. Normalized utilities often set these to 1 and 0, respectively. The utility of any other outcome can then be assessed by finding the probability p at which the agent is indifferent between that outcome and a standard lottery [p, u_T; (1-p), u_⊥].

## Utility of Money
The utility of money is typically not a linear function of its monetary value. For most individuals, the utility function for money is concave for positive wealth, reflecting diminishing marginal utility—the first million dollars provides more utility than the next million. A pioneering study by Grayson (1960) found that the utility of money for oil wildcatters was almost exactly proportional to the logarithm of the amount. A typical utility curve is S-shaped, being concave for gains and convex for losses.

## Relationships

- **foundational-to**: [[decision-theory|Decision Theory]]
- **determined-by**: [[preference-elicitation|Preference Elicitation]]
- **extended-by**: [[multiattribute-utility-theory|Multiattribute Utility Theory]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*