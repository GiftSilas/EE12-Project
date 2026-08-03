
# Orange Freshness Detection

## Project Overview

Orange Freshness Detection is a Streamlit-based web application that uses deep learning to determine whether an orange is **fresh** or **rotten** from an uploaded image. The system combines image classification and shape validation techniques to improve prediction accuracy and reduce incorrect classifications. The application provides users with a simple interface for uploading images and receiving freshness predictions with confidence scores. 0

## Features

- Upload images of oranges for freshness analysis.
- Two-step image validation to ensure correct object detection.
- MobileNetV2-based image classification.
- PCA shape analysis to filter out invalid objects.
- Displays prediction results with confidence scores.
- User-friendly Streamlit web interface.

## Technologies Used

- Python
- Streamlit
- TensorFlow / Keras
- NumPy
- Pillow (PIL)

## Project Structure

- `app.py` – Main Streamlit application.
- `orange_model.keras` – Trained deep learning model.
- `requirements.txt` – Project dependencies.
- `README.md` – Project documentation.

## How to Run

1. Clone the repository.
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Start the application:
   ```bash
   streamlit run app.py
   ```
4. Open the local URL provided by Streamlit in your browser and upload an image for prediction.

## Author

**Registration Number:** 23/EG/EE/075
=======

## Project Summary

### System Purpose

The Citrus Quality Evaluation tool is an interactive web platform built with Streamlit that analyzes uploaded images to identify whether oranges are sound or spoiled.

### Primary Features

* **Dual-Stage Image Filtering:**
* Employs MobileNetV2 pretrained weights to verify that input images depict citrus fruits rather than unrelated items.
* Applies Principal Component Analysis (PCA) to evaluate spatial geometry and filter out oblong items such as eggs based on aspect ratios.


* **Condition Assessment:** Features a dedicated neural network (`orange_model.keras`) to judge fruit viability and output corresponding probability metrics.

### Framework & Dependencies

Developed using Python, Streamlit, TensorFlow, Keras, NumPy, and PIL.

**ID:** 23/EG/EE/035


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

**ID:** 23/EG/EE/115
=======

A mini project in fulfilment of GET 324
# EE12-Project

An image classification project developed in fulfilment of GET 324. The application detects whether an orange is fresh or rotten from an uploaded image using a trained TensorFlow/Keras model and a Streamlit web interface.

---

## Overview

EE12-Project is a machine learning application that allows users to upload an image of an orange and receive a freshness prediction. Before classification, the system validates that the uploaded image is likely to contain an orange by using MobileNetV2 image recognition and a simple shape analysis algorithm.

If the uploaded image is not recognised as an orange or appears elongated (such as an egg-shaped object), the application prompts the user to upload a valid image.

---

## Features

- Fresh vs Rotten orange classification.
- Image upload through a Streamlit web interface.
- Image validation using MobileNetV2 (ImageNet pretrained model).
- Shape analysis to reject non-orange objects.
- Confidence score displayed with predictions.
- Warning messages for uncertain predictions.
- Cached model loading for improved performance.
- Includes a Jupyter notebook for model training.

---

## Technologies Used

- Python
- Streamlit
- TensorFlow
- Keras
- NumPy
- Pillow (PIL)
- Scikit-learn
- MobileNetV2 (pre-trained TensorFlow model)
- Jupyter Notebook

---

## Project Structure

```text
EE12-Project/
│
├── EE12/
│   ├── app.py                 # Streamlit application
│   ├── orange_model.keras     # Trained classification model
│   ├── requirements.txt       # Project dependencies
│   ├── train_model.ipynb      # Model training notebook
│   └── dataset/               # Dataset used for training
│
└── README.md
```

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/GiftSilas/EE12-Project.git
```

### 2. Navigate to the Project Folder

```bash
cd EE12-Project/EE12
```

### 3. Create a Virtual Environment (Optional)

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

macOS/Linux:

```bash
python -m venv venv
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## How to Run the Project

Run the Streamlit application using:

```bash
streamlit run app.py
```

After running the command, Streamlit will provide a local URL (typically):

```text
http://localhost:8501
```

Open the URL in your browser to use the application.

---

## Usage Instructions

1. Launch the application.
2. Upload an image file (.jpg, .jpeg, or .png).
3. The application will:

   - Validate that the image resembles an orange.
   - Check whether the object's shape is suitable.
   - Process the image through the trained model.

4. The application will display one of the following results:

   - Fresh Orange
   - Rotten Orange
   - Uncertain Prediction
   - Invalid image (not an orange or unsuitable image)

For best results:

- Use clear images.
- Ensure the orange is visible and well-lit.
- Use a plain or uncluttered background whenever possible.

---

## Screenshots

Add screenshots of the application interface here.

### Home Page

```
[Insert screenshot here]
```

### Fresh Orange Prediction

```
[Insert screenshot here]
```

### Rotten Orange Prediction

```
[Insert screenshot here]
```

### Invalid Image Warning

```
[Insert screenshot here]
```

---

## Future Improvements

Potential enhancements include:

