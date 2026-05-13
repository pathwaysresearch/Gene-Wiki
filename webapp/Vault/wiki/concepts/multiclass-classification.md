---
type: concept
aliases: [Multiclass Classification]
summary: A classification task that involves distinguishing between more than two classes, also known as multinomial classification.
tags: [classification, machine-learning-task]
sourced_from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019
---

# Multiclass Classification

## Definition
Multiclass classification, also called multinomial classification, refers to tasks where classifiers must distinguish between more than two classes. This is an extension of binary classification, which only handles two classes. A common example is classifying handwritten digits into one of ten classes (0 through 9).

## Algorithm Compatibility
Some machine learning algorithms, such as Random Forest classifiers or naive Bayes classifiers, are capable of handling multiple classes directly. However, other algorithms like Support Vector Machine (SVM) classifiers or Linear classifiers are strictly binary classifiers and require special strategies to be used for multiclass tasks.

## Strategies for Binary Classifiers
One common strategy to perform multiclass classification with binary classifiers is the one-versus-all (OvA) approach. This method involves training a separate binary classifier for each class (e.g., a 0-detector, a 1-detector, and so on). To classify a new image, you get the decision score from each of the 10 classifiers and select the class whose classifier outputs the highest score.

---
*Extracted from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019*