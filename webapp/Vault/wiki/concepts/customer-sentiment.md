---
type: concept
aliases: [Customer Sentiment]
summary: A metric that quantifies the emotional tone of a customer's text during a chat-based interaction, measured on a scale from negative to positive.
relationships:
  - target: agent-sentiment
    type: is_distinct_from
tags: [performance-metric, nlp, customer-experience]
sourced_from: 2304.11771V2
---

# Customer Sentiment

## Definition
Customer sentiment is a measure that reflects the emotional experience of a customer during a chat-based interaction with a support agent. It is calculated based on the text written by the customer to capture their emotional state during the conversation.

## Calculation
To calculate customer sentiment, the study uses a model that analyzes the customer's text from each chat. The model produces a sentiment score on a scale from -1 (indicating negative sentiment) to 1 (indicating positive sentiment). These chat-level scores are then aggregated to create a measure of average customer sentiment for each agent-month, as individual chat-level surveys are not always completed.

## Findings in the Study
The event study analysis presented in Figure 10A shows a significant increase in average customer sentiment immediately following the deployment of the AI assistant. This suggests that the AI tool helped agents improve the customer's experience during support interactions, leading to a more positive emotional response from customers.

## Relationships

- **is_distinct_from**: [[agent-sentiment|Agent Sentiment]]

---
*Extracted from: 2304.11771V2*