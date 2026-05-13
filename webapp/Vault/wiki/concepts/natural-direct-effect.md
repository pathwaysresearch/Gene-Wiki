---
type: concept
aliases: [Natural Direct Effect]
summary: A counterfactually defined direct effect that measures the impact of a treatment on an outcome while the mediator is set to the value it would have taken naturally without the treatment.
relationships:
  - target: direct-effect
    type: is_a_type_of
  - target: counterfactuals
    type: is_defined_by
tags: [causality, mediation, counterfactuals, statistics]
sourced_from: The Book Of Why  The New Science Of Cause And Effect ( Pdfdrive )
---

# Natural Direct Effect

## Definition
The Natural Direct Effect (NDE) is a type of direct effect defined using counterfactuals. It is designed to avoid the pitfalls of overcontrolled experiments where fixing a mediator to an arbitrary value might create an unnatural situation. The NDE measures the expected change in an outcome if the treatment variable is changed, while the mediator variable is set to whatever value it would have naturally taken in the absence of the treatment.

## Example and Formula
To measure the NDE of gender on admissions at Berkeley, the text proposes a hypothetical experiment: instruct applicants to report a randomized gender but apply to the department they would have otherwise preferred. This ensures the mediator (department choice) is at its "natural" level for each applicant. The formal definition is expressed as a counterfactual formula: NDE = P(Y_{M=M_0} = 1 | do(X = 1)) – P(Y_{M=M_0} = 1 | do(X = 0)), where M_0 is the value the mediator M would take under do(X=0).

## Significance
The NDE provides a more meaningful measure of direct effect in many policy and real-world scenarios compared to the Controlled Direct Effect (CDE), which fixes the mediator to a single value for all subjects. It allows the mediator to vary as it normally would for each individual under the control condition, providing a more realistic assessment of the direct impact.

## Relationships

- **is_a_type_of**: [[direct-effect|Direct Effect]]
- **is_defined_by**: [[counterfactuals|Counterfactuals]]

---
*Extracted from: The Book Of Why  The New Science Of Cause And Effect ( Pdfdrive )*