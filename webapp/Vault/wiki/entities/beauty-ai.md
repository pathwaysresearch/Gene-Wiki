---
type: entity
aliases: [Beauty.AI]
summary: An international beauty contest judged by an AI that became a prominent example of algorithmic bias due to a lack of diversity in its training data.
relationships:
  - target: algorithmic-bias
    type: is_an_example_of
tags: [ai-project, algorithmic-bias, case-study]
sourced_from: Ai
---

# Beauty.AI

## Overview
Beauty.AI was an international beauty contest staged in 2016 by a Russian company called Youth Laboratories. The contest was unique in that the judging was performed by an artificial intelligence system and received support from companies like Microsoft and Nvidia.

## The Biased Outcome
Despite thousands of contestants from diverse backgrounds, including many from Africa and India, the AI selected forty-four winners who were predominantly white. Only a few winners were Asian, and just one had dark skin. This outcome was a clear demonstration of algorithmic bias.

## Cause of the Bias
The CTO of Youth Laboratories attributed the biased results to a lack of diversity in the training dataset used to build the AI judge. The company had trained its algorithms on off-the-shelf, open-source datasets. This practice is a common way for biases to spread, as the "established norm" in such datasets may not be representative of global diversity, causing the AI to struggle with faces that deviate from that norm.

## Relationships

- **is_an_example_of**: [[algorithmic-bias|Algorithmic Bias]]

---
*Extracted from: Ai*