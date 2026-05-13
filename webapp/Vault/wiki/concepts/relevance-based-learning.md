---
type: concept
aliases: [Relevance-Based Learning]
summary: A learning approach that first uses prior knowledge, such as determinations, to identify a minimal set of relevant attributes before applying a standard learning algorithm to this reduced feature set.
relationships:
  - target: declarative-bias
    type: is-an-application-of
  - target: determinations
    type: uses
tags: [machine-learning, feature-selection, declarative-bias]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Relevance-Based Learning

## Overview
Relevance-based learning is a strategy that leverages prior knowledge to make learning more efficient. Instead of learning from all available attributes, it first identifies which attributes are relevant to the target predicate and then confines the learning process to this smaller, more manageable set, thereby reducing the hypothesis space.

## How It Works
This approach involves learning the relevance information itself from data. An algorithm can be used to find the simplest determination consistent with the observed examples. For instance, the RBDTL (Relevance-Based Decision-Tree Learning) algorithm first runs an algorithm like MINIMAL-CONSISTENT-DET to find a minimal set of relevant attributes and then passes only this set to the standard DECISION-TREE-LEARNING algorithm.

## Performance Advantage
By reducing the hypothesis space, relevance-based learning can significantly speed up the learning process. The text shows experimental results where RBDTL learns much faster than a standard decision tree learner on a problem where the target function only depended on 5 out of 16 available attributes. The advantage is most pronounced when many of the available attributes are irrelevant to the learning task.

## Relationships

- **is-an-application-of**: [[declarative-bias|Declarative Bias]]
- **uses**: [[determinations|Determinations]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*