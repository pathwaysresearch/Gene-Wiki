---
type: concept
aliases: [Overflow]
summary: A numerical error that occurs when numbers with a large magnitude are approximated as positive or negative infinity, often leading to not-a-number (NaN) values in subsequent calculations.
tags: [numerical-computation, floating-point, computer-science]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Overflow

## Definition
Overflow is a numerical error that occurs when the magnitude of a number is too large to be represented in the available floating-point format. Such numbers are approximated as positive infinity ($\infty$) or negative infinity ($-\infty$).

## Consequences
This form of numerical error is highly damaging because further arithmetic operations involving these infinite values typically result in not-a-number (NaN) values. The presence of a single NaN can propagate through subsequent calculations, rendering the final result meaningless.

## Example: Softmax Function
The softmax function is susceptible to overflow. If the input values to the function are large and positive, the `exp` function can produce numbers that are too large to be represented, causing an overflow. This necessitates the use of stabilization techniques in practical implementations.

---
*Extracted from: Deep+Learning+Ian+Goodfellow*