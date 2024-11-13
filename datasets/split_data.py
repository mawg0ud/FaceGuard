import os
import random
import shutil
from typing import Tuple, List

# Configuration
DATA_DIR = "../datasets/FaceForensics++_processed"
OUTPUT_DIR = "../datasets/FaceForensics++_split"
SPLIT_RATIOS = (0.7, 0.15, 0.15)  # Train, validation, test split ratios
SEED = 42

def get_file_list(data_dir: str, extensions: Tuple[str] = ('.jpg', '.png')) -> List[str]:
    """Get a list of all files in the data directory with the given extensions."""
    file_list = []
    for root, _, files in os.walk(data_dir):
        for file in files:
            if file.endswith(extensions):
                file_list.append(os.path.join(root, file))
    return file_list

def split_data(file_list: List[str], ratios: Tuple[float, float, float], seed: int) -> Tuple[List[str], List[str], List[str]]:
    """Split the data into train, validation, and test sets."""
    random.seed(seed)
    random.shuffle(file_list)
    train_size = int(ratios[0] * len(file_list))
    val_size = int(ratios[1] * len(file_list))
    train_files = file_list[:train_size]
    val_files = file_list[train_size:train_size + val_size]
    test_files = file_list[train_size + val_size:]
    return train_files, val_files, test_files

def organize_files(file_list: List[str], output_dir: str, split: str) -> None:
    """Copy files to the corresponding split directory."""
    split_dir = os.path.join(output_dir, split)
    os.makedirs(split_dir, exist_ok=True)
    for file_path in file_list:
        dest_path = os.path.join(split_dir, os.path.relpath(file_path, DATA_DIR))
        os.makedirs(os.path.dirname(dest_path), exist_ok=True)
        shutil.copy2(file_path, dest_path)
    print(f"Copied {len(file_list)} files to {split} set.")

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    file_list = get_file_list(DATA_DIR)
    train_files, val_files, test_files = split_data(file_list, SPLIT_RATIOS, SEED)

    # Organize files into train, val, and test directories
    organize_files(train_files, OUTPUT_DIR, "train")
    organize_files(val_files, OUTPUT_DIR, "val")
    organize_files(test_files, OUTPUT_DIR, "test")
    print("Data successfully split into train, validation, and test sets.")

if __name__ == "__main__":
    main()
