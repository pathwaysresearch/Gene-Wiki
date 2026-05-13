---
type: concept
aliases: [Do-Calculus]
summary: A formal axiomatic system consisting of three rules for manipulating expressions involving the 'do-operator' to determine if a causal effect can be identified from observational data and a causal diagram. A set of rules developed by Judea Pearl for manipulating probability distributions under interventions, allowing for the estimation of causal effects from observational data. A formal system of rules for manipulating causal diagrams and probability distributions to determine if a causal effect can be identified from observational data.
relationships:
  - target: d-separation
    type: is_based_on
  - target: back-door-adjustment
    type: generalizes
  - target: front-door-adjustment
    type: is_a_proof_system_for
  - target: judea-pearl
    type: developed_by
  - target: back-door-criterion
    type: generalizes
  - target: do-operator
    type: uses
  - target: backdoor-criterion
    type: generalizes
  - target: front-door-adjustment
    type: generalizes
tags: [causal-inference, formal-methods, graphical-models, intervention, methodology]
sourced_from: The Book Of Why  The New Science Of Cause And Effect ( Pdfdrive )
---

# Do-Calculus

## Purpose
The do-calculus is a mathematical framework designed to determine whether a causal effect, expressed as P(Y | do(X)), can be calculated from purely observational data. Its goal is to provide a systematic procedure to transform an expression containing a `do`-operator into an equivalent expression that does not, thereby allowing the causal effect to be estimated without performing an actual intervention or experiment. This allows researchers to move from rung one (association) to rung two (intervention) of the Ladder of Causation using only data and a causal model.

## The Three Rules
The do-calculus is built on three fundamental transformation rules:
- **Rule 1 (Insertion/Deletion of Observation):** Allows for the addition or removal of a conditioning variable if it is blocked from the outcome on a specific subgraph. This rule is based on the d-separation property.
- **Rule 2 (Action/Observation Exchange):** Permits swapping a `do(X)` term with a standard conditioning on X, provided the conditioning set Z satisfies the back-door criterion relative to the path from X to Y.
- **Rule 3 (Insertion/Deletion of Action):** Allows for the removal of a `do(X)` operator entirely if there are no causal paths from X to the outcome variable Y.

## Significance and Completeness
The development of do-calculus was a major breakthrough, as it provided a complete algorithm for identifying causal effects. The three rules were proven to be sufficient, meaning if a causal effect can be identified, it can be found by applying these rules. The system has been extended by researchers like Elias Bareinboim to solve more complex problems, such as transportability (external validity), which assesses whether experimental results from one population can be generalized to another.

## Relationships

- **is_based_on**: [[d-separation|D Separation]]
- **generalizes**: [[back-door-adjustment|Back Door Adjustment]]
- **is_a_proof_system_for**: [[front-door-adjustment|Front Door Adjustment]]
- **developed_by**: [[judea-pearl|Judea Pearl]]
- **generalizes**: [[back-door-criterion|Back Door Criterion]]
- **uses**: [[do-operator|Do Operator]]
- **generalizes**: [[backdoor-criterion|Backdoor Criterion]]
- **generalizes**: [[front-door-adjustment|Front Door Adjustment]]

---
*Extracted from: The Book Of Why  The New Science Of Cause And Effect ( Pdfdrive )*