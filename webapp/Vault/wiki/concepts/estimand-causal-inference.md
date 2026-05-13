---
type: concept
aliases: [Estimand (Causal Inference)]
summary: A mathematical formula or recipe, derived from a causal model, that specifies how to compute a causal quantity from statistical data.
relationships:
  - target: causal-inference-engine
    type: is_produced_by
tags: [causality, statistics, estimation]
sourced_from: The Book Of Why  The New Science Of Cause And Effect ( Pdfdrive )
---

# Estimand (Causal Inference)

## Definition
In the context of the Causal Inference Engine, an estimand is a mathematical formula that serves as a recipe for generating the answer to a causal query. It is the second output of the engine, produced after a query is deemed answerable from the given causal model and before any specific data is processed.

## Role in Causal Inference
The estimand's primary role is to bridge the gap between the causal question and the available observational data. Data are described as "profoundly dumb about causal relationships" and only provide statistical quantities like P(L | D). The estimand, which is derived from the causal model's assumptions, provides the logical steps to combine these statistical quantities into an expression that is equivalent to the causal query, such as P(L | do(D)).

## Distinction from Traditional Statistics
This concept represents a significant departure from traditional statistical analysis, where the query and the estimand typically coincide. For instance, in traditional statistics, if the query is the proportion of people with Lifespan L who took Drug D, the estimand is simply P(D | L). In causal inference, the causal query (e.g., P(L | do(D))) is distinct from the estimand, which might be a more complex formula involving various observed probabilities. The entire notion of a separate estimand generated from a model does not exist in traditional statistical methods.

## Relationships

- **is_produced_by**: [[causal-inference-engine|Causal Inference Engine]]

---
*Extracted from: The Book Of Why  The New Science Of Cause And Effect ( Pdfdrive )*