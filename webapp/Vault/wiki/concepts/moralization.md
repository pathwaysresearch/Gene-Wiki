---
type: concept
aliases: [Moralization]
summary: A procedure to convert a directed graphical model into an undirected graphical model, which is a necessary step for certain inference algorithms.
relationships:
  - target: directed-probabilistic-model
    type: operates_on
  - target: undirected-probabilistic-model
    type: produces
tags: [graphical-models, graph-theory, model-conversion]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Moralization

## Definition
Moralization is the process of converting a directed graphical model into an undirected one, called a moralized graph. This conversion is a key step in preparing a directed model for algorithms that operate on undirected graphs.

## The Process
The conversion involves two main steps. First, for any node that has multiple parents, an undirected edge is added between every pair of its parents. This step is sometimes referred to as "marrying the parents." Second, all the original directed edges in the graph are converted into undirected edges.

## Effect on Independence
This conversion process can alter the independence properties represented by the graph. Specifically, moralization can cause the loss of some independence information. For example, in a v-structure (a -> c <- b), variables 'a' and 'b' are marginally independent in the directed model, but the moralization process adds an edge between them, making them directly dependent in the resulting undirected graph.

## Relationships

- **operates_on**: [[directed-probabilistic-model|Directed Probabilistic Model]]
- **produces**: [[undirected-probabilistic-model|Undirected Probabilistic Model]]

---
*Extracted from: Deep+Learning+Ian+Goodfellow*