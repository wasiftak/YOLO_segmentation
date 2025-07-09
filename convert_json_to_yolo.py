import os
import json
from PIL import Image

# Paths (update if needed)
json_dir = "dataset_yolo/Instrument_detection/annotations_instrument"
train_img_dir = "dataset_yolo/images/train"
val_img_dir = "dataset_yolo/images/val"
train_lbl_dir = "dataset_yolo/labels/train"
val_lbl_dir = "dataset_yolo/labels/val"

# Helper: convert polygon points
def convert_polygons(points, img_w, img_h):
    poly_flat = []
    for x, y in points:
        poly_flat.append(x / img_w)
        poly_flat.append(y / img_h)
    return poly_flat

# Process all JSON files
json_files = os.listdir(json_dir)
for json_file in json_files:
    if not json_file.endswith(".json"):
        continue

    base_name = json_file.replace(".json", "")
    img_path = None
    lbl_path = None

    if os.path.exists(os.path.join(train_img_dir, base_name)):
        img_path = os.path.join(train_img_dir, base_name)
        lbl_path = os.path.join(train_lbl_dir, os.path.splitext(base_name)[0] + ".txt")
    elif os.path.exists(os.path.join(val_img_dir, base_name)):
        img_path = os.path.join(val_img_dir, base_name)
        lbl_path = os.path.join(val_lbl_dir, os.path.splitext(base_name)[0] + ".txt")
    else:
        print(f"⚠️ Image not found for: {base_name}")
        continue

    img = Image.open(img_path)
    img_w, img_h = img.size

    with open(os.path.join(json_dir, json_file), "r") as f:
        data = json.load(f)

    objects = data.get("objects", [])
    lines = []

    for obj in objects:
        if obj["geometryType"] != "polygon":
            continue
        points = obj["points"]["exterior"]
        if not points:
            continue
        poly_yolo = convert_polygons(points, img_w, img_h)
        line = "0 " + " ".join([f"{x:.6f}" for x in poly_yolo])
        lines.append(line)

    if lines:
        with open(lbl_path, "w") as f:
            f.write("\n".join(lines))
        print(f"✅ Label written: {lbl_path}")
    else:
        print(f"⚠️ No polygon found in: {json_file}, no label file created.")

print("🎉 All label files are generated!")
