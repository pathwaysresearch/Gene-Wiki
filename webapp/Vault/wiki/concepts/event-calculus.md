---
type: concept
aliases: [Event Calculus]
summary: A logical formalism for representing and reasoning about events and their effects on time-varying properties (fluents).
tags: [temporal-reasoning, logic, knowledge-representation]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Event Calculus

## Core Components
The event calculus is a framework for reasoning about events, time, and their effects. Events, such as a flying trip, can be reified as objects (e.g., `E₁ ∈ Flyings`). Properties that change over time are called fluents. Time is represented using intervals, which are defined by a start and end time, such as `i = (t₁, t₂)`.

## Key Predicates
The formalism is built on a set of core predicates. `Happens(e, i)` asserts that event `e` occurs over interval `i`. `T(f, t)` asserts that fluent `f` is true at time `t`. The effects of events are described by `Initiates(e, f, t)`, which means event `e` causes fluent `f` to become true at time `t`, and `Terminates(e, f, t)`, which means `e` causes `f` to cease being true. Other predicates like `Clipped(f, i)` and `Restored(f, i)` are used to reason about whether a fluent's truth value changes during an interval.

## Reasoning about Change
The central principle of reasoning in the event calculus is that a fluent holds true at a given time if it was initiated by an event at some point in the past and was not 'clipped' (made false) by another event in the intervening time. Conversely, a fluent does not hold if it was terminated by a past event and not subsequently restored. The initial state of the world is defined by a special `Start` event that specifies which fluents are initiated or terminated at the beginning of time.

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*