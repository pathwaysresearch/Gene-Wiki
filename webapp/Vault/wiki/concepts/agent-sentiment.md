---
type: concept
aliases: [Agent Sentiment]
summary: A metric that quantifies the emotional tone of an agent's text during a chat-based interaction, used to capture the tone of their responses.
relationships:
  - target: customer-sentiment
    type: is_distinct_from
tags: [performance-metric, nlp, agent-experience]
sourced_from: 2304.11771V2
---

# Agent Sentiment

## Definition
Agent sentiment is a measure that captures the tone of the responses provided by a support agent during a chat-based interaction. It is calculated separately from customer sentiment, focusing only on the text written by the agent to understand their emotional expression.

## Calculation
The study uses a sentiment analysis model to process the agent's text from each conversation. This model assigns a score on a scale from -1 (negative) to 1 (positive) for each piece of text. These individual scores are then aggregated to produce an average agent sentiment score for each agent-month.

## Application in the Study
Agent sentiment is used alongside customer sentiment to provide a more complete picture of the work experience and the nature of the agent-customer interaction. The paper analyzes it in an event study format (Figure 10B) to understand how the AI tool affected the emotional tone of the agents' own communications during support chats.

## Relationships

- **is_distinct_from**: [[customer-sentiment|Customer Sentiment]]

---
*Extracted from: 2304.11771V2*