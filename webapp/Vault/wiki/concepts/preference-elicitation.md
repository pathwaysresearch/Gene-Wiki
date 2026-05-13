---
type: concept
aliases: [Preference Elicitation]
summary: The process of determining an agent's utility function by presenting them with choices and observing their expressed preferences.
relationships:
  - target: utility-function
    type: determines
  - target: lottery-decision-theory
    type: uses
tags: [utility-theory, decision-support, methodology]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Preference Elicitation

## Purpose
To build a decision-theoretic system that can make decisions on an agent's behalf, it is essential to first understand and quantify the agent's preferences. Preference elicitation is the process of systematically working out an agent's underlying utility function by observing their choices in specific scenarios.

## Method Using a Standard Lottery
A common technique for preference elicitation involves the use of a "standard lottery." To assess the utility of a particular prize S, the agent is asked to choose between receiving S for certain and participating in a standard lottery [p, u_T; (1-p), u_⊥], where u_T is the utility of the best possible outcome and u_⊥ is the utility of the worst. The probability p is adjusted until the agent is indifferent between the prize and the lottery. 

## Determining Utility Values
Once the indifference point is found, the utility of the prize S can be calculated. Assuming normalized utilities where the best prize has a utility of 1 (u_T = 1) and the worst catastrophe has a utility of 0 (u_⊥ = 0), the utility of S is equal to the probability p from the standard lottery. By repeating this process for all relevant outcomes, the agent's utility function can be constructed.

## Relationships

- **determines**: [[utility-function|Utility Function]]
- **uses**: [[lottery-decision-theory|Lottery Decision Theory]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*