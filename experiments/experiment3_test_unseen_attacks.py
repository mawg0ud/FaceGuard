import torch
from torch.utils.data import DataLoader
from models.auto_encoder import YAutoEncoder
from data_preprocessing.data_loader import FaceForensicsDataset
from data_preprocessing.augmentation import get_test_augmentations
from utils.config_loader import load_config
from utils.logger import setup_logger
from models.metrics import compute_accuracy, compute_eer
from utils.save_load_model import load_model

def evaluate_unseen_attacks():
    config = load_config('configs/experiment3_unseen_attacks.yaml')
    logger = setup_logger('logs/experiment3_unseen_attacks.log')

    # Load unseen attack dataset
    test_augmentations = get_test_augmentations(config['image_size'])
    test_dataset = FaceForensicsDataset(config['data_dir'], phase='test', augmentations=test_augmentations)
    test_loader = DataLoader(test_dataset, batch_size=config['batch_size'], shuffle=False, num_workers=config['num_workers'])

    # Load pretrained model
    model = YAutoEncoder().to(config['device'])
    model = load_model(model, config['pretrained_model_path'])
    model.eval()

    logger.info("Evaluating model on unseen attack dataset...")
    total_accuracy, total_eer = 0, 0
    with torch.no_grad():
        for images, masks in test_loader:
            images, masks = images.to(config['device']), masks.to(config['device'])
            seg_output, _ = model(images)
            total_accuracy += compute_accuracy(seg_output, masks)
            total_eer += compute_eer(seg_output, masks)
    
    avg_accuracy = total_accuracy / len(test_loader)
    avg_eer = total_eer / len(test_loader)
    logger.info(f"Unseen Attack Evaluation - Accuracy: {avg_accuracy}, EER: {avg_eer}")

if __name__ == "__main__":
    evaluate_unseen_attacks()
