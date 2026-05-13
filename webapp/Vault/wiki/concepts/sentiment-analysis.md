---
type: concept
aliases: [Sentiment Analysis]
summary: A method used to capture the affective nature and emotional tone of text, as applied to conversations between customer service agents and customers.
relationships:
  - target: siebert
    type: implemented_with
  - target: generative-ai-assistance-in-customer-service
    type: evaluates
tags: [natural-language-processing, text-analysis, methodology]
sourced_from: 2304.11771V2
---

# Sentiment Analysis

## Definition
As referenced in the study, sentiment analysis is a technique for capturing the affective nature of text. It is used to systematically evaluate the emotional tone within written communication, such as identifying frustration, satisfaction, or neutrality.

## Application in the Study
The researchers employed sentiment analysis to assess how AI assistance impacted the way customers treat agents. The goal was to investigate whether AI-suggested language improved the tenor of conversations by helping agents resolve issues faster, or if it made interactions feel more 'corporate' and insincere, potentially increasing customer frustration. The analysis specifically looked for instances of swearing, verbal abuse, and 'yelling' (typing in all caps) from customers.

## Methodology
For this analysis, the study utilized SiEBERT, a Large Language Model (LLM) specifically fine-tuned for sentiment analysis. SiEBERT was trained on a variety of datasets, including product reviews and tweets, making it well-suited to interpret the emotional content of customer service chats. This specific tool was chosen to provide a systematic measure of the emotional content in both agent and customer text.

## Relationships

- **implemented_with**: [[siebert|Siebert]]
- **evaluates**: [[generative-ai-assistance-in-customer-service|Generative Ai Assistance In Customer Service]]

---
*Extracted from: 2304.11771V2*