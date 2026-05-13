---
type: concept
aliases: [Asymptotic Analysis]
summary: A method for analyzing algorithms by describing their performance as the input size approaches infinity, abstracting over constant factors and specific inputs.
tags: [algorithm-analysis, complexity-theory]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Asymptotic Analysis

## Definition and Notation
Asymptotic analysis describes the performance of an algorithm as its input size, n, asymptotically approaches infinity. It commonly uses the O() notation, where a function T(n) is said to be O(f(n)) if T(n) < kf(n) for some constant k, for all n greater than some value n_0. This provides an upper bound on the algorithm's measure.

## Purpose and Trade-offs
The primary purpose of asymptotic analysis is to compare algorithms in a way that is independent of specific hardware or small inputs, allowing for definitive statements such as an O(n) algorithm being better than an O(n^2) algorithm for large n. This approach abstracts over constant factors, which makes the analysis mathematically feasible but less precise than an exact T() function. For example, an algorithm with T(n) = 100n + 1000 is O(n), while one with T(n) = n^2 + 1 is O(n^2), but the O(n^2) algorithm is actually faster for n < 110.

## Significance in Algorithm Analysis
Despite its lack of precision for small inputs, asymptotic analysis is the most widely used tool for analyzing algorithms. Its power comes from abstracting over both the exact number of operations (by ignoring the constant factor k) and the exact content of the input (by considering only its size n). This makes it a good compromise between the precision of analysis and the ease of performing it.

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*