---
type: concept
aliases: [Structural Causal Models (SCMs)]
summary: A modeling framework that represents causal relationships using a set of equations, where each equation describes how a variable is determined by its direct causes.
relationships:
  - target: causal-model
    type: is_a_type_of
  - target: structural-equation-model
    type: is_a_generalization_of
tags: [causal-inference, modeling, graphical-models]
sourced_from: The Book Of Why  The New Science Of Cause And Effect ( Pdfdrive )
---

# Structural Causal Models (SCMs)

## Definition
Structural Causal Models (SCMs) are a formal framework for representing causal knowledge and answering causal questions. As referenced in the text, an SCM consists of a set of variables and a corresponding set of functions or equations that specify how each variable's value is determined by the values of its immediate causes.

## Function in Causal Inference
SCMs provide the mathematical foundation for the Causal Revolution. They serve as the engine for answering queries at all three levels of the Ladder of Causation. Interventions are modeled by modifying one or more equations in the system (an operation called "equation deletion" in some contexts), and counterfactuals are computed by solving the modified system of equations under specific evidence.

## Relationship to Other Models
SCMs are a generalization of the structural equation models (SEMs) traditionally used in social sciences and economics. While SEMs were often used to model correlational data, SCMs give the equations a direct causal interpretation, which allows for interventional and counterfactual reasoning.

## Relationships

- **is_a_type_of**: [[causal-model|Causal Model]]
- **is_a_generalization_of**: [[structural-equation-model|Structural Equation Model]]

---
*Extracted from: The Book Of Why  The New Science Of Cause And Effect ( Pdfdrive )*