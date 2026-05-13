---
type: concept
aliases: [Difference-in-Differences]
summary: A statistical method used to estimate the causal effect of a specific intervention by comparing the change in outcomes over time between a treatment group and a control group. An econometric method used to estimate the causal effect of an intervention by comparing the change in outcomes over time between a treatment group and a control group, particularly when treatment timing is staggered.
relationships:
  - target: ai-assistance-in-the-workplace
    type: is_used_to_measure
  - target: resolutions-per-hour
    type: measures_impact_on
  - target: fixed-effects
    type: uses
  - target: sun-abraham-estimator
    type: is_a_type_of
  - target: callaway-santanna-estimator
    type: is_a_type_of
  - target: heterogeneous-treatment-effects
    type: is_used_to_analyze
tags: [econometrics, causal-inference, statistical-method]
sourced_from: 2304.11771V2
---

# Difference-in-Differences

## Definition and Formula
Difference-in-Differences is a standard empirical strategy used to isolate the causal impact of an intervention. The study employs a regression model represented as $y_{it} = \delta_t + \alpha_i + \beta AI_{it} + \gamma X_{it} + \epsilon_{it}$. In this model, the coefficient $\beta$ on the treatment variable $AI_{it}$ captures the causal effect of interest, representing the impact of AI access.

## Application in the Study
This method is used to measure the causal impact of providing customer service agents with access to AI recommendations. It compares the performance of agents before and after they receive access to the AI tool (the "treated" group) against the performance of agents who never receive access (the "never-treated" or control group) over the same period. This approach allows researchers to attribute raw performance differences to the AI model's deployment while accounting for other factors.

## Key Variables and Controls
The outcome variables ($y_{it}$) in the analysis include productivity measures like average chat duration (handle time), chats handled per hour, chat resolution rates, and customer satisfaction scores. The model includes fixed effects for year-month ($\delta_t$), agent ($\alpha_i$), location, and agent tenure to control for potential confounding factors such as agent experience or differences in selection into treatment, thereby isolating the specific effect of the AI assistance.

## Relationships

- **is_used_to_measure**: [[ai-assistance-in-the-workplace|Ai Assistance In The Workplace]]
- **measures_impact_on**: [[resolutions-per-hour|Resolutions Per Hour]]
- **uses**: [[fixed-effects|Fixed Effects]]
- **is_a_type_of**: [[sun-abraham-estimator|Sun Abraham Estimator]]
- **is_a_type_of**: [[callaway-santanna-estimator|Callaway Santanna Estimator]]
- **is_used_to_analyze**: [[heterogeneous-treatment-effects|Heterogeneous Treatment Effects]]

---
*Extracted from: 2304.11771V2*