---
type: concept
aliases: [Decision-Theoretic Metareasoning]
summary: A technique for controlling an agent's deliberation by applying decision theory to the process of computation itself, weighing the costs and benefits of thinking.
relationships:
  - target: anytime-algorithm
    type: is-a-method-for-controlling
tags: [metareasoning, decision-theory, agent-architecture]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Decision-Theoretic Metareasoning

## Definition
Decision-theoretic metareasoning is a method for controlling an agent's deliberation process. The text explains that it "applies the theory of information value... to the selection of individual computations." In essence, it is the process of reasoning about which computations to perform.

## How It Works
The value of any given computation is assessed based on two key factors: its cost and its benefits. The cost is primarily the time it takes, which results in a delay of action. The benefits are measured by the expected improvement in the quality of the agent's final decision.

## Purpose in AI
This technique provides a general and principled method for an agent to manage its computational resources. Instead of relying on fixed rules, the agent can dynamically decide whether it is better to act immediately with its current knowledge or to continue deliberating to refine its plan, making it crucial for agents in complex, real-time domains.

## Relationships

- **is-a-method-for-controlling**: [[anytime-algorithm|Anytime Algorithm]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*