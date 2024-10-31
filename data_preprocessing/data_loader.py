import os
from typing import Tuple, List, Optional
import cv2
import torch
from torch.utils.data import Dataset, DataLoader
import albumentations as A
from albumentations.pytorch import ToTensorV2

class FaceForensicsDataset(Dataset):
    """Dataset class for loading and preprocessing images and masks for FaceForensics++."""

    def __init__(self, data_dir: str, phase: str = 'train', image_size: int = 256, augmentations: Optional[A.Compose] = None):
        assert phase in ['train', 'val', 'test'], "Phase must be 'train', 'val', or 'test'."
        self.data_dir = data_dir
        self.phase = phase
        self.image_size = image_size
        self.augmentations = augmentations
        self.image_paths, self.mask_paths = self._load_image_mask_paths()

    def __len__(self) -> int:
        return len(self.image_paths)

    def __getitem__(self, idx: int) -> Tuple[torch.Tensor, torch.Tensor]:
        image = cv2.imread(self.image_paths[idx])
        mask = cv2.imread(self.mask_paths[idx], cv2.IMREAD_GRAYSCALE)
        image, mask = cv2.resize(image, (self.image_size, self.image_size)), cv2.resize(mask, (self.image_size, self.image_size))

        if self.augmentations:
            augmented = self.augmentations(image=image, mask=mask)
            image, mask = augmented['image'], augmented['mask']
        else:
            image, mask = ToTensorV2()(image), torch.from_numpy(mask).unsqueeze(0).float()

        return image, mask

    def _load_image_mask_paths(self) -> Tuple[List[str], List[str]]:
        image_dir = os.path.join(self.data_dir, self.phase, 'images')
        mask_dir = os.path.join(self.data_dir, self.phase, 'masks')
        image_paths = sorted([os.path.join(image_dir, f) for f in os.listdir(image_dir) if f.endswith(('.jpg', '.png'))])
        mask_paths = sorted([os.path.join(mask_dir, f) for f in os.listdir(mask_dir) if f.endswith(('.jpg', '.png'))])
        assert len(image_paths) == len(mask_paths), "Mismatch between images and masks!"
        return image_paths, mask_paths
