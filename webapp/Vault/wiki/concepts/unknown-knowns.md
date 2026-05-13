---
type: concept
aliases: [Unknown Knowns]
summary: A critical weakness of prediction machines where they produce a precise but wrong prediction because they fail to understand the causal process that generated the data. A cognitive trap where decision-makers misinterpret predictions by failing to account for missing data or the process that generated the data, often confusing correlation with causation.
relationships:
  - target: known-knowns
    type: part-of-same-framework
  - target: known-unknowns
    type: part-of-same-framework
  - target: unknown-unknowns
    type: part-of-same-framework
  - target: abraham-wald
    type: exemplified_by
tags: [prediction-framework, causal-inference, machine-learning-failure, cognitive-bias, data-analysis, decision-making]
sourced_from: Prediction Machines The Simple Economics Of Artificial Intelligence By Ajay Agrawal 
---

# Unknown Knowns

## Definition
An "unknown known" is a situation where a prediction machine provides a very precise answer that it is confident is correct, but that answer is fundamentally wrong. This is described as perhaps the biggest weakness of prediction machines.

## Causal Misinterpretation
This error occurs because the machine does not understand the decision process that generated the data it was trained on. Data can be a result of decisions (like pricing), and if the machine mistakes correlation for causation, its predictions will fail when conditions change.

## Example: Hotel Pricing
The text illustrates this with the hotel industry, where data shows high prices correlate with high sales (peak season). A naive machine might predict that raising prices will increase sales. A human with economic training would understand that high demand causes both high prices and high sales, and can work with the machine to build a better model, turning an "unknown known" into a "known unknown" or even a "known known."

## Relationships

- **part-of-same-framework**: [[known-knowns|Known Knowns]]
- **part-of-same-framework**: [[known-unknowns|Known Unknowns]]
- **part-of-same-framework**: [[unknown-unknowns|Unknown Unknowns]]
- **exemplified_by**: [[abraham-wald|Abraham Wald]]

---
*Extracted from: Prediction Machines The Simple Economics Of Artificial Intelligence By Ajay Agrawal *