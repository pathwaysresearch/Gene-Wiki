---
type: entity
aliases: [REINFORCE Algorithm]
summary: A family of policy-gradient algorithms in reinforcement learning developed by Williams (1992) that adjusts policy parameters based on the rewards received.
relationships:
  - target: policy-search
    type: is-an-implementation-of
tags: [reinforcement-learning, algorithm, policy-gradient]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# REINFORCE Algorithm

## Overview
REINFORCE is a policy search algorithm developed by Williams (1992). It is designed to find a good set of parameters $\theta$ for a policy $\pi_\theta$ by performing gradient ascent on the expected reward.

## How It Works
The algorithm approximates the true gradient of the policy value ($\nabla_{\theta}\rho(\theta)$) by summing terms from multiple trials. For each state $s$ visited, the gradient is approximated by the formula $\frac{1}{N} \sum_{j=1}^{N} \frac{(\nabla_{\theta}\pi_{\theta}(s, a_j))R_j(s)}{\pi_{\theta}(s, a_j)}$, where $a_j$ is the action taken in state $s$ on trial $j$, and $R_j(s)$ is the total reward received from that state onwards in that trial.

## Performance
The REINFORCE algorithm is noted to be much more effective than simple hill-climbing methods that perform many trials at each parameter setting. However, the text also states that it is still much slower than necessary.

## Relationships

- **is-an-implementation-of**: [[policy-search|Policy Search]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*