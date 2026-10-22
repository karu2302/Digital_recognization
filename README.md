# ✍️ Digital Recognition (Handwritten Digit Classifier)

<div align="center">

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![Computer Vision](https://img.shields.io/badge/AI-Computer%20Vision-orange.svg)](https://opencv.org/)
[![Streamlit/Gradio](https://img.shields.io/badge/App-Interactive-red.svg)](https://streamlit.io/)

*A computer vision application that recognizes and classifies handwritten digits drawn live on an interactive canvas.*

</div>

---

## 📖 What This Space Does
**Digital_recognization** combines computer vision and neural networks to classify handwritten digits (0–9) in real time. It features a interactive drawing canvas where users can draw a digit directly with their mouse or touch input, which the underlying model instantly processes and identifies.

## 🧰 What is Inside This Space
- **Interactive Sketch Canvas:** A drawing component enabling freehand digital input directly in the browser.
- **Image Preprocessing Module:** OpenCV / PIL image manipulation pipeline responsible for cropping, resizing to target matrix size (e.g., 28x28 pixels), converting to grayscale, and normalizing pixel intensities.
- **Trained Neural Network / Classifier:** A deep learning (CNN/MLP) or machine learning classifier model trained on standard handwriting datasets (such as MNIST).
- **Confidence Visualizer:** Displays predicted numerical output along with probability distribution charts across all digits (0–9).

## ⚙️ How It Works
1. **Canvas Drawing:** The user draws a digit on the interactive screen.
2. **Image Capture & Inversion:** The canvas output is converted into a raw image matrix, inverted, and resized to match training dimensions.
3. **Tensor Conversion:** The image matrix is flattened or reshaped into the input tensor format required by the model.
4. **Inference & Visualization:** The neural network performs a forward pass, predicts the most probable digit, and displays the confidence percentages to the user.

---
*Migrated from Hugging Face Spaces by [karu2302](https://github.com/karu2302).*
# Welcome to Streamlit!

Edit `/src/streamlit_app.py` to customize this app to your heart's desire. :heart:

If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).
