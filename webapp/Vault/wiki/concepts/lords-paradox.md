---
type: concept
aliases: [Lord's Paradox]
summary: A statistical paradox concerning the analysis of group differences in change over time, highlighting the conflict between analyzing raw gain scores versus conditioning on initial values.
relationships:
  - target: frederic-lord
    type: formulated_by
  - target: causal-diagram
    type: is_resolved_by
tags: [statistics, paradox, causality]
sourced_from: The Book Of Why  The New Science Of Cause And Effect ( Pdfdrive )
---

# Lord's Paradox

## Overview
Originally stated by statistician Frederic Lord in 1967, Lord's Paradox is a fictitious thought experiment designed to probe the limits of statistical understanding. It involves a school studying the effects of its dining hall diet on student weight gain. The paradox arises when two different statisticians analyze the same data—one comparing raw weight gain between boys and girls, the other adjusting for initial weight—and arrive at conflicting conclusions.

## The Causal Structure
The text argues that the paradox can be rigorously answered by first drawing a causal diagram. The diagram shows that Sex is a common cause of both initial weight (W_I) and final weight (W_F). The variable of interest, weight gain (Y), is a deterministic function of the other two (Y = W_F - W_I). This graphical representation makes the underlying causal assumptions explicit.

## Resolution via Causal Diagram
By analyzing the causal diagram, the text concludes that the first statistician's approach—simply comparing the difference in weight gain between girls and boys—is correct in this case. The diagram reveals that there are no "back doors" between the Sex variable and the Gain variable that need to be blocked. Therefore, the observed, aggregate difference provides the correct answer without needing to condition on initial weight. The paradox is thus resolved by appealing to the causal story, not just the data.

## Relationships

- **formulated_by**: [[frederic-lord|Frederic Lord]]
- **is_resolved_by**: [[causal-diagram|Causal Diagram]]

---
*Extracted from: The Book Of Why  The New Science Of Cause And Effect ( Pdfdrive )*