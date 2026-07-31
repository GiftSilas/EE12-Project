import os
import streamlit as st
import numpy as np
from PIL import Image
import tensorflow as tf

imgsize = 120
classnames = ["Rotten", "Fresh"]

st.set_page_config(page_title="Orange Freshness Detection")

root = os.path.dirname(os.path.abspath(__file__))


@st.cache_resource
def loadvalidationnetwork():
    return tf.keras.applications.mobilenet_v2.MobileNetV2(weights="imagenet")


@st.cache_resource
def loadorangemodel():
    modelpath = os.path.join(root, "orange_model.keras")
    return tf.keras.models.load_model(modelpath)


validationnetwork = loadvalidationnetwork()
orangemodel = loadorangemodel()

st.title("Orange Freshness Detection")
st.write("Upload a photo of an orange to check if it's fresh or rotten")

uploadedfile = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])

if uploadedfile is not None:
    image = Image.open(uploadedfile).convert("RGB")
    st.image(image, caption="Uploaded image", use_container_width=True)

    preprocessinput = tf.keras.applications.mobilenet_v2.preprocess_input
    decodepredictions = tf.keras.applications.mobilenet_v2.decode_predictions

    resizedforvalidation = image.resize((224, 224))
    validationarray = np.array(resizedforvalidation)
    expandedarray = np.expand_dims(validationarray, axis=0)
    preppedarray = preprocessinput(expandedarray.copy())
    validationresult = validationnetwork.predict(preppedarray, verbose=0)
    decodedpredictions = decodepredictions(validationresult, top=10)[0]

    validtags = ["orange", "fruit", "lemon", "citrus"]
    isvalidorange = any(
        any(tag in label.lower() for tag in validtags) and confidence > 0.01
        for (code, label, confidence) in decodedpredictions
    )

    if not isvalidorange:
        st.error("This doesn't look like an orange. Please upload a clearer photo of an orange.")
    else:
        resized = image.resize((imgsize, imgsize))
        arr = np.array(resized, dtype="float32") / 255.0
        arr = np.expand_dims(arr, axis=0)

        prediction = orangemodel.predict(arr, verbose=0)[0][0]

        if 0.4 <= prediction <= 0.6:
            st.warning(f"Uncertain prediction (confidence: {prediction:.2f}). Try a clearer image")
        elif prediction > 0.5:
            confidence = prediction
            st.success(f"Prediction: **Fresh Orange** (confidence: {confidence:.2%})")
        else:
            confidence = 1 - prediction
            st.error(f"Prediction: **Rotten Orange** (confidence: {confidence:.2%})")