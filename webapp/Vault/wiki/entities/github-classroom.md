---
type: entity
aliases: [GitHub Classroom]
summary: A platform used in the study to administer coding assignments, accurately measure timing, and automatically grade submissions.
relationships:
  - target: controlled-experiment-on-ai-developer-productivity
    type: used_in
tags: [software-platform, education-technology, research-infrastructure]
sourced_from: 2302.06590V1
---

# GitHub Classroom

## Overview
GitHub Classroom is a platform designed for educational settings, enabling instructors to distribute, manage, and grade coding assignments. In this research, it was repurposed as the primary tool for administering the experimental task to all participants in a controlled and consistent manner.

## Role in the Experimental Setup
The researchers leveraged GitHub Classroom to manage the experiment's core logistics. Each participant was given a link to a GitHub Classroom instance, which automatically created a personal, private copy of a template repository for the assignment. The platform's creation of this repository served as the official start time for measuring task completion.

## Automation of Measurement
A critical function of GitHub Classroom in the study was the automation of measurement and validation. When participants committed and pushed their code changes, the platform automatically ran a pre-defined test suite against the submission. It logged a timestamp for each push and reported the number of passing tests, which allowed researchers to precisely and objectively determine the exact moment of successful task completion for each participant.

## Relationships

- **used_in**: [[controlled-experiment-on-ai-developer-productivity|Controlled Experiment On Ai Developer Productivity]]

---
*Extracted from: 2302.06590V1*