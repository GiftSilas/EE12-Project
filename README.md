Project Overview
The Orange Freshness Detection app is a Streamlit-based web application that classifies uploaded photos of oranges as Fresh or Rotten.

Key Highlights
Two-Step Image Validation:

Uses MobileNetV2 (ImageNet) to check if the uploaded object is an orange or lemon.

Uses PCA shape analysis (elongation estimation) to reject elongated objects like eggs.

Freshness Classification: Uses a custom Keras model (orange_model.keras) to determine freshness and provides confidence scores.

Tech Stack: Python, Streamlit, TensorFlow / Keras, NumPy, Pillow (PIL).
23/EG/EE/035


## Project Summary

### System Purpose
The Citrus Quality Evaluation tool is an interactive web platform built with Streamlit that analyzes uploaded images to identify whether oranges are sound or spoiled.

### Primary Features
* **Dual-Stage Image Filtering:**
* Employs MobileNetV2 pretrained weights to verify that input images depict citrus fruits rather than unrelated items.
* Applies Principal Component Analysis (PCA) to evaluate spatial geometry and filter out oblong items such as eggs based on aspect ratios.

* **Condition Assessment:** Features a dedicated neural network (`orange_model.keras`) to judge fruit viability and output corresponding probability metrics.

### Framework & Dependencies
Developed using Python, Streamlit, TensorFlow, Keras, NumPy and PIL.

**ID:** 23/EG/EE/000
