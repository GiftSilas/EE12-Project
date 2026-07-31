# EE12-Project
A mini project in fulfilment of GET 324
# Orange Freshness Detection Web App

A Computer Vision and Deep Learning web application built to classify oranges as **Fresh** or **Rotten**, complete with pre-validation filters to ensure uploaded images are actual oranges. Developed as a mini project in fulfillment of **GET 324**.

---

## 📌 Overview

This project uses a custom Keras Deep Learning model alongside MobileNetV2 pre-validation to assess orange quality. The application provides an interactive web interface built with **Streamlit** where users can upload image files (JPG, JPEG, PNG) and receive real-time freshness predictions with confidence scores.

To minimize false positive predictions on non-orange inputs or non-spherical objects (such as eggs), the app integrates image classification pre-validation and Principal Component Analysis (PCA) based elongation detection.

---

## ✨ Features

* **Fresh vs. Rotten Classification:** Classifies valid orange images into **Fresh** or **Rotten** status.
* **Pre-Validation Filter:** Uses standard MobileNetV2 ImageNet weights to verify whether the uploaded image contains an orange or lemon before passing it to the custom classifier.
* **Geometric Shape Check (PCA Elongation):** Converts the image to grayscale and uses Principal Component Analysis on foreground pixel coordinates to measure elongation, rejecting asymmetric or elongated objects (such as eggs).
* **Confidence & Uncertainty Handling:** Provides visual alerts (success, error, or warning) depending on classification probabilities and flags ambiguous predictions (confidence between $40\%$ and $60\%$).
* **Interactive UI:** A lightweight Streamlit web application supporting standard image uploads (`.jpg`, `.jpeg`, `.png`).

---

## 🛠️ Technologies Used

* **Language:** Python 3.x
* **Web Framework:** Streamlit
* **Deep Learning:** TensorFlow / Keras (MobileNetV2 & Custom `.keras` model)
* **Numerical & Data Processing:** NumPy
* **Image Processing:** Pillow (PIL)
* **Mathematical Operations:** NumPy Linear Algebra (`np.linalg.eigvalsh` for PCA)

---

## 📁 Project Structure

```text
EE12-Project/
└── EE12/
    ├── app.py                 # Main Streamlit web application script
    ├── orange_model.keras     # Trained Keras model for freshness classification
    ├── train_model.ipynb      # Jupyter notebook used for training the model
    ├── requirements.txt       # Python dependencies
    └── dataset/               # Image dataset used for training/validation
