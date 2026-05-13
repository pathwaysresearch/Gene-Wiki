---
type: concept
aliases: [Causal Network]
summary: A graphical model that represents causal assumptions through directed arrows, where the structure implies specific conditional independence relationships among variables that can be tested against data.
relationships:
  - target: confounding-bias
    type: helps-identify
tags: [causal-inference, graphical-models]
sourced_from: The Book Of Why  The New Science Of Cause And Effect ( Pdfdrive )
---

# Causal Network

## Definition
A causal network, also referred to as a causal diagram, is a model that visually represents causal relationships between variables. Each arrow in the network can be interpreted as a statement about the outcome of a hypothetical experiment, conveying the entirety of the causal knowledge assumed by the model.

## Relationship to Data
Causal networks are not arbitrary; they are subject to empirical scrutiny and can be falsified by data. The graphical structure dictates specific conditional independence conditions. For example, a chain model A → B → C implies that A and C are independent conditional on B. If observed data do not show this independence, the model is considered incompatible with the data and must be revised or discarded.

## Indistinguishability
A key implication of using causal networks is that some different causal structures can be indistinguishable based on observational data alone. For instance, a fork structure A ← B → C implies the same conditional independence (A is independent of C given B) as a chain structure A → B → C. This means that no amount of data can distinguish between these two models without further causal assumptions or interventions.

## Relationships

- **helps-identify**: [[confounding-bias|Confounding Bias]]

---
*Extracted from: The Book Of Why  The New Science Of Cause And Effect ( Pdfdrive )*