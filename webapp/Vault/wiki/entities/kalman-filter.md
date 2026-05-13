---
type: entity
aliases: [Kalman Filter]
summary: A filtering algorithm for forward inference in linear systems with Gaussian noise, used for tracking and estimation.
relationships:
  - target: rudolf-kalman
    type: developed-by
  - target: switching-kalman-filter
    type: is-a-generalization-of
tags: [filtering, linear-systems, estimation-theory]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Kalman Filter

## Overview
The Kalman filter is a technique for forward inference in linear systems that are subject to Gaussian noise. It is based on a direct state-space modeling of the stochastic process, which proved to be a simpler approach than earlier frequency-domain representations.

## Historical Development
The filter is named after Rudolf Kalman, who described it in a 1960 paper. However, the core results had been previously obtained by the Danish statistician Thorvold Thiele in 1880 and the Russian mathematician Ruslan Stratonovich in 1959. Peter Swerling also contributed to the development of the state-space modeling approach in 1959. Significant earlier classified work on filtering was also done during World War II by Wiener and Kolmogorov.

## Application in the Apollo Program
The practical application of the Kalman filter received a major boost after Rudolf Kalman's visit to NASA Ames Research Center in 1960. He recognized its applicability to the problem of tracking rocket trajectories, and the filter was subsequently implemented for the Apollo missions, demonstrating its real-world utility.

## Relationships

- **developed-by**: [[rudolf-kalman|Rudolf Kalman]]
- **is-a-generalization-of**: [[switching-kalman-filter|Switching Kalman Filter]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*