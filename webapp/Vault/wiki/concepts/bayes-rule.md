---
type: concept
aliases: [Bayes' Rule]
summary: A fundamental theorem of probability that relates the conditional probabilities of two events, allowing the updating of beliefs in light of new evidence. It is a cornerstone of modern AI systems for probabilistic inference.
relationships:
  - target: prior-probability
    type: relates
  - target: posterior-probability
    type: relates
  - target: conditional-probability
    type: relates
tags: [probability-theory, bayesian-inference, machine-learning, ai]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Bayes' Rule

## Definition and Forms
Bayes' rule, also known as Bayes' law or Bayes' theorem, is a simple equation that underlies most modern AI systems for probabilistic inference. In its basic form, it is written as $P(b|a) = \frac{P(a|b)P(b)}{P(a)}$. The rule can be generalized for multivalued variables as $\mathbf{P}(Y|X) = \frac{\mathbf{P}(X|Y)\mathbf{P}(Y)}{\mathbf{P}(X)}$ and can also be conditionalized on background evidence $\mathbf{e}$: $\mathbf{P}(Y|X, \mathbf{e}) = \frac{\mathbf{P}(X|Y, \mathbf{e})\mathbf{P}(Y|\mathbf{e})}{\mathbf{P}(X|\mathbf{e})}$.

## Application in Causal Reasoning
Bayes' rule is particularly useful in practice for diagnostic or causal reasoning, where we observe an effect and want to infer the probability of an underlying cause. The rule can be expressed as $P(\text{cause}|\text{effect}) = \frac{P(\text{effect}|\text{cause})P(\text{cause})}{P(\text{effect})}$. This is powerful because it is often easier to acquire probability estimates for the causal direction, $P(\text{effect}|\text{cause})$, than for the diagnostic direction, $P(\text{cause}|\text{effect})$.

## Challenge with Multiple Evidence
A key challenge arises when applying Bayes' rule to combine multiple pieces of evidence. A naive application to compute $P(\text{Cause}|\text{Evidence}_1 \wedge \text{Evidence}_2)$ requires knowing the conditional probability of the conjoined evidence, $P(\text{Evidence}_1 \wedge \text{Evidence}_2 | \text{Cause})$. This approach does not scale well, because if there are $n$ evidence variables, one would need to know conditional probabilities for $2^n$ combinations of evidence values, reintroducing the same intractability as the full joint distribution.

## Relationships

- **relates**: [[conditional-probability|Conditional Probability]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*

---
*Also referenced in: Deep+Learning+Ian+Goodfellow*