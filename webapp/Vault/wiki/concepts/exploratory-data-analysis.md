---
type: concept
aliases: [Exploratory Data Analysis]
summary: The process of investigating a dataset to summarize its main characteristics, often using visual methods, to gain insights, identify anomalies, and check assumptions before formal modeling.
tags: [data-analysis, data-visualization, machine-learning-workflow]
sourced_from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019
---

# Exploratory Data Analysis

## Initial Data Inspection
A first step in exploratory data analysis is to get a quick description of the data's structure. This involves using methods like `head()` to view the first few rows of a DataFrame and `info()` to understand the total number of rows, each attribute's data type, and the count of non-null values. This provides a high-level overview and can immediately flag issues like missing data.

## Visualizing Distributions
Histograms are a key tool for understanding the distribution of each numerical attribute. Plotting histograms can reveal important properties, such as features that have been scaled, capped, or have heavy tails. For example, analysis of the California Housing dataset's `median_income` attribute via a histogram showed that the data had been scaled and capped at both a lower and upper limit, which is crucial information for modeling.

## Discovering Relationships and Quirks
Scatter plots are used to visualize relationships between attributes and uncover insights. A geographical scatter plot of housing prices revealed strong correlations with location (e.g., proximity to the ocean) and population density. Similarly, a scatter plot of median income versus median house value showed a strong positive correlation but also exposed data quirks, such as a hard price cap at $500,000 and other artificial horizontal lines that might need to be addressed during data cleaning.

---
*Extracted from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019*