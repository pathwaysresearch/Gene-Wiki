---
type: concept
aliases: [Self-reported Productivity Gain]
summary: A subjective measure collected via an exit survey where participants estimated the percentage of productivity gain or loss from using GitHub Copilot.
relationships:
  - target: controlled-experiment-on-ai-developer-productivity
    type: is_metric_for
  - target: task-completion-time
    type: contrasted_with
tags: [survey-data, subjective-metric, user-perception]
sourced_from: 2302.06590V1
---

# Self-reported Productivity Gain

## Definition
Self-reported productivity gain refers to the participants' own estimation of how much their productivity was affected by using GitHub Copilot. This subjective measure was collected through a question in the exit survey, which asked participants to estimate the productivity gain or loss in percentage terms for completing the task.

## Data Collection
The survey question was posed to both the treatment group, who had used Copilot for the task, and the control group. To ensure the control group could provide an informed estimate despite not using the tool, they were shown a tutorial video explaining Copilot's features before they answered the question.

## Comparison with Observed Data
A key finding was the discrepancy between perceived and actual productivity gains. On average, participants in both the treated and control groups estimated a 35% increase in productivity from using Copilot. This was a significant underestimation when compared to the 55.8% faster task completion time that was objectively measured for the treatment group, suggesting that developers may not fully perceive the extent of the productivity benefits provided by the AI tool.

## Relationships

- **is_metric_for**: [[controlled-experiment-on-ai-developer-productivity|Controlled Experiment On Ai Developer Productivity]]
- **contrasted_with**: [[task-completion-time|Task Completion Time]]

---
*Extracted from: 2302.06590V1*