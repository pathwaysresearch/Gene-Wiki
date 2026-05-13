---
type: concept
aliases: [Undirected Graphical Model]
summary: A type of structured probabilistic model that represents dependencies between random variables using an undirected graph, suitable for modeling interactions that are bidirectional or have no clear directional cause.
relationships:
  - target: directed-graphical-model
    type: is_contrasted_with
tags: [probabilistic-models, graphical-models, structured-prediction]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Undirected Graphical Model

## Definition and Motivation
An undirected graphical model is a structured probabilistic model used when the interactions between variables have no intrinsic direction or appear to operate in both directions. Unlike directed models, which are based on a clear, uni-directional narrative like a sequence of events, undirected models are more appropriate for situations involving mutual influence. If two nodes in an undirected model are connected by an edge, it signifies that the corresponding random variables are directly related.

## Example Application
A canonical example is modeling the spread of a sickness among a group of people, such as yourself, a coworker, and your roommate. It is just as easy for you to cause your roommate to get sick as it is for your roommate to make you sick, so there is no clean, uni-directional relationship. An undirected graph can model the direct interactions (e.g., you-coworker, you-roommate) while assuming no direct interaction between the coworker and roommate, capturing the idea that transmission between them is indirect and mediated by you.

## Use Cases
Undirected models are chosen when it is difficult to establish a clear causal or temporal flow between variables. They are well-suited for modeling systems where influences are reciprocal. The structure of the graph encodes simplifying assumptions about the interactions; for instance, the absence of an edge between two variables typically represents a form of conditional independence, simplifying the overall model.

## Relationships

- **is_contrasted_with**: [[directed-graphical-model|Directed Graphical Model]]

---
*Extracted from: Deep+Learning+Ian+Goodfellow*