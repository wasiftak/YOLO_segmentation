# 🎯 YOLO Segmentation (YOLO_segmentation)

## 💡 Introduction
This repository provides a robust pipeline for training and evaluating YOLOv8 segmentation models on custom datasets. The framework can be adapted for various instance segmentation tasks across different domains.

## ⚙️ Features
### ✅ Annotation Conversion
- Convert COCO-style `.json` annotations to YOLO format using scripts in `convert_json_to_yolo/`
- Support for various dataset formats and structures
- Verification utilities in `check_files/` to ensure dataset integrity

### ✅ Training Pipeline
- **YOLOv8-seg** implementation for instance segmentation
- Pretrained weights support (COCO dataset)
- Customizable training configuration via `dataset.yaml`
- Comprehensive training metrics and visualization

### ✅ Performance
- Achieves **mAP50**: ~93% and **mAP50-95**: ~77% on surgical instrument dataset
- Early stopping integration to prevent overfitting
- Optimal performance typically around 30 epochs

## 🚀 Quick Start
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Prepare your dataset:
   ```bash
   # Convert annotations if needed
   python convert_json_to_yolo/convert_annotations.py
   
   # Verify dataset integrity
   python check_files/verify_dataset.py
   ```

3. Configure your dataset in `dataset.yaml`

4. Start training:
   ```bash
   python train_yolo.py
   ```

5. Evaluate results in the `runs/` directory

## 📊 Example Results
The framework has been successfully tested on the **InSegCat dataset** (263 annotated surgical images) achieving excellent segmentation performance for surgical instruments. The same pipeline can be adapted to your specific segmentation tasks.

## 🔧 Customization
- Modify `dataset.yaml` for your specific classes and paths
- Adjust hyperparameters in `train_yolo.py` for optimal performance
- Extend functionality with custom preprocessing and postprocessing modules

