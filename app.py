
import tensorflow as tf
from tensorflow.keras.models import load_model
import numpy as np
import cv2
from flask import Flask, request, jsonify
from PIL import Image
with open(r"c:\Users\lenovo\zinovation\backend\app.py", "r", encoding="utf-8") as f:
    content = f.read()

clean_content = "".join(c for c in content if c.isprintable() or c in "\n\r\t ")

with open("app.py", "w", encoding="utf-8") as f:
    f.write(clean_content)



model_path = r"C:C:\Users\lenovo\OneDrive\Documents"
model = load_model(model_path)
IMAGE_SIZE = (224, 224)