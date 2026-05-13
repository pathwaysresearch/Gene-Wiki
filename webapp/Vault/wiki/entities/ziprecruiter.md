---
type: entity
aliases: [ZipRecruiter]
summary: An online job board that uses a matching algorithm to connect job seekers with companies, used as a case study for reward function engineering in pricing.
relationships:
  - target: reward-function-engineering
    type: is_an_example_of
tags: [company, online-platform, case-study]
sourced_from: Prediction Machines The Simple Economics Of Artificial Intelligence By Ajay Agrawal 
---

# ZipRecruiter

## Overview
ZipRecruiter is an online job board whose core product is a matching algorithm. This algorithm serves as a modern, scalable version of a traditional head-hunter, efficiently connecting companies that have job openings with qualified candidates.

## Role as a Case Study
The text uses ZipRecruiter as a practical example to illustrate the concept of reward function engineering. The company faced a complex strategic challenge in determining how to price its services for companies posting job openings. The decision was not straightforward because the definition of the "best" price was unclear.

## The Pricing Challenge
ZipRecruiter's pricing problem involved significant trade-offs. Charging a high price would maximize short-term revenue from each customer but could lead to fewer customers, less word-of-mouth marketing, and a smaller pool of job postings, which in turn might deter job seekers. To resolve this, the company worked with economists to run experiments, assigning different prices to different customers to measure their response. This allowed them to gather data to more carefully define their objectives and engineer a reward function that balanced short-term profitability with long-term platform growth.

## Relationships

- **is_an_example_of**: [[reward-function-engineering|Reward Function Engineering]]

---
*Extracted from: Prediction Machines The Simple Economics Of Artificial Intelligence By Ajay Agrawal *