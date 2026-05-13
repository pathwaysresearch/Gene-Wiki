---
type: concept
aliases: [Underflow]
summary: A numerical error that occurs when numbers near zero are rounded to zero, which can lead to issues like division by zero or taking the logarithm of zero.
tags: [numerical-computation, floating-point, computer-science]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Underflow

## Definition
Underflow is a form of numerical rounding error that occurs in floating-point arithmetic when a number that is extremely close to zero is rounded to become exactly zero. It is a particularly devastating form of error in many numerical computations.

## Consequences
Many mathematical functions behave qualitatively differently when their argument is zero compared to a small positive number. Underflow can lead to critical failures, such as division by zero, which may cause a program to crash or return a not-a-number (NaN) value. Another common issue is attempting to take the logarithm of zero, which is treated as negative infinity and can corrupt subsequent calculations.

## Example: Softmax Function
The softmax function is an example of a function that must be stabilized to prevent underflow. If the inputs to the softmax are very negative, the `exp` function will produce values that can underflow to zero, potentially leading to a division by zero in the softmax calculation.

---
*Extracted from: Deep+Learning+Ian+Goodfellow*