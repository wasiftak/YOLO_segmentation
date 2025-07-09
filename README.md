# 🩺🔬 Cataract Surgery Instrument Segmentation with YOLOv8

## 💡 Introduction
This project focuses on segmenting surgical instruments in cataract surgery images using state-of-the-art deep learning techniques. The primary goal is to improve the detection and segmentation accuracy of fine surgical tools to support research in computer-assisted surgery.

## 📄 Dataset
- **Name**: InSegCat dataset 1 v1.0 (Publication version)
- **Link**: [InSegCat Dataset](https://ftp.itec.aau.at/datasets/ovid/InSegCat/index.html)
- **Images**: 263 annotated surgical images

## ⚙️ What was done
### ✅ Annotation conversion
- Converted InSegCat dataset COCO-style `.json` annotations to YOLO format using scripts in `convert_json_to_yolo/`.
- Verified all files using `check_files/` utilities to ensure no missing or mismatched images and annotations.

### ✅ Training
- Used **YOLOv8-seg** model for instance segmentation.
- Base weights (`yolov8n.pt`) pretrained on COCO dataset were fine-tuned.
- Training executed via `train_yolo.py`, with dataset configuration defined in `dataset.yaml`.

### ✅ Results
- **mAP50**: ~93%
- **mAP50-95**: ~77%
- Optimal performance observed around **30 epochs**, after which signs of overfitting appeared.

## 🚀 Usage
1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
2. Convert JSON annotations (if needed).
3. Verify dataset integrity using `check_files`.
4. Run training:
   ```
   python train_yolo.py
   ```
5. Check results in the `runs/` directory.

