---
type: concept
aliases: [Predictability-Resilience Paradox]
summary: The trade-off in algorithmic design between creating predictable, rule-based systems with limited flexibility and developing resilient, adaptive systems that are less understandable.
relationships:
  - target: explainability
    type: creates_need_for
  - target: alphago
    type: exemplifies_resilient_side_of
tags: [ai-design, machine-learning, explainable-ai]
sourced_from: A Human'S Guide To Machine Intelligence Pdf
---

# Predictability-Resilience Paradox

## Definition

The Predictability-Resilience Paradox describes a fundamental trade-off in the design of AI systems. On one hand, systems can be built with explicit rules, making them highly predictable but also rigid and inflexible. On the other hand, systems can be designed for resilience and adaptability, like those using machine learning, but their inner workings and decision processes become less transparent and understandable.

## Predictable Systems and Their Limits

Algorithms based on explicit rules, such as tax software, perform well in predictable environments but fail when faced with complex, human-like decision-making, a challenge highlighted by Polanyi's paradox. A key vulnerability of predictable algorithms is that they are prone to manipulation; the text cites Google's PageRank system as an example where knowledge of the algorithm can lead to exploitation.

## Resilient Systems and Explainability

Resilient systems, such as AlphaGo, can achieve superhuman performance and exhibit unexpected creativity by learning from data rather than following rigid rules. However, their very unpredictability and complexity create a significant challenge for explainability, making it difficult to understand why they make certain decisions. This lack of transparency is a major concern when such systems are used for critical life decisions.

## Relationships

- **creates_need_for**: [[explainability|Explainability]]
- **exemplifies_resilient_side_of**: [[alphago|Alphago]]

---
*Extracted from: A Human'S Guide To Machine Intelligence Pdf*