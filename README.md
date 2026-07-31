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
