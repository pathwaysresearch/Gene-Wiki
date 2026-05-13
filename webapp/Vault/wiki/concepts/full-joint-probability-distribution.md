---
type: concept
aliases: [Full Joint Probability Distribution]
summary: A probability distribution that specifies the probabilities for all possible combinations of values for all random variables in a domain. It serves as the theoretical foundation for probabilistic reasoning.
relationships:
  - target: marginalization
    type: is_input_for
tags: [probability-theory, probabilistic-reasoning, knowledge-representation]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Full Joint Probability Distribution

## Definition
A full joint probability distribution completely specifies a probability model by assigning a probability to every possible combination of values for all random variables in the domain. For a domain with variables *Cavity*, *Toothache*, and *Weather*, the full joint distribution is denoted by **P**(*Cavity*, *Toothache*, *Weather*) and can be represented as a table with an entry for each combination of these variables' values.

## Role in Probabilistic Inference
In principle, a full joint probability distribution is sufficient for calculating the probability of any proposition. To find the probability of a proposition, one must identify all the possible worlds (i.e., rows in the joint distribution table) in which the proposition is true and then sum their associated probabilities. For example, the probability of $cavity \lor toothache$ is found by summing the probabilities of all entries in the table where either *cavity* or *toothache* is true.

## Scalability Limitations
While foundational, the full joint probability distribution is not a practical tool for building reasoning systems of any significant size. Its primary limitation is scalability. For a domain described by $n$ Boolean variables, the distribution requires a table of size $O(2^n)$, and processing it takes $O(2^n)$ time. This becomes computationally intractable for realistic problems, which can easily have more than 100 variables. Therefore, it is viewed as a theoretical basis upon which more efficient methods are built.

## Relationships

- **is_input_for**: [[marginalization|Marginalization]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*