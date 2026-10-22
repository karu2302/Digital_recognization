import streamlit as st
from streamlit_drawable_canvas import st_canvas
from keras.models import load_model
import numpy as np
import cv2


st.set_page_config(page_title="Digit AI", layout="centered")



st.markdown("<h1>Digit Recognizer</h1>", unsafe_allow_html=True)
st.markdown("<p>Draw a digit (0–9) below and see what the AI thinks it is!</p>", unsafe_allow_html=True)


st.sidebar.markdown("### ✏️ Drawing Settings")
drawing_mode = st.sidebar.selectbox("Tool", ("freedraw", "line", "rect", "circle", "transform"))
stroke_width = st.sidebar.slider("Stroke Width", 1, 25, 10)
stroke_color = st.sidebar.color_picker("Stroke Color", "#FFFFFF")
bg_color = st.sidebar.color_picker("Background Color", "#000000")
realtime_update = st.sidebar.checkbox("Update Realtime", True)


@st.cache_resource
def load_mnist_model():
    return load_model("digit_recognization.keras")

model = load_mnist_model()


st.markdown('<div class="canvas-wrapper">', unsafe_allow_html=True)
canvas_result = st_canvas(
    fill_color="rgba(255, 255, 255, 0.05)",
    stroke_width=stroke_width,
    stroke_color=stroke_color,
    background_color=bg_color,
    update_streamlit=realtime_update,
    height=280,
    width=280,
    drawing_mode=drawing_mode,
    key="canvas"
)
st.markdown('</div>', unsafe_allow_html=True)


if canvas_result.image_data is not None:
    img = cv2.cvtColor(canvas_result.image_data.astype("uint8"), cv2.COLOR_RGBA2GRAY)
    img_resized = cv2.resize(img, (28, 28))
    img_normalized = img_resized / 255.0
    img_reshaped = img_normalized.reshape((1, 28, 28))

    prediction = model.predict(img_reshaped)
    predicted_digit = np.argmax(prediction)

    st.markdown(f"<div class='prediction-box'>Prediction: {predicted_digit}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='emoji'>{['0️⃣','1️⃣','2️⃣','3️⃣','4️⃣','5️⃣','6️⃣','7️⃣','8️⃣','9️⃣'][predicted_digit]}</div>", unsafe_allow_html=True)
