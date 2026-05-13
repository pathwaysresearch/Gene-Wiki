---
type: concept
aliases: [Dynamic Decision Network (DDN)]
summary: A model for online agents in partially observable, stochastic environments that extends Dynamic Bayesian Networks with decision and utility nodes for decision-making under uncertainty.
relationships:
  - target: dynamic-bayesian-network
    type: extends
  - target: partially-observable-markov-decision-process
    type: applies_to
tags: [agent-architecture, probabilistic-reasoning, decision-theory]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Dynamic Decision Network (DDN)

## Definition and Structure
A Dynamic Decision Network (DDN) is a model for designing online agents that operate in partially observable and stochastic environments. It is created by extending a Dynamic Bayesian Network (DBN) with decision and utility nodes, following the structure of decision networks from Chapter 16. In a DDN, the state is represented by a set of factored state variables ($X_t$), and the model includes a transition model $P(X_{t+1}|X_t, A_t)$ and a sensor model $P(E_t|X_t)$, where $A_t$ is the action and $E_t$ are evidence variables. This structure provides a practical implementation of a utility-based agent.

## Agent Operation
An agent based on a DDN uses a filtering algorithm to continuously update its belief state representation as it incorporates new percepts and performs actions. To make decisions, the agent projects forward possible action sequences and chooses the sequence that yields the best outcome according to its utility function. This allows the agent to operate online, constantly re-evaluating its situation and plans based on new information.

## Advantages and Limitations
DDN-based agents have several key advantages. They are well-suited for partially observable, uncertain environments and can revise their plans to handle unexpected evidence. They can also manage sensor failures and plan actions specifically to gather information. Furthermore, they exhibit "graceful degradation" under time pressure by using approximation techniques. However, the text identifies two main limitations. First, the decision-making process relies on forward search through the state space, which is less sophisticated than the hierarchical planning techniques from Chapter 11. Second, the DDN language is fundamentally propositional, which makes it difficult to extend with ideas from more expressive first-order probabilistic languages.

## Relationships

- **extends**: [[dynamic-bayesian-network|Dynamic Bayesian Network]]
- **applies_to**: [[partially-observable-markov-decision-process|Partially Observable Markov Decision Process]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*