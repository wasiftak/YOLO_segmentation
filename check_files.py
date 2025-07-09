import os

# Update your paths below 👇
train_img_dir = "dataset_yolo/images/train"
val_img_dir = "dataset_yolo/images/val"
json_dir = "dataset_yolo/Instrument_detection/annotations_instrument"

train_imgs = set(os.listdir(train_img_dir))
val_imgs = set(os.listdir(val_img_dir))
json_files = os.listdir(json_dir)

# Remove .json extension from JSON filenames to get base
json_bases = set(f.replace(".json", "") for f in json_files)

# Find images with JSON
common_train = train_imgs & json_bases
common_val = val_imgs & json_bases

print(f"Train images: {len(train_imgs)}")
print(f"Train images with JSON: {len(common_train)}")

print(f"Val images: {len(val_imgs)}")
print(f"Val images with JSON: {len(common_val)}")

missing_train = train_imgs - json_bases
missing_val = val_imgs - json_bases

print("\nMissing JSON for these train images:", list(missing_train)[:10])
print("Missing JSON for these val images:", list(missing_val)[:10])
