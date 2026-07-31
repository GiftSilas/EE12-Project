Project Overview
The Orange Freshness Detection app is a Streamlit-based web application that classifies uploaded photos of oranges as Fresh or Rotten.

Key Highlights
Two-Step Image Validation:

Uses MobileNetV2 (ImageNet) to check if the uploaded object is an orange or lemon.

Uses PCA shape analysis (elongation estimation) to reject elongated objects like eggs.

Freshness Classification: Uses a custom Keras model (orange_model.keras) to determine freshness and provides confidence scores.

Tech Stack: Python, Streamlit, TensorFlow / Keras, NumPy, Pillow (PIL).
23/EG/EE/035
