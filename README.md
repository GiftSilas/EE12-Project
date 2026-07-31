# EE12-Project
A mini project in fulfilment of GET 32
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

⚙️ Installation Steps
 * Clone the Repository:
   git clone [https://github.com/GiftSilas/EE12-Project.git](https://github.com/GiftSilas/EE12-Project.git)
cd EE12-Project/EE12

 * Set Up a Virtual Environment (Recommended):
   * Linux/macOS:
     python3 -m venv venv
source venv/bin/activate

   * Windows:
     python -m venv venv
venv\Scripts\activate

 * Install Dependencies:
   pip install -r requirements.txt

🚀 How to Run the Project
Navigate to the EE12 directory containing app.py and start the Streamlit app:
streamlit run app.py

The application will open automatically in your web browser at http://localhost:8501.
💡 Usage Instructions
 * Open the web application URL provided by Streamlit.
 * Click Choose an image to upload a photo of an orange (.jpg, .jpeg, or .png).
 * The application will:
   * Run shape analysis to confirm the object is roughly circular (elongation score close to 1.0).
   * Run MobileNetV2 pre-validation to check if the item closely matches an orange/lemon context.
   * If validated, resize the image to 120 \times 120 pixels and feed it into orange_model.keras.
 * Review the result:
   * Fresh Orange green notification with confidence percentage.
   * Rotten Orange red notification with confidence percentage.
   * Uncertain Prediction warning notification if confidence falls between 40\% and 60\%.
🖼️ Screenshots
| Upload & Fresh Result Placeholder | Rejection / Invalid Input Placeholder |
|---|---|
|  |  |
🔮 Future Improvements
 * [ ] Add batch uploading capabilities for multiple image evaluation at once.
 * [ ] Implement enhanced background segmentation (e.g., GrabCut or Otsu thresholding) for robust shape filtering on busy backgrounds.
 * [ ] Deploy the web app online using Streamlit Community Cloud or Hugging Face Spaces.
🤝 Contributing Guidelines
 * Fork the repository.
 * Create your feature branch: git checkout -b feature/NewFeature
 * Commit your changes: git commit -m 'Add NewFeature'
 * Push to the branch: git push origin feature/NewFeature
 * Open a Pull Request.
📜 License
This project is open-source and available under the MIT License.
👤 Author
 * Gift Silas - GitHub Profile
📑 Registration Details
Registration Number: 23/EG/EE/025

