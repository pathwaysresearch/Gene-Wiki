---
type: concept
aliases: [Causal Model]
summary: A representation of causal relationships within a system, typically using a diagram with arrows to show the direction of influence. A formal representation of the data-generating process that is essential for answering causal questions, as opposed to purely associational ones. A mathematical representation of causal relationships that encodes assumptions about the world, enabling the answering of causal and counterfactual questions from data.
relationships:
  - target: counterfactual-reasoning
    type: enables
  - target: data-mining
    type: contrasts_with
  - target: mediation-analysis
    type: prerequisite_for
  - target: structural-causal-models
    type: has_subtype
  - target: path-analysis
    type: is_a_precursor_to
  - target: causal-inference-engine
    type: is_a_component_of
tags: [causality, modeling, graphical-models, causal-inference, scientific-method, statistics]
sourced_from: The Book Of Why  The New Science Of Cause And Effect ( Pdfdrive )
---

# Causal Model

## Structure and Function
A causal model, often visualized as a causal diagram, uses arrows to represent causal relationships between variables (e.g., an arrow from X to Y implies X causes Y). These models are more than just drawings; they entail implicit probability rules that specify how a change in a cause variable would affect its effect.

## Power of Structure
A key feature of causal models is that their graphical structure alone can often be sufficient to answer causal and counterfactual questions. This allows for the estimation of various relationships—deterministic or probabilistic, linear or nonlinear—sometimes without needing to specify the exact mathematical functions behind the arrows.

## A General Procedure for Causal Queries
The text outlines a universal routine for using causal models to answer queries. The process involves translating a story into a causal diagram, identifying the query type (associational, interventional, or counterfactual), performing a "surgery" on the model for interventional or counterfactual queries, and then using the modified model to compute the answer. This flexible approach works across diverse scenarios.

## Relationships

- **enables**: [[counterfactual-reasoning|Counterfactual Reasoning]]
- **contrasts_with**: [[data-mining|Data Mining]]
- **prerequisite_for**: [[mediation-analysis|Mediation Analysis]]
- **has_subtype**: [[structural-causal-models|Structural Causal Models]]
- **is_a_precursor_to**: [[path-analysis|Path Analysis]]
- **is_a_component_of**: [[causal-inference-engine|Causal Inference Engine]]

---
*Extracted from: The Book Of Why  The New Science Of Cause And Effect ( Pdfdrive )*