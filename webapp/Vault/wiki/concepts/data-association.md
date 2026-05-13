---
type: concept
aliases: [Data Association]
summary: The problem of determining which observations at a given time correspond to which objects or tracks from a previous time, especially when multiple objects and observations are present.
relationships:
  - target: particle-filtering
    type: can-be-solved-with
  - target: mcmc
    type: can-be-solved-with
tags: [tracking, estimation, probabilistic-reasoning]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Data Association

## Definition
The data association problem is the challenge of correctly assigning observations to the objects that generated them over time. Originally studied in radar tracking, it addresses the question of which detected 'blips' at time *t* belong to which 'blips' from time *t-1*. The labeling of observations within a single time step is arbitrary and provides no information for solving the association.

## Complications in Real Applications
Real-world applications of data association are often more complex than scenarios with a fixed number of objects and observations. Common complications include 'false alarms' or 'clutter,' which are observations not caused by any real object. Conversely, 'detection failures' occur when a real object is present but generates no observation. Furthermore, the problem must often account for new objects appearing and old objects disappearing from the scene.

## Modern Algorithmic Approaches
Two modern approaches are noted as being much more effective for data association. One is using a particle filtering algorithm, which works by maintaining a large collection of possible current assignments. The other is using a Markov Chain Monte Carlo (MCMC) algorithm, which explores the entire space of assignment histories. MCMC methods have the advantage of being able to change their decisions about previous assignments and can handle hundreds of objects in real time while approximating the true posterior distributions.

## Relationships

- **can-be-solved-with**: [[particle-filtering|Particle Filtering]]
- **can-be-solved-with**: [[mcmc|Mcmc]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*