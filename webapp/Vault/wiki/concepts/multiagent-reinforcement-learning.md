---
type: concept
aliases: [Multiagent Reinforcement Learning]
summary: A subfield of reinforcement learning that deals with multiple interacting agents in a common environment, where each agent's optimal policy depends on the policies of other agents.
tags: [reinforcement-learning, game-theory, multiagent-systems]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Multiagent Reinforcement Learning

## Definition
Multiagent Reinforcement Learning (Multiagent RL) addresses sequential game-theoretic problems, also known as Markov games, involving multiple agents. It is distinguished from distributed RL by the presence of agents who cannot coordinate their actions, except through explicit communication, and who may not share the same utility function.

## Key Challenges
The primary challenge in multiagent RL is that the environment becomes nonstationary from the perspective of any single agent. As one agent is learning to defeat its opponent's policy, the opponent is simultaneously changing its policy to defeat the agent. This dynamic, first noted by Littman (1994) in the context of zero-sum Markov games, makes convergence to a stable, optimal policy difficult.

## Cooperative Approaches
One approach to cooperative multiagent RL involves devising methods where separate subagents can achieve a globally optimal combined control system. The basic idea is that each subagent learns its own Q-function from its own stream of rewards, for example, a navigation component rewarded for progress and an obstacle-avoidance component penalized for collisions. Global decisions are then made by maximizing the sum of these Q-functions, a process which can converge to globally optimal solutions.

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*