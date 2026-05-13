---
type: concept
aliases: [Proportional-Integral-Derivative (PID) Control]
summary: A control loop mechanism that adds an integral term to a proportional-derivative (PD) controller to correct for systematic, long-lasting errors.
tags: [robotics, control-theory, feedback-control]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Proportional-Integral-Derivative (PID) Control

## Definition
Proportional-Integral-Derivative (PID) control is a control law that extends a proportional-derivative (PD) controller by adding a third term based on the integrated error over time. The control action, \(a_t\), is calculated using the formula \(a_t = K_P(y(t) - x_t) + K_I \int (y(t) - x_t)dt + K_D \frac{\partial(y(t) - x_t)}{\partial t}\), where \(K_P\), \(K_I\), and \(K_D\) are gain parameters for the proportional, integral, and derivative terms, respectively.

## How It Works
The controller continuously calculates an error value as the difference between a desired reference signal \(y(t)\) and the actual state \(x_t\). The proportional term provides a control action proportional to the current error. The derivative term provides a control action proportional to the rate of change of the error, which helps in smoothing the path and preventing oscillations. The integral term calculates the accumulated error over time, allowing the controller to address persistent, systematic deviations.

## Purpose and Advantages
The primary purpose of the integral term in a PID controller is to eliminate systematic errors that PD controllers may fail to regulate down to zero. Such errors can arise from unmodeled, systematic external forces, like a car being pulled to one side on a banked surface or errors from wear and tear in robot arms. By integrating the error, a long-lasting deviation will cause the integral term to grow, increasing the control action until the error is forced to shrink, thereby ensuring the controller does not exhibit a persistent systematic error.

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*