---
type: concept
aliases: [Causal Diagram]
summary: A graphical model that represents causal relationships between variables, used to identify confounders, colliders, and determine appropriate statistical adjustments.
relationships:
  - target: simpsons-paradox
    type: is_used_to_resolve
  - target: lords-paradox
    type: is_used_to_resolve
  - target: confounder
    type: is_used_to_identify
tags: [causality, graphical-models, methodology]
sourced_from: The Book Of Why  The New Science Of Cause And Effect ( Pdfdrive )
---

# Causal Diagram

## Purpose and Importance
Causal diagrams are presented as an essential tool for moving beyond raw data to understand the data-generating process. The text asserts that it is "practically impossible" to discuss this process or answer causal questions without them. These diagrams encode crucial, often commonsensical, assumptions about the causal relationships between variables, making them explicit and open to analysis.

## Application in Resolving Paradoxes
The excerpts demonstrate the power of causal diagrams in resolving long-standing statistical paradoxes. For Simpson's Paradox, the diagram (Figure 6.4) clearly identifies Gender as a confounder, dictating that the data must be stratified. For Lord's Paradox, the diagram (Figure 6.8) clarifies the relationships between Sex, Initial Weight, and Final Weight, showing that a simple comparison of weight gain is appropriate and no adjustment is needed.

## A Formal Language for Causation
The text highlights that causal diagrams provide a formal, well-defined language for causation that was previously lacking in statistics. This addresses the frustration expressed by statisticians like Dennis Lindley and Melvin Novick, who recognized the need for causal information but felt the concept was too ill-defined to be used formally. The diagrams provide the rigorous framework they were missing.

## Relationships

- **is_used_to_resolve**: [[simpsons-paradox|Simpsons Paradox]]
- **is_used_to_resolve**: [[lords-paradox|Lords Paradox]]
- **is_used_to_identify**: [[confounder|Confounder]]

---
*Extracted from: The Book Of Why  The New Science Of Cause And Effect ( Pdfdrive )*