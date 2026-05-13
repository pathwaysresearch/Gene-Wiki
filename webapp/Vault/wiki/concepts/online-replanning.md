---
type: concept
aliases: [Online Replanning]
summary: A process where an agent monitors its plan execution in the real world and generates a new plan if the current one becomes invalid or an unexpected situation arises.
tags: [planning, execution, robotics, agent-architecture]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Online Replanning

## Overview
Online replanning is a strategy for acting in the real world where an agent combines planning with execution, allowing it to respond flexibly to unforeseen events. Instead of relying on a vast, precomputed contingent plan, the agent generates and executes plans dynamically. This process makes an agent's behavior seem purposive and intelligent rather than rote, as it can adapt its actions to achieve its goals when the world changes unexpectedly, such as a robot reattaching a car door that has fallen off.

## The Role of Execution Monitoring
A key prerequisite for replanning is execution monitoring. The agent continuously checks the state of the world to ensure the plan is proceeding as expected. This can involve checking the preconditions of the remaining steps in the plan. If a precondition is not met—for example, an action fails to produce its intended effect—the need for a new plan is triggered. Some branches of a plan can even explicitly contain a `Replan` step, which, if reached, sends the agent back into planning mode.

## The Replanning Cycle
When execution monitoring detects a problem, the agent enters a replanning phase. It must figure out a repair action sequence to get from its current, unexpected state to a state where it can resume its overall plan. This can create a plan-execute-replan loop. For instance, if painting a chair once doesn't achieve the desired color, the agent perceives this failure, replans to execute the same paint action again, and retries, looping until the goal is perceived to be met.

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*