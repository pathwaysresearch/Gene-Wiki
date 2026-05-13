---
type: concept
aliases: [Root Mean Square Error (RMSE)]
summary: A common performance metric for regression models that measures the standard deviation of the prediction errors, giving higher weight to larger errors.
relationships:
  - target: regression-machine-learning
    type: is-performance-measure-for
tags: [machine-learning, performance-metrics, regression]
sourced_from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019
---

# Root Mean Square Error (RMSE)

## Definition
The Root Mean Square Error (RMSE) is presented as a typical performance measure for regression problems. It is used to get an idea of how much error the system typically makes in its predictions.

## Key Characteristic
A significant feature of RMSE is that it gives a higher weight to large errors. This means that predictions that are far off from the actual value will penalize the model more heavily than small errors, making it sensitive to outliers.

## Preferred Use Case
According to the text, RMSE performs very well and is generally the preferred metric when outliers in the data are exponentially rare, such as in data that follows a bell-shaped distribution.

## Relationships

- **is-performance-measure-for**: [[regression-machine-learning|Regression Machine Learning]]

---
*Extracted from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019*