# AI-OCR Technical Document Pipeline 🚀

End-to-end pipeline to detect specific regions in documents using YOLOv8 and extract structured data using EasyOCR.

## 🛠 Tech Stack
- **Detection:** Ultralytics YOLOv8
- **OCR:** EasyOCR
- **Processing:** OpenCV, Python, Pandas

## 📁 Folder Structure
- `src/`: Core logic and modular Python scripts.
- `models/`: Trained YOLOv8 models (`best.pt`).
- `data/`: Sample images for testing.

## 🚀 How to Run
1. Install dependencies: `pip install -r requirements.txt`
2. Run: `python main.py`