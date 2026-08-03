
# EE12-Project
A mini project in fulfilment of GET 324
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
* **Image Processing:** Pillow (PIL)
* **Mathematical Operations:** NumPy Linear Algebra (`np.linalg.eigvalsh` for PCA)
=======
* **Primary Language:** Python / C (or project target language)
* **Environment:** Command Line Interface (CLI) / Unix / Windows Terminal
* **Version Control:** Git & GitHub

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
=======
│
├── src/                    # Source code files
│   └── main.py             # Main entry point / core execution script
├── README.md               # Project documentation
└── .gitignore              # Files to be ignored by Git

```

---

## ⚙️ Installation Steps

Follow these steps to set up the project environment on your local machine:

1. **Clone the repository:**
```bash
git clone https://github.com/GiftSilas/EE12-Project.git

```


2. **Navigate to the project directory:**
```bash
cd EE12-Project

```


3. **Install dependencies (if applicable):**
```bash
pip install -r requirements.txt

```



---

## 🚀 How to Run the Project

Execute the core script from your terminal:

```bash
python3 main.py

```

*Or, if compiled via Makefile / C source:*

```bash
make
./ee12_project

```

---

## 💡 Usage Instructions

1. **Setup:** Ensure prerequisites and dependencies are installed as outlined above.
2. **Execution:** Run the target script/executable.
3. **Output:** Review the console logs or generated output files within the workspace.

---

## 🖼️ Screenshots

*No screenshots currently provided. You can add execution outputs or interface captures below:*

```
+-------------------------------------------------------+
|                 [ Screenshot Placeholder ]            |
|         Include screenshots of execution logs         |
|             or output visualizations here             |
+-------------------------------------------------------+

```

---

## 🔮 Future Improvements

* [ ] Add automated testing suites.
* [ ] Optimize performance and code modularity.
* [ ] Improve error handling and user prompts.

---

## 🤝 Contributing Guidelines

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create your feature branch:
```bash
git checkout -b feature/YourFeatureName

```


3. Commit your changes:
```bash
git commit -m "Add some YourFeatureName"

```


4. Push to the branch:
```bash
git push origin feature/YourFeatureName

```


5. Open a Pull Request.

---

## 📄 License

This project is open-source and available under the [MIT License](https://www.google.com/search?q=LICENSE).

---

## 👤 Author

**Gift Silas**

* GitHub: [@GiftSilas](https://www.google.com/search?q=https://github.com/GiftSilas)

---

## 🙏 Acknowledgements

* Instructors and supervisors supporting the EE12 course.
* Open-source tools and community support.

---

## 🪪 Registration / Student Identifier

**Registration Number:** `23/EG/EE/005`

