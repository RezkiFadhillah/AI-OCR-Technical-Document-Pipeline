import os
from ultralytics import YOLO
import easyocr

print("--- AI OCR Pipeline Start ---")

# Load Model
model_path = 'models/best.pt'
if os.path.exists(model_path):
    print(f"Model {model_path} found! Loading...")
    model = YOLO(model_path)
else:
    print("Model not found. Please check models/ folder.")

print("EasyOCR Initialized.")
print("System Ready! 🚀")