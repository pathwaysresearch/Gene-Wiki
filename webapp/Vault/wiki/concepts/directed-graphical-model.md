---
type: concept
aliases: [Directed Graphical Model]
summary: A type of structured probabilistic model that represents a probability distribution over a set of variables using a directed acyclic graph (DAG) to specify conditional dependencies.
relationships:
  - target: undirected-graphical-model
    type: is_contrasted_with
tags: [probabilistic-models, graphical-models, structured-prediction]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Directed Graphical Model

## Definition
A directed graphical model is a structured probabilistic model defined on a set of variables **x**. It is formally defined by a directed acyclic graph (DAG) $\mathcal{G}$, whose vertices are the random variables in the model, and a set of local conditional probability distributions $p(x_i | \text{Pa}_{\mathcal{G}}(x_i))$, where $\text{Pa}_{\mathcal{G}}(x_i)$ gives the parents of node $x_i$ in the graph.

## Factorization
The primary property of a directed graphical model is that it allows the joint probability distribution over all variables to be factorized into a product of local conditional probabilities, based on the graph structure. The joint distribution is given by the formula $p(\text{x}) = \prod_i p(x_i | \text{Pa}_{\mathcal{G}}(x_i))$. This factorization captures the conditional independence assumptions encoded in the graph and dramatically reduces the complexity of the model.

## Advantages and Example
This structured approach avoids the intractable memory and computational costs of unstructured, table-based models that must explicitly model every possible interaction. For example, in a relay race with three runners' times $t_0, t_1, t_2$, the joint probability $p(t_0, t_1, t_2)$ can be simplified to $p(t_0)p(t_1 | t_0)p(t_2 | t_1)$. This requires storing much smaller conditional probability tables instead of one massive table for all combinations, making storage, inference, and sampling computationally feasible.

## Relationships

- **is_contrasted_with**: [[undirected-graphical-model|Undirected Graphical Model]]

---
*Extracted from: Deep+Learning+Ian+Goodfellow*