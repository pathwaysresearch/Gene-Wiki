---
type: concept
aliases: [Reward Function Engineering]
summary: The process of defining the objective or what "best" means for a decision-making system, which involves carefully considering and balancing various trade-offs.
relationships:
  - target: ziprecruiter
    type: is_exemplified_by
tags: [ai-strategy, optimization, business-objectives]
sourced_from: Prediction Machines The Simple Economics Of Artificial Intelligence By Ajay Agrawal 
---

# Reward Function Engineering

## Definition
Reward function engineering is the process of determining the ultimate goal or definition of success for a system. As illustrated by the pricing decisions at ZipRecruiter, it involves figuring out what "best" means when there are multiple, often competing, objectives. This is a critical step before a system can be optimized to make decisions.

## The Challenge of Trade-offs
The core challenge of reward function engineering is balancing trade-offs between different goals. The text uses ZipRecruiter's pricing problem to highlight this. A strategy to maximize short-term revenue (e.g., a high price) might negatively impact other important metrics like the total number of customers, word-of-mouth growth, the number of job postings on the platform, and long-term customer retention. Defining the reward function requires making explicit choices about how to weigh these different factors.

## Application in Practice
To engineer its reward function for pricing, ZipRecruiter brought in economists to design experiments. They randomly assigned different prices to customer leads to measure how various customer groups responded to different price points. This data allowed them to understand the quantitative relationships between price and outcomes like purchase likelihood, enabling them to make a more informed decision about how to balance the trade-off between short-term profit and long-term growth.

## Relationships

- **is_exemplified_by**: [[ziprecruiter|Ziprecruiter]]

---
*Extracted from: Prediction Machines The Simple Economics Of Artificial Intelligence By Ajay Agrawal *