---
type: concept
aliases: [Bayesian Networks]
summary: A probabilistic graphical model that represents conditional independence relationships among a set of variables using a directed acyclic graph. A probabilistic graphical model that represents a set of random variables and their conditional dependencies via a directed acyclic graph (DAG).
relationships:
  - target: ladder-of-causation
    type: operates_on_rung_one_of
  - target: bayes-s-rule
    type: uses
  - target: bayes-s-rule
    type: extends
  - target: david-rumelhart
    type: influenced_by
  - target: belief-propagation
    type: uses_method
  - target: causal-chains
    type: incorporates_structure
  - target: colliders
    type: incorporates_structure
  - target: judea-pearl
    type: developed_by
  - target: d-separation
    type: uses
  - target: conditional-independence
    type: represents
  - target: variable-elimination
    type: uses-method
  - target: markov-network
    type: can-be-converted-to
  - target: ross-shachter
    type: was-researched-by
tags: [probabilistic-reasoning, graphical-models, artificial-intelligence, probabilistic-models, uncertain-reasoning]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Bayesian Networks

## Definition and Purpose

A Bayesian network is a formal and systematic method for representing conditional independence relationships among variables in an uncertain domain. As introduced in the text, their purpose is to capture uncertain knowledge in a natural and efficient way, enabling probabilistic inference that, while computationally intractable in the worst case, can be performed efficiently in many practical situations.

## Structure and Semantics

A Bayesian network has two main components: a topology and a set of conditional probability tables (CPTs). The topology is a directed acyclic graph where nodes represent variables and directed edges signify direct influence. The structure explicitly shows dependencies; for example, an arrow from node X to node Y means X has a direct influence on Y. The absence of an edge between nodes represents a conditional independence assumption. Each node has an associated CPT that quantifies the probability distribution of that node's variable, conditioned on the values of its parent nodes.

## Example: The Burglary-Alarm Network

The text provides a typical example of a Bayesian network for a scenario involving a Burglary, an Earthquake, an Alarm, and two neighbors, John and Mary, who might call. The network structure shows that Burglary and Earthquake are independent parent nodes that both directly affect the Alarm node. The Alarm node, in turn, is the parent of the JohnCalls and MaryCalls nodes. The CPTs provide the specific probabilities, such as P(Alarm | Burglary=True, Earthquake=False) = 0.94. This model allows for reasoning about the probability of a burglary given evidence, such as which neighbors have called.

## Relationships

- **represents**: [[conditional-independence|Conditional Independence]]
- **uses-method**: [[variable-elimination|Variable Elimination]]
- **can-be-converted-to**: [[markov-network|Markov Network]]
- **was-researched-by**: [[ross-shachter|Ross Shachter]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*

---
*Also referenced in: The Book Of Why  The New Science Of Cause And Effect ( Pdfdrive )*