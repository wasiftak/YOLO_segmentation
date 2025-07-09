from ultralytics import YOLO

def main():
    # Load model
    model = YOLO("yolov8n-seg.pt")

    # Train
    model.train(
        data="dataset.yaml",
        epochs=50,
        imgsz=640,
        batch=4,
        project="runs",
        name="instrument_segmentation",
        save=True
    )

if __name__ == "__main__":
    main()
