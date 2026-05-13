---
type: entity
aliases: [Street View Address Number Transcription System]
summary: A commercial application from Google that uses a convolutional network to automatically recognize and transcribe address numbers from Street View imagery to improve Google Maps data.
relationships:
  - target: convolutional-neural-network
    type: uses
  - target: google-maps
    type: contributes-to
tags: [computer-vision, deep-learning-application, google, ocr]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Street View Address Number Transcription System

## Overview and Purpose
The Street View address number transcription system is a real-world deep learning application developed to enhance the accuracy and completeness of Google Maps. Its primary function is to automatically add building addresses to the map in their correct geographical locations. This is achieved by processing the vast amount of imagery collected by Google's Street View cars.

## System Workflow
The system operates through a two-stage process. First, Street View cars drive through streets, photographing buildings and simultaneously recording the precise GPS coordinates associated with each photograph. In the second stage, a convolutional neural network (CNN) analyzes these photographs to locate and recognize the address number displayed on each building. This transcribed number is then associated with its GPS location and added to the Google Maps database.

## Key Design Consideration
A critical aspect of this system's design is its handling of uncertainty. Because an inaccurate address on a map significantly degrades its value, the system is built to prioritize correctness. It is designed to be able to refuse to make a decision if its confidence in a transcription is low. In such cases, a human operator might take over, ensuring that only high-confidence transcriptions are added to the map, thereby maintaining the integrity of the map data.

## Relationships

- **uses**: [[convolutional-neural-network|Convolutional Neural Network]]
- **contributes-to**: [[google-maps|Google Maps]]

---
*Extracted from: Deep+Learning+Ian+Goodfellow*