---
type: concept
aliases: [Principal Component Analysis (PCA)]
summary: A popular dimensionality reduction technique that projects data onto a lower-dimensional subspace defined by principal components, which are axes that capture the maximum amount of variance in the data.
relationships:
  - target: unsupervised-learning
    type: is_a_type_of
  - target: curse-of-dimensionality
    type: addresses
tags: [dimensionality-reduction, unsupervised-learning, linear-algebra]
sourced_from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019
---

# Principal Component Analysis (PCA)

## Core Idea
The fundamental idea behind PCA is to identify the axes, called principal components, that preserve the maximum amount of variance when the data is projected onto them. This choice is justified because it is likely to lose the least amount of information. An alternative justification is that this projection minimizes the mean squared distance between the original data points and their projections.

## Explained Variance
A key output of PCA is the explained variance ratio for each principal component. This value, accessible via the `explained_variance_ratio_` attribute in Scikit-Learn, indicates the proportion of the dataset's total variance that lies along that component's axis. This helps in deciding how many components to keep. For example, the text shows a case where the first two components capture 84.2% and 14.6% of the variance respectively.

## Choosing the Number of Dimensions
Rather than arbitrarily selecting the number of dimensions for reduction, a common practice is to choose the number of principal components that collectively capture a sufficiently large portion of the total variance, for example, 95%. The components themselves can be accessed via the `components_` attribute in Scikit-Learn's PCA implementation.

## Relationships

- **addresses**: [[curse-of-dimensionality|Curse Of Dimensionality]]

---
*Extracted from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019*

---
*Also referenced in: Deep+Learning+Ian+Goodfellow*