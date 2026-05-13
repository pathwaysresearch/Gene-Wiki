---
type: concept
aliases: [Causal Inference Engine]
summary: A conceptual machine that formalizes the process of causal reasoning by taking assumptions, queries, and data as inputs to produce causal conclusions. A computational system designed to automate the process of answering causal questions, particularly those involving interventions, by analyzing causal diagrams.
relationships:
  - target: causal-inference
    type: is_a_framework_for
  - target: estimand-causal-inference
    type: produces
  - target: causal-diagrams
    type: uses
tags: [causality, reasoning-model, artificial-intelligence, computation, inference]
sourced_from: The Book Of Why  The New Science Of Cause And Effect ( Pdfdrive )
---

# Causal Inference Engine

## Overview
The Causal Inference Engine is a conceptual blueprint for a system that handles causal reasoning. It is a machine that accepts three different kinds of inputs—Assumptions, Queries, and Data—and produces three kinds of outputs to provide a structured way of answering causal questions.

## Inputs and Outputs
The engine processes three distinct inputs: Assumptions (in the form of a causal model), Queries (the specific causal question being asked, e.g., P(L | do(D))), and Data (statistical information from observations). It produces three outputs in sequence. First, it determines if the query is answerable in theory (Yes/No) based on the model. Second, if the answer is yes, it produces an Estimand. Third, after receiving the data, it uses the estimand to compute an actual Estimate for the query, along with measures of uncertainty.

## Key Features
A critical feature of the engine is its adaptability, which stems from the separation of the model from the data. The estimand is generated based on the causal model alone, prior to examining the data. This makes the engine's logic applicable to any dataset compatible with the model's structure, unlike purely data-driven methods like deep learning that require complete retraining for new environments. The engine also formally recognizes that some queries may be unanswerable if the model is incomplete or necessary data on confounding variables cannot be collected.

## Relationships

- **is_a_framework_for**: [[causal-inference|Causal Inference]]
- **produces**: [[estimand-causal-inference|Estimand Causal Inference]]
- **uses**: [[causal-diagrams|Causal Diagrams]]

---
*Extracted from: The Book Of Why  The New Science Of Cause And Effect ( Pdfdrive )*