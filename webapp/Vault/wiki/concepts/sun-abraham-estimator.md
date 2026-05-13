---
type: concept
aliases: [Sun-Abraham Estimator]
summary: A robust difference-in-differences estimator designed to provide unbiased estimates in studies with staggered treatment adoption by using an interaction-weighted approach.
relationships:
  - target: difference-in-differences
    type: is_a_type_of
  - target: event-study
    type: used_in
tags: [econometrics, causal-inference, did-estimator]
sourced_from: 2304.11771V2
---

# Sun-Abraham Estimator

## Overview
The Sun and Abraham (2021) estimator is a modern econometric technique for difference-in-differences (DiD) analysis. It is specifically designed to address biases that can arise in traditional DiD models when different units (e.g., agents) receive a treatment at different points in time, a situation known as staggered adoption.

## Application in the Study
This estimator is applied in two key parts of the paper's analysis. First, it is used to generate the event study regressions shown in Figure A.3, which plot the dynamic effects of AI deployment on agent performance. The notes explicitly state the use of the "Sun and Abraham (2021) interaction weighted estimator." Second, it is included in the comparison of robust DiD estimators in Table A.9, where it is used to calculate the average treatment effect on resolutions per hour.

## Performance and Significance
In the comparative analysis of DiD methods (Table A.9), the Sun-Abraham estimator produces a point estimate of 0.521 for the impact on resolutions per hour. This result is substantially larger than the estimate from the conventional TWFE-OLS model (0.296) and is in line with other modern robust estimators. This highlights its importance in providing a more accurate measure of the AI's impact in a real-world setting with staggered implementation.

## Relationships

- **is_a_type_of**: [[difference-in-differences|Difference In Differences]]
- **used_in**: [[event-study|Event Study]]

---
*Extracted from: 2304.11771V2*