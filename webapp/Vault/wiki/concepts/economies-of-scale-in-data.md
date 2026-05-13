---
type: concept
aliases: [Economies of Scale in Data]
summary: The principle that the benefit of additional data for prediction can have increasing or decreasing returns, with a key distinction between statistical and economic viewpoints.
relationships:
  - target: known-knowns
    type: is-a-precondition-for
tags: [data-economics, statistics, prediction]
sourced_from: Prediction Machines The Simple Economics Of Artificial Intelligence By Ajay Agrawal 
---

# Economies of Scale in Data

## Definition
Economies of scale in data refers to how the benefit of additional information—whether in terms of number of units, types of variables, or frequency—changes with the existing amount of data. In economist speak, this means data may have increasing or decreasing returns to scale.

## The Statistical View
From a purely statistical point of view, data has decreasing returns to scale. This means that each additional observation becomes progressively less useful for improving a prediction. The text notes that you get more useful information from the third observation than the hundredth, and much more from the hundredth observation than the millionth.

## Implications for Prediction
The principle of decreasing returns in statistics implies that as you add observations to your training data, the marginal improvement to your prediction diminishes. This is a fundamental consideration when deciding how much data to collect for a prediction task.

## Relationships

- **is-a-precondition-for**: [[known-knowns|Known Knowns]]

---
*Extracted from: Prediction Machines The Simple Economics Of Artificial Intelligence By Ajay Agrawal *