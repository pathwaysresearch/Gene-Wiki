---
type: concept
aliases: [Marginalization]
summary: The process of calculating the probability distribution of a subset of random variables from a larger joint probability distribution by summing out the other variables.
relationships:
  - target: full-joint-probability-distribution
    type: operates-on
tags: [probability-theory, inference, statistics]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Marginalization

## Definition
Marginalization, also known as summing out, is the process of deriving the probability distribution of a subset of variables from a full joint probability distribution. This is achieved by summing the probabilities over all possible values of the variables that are to be excluded. The general rule for any sets of variables **Y** and **Z** is given by $\mathbf{P}(\mathbf{Y}) = \sum_{\mathbf{z}} \mathbf{P}(\mathbf{Y}, \mathbf{z})$, where the sum is over all possible value combinations **z** of the variables in **Z**.

## Marginal Probability
The result of marginalization is the unconditional or marginal probability distribution for the variables of interest. This distribution gives the probabilities of these variables without reference to the other variables that were summed out. For example, one can compute the marginal probability $P(cavity)$ from the joint distribution **P**(*Cavity*, *Toothache*, *Catch*).

## Example Calculation
Using a full joint distribution table for the variables *Toothache*, *Cavity*, and *Catch*, the marginal probability of *cavity* can be calculated. This is done by adding up the probabilities of all entries in the table where *cavity* is true, regardless of the values of *Toothache* and *Catch*. The text shows this calculation as $P(cavity) = 0.108 + 0.012 + 0.072 + 0.008 = 0.2$.

## Relationships

- **operates-on**: [[full-joint-probability-distribution|Full Joint Probability Distribution]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*