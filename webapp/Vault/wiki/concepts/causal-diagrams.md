---
type: concept
aliases: [Causal Diagrams]
summary: Pictorial models that use dots (variables) and arrows (causal relationships) to explicitly represent the cause-effect structure of a system.
relationships:
  - target: causal-inference-engine
    type: is_used_by
  - target: causal-models
    type: represents
tags: [causality, modeling, graph-theory]
sourced_from: The Book Of Why  The New Science Of Cause And Effect ( Pdfdrive )
---

# Causal Diagrams

## Definition
Causal diagrams are explicit "dots-and-arrows" pictures that visually represent the intricate web of cause-effect relationships that structure our knowledge of the world. They serve as a formal and computable representation of a causal model, making abstract causal assumptions concrete and analyzable.

## Function and Use
These diagrams are the computational core of the "causal inference engine." They are essential tools for answering causal questions from all rungs of the Ladder of Causation, including association, intervention, and counterfactuals. By inspecting the graph and tracing the rules represented by the arrows, a user or a computer can deduce logical consequences and determine if a causal effect can be estimated from data.

## Example: The Firing Squad
A provided example illustrates a firing squad scenario where a diagram shows the chain of events: a court order (CO) causes a captain (C) to signal, which causes soldiers (A and B) to fire, which in turn causes the prisoner's death (D). Each node is a true/false variable. This diagram allows for reasoning about associations (e.g., if the prisoner is dead, the court order must have been given) by tracing the causal pathways.

## Relationships

- **is_used_by**: [[causal-inference-engine|Causal Inference Engine]]
- **represents**: [[causal-models|Causal Models]]

---
*Extracted from: The Book Of Why  The New Science Of Cause And Effect ( Pdfdrive )*