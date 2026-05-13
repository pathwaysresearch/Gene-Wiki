---
type: concept
aliases: [Batch Learning]
summary: A machine learning method where the system is trained using all the available data at once and cannot learn incrementally from new data. A machine learning training method where the model is trained on the entire dataset at once, as opposed to learning incrementally.
relationships:
  - target: online-learning
    type: is_contrasted_with
tags: [machine-learning, training-method, training-methods]
sourced_from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019
---

# Batch Learning

## Definition
In batch learning, the system is incapable of learning incrementally. It must be trained using all the available data at one time. This is sometimes referred to as offline learning.

## Training and Updating
To train a batch learning system, you provide it with the entire training dataset. If you need the system to learn about new data, you must retrain a new version of the system from scratch on the full dataset, which includes both the original and the new data. This process is then repeated, replacing the old system with the new one.

## Use Cases and Limitations
This approach is common for systems that do not require rapid adaptation to changing data. However, retraining on a full dataset can be resource-intensive and time-consuming, especially for large datasets, making it impractical for systems that need to learn continuously.

## Relationships

- **is_contrasted_with**: [[online-learning|Online Learning]]

---
*Extracted from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019*