- Support for additional fruit freshness detection.
- Improved dataset diversity for better accuracy.
- Model performance evaluation metrics.
- Deployment to cloud platforms such as Streamlit Community Cloud.
- Batch image prediction.
- Improved object segmentation for complex backgrounds.
- User interface enhancements.

---

## Contributing

Contributions are welcome.

To contribute:

1. Fork the repository.
2. Create a new branch.

```bash
git checkout -b feature-name
```

3. Make your changes.
4. Commit your work.

```bash
git commit -m "Add new feature"
```

5. Push your changes.

```bash
git push origin feature-name
```

6. Open a Pull Request.

---

## License

No license file is currently included in this repository.

If you intend to make this project open source, consider adding an appropriate license such as:

- MIT License
- Apache License 2.0
- GPL v3

---

## Author

Developed as part of a GET 324 mini project.

Repository Owner:

- oliver-creator1

GitHub Repository:

- https://github.com/oliver-creator1/EE12-Project

---

## Acknowledgements

This project makes use of:

- TensorFlow and Keras for machine learning.
- Streamlit for building the web interface.
- MobileNetV2 pretrained on ImageNet for image validation.
- Open-source Python libraries including NumPy and Pillow.

---

## 23/EG/EE/015
=======

# EE12-Project
A mini project in fulfilment of GET 324

EE12 Project

Overview

EE12 Project is a mini project developed in fulfilment of the requirements for GET 324. The project is designed to demonstrate the practical application of knowledge and skills acquired during the course through the development of a structured and functional solution.

The project focuses on applying relevant technical concepts to solve a practical problem while demonstrating proper project planning, implementation, documentation, and presentation.

Objectives

The main objectives of this project are to:

- Apply the knowledge and concepts acquired in GET 324.
- Develop a practical solution to a real-world problem.
- Demonstrate technical and problem-solving skills.
- Gain practical experience in project development.
- Document and present the development process effectively.

Features

- Practical implementation of the project requirements.
- Structured and organized project files.
- Application of relevant technical concepts.
- Designed for academic and educational purposes.

Technologies Used

The project was developed using the appropriate tools and technologies required for its implementation.

Project Structure

EE12-Project/
│
├── README.md
└── EE12/
    └── Project files

Installation

To get a local copy of the project:

git clone https://github.com/mfongodswill68-cmd/EE12-Project.git

Navigate into the project directory:

cd EE12-Project

Usage

Open the project files using the appropriate development environment and follow the project-specific instructions to run or interact with the application.

Purpose

This project is developed primarily for academic purposes as part of the requirements for GET 324. It demonstrates the ability to apply theoretical knowledge to practical project development.

Author

Godswill Mfon

Acknowledgements

- Department/Course requirements for GET 324
- Course instructors and project supervisors
- Resources and tools used during the development of the project

License

This project is intended for educational and academic purposes.

23/EG/EE/045
=======
# Orange Freshness Detection Web App

A Computer Vision and Deep Learning web application built to classify oranges as **Fresh** or **Rotten**, complete with pre-validation filters to ensure uploaded images are actual oranges. Developed as a mini project in fulfillment of **GET 324**.

---

## 📌 Overview

This project uses a custom Keras Deep Learning model alongside MobileNetV2 pre-validation to assess orange quality. The application provides an interactive web interface built with **Streamlit** where users can upload image files (JPG, JPEG, PNG) and receive real-time freshness predictions with confidence scores.

To minimize false positive predictions on non-orange inputs or non-spherical objects (such as eggs), the app integrates image classification pre-validation and Principal Component Analysis (PCA) based elongation detection.
=======
# EE12 Project

> A comprehensive project repository for the EE12 coursework.

---

## 📖 Overview

The **EE12 Project** is designed to demonstrate key engineering principles, programming practices, and computational implementations. This repository contains the source code, configurations, and documentation needed to build and execute the project.

---

## ✨ Features


* **Fresh vs. Rotten Classification:** Classifies valid orange images into **Fresh** or **Rotten** status.
* **Pre-Validation Filter:** Uses standard MobileNetV2 ImageNet weights to verify whether the uploaded image contains an orange or lemon before passing it to the custom classifier.
* **Geometric Shape Check (PCA Elongation):** Converts the image to grayscale and uses Principal Component Analysis on foreground pixel coordinates to measure elongation, rejecting asymmetric or elongated objects (such as eggs).
* **Confidence & Uncertainty Handling:** Provides visual alerts (success, error, or warning) depending on classification probabilities and flags ambiguous predictions (confidence between $40\%$ and $60\%$).
* **Interactive UI:** A lightweight Streamlit web application supporting standard image uploads (`.jpg`, `.jpeg`, `.png`).
=======
* **Structured Design:** Clean code layout for readability and maintainability.
* **Engineering Logic:** Implementation of targeted project tasks and algorithms.
* **Version Control Ready:** Fully tracked using Git.

---

## 🛠️ Technologies Used
* **Language:** Python 3.x
* **Web Framework:** Streamlit
* **Deep Learning:** TensorFlow / Keras (MobileNetV2 & Custom `.keras` model)
* **Numerical & Data Processing:** NumPy
* **Ima

## 🪪 Registration / Student Identifier

**Registration Number:** `23/EG/EE/065

