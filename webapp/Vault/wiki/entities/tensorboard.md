---
type: entity
aliases: [TensorBoard]
summary: A visualization toolkit that allows users to inspect and understand their model's structure, metrics, and training data, often used with TensorFlow and Keras.
tags: [visualization, debugging, tensorflow, machine-learning-tools]
sourced_from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019
---

# TensorBoard

## Overview
TensorBoard is a tool for visualizing data generated during the training of machine learning models. It helps in understanding, debugging, and optimizing the training process by providing graphical representations of various metrics and model parameters.

## How It Works
To use TensorBoard, a program must be configured to output data to special binary log files called "event files." Each data record in these files is known as a "summary." The TensorBoard server monitors a specified log directory for these event files, automatically picking up changes and updating its visualizations. This allows for near real-time monitoring of live data, such as learning curves during training.

## Log Management
A best practice for using TensorBoard is to point the server to a root log directory and have the training script write to a different subdirectory for each run. This can be achieved by creating a unique directory name for each run, for example, based on the current date and time or the hyperparameters being tested. This setup allows the TensorBoard instance to display and compare data from multiple experimental runs without mixing them up.

---
*Extracted from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019*