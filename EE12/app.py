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

def estimateelongation(image, threshold=235):
    """
    Segments the foreground object against a plain/light background and
    measures how elongated it is (via PCA on foreground pixel coordinates).
    Oranges are roughly circular in outline (elongation close to 1.0).
    Eggs are noticeably elongated and asymmetric (elongation clearly > 1.0).
    Returns None if the object can't be reliably segmented (e.g. busy background).
    """
    gray = np.array(image.convert("L"), dtype=np.float32)
    mask = gray < threshold
    ys, xs = np.nonzero(mask)
    if len(xs) < 200:
        return None

    coords = np.stack([xs, ys], axis=1).astype(np.float64)
    coords -= coords.mean(axis=0)
    cov = np.cov(coords, rowvar=False)
    eigvals = np.sort(np.linalg.eigvalsh(cov))[::-1]
    if eigvals[1] <= 0:
        return None
    return float(np.sqrt(eigvals[0] / eigvals[1]))


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

    validtags = ["orange", "lemon"]
    minconfidence = 0.15
    topn = 3

    isvalidorange = any(
        any(tag in label.lower() for tag in validtags) and confidence > minconfidence
        for (code, label, confidence) in decodedpredictions[:topn]
    )

    elongationthreshold = 1.2
    elongation = estimateelongation(image)
    iseggshaped = elongation is not None and elongation > elongationthreshold

    if iseggshaped:
        st.error(
            f"This looks too elongated/asymmetric to be an orange "
            f"(shape score: {elongation:.2f}, expected close to 1.0 for a round orange). "
            "Please upload a photo of an orange."
        )
    elif not isvalidorange:
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
