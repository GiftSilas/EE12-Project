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

**Registration Number:** 23/EG/EE/035
