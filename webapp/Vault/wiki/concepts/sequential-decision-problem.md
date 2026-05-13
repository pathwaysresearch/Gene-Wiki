---
type: concept
aliases: [Sequential Decision Problem]
summary: A class of problems where an agent's utility depends on a sequence of decisions made in a stochastic environment, rather than a single one-shot action.
relationships:
  - target: markov-decision-process
    type: is_formalized_as
tags: [decision-theory, artificial-intelligence, planning]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Sequential Decision Problem

## Definition
A sequential decision problem is one in which an agent's utility depends on a sequence of decisions. This contrasts with one-shot or episodic decision problems where the utility of each action's outcome is well known. These problems incorporate utilities, uncertainty, and sensing, and include search and planning problems as special cases.

## Environment Characteristics
The environment for a sequential decision problem is stochastic, and the agent's utility function depends on an environment history—a sequence of states—rather than on a single state. In each state, the agent receives a reward, and the total utility is a function of the sequence of rewards received. For example, a negative reward in non-terminal states can incentivize an agent to reach a goal state quickly.

## Time Horizon
A key consideration in sequential decision problems is the time horizon for decision making, which can be finite or infinite. For infinite horizon problems, calculating utility as a simple sum of rewards can lead to infinite values, which makes comparing policies difficult. This issue necessitates methods like discounted rewards or considering the average reward per time step to ensure utilities are finite and comparable.

## Relationships

- **is_formalized_as**: [[markov-decision-process|Markov Decision Process]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*