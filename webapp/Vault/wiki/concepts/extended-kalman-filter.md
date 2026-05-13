---
type: concept
aliases: [Extended Kalman Filter]
summary: An extension of the Kalman filter for nonlinear systems that works by applying local linearization to the system model at each time step.
relationships:
  - target: kalman-filter
    type: is-an-extension-of
tags: [probabilistic-reasoning, state-estimation, nonlinear-systems]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Extended Kalman Filter

## Purpose
The Extended Kalman Filter (EKF) is an adaptation of the Kalman filter designed to handle nonlinear systems. A system is considered nonlinear if its transition or sensor model cannot be described as a simple matrix multiplication of the state vector, as required by the standard Kalman filter. The EKF attempts to overcome this limitation to allow for tracking in a wider range of applications.

## How It Works
The EKF approximates a nonlinear system as being *locally linear* in the region of the mean of the current state distribution. At each time step, it linearizes the system model around the current state estimate. This allows the standard Kalman filter update equations to be applied to the linearized model. This process enables the EKF to maintain and update a Gaussian state distribution that serves as a reasonable approximation of the true posterior for certain types of nonlinear systems.

## Limitations
The local linearization approach works well for systems that are smooth and well-behaved. However, the EKF can perform poorly if there is significant nonlinearity in the system's response within the region of high probability defined by the state covariance. An example is tracking a bird flying at high speed towards a tree trunk. A linear prediction would place the mean of the future state inside the trunk, but the bird's actual behavior (a sharp turn) is a highly nonlinear event that the EKF's Gaussian approximation would fail to capture accurately.

## Relationships

- **is-an-extension-of**: [[kalman-filter|Kalman Filter]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*