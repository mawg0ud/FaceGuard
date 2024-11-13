import os
import cv2
from typing import Tuple

# Configuration
DATA_DIR = "../datasets/FaceForensics++"
PROCESSED_DIR = "../datasets/FaceForensics++_processed"
IMAGE_SIZE = 256  # Target image size for preprocessing

def preprocess_image(image_path: str, output_size: Tuple[int, int]) -> None:
    """Resize and save a single image."""
    image = cv2.imread(image_path)
    if image is None:
        print(f"Warning: Could not read image {image_path}")
        return
    image = cv2.resize(image, output_size)
    output_path = os.path.join(PROCESSED_DIR, os.path.relpath(image_path, DATA_DIR))
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    cv2.imwrite(output_path, image)

def preprocess_data(data_dir: str, output_size: Tuple[int, int]) -> None:
    """Apply preprocessing to all images in a directory."""
    for root, _, files in os.walk(data_dir):
        for file in files:
            if file.endswith(('.jpg', '.png')):
                image_path = os.path.join(root, file)
                preprocess_image(image_path, output_size)
    print(f"All images processed and saved to {PROCESSED_DIR}")

def main():
    os.makedirs(PROCESSED_DIR, exist_ok=True)
    preprocess_data(DATA_DIR, (IMAGE_SIZE, IMAGE_SIZE))

if __name__ == "__main__":
    main()
