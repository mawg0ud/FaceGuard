import os
import shutil
from typing import Tuple

def create_data_split(data_dir: str, split_ratios: Tuple[float, float, float] = (0.7, 0.15, 0.15)):
    images = os.listdir(os.path.join(data_dir, 'images'))
    masks = os.listdir(os.path.join(data_dir, 'masks'))
    assert len(images) == len(masks), "Images and masks count mismatch."
    
    # Code to shuffle and split data into train, val, and test sets based on split_ratios
    # For demonstration, code specifics are omitted
