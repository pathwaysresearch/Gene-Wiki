---
type: concept
aliases: [The Grasping Problem]
summary: A key challenge in robotics and automation, particularly in fulfillment, involving the difficulty for machines to reliably pick up and handle a wide variety of objects.
relationships:
  - target: missing-links-in-automation
    type: is_an_example_of
  - target: kindred
    type: addressed_by
tags: [robotics, automation, reinforcement-learning, fulfillment]
sourced_from: Prediction Machines The Simple Economics Of Artificial Intelligence By Ajay Agrawal 
---

# The Grasping Problem

## Definition
The grasping problem is a significant challenge in robotics that serves as a "missing link in automation," particularly in the fulfillment industry. It refers to the difficulty of training a robot to successfully and reliably mimic human ability to pick up and handle a wide variety of objects, which is a crucial step in processes like online shopping fulfillment.

## Role as an Automation Bottleneck
In the context of fulfillment, the grasping problem is a fundamental constraint on full automation. While other parts of the workflow may be automated, the inability of a machine to reliably perform this seemingly low-skilled task can derail the entire exercise. It is a critical step that prevents the complete reformulation of jobs in warehouses.

## AI-Based Solution Approach
The text describes how the startup Kindred addresses the grasping problem using reinforcement learning. Their robot, Kindred Sort, initially uses a human controller with a virtual reality headset to guide the robotic arm via teleoperation. This process of a human grasping via teleoperation generates a large number of observations that are then used as training data for a prediction machine, teaching the robot to eventually perform the task autonomously.

## Relationships

- **is_an_example_of**: [[missing-links-in-automation|Missing Links In Automation]]
- **addressed_by**: [[kindred|Kindred]]

---
*Extracted from: Prediction Machines The Simple Economics Of Artificial Intelligence By Ajay Agrawal *