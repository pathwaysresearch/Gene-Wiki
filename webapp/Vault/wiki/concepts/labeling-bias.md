---
type: concept
aliases: [Labeling Bias]
summary: A form of algorithmic bias that arises when human-generated labels or tags for training data reflect societal prejudices or stereotypes.
relationships:
  - target: algorithmic-bias
    type: is_a_type_of
tags: [ai-ethics, data-labeling, crowdsourcing]
sourced_from: Ai
---

# Labeling Bias

## Definition
Labeling bias is a specific type of bias that is introduced into an AI system during the data labeling or tagging phase. This often occurs when the task is crowdsourced, and the human workers who are labeling the data embed their own conscious or unconscious biases into the descriptions and tags they create.

## How It Occurs
The process of creating labeled datasets for training machine learning models often relies on human input. If the individuals providing these labels hold biased views, those views can become encoded in the dataset. In a 2016 paper, Emiel van Miltenburg studied the Flickr30k dataset and found that crowdsourced labels exhibited clear bias, such as tagging an image of a woman and a man as a conversation between a "woman" and her "boss."

## Impact
This form of bias can lead to AI systems that perpetuate and even amplify harmful stereotypes. Because many developers use off-the-shelf, open-source datasets to train their algorithms, labeling bias present in one popular dataset can spread to numerous different applications, creating a systemic problem.

## Relationships

- **is_a_type_of**: [[algorithmic-bias|Algorithmic Bias]]

---
*Extracted from: Ai*