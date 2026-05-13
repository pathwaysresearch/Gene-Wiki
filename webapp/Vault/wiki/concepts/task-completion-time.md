---
type: concept
aliases: [Task Completion Time]
summary: The primary performance metric in the GitHub Copilot study, defined as the time elapsed from starting the assignment to the first successful code submission.
relationships:
  - target: controlled-experiment-on-ai-developer-productivity
    type: is_metric_for
tags: [performance-metric, experiment-design, productivity]
sourced_from: 2302.06590V1
---

# Task Completion Time

## Definition
In the context of this experiment, task completion time was the key dependent variable used to objectively measure developer productivity. It was precisely defined as the total time elapsed between the timestamp of a participant's personal repository creation and the timestamp of their first code commit that successfully passed all 12 checks in the provided test suite.

## Measurement Methodology
The measurement process was automated and standardized using GitHub Classroom. The start time was logged the moment a participant clicked the link to join the assignment, which created their personal repository. The end time was recorded when a participant pushed a commit to GitHub that triggered the automated test suite and resulted in all twelve checks passing. The number of commits made during the task had no impact on this final measurement.

## Experimental Results
The study found a substantial and statistically significant difference in task completion time between the two experimental groups. The treatment group, which had access to GitHub Copilot, was 55.8% faster than the control group. The distribution of completion times showed that the treated group's times were heavily concentrated at the lower end of the scale, while the control group's times were more spread out and had a much higher average.

## Relationships

- **is_metric_for**: [[controlled-experiment-on-ai-developer-productivity|Controlled Experiment On Ai Developer Productivity]]

---
*Extracted from: 2302.06590V1*