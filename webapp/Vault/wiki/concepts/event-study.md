---
type: concept
aliases: [Event Study]
summary: A statistical method used to examine the impact of an event by observing changes in a variable around the time of the event. A statistical method used to measure the effect of an event by analyzing data in periods before and after the event occurs, often to assess dynamic effects and test for pre-existing trends.
relationships:
  - target: customer-sentiment
    type: is_used_to_analyze
  - target: agent-sentiment
    type: is_used_to_analyze
  - target: sun-abraham-estimator
    type: uses
tags: [econometrics, statistical-method, visualization, causal-inference, time-series-analysis]
sourced_from: 2304.11771V2
---

# Event Study

## Definition
An event study is a method used to measure the impact of a specific event on a variable of interest. It involves aligning data relative to the event date (time 0) and plotting the variable's average change in the periods before and after the event, often with confidence intervals to show statistical significance.

## Application in the Study
The paper employs event studies to visualize the impact of the AI system rollout on several outcomes, including chat duration, customer sentiment, and agent sentiment. These plots show the evolution of the outcome variable for months leading up to the AI deployment and for months following it, providing a clear visual representation of the intervention's effect over time.

## Interpretation of Plots
In the study's event study plots, the x-axis represents months relative to AI deployment, with 0 marking the deployment month. The y-axis shows the change in the outcome variable. The plots for customer sentiment (Figure 10A) show that data points are clustered around zero before deployment, indicating no pre-existing trend, and then become significantly positive after deployment, suggesting a positive impact from the AI.

## Relationships

- **is_used_to_analyze**: [[customer-sentiment|Customer Sentiment]]
- **is_used_to_analyze**: [[agent-sentiment|Agent Sentiment]]
- **uses**: [[sun-abraham-estimator|Sun Abraham Estimator]]

---
*Extracted from: 2304.11771V2*