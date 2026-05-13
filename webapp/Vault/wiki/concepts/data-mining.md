---
type: concept
aliases: [Data Mining]
summary: The practice of searching large datasets to find patterns and correlations, which is insufficient for answering causal questions on its own.
relationships:
  - target: causal-model
    type: contrasts_with
tags: [data-analysis, statistics, big-data, correlation]
sourced_from: The Book Of Why  The New Science Of Cause And Effect ( Pdfdrive )
---

# Data Mining

## Role and Function
Data mining is presented as the practice of analyzing large datasets to find interesting patterns of association. The text acknowledges its value as an "essential first step" in the scientific process. It can help refine broad questions into more precise, testable hypotheses by identifying strong correlations that warrant further investigation.

## Limitations in Causal Inference
The author argues that data mining is fundamentally incapable of answering causal questions by itself. The text warns against the hype and "almost religious faith" that answers can be found in the data alone. Any analysis that is "model-free" can only summarize or transform data, not interpret it. To move from correlation to causation, one must formulate a causal model of the data-generating process.

## Example Application
The text provides a clear example to illustrate the distinction between data mining and causal analysis. A data mining approach might scan the human genome and find a gene highly correlated with lung cancer. This is a valuable finding. However, data mining cannot answer the subsequent, causal question: "Does this gene cause lung cancer?" Answering that question requires a causal model and a different set of inferential tools.

## Relationships

- **contrasts_with**: [[causal-model|Causal Model]]

---
*Extracted from: The Book Of Why  The New Science Of Cause And Effect ( Pdfdrive )*