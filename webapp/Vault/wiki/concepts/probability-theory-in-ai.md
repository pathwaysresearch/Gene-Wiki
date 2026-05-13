---
type: concept
aliases: [Probability Theory (in AI)]
summary: A formal framework used in AI to represent and reason with an agent's degrees of belief, summarizing uncertainty that arises from ignorance or nondeterminism.
relationships:
  - target: acting-under-uncertainty
    type: is-a-solution-for
  - target: decision-theoretic-agent
    type: is-a-foundation-for
tags: [uncertainty, reasoning, knowledge-representation]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Probability Theory (in AI)

## Epistemological Commitment
Probability theory is presented as the primary tool for handling degrees of belief. While logic commits to sentences being true, false, or unknown, a probabilistic agent assigns a numerical degree of belief between 0 (certainly false) and 1 (certainly true). The ontological commitment, however, is the same as logic: the world is composed of facts that either hold or do not.

## Summarizing Uncertainty
The theory provides a method for summarizing the uncertainty that comes from an agent's "laziness and ignorance," effectively solving the qualification problem. For example, an agent can express an 80% chance (a probability of 0.8) that a patient with a toothache has a cavity, based on statistical data, general knowledge, or a combination of evidence.

## Interpretation of Probability
The text explains that a probabilistic belief represents an agent's expectation. A probability of 0.8 for a cavity means that out of all situations that are indistinguishable from the current one based on the agent's knowledge, the patient will have a cavity in 80% of them.

## Relationships

- **is-a-solution-for**: [[acting-under-uncertainty|Acting Under Uncertainty]]
- **is-a-foundation-for**: [[decision-theoretic-agent|Decision Theoretic Agent]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*