---
type: concept
aliases: [Instrumental Variables Approach for Innovation]
summary: A statistical method used in the study to establish a causal link between innovation and new work, using breakthrough patents to instrument for subsequent augmentation and automation patent flows.
relationships:
  - target: breakthrough-innovation
    type: uses
  - target: augmentation
    type: estimates_causal_effect_of
  - target: automation
    type: estimates_causal_effect_of
tags: [econometrics, causal-inference, innovation-studies]
sourced_from: Acss Newfrontiers 20220814
---

# Instrumental Variables Approach for Innovation

## Rationale
To move beyond correlation and establish a causal link between innovation and new work creation, the study employs an instrumental variables (IV) strategy. The core identification assumption is that the precise timing of breakthrough innovations is not anticipated by economic agents, but the arrival of these breakthroughs causally affects the flow of subsequent, follow-on innovations.

## Implementation
The IV approach is implemented in several steps. First, it uses the flow of breakthrough patents in a given technology class from a past period (e.g., decade t-20) to predict the total flow of patents in that class in a later period. Second, it uses historical data (from t-20) to calculate each occupation's exposure to different patent classes for both augmentation and automation. Finally, it combines the breakthrough-induced patent flows with these historical exposure weights to create instruments for the observed augmentation and automation patent flows in the current period (decade t).

## Findings
The results from this 2SLS (Two-Stage Least Squares) estimation corroborate the findings from the OLS models. They confirm that augmentation innovations have a robustly positive causal effect on the emergence of new job titles. This provides stronger evidence that augmentation technology actively catalyzes the creation of new work.

## Relationships

- **uses**: [[breakthrough-innovation|Breakthrough Innovation]]
- **estimates_causal_effect_of**: [[augmentation|Augmentation]]
- **estimates_causal_effect_of**: [[automation|Automation]]

---
*Extracted from: Acss Newfrontiers 20220814*