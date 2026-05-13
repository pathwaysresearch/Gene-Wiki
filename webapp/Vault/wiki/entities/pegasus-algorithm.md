---
type: entity
aliases: [PEGASUS Algorithm]
summary: A policy-search algorithm developed by Ng and Jordan (2000) that utilizes correlated sampling to efficiently compare and improve policies.
relationships:
  - target: policy-search
    type: is-an-implementation-of
  - target: correlated-sampling
    type: uses
tags: [reinforcement-learning, algorithm, policy-search]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# PEGASUS Algorithm

## Overview
PEGASUS is a policy-search algorithm introduced by Ng and Jordan (2000). Its key innovation is the use of correlated sampling to improve the efficiency and accuracy of policy evaluation.

## Core Principle
The algorithm is based on the idea of correlated sampling, which reduces measurement error when comparing policies. By having different policies execute on the same set of pre-generated scenarios or random seeds, the variance due to environmental stochasticity is removed, allowing for a more direct comparison of the policies' effectiveness.

## Significance
The paper introducing PEGASUS also proved its formal properties. The use of correlated sampling in reinforcement learning is attributed to work by Van Roy (1998) and Ng and Jordan (2000).

## Relationships

- **is-an-implementation-of**: [[policy-search|Policy Search]]
- **uses**: [[correlated-sampling|Correlated Sampling]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*