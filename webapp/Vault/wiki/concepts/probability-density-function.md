---
type: concept
aliases: [Probability Density Function]
summary: A function used for continuous random variables that describes the relative likelihood for the variable to take on a given value. The probability over a range is the integral of the function over that range. A function for continuous random variables that describes the relative likelihood for the variable to take on a given value, where the probability of any single value is zero.
tags: [probability-theory, continuous-variables, statistics]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Probability Density Function

## Definition
For continuous random variables, which can take on infinitely many values, a probability distribution cannot be listed in a table. Instead, it is defined by a parameterized function of the variable, known as a probability density function (PDF). The formal definition of the probability density $P(x)$ for a continuous variable $X$ at value $x$ is the limit of the probability that $X$ falls within an arbitrarily small region starting at $x$, divided by the width of the region: $P(x) = \lim_{dx \to 0} P(x \le X \le x+dx)/dx$.

## Interpretation
The value of a PDF at a specific point, $P(x)$, is not a probability itself but a probability density. The probability that the variable falls within a specific range is calculated by integrating the PDF over that range. For example, a uniform PDF over an 8-degree range implies a 100% chance the value will fall in that range and a 50% chance it will fall in any 4-degree sub-range within it.

## Example
The text provides an example for the temperature at noon, believed to be uniformly distributed between 18°C and 26°C. The PDF is expressed as $P(\text{NoonTemp} = x) = \text{Uniform}_{18C,26C}(x)$. This function has a constant value of $1/8$ for any $x$ between 18 and 26, and is 0 otherwise. The value $1/8$ is a density, not a probability.

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*